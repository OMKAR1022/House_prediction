import json
import pickle
__locations =None
__data_col =None
__model = None



def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading artifacts >>>> start")
    global  __data_col
    global  __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_col = json.load(f)['data_columns']
        __locations = __data_col[3:]

    with open("./artifacts/house_prediction_banglore.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved >>>> Done")


if __name__ =='__main__':
    load_saved_artifacts()
    print(get_location_names())