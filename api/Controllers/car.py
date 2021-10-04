import pandas as pd
import pickle

# import model prediksi
model = pickle.load(open(r"C:\Users\ROG\Documents\used_car_regression\model\model_regresi_rf.pkl", 'rb'))

# semua data dalam bentuk feather
data = pd.read_feather(r"C:\Users\ROG\Documents\used_car_regression\dataset\carUsedPriceFix.feather").to_dict(orient="records")

# function yang digunakan untuk melihat semua data
def showData():
    try:
        return data
    except Exception as e:
        print(f"kesalahan function showData: {e}")

# function yang digunakan untuk memprediksi berdasarkan data
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