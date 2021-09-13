import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

 
layout = html.Div([
    dbc.Container([        
        dbc.Row([
            dbc.Col(
                html.H1(children='Phase 2 MILESTONES 2', className="text-center"),
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(
                html.H4("Lia Rainingsih")
                )
        ]),
        dbc.Row([
            dbc.Col(
                html.H4("Hactiv 8")
                )
        ]),
        dbc.Row([
            dbc.Col(
                html.H4("FTDS 001"),
                className="mb-7"
                )
        ]),
        dbc.Row([
            dbc.Col(
                html.P(html.Br()),
                )
        ]),
        dbc.Row([
            dbc.Col(
                html.P(html.Br()),
                )
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.Div([html.Img(
                            src=app.get_asset_url('dashboard.png'),
                            style={
                                'height': '50%',
                                'width': '50%'
                            })], style={'textAlign': 'center'}),
                        dbc.Button("Dashboard",
                        href="apps/dashboard",
                        color="info",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=4,  className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.Div([html.Img(
                            src=app.get_asset_url('github.png'),
                            style={
                                'height': '28%',
                                'width': '28%'
                            })], style={'textAlign': 'center'}),
                        dbc.Button("GitHub",
                        href="https://github.com/liarainingsih",
                        color="info",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=4, className="mb-6"
            ),
            dbc.Col(
                dbc.Card(
                    children=[
                        html.Div([html.Img(
                            src=app.get_asset_url('linkedin.png'),
                            style={
                                'height': '28%',
                                'width': '28%'
                            })], style={'textAlign': 'center'}),
                        dbc.Button("Linkedin",
                        href="https://linkedin.com/in/lia-rainingsih-9687042a",
                        color="info",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=4, className="mb-6"
            ),
            dbc.Row([
            dbc.Col(
                html.P(html.Br()),
                )
            ]),
            dbc.Row([
            dbc.Col(
                html.P(html.Br()),
                )
            ])
        ]
        ),
    ])
 
])