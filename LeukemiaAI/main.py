"""
Leukemia AI Full Pipeline.
"""
from LeukemiaAI.pipeline import p01
from LeukemiaAI import logger


# P01
STAGE_NAME = p01.STAGE_NAME
try:
    logger.info(f'started pipeline stage {STAGE_NAME}')
    p01.run()
    logger.info(f'finished pipeline stage {STAGE_NAME}')

except Exception as e:
    logger.exception(e)
    raise e

