from gendiff import (
    generate_diff,
    is_json_files,
    parse_args,
    read_json_files,
    read_yaml_files,
)


def main():
    args = parse_args()

    if is_json_files(args):
        file1, file2 = read_json_files(args)
    else:
        file1, file2 = read_yaml_files(args)

    print(generate_diff(file1, file2))


if __name__ == "__main__":
    main()
