import pandas as pd
import pickle

model = pickle.load(open(r"C:\Users\ROG\Documents\used_car_regression\model\model_regresi_rf.pkl", 'rb'))
data = pd.read_feather(r"C:\Users\ROG\Documents\used_car_regression\dataset\carUsedPriceFix.feather").to_dict(orient="records")


def showData():
    try:
        return data
    except Exception as e:
        print(f"kesalahan function showData: {e}")

def prediksi(**params):
    try:
        data = [[
            str(params["model"]),
            int(params["year"]),
            str(params["transmission"]),
            int(params["mileage"]),
            str(params["fuelType"]),
            float(params["tax"]),
            float(params["mpg"]),
            float(params["engineSize"])
        ]]
        dataTest = pd.DataFrame(data, index=[0], columns=["model", "year", "transmission", "mileage", "fuelType", "tax", "mpg", "engineSize"])
        hasilPrediksi = model.predict(dataTest)[0]
        return float(hasilPrediksi)
    except Exception as e:
        print(f"keslahan function prediksi: {e}")