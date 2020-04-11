#!/bin/python3

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from Data.Data import Data
from plot.histogram import create_line_chart
from dash.dependencies import Input, Output
from table.table_backend import get_table

# CONFIG
external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# DATA
mediums = Data("/home/rafcio/Dash/files/abundance_24.tsv", "\t").get_medium_length_subset()
x, y = Data("/home/rafcio/Dash/files/abundance_24.tsv", "\t").get_histogram_data()

dropdown = dcc.Dropdown(
    id='main-dropdown',
    options=[
            {'label': 'Plot', 'value': 'Plot'},
            {'label': 'Table', 'value': 'Table'},
    ],
    value="Plot"
)

# PLOT
navbar = dbc.NavbarSimple(
    children=[dropdown],
    brand="MNM Plotting",
    color="#1a1a1a",
    dark=True,
)

app.layout = html.Div(children=[
                      html.Div(navbar),
                      html.Span(id="click-output", style={"vertical-align": "middle"}),
                      ])


@app.callback(
    Output('click-output', 'children'),
    [Input("main-dropdown", "value")]
)
def update_output(value):
    if value == "Table":
        return get_table(mediums)
    elif value == "Plot":
        return create_line_chart(x, y)


if __name__ == "__main__":
    app.run_server(debug=True)
