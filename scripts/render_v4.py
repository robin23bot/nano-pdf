#!/usr/bin/env python3
import argparse
import os
import markdown
import re
from weasyprint import HTML, CSS

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a professional PDF using WeasyPrint for guaranteed margins and layout.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf} via WeasyPrint...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Convert MD to HTML
    html_body = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc', 'tables'])

    # PRODUCTION-GRADE DESIGN SYSTEM (WeasyPrint compatible)
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{
                size: A4;
                margin: 2.5cm; /* GUARANTEED MARGINS */
                @bottom-right {{
                    content: "Page " counter(page);
                    font-family: sans-serif;
                    font-size: 9pt;
                    color: #888;
                }}
            }}
            
            body {{
                font-family: 'Helvetica', 'Arial', sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #1a1a1a;
                margin: 0;
                padding: 0;
            }}
            
            .report-title-page {{
                text-align: center;
                margin-top: 5cm;
                margin-bottom: 5cm;
                page-break-after: always;
            }}
            
            .brand {{
                font-size: 14pt;
                letter-spacing: 4px;
                color: #666;
                text-transform: uppercase;
                margin-bottom: 2cm;
            }}
            
            h1 {{ font-size: 32pt; margin-bottom: 1cm; }}
            
            h2 {{ 
                font-size: 20pt; 
                margin-top: 2cm;
                border-bottom: 2px solid #333;
                padding-bottom: 10px;
                page-break-before: always;
            }}
            
            h3 {{ font-size: 14pt; margin-top: 1cm; font-weight: bold; }}
            
            p {{ margin-bottom: 12pt; text-align: justify; }}
            
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 20pt 0;
            }}
            
            th {{ background-color: #f2f2f2; border: 1px solid #ccc; padding: 10pt; text-align: left; }}
            td {{ border: 1px solid #eee; padding: 10pt; vertical-align: top; }}
            
            tr:nth-child(even) {{ background-color: #fafafa; }}
        </style>
    </head>
    <body>
        <div class="report-title-page">
            <div class="brand">Colossal Forge Intelligence</div>
            <h1>{re.sub(r'# ', '', md_text.split('\n')[0]) if md_text.startswith('# ') else 'Research Report'}</h1>
            <div style="font-size: 12pt; color: #888;">Prepared for Boss Fúlvio | January 2026</div>
        </div>
        <div class="report-content">
            {html_body}
        </div>
    </body>
    </html>
    """

    # WeasyPrint renders directly to PDF without wkhtmltopdf quirks
    HTML(string=styled_html).write_pdf(output_pdf)
    print(f"✅ Masterpiece Rendered with WeasyPrint.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="report.pdf")
    args = parser.parse_args()
    create_pdf(args.input, args.output)
