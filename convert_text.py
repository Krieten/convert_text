#!/usr/bin/env python3

import sys
from os.path import exists
from sys import argv


def main(path_to_files, file_type="html", capital=""):
    file_type, capital = arg_validation(path_to_files, file_type, capital)
    sys.exit(0)


def arg_validation(path_to_files, file_type, capital):
    if not exists(path_to_files):
        print(f"Invalid path: {path_to_files}")
        sys.exit(1)

    file_type = file_type.lower()
    if file_type != "html" and file_type != "pdf":
        print(f"Invalid filetype: {file_type}")
        sys.exit(1)

    capital = capital.lower()
    if capital == "capital":
        capital = bool(True)
    elif capital == "":
        capital = bool(False)
    else:
        print(f"Invalid Argument: {capital}")
        sys.exit(1)

    return file_type, capital


if __name__ == "__main__":
    if len(argv) == 2:
        main(argv[1])
    elif len(argv) == 3:
        main(argv[1], argv[2])
    elif len(argv) == 4:
        main(argv[1], argv[2], argv[3])
