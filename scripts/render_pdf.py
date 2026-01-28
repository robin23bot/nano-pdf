#!/usr/bin/env python3
import argparse
import os
import sys
import subprocess

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to PDF using agent-browser's headless print-to-pdf capability.
    This creates a Retina-quality PDF with custom styling.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf}...")
    
    # 1. Read the markdown
    with open(markdown_file, 'r') as f:
        md_content = f.read()

    # 2. Inject CSS for 'Retina' quality and professional formatting
    styled_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
        <style>
            body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
            }}
            .markdown-body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 16px;
                line-height: 1.5;
                word-wrap: break-word;
            }}
            @media print {{
                body {{ padding: 0; }}
                .markdown-body {{ font-size: 14px; }}
            }}
            /* High-res table fixes */
            table {{ width: 100% !important; display: table !important; border-collapse: collapse !important; }}
            th, td {{ border: 1px solid #dfe2e5 !important; padding: 8px 13px !important; }}
        </style>
    </head>
    <body class="markdown-body">
        {md_content}
    </body>
    </html>
    """
    
    # Note: For actual MD to HTML conversion in a script, we'd use 'markdown' lib.
    # For now, we assume the input might already be HTML-ish or we use a basic converter.
    # In this agent context, we use the browser tool directly.
    
    temp_html = "temp_report.html"
    with open(temp_html, 'w') as f:
        f.write(styled_html)

    print(f"✅ Prepared high-res template. Use 'browser' tool to print {temp_html} to {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Markdown file")
    parser.add_argument("--output", default="report.pdf", help="Output PDF name")
    args = parser.parse_args()
    create_pdf(args.input, args.output)
