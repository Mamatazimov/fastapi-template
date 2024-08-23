"""Routes for the home screen and templates."""

from typing import Union

from fastapi import APIRouter, Header, Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from app.config.helpers import get_api_version, get_project_root
from app.config.settings import get_settings

router = APIRouter()

# template_folder = get_project_root() / "app" / "templates"
# templates = Jinja2Templates(directory=template_folder)



@router.get("/", include_in_schema=False, response_model=None)
def root_path(request: Request):
    return {"message": "Hello World!"}
