import os

from aws_cdk import Duration, Stack, aws_apigateway, aws_iam, aws_lambda
from constructs import Construct


class FlaskStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.construct_id = construct_id

        self.create_docker_lambda_function()
        self.add_role_policy_cognito()

        self.create_api_gateway()

    def create_docker_lambda_function(self):
        path_to_function_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src",)

        is_arm64 = os.getenv('IS_ARM64', 'true').lower() == 'true'
        architecure_config = {'architecture': aws_lambda.Architecture.ARM_64} if is_arm64 else {}

        self.docker_lambda_function = aws_lambda.DockerImageFunction(
            self,
            id=f"{self.construct_id}-Lambda",
            code=aws_lambda.DockerImageCode.from_image_asset(path_to_function_folder),
            timeout=Duration.seconds(30),
            **architecure_config
        )

    def add_role_policy_cognito(self):
        self.docker_lambda_function.add_to_role_policy(
            aws_iam.PolicyStatement(
                sid='VisualEditor0',
                effect=aws_iam.Effect.ALLOW,
                actions=[
                    "cognito-idp:AdminInitiateAuth",
                    "cognito-idp:GetUser",
                    "cognito-idp:AdminRespondToAuthChallenge"
                ],
                resources=['*']
            )
        )

    def create_api_gateway(self):
        self.lambda_rest_api = aws_apigateway.LambdaRestApi(
            self,
            id=f'{self.construct_id}-API-Gateway',
            handler=self.docker_lambda_function  # type: ignore
        )
