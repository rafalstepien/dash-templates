import dash_html_components as html
import dash_bootstrap_components as dbc


def get_table(data):
    colnames = list(data)

    # HEADER
    table_header = [html.Thead(html.Tr([html.Th(str(name)) for name in colnames]))]

    # ROWS
    row_list = [html.Tr([html.Td(row[column_name]) for column_name in colnames]) for id, row in data.iterrows()]
    table_body = [html.Tbody(row_list)]

    # TABLE
    table = dbc.Table(table_header + table_body,
                      bordered=True,
                      hover=True,
                      striped=True,
    )

    return table
