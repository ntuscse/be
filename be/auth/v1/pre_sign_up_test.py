from be.auth.v1.pre_sign_up import lambda_handler


def test_pre_sign_up_valid_ntu_email():
    event_request = {
        'response': {
            'autoConfirmUser': True
        },
        'request': {
            'userAttributes': {
                'email': 'test@ntu.edu.sg'
            }
        }
    }

    event_response = lambda_handler(event_request, None)
    assert event_response['response']['autoConfirmUser'] == True

def test_pre_sign_up_invalid_ntu_email():
    event_request = {
        'response': {
            'autoConfirmUser': True
        },
        'request': {
            'userAttributes': {
                'email': 'test@not_valid.com'
            }
        }
    }

    event_response = lambda_handler(event_request, None)
    assert event_response['response']['autoConfirmUser'] == False
