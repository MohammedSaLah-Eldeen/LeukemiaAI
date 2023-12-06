"""
This module defines utility functiosn.
"""
import os
import yaml
import json
import joblib
import base64
from box.exceptions import BoxValueError
from LeukemiaAI import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Dict


@ensure_annotations
def loadyaml(filepath: Path) -> ConfigBox:
    """
    reads yaml file and returns a ConfigBox.

    Args:
        filepath (Path): a Path object to the yaml file.

    Returns:
        yaml file attributes as a ConfigBox.
    """
    try:
        with open(filepath) as yml:
            content = yaml.safe_load(yml)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e

    logger.info(f"yml file: {filepath} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def createdirs(paths: List, verbose=True):
    """
    a shortcut to creating multiple directories.

    Args:
        paths list(Path): list of paths of the directories to make.
    """
    for p in paths:
        os.makedirs(p, exist_ok=True)
        if verbose:
            logger.info(f"Created directory in: {p}")


@ensure_annotations
def createjson(filepath: Path, content: Dict):
    """
    a shortcut to create json files.

    Args:
        filepath (Path): path of the new file to create.
        content (dict): data.
    """

    with open(filepath, 'w') as f:
        json.dump(content, f)

    logger.info(f"Created json file at: {filepath} succussfully")


@ensure_annotations
def loadjson(filepath: Path) -> ConfigBox:
    """
    a shortcut to load json files.

    Args:
        filepath (Path): path of json file to create.

    Returns:
        ConfigBox representation of a json file.
    """

    try:
        with open(filepath, 'r') as f:
            content = json.load(f)

    except BoxValueError:
        raise ValueError('json file is empty')
    
    except Exception as e:
        raise e

    logger.info(f"loaded json file from: {filepath} succussfully")
    return ConfigBox(content)