
import json
import os
import pytest

from gendiff.formatters import json as json_formatter
from gendiff.formatters import plain, text
from gendiff.generate_diff import generate_diff


def test_text_json_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_func=text.format_dict,
    )
    assert diff.split('\n') == expected_text_result


def test_yaml_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.yaml',
        'tests/fixtures/after.yaml',
        format_func=text.format_dict,
    )
    assert diff.split('\n') == expected_text_result


def test_json_yaml_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.yaml',
        format_func=text.format_dict,
    )
    assert diff.split('\n') == expected_text_result


def test_plain_format(expected_plain_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_func=plain.format_dict,
    )
    assert sorted(diff.split('\n')) == sorted(expected_plain_result)


def test_json_format(expected_json_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_func=json_formatter.format_dict,
    )
    assert json.loads(diff) == expected_json_result


@pytest.fixture
def expected_text_result():
    with open('tests/fixtures/expected_text.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_plain_result():
    with open('tests/fixtures/expected_plain.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_json_result(request):
    file_path = os.path.join(
        request.fspath.dirname,
        'fixtures',
        'expected_json.json'
    )
    with open(file_path) as file:
        yield json.load(file)
