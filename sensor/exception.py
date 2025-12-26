import sys
import os

def error_message_detail(error, error_detail:sys):
    # Ask the system for the last error (returns 3 things, we want the 3rd)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract filename from the traceback object
    filename = exc_tb.tb_frame.f_code.co_filename
    
    # Create the detailed message string
    error_message = "Error occured in script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)
    )

    return error_message

class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # Allow Parent class to handle the basic message
        super().__init__(error_message)
        
        # Use our helper function to create the detailed message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # Print the detailed message when this error is raised
        return self.error_message




# import sys
# import os

# def error_message_detail(error, error_detaill:sys):
#     _,_,exc_tb = sys.error_detail.exc_info()
#     filename = exc_tb.tb_frame.f_code.co_filename

#     error_message = "Error occured in script or file name is [{0}] and at line number: [{1}] error message: [{2}]".format(

#     filename, exc_tb.tb_lineno, str(error)
#     )

#     return error_message

# class SensorException(Exception):

#     def __init__(self, error_message, error_detail: sys):

#         super().__init__(error_message)

#         self.error_message = error_message_detail(error_message, error_details=error_detail)

#     def __str__(self):
#         return super().error_message    