import os
from os import listdir
from os import path
from os.path import isfile, join

def find_all_in(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result