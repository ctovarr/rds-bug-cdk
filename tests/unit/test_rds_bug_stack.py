import aws_cdk as core
import aws_cdk.assertions as assertions

from rds_bug.rds_bug_stack import RdsBugStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rds_bug/rds_bug_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RdsBugStack(app, "rds-bug")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
