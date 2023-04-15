"""Configuration"""
import configparser


def get_header() -> str:
    """retorno de user agent"""
    return config["DEFAULT"]["USER_AGENT"]


def get_time_out() -> int:
    """TIMEOUT"""
    return int(config["DEFAULT"]["TIME_OUT"])


def get_parser() -> str:
    """parser"""
    return str(config["DEFAULT"]["PARSER"])


config = configparser.ConfigParser()
config.read("config.ini")
