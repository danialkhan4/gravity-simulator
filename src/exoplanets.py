import pyvo as vo
import pandas as pd

def query_by_selection(exoplanet):

    # Reference: https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
    service = vo.dal.TAPService('https://exoplanetarchive.ipac.caltech.edu/TAP')

    # we need default_flag = 1 because there are multiple sources for data 
    # the ones with default_flag = 1 are the default parameters 
    query = "SELECT * FROM ps WHERE pl_name = '{}' and default_flag = 1".format(exoplanet)

    # Query data and add to pandas dataframe 
    table = pd.DataFrame(service.search(query))

    exoplanet_data = pd.DataFrame({
        'name': table['pl_name'].values[0]
    }, index=[0])
    
    print(exoplanet_data)

query_by_selection('11 Com b')