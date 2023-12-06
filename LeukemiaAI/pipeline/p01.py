"""
pipeline stage 01.
"""
from pathlib import Path
from LeukemiaAI.config import DataIngestionConfig
from LeukemiaAI.config import ConfigurationManager
from LeukemiaAI.components import DataIngestion
from LeukemiaAI import logger

STAGE_NAME = "Data Ingestion"


def run():
    """runs pipeline stage 01"""
    config_manager = ConfigurationManager(
        Path('config/config.yml'),
        Path('params.yml')
    )
    diconfig = config_manager.data_ingestion_configs()
    di = DataIngestion(diconfig)
    di.prepare_data()


if __name__ == "__main__":
    try:
        logger.info(f'started pipeline stage {STAGE_NAME}')
        run()
        logger.info(f'finished pipeline stage {STAGE_NAME}')

    except Exception as e:
        logger.exception(e)
        raise e
    