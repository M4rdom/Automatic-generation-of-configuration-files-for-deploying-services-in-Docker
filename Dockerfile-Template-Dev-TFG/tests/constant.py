from pathlib import Path


CURRENT_PATH = Path(__file__).resolve().parent

TEMPLATE_PATH      = CURRENT_PATH.parent/'Templates'/'dockerfile'/'Latest'/'Jinja Templates'/'dockerfile.jinja'
MAPPING_MODEL_PATH = CURRENT_PATH.parent/'Templates'/'dockerfile'/'Latest'/'Mapping Model'/'dockerfile_mapping_model.csv'

FRONTEND       = 'FrontEnd'
BACKEND        = 'Backend'
DATABASE       = 'Database'
DATABASESERVER = 'DatabaseServer'
WEBSERVER      = 'WebServer'