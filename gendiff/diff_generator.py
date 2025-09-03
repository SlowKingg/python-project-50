from gendiff.format import generate_json, generate_plain, generate_stylish
from gendiff.parsers import parse_file


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
    """
    Builds a diff representation between two dictionaries.

    Compares two dictionaries and generates a diff structure that describes
    the differences between them. The diff structure is a dictionary where each
    key corresponds to a key in either input dictionary, and the value is a node
    describing the type of change (added, deleted, changed, unchanged, or
    nested).

    Args:
        dict1 (dict): The first dictionary to compare.
        dict2 (dict): The second dictionary to compare.

    Returns:
        dict: A dictionary representing the diff between dict1 and dict2, where
            each key maps to a diff node indicating the type of change and the
            associated values.
    """

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
    """
    Generates a difference report between two configuration files
    in the specified format.

    Args:
        file_path1 (str): Path to the first file to compare.
        file_path2 (str): Path to the second file to compare.
        format_name (str, optional): The format of the output diff.
                        Supported formats are "stylish", "plain", and "json".
                        Defaults to "stylish".

    Returns:
        str: The formatted difference between the two files.
    """

    file1, file2 = parse_file(file_path1), parse_file(file_path2)

    diff = build_diff(file1, file2)

    match format_name:
        case "stylish":
            return generate_stylish(diff)
        case "plain":
            return generate_plain(diff)
        case "json":
            return generate_json(diff)
