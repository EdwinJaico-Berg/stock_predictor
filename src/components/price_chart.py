import yfinance as yf
import plotly.graph_objects as go
from dash import Dash, html, Input, Output, dcc
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(component_id='price_graph', component_property='children'),
        Input(component_id='ticker_input', component_property='value')
    )
    def update_price(input_value: str) -> html.Div:
        ticker = yf.Ticker(input_value)
        data = ticker.history(period='1mo')
        data = data[['Close']]
        test = data.values
        
        scaler = MinMaxScaler()

        test = scaler.fit_transform(test)
    
        lstm_model = load_model("./src/model.h5")

        prediction = lstm_model.predict(test)
        prediction = scaler.inverse_transform(prediction)

        fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = prediction[0][0],
            number = {'prefix': "$"},
            delta = {'position': "top", 'reference': data.iloc[-1,0]},
            domain = {'x': [0, 1], 'y': [0, 1]}))

        return html.Div(dcc.Graph(figure=fig))