import botocore.exceptions

from apps.auth.constants.errors.login_error_constant import ERROR_CODE
from apps.auth.helpers.cognito_helper import CognitoHelper
from apps.auth.schemas.login_schema import LoginRequest, LoginResponse
from core.api_exception import BadRequestException, UnauthorizedException
from core.logger import logger


def login_service(request: LoginRequest):
    cognito_helper = CognitoHelper()
    response = __login_by_email_password(cognito_helper, request.email, request.password)

    if response.get('ChallengeName', '') == 'NEW_PASSWORD_REQUIRED':
        if request.new_password is None:
            raise BadRequestException(
                message='Request new password for first login',
                error_code=1,
                error_fields={'new_password': 'Field required'}
            )
        cognito_helper.admin_respond_to_auth_challenge(response['Session'], request.email, request.new_password)
        response = __login_by_email_password(cognito_helper, request.email, request.new_password)

    access_token = response['AuthenticationResult']['AccessToken']
    return LoginResponse(access_token=access_token)


def __login_by_email_password(cognito_helper: CognitoHelper, email: str, password: str):
    try:
        return cognito_helper.admin_initiate_auth(username=email, password=password)
    except botocore.exceptions.ClientError as err:
        logger.error(err.response)
        message = err.response['Error']['Message']
        raise UnauthorizedException(message=message, error_code=ERROR_CODE.get(message, 10)) from err
