import plotly.graph_objects as go
from reporting import figure_defaults_wrapper, create_report

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


if __name__ == "__main__":
    bar_figure = bar_graph()
    scatter_figure = scatter_graph()
    pie_figure = pie_graph()
    boxplot_figure = box_graph()
    figures = [
        bar_figure,
        scatter_figure,
        pie_figure,
        boxplot_figure,
    ]
    create_report(figures=figures, report_title="Example Report")