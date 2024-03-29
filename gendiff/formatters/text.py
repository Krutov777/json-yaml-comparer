"""Text formatter from dict."""

from gendiff import dict_diff

_SYMBOLS = {
    dict_diff.ADDED: '+',
    dict_diff.REMOVED: '-',
    dict_diff.UNCHANGED: ' ',
}


def format_dict(diff):
    """Format dict_diff to text string."""
    return '{{\n{message}\n}}'.format(
        message=_build_message(diff),
    )


def _build_message(diff, depth=0):
    message_lines = []
    for key, node in sorted(diff.items(), key=lambda item: item[0]):
        node_type = node[dict_diff.TYPE]
        if node_type == dict_diff.PARENT:
            children = _build_message(node[dict_diff.CHILDREN], depth=depth+1)
            line = '    {indent}{key}: {{\n{children}\n    {indent}}}'.format(
                children=children,
                key=key,
                indent=_get_indent(depth),
            )
        elif node_type == dict_diff.CHANGED:
            line = '{added}\n{removed}'.format(
                added=_get_message(
                    dict_diff.ADDED,
                    key,
                    node[dict_diff.VALUE],
                    depth
                    ),
                removed=_get_message(
                    dict_diff.REMOVED,
                    key,
                    node[dict_diff.OLD_VALUE],
                    depth,
                ),
            )
        else:
            line = _get_message(node_type, key, node[dict_diff.VALUE], depth)
        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_message(node_type, key, value, depth):
    return '{indent}  {symbol} {key}: {value}'.format(
        symbol=_SYMBOLS.get(node_type, ' '),
        key=key,
        value=_get_value(value, depth + 1),
        indent=_get_indent(depth),
    )


def _get_value(value, depth):
    if isinstance(value, dict):
        return _get_dict_value(value, depth)
    return value


def _get_dict_value(sub_dict, depth):
    res = []
    for key, value in sub_dict.items():
        res.append('{{\n    {indent}{key}: {value}\n{indent}}}'.format(
            key=key,
            value=value,
            indent=_get_indent(depth),
        ))
    return '\n'.join(res)


def _get_indent(depth):
    return '    ' * depth
