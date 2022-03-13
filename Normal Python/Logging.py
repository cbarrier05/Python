# Allows you to output to log
import logging
# By default only warning, error and critical output to log
# This can be changed with
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%d/%m/%Y %H:%M:%S")
# The types of log
logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")