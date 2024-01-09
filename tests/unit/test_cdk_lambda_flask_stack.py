import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_flask.cdk_lambda_flask_stack import CdkLambdaFlaskStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_flask/cdk_lambda_flask_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaFlaskStack(app, "cdk-lambda-flask")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
