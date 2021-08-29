import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output

app = dash.Dash(name=__name__)

app.layout = html.Div([
    html.H1(children='Visualizing Stock Data (Open Price)'),
    html.H3(children='Input a ticker'),
    dcc.Input(
        id='my-input',
        type='text',
        value='TSLA'
    ),
    dcc.Graph(id='my-graph')
    ]
)

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='my-input', component_property='value')
)
def updateGraph(stockTicker):
    df = web.DataReader(stockTicker, 'yahoo')
    figure = {
        'data': [
            {
                'x': df.index,
                'y': df.Open
            }
        ]
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
