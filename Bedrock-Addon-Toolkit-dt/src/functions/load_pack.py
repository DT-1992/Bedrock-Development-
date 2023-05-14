"""
imports  
"""
import sys
import os
import re
import ntpath
from .base.copy_from_to import *
from .base.unzip import *


from tkinter import StringVar
"""
load pack to temp  
"""



def load_pack_zip(path_in,path_out):
    
        print("pack is zip")
        unzip_from_to(path_in,path_out)
        print("extraction done")

def load_pack_folder(path_in,path_out):
    
        print("pack is folder")
        copy_from_to(path_in, path_out)
        print("copy done")
