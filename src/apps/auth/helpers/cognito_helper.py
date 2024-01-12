import boto3

from core.config import Config


class CognitoHelper:
    AWS_REGION = Config.AWS_REGION
    USER_POOL_ID = Config.USER_POOL_ID
    CLIENT_ID = Config.CLIENT_ID

    def __init__(self) -> None:
        self.client = boto3.client('cognito-idp', region_name=self.AWS_REGION)

    def admin_initiate_auth(self, username: str, password: str):
        return self.client.admin_initiate_auth(
            UserPoolId=self.USER_POOL_ID,
            ClientId=self.CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
            }
        )

    def get_user(self, access_token: str):
        return self.client.get_user(AccessToken=access_token)

    def admin_respond_to_auth_challenge(self, session: str, username: str, new_password: str):
        return self.client.admin_respond_to_auth_challenge(
            UserPoolId=self.USER_POOL_ID,
            ClientId=self.CLIENT_ID,
            Session=session,
            ChallengeName="NEW_PASSWORD_REQUIRED",
            ChallengeResponses={
                "USERNAME": username,
                "NEW_PASSWORD": new_password,
            })
