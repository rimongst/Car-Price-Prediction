import requests

url = "http://127.0.0.1:8001/predict"
data = {
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

response = requests.post(url, data=data)  # 🔹Use data=data to send the Form format
print(response.json())
