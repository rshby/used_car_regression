from fastapi import FastAPI
from Controllers import car
import uvicorn

app = FastAPI()

#route API yang digunakan untuk test
@app.get("/test")
async def showTest():
    try:
        data = {
            "message": "success API"
        }
        return data
    except Exception as e:
        print("gagal")

#route API yang digunakan untuk melihat semua data
@app.get("/data")
async def showAllDatas():
    try:
        return car.showData()
    except Exception as e:
        print(f"kesalahan function API showAllDatas: e")


if __name__ == "__main__":
    uvicorn.run("app:app", port=8005, reload=True)