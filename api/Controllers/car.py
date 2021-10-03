import pandas as pd

data = pd.read_feather(r"C:\Users\ROG\Documents\used_car_regression\dataset\carUsedPriceFix.feather").to_dict(orient="records")


def showData():
    try:
        return data
    except Exception as e:
        print(f"kesalahan function showData: {e}")