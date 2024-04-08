import os 
import logging
from datetime import datetime

# Creating log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating directory for logs if it doesn't exist
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

# Setting log file path

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)


# Configuring basic logging settings
logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)