import requests

__all__ = [
    "where",
    "who"
]

def where():

    r = requests.get("http://api.open-notify.org/iss-now.json")

    return r


def who():

    r = requests.get("http://api.open-notify.org/astros.json")

    return r
