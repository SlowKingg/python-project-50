import argparse


def is_json_files(args):
    return args.first_file.endswith(".json") and args.second_file.endswith(
        ".json"
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    return parser.parse_args()
