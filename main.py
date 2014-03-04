# coding=utf-8
__author__ = 'sudo'

from configparser import ConfigParser
import requests


def login():
    LOGIN_URL = "http://en.ogame.gameforge.com/main/login"

    cparser = ConfigParser()
    cparser.read("settings/settings.ini")

    password = cparser.get('credentials', 'password')
    username = cparser.get('credentials', 'username')
    universe = cparser.get('credentials', 'universe')

    data = dict()
    data['pass'] = password
    data['login'] = username
    data['uni'] = "s"+universe+"-en.ogame.gameforge.com"

    requests.post(LOGIN_URL, data)

    print('Logged in with: [{username} | {password}] on universe [{universe}]'.format(**locals()))



login()