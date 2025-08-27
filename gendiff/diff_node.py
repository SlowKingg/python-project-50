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
