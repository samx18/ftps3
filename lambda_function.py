import boto3
import pysftp

def lambda_handler(event, context):
    # TODO implement
    # Get env variables

    hostname=process.env.HOST
    username=process.env.USER
    secret=process.env.SECRET

    # Handle host keys
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    
    # Make a secure connection to the site and download the file
    
    with pysftp.Connection(hostname, username=username, password=secret,cnopts=cnopts) as sftp:
            sftp.get('VendorWebSTG.csv')         # get a remote file
    
    
    # Upload the file to a S3 bucket
    data = open('VendorWebSTG.csv', 'rb')
    s3 = boto3.resource('s3')
    s3.Bucket('ctrbot').put_object(Key='VendorWebSTG.csv', Body=data)
    return "Upload sucessful"
    

