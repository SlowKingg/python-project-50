import json

from gendiff import generate_diff


def test_generate_diff_simple():
    file1 = json.load(open("tests/test_data/file1.json"))
    file2 = json.load(open("tests/test_data/file2.json"))

    expected = (
        "{\n- follow: False\n"
        "  host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50\n"
        "+ timeout: 20\n"
        "+ verbose: True\n}"
    )

    assert generate_diff(file1, file2) == expected
