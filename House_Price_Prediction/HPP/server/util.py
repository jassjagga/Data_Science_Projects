import pickle
import json
import sklearn
import numpy as np

__loactions=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath,story):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index= -1

    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    x[3]=story
    if loc_index >=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __loactions

def load_saved_artifacts():
    print("loading saved artifacts,,,,,start")
    global __data_columns
    global __loactions

    with open("./artifacts/columns.json","r") as f:
        __data_columns= json.load(f)["data_columns"]
        __loactions = __data_columns[4:]

    global __model
    with open("./artifacts/House_price_prediction.pickle","rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts ... done")

if  __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("blmngtn",1000,3,2,1))
    print(get_estimated_price("clearcr",1000,3,2,1))
    print(get_estimated_price("Blueste",1000,2,2,1)) #other location