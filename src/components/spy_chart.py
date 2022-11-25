import pandas as pd
from dash import html
import plotly.express as px
import dash_core_components as dcc


def render(data: pd.DataFrame) -> html.Div:
    fig = px.line(
        data_frame=data,
        x=data.index,
        y=data['Close'],
        title="SPY Closing Prices",
        labels={
            'Close': 'Closing Price',
            'Date': 'Date'
        }
    )

    fig.update_xaxes(rangeslider_visible=True)

    return html.Div(dcc.Graph(figure=fig))