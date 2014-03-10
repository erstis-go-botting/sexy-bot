__author__ = 'jonasfelber'
from bs4 import BeautifulSoup
import re
from builder import techID_to_string
 # TODO add constants

def parse_buildings(soup, planet,counter_start):
    if not planet.__contains__('levels'):
        planet['levels'] = dict()


    counter = counter_start
    building_nodes = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    #DISCLAIMER: Do not read the code, when you can't handle it!
    while len(building_nodes) > 0:
        #This is the part, where we kill the lamb
        sub_nodes = building_nodes[0].find_all('a',re.compile('detail'))
        if not sub_nodes:
            sub_nodes = building_nodes[0].find_all('a', attrs = {'id' : 'details'})
            if not sub_nodes:
                sub_nodes = building_nodes[0].find_all('a', attrs = {'id' : 'details2'})
        techid = sub_nodes[0].attrs.get('ref')
        #This is the part, where we extract the blood out of the lamb (for later use in our black macic code)
        level = building_nodes[0].find_all('span', attrs ={'class' : 'level'})[0].text.strip().split('\t')[-1].strip()
        planet['levels'][techID_to_string(techid)] = int(level)
        counter = counter + 1
        building_nodes = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    return planet

def parse_resources(text, planet = dict()):
    """
    text = whole html page!
    parsed the 'resources' page
    """
    #DISCLAIMER: Black macic code here!
    soup = BeautifulSoup(text)

    planet['metal'] = metal = soup.find_all('span', attrs={'id': 'resources_metal'})[0].next.strip()
    planet['crystal'] = soup.find_all('span', attrs={'id': 'resources_crystal'})[0].next.strip()
    planet['deuterium'] = soup.find_all('span', attrs={'id': 'resources_deuterium'})[0].next.strip()
    planet['energy'] = soup.find_all('span', attrs={'id': 'resources_energy'})[0].next.strip()

    # TODO parse (Ich mache das, sobald ich mehre Planeten habe)
    planet['galaxy'] = -1
    planet['system'] = -1
    planet['position'] = -1
    planet['name'] = 'you'
    planet['owner'] = 'you'

    if not planet.__contains__('levels'):
        planet['levels'] = dict()

    parse_buildings(soup,planet,1)
    return planet



def parse_station(text,planet = dict()):
    soup = BeautifulSoup(text)
    if not planet.__contains__('levels'):
        planet['levels'] = dict()

    return parse_buildings(soup,planet,counter_start=0)

def parse_research(text,planet = dict()):
    soup = BeautifulSoup(text)
    if not planet.__contains__('levels'):
        planet['levels'] = dict()

    nodes = soup.find_all('div',attrs={'class':'buildingimg'})
    for node in nodes:
        id = node.find_all('a')[-1].attrs.get('ref')
        levels = node.find_all('a')[-1].find_all('span',attrs= {'class':'level'})[-1]
        level = -1
        if len(levels.contents) == 1:
            level = levels.contents[0].strip()
        else:
            level = levels.contents[2].strip()
        planet['levels'][techID_to_string(id)] = int(level)
    return planet

def parse_system(text):
    soup = BeautifulSoup(text)
    soup.find_all()
    #planetname = soup.find_all('tr',attrs={'class' : 'row'})[4].find_all('td',attrs={'class' : 'planetname'})[0].text.strip()
    #pos-planet = soup.find_all('tr',attrs={'class' : 'row'})[4].find_all('span',attrs={'id' : 'pos-planet'})[0].text.strip()
    print('debug')
