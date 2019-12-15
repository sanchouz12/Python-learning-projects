import logging

logging.basicConfig(format = "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)s] %(message)s",
                    datefmt = "%d.%m.%Y %H:%M:%S",
                    level = logging.DEBUG,
                    filename = "logs.txt")

logger = logging.getLogger("simple-logger")

logger.info("This is an example of message")
logger.critical("This is another example of message")
