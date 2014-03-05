import requests

data = dict()

login_url = "http://de.ogame.gameforge.com/main/login"

data["kid"] = ""
data["uni"] = "s124-de.ogame.gameforge.com"
data["login"] = "canon"
data["pass"] = "zensored"

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
