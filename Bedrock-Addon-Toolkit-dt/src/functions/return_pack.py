"""
imports  
"""

import sys
import shutil
import os
import re

from .base.copy_from_to import *

"""
load temp_pack to output
"""
def return_pack(type):
    path_in="temp/pack"
    path_out="output"
    if type==1:
        print("pack will be zipped")
    
        print("pack is zipped")
    elif type==2:
        print("pack will be copyed")
        copy_from_to(path_in, path_out)
        print("pack is copyed")
    else:
        print("temp is emty load pack")