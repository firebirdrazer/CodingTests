import json
import pandas as pd
poi_json = open("./poi_format_data/poi_format.json").read()                         #read the cource file
poi_all = json.loads(poi_json)                                                      #convert to Python dictionary format
poi=[]
for p in poi_all:                                                                   #for each element in the dictionary
    try:                                                                            #get the name from "name", even if it is empty
        name = p['tags']['name']
    except KeyError:                                                                #if there's no "name"
        try:                                                                        #then get the "name:ja"
            name = p['tags']['name:ja']
        except KeyError:
            try:                                                                    #then the "name:en", because the above keys are appeared sometimes
                name = p['tags']['name:en']
            except KeyError:                                                        #if there's no name keys
                name = '__noname__'                                                 #give it a "noname"
    try:                                                                            #filter the target from tags
        if (p['tags']['amenity'] in ['cafe','fastfood','biergarten','bar','pub']):  #if it has a tag of "amenity" with desired values
            poi.append([p['latitude'],p['longitude'],name])                         #append it to the list
    except KeyError:                                                                #if there's no "amenity" tag
        try:
            if p['tags']['railway'] == 'station':                                   #then test it with a "railway" tag
                poi.append([p['latitude'],p['longitude'],name])                     #append it if it's a station
        except KeyError:                                                            #if there's no "amenity" or "railway" tags
            continue                                                                #just skip it

poi_df = pd.DataFrame(poi)
poi_df.columns = ['latitude','longitude','name']                                    #set the column names
poi_df.to_csv("./poi_format_data/poi_format_result.csv",index=False)                #output the result file