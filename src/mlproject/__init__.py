# Writ a logging to make our import easy, so it  records messages to a file and displays them on the console, providing a comprehensive view of application activity.

import logging
import sys
import os

# Define a format for the log messages
logging_str = '[%(asctime)s] : %(levelname)s : %(module)s :  %(message)s]'


# Set up the directory for storing log files
log_directory = 'logs'
logs_filepath = os.path.join(log_directory, 'running_logs.log')
os.makedirs(log_directory , exist_ok=True)

# Configure the basic logging settings
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(logs_filepath),# Saves log messages to a file named running_logs.log in the logs directory.
        logging.StreamHandler(sys.stdout)  # Displays log messages directly to the console (standard output).

    ]
)

# Create a logger object with the name 'mlProjectLogger'
logger = logging.getLogger('mlProjectLogger')