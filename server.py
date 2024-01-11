# Figma Font Helper
# Maintainer Vin <github.com/tryvin>
# Copyright 2019 Vin
# MIT License

import io
import os
import sys

from flask import Flask, jsonify, make_response, request, send_file
from flask_cors import CORS

from helpers import get_font_list, is_valid_origin

app = Flask(__name__)
CORS(app, resources={r"/figma/*": {"origins": "*"}})

HTTP_PORT = 18412
HTTPS_PORT = 7335
PROTOCOL_VERSION = 17
FONT_FILES = get_font_list()

# Figma now returns a 403 by default
@app.errorhandler(404)
def answers_with_403(e = None):
    return ('Unauthorized', 403)


@app.route("/figma/version")
def version():
    if is_valid_origin(request.referrer):
        response = make_response(jsonify({
            "version": PROTOCOL_VERSION
        }))

        response.headers['Content-Type'] = 'application/json'

        return response
    else:
        return answers_with_403()


@app.route("/figma/font-files")
def font_files():
    if is_valid_origin(request.referrer):
        response = make_response(jsonify({
            "version": PROTOCOL_VERSION,
            "fontFiles": FONT_FILES
        }))

        response.headers['Content-Type'] = 'application/json'

        return response
    else:
        return answers_with_403()


@app.route("/figma/font-file")
def font_file():
    file_name = request.args.get("file")

    if file_name:
        if file_name in FONT_FILES:
            with open(file_name, 'rb') as bites:
                response = make_response(send_file(
                    io.BytesIO(bites.read()),
                    download_name=os.path.basename(file_name),
                    mimetype='application/octet-stream'
                ))

                response.headers['Content-Type'] = 'application/json'

                return response

    return ('', 404)


@app.route("/figma/update")
def need_update():
    if is_valid_origin(request.referrer):
        response = make_response(jsonify({
            "version": PROTOCOL_VERSION
        }))

        response.headers['Content-Type'] = 'application/json'

        return response
    else:
        return answers_with_403()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "docker-mode":
            hostname = "0.0.0.0"
        else:
            hostname = sys.argv[1]
    else:
        hostname = "127.0.0.1"

    app.run(host=hostname, port=HTTP_PORT)
