from cnnClassifier import logger 
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.trainer import Training

STAGE_NAME = "Trainer Stage"
class TrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try:
        logger.info(f" >>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>> ")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>. The {STAGE_NAME} stage has completed successfully >>>>>>")
    except Exception as e:
        raise e
        
