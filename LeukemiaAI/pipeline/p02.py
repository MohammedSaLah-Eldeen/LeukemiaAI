"""
pipeline stage 02.
"""
from pathlib import Path
from LeukemiaAI.config import FinetunedModelConfig
from LeukemiaAI.config import ConfigurationManager
from LeukemiaAI.components import FinetuendModel
from LeukemiaAI import logger

STAGE_NAME = "Loading Fine Tuned Model"


def run():
    """runs pipeline stage 02"""
    config_manager = ConfigurationManager(
        Path('config/config.yml'),
        Path('params.yml')
    )
    mconfig = config_manager.model_configs()
    ftm = FinetuendModel(mconfig)
    ftm.prepare_model()


if __name__ == "__main__":
    try:
        logger.info(f'started pipeline stage {STAGE_NAME}')
        run()
        logger.info(f'finished pipeline stage {STAGE_NAME}')

    except Exception as e:
        logger.exception(e)
        raise e