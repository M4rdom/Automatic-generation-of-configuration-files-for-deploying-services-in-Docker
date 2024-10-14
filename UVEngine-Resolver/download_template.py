from constant import URL_REPOSITORY_MANAGER
import requests
import time
import zipfile
import os

def download_and_extract_file():
    file_url = f'{URL_REPOSITORY_MANAGER}/repository-manager/download-repo'
    local_filename = 'templates.zip'
    
    templates_dir = os.path.join(os.getcwd(), 'Templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
    
    local_filepath = os.path.join(templates_dir, local_filename)
    
    # Intentar descargar el archivo hasta que el servidor esté disponible
    while True:
        try:
            response = requests.get(file_url)
            response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
            break  # Salir del bucle si la petición fue exitosa
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con el servidor: {e}. \n Reintentando en 5 segundos...")
            time.sleep(5)  # Esperar 5 segundos antes de reintentar
    
    # Guardar el archivo descargado
    with open(local_filepath, 'wb') as f:
        f.write(response.content)
    
    print(f"File downloaded and saved as {local_filepath}")
    
    # Descomprimir el archivo
    with zipfile.ZipFile(local_filepath, 'r') as zip_ref:
        zip_ref.extractall(templates_dir)
    
    print(f"File extracted to {templates_dir}")

download_and_extract_file()