import requests

def query():

    r = requests.get("http://api.open-notify.org/iss-now.json")

    return r
