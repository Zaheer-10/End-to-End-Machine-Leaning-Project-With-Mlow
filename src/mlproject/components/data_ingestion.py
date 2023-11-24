import os
import urllib.request as request
import zipfile
from mlproject import logger
from mlproject.utils.common import get_size
import os
import time
from urllib.request import urlretrieve
from urllib.error import URLError
from mlproject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        retries = 5
        for i in range(retries):
            try:
                if not os.path.exists(self.config.local_data_file):
                    filename, headers = request.urlretrieve(
                        url = self.config.source_URL,
                        filename = self.config.local_data_file
                    )
                    logger.info(f"{filename} download! with following info: \n{headers}")
                else:
                    logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
                break
            except Exception as e:
                if i < retries - 1:
                    logger.warning(f"Retry {i + 1} due to connection issue: {e}")
                    time.sleep(5)  # Wait before retrying
                else:
                    raise  # If retries are exhausted, raise the exception
                


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
  