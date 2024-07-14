from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def data_transformation(self):
        try:
            with open(Path("artifacts/Data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]


            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            
            else:
                raise Exception("you data schema is not valid")
            
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.data_transformation()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=============X")
    except Exception as e:
        logger.exception(e)
        raise e