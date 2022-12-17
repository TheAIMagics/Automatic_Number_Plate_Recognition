import os
from from_root import from_root
from dataclasses import dataclass
from src.ANPR.constants import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_DATA_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, S3_DATA_FOLDER_NAME)
        self.UNZIP_FOLDER_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, UNZIP_FOLDER_NAME)

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.LABELED_DATAFRAME : str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, LABELED_DATAFRAME)
        self.DATA_TRANSFORMATION_DATA :str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_DATA)
        self.DATA_TRANSFORMATION_OUTPUT :str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRANSFORMED_OUTPUT)

@dataclass
class PrepareBaseModelConfig:
    def __init__(self):
        self.PREPARE_BASEMODEL_ARTIFACTS_DIR :str = os.path.join(from_root(), ARTIFACTS_DIR, PREPARE_BASE_MODEL_DIR)
        self.BASEMODEL_PATH:str= os.path.join(self.PREPARE_BASEMODEL_ARTIFACTS_DIR, BASE_MODEL_PATH)
        self.UPDATED_MODEL_PATH:str = os.path.join(self.PREPARE_BASEMODEL_ARTIFACTS_DIR, UPDATED_MODEL_PATH)
