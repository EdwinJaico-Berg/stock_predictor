import yfinance as yf

from dash import Dash, html, Input, Output

def render(app: Dash) -> html.H5:
    @app.callback(
        Output(component_id='ticker-title', component_property='children'),
        Input(component_id='ticker_input', component_property='value')
    )
    def update_title(input_value: str) -> str:
        ticker = yf.Ticker(input_value)
        name = f"{ticker.info['symbol']}: {ticker.info['longName']}"
        return name