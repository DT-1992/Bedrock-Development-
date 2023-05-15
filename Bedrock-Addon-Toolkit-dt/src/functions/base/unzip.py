import os
from zipfile import ZipFile 
from .files_in_path import *
"""
unzip  from   to  
"""

def unzip_from_to(path_in,path_out ):

            with ZipFile(path_in, 'r') as  zip_ref:
                zip_ref.extractall(path_out)
