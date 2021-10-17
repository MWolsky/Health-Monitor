class Error(Exception):
    """Base class for other errors"""

class TrainingTypeError(Error):
    """Raised when unknown training type is passed in"""
    def __init__(self, training_type: str, message='Unknown training type. Training type passed in is not in configuration.') -> None:
        super().__init__(message)
        self.message = message


class PrimaryKeyNotValid(Error):
    """Raised when not valid primary key is passed in"""
    def __init__(self, primary_key: str, message="""Primary Key field provided is not valid. Indicate which field is a primary key in its tuple by 
    'primary key' keyword""") -> None:
        super().__init__(message)
        self.message = message