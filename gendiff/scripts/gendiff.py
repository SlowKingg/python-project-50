import argparse
import json


def read_files(args):
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    return file1, file2


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    file1, file2 = read_files(args)
    
    print(file1)
    print(file2)


if __name__ == "__main__":
    main()
