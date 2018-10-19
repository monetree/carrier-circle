import pathlib
import requests
import shutil
from .models import *


def create_delete_pdf_dir(pdf_dir):
    try:
        shutil.rmtree(pdf_dir)
    except FileNotFoundError:
        pass
    try:
        pathlib.Path(pdf_dir).mkdir(parents=True, exist_ok=True)
    except FileNotFoundError:
        pass

def download_pdf(pdf_url,pdf_file_name):
    get_url = requests.get(pdf_url)
    with open(pdf_file_name,'wb') as pdf:
        pdf.write(get_url.content)
