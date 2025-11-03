import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def compute_kpis(df: pd.DataFrame):
    total_sales = df['Sales'].sum()
    avg_order = df['Sales'].mean()
    growth = ((df['Sales'].iloc[-1] - df['Sales'].iloc[0]) / df['Sales'].iloc[0]) * 100
    return total_sales, avg_order, growth

def forecast_sales(df, periods):
    # Ensure Month column is datetime
    df['Month'] = pd.to_datetime(df['Month'])
    df = df.sort_values('Month')

    # Basic numeric time index for regression
    df['t'] = np.arange(len(df))

    # Train simple linear regression model on existing data
    model = LinearRegression()
    model.fit(df[['t']], df['Sales'])

    # Generate future months
    last_date = df['Month'].iloc[-1]
    future_dates = pd.date_range(last_date + pd.offsets.MonthBegin(1), periods=periods, freq='MS')

    # Create time index for forecast period
    future_t = np.arange(len(df), len(df) + periods).reshape(-1, 1)

    # Predict future sales
    future_sales = model.predict(future_t)

    # Build forecast dataframe
    forecast_df = pd.DataFrame({
        'Month': future_dates,
        'Sales': future_sales
    })

    return forecast_df

