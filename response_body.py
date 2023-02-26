class ResponseBody:

    def __init__(self, status: str, code: int, data: list, message: str):
        self.status = status
        self.code = code
        self.data = data
        self.message = message

    @staticmethod
    def ok(data: list = []):
        return ResponseBody('ok', 200, data, 'Success!')

    @staticmethod
    def error(code: int = 500, message: str = 'Internal server error.'):
        return ResponseBody(status='error', code=code, data=[], message=message)

    @staticmethod
    def error_404():
        return ResponseBody(status='error', code=404, data=[], message="The record cannot be queried.")
