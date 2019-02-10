import boto3
# Enter the region your instances are in. 
# Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'ap-southeast-1'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-XXXXXXXX', 'i-XXXXXXXX']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)
