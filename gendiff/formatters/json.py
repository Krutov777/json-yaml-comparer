"""Json formatter from dict diff."""
import json
from typing import Any, Dict

from gendiff import dict_diff


def format_dict(dict_diff):
    """Format dict diff to json string."""
    filtered_ast = _build_dict(dict_diff)
    return json.dumps(filtered_ast)


def _build_dict(dict_diff):
    result = {}
    for key, node in dict_diff.items():
        if node[dict_diff.TYPE] == dict_diff.PARENT:
            result[key] = _build_dict(node[dict_diff.CHILDREN])
        else:
            result[key] = node
    return result