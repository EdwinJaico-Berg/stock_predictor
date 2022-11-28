import pandas as pd
from dash import Dash, html, dcc
import src.components.spy_chart as spy_chart
import src.components.ticker_chart as ticker_chart
import src.components.earnings_table as earnings
import src.components.price_chart as price



def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div", 
        children=[
            html.H3(app.title),
            dcc.Tabs(
                id='tabs-with-classes',
                value='tab-1',
                parent_className='custom-tabs',
                className='custom-tabs-container',  
                colors={'primary': '#FF4136'}, 
                children=[
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
                                children=[
                                    html.Div(
                                        className='six columns pretty-container',
                                        id='price-div',
                                        children=[
                                            html.H4(
                                                className="container_title",
                                                children=[
                                                    "Prediction Price"
                                                ],
                                            ),
                                            dcc.Loading(
                                                html.Div(
                                                    id='price_graph',
                                                    children=[
                                                        price.render(app)
                                                    ]
                                                ),
                                                className="svg-container",
                                                style={"height": 400}
                                            ),
                                        ]
                                    ),
                                    html.Div(
                                        className='six columns pretty-container',
                                        id='earnings-div',
                                        children=[
                                            html.H4(
                                                className="container_title",
                                                children=[
                                                    "Earnings"
                                                ],
                                            ),
                                            dcc.Loading(
                                                html.Div(
                                                    id='earnings_graph',
                                                    children=[
                                                        earnings.render(app)
                                                    ],
                                                ),
                                                className="svg-container",
                                                style={"height": 400}
                                            )
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                id='ticker_output',
                                className="twelve columns pretty-container", 
                                children=[
                                    ticker_chart.render(app),
                                ]
                            )
                        ]
                    ),
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
                ]
            ),
            html.Div(
                id='bottom-banner',
                className='banner',
                children=[
                    html.Div(
                        className='image-div',
                        style= {'display':'inline-block', 'float':'left'},
                        children=[
                            html.A(
                                href='https://github.com/EdwinJaico-Berg',
                                children=[
                                    html.Img(
                                        alt='My GitHub profile',
                                        src="assets/images/icons8-github.svg"
                                    )
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        className='image-div',
                        style= {'display':'inline-block', 'float':'left'},
                        children=[
                            html.A(
                                href='https://www.linkedin.com/in/edwin-j-berg/',
                                children=[
                                    html.Img(
                                        alt='My LinkedIn profile',
                                        src="assets/images/icons8-linkedin.svg"
                                    )
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        className='image-div',
                        style= {'display':'inline-block', 'float':'left'},
                        children=[
                            html.A(
                                href='https://twitter.com/ejaicoberg',
                                children=[
                                    html.Img(
                                        alt='My Twitter profile',
                                        src="assets/images/icons8-twitter.svg"
                                    )
                                ]
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )