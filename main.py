import yfinance as yf
from dash import Dash, html
from src.data.load import load_data
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


def main() -> None:
    # Get the data
    data = load_data()

    # Initialise the app
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = 'Stock Predictor'
    app.layout  = create_layout(app, data)
    app.run()

if __name__ == '__main__':
    main()