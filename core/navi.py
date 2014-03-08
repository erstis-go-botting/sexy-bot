# coding=utf-8
__author__ = 'alskgj'

# interface between bot logic and ogame

import requests
import logging
import configparser
from bs4 import BeautifulSoup


class Bot(object):
    """
    Accesses ogame and provides functionality

    There are several different methods implemented.
    Login logs you in, goto helps you to easily navigate the different pages, build_something(techid)
    constructs a building (probably only works for buildings found under page=resources).

    More sexy stuff coming soon. My hands are typing code. alskdfjölkasdjfölj <-- important part of
    documentation.
    """

    # Create a lovely session!
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/17.0 Firefox/17.0'})
    config = configparser.ConfigParser()
    config.read(r'settings/settings.ini')

    # some cool settings
    universe = config.get('credentials', 'universe')

    # Constants
    baseurl = 'http://s{universe}-de.ogame.gameforge.com/game/index.php?page='.format(**locals())

    def __init__(self):

        # a cool logging functionality
        self.logger = logging.getLogger('root.'+__name__)
        self.logger.info('Bot initialized')

        self.login()
        self.build_something(4)  # just an example. ofc techid shouldnt be hardcoded

    def login(self):
        """
        Takes no argument,
        Returns 1 if successful
        else 0.
        """

        # TODO check if is already logged in
        # TODO check if login is actually successful

        login_url = "http://de.ogame.gameforge.com/main/login"
        password = Bot.config.get('credentials', 'password')
        username = Bot.config.get('credentials', 'username')

        data = dict()
        data['kid'] = ""
        data['pass'] = password
        data['login'] = username
        data['uni'] = "s"+self.universe+"-de.ogame.gameforge.com"

        Bot.session.post(login_url, data)

        self.logger.info('Logged in with: [{username}]:[{password}] on universe [{self.universe}]'.format(**locals()))
        return 1

    def goto(self, destination):
        """
        Brings you where you need to go.
        Usage:
        goto("resources")
        --> Bot.session is now at page ogame.com/game/index.php?page=resources
        returns Bot.session.text
        """
        self.logger.info('Navigating to '+destination)
        return Bot.session.get(Bot.baseurl+destination).text

    def build_something(self, techid):
        """
        Takes a techid (TODO /a string)
        and tries to build it.
        Returns 1 if succesful,
        else 0.
        """
        techid = str(techid)
        self.logger.info("Trying to build "+techid)

        # // TODO DOUBLECHECK THIS: is it always resources? --> probably other for some buildings?
        soup = BeautifulSoup(self.goto("resources"))

        temp_buildings_parse = soup.find_all('div', attrs={"class": "buildingimg"})
        buildable = [element.a["onclick"] for element in temp_buildings_parse if "onclick" in element.a.attrs]
        self.logger.debug("%s possible buildings." % len(buildable))

        if buildable:
            building_links = [element.split("'")[1] for element in buildable]
            target = [element for element in building_links if "type="+techid in element]
            if len(target) == 0:
                logging.info(techid+" isn't buildable atm.")
                return 0
            elif len(target) == 1:
                logging.info("sent build request. techid: [%s]. url: [%s]" % (techid, target[0]))
                Bot.session.get(target[0])
                return 1
            else:
                logging.critical("Strange error. Needs inspection asap. list: [%s]" % target)
