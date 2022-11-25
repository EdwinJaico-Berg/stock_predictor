import pandas as pd
from dash import Dash, html
import dash_core_components as dcc
import src.components.spy_chart as spy_chart
import src.components.ticker_chart as ticker_chart


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            dcc.Tabs(id='tabs', children=[
                dcc.Tab(label='S&P 500', children=[
                    html.Div(className='app-div', children=[
                        spy_chart.render(data)
                    ])
                ]),
                dcc.Tab(label='Ticker', children=[
                    dcc.Input(
                        id='ticker_input',
                        type='search',
                        placeholder='Stock Ticker',
                        value='AAPL'
                    ),
                    html.Div(id='ticker_output', children=[
                        ticker_chart.render(app)
                    ])
                ])
            ])
        ]
    )