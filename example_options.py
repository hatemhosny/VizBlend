import plotly.graph_objects as go
from figure_defaults import figure_defaults

def figure_defaults_wrapper(fig, options):
    @figure_defaults()
    def wrapper_figure_defaults(fig, options):
        return fig

    styled_fig = wrapper_figure_defaults(fig, options)
    return styled_fig

# ===========================================================================
def bar_graph():
    bar_options = {"title": "Bar Graph"}
    x = ["A", "B", "C"]
    y = [3, 1, 2]
    fig = go.Figure(go.Bar(x=x, y=y, text=y))
    fig = figure_defaults_wrapper(fig, bar_options)
    return fig
# ===========================================================================
def scatter_graph():
    scatter_options = {"title": "Scatter Graph"}
    x_scatter = [0, 1, 2, 3, 4]
    y_scatter = [0, 1, 4, 9, 16]
    fig = go.Figure(go.Scatter(x=x_scatter, y=y_scatter, mode="lines+markers"))
    fig = figure_defaults_wrapper(fig, scatter_options)
    return fig
# ===========================================================================
def pie_graph():
    pie_options = {"title": "Pie Graph"}
    labels = ["Apples", "Bananas", "Cherries"]
    values = [30, 20, 50]
    fig = go.Figure(go.Pie(labels=labels, values=values))
    fig = figure_defaults_wrapper(fig, pie_options)
    return fig
# ===========================================================================
def box_graph():
    box_options = {"title": "Box Graph"}
    data_box = [10, 15, 20, 25, 30, 35, 40]
    fig = go.Figure(go.Box(y=data_box, boxpoints="all", jitter=0.3))
    fig = figure_defaults_wrapper(fig, box_options)
    return fig
# ===========================================================================