import os

import aws_cdk as cdk
from dotenv import load_dotenv
from stack.flask_stack import FlaskStack

if not load_dotenv():
    raise FileNotFoundError('Load environment variables failed')

CONSTRUCT_ID = os.getenv('CONSTRUCT_ID', 'Flask')

# Create stack app
app = cdk.App()

# Register stack with app
FlaskStack(app, CONSTRUCT_ID)

# Synth the stack app
app.synth()
