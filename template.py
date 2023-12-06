"""
Auto project file structure creator.
"""
import os
from pathlib import Path
import logging

# logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s]: %(message)s")

PROJECT_NAME = "LeukemiaAI"

FILES_PATHS = [
    ".github/workflows/.gitkeep",
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/utils/__init__.py",
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/components.py",
    f"{PROJECT_NAME}/config.py",
    f"{PROJECT_NAME}/constants.py",
    "config/config.yml",
    "dvc.yml",
    "params.yml",
    "requirements.txt",
    "requirements.dev.txt",
    "research/trials.ipynb",
    "templates/index.html",
]

# creating files.
for f_path in FILES_PATHS:
    f_dir, f_name = os.path.split(Path(f_path))

    if f_dir != "":
        os.makedirs(f_dir, exist_ok=True)
        logging.info(f"created dir: [{f_dir}]")

    if not os.path.exists(f_path):
        with open(f_path, "w") as f:
            logging.info(f"created file [{f_name}]")

    else:
        logging.info(f"[{f_name}], already created !")
