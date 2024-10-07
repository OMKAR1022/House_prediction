import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

__locations =None
__data_col =None
__model = None

def get_prediction_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_col.index(location.lower())

    except:
        loc_index =-1

    x = np.zeros(len(__data_col))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk


    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading artifacts >>>> start")
    global  __data_col
    global  __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_col = json.load(f)['data_columns']
        __locations = __data_col[3:]
    global __model
    with open("./artifacts/house_prediction_banglore.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved >>>> Done")


if __name__ =='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_prediction_price('1st phase jp nagar',1000,3,3))
    print(get_prediction_price('1st phase jp nagar',1400,3,3))
    print(get_prediction_price('Pune',1000,2,3))
