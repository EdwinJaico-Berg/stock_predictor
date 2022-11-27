import pandas as pd
from dash import Dash, html, dcc
import src.components.spy_chart as spy_chart
import src.components.ticker_chart as ticker_chart


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div", 
        children=[
            html.H1(app.title),
            dcc.Tabs(
                id='tabs-with-classes',
                value='tab-1',
                parent_className='custom-tabs',
                className='custom-tabs-container',  
                colors={'primary': '#FF4136'}, 
                children=[
                    dcc.Tab(
                        label='S&P 500',
                        value='tab-1',
                        className='custom-tab',
                        selected_className='custom-tab--selected', 
                        children=[
                            html.Div(
                                className='app-div', 
                                children=[
                                    spy_chart.render(data)
                                ]
                            )
                        ]
                    ),
                    dcc.Tab(
                        label='Ticker',
                        value='tab-2',
                        className='custom-tab',
                        selected_className='custom-tab--selected', 
                        children=[
                            html.Div(
                                style={'textAlign': 'center'}, 
                                children=[
                                    dcc.Input(
                                        id='ticker_input',
                                        type='search',
                                        placeholder='Search for a ticker...',
                                        value='AAPL'
                                    )
                                ]
                            ),
                            html.Div(
                                id='ticker_output', 
                                children=[
                                    ticker_chart.render(app)
                                ]
                            )
                        ]
                    )
                ]
            ),
            html.Div(
                id='bottom-banner',
                className='bottome-banner'
            )
        ]
    )