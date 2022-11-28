import pandas as pd
from dash import Dash, html, dcc
import src.components.ticker_chart as ticker_chart
import src.components.earnings_chart as earnings
import src.components.price_chart as price

colours = ['#252744D', '#464866', '#AAABB8', '#2E9CCA', '#29648A']

def create_layout(app: Dash) -> html.Div:
    return html.Div( 
        children=[
            html.H4(app.title),
            html.Div(
                id='ticker_search',
                className='pretty-container',
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
                className="twelve columns pretty-container", 
                children=[
                    ticker_chart.render(app),
                ]
            ),
            html.Div(
                id='div-container',
                className="twelve columns pretty-container",
                children=[
                    html.Div(
                        id='price-div',
                        className='six columns pretty-container',
                        children=[
                            html.H5(
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
                        id='earnings-div',
                        className='six columns pretty-container',
                        children=[
                            html.H5(
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
                className='twelve columns bottom-banner',
                children=[
                    html.Div(
                        className='four columns image-div',
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
                        className='four columns image-div',
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
                        className='four columns image-div',
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