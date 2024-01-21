import logging

import pytest


@pytest.mark.usefixtures("OpenBrowser")
class BaseClass():


    def getLogger(self):
        file_handler = logging.FileHandler('./Reports.log')
        logging.basicConfig(filemode='w')
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        # Add the file handler to the logger
        logger = logging.getLogger('MakeMyTrip')
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger