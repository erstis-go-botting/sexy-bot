import os

#checks if settings.ini should be generated. if not given universe, username and password it will generate a settings.ini with the default account
#This settings_generator will only work for universe 82 if the flag argument is given als True(to make sure that universe 82 is intended)

def settings_generator(universe = 82, username = 'defaultName', password = 'defaultPassword', flag=False):
    if (universe == 82 and not(flag)) or (username == 'defaultName') or (password == 'defaultPassword'):
        print("Not all fields specified, fallback on default configuration")
        universe = 82
        username = 'defaultName'
        password = 'defaultPassword'
    if not (os.path.isdir('settings')):
        os.makedir('settings')
    path = os.path.normcase('settings/settings.ini')
    if not(os.path.isfile(path)):
        with open(path,'w') as foo:
            foo.write('[credentials]\nuniverse = '+ str(universe) +'\npassword = '+password+'\nusername = '+username)

#settings_generator()
