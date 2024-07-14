from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def evaluation(self):
                
        config = ConfigurationManager()
        model_evalution_config = config.get_model_evalution_config()
        model_evalution_config = ModelEvaluation(config=model_evalution_config)
        model_evalution_config.log_into_mlflow()





if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



from sqlite3 import connect
conn = c