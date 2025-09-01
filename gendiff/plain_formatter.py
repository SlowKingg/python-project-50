from gendiff.format import format


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
