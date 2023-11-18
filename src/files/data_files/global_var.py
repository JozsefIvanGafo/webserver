import os

# Get the path of the current directory (where __init__.py is located)
current_directory = os.path.dirname(__file__)

# Construct the complete paths for data and error_data directories
DATA_DIRECTORY_PATH = os.path.join(current_directory, 'data')
ERROR_DATA_DIRECTORY_PATH = os.path.join(current_directory, 'error_data')
STATISTICS_PATH = os.path.join(current_directory, 'statistics')