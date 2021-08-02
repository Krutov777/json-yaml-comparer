import pytest

from gendiff import parser


def test_json_parse():
    json_path = 'tests/fixtures/before.json'
    expected = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": True,
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}

    assert parser.read_file(json_path) == expected


def test_yaml_parse():
    yaml_path = 'tests/fixtures/before.yaml'
    expected = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": True,
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}

    assert parser.read_file(yaml_path) == expected