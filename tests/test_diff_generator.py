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


def test_generate_diff_nested_json():
    file1 = "tests/test_data/file1_nested.json"
    file2 = "tests/test_data/file2_nested.json"

    with open("tests/test_data/expected_nested_diff.txt", "r") as f:
        expected = f.read()

    print(generate_diff(file1, file2))
    print(expected)

    assert generate_diff(file1, file2) == expected


def test_generate_diff_nested_yaml():
    file1 = "tests/test_data/file1_nested.yml"
    file2 = "tests/test_data/file2_nested.yml"

    with open("tests/test_data/expected_nested_diff.txt", "r") as f:
        expected = f.read()

    assert generate_diff(file1, file2) == expected
