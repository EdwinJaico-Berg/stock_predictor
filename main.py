from dash import Dash, html
from src.data.load import load_data
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP


def main() -> None:
    # Initialise the app
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = 'Stock Predictor'
    app.layout  = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()