import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def predict_stock(ticker, days):
    df = yf.download(ticker, period="1y")

    if df.empty:
        return [], 0, []

    df = df[['Close']]
    df['Prediction'] = df[['Close']].shift(-days)

    X = np.array(df.drop(['Prediction'], axis=1))[:-days]
    y = np.array(df['Prediction'])[:-days]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    x_forecast = np.array(df.drop(['Prediction'], axis=1))[-days:]
    forecast = model.predict(x_forecast)

    accuracy = model.score(X_test, y_test)

    historical = df['Close'].tail(30).tolist()

    return forecast.tolist(), float(accuracy), historical