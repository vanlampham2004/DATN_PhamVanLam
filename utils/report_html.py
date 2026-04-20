def generate_html_report(result, errors, screenshot, diff, ai_analysis):
    html = f"""
    <html>
    <head>
        <title>UI Test Report</title>
        <style>
            body {{ font-family: Arial; }}
            .fail {{ color: red; }}
            .pass {{ color: green; }}
            img {{ width: 400px; margin: 10px; }}
        </style>
    </head>

    <body>
        <h1>UI TEST REPORT</h1>

        <h2>Result: <span class="{result.lower()}">{result}</span></h2>
        <p>Errors detected: {errors}</p>

        <h3>Screenshot</h3>
        <img src="../{screenshot}">

        <h3>Diff Image</h3>
        <img src="../{diff}">

        <h3>AI Analysis</h3>
        <p>{ai_analysis}</p>

    </body>
    </html>
    """

    path = "reports/report.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return path