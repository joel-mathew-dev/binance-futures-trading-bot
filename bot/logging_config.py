import logging
import os

def setup_logging():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        
        # File Handler (saves logs to trading_bot.log)
        file_handler = logging.FileHandler("trading_bot.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        # Console Handler (prints to terminal screen)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger

logger = setup_logging()