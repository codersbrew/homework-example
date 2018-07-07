import logging

ROOT_URL = "http://homework.ad-juster.com/api/"

# Logging
logging.basicConfig(
    format='%(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
