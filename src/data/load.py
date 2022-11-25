import datetime
import pandas as pd
import yfinance as yf

def load_data() -> pd.DataFrame:
    # Get current date
    today = datetime.date.today()

    # Download S&P data
    df_spy = yf.download('SPY', start='1993-02-01', end=today)
    
    return df_spy