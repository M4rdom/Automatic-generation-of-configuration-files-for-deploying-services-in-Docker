import asyncio
import io
import requests
import aiohttp  
from flask import Flask, jsonify ,send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GITHUB_TEMPLATES_URL='https://github.com/M4rdom/Templates/archive/refs/heads/main.zip'
GITHUB_API_URL = 'https://api.github.com/repos/M4rdom/Templates/contents'
GITHUB_RAW_API_URL = 'https://raw.githubusercontent.com/M4rdom/Templates/main'

#Development URLs
#URL_UVENGINE_RESOLVER = "http://localhost:5001"
#URL_REPOSITORY_MANAGER = "http://localhost:5000"
#URL_FRONTEND = "http://localhost:4200"  

#Production URLs
URL_UVENGINE_RESOLVER = "http://uvengine-resolver:5001"

@app.route('/repository-manager/')
def index():
    return 'Repository Manager is running'

@app.route('/repository-manager/status')
def status():
    return 'Repository Manager is running'

@app.route('/repository-manager/templates', methods=['GET'])
def list_templates():
    try:
        # Petición sincrónica a la API de GitHub
        response = requests.get(GITHUB_API_URL)

        # Ejecuta la notificación de manera asíncrona sin bloquear el flujo
        asyncio.run(notify_uvengineresolver())

        if response.status_code == 200:
            contents = response.json()
            directories = [item['name'] for item in contents if item['type'] == 'dir']
            return jsonify(directories)
        else:
            return jsonify({'error': 'No se pudo obtener el contenido del repositorio'}), response.status_code 
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/repository-manager/<directory_name>/Versions', methods=['GET'])
def list_versions(directory_name):
    try:
        response = requests.get(GITHUB_API_URL+f'/{directory_name}')

        if response.status_code == 200:
            contents = response.json()

            directories = [item['name'] for item in contents if item['type'] == 'dir']

            return jsonify(directories)

        else:
            return jsonify({'error': 'No se pudo obtener el contenido del repositorio'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/repository-manager/<directory_name>/<version>/FeatureModel', methods=['GET'])
def download_uvl(directory_name, version):
    try:
        file_url = f'{GITHUB_RAW_API_URL}/{directory_name}/{version}/Feature Model/{directory_name}_fm.uvl'
        
        # Hacemos una solicitud GET a la URL del archivo
        response = requests.get(file_url)

        if response.status_code == 200:
            # Crear un objeto BytesIO para enviar el archivo como respuesta
            file_stream = io.BytesIO(response.content)
            return send_file(file_stream, as_attachment=True, download_name=f'{directory_name}_fm.uvl')
        else:
            return jsonify({'error': 'No se pudo descargar el archivo'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/repository-manager/download-repo', methods=['GET'])
def download_repo():
    try:
        
        # Hacemos una solicitud GET a la URL del archivo ZIP
        response = requests.get(GITHUB_TEMPLATES_URL)
        
        if response.status_code == 200:
            # Crear un objeto BytesIO para enviar el archivo como respuesta
            zip_stream = io.BytesIO(response.content)
            return send_file(zip_stream, as_attachment=True, download_name='Templates.zip')
        else:
            return jsonify({'error': 'No se pudo descargar el repositorio'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


async def notify_uvengineresolver():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{URL_UVENGINE_RESOLVER}/uvengine-resolver/update-repo') as response:
                return response.status  # Retorna el código de estado de la respuesta
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)