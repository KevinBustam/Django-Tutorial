import dash
import uuid
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import dpd_components as dpd
from django_plotly_dash import DjangoDash
from django_plotly_dash.consumers import send_to_pipe_channel


X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)


app = DjangoDash('liveArduino')
app.layout = html.Div(
    [   dpd.Pipe(id="arduino_sensor_pipe",
                 value={'valor':0},
                 label="arduino_sensor",
                 channel_name="live_arduino_sensor"),
        html.Div(id="internal_state",
                 children="No state has been computed yet",
                 style={'display':'none'}),
        dcc.Graph(id="timeseries_plot"),
        ]
        )


@app.callback(
    dash.dependencies.Output('internal_state', 'children'),
    [dash.dependencies.Input('arduino_sensor_pipe', 'value'),])#dash.dependencies.Input('state_uid', 'value'),])
def callback_arduino_sensor_pipe(arduino_sensor,**kwargs):
     ## Guard against missing input on startup
    if not arduino_sensor:
        arduino_sensor = {}

    # extract incoming info from the message and update the internal state
    valor = arduino_sensor.get('valor', None)
    print("Entro: "+str(valor))
    #'Change output message'
    return valor

#@app.callback(Output('live-graph', 'figure'),
#            [Input('graph-update','n_intervals')])

@app.callback(
    dash.dependencies.Output('timeseries_plot', 'figure'),
    [dash.dependencies.Input('internal_state', 'children'),],
    )

def update_graph_scatter(input_data):

    #print("Graph "+str(input_data))

    global X
    global Y
    X.append(X[-1]+1)
    Y.append(input_data)
    #Y.append(Y[-1]+100)
    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name = 'Scatter',
        mode = 'lines+markers'
        )

    value = {'valor':min(X)}

    #send_to_pipe_channel(channel_name="live_arduino_sensor",label="arduino_sensor",value=value)

    return {'data':[data], 'layout':go.Layout(xaxis = dict(range=[min(X) , max(X)]),
                                              yaxis = dict(range=[min(Y) , max(Y)]))}

#if __name__== "__main__":
#    app.run_server(debug=True)

