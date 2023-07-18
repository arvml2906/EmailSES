import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
def send_email(sender_email, recipient_email, subject, message):
    # Configure SMTP settings
    smtp_host = 'email-smtp.us-east-1.amazonaws.com'  # Replace with your SES SMTP endpoint
    smtp_port = 587  # Use the appropriate SMTP port (e.g., 587 or 465)
    smtp_username = 'XXXXXXXXXXXXXXX'  # Replace with your SES SMTP username
    smtp_password = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your SES SMTP password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the email using SMTP
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/445226378433/MailMessage'  # Replace with your SQS queue URL

    # Process messages in the SQS queue
    #queue = sqs.Queue(queue_url)
    #messages = queue.receive_messages(MaxNumberOfMessages=10)

    for record in event['Records']:
        message_body = json.loads(record["body"])

        # Extract form details from the message body
        name = message_body.get('name')
        email = message_body.get('email')
        project = message_body.get('project')
        message_content = message_body.get('message')

        # Prepare email details
        sender_email = 'arvindrox.619@gmail.com'
        recipient_email = 'arvindrox.619@gmail.com'  # Use the submitted email as the recipient
        subject = f'New message from {email} regarding {project}'
        message1 = f'I am {name},\n\nYou have a new message regarding {project}:\n\n{message_content}'

        # Send the email using the send_email function
        send_email(sender_email, recipient_email, subject, message1)
        print({message1})
        # Delete the message from the SQS queue after processing
        #receipt_handle = message.receipt_handle
        #queue.delete_messages(Entries=[{'Id': message.message_id, 'ReceiptHandle': receipt_handle}])
        #message.delete()
    return {
        'statusCode': 200,
        'body': 'Messages processed successfully'
    }
