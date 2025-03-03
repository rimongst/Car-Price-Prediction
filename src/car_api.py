from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
import uvicorn
import requests
import os

app = FastAPI(title="Car Price Prediction API",
              description="Predict car price based on input features")

model_path = os.path.join(os.getcwd(), "best_model.pkl")
print(f"Looking for model at: {model_path}")

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    model = None
    print(f"Warning: Failed to load model. Error: {str(e)}")

@app.get("/", response_class=HTMLResponse)
def form_page():
    return """
    <html>
        <head>
            <title>Car Price Prediction</title>
        </head>
        <body>
            <h2>Enter Car Details</h2>
            <form action="/predict" method="post">
                Levy: <input type="text" name="levy"><br>
                Prod Year: <input type="text" name="prod_year"><br>
                Leather Interior: <input type="text" name="leather_interior"><br>
                Engine Volume: <input type="text" name="engine_volume"><br>
                Mileage: <input type="text" name="mileage"><br>
                Cylinders: <input type="text" name="cylinders"><br>
                Doors: <input type="text" name="doors"><br>
                Airbags: <input type="text" name="airbags"><br>
                Wheel Left Wheel: <input type="text" name="wheel_left_wheel"><br>
                Wheel Right-Hand Drive: <input type="text" name="wheel_right_hand_drive"><br>
                Drive 4x4: <input type="text" name="drive_4x4"><br>
                Drive Front: <input type="text" name="drive_front"><br>
                Drive Rear: <input type="text" name="drive_rear"><br>
                Gear Automatic: <input type="text" name="gear_automatic"><br>
                Gear Manual: <input type="text" name="gear_manual"><br>
                Gear Tiptronic: <input type="text" name="gear_tiptronic"><br>
                Gear Variator: <input type="text" name="gear_variator"><br>
                Fuel CNG: <input type="text" name="fuel_cng"><br>
                Fuel Diesel: <input type="text" name="fuel_diesel"><br>
                Fuel Hybrid: <input type="text" name="fuel_hybrid"><br>
                Fuel Hydrogen: <input type="text" name="fuel_hydrogen"><br>
                Fuel LPG: <input type="text" name="fuel_lpg"><br>
                Fuel Petrol: <input type="text" name="fuel_petrol"><br>
                Fuel Plug-in Hybrid: <input type="text" name="fuel_plugin_hybrid"><br>
                Turbo: <input type="text" name="turbo"><br>
                Color Num: <input type="text" name="color_num"><br>
                Category Num: <input type="text" name="category_num"><br>
                Model Num: <input type="text" name="model_num"><br>
                Manufacturer Num: <input type="text" name="manufacturer_num"><br>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

@app.post("/predict")
def predict(
    levy: float = Form(...),
    prod_year: int = Form(...),
    leather_interior: int = Form(...),
    engine_volume: float = Form(...),
    mileage: float = Form(...),
    cylinders: float = Form(...),
    doors: int = Form(...),
    airbags: int = Form(...),
    wheel_left_wheel: int = Form(...),
    wheel_right_hand_drive: int = Form(...),
    drive_4x4: int = Form(...),
    drive_front: int = Form(...),
    drive_rear: int = Form(...),
    gear_automatic: int = Form(...),
    gear_manual: int = Form(...),
    gear_tiptronic: int = Form(...),
    gear_variator: int = Form(...),
    fuel_cng: int = Form(...),
    fuel_diesel: int = Form(...),
    fuel_hybrid: int = Form(...),
    fuel_hydrogen: int = Form(...),
    fuel_lpg: int = Form(...),
    fuel_petrol: int = Form(...),
    fuel_plugin_hybrid: int = Form(...),
    turbo: int = Form(...),
    color_num: int = Form(...),
    category_num: int = Form(...),
    model_num: int = Form(...),
    manufacturer_num: int = Form(...)
):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    input_data = pd.DataFrame({
        'Levy': [levy],
        'Prod. year': [prod_year],
        'Leather interior': [leather_interior],
        'Engine volume': [engine_volume],
        'Mileage': [mileage],
        'Cylinders': [cylinders],
        'Doors': [doors],
        'Airbags': [airbags],
        'Wheel_Left wheel': [wheel_left_wheel],
        'Wheel_Right-hand drive': [wheel_right_hand_drive],
        'Drive_4x4': [drive_4x4],
        'Drive_Front': [drive_front],
        'Drive_Rear': [drive_rear],
        'Gear_Automatic': [gear_automatic],
        'Gear_Manual': [gear_manual],
        'Gear_Tiptronic': [gear_tiptronic],
        'Gear_Variator': [gear_variator],
        'Fuel_CNG': [fuel_cng],
        'Fuel_Diesel': [fuel_diesel],
        'Fuel_Hybrid': [fuel_hybrid],
        'Fuel_Hydrogen': [fuel_hydrogen],
        'Fuel_LPG': [fuel_lpg],
        'Fuel_Petrol': [fuel_petrol],
        'Fuel_Plug-in Hybrid': [fuel_plugin_hybrid],
        'Turbo': [turbo],
        'Color_num': [color_num],
        'Category_num': [category_num],
        'Model_num': [model_num],
        'Manufacturer_num': [manufacturer_num]
    })

    try:
        prediction = model.predict(input_data)
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

# Test the API locally
if __name__ == "__main__":
    sample_data = {
        "levy": 0,
        "prod_year": 2018,
        "leather_interior": 1,
        "engine_volume": 2.5,
        "mileage": 50000,
        "cylinders": 4,
        "doors": 4,
        "airbags": 6,
        "wheel_left_wheel": 1,
        "wheel_right_hand_drive": 0,
        "drive_4x4": 0,
        "drive_front": 1,
        "drive_rear": 0,
        "gear_automatic": 1,
        "gear_manual": 0,
        "gear_tiptronic": 0,
        "gear_variator": 0,
        "fuel_cng": 0,
        "fuel_diesel": 0,
        "fuel_hybrid": 0,
        "fuel_hydrogen": 0,
        "fuel_lpg": 0,
        "fuel_petrol": 1,
        "fuel_plugin_hybrid": 0,
        "turbo": 0,
        "color_num": 3,
        "category_num": 2,
        "model_num": 15,
        "manufacturer_num": 8
    }
    response = requests.post("http://127.0.0.1:8001/predict", json=sample_data)
    print(response.json())
