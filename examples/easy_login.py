import requests

data = dict()

login_url = "http://en.ogame.gameforge.com/main/login"

data["kid"] = ""
data["uni"] = "s124-en.ogame.gameforge.com"
data["login"] = "name"
data["pass"] = "password"

r = requests.post(login_url, data)

print(r.text) # gets the whole sourcecode and prints it


###############################################
# CHEAT SHEET
#
# post: requests.post
# get: requests.get
# sourcecode: requests.get.text
#
###############################################
