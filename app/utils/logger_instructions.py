import logging
from rich.logging import RichHandler
import os

DISABLE_LOGGING = False  # Set this to True to disable logging

logger = logging.getLogger(__name__)

if not DISABLE_LOGGING:
    # Define log file paths
    if os.path.exists('tmp'):
        debug_file_path = "tmp/debug.log"
        info_file_path = "tmp/info.log"
    else:
        debug_file_path = "/tmp/debug.log"
        info_file_path = "/tmp/info.log"

    # Create handlers
    shell_handler = RichHandler()
    file_handler_debug = logging.FileHandler(debug_file_path)
    file_handler_info = logging.FileHandler(info_file_path)

    # Set logging levels
    logger.setLevel(logging.DEBUG)
    shell_handler.setLevel(logging.INFO)  # Changed to DEBUG so that all messages appear on the console
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_info.setLevel(logging.INFO)

    # Define formatters
    shell_fmt = '%(message)s'
    file_fmt = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d]: %(message)s'
    
    shell_formatter = logging.Formatter(shell_fmt)
    file_formatter = logging.Formatter(file_fmt)

    # Set the formatters to the handlers
    shell_handler.setFormatter(shell_formatter)
    file_handler_debug.setFormatter(file_formatter)
    file_handler_info.setFormatter(file_formatter)

    # Add the handlers to the logger
    logger.addHandler(shell_handler)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_info)
else:
    # Disable logging completely
    logging.disable(logging.CRITICAL + 1)
