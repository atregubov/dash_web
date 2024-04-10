import plotly.graph_objects as go
import networkx as nx


def user_graph(data, day_index, nodes_and_edges_cache=None):
    """This is a demo layout. Actual data is not currently loaded."""
    nodes_and_edges = get_nodes_and_edges(data) if nodes_and_edges_cache is None else nodes_and_edges_cache
    G = nx.Graph()
    G.add_edges_from(nodes_and_edges[int(day_index)][1])
    G.add_nodes_from(nodes_and_edges[int(day_index)][0])
    pos = nx.spring_layout(G)

    # edges trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color='black', width=1),
        hoverinfo='none',
        showlegend=False,
        mode='lines')

    # nodes trace
    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=text,
        mode='markers+text',
        showlegend=False,
        hoverinfo='none',
        marker=dict(
            color='pink',
            size=5,
            line=dict(color='black', width=1)))

    # layout
    layout = dict(plot_bgcolor='white',
                  paper_bgcolor='white',
                  margin=dict(t=10, b=10, l=10, r=10, pad=0),
                  xaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True),
                  yaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True))

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)

    return fig


def get_nodes_and_edges(data, verbose=False):
    """
    For each day returns a set of users that interacted as nodes and a all interactions as edges.
    :param data: data in DASH simulation format
    :param verbose:
    :return: dictionary: each day is a keys and value is (nodes, edges) tuple.
    """
    data = data.assign(day=lambda x: x['nodeTime'] // (24 * 3600))

    day_index_min = data['day'].min()
    day_index_max = data['day'].max()

    nodes_and_edges = dict()

    if verbose:
        print(f"days: {len(sorted(list(data['day'].unique())))}, min: {day_index_min}, max: {day_index_max}")
    for day_index in range((day_index_max - day_index_min) + 1):
        day_data = data[data['day'] == day_index_min + day_index]
        if verbose:
            print(f"day {day_index}: {len(day_data)}")
        edges = set()
        nodes = set()
        for index, event in day_data.iterrows():
            node_user = event['rootUserID']
            node_parent = event['parentUserID']
            nodes.add(node_user)
            nodes.add(node_parent)
            if node_user != node_parent:
                edges.add((node_user, node_parent))
        nodes_and_edges[day_index] = (nodes, edges)

    return nodes_and_edges


