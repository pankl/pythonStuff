import requests
from bs4 import *
import validators
from requests import Response


def getPageByUrl(_url="https://www.google.com"):
    """A method that gets url and returns its content parsed as html tree,
    if no url provided falls back to default one"""
    if not validators.url(_url):
        return "Invalid url provided"
    with requests.Session() as session:
        response: Response = session.get(_url)
        return BeautifulSoup(response.content, 'lxml')


if __name__ == "__main__":
    url = input("Please provide url to be scrapped")

    res = getPageByUrl()

    print(res)