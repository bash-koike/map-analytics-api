import functools
import json
import traceback

from handlers import exceptions


def func_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as error:
            print(traceback.format_exc())
            res = error_hander(error)
        print(res)
        return res
    return wrapper


def error_hander(error):

    # Get context of body
    if hasattr(error, 'code'):
        code = error.code
    else:
        code = exceptions.InternalServerError.code

    if hasattr(error, 'description'):
        description = error.description
    else:
        description = exceptions.InternalServerError.description

    # Make response
    body = {
        'status': 'NG',
        'error': {
            'code': code,
            'description': description
        }
    }
    body = json.dumps(body, ensure_ascii=False)
    res = {
        'isBase64Encoded': True,
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': body
    }
    return res
