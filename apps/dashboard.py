import datetime

from pandas._config.config import options
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from app import app
import plotly.graph_objects as go

external_stylesheets = [dbc.themes.LUX]
 

df = pd.read_csv('bank-additional-full.csv', sep=';')
data = df
data['y']=data.y.replace({'yes':1,'no':0})

fig_job = px.scatter(data, x="job", y="age",  color="y", hover_name="month", hover_data=["housing", "loan", "marital", "duration", "euribor3m"])
fig_education = px.scatter(data, x="education", y="age",  color="y", hover_name="month", hover_data=["housing", "loan", "marital", "duration", "euribor3m"])
fig_age = px.scatter(data, x = "age", y = "age", color = "y")
fig_campaign = px.bar(df, "campaign", y = "y", title='Campaign')

fig_corr = px.imshow(data.corr())

layout = html.Div([
    html.H1(children="Dashboard Marketing of Bank",className="hello",
    style={'color':'#00361c','text-align':'center'
          }),  
    html.P(html.Br()),
    html.H5(children="Select Month:",className="select_month",
    style={'color':'#00361c','text-align':'left'
          }), 
    dcc.Dropdown(
        id='dropdown-month',
        options=[     
            {'label': 'April', 'value': 'apr'},
            {'label': 'May', 'value': 'may'},
            {'label': 'June', 'value': 'jun'},
            {'label': 'July', 'value': 'jul'},
            {'label': 'August', 'value': 'aug'},
            {'label': 'Sept', 'value': 'sep'},
            {'label': 'October', 'value': 'oct'},
            {'label': 'November', 'value': 'nov'},
            {'label': 'December', 'value': 'dec'}
        ],
        value=['apr'],
        multi=True
    ),  
    html.P(html.Br()),
    html.H5(children="Select Marital:",className="select_marital",
    style={'color':'#00361c','text-align':'left'
          }),
    dcc.Dropdown(
        id='dropdown-marital',
        options=[     
            {'label': 'Single', 'value' :'single'},
            {'label': 'Married', 'value': 'married'},
            {'label': 'Divorced', 'value': 'divorced'}
        ],
        value=['single'],
        multi=True
    ),
    dcc.Graph(id='graph-job',
              figure=fig_job
    ),
    dcc.Graph(
        id='graph-education',
        figure=fig_education
    ),
    dcc.Graph(
        id='graph-age',
        figure=fig_age
    ),
    dcc.Graph(
        id='graph-campaign',
        figure=fig_campaign
    ),
    dcc.Graph(
        id='graph-corr',
        figure=fig_corr
    )
])

@app.callback(
    Output('graph-job', 'figure'),
    [Input('dropdown-month', 'value')],
    [Input('dropdown-marital', 'value')])
def update_graph(input_month, input_marital):
    ts = df[df["month"].isin(input_month) & df["marital"].isin(input_marital)]
    fig = px.scatter(ts, x="job", y="age",  color="y", hover_name="month", hover_data=["housing", "loan", "marital", "duration", "euribor3m"])
    return fig

@app.callback(
    Output('graph-education', 'figure'),
    [Input('dropdown-month', 'value')],
    [Input('dropdown-marital', 'value')])
def update_graph(input_month, input_marital):
    ts = df[df["month"].isin(input_month) & df["marital"].isin(input_marital)]
    fig = px.scatter(ts, x="education", y="age",  color="y", hover_name="month", hover_data=["housing", "loan", "marital", "duration", "euribor3m"])
    return fig

@app.callback(
    Output('graph-campaign', 'figure'),
    [Input('dropdown-month', 'value')],
    [Input('dropdown-marital', 'value')])
def update_graph(input_month, input_marital):
    ts = df[df["month"].isin(input_month) & df["marital"].isin(input_marital)]
    fig = px.bar(df, "campaign", y = "euribor3m",color = "y", title='Campaign')
    return fig

@app.callback(
    Output('graph-age', 'figure'),
    [Input('dropdown-month', 'value')],
    [Input('dropdown-marital', 'value')])
def update_graph(input_month, input_marital):
    ts = df[df["month"].isin(input_month) & df["marital"].isin(input_marital)]
    fig = px.bar(df, x = "age", y = "age", color = "y")
    return fig

