from jsonschema import validate

def validate_files(path_in,name,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            res_vali=validate(path_in)

"""
run validate over selected pack folder files 
"""
def validate_Pack(folderPath):
    b_files=find_all_in("*.json",folderPath)
    for bs in b_files:    
        validate(folderPath,bs,folderPath )
    
