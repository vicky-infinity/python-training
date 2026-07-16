import logging

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# File Handler
file_handler = logging.FileHandler('log.log')

# Console Handler
stream_handler = logging.StreamHandler()

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug("Application started")