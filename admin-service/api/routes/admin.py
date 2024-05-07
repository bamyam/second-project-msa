from math import ceil
from typing import List

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse

from api.schemas.employee import Employee
from api.schemas.location import Location
from api.services.admin import AdminService
from api.services.mail import MailService

admin_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@admin_router.get('/{cpg}', response_class=HTMLResponse)
def admin(req: Request, cpg: int):
    stpg = int((cpg - 1) / 15) * 15 + 1
    info, cnt = AdminService.select_visit(cpg)
    allpage = ceil(cnt / 15)
    print(stpg)
    return templates.TemplateResponse('admin/admin.html', {'request': req,
        'info': info, 'cpg': cpg, 'stpg': stpg, 'allpage': allpage, 'baseurl': '/admin/'})


@admin_router.post('/accept')
def accept(data: dict):
    number = data['number']

    result = AdminService.accept_visit(number)

    res_url = '/error'
    if result.rowcount > 0:
        res_url = '/admin/1'
        visitor_name, visitor_email, time = MailService.find_data(number)
        MailService.mail_accepted(visitor_name, visitor_email, time)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)

@admin_router.post('/reject')
def reject(data: dict):
    number = data['number']
    reason = data['reason']

    result = AdminService.reject_visit(number)

    res_url = '/error'
    if result.rowcount > 0:
        res_url = '/admin/1'
        visitor_name, visitor_email, time = MailService.find_data(number)
        MailService.mail_regected(visitor_name, visitor_email, time, reason)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)

