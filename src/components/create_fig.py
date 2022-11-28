def blank_fig() -> dict:

    return {
        "data": [],
        "layout": {
            "height": 150,
            "template": {
                "layout": {"paper_bgcolor": "#f3f3f1", "plot_bgcolor": "#f3f3f1"}
            },
            "xaxis": {"visible": False},
            "yaxis": {"visible": False}
        }
    }