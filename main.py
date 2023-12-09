from cnnClassifier import logger 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_trainer import TrainingPipeline

STAGE_NAME = "Data ingestion"
try:
    logger.info(f">>>>>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>>")
    
except Exception as e:
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>>>>>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>>>>>>> ")
    obj = PrepareBaseModelPipeline()
    obj.main()
except Exception as e:
    raise e

STAGE_NAME = "Training Stage"
try:
    logger.info(f" >>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>> ")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>>. The {STAGE_NAME} stage has completed successfully >>>>>>")
except Exception as e:
    raise e
