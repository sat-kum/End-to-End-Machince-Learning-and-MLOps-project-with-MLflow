from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.data_ingestion()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n ==========x")
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