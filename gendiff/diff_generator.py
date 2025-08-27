from .diff_node import (
    make_diff_node_added,
    make_diff_node_changed,
    make_diff_node_deleted,
    make_diff_node_nested,
    make_diff_node_unchanged,
)
from .format import generate_json, generate_plain, generate_stylish
from .parser import parse_file


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
