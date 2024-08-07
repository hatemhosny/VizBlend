import pytest
import plotly.graph_objs as go
from vizblend.create_report import CreateReport


def test_add_regular_figure():
    report = CreateReport(report_title="Test Report")
    bar_fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[1, 2, 3]))
    options = {"title": "Bar Graph"}

    report.add_figure(bar_fig, options)

    assert len(report.figures) == 1
    assert report.figures[0] == bar_fig


def example_graph_with_options(options):
    fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[3, 1, 2]))
    fig.update_layout(title=options.get("title"))
    return fig


def test_add_figure_from_function():
    report = CreateReport(report_title="Test Report")
    options = {"title": "Generated Bar Graph"}

    report.add_figure(example_graph_with_options, options)

    assert len(report.figures) == 1
    assert report.figures[0].layout.title.text == "Generated Bar Graph"
