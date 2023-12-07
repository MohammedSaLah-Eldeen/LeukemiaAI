"""
Leukemia AI Full Pipeline.
"""
from LeukemiaAI.pipeline import (
    p01,
    p02
)
from LeukemiaAI import logger


def step(pipeline_stage):
    """steps into the pipeline."""
    STAGE_NAME = pipeline_stage.STAGE_NAME
    try:
        logger.info(f'started pipeline stage {STAGE_NAME}')
        pipeline_stage.run()
        logger.info(f'finished pipeline stage {STAGE_NAME}')

    except Exception as e:
        logger.exception(e)
        raise e



# P01 - Data ingestion.
step(p01)
# P02 - loading fine-tuned model.
step(p02)
# 
