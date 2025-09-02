import os

import pytest

from gendiff import generate_diff

STYLISH_FORMAT = 0
PLAIN_FORMAT = 1

cases_plain = [
    (
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "stylish",
        STYLISH_FORMAT,
    ),
    (
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "plain",
        PLAIN_FORMAT,
    ),
    (
        "tests/test_data/file1.yml",
        "tests/test_data/file2.yml",
        "stylish",
        STYLISH_FORMAT,
    ),
    (
        "tests/test_data/file1.yml",
        "tests/test_data/file2.yml",
        "plain",
        PLAIN_FORMAT,
    ),
]

cases_nested = [
    (
        "tests/test_data/file1_nested.json",
        "tests/test_data/file2_nested.json",
        "stylish",
        STYLISH_FORMAT,
    ),
    (
        "tests/test_data/file1_nested.json",
        "tests/test_data/file2_nested.json",
        "plain",
        PLAIN_FORMAT,
    ),
    (
        "tests/test_data/file1_nested.yml",
        "tests/test_data/file2_nested.yml",
        "stylish",
        STYLISH_FORMAT,
    ),
    (
        "tests/test_data/file1_nested.yml",
        "tests/test_data/file2_nested.yml",
        "plain",
        PLAIN_FORMAT,
    ),
]


def get_test_data_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "test_data", file_name)


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


plain_expected_data = read(get_test_data_path("expected_plain.txt")).split(
    "\n\n\n\n"
)
nested_expected_data = read(get_test_data_path("expected_nested.txt")).split(
    "\n\n\n\n"
)


@pytest.mark.parametrize("file1,file2,format,format_index", cases_plain)
def test_plain(file1, file2, format, format_index):
    expected = plain_expected_data[format_index]
    assert generate_diff(file1, file2, format) == expected


@pytest.mark.parametrize("file1,file2,format,format_index", cases_nested)
def test_nested(file1, file2, format, format_index):
    expected = nested_expected_data[format_index]
    assert generate_diff(file1, file2, format) == expected
