from src.ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from src.ChickenDiseaseClassifier.components.prepare_callbacks import PrepareCallback
 
try:
    config = ConfigurationManager()
    prepare_callbacks_config = config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

except Exception as e:
    raise e
