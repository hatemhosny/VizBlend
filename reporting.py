import os
from figure_defaults import figure_defaults
from jinja2 import Environment, FileSystemLoader


def figure_defaults_wrapper(fig, options):
    """Styling Plotly figure

    Args:
        fig (plotly.core.figure): Plotly chart. The package supports: go.Bar, go.Pie, go.Scatter, go.Histogram, go.Treemap
        options (dict): User options. The dict must contain a least a chart title. Accepts: "groupby", "benchmark", "calender"

    Returns:
        Plotly fig: styled Plotly figure
    """

    @figure_defaults()
    def wrapper_figure_defaults(fig, options):
        return fig

    styled_fig = wrapper_figure_defaults(fig, options)
    return styled_fig


def create_report(figures: list, report_title: str):
    divs = []
    for i, figure in enumerate(figures):
        div = figure.to_html(
            full_html=False, include_plotlyjs="cdn", config={"displayModeBar": False}
        )
        divs.append(div)

    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    # Render the template with the required variables
    html_content = template.render(
        divs=divs,
        total_pages=len(divs) + 1,  # Include the initial report title page
        report_name=report_title,
    )
    output_dir = "./"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, f"{report_title}.html")
    with open(output_file, "w") as report_file:
        report_file.write(html_content)
    return report_file
