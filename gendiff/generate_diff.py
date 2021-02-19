#!/usr/bin/env python3
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


def get_diff(file_path1, file_path2):
    json1 = read_file(file_path1)
    json2 = read_file(file_path2)
    keys_json1 = sorted(list(json1.keys()))
    list_str = []
    for key in keys_json1:
        if json2.get(key, None) == json1.get(key):
            string = '    {}: {}'.format(key, json1.get(key))
            list_str.append(string)
            json2.pop(key)
        elif json2.get(key, None) is None:
            string = '  - {}: {}'.format(key, json1.get(key))
            list_str.append(string)
        else:
            string = '  - {}: {}'.format(key, json1.get(key))
            list_str.append(string)
            string = '  + {}: {}'.format(key, json2.get(key))
            list_str.append(string)
            json2.pop(key)
    keys_json2 = sorted(list(json2.keys()))
    for key in keys_json2:
        string = '  + {}: {}'.format(key, json2.get(key))
        list_str.append(string)
    result = '{\n' + '\n'.join(list_str) + '\n}'
    return result


def output(args):
    print(get_diff(args.first_file, args.second_file))
