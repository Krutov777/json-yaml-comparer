import json
import os
import yaml


def read_file(file_path):
    ext = os.path.splitext(file_path)[-1]
    if ext == '.json':
        file = json.load(open(file_path))
    elif ext == '.yml' or ext == '.yaml':
        stream = open(file_path, 'r')
        file = yaml.safe_load(stream)
        stream.close()
    else:
        return "Sorry, our program not supported this format. Try 'Json' or 'Yaml'"  # noqa: E501
    return file
