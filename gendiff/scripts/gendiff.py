from gendiff import generate_diff, parse_args, read_files


def main():
    args = parse_args()
    file1, file2 = read_files(args)
    print(generate_diff(file1, file2))


if __name__ == "__main__":
    main()
