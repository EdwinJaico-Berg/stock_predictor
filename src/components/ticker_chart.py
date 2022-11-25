import pandas as pd
import yfinance as yf
from dash import Dash, html, Input, Output
import plotly.express as px
import dash_core_components as dcc


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(component_id='ticker_output', component_property='children'),
        Input(component_id='ticker_input', component_property='value')
    )
    def update_ticker_chart(input_value: str) -> html.Div:
        ticker = yf.Ticker(input_value)
        data = ticker.history(period='max')

        fig = px.line(
            data_frame=data,
            x=data.index,
            y=data['Close'],
            title=f"{input_value} Closing Prices",
            labels={
                'Close': 'Closing Price',
                'Date': 'Date'
            }
        )

        fig.update_xaxes(rangeslider_visible=True)

        return html.Div(dcc.Graph(figure=fig))
