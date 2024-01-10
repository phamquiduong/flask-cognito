import aws_cdk as cdk
from stack.flask_stack import FlaskStack

CONSTRUCT_ID = 'Flask'

# Create stack app
app = cdk.App()

# Register stack with app
FlaskStack(app, CONSTRUCT_ID)

# Synth the stack app
app.synth()
