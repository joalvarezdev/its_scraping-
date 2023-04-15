"""Json utils"""
import json


def save_json(
        file_name: str = "test.json",
        mode: str = "r",
        encoding__: str = "utf-8",
        info: any = ""):
    """Save file at current path"""
    with open(file_name, mode, encoding=encoding__) as file:
        json.dump(info, file, indent=2)
