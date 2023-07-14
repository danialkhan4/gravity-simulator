import pyvo as vo
import math
import os
import constants

def load_exoplanet_data():

    planets = []

    # Reference: https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
    service = vo.dal.TAPService('https://exoplanetarchive.ipac.caltech.edu/TAP')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    query_list = None
    with open(os.path.join(current_dir, 'exoplanets.txt')) as f:
        query_list = f.read().splitlines()

    query_list = tuple(query_list)
    # we need default_flag = 1 because there are multiple sources for data 
    # the ones with default_flag = 1 are the default parameters 
    query = "SELECT pl_name, pl_masse FROM ps WHERE default_flag = 1 and pl_name IN {}".format(query_list)

    # Query data
    table = service.search(query)

    planets.append(('Earth', 1))
    for item in table:
        if math.isnan(item['pl_masse']):
            print("No mass available for ", item['pl_name'])
        else:
            planets.append((item['pl_name'], item['pl_masse']))

    print("Loaded planet data", planets)
    return planets
