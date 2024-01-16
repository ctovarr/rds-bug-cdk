## Reproduce the bug

Go to localstack.yaml and put your PRO token in the environment variable LOCALSTACK_AUTH_TOKEN, then

```bash
docker compose -f localstack.yaml up
```

You are gonna see this error

```bash
ds-bug  | RdsBugStack | 11:42:25 PM | CREATE_FAILED        | AWS::RDS::DBSubnetGroup                     | DBInstance/SubnetGroup/Default (DBInstanceSubnetGroupF597B45B) An error occurred (InvalidSubnetID.NotFound) when calling the CreateDBSubnetGroup operation: The subnet ID 'subnet-18fa7836' does not exist
rds-bug  | 
rds-bug  |  ❌  RdsBugStack failed: Error: The stack named RdsBugStack failed to deploy: CREATE_FAILED (An error occurred (InvalidSubnetID.NotFound) when calling the CreateDBSubnetGroup operation: The subnet ID 'subnet-18fa7836' does not exist)
rds-bug  |     at FullCloudFormationDeployment.monitorDeployment (/usr/local/lib/node_modules/aws-cdk/lib/index.js:421:10615)
rds-bug  |     at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
rds-bug  |     at async Object.deployStack2 [as deployStack] (/usr/local/lib/node_modules/aws-cdk/lib/index.js:424:181611)
rds-bug  |     at async /usr/local/lib/node_modules/aws-cdk/lib/index.js:424:164027
```
