from gendiff.file_parser import parse_file
from gendiff.json_formatter import generate_json
from gendiff.plain_formatter import generate_plain
from gendiff.stylish_formatter import generate_stylish


def make_diff_node_added(value):
    return {"status": "added", "value": value}


def make_diff_node_deleted(value):
    return {"status": "deleted", "value": value}


def make_diff_node_changed(old_value, new_value):
    return {"status": "changed", "old_value": old_value, "new_value": new_value}


def make_diff_node_unchanged(value):
    return {"status": "unchanged", "value": value}


def make_diff_node_nested(value):
    return {"status": "nested", "value": value}


def build_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff = {}

    for key in keys:
        if key not in dict1:
            diff[key] = make_diff_node_added(dict2[key])
        elif key not in dict2:
            diff[key] = make_diff_node_deleted(dict1[key])
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = make_diff_node_nested(
                build_diff(dict1[key], dict2[key])
            )
        elif dict1[key] != dict2[key]:
            diff[key] = make_diff_node_changed(dict1[key], dict2[key])
        else:
            diff[key] = make_diff_node_unchanged(dict1[key])

    return diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1, file2 = parse_file(file_path1), parse_file(file_path2)

    diff = build_diff(file1, file2)

    match format_name:
        case "stylish":
            return generate_stylish(diff)
        case "plain":
            return generate_plain(diff)
        case "json":
            return generate_json(diff)
