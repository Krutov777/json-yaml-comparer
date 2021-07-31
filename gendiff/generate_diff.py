#!/usr/bin/env python3
from gendiff.parser import read_file
from gendiff import dict_diff

def generate_diff(file_path1, file_path2, format_func):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = dict_diff.build_dict_diff(data1, data2)
    return format_func(diff)

'''
def output(args):
    print(get_diff(args.first_file, args.second_file))
'''