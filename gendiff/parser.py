import argparse
import json

import yaml


def parse_file(file_path):  # pragma: no cover
    if file_path.endswith(".json"):
        file = json.load(open(file_path))
    else:
        file = yaml.safe_load(open(file_path))
    return file


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    return parser.parse_args()
