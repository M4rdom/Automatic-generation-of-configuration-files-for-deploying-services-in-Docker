import os
import zipfile
import json
from flask import Flask, jsonify, request
import UVengine
import requests
from pathlib import Path
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#Development URLs
URL_UVENGINE_RESOLVER = "http://localhost:5001"
URL_REPOSITORY_MANAGER = "http://localhost:5000"
URL_FRONTEND = "http://localhost:4200"  

#Production URLs
URL_REPOSITORY_MANAGER = "http://repository-manager:5000"

CURRENT_PATH = Path(__file__).resolve().parent


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
            return "No se ha podido resolver:"+ str(e), 500

        response = {
            "result": result
        }
        
        return jsonify(response)
    except Exception as e:
        return str(e), 500


def download_and_extract_file():
    file_url = f'{URL_REPOSITORY_MANAGER}/repository-manager/download-repo'
    local_filename = 'templates.zip'
    
    templates_dir = os.path.join(os.getcwd(), 'Templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
    
    local_filepath = os.path.join(templates_dir, local_filename)
    
    # Descargar el archivo
    response = requests.get(file_url)
    with open(local_filepath, 'wb') as f:
        f.write(response.content)
    
    print(f"File downloaded and saved as {local_filepath}")
    
    # Descomprimir el archivo
    with zipfile.ZipFile(local_filepath, 'r') as zip_ref:
        zip_ref.extractall(templates_dir)
    
    print(f"File extracted to {templates_dir}")
    

if __name__ == '__main__':
    download_and_extract_file()
    app.run(debug=True, port=5001)