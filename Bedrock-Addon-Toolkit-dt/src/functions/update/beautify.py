from jsbeautifier import beautify_file

def beautify_files(path_in,name,path_out ):
    for root, path_in, files in os.walk(path_in):
        if name in files:
            with beautify_file(path_in, 'r') as  beauty_ref:
                beauty_ref.extractall(path_out)


"""
run beautify over selected pack folder files 
"""
def beautify_Pack(folderPath):
    b_files=find_all_in("*.json",folderPath)
    for bs in b_files:    
        beautify_files(folderPath,bs,folderPath )
    
