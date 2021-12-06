import json
def getAirportData():
    airportList=[]
    with open('data.json') as f:
        data=json.load(f)
        #print(data)
        #print(data['array'])
    airportList=data['array']
    return airportList