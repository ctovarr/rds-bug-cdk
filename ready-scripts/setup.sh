#!/usr/bin/env bash

npm install -y -g aws-cdk-local aws-cdk

awslocal secretsmanager create-secret --name "db-secret" --secret-string '{"username":"dummyuser", "password": "dummypassword"}' --region us-east-1

# Execute CDK project
pip install -r /var/lib/localstack/rds_bug/requirements.txt
cd /var/lib/localstack/rds_bug && cdklocal bootstrap --app "python3 app.py" --region us-east-1
cd /var/lib/localstack/rds_bug && cdklocal deploy --app "python3 app.py" --require-approval never --region us-east-1
