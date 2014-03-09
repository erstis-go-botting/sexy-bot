import os

#checks if settings.ini should be generated. if not given universe, username and password it will generate a settings.ini with the default account


def settings_generator(universe = 82, username = 'defaultName', password = 'defaultPassword'):
    if not (os.path.isdir('settings')):
        os.makedir('settings')
    path = os.path.normcase('settings/settings.ini')
    if not(os.path.isfile(path)):
        with open(path,'w') as foo:
            foo.write('[credentials]\nuniverse = '+ str(universe) +'\npassword = '+password+'\nusername = '+username)

settings_generator()
