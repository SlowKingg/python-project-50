import json

import yaml


def parse_file(file_path):
    if file_path.endswith(".json"):
        with open(file_path) as f:
            return json.load(f)
    else:
        with open(file_path) as f:
            return yaml.safe_load(f)
