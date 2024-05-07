from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

svc_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@svc_router.get('/', response_class=HTMLResponse)
def check(req: Request):
    return templates.TemplateResponse('svc/svc.html', {'request': req})

