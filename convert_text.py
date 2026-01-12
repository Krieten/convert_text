#!/usr/bin/env python3

import sys
from os import listdir, path
from os.path import exists
from sys import argv

from fpdf import FPDF


def main(path_to_files, file_type="html", capital=""):
    file_type, capital = arg_validation(path_to_files, file_type, capital)
    txt_files = filter_txt_files(path_to_files)
    for file in txt_files:
        with open(file, "r") as f:
            content = f.read()
        if capital:
            content = content.upper()
        if file_type == "html":
            to_html(file, content)
        else:
            to_pdf(file, content)
    sys.exit(0)


def to_html(file, content):
    filename = path.basename(file)
    clean_name = path.splitext(filename)[0]
    title = clean_name.replace("_", " ")
    output_file = path.join(path.dirname(file), clean_name + ".html")

    with open(output_file, "w") as f:
        f.write(f"""<!DOCTYPE html>
    <html lang="">
    <head>
        <meta charset="UTF-8" />
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>
""")
        for line in content.split("\n"):
            f.write(f"\t\t\t{line}<br>\n")
        f.write("""\t\t</p>
    </body>
</html>
""")


def to_pdf(file, content):
    filename = path.basename(file)
    clean_name = path.splitext(filename)[0]
    title = clean_name.replace("_", " ")
    output_file = path.join(path.dirname(file), clean_name + ".pdf")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(0, 10, title, ln=True)
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)
    pdf.output(output_file)


def show_help():
    print(
        "usage:\t\tconvert_text.py path_to_files [HTML|pdf] [capital]\n"
        "example:\tconvert_text.py ~/Documents/input/ pdf capital"
    )


def filter_txt_files(path_to_files):
    txt_files = []
    for file in listdir(path_to_files):
        if file.endswith(".txt"):
            txt_files.append(path.join(path_to_files, file))
    return txt_files


def arg_validation(path_to_files, file_type, capital):
    if not exists(path_to_files):
        print(f"Invalid path: {path_to_files}")
        show_help()
        sys.exit(1)

    file_type = file_type.lower()
    if file_type != "html" and file_type != "pdf":
        print(f"Invalid filetype: {file_type}")
        show_help()
        sys.exit(1)

    capital = capital.lower()
    if capital == "capital":
        capital = bool(True)
    elif capital == "":
        capital = bool(False)
    else:
        print(f"Invalid Argument: {capital}")
        show_help()
        sys.exit(1)

    return file_type, capital


if __name__ == "__main__":
    if len(argv) == 2:
        main(argv[1])
    elif len(argv) == 3:
        main(argv[1], argv[2])
    elif len(argv) == 4:
        main(argv[1], argv[2], argv[3])
    else:
        show_help()
