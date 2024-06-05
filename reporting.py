import pandas as pd
import plotly.graph_objects as go
from figure_defaults import figure_defaults

def figure_defaults_wrapper(fig):
    styled_figure = figure_defaults()(fig)
    return styled_figure


def create_report(figures):
    divs = []
    for i, figure in enumerate(figures):
        div = figure.to_html(
            full_html=False, 
            include_plotlyjs="cdn", 
            config={"displayModeBar": False}
        )
        divs.append(f'<div id="page{i}" class="page">{div}</div>')
    
    # with open("report_template.html", "r") as template_file:
    #     html_template = template_file.read()
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{report_name}</title>
        <style>
            body, html {{
                margin: 0;
                padding: 0;
                height: 100%;
                width: 100%;
                overflow: hidden;
            }}
            .page {{
                display: none;
                height: 100vh;
                width: 100vw;
            }}
            .active {{
                display: block;
            }}
            .plotly-graph-div {{
                height: 100vh !important;
                width: 100vw !important;
            }}
        </style>
    </head>
    <body>
        {divs}
        <script>
            var currentPage = 0;
            var totalPages = {total_pages};
            function showPage(page) {{
                document.querySelectorAll('.page').forEach(function(div, index) {{
                    div.classList.remove('active');
                    if (index === page) {{
                        div.classList.add('active');
                    }}
                }});
            }}
            function prevPage() {{
                if (currentPage > 0) {{
                    currentPage--;
                    showPage(currentPage);
                }}
            }}
            function nextPage() {{
                if (currentPage < totalPages - 1) {{
                    currentPage++;
                    showPage(currentPage);
                }}
            }}
            document.addEventListener('keydown', function(event) {{
                if (event.key === 'ArrowLeft') {{
                    prevPage();
                }} else if (event.key === 'ArrowRight') {{
                    nextPage();
                }}
            }});
            
            showPage(currentPage);
        </script>
    </body>
    </html>
    """
    html_content = html_template.format(divs="\n".join(divs), total_pages=len(divs), report_name="VizBlend")
    
    with open("report_template.html", "w") as report_file:
        report_file.write(html_content)
    return report_file


df_bar = pd.DataFrame({
    "col1": ["A", "B", "C"],
    "col2": [3, 1, 2]
})
@figure_defaults()
def create_bar_fig(df, options):
    # Example data
    x = df["col1"]
    y = df["col2"]

    # Create a bar chart
    fig = go.Figure(go.Bar(x=x, y=y, text=y))
    return fig

df_scatter = pd.DataFrame({
    "col1": [0, 1, 2, 3, 4],
    "col2": [0, 1, 4, 9, 16]
})
@figure_defaults()
def create_scatter_fig(df, options):
    x_scatter = df["col1"]
    y_scatter = df["col2"]

    # Create a scatter plot
    fig = go.Figure(go.Scatter(x=x_scatter, y=y_scatter, mode="lines+markers"))
    return fig

df_pie = pd.DataFrame({
    "col1": ["Apples", "Bananas", "Cherries"],
    "col2": [30, 20, 50]
})
@figure_defaults()
def create_pie_fig(df, options):
    labels = df["col1"]
    values = df["col2"]

    # Create a pie chart
    fig = go.Figure(go.Pie(labels=labels, values=values))
    return fig

df_box = pd.DataFrame({
    "col1": [10, 15, 20, 25, 30, 35, 40]
})
@figure_defaults()
def create_boxplot_fig(df, options):
    data_box = df["col1"]
    # Create a box plot
    fig = go.Figure(go.Box(y=data_box, boxpoints="all", jitter=0.3))
    return fig

options = {"title": "Bar Graph"}
bar_figure = create_bar_fig(df_bar, options)
options = {"title": "Scatter Graph"}
scatter_figure = create_scatter_fig(df_scatter, options)
options = {"title": "Pie Graph"}
pie_figure = create_pie_fig(df_pie, options)
options = {"title": "Box Graph"}
boxplot_figure = create_boxplot_fig(df_box, options)

figures = [
    bar_figure,
    scatter_figure,
    pie_figure,
    boxplot_figure,
]

if __name__ == "__main__":
    create_report(figures=figures)