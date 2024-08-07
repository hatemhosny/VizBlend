import os


def test_html_file_creation(tmpdir):
    report = CreateReport(report_title="Test Report")
    bar_fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[1, 2, 3]))
    options = {"title": "Bar Graph"}

    report.add_figure(bar_fig, options)
    output_file = report.blend_graphs_to_html()

    assert os.path.isfile(output_file)
    assert output_file.endswith(".html")
