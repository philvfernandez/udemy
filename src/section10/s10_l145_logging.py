import logging

#basic config
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)
# more readable config
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename='log.txt'
)

logger = logging.getLogger('test_logger')
"""
other ways to name your logger instance
This will name the logger based on the module.
logger = logging.getLogger(__name__) 
"""


# Note: Logging in Python is configured for warning and above by default.
"""
Warning levels available:
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
logger.info('Log message #1')
logger.warning('Log message #2')
logger.error('Log message #3')
logger.critical('Log message #4')