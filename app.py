import aws_cdk as cdk

from cdk_lambda_flask.cdk_lambda_flask_stack import CdkLambdaFlaskStack

app = cdk.App()
CdkLambdaFlaskStack(app, 'CdkLambdaFlask')

app.synth()
