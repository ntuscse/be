def lambda_handler(event, context):
    # It sets the user pool autoConfirmUser flag after validating the email domain
    event['response']['autoConfirmUser'] = False

    # Split the email address so we can compare domains
    email: str = event['request']['userAttributes']['email']

    # Check if user is from a valid domain
    if email.endswith('ntu.edu.sg'):
        event['response']['autoConfirmUser'] = True

    return event