import os
from os import listdir
from os import path
from os.path import isfile, join

def files_in_path(path):
    result = []
    for root, dirs, files in os.walk(path):
        result.append(os.path.join(root))
    return result