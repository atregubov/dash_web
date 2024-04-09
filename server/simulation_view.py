from dash import dcc
from dash import html


def simulation_div(app, data, hidden=True):
    """
    Simulation section/page div block layout.
    :param app: DASH/Flask webapp object
    :param data: dataframe with simulation outputs/inputs
    :param hidden: True/False if block is visible
    :return: div block
    """
    res_div = html.Div(id="simulation_div",
                       children=[html.H2("Simulation"),
                                 html.Div(children=[html.I('Simulation start day: '),
                                                    dcc.Input(id='start_day', type='text', value='2020-01-01',
                                                              debounce=True)
                                                    ]
                                          ),
                                 html.Div(children=[html.I('Simulation end day: '),
                                                    dcc.Input(id='end_day', type='text', value='2020-06-30',
                                                              debounce=True)
                                                    ]
                                          ),
                                 html.Div(children=[html.I('Number of users: '),
                                                    dcc.Input(id='n_users', type='number', value='1000',
                                                              debounce=True)
                                                    ]
                                          ),
                                 html.Div(children=[html.Button('Run simulation',
                                                                id="run_sim",
                                                                n_clicks=0,
                                                                style={'margin-right': '10px'}
                                                                )
                                                    ]
                                          ),
                                 ],
                       style={'width': '100%', 'padding': '10px 10px 20px 20px', 'display': 'none'} if hidden \
                           else {'width': '100%', 'padding': '10px 10px 20px 20px'}
                       )

    return res_div
