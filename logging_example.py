import logging

location = 'D:\\Essentials\\Blue Bird ==========\\Tracing\\Pycharm_project\\'

# Setting logging to DEBUG will return every type of message
logging.basicConfig(level=logging.DEBUG, filename=location + 'test_99.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filemode='w')
logger = logging.getLogger()


logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
