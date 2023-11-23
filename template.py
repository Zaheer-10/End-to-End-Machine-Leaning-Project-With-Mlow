# This file is just to make our work easier

# IMPORT LIBRARIES
import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s')
# It  configures the Python logging module to output messages to the console (CLI). The messages will be formatted to include the timestamp and the message itself.

project_name = 'mlproject'

# The folder & files I Need

list_of_files = [
    
    '.github/workflows/.gitkeep' , 
    f'src/{project_name}/__init__.py',
    
    f'src/{project_name}/components/__init__.py',
    
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    
    f'src/{project_name}/pipeline/__init__.py',
    
    f'src/{project_name}/entity/__init__.py',
    
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    
    'config/config.yaml',
    # 'dvc.yaml',
    'params.yaml'
    'schema.yaml',
    
    'main.py',
    'app.py',
    
    'Dockerfile',
    
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'templates/index.html',
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir , file_name = os.path.split(filepath)
    
    if file_dir != "":
        os.makedirs(file_dir , exist_ok=True)
        logging.info(f'Creating a directory - {file_dir} for file : {file_name}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , 'w') as f:
            pass
            logging.info(f'Creating empty file :{filepath}')
            
    else:
        logging.info(f'{file_name} is already exists')

# Note : iterates over a list of file paths and creates directories for the files if they don't already exist. It also creates empty files for any paths that don't have a file with the specified size.

