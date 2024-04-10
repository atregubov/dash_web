from dash import dcc
from dash import html

from dash.dependencies import Input, Output
from data_processing.data_processing import user_graph, get_nodes_and_edges


def results_div(app, data, hidden=True):
    """
    Results section/page div block layout.
    :param app: DASH/Flask webapp object
    :param data: dataframe with simulation outputs/inputs
    :param hidden: True/False if block is visible
    :return: div block
    """
    nodes_and_edges_cache = get_nodes_and_edges(data)
    res_div = html.Div(id="results_div",
                       children=[html.H2("Results"),
                                 html.I('Simulation day:'),
                                 dcc.Input(id='day_index', type='number', value='0', debounce=True),
                                 dcc.Graph(id='user_graph', figure=user_graph(data, 0, nodes_and_edges_cache)),
                                 ],
                       style={'width': '100%', 'padding': '10px 10px 20px 20px', 'display': 'none'} if hidden \
                           else {'width': '100%', 'padding': '10px 10px 20px 20px'}
                       )

    @app.callback(
        Output('user_graph', 'figure'),
        [Input('day_index', 'value')],
    )
    def update_output(day_index):
        day_index = int(day_index)
        if day_index >= len(nodes_and_edges_cache):
            day_index = len(nodes_and_edges_cache) - 1
        return user_graph(data, day_index, nodes_and_edges_cache)

    return res_div
