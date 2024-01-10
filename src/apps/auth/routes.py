from flask import Blueprint, request

from apps.auth.schemas.get_user_schema import GetUserRequest
from apps.auth.schemas.login_schema import LoginRequest
from apps.auth.services.get_user_service import get_user_service
from apps.auth.services.login_service import login_service
from core.decorator import response_jsonify
from core.utils.parse_request import parse_request

auth_route = Blueprint('auth', __name__)


@auth_route.post('/login')  # type: ignore
@response_jsonify(api_code=1)
def login():
    request_data = LoginRequest(**parse_request(request))
    return login_service(request_data)


@auth_route.post('/user')  # type: ignore
@response_jsonify(api_code=2)
def get_user():
    request_data = GetUserRequest(**parse_request(request))
    return get_user_service(request_data)
