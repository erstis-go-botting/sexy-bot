__author__ = 'jonasfelber'
from datatypes import Planet
from bs4 import BeautifulSoup

def parseRessources(text, planet =  Planet()):
    soup = BeautifulSoup(text)
    planet.metal = soup.find_all('span',attrs={'id': 'resources_metal'})[0].next.strip()
    planet.crystal = soup.find_all('span',attrs={'id': 'resources_crystal'})[0].next.strip()
    planet.deuterium = soup.find_all('span',attrs={'id': 'resources_deuterium'})[0].next.strip()
    planet.energy = soup.find_all('span',attrs={'id': 'resources_energy'})[0].next.strip()

    planet.coordinates = ''
    planet.name = ''
    planet.owner = ''

    counter = 1
    list = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    while len(list) > 0:
        print (counter)
        techid = soup.find_all('li',attrs = {'id':'button' + str(counter)})[0].find_all('a')[0].attrs.get('ref')
        level = list[0].find_all('span', attrs ={'class' : 'level'})[0].text.strip().split('\t')[-1].strip()
        planet.levels[techid] = level
        counter = counter + 1
        list = soup.find_all('li',attrs = {'id':'button'+str(counter)})
    return planet

text = open('examples/ressources.html').read()
parseRessources(text)