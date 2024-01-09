from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_a
from constructs import Construct


class CdkLambdaFlaskStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda_a.PythonFunction(
            scope=self,
            id='LambdaFunction',
            entry='./src/',
            runtime=_lambda.Runtime.PYTHON_3_11,
            index='main.py',
            handler='handle',
            layers=[_lambda_a.PythonLayerVersion(self, "Request", entry="./cdk_lambda_flask/layer/")],
        )
