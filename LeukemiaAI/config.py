"""
defines all configuration classes needed for the pipeline.
"""
# system
import os
import sys
from pathlib import Path

# LeukemiaAI
from LeukemiaAI.constants import *
from LeukemiaAI.utils import tools

# python
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration settings for Data."""
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    kaggle: bool


@dataclass(frozen=True)
class FinetunedModelConfig:
    """Configuration settings for the fine-tuned model."""
    root_dir: Path
    huggingface_repo: str
    model_dir: Path


class ConfigurationManager:
    """manages configuration of all modules."""
    def __init__(self, config_filepath: Path, params_filepath: Path):

        self.config = tools.loadyaml(config_filepath)
        self.params = tools.loadyaml(params_filepath)

        dirs = []
        dirs.append(self.config.research_data.root_dir)
        dirs.append(self.config.model.root_dir)
        tools.createdirs(dirs)

    def data_ingestion_configs(self) -> DataIngestionConfig:
        """reads `self.config` yml file and returns a config class."""

        diconfig = DataIngestionConfig(
            root_dir=self.config.research_data.root_dir,
            source_URL=self.config.research_data.source_URL,
            local_data_file=self.config.research_data.local_data_file,
            unzip_dir=self.config.research_data.unzip_dir,
            kaggle=self.config.research_data.kaggle
        )

        return diconfig
    
    def model_configs(self) -> FinetunedModelConfig:
        """reads `self.config` yml file and returns a config class."""

        mconfig = FinetunedModelConfig(
            root_dir=self.config.model.root_dir,
            huggingface_repo=self.config.model.huggingface_repo,
            model_dir=self.config.model.model_dir
        )
    
        return mconfig

