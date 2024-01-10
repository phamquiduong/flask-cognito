import os

from aws_cdk import Stack, aws_apigateway, aws_lambda
from constructs import Construct


class FlaskStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.construct_id = construct_id

        self.create_docker_lambda_function()
        self.create_api_gateway()

    def create_docker_lambda_function(self):
        # path_to_function_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src",)
        path_to_function_folder = os.path.dirname(os.path.dirname(__file__))

        self.docker_lambda_function = aws_lambda.DockerImageFunction(
            self,
            id=f"{self.construct_id}-Lambda",
            architecture=aws_lambda.Architecture.ARM_64,
            code=aws_lambda.DockerImageCode.from_image_asset(path_to_function_folder),
            environment={}
        )

    def create_api_gateway(self):
        self.lambda_rest_api = aws_apigateway.LambdaRestApi(
            self,
            id=f'{self.construct_id}-API-Gateway',
            handler=self.docker_lambda_function  # type: ignore
        )
