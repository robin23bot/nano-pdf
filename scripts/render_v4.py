#!/usr/bin/env python3
import argparse
import os
import markdown
import re
from weasyprint import HTML
from jinja2 import Template

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a professional, high-end PDF.
    Uses WeasyPrint for deterministic layout and Jinja2 for luxury templating.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf} via WeasyPrint...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Split title and body
    lines = md_text.split('\n')
    title = "Research Report"
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
            content_start = i + 1
            break
    
    html_body = markdown.markdown('\n'.join(lines[content_start:]), extensions=['extra', 'codehilite', 'toc', 'tables'])

    # --- LUXURY ACADEMIC TEMPLATE ---
    template_str = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;700&display=swap');
            
            @page {
                size: A4;
                margin: 2.54cm; /* Strict 1-inch margins */
                @bottom-right {
                    content: counter(page);
                    font-family: 'Montserrat', sans-serif;
                    font-size: 9pt;
                    color: #888;
                }
                @top-left {
                    content: "{{ title }}";
                    font-family: 'Montserrat', sans-serif;
                    font-size: 8pt;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    color: #aaa;
                }
            }
            
            body {
                font-family: 'Libre Baskerville', serif;
                font-size: 11pt;
                line-height: 1.8;
                color: #1a1a1a;
                margin: 0;
                text-align: justify;
            }
            
            .title-page {
                text-align: center;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
                page-break-after: always;
                border: 1pt solid #eee;
                margin: -1cm;
                padding: 4cm 2cm;
            }
            
            .brand {
                font-family: 'Montserrat', sans-serif;
                font-weight: 300;
                font-size: 12pt;
                letter-spacing: 8px;
                color: #666;
                text-transform: uppercase;
                margin-bottom: 4cm;
            }
            
            h1 { 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 32pt; 
                margin-bottom: 1cm;
                line-height: 1.1;
                text-align: center;
            }
            
            .author-box {
                margin-top: 4cm;
                font-family: 'Montserrat', sans-serif;
                font-size: 11pt;
                color: #444;
            }

            h2 { 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 20pt; 
                margin-top: 2cm;
                margin-bottom: 1cm;
                border-bottom: 1.5pt solid #1a1a1a;
                padding-bottom: 8pt;
                page-break-before: always;
                text-align: left;
            }
            
            h3 { 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 14pt; 
                margin-top: 1.2cm; 
                color: #2c3e50;
                text-align: left;
            }
            
            table { 
                width: 100%; 
                border-collapse: collapse; 
                margin: 30pt 0;
                border-top: 2pt solid #1a1a1a;
                border-bottom: 2pt solid #1a1a1a;
            }
            
            th { 
                border-bottom: 1pt solid #1a1a1a;
                padding: 12pt; 
                text-align: left;
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 10pt;
                background-color: #f9f9f9;
            }
            
            td { 
                padding: 12pt; 
                border-bottom: 0.5pt solid #eee;
            }
            
            tr:nth-child(even) { background-color: #fafafa; }

            .content-container { width: 100%; }
        </style>
    </head>
    <body>
        <div class="title-page">
            <div class="brand">Colossal Forge Intelligence</div>
            <h1>{{ title }}</h1>
            <div class="author-box">
                Commissioned by Boss Fúlvio<br>
                Strategic Research Division<br>
                January 2026
            </div>
        </div>
        <div class="content-container">
            {{ body }}
        </div>
    </body>
    </html>
    """
    
    template = Template(template_str)
    final_html = template.render(title=title, body=html_body)

    HTML(string=final_html).write_pdf(output_pdf)
    print(f"✅ Final Masterpiece Rendered with Luxury Templating.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="report.pdf")
    args = parser.parse_args()
    create_pdf(args.input, args.output)
