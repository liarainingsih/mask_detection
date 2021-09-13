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
import dash_table
import base64

external_stylesheets = [dbc.themes.LUX]
 

df = pd.read_csv('bank-additional-full.csv', sep=';')


fig_corr = px.imshow(df.corr())


layout = html.Div(style={'marginTop' : '10px',
            'marginRight' : '10px',
            'marginBottom' : '50px',
            'marginLeft' : '100px',}, children=[
    dbc.Row([
        dbc.Col(
            html.H3(children='Hypothesis Marketing of Bank'), style={'text-align': 'center'},
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Data Set Information:'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('dataset.png')),
    html.P(html.Br()),
    #dbc.Table.from_dataframe(df.head(5), striped=True, bordered=True, hover=True),
    #html.P(html.Br()),
    dcc.Markdown('''
        Bank client data:
        * 1 - age (numeric)
        * 2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
        * 3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
        * 4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
        * 5 - default: has credit in default? (categorical: 'no','yes','unknown')
        * 6 - housing: has housing loan? (categorical: 'no','yes','unknown')
        * 7 - loan: has personal loan? (categorical: 'no','yes','unknown')

        Related with the last contact of the current campaign:
        * 8 - contact: contact communication type (categorical: 'cellular','telephone')
        * 9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
        * 10 - day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
        * 11 - duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
        
        Other attributes:
        * 12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
        * 13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
        * 14 - previous: number of contacts performed before this campaign and for this client (numeric)
        * 15 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
        
        Social and economic context attributes
        * 16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
        * 17 - cons.price.idx: consumer price index - monthly indicator (numeric)
        * 18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)
        * 19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
        * 20 - nr.employed: number of employees - quarterly indicator (numeric)

        Output variable (desired target):
        * 21 - y - has the client subscribed a term deposit? (binary: 'yes','no')
    '''
        
    ),    
    dbc.Row([
        dbc.Col(
            html.H4(children='Data Cleaning'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('DataCleaning.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H6(children='Duplicate'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('DataCleaning_duplicate.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H6(children='Drop Column: pdays, contact'),
            className="mb-4"
            )
        ]),        
    html.Img(src=app.get_asset_url('counts_y.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H6(children='Korelasi antar kolom'),
            className="mb-4"
            )
        ]),
    dcc.Graph(
        id='graph-corr',
        figure=fig_corr
    ),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H6(children='Kolom emp.var.rate, nr.employed and euribor3m memiliki korelasi yang tinggi. Kolom-kolom ini akan menjadi perhatian lebih.'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Exploratory Data Anaysis(EDA)'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('EDA_campaign.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H5(children='Campaign yang dilakukan pada bulan May, memiliki impact yang tinggi terhadap kemungkinan nasabah membuka deposit'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('EDA2.png')),
    html.P(html.Br()),
    html.Img(src=app.get_asset_url('EDA3.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.P(children='Pekerjaan sebagai Admin, Technician, Blue-Collar, Management, Retired dan Services bisa dijadikan target campaign.'), className="mb-4"),
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Status Marital Single dan Married memiliki perbandingan membuka deposit yang hampir sama.', className="mb-4"),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Nasabah dengan tingkat pendidikan Univercity Degree, basic dan High-School memiliki perbandingan membuka deposit yang hampir sama.', className="mb-4"),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Kalau dilihat Housing Loan, perbandingan nasabah yang membuka dan tidak membuka deposit hampir sama.', className="mb-4"),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Dilihat dari Personal Loan, perbandingan nasabah yang membuka dan tidak membuka deposit hampir sama.', className="mb-4"),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Nasabah yang dihubungi pada hari senin-jumat memiliki perbandingan membuka deposit yang hampir sama.', className="mb-4"),      
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Bulan Mei, Juni, Juli, Agustus, dan November memiliki performa campaign yang bagus.', className="mb-4"),
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Data Preprocessing'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('DataPreprocessing.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H4(children='Pendefinisian Model'),
            className="mb-4"
            )
        ]),
    html.Img(src=app.get_asset_url('Data_pendefinisianModel.png')),
    html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.P(children='Pelatihan Model'),
            className="mb-4"
            ),
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)'),
            className="mb-4"
            ),
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Evaluasi Model'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='1. Baseline Model'),
            className="mb-4"
            )
        ]),
        html.Img(src=app.get_asset_url('Evaluasi_baseline.png')),
        html.P(html.Br()),
        html.Img(src=app.get_asset_url('Evaluasi_baseline2.png')),
        html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.P(children='2. UnderSampling Model'),
            className="mb-4"
            ),
    ]),
        html.P(html.Br()),
        html.Img(src=app.get_asset_url('Evaluasi_under.png')),
        html.P(html.Br()),
        html.Img(src=app.get_asset_url('Evaluasi_under2.png')),
        html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.H6(children='Model yang terbaik berdasarkan precision, recall, f1 dan support adalah RandomForest dengan underSampling.'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Model Inference'),
            className="mb-4"
            )
        ]),
        html.Img(src=app.get_asset_url('Model_Inference.png')),
        html.P(html.Br()),
    dbc.Row([
        dbc.Col(
            html.P(children='Atribut yang memberikan impact cukup besar untuk membuka deposit adalah duration, nr.employed, euribor3m, dan cons.conf.idx'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Kesimpulan'),
            className="mb-4"
            )
        ]),
     dbc.Row([
        dbc.Col(
            html.P(children='* Duration memiliki impact yang besar terhadap hasil. semakin banyak nasabah terlibat semakin besar kemungkinan nasabah membuka deposit.'),
            className="mb-4"
            )
        ]),
     dbc.Row([
        dbc.Col(
            html.P(children='* Atribut Social Economic seperti nr.employed(number of employee), euribor3m(euribor 3 month rate), cons.conf.idx(consumer confidence index) memiliki peranan penting untuk kemungkinan nasabah membuka deposit.'),
            className="mb-4"
            )
        ]),
     dbc.Row([
        dbc.Col(
            html.P(children='* Bulan Oktober merupakan bulan paling tidak memungkinkan melakukan campaign.'),
            className="mb-4"
            )
        ]),
     dbc.Row([
        dbc.Col(
            html.P(children='* Nasabah dengan profesi pekerjaan sebagai technician, admins, blue-collar memiliki kemungkinan membuka deposit yang cukup tinggi.'),
            className="mb-4"
            )
        ]),
     dbc.Row([
        dbc.Col(
            html.P(children='* Nasabah dengan background pendidikan University degree keatas memiliki kemungkinan membuka deposit lebih banyak karena cenderung memiliki financially yang baik memiliki mind set untuk menabung.'),
            className="mb-4"
            )
        ])
])
