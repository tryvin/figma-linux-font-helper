# Figma Font Helper
# Maintainer Vin <github.com/tryvin>
# Copyright 2019 Vin
# MIT License

import os
import re
import subprocess
import sys


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


def __split_if_comma__(value):
    return value.split(",", 1)[0] if value.find(",") > -1 else value


def get_font_list():
    font_list = {}

    allowed_extensions = ('\\.ttf', '\\.ttc', '\\.otf')

    font_shell_command = ["fc-list --format '%%{file} | %%{family} | %%{weight} | %%{style} | %%{postscriptname}\\n' | sort | grep -e '%s'" % (
        "\\|".join(allowed_extensions),
    )]

    new_env = dict(os.environ)
    new_env['LC_ALL'] = 'C'

    font_shell_return = subprocess.run(
        font_shell_command, shell=True, env=new_env, capture_output=True)

    if font_shell_return.returncode == 0:
        stdout_encoding = sys.stdout.encoding

        for font_line in str(font_shell_return.stdout.decode(stdout_encoding)).split("\n"):
            details = font_line.split(" | ")
            if len(details) == 5:
                if details[0] not in font_list:
                    font_list[details[0].strip()] = [{
                        "localizedFamily": __split_if_comma__(details[1]).strip(),
                        "postscript": details[4].strip(),
                        "style": __split_if_comma__(details[3]).strip(),
                        "weight": details[2],
                        "stretch": 5,
                        "italic": True if re.match("Italic|Oblique", details[3]) else False,
                        "family": __split_if_comma__(details[1]).strip(),
                        "localizedStyle": __split_if_comma__(details[3]).strip()
                    }]

    return font_list


if __name__ == "__main__":
    print("Font List:")
    print(get_font_list())
