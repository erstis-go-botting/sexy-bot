__author__ = 'blackmesa'

# coding=utf-8
__author__ = 'sudo'

from configparser import ConfigParser
import requests
import bs4


session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/17.0 Firefox/17.0'})


def login():

    LOGIN_URL = "http://de.ogame.gameforge.com/main/login"

    cparser = ConfigParser()
    cparser.read("settings/settings.ini")

    password = cparser.get('credentials', 'password')
    username = cparser.get('credentials', 'username')
    universe = cparser.get('credentials', 'universe')

    data = dict()
    data['kid'] = ""
    data['pass'] = "put your pw here"
    data['login'] = "put your username here"
    data['uni'] = "s"+universe+"-de.ogame.gameforge.com"

    session.post(LOGIN_URL, data)

    print('Logged in with: [{username} | {password}] on universe [{universe}]'.format(**locals()))

login()

page = session.get("http://s125-de.ogame.gameforge.com/game/index.php?page=resources").text
soup = bs4.BeautifulSoup(page)

# ugly voodoo stuff:
temp_buildings_parse = soup.find_all('div', attrs={"class": "buildingimg"})
buildable = [element.a["onclick"] for element in temp_buildings_parse if "onclick" in element.a.attrs]
# end of uvs

print("%s possible buildings." % len(buildable))

## Just build the first possible building
print(buildable[0].split("'")[1])
session.get(buildable[0].split("'")[1])



