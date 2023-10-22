import boto3

# Create an Elastic Beanstalk client
client = boto3.client('elasticbeanstalk')

# Create an application
response = client.create_application(
  applicationName='my-app',
  description='My first Elastic Beanstalk application',
)

# Print the application name
print(response['Application']['ApplicationName'])
