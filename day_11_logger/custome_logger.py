import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



# A handler decides where the logs should go.

handler = logging.FileHandler('log.log')
# A formatter decides how the log message should look.
formatter  = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
# apply the formatting onto the custom formatter
handler.setFormatter(formatter)
# Adding the handler to the logger
logger.addHandler(handler)
#loging 
logger.debug("Test the custome logging ")