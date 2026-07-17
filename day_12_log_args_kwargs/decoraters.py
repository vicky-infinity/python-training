# This is the code to log the time of each function
import time
import logging

logging =logging

logger = logging.getLogger("ExecutionLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("log.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("This is the test")
logger.warning("This is the warning test")
exctime_longfun = []
exctime_quick = []

def decorater(func):
    def wrapper(*args,**kwargs):
        logger.info(f"Function: {func.__name__} Inputs are {args} and {kwargs}")
        starttime = time.time() 
        result = func(*args,**kwargs)
        endtime = time.time()
        final_time = endtime - starttime
        
        print(f"Final Execution time is: {final_time}")
        logger.debug("Execution time printed")

        if func.__name__ == "long_exc_function":
            logger.warning(f"Long function {func.__name__} is Executed")
            exctime_longfun.append(final_time)
            logger.info(f"Exc Time of {func.__name__} appented to the list")
        else:
            logger.debug(f"Short Function is Exe.. name is {func.__name__}")
            exctime_quick.append(final_time)
            logger.debug(f"Function: {func.__name__} Execution time is appended to the list")

        return result
    return wrapper

@decorater
def long_exc_function(num1: int, num2: int, name:str):
    time.sleep(3)
    result = f"Hi {name} addition is {num1+num2}"
    return result


@decorater
def quick_exc_function(a="Hello"):
    return a


print(long_exc_function(50,50,"Vicky"))

print(quick_exc_function("123"))

print(f"Exc time of Quick function: {exctime_quick} \nExc time of Short function:{exctime_longfun}")