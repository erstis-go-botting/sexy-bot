author__ = 'seamaster'

import configparser
import os

def builddec(currentlevels):
    """Decides, what to build next. Based on an input-dict and a build_guide.txt.
    Returns the name of the building as a string"""
    build_guide = open("settings" + os.sep + " build_guide.txt",'r').readlines()
    for line in build_guide:
        line = line.strip().split()
        print("hail: " + line[0] + "lvl: " + line[1])
        if not line[0] in currentlevels:
            print("LOL: " + line[0])
            return line[0]
        else:
            if currentlevels[line[0]] < int(line[1]):
                print(line[0])
                return str(line[0])

buildings_lvls = {"Metallmine": 2, "Kristallmine": 3, "Solarkraftwerk": 1}

builddec(buildings_lvls)

#techID_to_String
#returns "NA" if techid is not found.
def techID_to_string(techid):
    """Returns a the apropriate tech as a string."""
    config = configparser.ConfigParser()
    config.read(r'techIDs.ini')
    section = config.sections()
    for sec in section:
       # print("section" + sec)
        for item in config[sec].items():
            #print(int(item[1].strip()))
            if str(item[1].strip())==str(techid):
                return str(item[0]).title()
    return("NA")

#returns string of tech id
#returns "NA" if not available
def string_to_techID(techString):
    config = configparser.ConfigParser()
    config.read(r'techIDs.ini')
    sections = config.sections()
    for sec in sections:
        if not (config.get(sec, techString.title(), fallback=None))==None:
            return config.get(sec, techString)
    return("NA")

#returns the section name, can be called with integer variable or string.
#returns "NA" if not available
#also deals with shortcuts
def get_section(techString):
    tdechString=str(techString)
    if(isinstance(techString, int)):
        techString=techID_to_string(techString)
    config = configparser.ConfigParser()
    config.read(r'techIDs.ini')
    sections = config.sections()
    for sec in sections:
        if not (config.get(sec, techString.title(), fallback=None))==None:
            if sec=='shortcuts':
                return get_section(config.get(sec,techString))
            else:
                return sec
    return "NA"

#print(get_section(1))
#print(get_section('S'))
#print(get_section("Roboterfabrik"))
#print(techID_to_string(404))
