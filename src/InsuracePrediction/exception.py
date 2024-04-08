import sys
from src.InsuracePrediction.logger import logging

# Custom exception class
class customexception(Exception):
    def __init__(self,error_message,error_details):
        self.error_message = error_message
        self.error_details = error_details

        #Extracting line number and file name if avialable

        _,_,exc_tb = self.error_details.exc_info()
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None
    
    def __str__(self):
        # String representation of the custom exception
        logging.info("Error occurred in Python script name [{0}] line number [{1}] ".format(self.file_name,
        self.lineno))
        return "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))
        