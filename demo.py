import sys
from src.ANPR.exception import CustomException
from src.ANPR.logger import logging
from src.ANPR.pipeline.train_pipeline import TrainPipeline

train_obj = TrainPipeline()
train_obj.run_pipeline()