def lambda_handler(event, context):
    print(f'DEBUG: Lambda Event {event}')
    # Split the email address so we can compare domains
    email: str = event['request']['userAttributes']['email']

    # Check if user is from a valid domain
    if email.endswith('ntu.edu.sg'):
        return event

    raise Exception('Invalid domain name')