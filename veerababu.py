import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2', region_name='us-east-1')

# Create the instance
instances = ec2.create_instances(
    ImageId='ami-0c7217cdde317cfec',  # Replace with a valid AMI ID for your region
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-key-pair'             # Replace with your AWS key pair name
)

print(f"Created instance with ID: {instances[0].id}")

