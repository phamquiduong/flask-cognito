import botocore.exceptions

from apps.auth.helpers.cognito_helper import CognitoHelper
from apps.auth.schemas.get_user_schema import GetUserRequest, GetUserResponse
from core.api_exception import UnauthorizedException
from core.logger import logger


def get_user_service(request: GetUserRequest):
    try:
        response = CognitoHelper().get_user(access_token=request.access_token)
    except botocore.exceptions.ClientError as err:
        logger.error(err.response)
        raise UnauthorizedException(message=err.response['Error']['Message'], error_code=1) from err

    user_attributes = {user_attr['Name']: user_attr['Value'] for user_attr in response['UserAttributes']}

    return GetUserResponse(**user_attributes)
