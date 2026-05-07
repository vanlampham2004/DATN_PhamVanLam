import os


def generate_html_report(result, errors, screenshots, diff_images, analysis, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    screenshot_html = ""
    for img in screenshots:
        screenshot_html += f"<p>{img}</p><img src='../../{img}' width='450'>"

    diff_html = ""
    for img in diff_images:
        diff_html += f"<p>{img}</p><img src='../../{img}' width='450'>"

    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Register UI Test Report</title>
    </head>
    <body style="font-family:Arial">
        <h1>Register UI Test Report</h1>
        <h2>Result: {result}</h2>
        <p>Total UI differences: {errors}</p>

        <h2>Screenshots</h2>
        {screenshot_html}

        <h2>Diff Images</h2>
        {diff_html}

        <h2>AI Analysis</h2>
        <pre>{analysis}</pre>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path