import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from dash import Dash, html, Input, Output, dcc

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(component_id='earnings_graph', component_property='children'),
        Input(component_id='ticker_input', component_property='value')
    )
    def update_table(input_value: str) -> html.Div:
        ticker = yf.Ticker(input_value)
        df = ticker.earnings_dates
        df = df[~df['EPS Estimate'].isna()].head()
        
        fig = go.Figure(data=[
            go.Bar(name='Estimated EPS', x=df.index, y=df['EPS Estimate'], marker_color='firebrick'),
            go.Bar(name='Reported EPS', x=df.index, y=df['Reported EPS'], 
                hovertemplate = '<b>%{text}</b>',
                text = [f'Surprise: {surprise*100: .2f}%' for surprise in df['Surprise(%)']],
                marker_color='steelblue')
        ])
        
        fig.update_layout(
            barmode='group',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )

        return html.Div(dcc.Graph(figure=fig))