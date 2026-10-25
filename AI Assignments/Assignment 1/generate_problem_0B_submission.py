"""Generate a print-ready HTML submission for AI Assignment 1, Problem Statement 0-B."""

from __future__ import annotations

import html
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parents[1]
SCRIPT_PATH = BASE_DIR / "problem_0B_solution.py"
HTML_PATH = BASE_DIR / "problem_0B_submission.html"


def run_solution() -> str:
    result = subprocess.run(
        [str(ROOT_DIR / ".venv" / "bin" / "python"), str(SCRIPT_PATH)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def build_html(output_text: str, source_code: str) -> str:
    safe_output = html.escape(output_text, quote=False)
    safe_code = html.escape(source_code, quote=False)
    generated_on = datetime.now().strftime("%d %B %Y")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AI Assignment 1 - Problem Statement 0-B</title>
    <style>
        @page {{
            size: A4;
            margin: 0.45in;
        }}

        * {{ box-sizing: border-box; }}

        body {{
            font-family: Helvetica, Arial, sans-serif;
            color: #1f2937;
            line-height: 1.35;
            margin: 0;
            background: #f5f7fb;
        }}

        .page {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 20px 22px 24px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        }}

        .header {{
            text-align: center;
            padding: 10px 0 14px;
            border-bottom: 2px solid #d9e2ec;
            margin-bottom: 16px;
        }}

        .header h1 {{
            margin: 0;
            font-size: 22pt;
            color: #17324d;
        }}

        .header h2 {{
            margin: 6px 0 2px;
            font-size: 16pt;
            color: #1f4e79;
        }}

        .header p {{
            margin: 3px 0 0;
            color: #4b5563;
            font-size: 9.5pt;
        }}

        .meta {{
            width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            table-layout: fixed;
            margin-bottom: 14px;
            font-size: 9.5pt;
        }}

        .meta td {{
            border: 1px solid #c8d3df;
            padding: 7px 9px;
            vertical-align: top;
            overflow-wrap: anywhere;
        }}

        .meta td:first-child {{
            width: 28%;
            background: #f3f7fb;
            font-weight: 700;
            color: #17324d;
        }}

        .section {{
            margin-top: 10px;
            margin-bottom: 12px;
        }}

        .section h3 {{
            margin: 0 0 8px;
            font-size: 13pt;
            color: #1f4e79;
            border-bottom: 1px solid #cdd8e3;
            padding-bottom: 4px;
        }}

        .section p {{
            margin: 0 0 8px;
            font-size: 10pt;
        }}

        .result-table {{
            width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            table-layout: fixed;
            margin-top: 8px;
            font-size: 9.5pt;
        }}

        .result-table th, .result-table td {{
            border: 1px solid #c8d3df;
            padding: 7px 8px;
            vertical-align: top;
            text-align: left;
            overflow-wrap: anywhere;
        }}

        .result-table th {{
            background: #1f4e79;
            color: #ffffff;
            font-weight: 700;
        }}

        .code-block {{
            font-family: "Courier New", Courier, monospace;
            font-size: 8pt;
            line-height: 1.18;
            white-space: pre-wrap;
            word-break: break-word;
            overflow-wrap: anywhere;
            border: 1px solid #c8d3df;
            background: #fbfcfe;
            padding: 10px 11px;
        }}

        .output-block {{
            font-family: "Courier New", Courier, monospace;
            font-size: 8pt;
            line-height: 1.2;
            white-space: pre-wrap;
            word-break: break-word;
            overflow-wrap: anywhere;
            border: 1px solid #c8d3df;
            background: #fcfefe;
            padding: 10px 11px;
        }}

        .note {{
            font-size: 9pt;
            color: #4b5563;
            margin-top: 4px;
        }}

        .page-break {{
            page-break-before: always;
            break-before: page;
        }}

        @media print {{
            * {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            body {{ background: #ffffff; }}
            .page {{
                box-shadow: none;
                padding: 6px 8px 8px;
                max-width: none;
                width: 100%;
                margin: 0;
            }}
            .header {{ padding-top: 0; }}

            .meta, .result-table {
                margin-left: 0;
                margin-right: 0;
            }

            .page-break {{ page-break-before: always; }}
        }}
    </style>
</head>
<body>
    <div class="page">
        <div class="header">
            <h1>Artificial and Computational Intelligence</h1>
            <h2>Assignment 1 Submission</h2>
            <p>Problem Statement 0-B - Travelling Agent</p>
            <p>Student: Gadamsetty V Sai Manoj Kumar | BITS ID: 2025MT12100</p>
        </div>

        <table class="meta">
            <tr><td>Assigned Problem</td><td>Problem Statement 0-B</td></tr>
            <tr><td>Graph Goal</td><td>Find the shortest route from A to X</td></tr>
            <tr><td>Heuristic</td><td>Average cost of all simple paths from node to X</td></tr>
            <tr><td>Implementation</td><td>Executable Python solution with IDA* and Hill Climbing</td></tr>
            <tr><td>Generated On</td><td>{generated_on}</td></tr>
        </table>

        <div class="section">
            <h3>Environment</h3>
            <p>Deterministic, fully observable graph-search environment. The agent begins at A and must reach X by traversing adjacent roads with minimum travel cost.</p>
        </div>

        <div class="section">
            <h3>Result Summary</h3>
            <table class="result-table">
                <tr><th>Algorithm</th><th>Observed Result</th><th>Time Complexity</th><th>Space Complexity</th></tr>
                <tr><td>IDA*</td><td>A -&gt; D -&gt; G -&gt; X</td><td>O(b^d) worst case</td><td>O(bd) worst case</td></tr>
                <tr><td>Hill Climbing</td><td>A -&gt; D -&gt; G -&gt; X</td><td>O(b) per move</td><td>O(b) for neighbor inspection</td></tr>
            </table>
        </div>

        <div class="section">
            <h3>Verified Program Output</h3>
            <div class="output-block">{safe_output}</div>
        </div>

        <div class="page-break"></div>

        <div class="header" style="border-bottom: 0; margin-bottom: 10px;">
            <h2>Source Code</h2>
            <p>Plain code only, without explanatory text.</p>
        </div>
        <div class="code-block">{safe_code}</div>
    </div>
</body>
</html>"""


def write_html(html_text: str) -> None:
    with HTML_PATH.open("w", encoding="utf-8") as handle:
        handle.write(html_text)


def main() -> None:
    output_text = run_solution()
    source_code = SCRIPT_PATH.read_text(encoding="utf-8")
    html_text = build_html(output_text, source_code)
    write_html(html_text)
    print(f"Generated: {HTML_PATH}")
    print("Print to PDF: Open HTML in browser and use Cmd+P -> Save as PDF")


if __name__ == "__main__":
    main()
