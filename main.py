from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.data_ingestion()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = DatavalidationTrainingPipeline()
    obj.data_validation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX=============X")

except Exception as e:
    raise e



STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.data_transformation()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.model()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nX============X")

except Exception as e:
    raise e



STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e