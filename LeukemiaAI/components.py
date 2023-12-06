"""
defines LeukemiaAI components 
"""
import os
import sys
import requests
import reusables
import urllib.request as request
import subprocess
import kaggle

from pathlib import Path
from config import DataIngestionConfig
from typing import Any

from LeukemiaAI import logger


class DataIngestion:
    """ingest data."""

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def prepare_data(self):
        """
        downloads the zipfile and extracts.
        as in the configs.
        """

        if not os.path.exists(self.config.unzip_dir):

            if self.config.kaggle and not os.path.exists(self.config.local_data_file):
                os.chdir('data')
                
                subprocess.run(f"kaggle datasets download -d {self.config.source_URL}", shell=True)
                os.chdir('..')
                logger.info(f"downloaded data from Kaggle")

            elif not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"downloaded data.")
            
            reusables.extract(
                self.config.local_data_file,
                self.config.unzip_dir
            ) 
            logger.info(f"Extracted data")

        else:
            logger.info(f"data already exists.")