from cnnClassifier import logger 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data ingestion"
try:
    logger.info(f">>>>>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>>")
    
except Exception as e:
    raise e