from cnnClassifier import logger 
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion"
class DataIngestionPipeline:
    def __init__(self):
        pass 

    def main(self):   
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> The {STAGE_NAME} stage has started >>>>>>>>>>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>>")
        
    except Exception as e:
        raise e
