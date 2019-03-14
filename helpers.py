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


def get_font_extra_information(file_name):
    font_extra_info = {}

    file_list = " ".join(["\"" + x + "\"" for x in file_name])

    [font_scan_result_status, font_scan_result] = \
        subprocess.getstatusoutput('fc-scan %s' % (file_list,))

    if font_scan_result_status == 0:
        font_weight = re.findall("weight: (\\d*)", font_scan_result)
        font_style = re.findall("style: \"(.*?)\"", font_scan_result)

        element_index = 0
        for file_element in file_name:
            if len(file_name) > element_index:
                font_extra_info[file_element] = {
                    "weight": font_weight.pop(),
                    "style": font_style.pop()
                }

                element_index = element_index + 1
            else:
                break

    return font_extra_info


def get_font_list():
    font_list = {}

    for font_line in subprocess.getoutput('fc-list').split("\n"):
        [font_file, font_info] = font_line.split(":", 1)
        # Only allows TTF or TTC files, we look at the extension
        # But we could extend this to look for the mime type

        if font_file.endswith(".ttf") or font_file.endswith(".ttc"):
            if font_file not in font_list:
                font_info = font_info.strip()
                font_extra_info = ""

                if font_info.find(",") > -1:
                    [font_family, font_extra_info] = font_info.split(",", 1)
                elif font_info.find(":") > -1:
                    [font_family, font_extra_info] = font_info.split(":", 1)
                else:
                    font_family = font_info

                font_base_name, font_extension = \
                    os.path.splitext(
                        os.path.basename(font_file)
                    )

                font_list[font_file] = [{
                    "localizedFamily": font_family.replace("\\", ""),
                    "postscript": font_base_name.replace(" ", ""),
                    "style": "Regular",
                    "weight": 200,
                    "stretch": 5,
                    "italic": False,
                    "family": font_family.replace("\\", ""),
                    "localizedStyle": "Regular"
                }]

    font_extra_info = get_font_extra_information(list(font_list.keys()))
    for font_extra_info_name in font_extra_info:
        font_list[font_extra_info_name][0]['style'] = \
            font_extra_info[font_extra_info_name]['style']

        font_list[font_extra_info_name][0]['localizedStyle'] = \
            font_extra_info[font_extra_info_name]['style']

        font_list[font_extra_info_name][0]['italic'] = \
            True if \
            font_extra_info[font_extra_info_name]['style'].find("Italic") > -1 \
            else False

        if len(font_extra_info[font_extra_info_name]['weight']) > 0:
            font_list[font_extra_info_name][0]['weight'] = \
                int(font_extra_info[font_extra_info_name]['weight'])

    return font_list


if __name__ == "__main__":
    print("Font List:")
    print(get_font_list())
