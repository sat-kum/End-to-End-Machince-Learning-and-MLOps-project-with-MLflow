from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def model(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config= model_trainer_config)
        model_trainer_config.train()



if __name__== '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.model()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nX============X")

    except Exception as e:
        raise e