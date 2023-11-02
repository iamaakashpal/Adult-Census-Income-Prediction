import logging
import os
from datetime import datetime

LOG_FOLDER_NAME = "logs"

os.makedirs(LOG_FOLDER_NAME,exist_ok=True)

CURRENT_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

LOG_FILE_NAME = f'logs_{CURRENT_TIME}.log'

LOG_FILE_PATH = os.path.join(LOG_FOLDER_NAME,LOG_FILE_NAME)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    filemode = 'w',
    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO)