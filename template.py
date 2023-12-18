import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name='textsummarizer'

list_of_files=[
  '.github/workflows/.gitkeep',#for ci/cd pipelines
  f'src/{project_name}/__init__.py',#if we want to import components from project_name file we do from textsummarizer import... so we need to keep that folder as a local package and if we want to install as a local package we need __init__ constructor file .whenever u do installation of thatfolder it will look for that construction file.so wherever constructor file is present that folder is considered as a local package
  f'src/{project_name}/components/__init__.py',#again local package needed
  f'src/{project_name}/utils/__init__.py',
  f'src/{project_name}/utils/common.py',#utility code written here
  f"src/{project_name}/logging/__init__.py",
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/config/configuration.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constants/__init__.py",
  "config/config.yaml",
  "params.yaml",
  "app.py",
  "main.py",
  "Dockerfile",
  "requirements.txt",
  "setup.py",
  "research/trials.ipynb",

   ]
for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)

  if filedir != "":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory:{filedir} for the file {filename}")

  
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath,'w') as f:
          pass
          logging.info(f"Creating empty file: {filepath}")


  
  else:
      logging.info(f"{filename} is already exists")