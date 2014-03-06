__author__ = 'seamaster'

def builddec(currentlevels):
    """Decides, what to build next. Based on an input-dict and a build_guide.txt.
    Returns the name of the building as a string"""
    build_guide = open(r"settings\build_guide.txt").readlines()
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
