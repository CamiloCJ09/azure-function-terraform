import os
def lambda_example(event, context):
    return "{} from Lambda!".format(os.environ['greeting'])