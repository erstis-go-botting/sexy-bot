# coding=utf-8
__author__ = 'sudo'

from configparser import ConfigParser
import requests
import bs4
import os
import logging
import inspect
from core.navi import Bot


def get_logger():
    """
    Creates a sexy rootlogger.
    Saves everything in 'logs/'
    """
    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    #logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)

    # create a filehandler
    fh = logging.FileHandler('logs/debug.log')
    fh.setLevel(logging.INFO)

    # Give us lots of infos hurrdurr
    formatter = logging.Formatter('%(asctime)s |%(levelname)-7s | [%(filename)s:%(lineno)s - %(funcName)20s() ] '
                                  '|%(name)-20s: %(message)s', datefmt='%d.%m %H:%M:%S')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.info('created logger')
    return logger

logger = get_logger()
bot = Bot()


# page = bot.goto("resources")
#
# soup = bs4.BeautifulSoup(page)
#
# temp_buildings_parse = soup.find_all('div', attrs={"class": "buildingimg"})
# buildable = [element.a["onclick"] for element in temp_buildings_parse if "onclick" in element.a.attrs]
# print("%s possible buildings." % len(buildable))
#
# if buildable:
#     print(buildable[0].split("'")[1])
#     bot.session.get(buildable[0].split("'")[1])



#soup.find_all('span',attrs={'id': 'resources_metal'})[0].next.strip()
