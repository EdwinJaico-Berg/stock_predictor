import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from dash import Dash, html, Input, Output, dcc


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(component_id='ticker_output', component_property='children'),
        Input(component_id='ticker_input', component_property='value')
    )
    def update_ticker_chart(input_value: str) -> html.Div:
        ticker = yf.Ticker(input_value)
        data = ticker.history(period='1mo')
        data = data[['Close']]
        test = data.values
        
        scaler = MinMaxScaler()

        test = scaler.fit_transform(test)
    
        lstm_model = load_model("./src/model.h5")

        prediction = lstm_model.predict(test)
        prediction = scaler.inverse_transform(prediction)

        prediction_date = data.index[-1] + datetime.timedelta(days=1)

        prediction_df = pd.DataFrame(
            {'Close': prediction[0]},
            index=[prediction_date]
        )
        prediction_data = pd.concat([pd.DataFrame(data.iloc[-1,]).T, prediction_df])

        fig = go.Figure()

        # Add actual data
        fig.add_trace(
            go.Scatter(
                x=data.index, 
                y=data['Close'].values,
                name=f'{input_value} Closing Price'
            )
        )

        # Add prediction data
        fig.add_trace(
            go.Scatter(
                x=prediction_data.index, 
                y=prediction_data['Close'].values,
                name='Predicted Price'
            )
        )

        # Add title and axes
        fig.update_layout(
            yaxis_title='Closing Price',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )

        return html.Div(dcc.Graph(figure=fig))