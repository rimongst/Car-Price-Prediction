# 🚗 Car Price Prediction API

## 📌 Project Overview
This project is a **machine learning-based car price prediction system**, deployed as a RESTful API using **FastAPI**. The model predicts car prices based on user input features, leveraging a trained regression model.

## 📌 Project Structure
```
car_price_prediction/
│── data/                  # Contains dataset (train.csv)
│── models/                # Trained machine learning models (best_model.pkl)
│── notebooks/             # Jupyter Notebook for model training (train.ipynb)
│── src/                   # Core application files
│   │── car_api.py         # FastAPI implementation
│   │── test_api.py        # API testing script
│── requirements.txt       # Dependency list
│── README.md              # Documentation file
│── .gitignore             # Ignored files
```

## 📌 Setup and Installation
### 1️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API
```bash
uvicorn src.car_api:app --host 0.0.0.0 --port 8001 --reload
```
Then, open your browser and visit:
```
http://127.0.0.1:8001/docs
```
This will display the **Swagger UI** for API testing.

## 📌 API Endpoints
### **1️⃣ `GET /`**
- Returns an HTML form for manual input of car details and submission for prediction.

### **2️⃣ `POST /predict`**
- **Input Format** (Form Data):
  ```json
  {
    "levy": 0,
    "prod_year": 2018,
    "leather_interior": 1,
    "engine_volume": 2.5,
    "mileage": 50000,
    "cylinders": 4,
    "doors": 4,
    "airbags": 6,
    "fuel_petrol": 1
  }
  ```
- **Response Format**:
  ```json
  {
    "predicted_price": 15000.0
  }
  ```

## 📌 Testing the API
You can test the API using the included `test_api.py` script:
```bash
python src/test_api.py
```
Or, use `cURL`:
```bash
curl -X 'POST' 'http://127.0.0.1:8001/predict' \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     -d 'levy=0&prod_year=2018&leather_interior=1&engine_volume=2.5&mileage=50000'
```

## 📌 Model Details
- The model is a **machine learning regression model** trained using the `train.csv` dataset.
- The training process is documented in `train.ipynb`.
- The best-performing model is stored in `models/best_model.pkl` and loaded for inference.

## 📌 Deployment (Render)
1. **Initialize GitHub Repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```
2. **Deploy on [Render](https://render.com/)**:
   - Create a new **Web Service**
   - Connect your **GitHub repository**
   - Set the **Start Command**:
     ```bash
     uvicorn src.car_api:app --host 0.0.0.0 --port $PORT
     ```

## 📌 Conclusion
🚀 This project integrates **data science** and **FastAPI** to provide a scalable **car price prediction API**. Further improvements could involve **feature engineering**, **model optimization**, and **database integration** to enhance performance.

