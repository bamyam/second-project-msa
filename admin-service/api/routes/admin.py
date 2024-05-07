from math import ceil
from typing import List

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse, JSONResponse

from api.schemas.employee import Employee
from api.schemas.location import Location
from api.services.admin import AdminService
from api.services.mail import MailService

from api.schemas.admin import Admin
from fastapi import HTTPException
import logging

admin_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@admin_router.get('/{cpg}', response_model=list[Admin])
async def admin(req: Request, cpg: int):
    stpg = int((cpg - 1) / 15) * 15 + 1
    info, cnt = AdminService.select_visit(cpg)
    allpage = ceil(cnt / 15)

    admin_list = []
    for admin in info:
        admin_dict = admin._asdict()
        admin_dict['stpg'] = stpg
        admin_dict['allpage'] = allpage
        admin_dict['cpg'] = cpg
        admin_list.append(admin_dict)

    return admin_list


@admin_router.post('/accept')
def accept(data: dict):
    try:
        number = data['number']

        result = AdminService.accept_visit(number)

        res_url = '/error'
        if result.rowcount > 0:
            res_url = '/admin/1'
            visitor_name, visitor_email, time = MailService.find_data(number)
            MailService.mail_accepted(visitor_name, visitor_email, time)

        return JSONResponse(content={"res_url": res_url}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"An error occurred while sending rejection email: {str(e)}")
        raise HTTPException(status_code=500, detail="승인 이메일을 보내는 중 오류가 발생했습니다.")

@admin_router.post('/reject')
def reject(data: dict):

    try:
        number = data['number']
        reason = data['reason']

        result = AdminService.reject_visit(number)

        res_url = '/error'
        if result.rowcount > 0:
            res_url = '/admin/1'
            visitor_name, visitor_email, time = MailService.find_data(number)
            MailService.mail_regected(visitor_name, visitor_email, time, reason)

        return JSONResponse(content={"res_url": res_url}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"An error occurred while sending rejection email: {str(e)}")
        raise HTTPException(status_code=500, detail="거절 이메일을 보내는 중 오류가 발생했습니다.")

