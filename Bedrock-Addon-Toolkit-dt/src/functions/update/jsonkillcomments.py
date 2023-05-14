def loadJsonKillComments(jsonFile):
    data=""
    with open(jsonFile, 'r+') as f:
        
        for line in f:
            data+=line
    data=re.sub("\/\/[^\n]*\n", '', data )
    data = json.loads(data)
    return data
