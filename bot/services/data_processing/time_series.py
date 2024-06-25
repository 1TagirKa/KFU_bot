import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import IsolationForest

def analyze_resolution_time(data):
    df = pd.DataFrame(data)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['resolution_time'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60

    stats = df['resolution_time'].describe()
    return stats

def detect_anomalies(df, column):
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[[column]])
    return df[df['anomaly'] == -1]

def forecast_resolution_time(df, column, periods):
    model = ARIMA(df[column], order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=periods)
    return forecast
