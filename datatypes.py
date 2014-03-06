__author__ = 'jonasfelber'
class Planet:
    NOT_INITIALIZIZED = -99999 #Const, do not change!

    metal = NOT_INITIALIZIZED
    crystal = NOT_INITIALIZIZED
    deuterium = NOT_INITIALIZIZED
    dark_matter = NOT_INITIALIZIZED
    energy = NOT_INITIALIZIZED

    coordinates = '-1:-1:-1' #Koordinaten des Planeten
    name = 'unknown' #Name des Planeten
    owner = 'unknown' #Besitzer des Planeten

    resources = [] # Stufe/Level der 'ressources' Gebäude