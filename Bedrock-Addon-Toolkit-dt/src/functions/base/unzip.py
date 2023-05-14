import os
from zipfile import ZipFile 
from .files_in_path import *
"""
unzip  from   to  
"""

def unzip_from_to(path_in,path_out ):
    name=files_in_path(path_in)
    for root, path_in, files in os.walk(path_in):
        if name in files:
            with ZipFile(path_in, 'r') as  zip_ref:
                zip_ref.extractall(path_out)
