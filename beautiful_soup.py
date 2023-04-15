"""Beatiful Soup"""
from requests import Response
from bs4 import BeautifulSoup, PageElement, ResultSet

import configuration

PARSER = configuration.get_parser()


def obtain_html(body: Response = ""):
    """Initialize BeautifulSoup"""
    return BeautifulSoup(body.text, PARSER)


def find(beatiful: BeautifulSoup, tag: str = "") -> PageElement:
    """Execute find method to BeautifulSoup"""
    return beatiful.find(tag)


def find_all(beautiful: BeautifulSoup, tag: str = "") -> ResultSet:
    """Execute find_all method to BeatifulSoup"""
    return beautiful.find_all(tag)


def get_attribute(beautiful: BeautifulSoup, attr: str = "") -> str:
    """obtain something attribute of tag"""
    return beautiful[attr]


def get_text(beautiful: BeautifulSoup):
    """Obtain text of tag"""
    return beautiful.text
