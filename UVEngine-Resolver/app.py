import os
import time
import zipfile
import json
import traceback
from flask import Flask, jsonify, request
import UVengine
import requests
from pathlib import Path
from flask_cors import CORS

from constant import URL_REPOSITORY_MANAGER, CURRENT_PATH
from download_template import download_and_extract_file

app = Flask(__name__)
CORS(app)



@app.route('/uvengine-resolver/status')
def hello_world():
    return 'UVLEngine resolver is running'

@app.route('/uvengine-resolver/update-repo')
def update():
    download_and_extract_file()
    return 'Templates updated'

@app.route('/uvengine-resolver/Resolver', methods=['POST'])
def Resolver():
    try:
        
        data = request.get_json()
        template:str = data.get('template')
        version:str = data.get('version')

        if not template:
            return 'Template is required', 400
        if not version:
            return 'Version is required', 400
       


        json_filename = 'configuration.json'
        json_filepath = CURRENT_PATH / json_filename
        with open(json_filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        configuration_path = json_filename
        mapping_model_path = CURRENT_PATH/'Templates'/'Templates-main'/template/version/'Mapping Model'/f'{template}_mapping_model.csv'
        template_path = CURRENT_PATH/'Templates'/'Templates-main'/template/version/"Jinja Templates"/f'{template}.jinja'

        if not template_path.exists():
            return f'Template file not found: {template_path}', 400

        vengine = UVengine.VEngine()
        vengine.load_configuration(configuration_path)
        if mapping_model_path:
            vengine.load_mapping_model(mapping_model_path)
        vengine.load_template(template_path)

        try:
            result = vengine.resolve_variability()
        except Exception as e:
            error_message = str(e)
            error_traceback = traceback.format_exc()
            return f"No se ha podido resolver: {error_message}\n{error_traceback}", 500

        response = {
            "result": result
        }
        
        return jsonify(response)
    except Exception as e:
        return str(e), 500



if __name__ == '__main__':
    download_and_extract_file()
    app.run(debug=True, port=5001)