import logging

# This is the basic config but this is not  prefered can and have to create the different logger for this which is called as custome logs
#For example we want to sent the email of the logs or we want to send the logs to the db or just print it 
# We can and have to meke the custome logs so that we can change there setting lr formatting and all
logging.basicConfig(filename="file.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s ")

# These are the levels of logs in order
logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")


# How to log the veriable value
a = 10
logging.debug(f"{a}")
logging.debug(a)
b = a
logging.debug(f"This is the b {b}")

# Try Except

try:
    1/0
except ZeroDivisionError as e:
    logging.exception(f"This is the exception {e}")
