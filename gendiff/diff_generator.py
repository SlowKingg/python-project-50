import itertools

from .parser import parse_file

SPACE = " "
MINUS = "- "
PLUS = "+ "
SPACES_COUNT = 4
SPACES_COUNT_FOR_SIGNS = 2


# {
#     "key": "common",
#     "status": "unchanged" / "changed" / "added" / "deleted"
#     "value": "{
#            "key": "follow"
#            "status": "added"
#            "value": false
#      }"
# }
def format(data):
    match data:
        case True:
            return "true"
        case False:
            return "false"
        case None:
            return "null"
        case _:
            return str(data)


def build_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff = {}

    for key in keys:
        if key not in dict1:
            diff[key] = {
                "status": "added",
                "value": dict2[key],
            }
        elif key not in dict2:
            diff[key] = {
                "status": "deleted",
                "value": dict1[key],
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = build_diff(dict1[key], dict2[key])
        elif dict1[key] != dict2[key]:
            diff[key] = {
                "status": "changed",
                "old_value": dict1[key],
                "new_value": dict2[key],
            }
        else:
            diff[key] = {
                "status": "unchanged",
                "value": dict1[key],
            }

    return diff


def generate_stylish(diff):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return format(current_value)

        deep_indent = SPACE * (depth + SPACES_COUNT)
        sign_indent = SPACE * (depth + SPACES_COUNT_FOR_SIGNS)
        current_indent = SPACE * depth
        lines = []

        for key, val in current_value.items():
            if isinstance(val, dict) and "status" in val:
                match val:
                    case {"status": "added", "value": v}:
                        lines.append(
                            f"{sign_indent}{PLUS}{key}: {iter_(v, (depth + SPACES_COUNT))}"
                        )
                    case {"status": "deleted", "value": v}:
                        lines.append(
                            f"{sign_indent}{MINUS}{key}: {iter_(v, (depth + SPACES_COUNT))}"
                        )
                    case {
                        "status": "changed",
                        "old_value": ov,
                        "new_value": nv,
                    }:
                        lines.append(
                            f"{sign_indent}{MINUS}{key}: {iter_(ov, (depth + SPACES_COUNT))}"
                        )
                        lines.append(
                            f"{sign_indent}{PLUS}{key}: {iter_(nv, (depth + SPACES_COUNT))}"
                        )
                    case {"status": "unchanged", "value": v}:
                        lines.append(
                            f"{deep_indent}{key}: {iter_(v, (depth + SPACES_COUNT))}"
                        )
            else:
                lines.append(
                    f"{deep_indent}{key}: {iter_(val, (depth + SPACES_COUNT))}"
                )

        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(diff, 0)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1, file2 = parse_file(file_path1), parse_file(file_path2)

    diff = build_diff(file1, file2)

    return generate_stylish(diff)
