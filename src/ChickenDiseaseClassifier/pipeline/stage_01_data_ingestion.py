import sys
sys.path.append("/home/shreya/work/mlproject/Chicken-Disease-Classification")
from src.ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from src.ChickenDiseaseClassifier.components.data_ingestion import DataIngestion
from src.ChickenDiseaseClassifier import logger


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(Self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
