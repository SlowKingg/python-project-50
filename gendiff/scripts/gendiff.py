from gendiff import generate_diff, parse_args


def main():
    args = parse_args()
    file1_path = args.first_file
    file2_path = args.second_file
    format_name = args.format

    print(generate_diff(file1_path, file2_path, format_name))


if __name__ == "__main__":
    main()
