import json


def read_files(args):  # pragma: no cover
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
