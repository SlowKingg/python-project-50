import sys

from gendiff.arg_parser import parse_args


def test_parse_args(monkeypatch):
    test_args = ["gendiff", "file1.json", "file2.json", "--format", "plain"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parse_args()
    assert args.first_file == "file1.json"
    assert args.second_file == "file2.json"
    assert args.format == "plain"
