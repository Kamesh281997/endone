import sys

def get_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    err_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occurs on file name [{0}] in line number [{1}] having error message[{3}]".format(err_name,exc_tb.tb_lineno,str(error) 
    )
    return error_msg
    



class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message=get_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message