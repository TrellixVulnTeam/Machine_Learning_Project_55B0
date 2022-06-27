from housing.constant import CONFIG_FILE_PATH
from housing.entity.config_entity import DataIngestionConfig , DataValidationConfig, DataTransformationConfig, ModelTrainingConfig , ModelEvaluationConfig, ModelPusherConfig, TrainingPiplineConfig
from housing.util.util import read_yaml_file 
from housing.constant import *
from housing.exception import HousingException
import sys
from housing.logger import logging

class Configuration:

    def __init__(self,config_file_path:str=CONFIG_FILE_PATH,
                  current_time_stamp:str=CURRENT_TIME_STAMP) -> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPiplineConfig:
        try:
            training_pipline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir= os.path.join(ROOT_DIR,training_pipline_config[TRAINING_PIPELINE_NAME_KEY],training_pipline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            trainingPiplineConfig = TrainingPiplineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config : {training_pipline_config}")
        except Exception as e:
            raise HousingException(e,sys) from e

