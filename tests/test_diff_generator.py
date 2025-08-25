from gendiff import generate_diff


def test_generate_diff_json():
    file1 = "tests/test_data/file1.json"
    file2 = "tests/test_data/file2.json"

    with open("tests/test_data/expected_diff.txt", "r") as f:
        expected = f.read()

    assert generate_diff(file1, file2) == expected


def test_generate_diff_yaml():
    file1 = "tests/test_data/file1.yml"
    file2 = "tests/test_data/file2.yml"

    with open("tests/test_data/expected_diff.txt", "r") as f:
        expected = f.read()

    assert generate_diff(file1, file2) == expected
