"""Plain formatter from dict diff."""

from gendiff import dict_diff


def format_dict(diff):
    """Format dict_diff to plain string."""
    return _build_message(diff)


def _build_message(diff, parents=None):
    if not parents:
        parents = []

    message_lines = []
    for key, node in sorted(diff.items(), key=lambda item: item[0]):
        node_type = node[dict_diff.TYPE]

        if node_type == dict_diff.PARENT:
            line = _build_message(
                node[dict_diff.CHILDREN],
                parents=parents + [key],
                )
        elif node_type == dict_diff.CHANGED:
            message = "Property '{key}' was changed. From '{old}' to '{new}'"
            line = message.format(
                key=_get_path(parents, key),
                old=_get_value(node[dict_diff.OLD_VALUE]),
                new=_get_value(node[dict_diff.VALUE]),
            )
        elif node_type == dict_diff.ADDED:
            message = "Property '{key_path}' was added with value: '{value}'"
            line = message.format(
                key_path=_get_path(parents, key),
                value=_get_value(node[dict_diff.VALUE]),
            )
        elif node_type == dict_diff.REMOVED:
            line = "Property '{key_path}' was removed".format(
                key_path=_get_path(parents, key),
            )
        else:
            continue

        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_value(value):
    if isinstance(value, (dict, list)):
        return 'complex value'
    return str(value)


def _get_path(parents, key):
    return '.'.join(parents + [key])
