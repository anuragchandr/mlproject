import sys
from .logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is None:
        return f"Error message [{error}]"

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{}] line number [{}] error message [{}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error occurred.")
        raise CustomException(e, sys) from e