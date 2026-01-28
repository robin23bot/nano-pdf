#!/usr/bin/env python3
import argparse
import os
import markdown
import pdfkit
import re

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a 30-page quality PDF.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf}...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Convert MD to HTML
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc', 'tables'])

    # --- LUXURY REPORT CSS ---
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700&display=swap');
            
            @page {{
                size: A4;
                margin: 3cm 2.5cm;
                @bottom-right {{
                    content: counter(page);
                    font-size: 9pt;
                    color: #666;
                }}
            }}
            
            body {{
                font-family: 'Inter', sans-serif;
                font-size: 11pt;
                line-height: 1.7;
                color: #1a1a1a;
                margin: 0;
            }}
            
            h1 {{ 
                font-family: 'Playfair Display', serif;
                font-size: 36pt; 
                margin-bottom: 40pt; 
                color: #000; 
                text-align: center;
                page-break-after: always;
                display: flex;
                flex-direction: column;
                justify-content: center;
                height: 80vh;
            }}
            
            h2 {{ 
                font-family: 'Playfair Display', serif;
                font-size: 22pt; 
                margin-top: 50pt; 
                border-bottom: 2px solid #000;
                padding-bottom: 10pt;
                page-break-before: always;
            }}
            
            h3 {{ font-size: 16pt; margin-top: 25pt; color: #444; }}
            
            p {{ margin-bottom: 15pt; text-align: justify; }}
            
            /* Professional Tables */
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 30pt 0;
                font-size: 10pt;
            }}
            
            th {{ 
                background-color: #1a1a1a; 
                color: #fff;
                font-weight: 600; 
                border: 1px solid #1a1a1a; 
                padding: 12pt; 
            }}
            
            td {{ 
                border: 1px solid #eee; 
                padding: 12pt; 
            }}
            
            tr:nth-child(even) {{ background-color: #fafafa; }}

            .source {{ font-size: 8pt; color: #0066cc; word-break: break-all; }}
            
            .toc {{ page-break-after: always; }}
        </style>
    </head>
    <body class="markdown-body">
        <div class="container">
            {html_content}
        </div>
    </body>
    </html>
    """

    temp_html = "temp_report.html"
    with open(temp_html, 'w') as f:
        f.write(styled_html)

    options = {
        'page-size': 'A4',
        'margin-top': '1.2in',
        'margin-right': '1in',
        'margin-bottom': '1.2in',
        'margin-left': '1in',
        'encoding': "UTF-8",
        'custom-header': [('Accept-Encoding', 'gzip')],
        'no-outline': None,
    }
    
    try:
        pdfkit.from_file(temp_html, output_pdf, options=options)
        print(f"✅ Final Masterpiece Rendered.")
        return True
    except Exception as e:
        print(f"❌ PDF rendering failed: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Markdown file")
    parser.add_argument("--output", default="report.pdf", help="Output PDF name")
    args = parser.parse_args()
    create_pdf(args.input, args.output)
