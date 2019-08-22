# Figma Font Helper
# Maintainer Vin <github.com/tryvin>
# Copyright 2019 Vin
# MIT License

import re
import subprocess
import os


def is_valid_origin(origin):
    if origin is None:
        return True

    if origin.endswith("/"):
        origin = origin[:-1]

    return re.match(
        (
            '^https?:\\/\\/(?:(?:\\w+\\.)?figma.com|localhost|'
            '127\\.0\\.0\\.1)(?::\\d+)?$'
        ),
        origin
    )


def get_font_list():
    font_list = {}
    font_shell_command = "fc-list --format '%{file} | %{family} | %{weight} | %{style} | %{postscriptname}\n' | sort | grep -e '\.ttf\|\.ttc\|\.otf'"

    for font_line in subprocess.getoutput(font_shell_command).split("\n"):
        details = font_line.split(" | ")

        if details[0] not in font_list:

            font_list[details[0].strip()] = [{
                "localizedFamily": details[1].split(",", 1)[0].strip(),
                "postscript": details[4].strip(),
                "style": details[3].split(",", 1)[0].strip(),
                "weight": details[2],
                "stretch": 5,
                "italic": True if re.match("Italic|Oblique", details[3]) else False,
                "family": details[1].split(",", 1)[0].strip(),
                "localizedStyle": details[3].split(",", 1)[0].strip()
            }]

    return font_list


if __name__ == "__main__":
    print("Font List:")
    print(get_font_list())
