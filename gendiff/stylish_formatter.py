import itertools

from gendiff.format import format

SPACE = " "
MINUS = "- "
PLUS = "+ "
SPACES_COUNT = 4
SPACES_COUNT_FOR_SIGNS = 2


def make_line_stylish(key, value, depth, sign=None):
    indent = SPACE * (
        depth + (SPACES_COUNT_FOR_SIGNS if sign else SPACES_COUNT)
    )
    sign_str = sign if sign else ""
    return f"{indent}{sign_str}{key}: {value}"


def format_node_stylish(depth, key, node, iter_):
    status = node["status"]

    if status == "nested" or status == "unchanged":
        return make_line_stylish(
            key, iter_(node["value"], depth + SPACES_COUNT), depth
        )
    elif status == "added":
        return make_line_stylish(
            key, iter_(node["value"], depth + SPACES_COUNT), depth, PLUS
        )
    elif status == "deleted":
        return make_line_stylish(
            key, iter_(node["value"], depth + SPACES_COUNT), depth, MINUS
        )
    elif status == "changed":
        line1 = make_line_stylish(
            key,
            iter_(node["old_value"], depth + SPACES_COUNT),
            depth,
            MINUS,
        )
        line2 = make_line_stylish(
            key, iter_(node["new_value"], depth + SPACES_COUNT), depth, PLUS
        )
        return f"{line1}\n{line2}"


def generate_stylish(diff):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return format(current_value)

        lines = []

        for key, value in current_value.items():
            if isinstance(value, dict) and "status" in value:
                lines.append(format_node_stylish(depth, key, value, iter_))
            else:
                lines.append(
                    make_line_stylish(
                        key, iter_(value, depth + SPACES_COUNT), depth
                    )
                )

        current_indent = SPACE * depth
        result = itertools.chain("{", lines, [current_indent + "}"])

        return "\n".join(result)

    return iter_(diff, 0)
