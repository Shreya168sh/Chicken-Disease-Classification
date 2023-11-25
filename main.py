from src.ChickenDiseaseClassifier import logger
from src.ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.ChickenDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.ChickenDiseaseClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.ChickenDiseaseClassifier.pipeline.stage_04_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"

try:
    logger.info(f"*******************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
