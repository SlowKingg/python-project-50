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


def generate_diff(file1, file2):
    result = ""
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    for key in all_keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += f"  {key}: {file1[key]}\n"
            else:
                result += f"- {key}: {file1[key]}\n+ {key}: {file2[key]}\n"
        elif key in file1:
            result += f"- {key}: {file1[key]}\n"
        else:
            result += f"+ {key}: {file2[key]}\n"
    return "{\n" + result + "}"


def main():
    args = parse_args()

    file1, file2 = read_files(args)

    print(generate_diff(file1, file2))


if __name__ == "__main__":
    main()
