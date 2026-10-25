"""Generate HTML file for PDF submission of Mathematical Foundations assignments.

By default this script generates Assignment 1 HTML.
Use --assignment 2 to generate Assignment 2 HTML.
"""

import argparse
import subprocess
import sys
from datetime import datetime


ASSIGNMENT_CONFIG = {
    1: {
        "script": "assignment_1_solution.py",
        "output_html": "Assignment_1_Submission.html",
        "title": "Mathematical Foundations for Data Science - Assignment 1",
        "subtitle": "Assignment 1 - Solutions",
        "due_date": "7 March 2026",
        "marks": "10 (2 marks per question)",
        "summary_items": [
            "<li><strong>Problem 1:</strong> Reduced Row-Echelon Form computed with step-by-step transformations</li>",
            "<li><strong>Problem 2:</strong> Matrix inverse calculated using Gauss-Jordan elimination with verification</li>",
            "<li><strong>Problem 3:</strong> Basis verification performed using determinant, rank, and linear independence tests</li>",
            "<li><strong>Problem 4:</strong> Matrix rank determined using multiple methods (numpy, REF, SVD)</li>",
            "<li><strong>Problem 5:</strong> Complete SVD decomposition with U, Sigma, and V^T matrices and verification</li>",
        ],
        "submission_date": "7 March 2026",
    },
    2: {
        "script": "assignment_2_solution.py",
        "output_html": "Assignment_2_Submission.html",
        "title": "Mathematical Foundations for Data Science - Assignment 2",
        "subtitle": "Assignment 2 - Solutions",
        "due_date": "16 April 2026",
        "marks": "10 (Q1: 4 marks, Q2: 4 marks, Q3: 2 marks)",
        "summary_items": [
            "<li><strong>Problem 1:</strong> Adam optimizer implemented for f(x, y) = x^2 + y^2 with all intermediate iterations</li>",
            "<li><strong>Problem 2:</strong> AdaGrad optimizer implemented for f(x, y) = x^2 + y^2 with accumulated gradient tracking</li>",
            "<li><strong>Problem 3:</strong> Lagrange multiplier method used to solve constrained minimization analytically</li>",
        ],
        "submission_date": "11 April 2026",
    },
}


def generate_html(assignment_number):
    """Generate HTML file with assignment solutions."""
    cfg = ASSIGNMENT_CONFIG[assignment_number]
    solution_script = cfg["script"]

    # Run the assignment solution script and capture output
    try:
        result = subprocess.run(
            [sys.executable, solution_script],
            capture_output=True,
            text=True,
            timeout=60,
        )
        output = result.stdout
        if result.returncode != 0:
            print(f"Error running solution script: {result.stderr}", file=sys.stderr)
            return False
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return False

    # Read the Python source code
    with open(solution_script, "r", encoding="utf-8") as file_obj:
        python_code = file_obj.read()

    summary_html = "\n                ".join(cfg["summary_items"])

    # HTML template with embedded CSS
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>""" + cfg["title"] + """</title>
    <style>
        @media print {
            @page { margin: 1.5cm; }

            * {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }

            body {
                margin: 0;
                background: #ffffff !important;
                color: #000000 !important;
                max-width: none;
                padding: 0;
            }

            .container {
                box-shadow: none;
                background: #ffffff !important;
                padding: 0;
            }

            .header h1,
            .header h2,
            .student-info p,
            .problem-section h2,
            .code-section h3,
            .output-section h3,
            .summary h2,
            .summary li,
            .footer {
                color: #000000 !important;
            }

            .student-info,
            .output-section,
            .summary,
            .highlight {
                background: #ffffff !important;
                border: 1px solid #000000 !important;
            }

            pre {
                background: #ffffff !important;
                color: #000000 !important;
                border: 1px solid #000000 !important;
            }

            pre {
                font-size: 8.5px;
                line-height: 1.2;
                white-space: pre;
                word-break: normal;
                overflow-wrap: normal;
                overflow: visible;
                tab-size: 4;
            }
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .container {
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        
        .header {
            text-align: center;
            border-bottom: 3px solid #2c3e50;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        
        .header h1 {
            color: #2c3e50;
            margin: 10px 0;
            font-size: 24px;
        }
        
        .header h2 {
            color: #34495e;
            margin: 5px 0;
            font-size: 18px;
        }
        
        .student-info {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        
        .student-info p {
            margin: 5px 0;
            color: #2c3e50;
        }
        
        .problem-section {
            margin: 30px 0;
            border-left: 4px solid #3498db;
            padding-left: 20px;
        }
        
        .problem-section h2 {
            color: #2980b9;
            font-size: 20px;
        }
        
        .code-section {
            margin: 20px 0;
        }
        
        .code-section h3 {
            color: #27ae60;
            font-size: 16px;
            margin-bottom: 10px;
        }
        
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 12px;
            line-height: 1.4;
            white-space: pre;
            word-break: normal;
            overflow-wrap: normal;
            tab-size: 4;
        }
        
        .output-section {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }
        
        .output-section h3 {
            color: #e74c3c;
            font-size: 16px;
            margin-top: 0;
        }
        
        .highlight {
            background-color: #fff3cd;
            padding: 2px 5px;
            border-radius: 3px;
        }
        
        .summary {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            padding: 20px;
            margin-top: 30px;
        }
        
        .summary h2 {
            color: #155724;
            margin-top: 0;
        }
        
        .summary ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .summary li {
            padding: 5px 0;
            color: #155724;
        }
        
        .summary li:before {
            content: "• ";
            color: #28a745;
            font-weight: bold;
            margin-right: 10px;
        }
        
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Mathematical Foundations for Data Science</h1>
            <h2>""" + cfg["subtitle"] + """</h2>
        </div>
        
        <div class="student-info">
            <p><strong>Student Name:</strong> <span class="highlight">Gadamsetty V Sai Manoj Kumar</span></p>
            <p><strong>Student ID:</strong> <span class="highlight">2025MT12100</span></p>
            <p><strong>Submission Date:</strong> """ + cfg["submission_date"] + """</p>
        </div>
        
        <div class="code-section">
            <h3>Complete Python Code for All Problems:</h3>
            <pre>""" + python_code.replace('<', '&lt;').replace('>', '&gt;') + """</pre>
        </div>
        
        <div class="output-section">
            <h3>Program Output - All Solutions:</h3>
            <pre>""" + output.replace('<', '&lt;').replace('>', '&gt;') + """</pre>
        </div>
        
        <div class="summary">
            <h2>Summary of Solutions</h2>
            <ul>
                """ + summary_html + """
            </ul>
        </div>
        
    </div>
</body>
</html>
"""

    # Write HTML file
    output_file = cfg["output_html"]
    with open(output_file, "w", encoding="utf-8") as file_obj:
        file_obj.write(html_content)

    print(f"HTML file generated successfully: {output_file}")
    print(f"\nTo convert to PDF:")
    print(f"  1. Open '{output_file}' in your web browser")
    print(f"  2. Press Cmd+P (Mac) or Ctrl+P (Windows/Linux)")
    print(f"  3. Select 'Save as PDF' as destination")
    print(f"  4. Update your name and ID in the PDF before submitting")
    print(f"\nAlternatively, you can edit the HTML file directly to add your name and ID.")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate HTML submission for MFDS assignments"
    )
    parser.add_argument(
        "--assignment",
        "-a",
        type=int,
        default=1,
        choices=[1, 2],
        help="Assignment number to generate (default: 1)",
    )
    args = parser.parse_args()

    success = generate_html(args.assignment)
    sys.exit(0 if success else 1)
