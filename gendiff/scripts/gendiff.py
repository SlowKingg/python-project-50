import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    return parser.parse_args()


def read_files(args):
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    return file1, file2


def main():
    args = parse_args()

    file1, file2 = read_files(args)

    print(file1)
    print(file2)


if __name__ == "__main__":
    main()
