import requests
import json

from adjuster.campaign import Campaign
from adjuster.creative import Creative
from adjuster.util import *


class RestService:
    """
    Basic REST Service for Homework
    """

    @staticmethod
    def http_get_campaigns():
        """
        Get Campaigns from Ad-Juster
        :param self:
        :return: list Campaign objects
        """
        return json.loads(RestService.get_method(ROOT_URL + "campaigns"), object_hook=lambda d: Campaign(d))

    @staticmethod
    def http_get_creatives():
        """
        Get Creatives from Ad-Juster
        :param self:
        :return: list Creative objects
        """
        return json.loads(RestService.get_method(ROOT_URL + "creatives"), object_hook=lambda d: Creative(d))

    @staticmethod
    def get_method(url):
        """
        Calls Requests.Get Method
        :param url:
        :return: text of result
        """
        try:
            r = requests.get(url, timeout=3)
            r.raise_for_status()
            return r.text
        except requests.exceptions.HTTPError as eh:
            logger.fatal("Http Error:", eh)
        except requests.exceptions.ConnectionError as ec:
            logger.fatal("Error Connecting:", ec)
        except requests.exceptions.Timeout as et:
            logger.fatal("Timeout Error:", et)
        except requests.exceptions.RequestException as err:
            logger.fatal("Uhh Ohh: Something Else", err)  # general error
            raise
