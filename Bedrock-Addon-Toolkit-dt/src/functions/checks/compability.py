def check_compatiblity(Base,Cross):
    path_to_base="base"
    path_to_cross="Cross"
    with ZipFile(Base, 'r') as zipObj:
        zipObj.extractall(path_to_base)
        
    with ZipFile(Cross, 'r') as zipObj:
        zipObj.extractall(path_to_cross)
    result = [y for x in os.walk(path_to_base) for y in glob(os.path.join(x[0], '*.json'))] 
    base_handles=[]
    for file in result:
        print(file)
        data=loadJsonKillComments(file)
        try:
            fields_found, keys=get_recursively(data,"identifier")
        except:
            fields_found=[]
            keys=[]
        base_handles+=fields_found
    result2 = [y for x in os.walk(path_to_cross) for y in glob(os.path.join(x[0], '*.json'))] 
    cross_handles=[]
    for file in result2:
        print(file)
        data=loadJsonKillComments(file)
        try:
            fields_found, keys=get_recursively(data,"identifier")
        except:
            fields_found=[]
            keys=[]
        cross_handles+=fields_found
    print(base_handles)
    print(cross_handles)
    shutil.rmtree(path_to_base)
    shutil.rmtree(path_to_cross)
    return set(base_handles).intersection(set(cross_handles))
