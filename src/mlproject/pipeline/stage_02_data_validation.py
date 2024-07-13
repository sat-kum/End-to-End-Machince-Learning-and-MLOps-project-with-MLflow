from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import DataValidation
from mlproject import logger


STAGE_NAME = "Data Validation stage"

class DatavalidationTrainingPipeline:
    def __init__(self):
        pass

    def data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validation_all_columns()




if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = DatavalidationTrainingPipeline()
        obj.data_validation()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX=============X")

    except Exception as e:
        raise e