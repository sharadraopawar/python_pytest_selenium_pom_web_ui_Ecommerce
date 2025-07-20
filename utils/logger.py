import logging
import os

def setup_logger(name="test_logger"):
    os.makedirs("logs",exist_ok=True)
    logger= logging.getLogger(name)
    logger.setLevel(logging.INFO)

    file_handler =logging.FileHandler("logs/test_log.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger