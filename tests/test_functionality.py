import os
import pytest
import plotly.graph_objs as go
from vizblend.create_report import CreateReport


@pytest.fixture
def sample_report():
    """Fixture to create a sample report object."""
    return CreateReport(report_title="Test Report")


@pytest.fixture
def sample_figure():
    """Fixture to create a sample Plotly figure."""
    return go.Figure(go.Bar(x=["A", "B", "C"], y=[1, 2, 3]))


def test_add_regular_figure(sample_report, sample_figure):
    """Test adding a regular Plotly figure."""
    options = {"title": "Bar Chart"}
    sample_report.add_figure(sample_figure, options)

    assert len(sample_report.figures) == 1
    assert sample_report.figures[0] == sample_figure


def test_add_figure_from_function(sample_report):
    """Test adding a figure returned by a function."""
    def example_graph(options):
        fig = go.Figure(go.Pie(labels=["A", "B", "C"], values=[30, 20, 50]))
        fig.update_layout(title=options["title"])
        return fig

    options = {"title": "Pie Chart"}
    sample_report.add_figure(example_graph, options)

    assert len(sample_report.figures) == 1
    assert sample_report.figures[0].layout.title.text == "Pie Chart"


def test_blend_graphs_to_html(sample_report, sample_figure, tmpdir):
    """Test blending graphs to an HTML report."""
    options = {"title": "Bar Chart"}
    sample_report.add_figure(sample_figure, options)

    # Override output directory for testing
    sample_report.blend_graphs_to_html = lambda: os.path.join(
        tmpdir, f"{sample_report.report_title}.html"
    )

    output_file = sample_report.blend_graphs_to_html()
    assert os.path.isfile(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Bar Chart" in content


def test_html_generation_content(sample_report, tmpdir):
    """Test the generated HTML file for expected content."""
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    options = {"title": "Scatter Plot"}
    sample_report.add_figure(fig, options)

    output_file = os.path.join(tmpdir, f"{sample_report.report_title}.html")
    sample_report.blend_graphs_to_html = lambda: output_file

    generated_file = sample_report.blend_graphs_to_html()
    assert os.path.exists(generated_file)

    with open(generated_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Scatter Plot" in content
        assert "Test Report" in content


def test_empty_figures_list(sample_report, tmpdir):
    """Test blending graphs with no figures added."""
    output_file = os.path.join(tmpdir, f"{sample_report.report_title}.html")
    sample_report.blend_graphs_to_html = lambda: output_file

    generated_file = sample_report.blend_graphs_to_html()
    assert os.path.exists(generated_file)

    with open(generated_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Test Report" in content
