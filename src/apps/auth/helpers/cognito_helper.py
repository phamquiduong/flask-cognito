import boto3

from core.config import config


class CognitoHelper:
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str,
                 user_pool_id: str, client_id: str) -> None:
        self.user_pool_id = user_pool_id
        self.client_id = client_id
        self.client = boto3.client('cognito-idp',
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key,
                                   region_name=region_name)

    def admin_initiate_auth(self, username: str, password: str):
        return self.client.admin_initiate_auth(
            UserPoolId=self.user_pool_id,
            ClientId=self.client_id,
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
            UserPoolId=self.user_pool_id,
            ClientId=self.client_id,
            Session=session,
            ChallengeName="NEW_PASSWORD_REQUIRED",
            ChallengeResponses={
                "USERNAME": username,
                "NEW_PASSWORD": new_password,
            })


cognito_helper = CognitoHelper(aws_access_key_id=config.get('USER_POOL_ID'),
                               aws_secret_access_key=config.get('CLIENT_ID'),
                               region_name=config.get('AWS_ACCESS_KEY_ID'),
                               user_pool_id=config.get('AWS_SECRET_ACCESS_KEY'),
                               client_id=config.get('AWS_REGION'))
