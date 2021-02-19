#!/usr/bin/env python3
import json


def read_file(file_path):
    file = json.load(open(file_path))
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
        elif json2.get(key, None) == None:
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
