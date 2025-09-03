import argparse


def parse_args():
    """
    Parses command-line arguments for the gendiff utility.

    Returns:
        argparse.Namespace: An object containing the parsed arguments:
            - first_file (str): Path to the first configuration file.
            - second_file (str): Path to the second configuration file.
            - format (str): Output format for the difference.
                            Choices are "plain", "stylish", or "json".
                            Defaults to "stylish".
    """

    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        metavar="[type]",
        choices=["plain", "stylish", "json"],
        default="stylish",
        help='output format (default: "%(default)s")',
    )

    return parser.parse_args()
