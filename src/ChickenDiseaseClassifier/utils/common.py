import os
import yaml
import json
import joblib
import base64
import re
from pathlib import Path
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
from src.ChickenDiseaseClassifier import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs are to be created. Defaults to False.    
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """save json data

    Args:
        path_to_json (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path_to_json, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"Json file saved at: {path_to_json}")


@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """load data of json file

    Args:
        path_to_json (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path_to_json) as f:
        content = json.load(f)

    logger.info(f"Json file loaded successfully from: {path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path_to_file: Path):
    """save binary data
    
    Args:
        data (Any): data to be saved in the file
        path_to_file (Path): path to binary file
    """
    joblib.dump(value=data, filename=path_to_file)
    logger.info(f"Binary file saved at: {path_to_file}")


@ensure_annotations
def load_bin(path_to_file: Path) -> Any:
    """load binary file

    Args:
        path_to_file (Path): path to binary file

    Returns:
        Any: object stored in the binary file
    """
    data = joblib.load(path_to_file)
    logger.info(f"Binary file loaded from: {path_to_file}")
    return data


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """get size in KB

    Args:
        path_to_file (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path_to_file)/1024)
    return f"~ {size_in_kb} KB"


def decode_image(img_string, filename):
    is_encoded = re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", img_string)
    if is_encoded:
        img_data = base64.b64decode(img_string)
    else:
        img_data = base64.b64encode(img_string)
    
    with open(filename, "wb") as f:
        f.write(img_data)
        f.close()


def encode_image(img_path):
    print(f"encoded image path: {img_path}")
    with open(img_path, "rb") as f:
        return base64.b64decode(f.read())

