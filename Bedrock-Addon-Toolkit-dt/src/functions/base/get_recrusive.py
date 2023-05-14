import json
import os
import shutil
from os.path import isfile, join

def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []
    keys=[]

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)
            keys.append([key])

        elif isinstance(value, dict):
            results,recurKeys = get_recursively(value, field)
            for result in results:
                fields_found.append(result)
            for recurKey in recurKeys:
                tempKey=[key]
                tempKey+=recurKey
                keys.append(tempKey)

        elif isinstance(value, list):
            for ind in range(len(value)):
                item=value[ind]
                if isinstance(item, dict):
                    more_results,more_recurKeys = get_recursively(item, field)
                    
                    for another_result in more_results:
                        fields_found.append(another_result)
                    for more_recurkey in more_recurKeys:
                        tempKey=[ind]
                        tempKey+=more_recurkey
                        keys.append(tempKey)
                        

    return fields_found, keys