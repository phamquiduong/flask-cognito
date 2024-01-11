# Flask with AWS Cognito
> * Flask with AWS Cognito
> * Build with docker-compose
> * Deploy by AWS CDK

<br>

# Development
Langage | Framework | User Management | Build | Deploy
--- | ---| --- | --- | --- |
[Python 3.11](https://peps.python.org/pep-0664/) | [Flask 3.0.x](https://flask.palletsprojects.com/en/3.0.x/) | [AWS Cognito](https://aws.amazon.com/pm/cognito/) | [Docker compose](https://docs.docker.com/compose/) | [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

<br>

# Installation
## Project
> * Change directory to src folder
>   ```bash
>   cd src/
>   ```
> * Copy and config project environment variables
>   ```bash
>   cp .env.example .env
>   ```
> * Install Python package
>   ```bash
>   pip install -r requirements.txt
>   ```


## Build with docker compose
> * Change directory to docker folder
>   ```bash
>   cd docker/
>   ```
> * Copy and config docker compose environment variables
>   ```bash
>   cp .env.example .env
>   ```

#### Docker compose command
> * Create a network
>   ```bash
>   docker network create flask_network
>   ```
> * Build or rebuild services
>   ```bash
>   docker-compose build
>   ```
> * Create and start containers
>   ```bash
>   docker-compose up
>   ```
>   * `-d` : (Detached mode) to run containers in the background
>   * `--build` : Build images before starting containers.
> * Stop services
>   ```bash
>   docker-compose stop
>   ```
> * Stop and remove containers, networks
>   ```bash
>   docker-compose down
>   ```


## Deploy with CDK
> * Change directory to CDK folder
>   ```bash
>   cd cdk/
>   ```
> * Copy and config CDK environment variables
>   ```bash
>   cp .env.example .env
>   ```
>   * Change `IS_ARM64=true` if you use AppleM1

#### CDK command
> * List all stacks in the app
>   ```
>   cdk ls
>   ```
> * Emits the synthesized CloudFormation template
>   ```
>   cdk synth
>   ```
> * Process of provisioning resources for the AWS CDK
>   ```
>   cdk bootstrap
>   ```
> * Deploy this stack to your default AWS account region
>   ```
>   cdk deploy
>   ```
> * Compare deployed stack with current state
>   ```
>   cdk diff
>   ```
> * Open CDK documentation
>   ```
>   cdk docs
>   ```
