from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from api.schemas.employee import Employee
from api.schemas.location import Location
from api.schemas.visitors import Visitors
from api.services.employee import EmployeeService
from api.services.location import LocationService
from api.services.visitors import VisitorsService
import requests

apply_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')




@apply_router.get("/employees", response_model=list[Employee])
async def list_employees(req: Request):
    emp_list = EmployeeService.get_all_employees()
    return [Employee.from_orm(emp) for emp in emp_list]

@apply_router.get("/locations", response_model=list[Location])
async def list_locations(req: Request):
    location_list = LocationService.get_all_location()
    return [Location.from_orm(loc) for loc in location_list]



@apply_router.post('/applyok')
def applyok(vmdto: Visitors):
    print(vmdto)
    result = VisitorsService.insert_visitor(vmdto)
    return result.rowcount


@apply_router.get('/applyok', response_class=HTMLResponse)
def applycheck(req: Request):
    return templates.TemplateResponse('apply/applyok.html', {'request': req})




