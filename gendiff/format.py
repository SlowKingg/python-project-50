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


def format_node_stylish(depth, key, node, iter_):
    match node:
        case {"status": "nested", "value": v}:
            return make_line_stylish(key, iter_(v, depth + SPACES_COUNT), depth)

        case {"status": "added", "value": v}:
            return make_line_stylish(
                key, iter_(v, depth + SPACES_COUNT), depth, PLUS
            )

        case {"status": "deleted", "value": v}:
            return make_line_stylish(
                key, iter_(v, depth + SPACES_COUNT), depth, MINUS
            )

        case {"status": "changed", "old_value": ov, "new_value": nv}:
            line1 = make_line_stylish(
                key, iter_(ov, depth + SPACES_COUNT), depth, MINUS
            )
            line2 = make_line_stylish(
                key, iter_(nv, depth + SPACES_COUNT), depth, PLUS
            )
            return f"{line1}\n{line2}"
        case {"status": "unchanged", "value": v}:
            return make_line_stylish(key, iter_(v, depth + SPACES_COUNT), depth)

        case _:
            return make_line_stylish(
                key, iter_(node, depth + SPACES_COUNT), depth
            )


def generate_stylish(diff):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return format(current_value)

        lines = []

        for key, node in current_value.items():
            lines.append(format_node_stylish(depth, key, node, iter_))

        current_indent = SPACE * depth
        result = itertools.chain("{", lines, [current_indent + "}"])

        return "\n".join(result)

    return iter_(diff, 0)


def format_node_plain(path, node, iter_):
    match node:
        case {"status": "nested", "value": v}:
            return iter_(v, path)
        case {"status": "added", "value": v}:
            return (
                f"Property '{path}' was added with value: "
                f"{format(v, plain=True)}"
            )
        case {"status": "deleted"}:
            return f"Property '{path}' was removed"
        case {"status": "changed", "old_value": ov, "new_value": nv}:
            return (
                f"Property '{path}' was updated. "
                f"From {format(ov, plain=True)} "
                f"to {format(nv, plain=True)}"
            )
        case _:  # case unchanged
            return None


def generate_plain(diff):
    def iter_(current_value, path):
        lines = []

        for key, node in current_value.items():
            full_path = f"{path}.{key}" if path else key

            line = format_node_plain(full_path, node, iter_)

            if line:
                lines.append(line)

        return "\n".join(lines)

    return iter_(diff, "")


def generate_json(diff):  # pragma: no cover
    return json.dumps(diff)
