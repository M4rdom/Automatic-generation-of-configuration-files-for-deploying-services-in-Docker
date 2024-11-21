import os
import UVengine
from pathlib import Path



CURRENT_PATH = Path(__file__).resolve().parent
#print(CURRENT_PATH)


#Entrada Para Dockerfile
CONFIGURATION_PATH = os.path.join('Dockerfile_fm.uvl.json')


# CONSTANTS
FM_MODEL_PATH = os.path.join('Templates','dockerfile','Latest','Feature Models','dockerfile_fm.uvl')
TEMPLATE_PATH = os.path.join('Templates','dockerfile','Latest','Jinja Templates','dockerfile.jinja')
MAPPING_MODEL_PATH = os.path.join('Templates','dockerfile','Latest','Mapping Model','dockerfile_mapping_model.csv')


if __name__ == '__main__':

    configuration_path = CONFIGURATION_PATH

    fm_model_path = FM_MODEL_PATH
    template_path = TEMPLATE_PATH
    mapping_model_path = MAPPING_MODEL_PATH
    
    
    
    vengine = UVengine.VEngine()
    vengine.load_configuration(configuration_path)
    vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)

    
    
    result = vengine.resolve_variability()
    
    
    
    
    print(result)
    with open('dockerfile', 'w' ,encoding="utf-8") as file:
        file.write(result)