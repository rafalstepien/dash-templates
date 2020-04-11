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
    style={'height': '30px', 'width': '500px'},
    placeholder="Select view",
    options=[
            {'label': 'Length distribution plot', 'value': 'Length distribution plot'},
            {'label': 'Transcripts with length 1300-1600', 'value': 'Transcripts with length 1300-1600'},
    ],
)

# FILES UPLOAD BUTTON
files = dcc.Upload(
              id='upload-data',
              children=dbc.Button("Select Files")
              )

# CURRENT FILE UPDATED INFO
updated = dbc.Badge(
    id="updated-file",
    color="primary",
    className="mr-1"
)

# NAVBAR
navbar = dbc.NavbarSimple(
    children=[
        html.H4(updated),
        html.Div(files, className="p-1"),
        html.Div(view, className="p-1"),
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
              [Input('upload-data', 'contents'), Input("main-dropdown", "value")],
              [State('upload-data', 'filename')]
              )
def get_input_file(content, value, filename):
    if content is not None:
        data = Data(content, filename)
        if value == "Transcripts with length 1300-1600":
            return get_table(data.get_medium_length_subset())
        elif value == "Length distribution plot":
            x, y = data.get_histogram_data()
            return create_line_chart(x, y)
        else:
            return dbc.Alert("Please select view type", color="primary")
    else:
        return dbc.Alert("Please update file", color="primary")


@app.callback(Output('updated-file', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename')])
def file_updated(contents, filename):
    if contents is not None:
        return filename


if __name__ == "__main__":
    app.run_server(debug=True)
