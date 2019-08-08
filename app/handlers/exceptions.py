

class BadRequest(Exception):
    code = 400
    description = 'Bad Request.'


class InternalServerError(Exception):
    code = 500
    description = 'Internal Server Error.'
