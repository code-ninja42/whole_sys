from fastapi import FastAPI
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Load model + scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Stock Prediction API Running"}

@app.get("/predict/{symbol}")
def predict(symbol: str):

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        return {"error": "Invalid symbol or API issue"}

    df = pd.DataFrame(data["Time Series (Daily)"]).T

    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })

    df = df.astype(float)
    df = df.sort_index()

    # Features
    df["MA10"] = df["Close"].rolling(10).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["EMA10"] = df["Close"].ewm(span=10).mean()
    df["Return"] = df["Close"].pct_change()
    df["High_Low_Diff"] = df["High"] - df["Low"]

    df.dropna(inplace=True)

    latest = df.iloc[-1]

    input_data = [[
        latest["Open"],
        latest["High"],
        latest["Low"],
        latest["Close"],
        latest["Volume"],
        latest["MA10"],
        latest["MA50"],
        latest["EMA10"],
        latest["Return"],
        latest["High_Low_Diff"]
    ]]

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)[0]

    current_price = float(latest["Close"])
    predicted_price = current_price * (1 + prediction)

    return {
        "symbol": symbol.upper(),
        "current_price": round(current_price, 2),
        "predicted_price": round(predicted_price, 2),
        "trend": "UP" if prediction > 0 else "DOWN"
    }