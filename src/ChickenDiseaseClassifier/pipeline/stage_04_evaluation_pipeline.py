import sys
sys.path.append("/home/shreya/work/mlproject/Chicken-Disease-Classification")
from src.ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from src.ChickenDiseaseClassifier.components.evaluation import Evaluation
from src.ChickenDiseaseClassifier import logger


STAGE_NAME = "Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
