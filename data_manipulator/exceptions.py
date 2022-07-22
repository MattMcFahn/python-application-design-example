"""Package exceptions"""


class FileNotFound(Exception):
    """Input file not found"""

    log_code = "MANIPULATOR-E000"


class TypeNotSupported(Exception):
    """Type for specified as input/output format isn't supported"""

    log_code = "MANIPULATOR-E001"


class DirectoryDoesntExist(Exception):
    """Specified directory doesn't exist"""

    log_code = "MANIPULATOR-E002"
