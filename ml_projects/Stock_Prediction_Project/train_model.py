import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Create dummy dataset
np.random.seed(42)

rows = 1000

df = pd.DataFrame({
    "Open": np.random.uniform(100, 500, rows),
    "High": np.random.uniform(100, 500, rows),
    "Low": np.random.uniform(100, 500, rows),
    "Close": np.random.uniform(100, 500, rows),
    "Volume": np.random.uniform(100000, 1000000, rows),
})

df["MA10"] = df["Close"].rolling(10).mean()
df["MA50"] = df["Close"].rolling(50).mean()
df["EMA10"] = df["Close"].ewm(span=10).mean()
df["Return"] = df["Close"].pct_change()
df["High_Low_Diff"] = df["High"] - df["Low"]

df.dropna(inplace=True)

X = df[[
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "MA10",
    "MA50",
    "EMA10",
    "Return",
    "High_Low_Diff"
]]

# Dummy target
y = np.random.uniform(-0.05, 0.05, len(X))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("model.pkl and scaler.pkl created successfully")