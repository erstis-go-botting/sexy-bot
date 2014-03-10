# coding=utf-8
__author__ = 'sudo'

import os
import logging
import time

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
    fh.setLevel(logging.DEBUG)

    # create a streamhandler
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)

    # Give us lots of infos hurrdurr
    fileformatter = logging.Formatter('%(asctime)s |%(levelname)-7s | [%(filename)s:%(lineno)s - %(funcName)20s() ] '
                                      '|%(name)-20s: %(message)s', datefmt='%d.%m %H:%M:%S')
    standardformatter = logging.Formatter(' %(asctime)s | %(filename)s:%(lineno)-5s| %(message)s',
                                          datefmt='%d.%m %H:%M:%S')
    fh.setFormatter(fileformatter)
    sh.setFormatter(standardformatter)

    # Add everything
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.info('created logger')
    return logger

logger = get_logger()
while 1:
    bot=Bot()
    bot.build_random()
    time.sleep(300)

