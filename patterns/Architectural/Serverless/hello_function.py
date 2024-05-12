import json

def lambda_handler(event, context):
    """ Пример функции AWS Lambda, возвращающей приветственное сообщение """
    body = {
        "message": "Hello from Lambda!",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Content-Type': 'application/json',
        },
    }
    return response
