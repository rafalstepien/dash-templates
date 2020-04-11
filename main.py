#!/bin/python3

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from Data.Data import Data
from plot.histogram import create_line_chart
from dash.dependencies import Input, Output, State
from table.table_backend import get_table

# CONFIG
external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # DROPDOWN MENU IN NAVBAR
view = dcc.Dropdown(
    id='main-dropdown',
    options=[
            {'label': 'Plot', 'value': 'Plot'},
            {'label': 'Table', 'value': 'Table'},
    ],
    value="Plot"
)

# FILES UPLOAD BUTTON
files = dcc.Upload(
              id='upload-data',
              children=dbc.Button("Select Files")
              )


# NAVBAR
navbar = dbc.NavbarSimple(
    children=[
        files,
        view,
        ],
    brand="MNM Plotting",
    color="#1a1a1a",
    dark=True,
)

# MAIN LAYOUT
app.layout = html.Div(children=[
                      html.Div(navbar),
                      html.Span(id="output-data-upload", style={"vertical-align": "middle"}),
                      ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents'), Input("main-dropdown", "value")]
              )
def get_input_file(content, value):
    filename = "abundance.tsv"
    if content is not None:
        data = Data(content, filename)
        if value == "Table":
            return get_table(data.get_medium_length_subset())
        elif value == "Plot":
            x, y = data.get_histogram_data()
            return create_line_chart(x, y)
        else:
            return "Please input file and pick view to display"


if __name__ == "__main__":
    app.run_server(debug=True)
