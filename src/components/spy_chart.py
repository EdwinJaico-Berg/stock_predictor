import pandas as pd
from dash import html, dcc
import plotly.express as px


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

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_xaxes(rangeslider_visible=True)

    return html.Div(dcc.Graph(figure=fig))