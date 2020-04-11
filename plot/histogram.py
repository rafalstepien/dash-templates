import dash
import dash_core_components as dcc
import dash_html_components as html


def create_line_chart(x, y):
    graph = dcc.Graph(
        figure={
            'data': [
                {'x': x,
                 'y': y,
                 'type': 'bar',
                 'name': 'Transcripts length distribution'}
            ],
            'layout':{
                'title': "Transcripts length distribution",
                "height": 700,
                'plot_bgcolor': '#111111',
                'paper_bgcolor': '#111111',
                'font': {
                    'color': '#7FDBFF'
                }
            }
        })
    return graph

