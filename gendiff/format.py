import itertools
import json

SPACE = " "
MINUS = "- "
PLUS = "+ "
SPACES_COUNT = 4
SPACES_COUNT_FOR_SIGNS = 2


def format(data, plain=False):
    if isinstance(data, dict):
        return "[complex value]"
    match data:
        case True:
            return "true"
        case False:
            return "false"
        case None:
            return "null"
        case _:
            if isinstance(data, int) or isinstance(data, float):
                return str(data)
            return f"'{str(data)}'" if plain else str(data)


def make_line_stylish(key, value, depth, sign=None):
    indent = SPACE * (
        depth + (SPACES_COUNT_FOR_SIGNS if sign else SPACES_COUNT)
    )
    sign_str = sign if sign else ""
    return f"{indent}{sign_str}{key}: {value}"


def format_node_stylish(depth, lines, key, node, iter_):
    match node:
        case {"status": "nested", "value": v}:
            lines.append(
                make_line_stylish(key, iter_(v, depth + SPACES_COUNT), depth)
            )
        case {"status": "added", "value": v}:
            lines.append(
                make_line_stylish(
                    key, iter_(v, depth + SPACES_COUNT), depth, PLUS
                )
            )
        case {"status": "deleted", "value": v}:
            lines.append(
                make_line_stylish(
                    key, iter_(v, depth + SPACES_COUNT), depth, MINUS
                )
            )
        case {"status": "changed", "old_value": ov, "new_value": nv}:
            line1 = make_line_stylish(
                key, iter_(ov, depth + SPACES_COUNT), depth, MINUS
            )
            line2 = make_line_stylish(
                key, iter_(nv, depth + SPACES_COUNT), depth, PLUS
            )
            lines.append(f"{line1}\n{line2}")
        case {"status": "unchanged", "value": v}:
            lines.append(
                make_line_stylish(key, iter_(v, depth + SPACES_COUNT), depth)
            )
        case _:
            lines.append(
                make_line_stylish(key, iter_(node, depth + SPACES_COUNT), depth)
            )


def generate_stylish(diff):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return format(current_value)

        current_indent = SPACE * depth
        lines = []

        for key, node in current_value.items():
            format_node_stylish(depth, lines, key, node, iter_)

        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)

    return iter_(diff, 0)


def format_node_plain(path, lines, key, node, iter_):
    match node:
        case {"status": "nested", "value": v}:
            lines.append(iter_(v, f"{path}.{key}" if path else key))
        case {"status": "added", "value": v}:
            lines.append(
                (
                    f"Property '{path}.{key}' was added with value: "
                    f"{format(v, plain=True)}"
                )
                if path
                else (
                    f"Property '{key}' was added with value: "
                    f"{format(v, plain=True)}"
                )
            )
        case {"status": "deleted"}:
            lines.append(
                f"Property '{path}.{key}' was removed"
                if path
                else f"Property '{key}' was removed"
            )
        case {"status": "changed", "old_value": ov, "new_value": nv}:
            lines.append(
                (
                    f"Property '{path}.{key}' was updated. "
                    f"From {format(ov, plain=True)} "
                    f"to {format(nv, plain=True)}"
                )
                if path
                else (
                    f"Property '{key}' was updated. "
                    f"From {format(ov, plain=True)} "
                    f"to {format(nv, plain=True)}"
                )
            )


def generate_plain(diff):
    def iter_(current_value, path):
        lines = []

        for key, node in current_value.items():
            format_node_plain(path, lines, key, node, iter_)

        return "\n".join(lines)

    return iter_(diff, "")


def generate_json(diff):
    return json.dumps(diff)
