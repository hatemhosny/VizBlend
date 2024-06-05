from figure_defaults import figure_defaults
from example_options import bar_graph, pie_graph, scatter_graph, box_graph

def figure_defaults_wrapper(fig, options):
    @figure_defaults()
    def wrapper_figure_defaults(fig, options):
        return fig

    styled_fig = wrapper_figure_defaults(fig, options)
    return styled_fig



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
    create_report(figures=figures)