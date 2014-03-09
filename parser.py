__author__ = 'jonasfelber'
from datatypes import Planet
from bs4 import BeautifulSoup


def parse_resources(text, planet = Planet()):
    #DISCLAIMER: Black macic code here!
    soup = BeautifulSoup(text)
    planet.metal = soup.find_all('span', attrs={'id': 'resources_metal'})[0].next.strip()
    planet.crystal = soup.find_all('span', attrs={'id': 'resources_crystal'})[0].next.strip()
    planet.deuterium = soup.find_all('span', attrs={'id': 'resources_deuterium'})[0].next.strip()
    planet.energy = soup.find_all('span', attrs={'id': 'resources_energy'})[0].next.strip()

    planet.coordinates = ''
    planet.name = ''
    planet.owner = ''

    counter = 1
    building_nodes = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    #DISCLAIMER: Do not read the code, when you can't handle it!
    while len(building_nodes) > 0:
        print (counter)
        #This is the part, where we kill the lamb
        techid = building_nodes[0].find_all('a', attrs = {'id' : 'details'})[0].attrs.get('ref')
        #This is the part, where we extract the blood out of the lamb (for later use in our black macic code)
        level = building_nodes[0].find_all('span', attrs ={'class' : 'level'})[0].text.strip().split('\t')[-1].strip()
        planet.levels[int(techid)] = int(level)
        counter = counter + 1
        building_nodes = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    return planet

#text = open('examples/ressources.html').read()
#parseRessources(text)