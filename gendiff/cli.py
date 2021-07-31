#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
from gendiff.formatters import json, plain, text

_FORMATS = {
    'json': json.format_dict,
    'plain': plain.format_dict,
    'text': text.format_dict,
}

def arguments_parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
    '-f',
    '--format',
    dest='FORMAT',
    choices=_FORMATS,
    default='text',
    help='set format of output',
    )
    parser.add_argument('first_file', metavar='FIRST_FILE')
    parser.add_argument('second_file', metavar='SECOND_FILE')
    args = parser.parse_args()
    return args




def main():
    args = arguments_parse()
    diff = generate_diff.generate_diff(args.first_file, args.second_filef, format_func=_FORMATS[args.FORMAT])
    print(diff)


if __name__ == '__main__':
    main()