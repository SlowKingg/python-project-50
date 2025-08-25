import json

import yaml


def read_file(file_path):  # pragma: no cover
    if file_path.endswith(".json"):
        file = json.load(open(file_path))
    else:
        file = yaml.safe_load(open(file_path))
    return file


def generate_diff(file_path1, file_path2):
    file1, file2 = read_file(file_path1), read_file(file_path2)

    result = ""
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    for key in all_keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += f"  {key}: {file1[key]}\n"
            else:
                result += f"- {key}: {file1[key]}\n+ {key}: {file2[key]}\n"
        elif key in file1:
            result += f"- {key}: {file1[key]}\n"
        else:
            result += f"+ {key}: {file2[key]}\n"
    return "{\n" + result + "}"
