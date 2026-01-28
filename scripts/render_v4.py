#!/usr/bin/env python3
import argparse
import os
import markdown
import pdfkit
import re

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a luxury, 30-page quality PDF with professional design.
    Fixes title collisions and ensures high-fidelity visual structure.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf}...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Convert MD to HTML
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc', 'tables'])

    # --- LUXURY DESIGN SYSTEM ---
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Lora:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@700;800&display=swap');
            
            @page {{
                size: A4;
                margin: 3.5cm 2.5cm;
                @bottom-center {{
                    content: "Page " counter(page);
                    font-family: 'Inter', sans-serif;
                    font-size: 9pt;
                    color: #888;
                }}
            }}
            
            body {{
                font-family: 'Lora', serif;
                font-size: 11.5pt;
                line-height: 1.75;
                color: #2c3e50;
                margin: 0;
                background-color: white;
            }}
            
            /* Cover Page Styling */
            .report-title-page {{
                height: 90vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                page-break-after: always;
            }}
            
            h1 {{ 
                font-family: 'Montserrat', sans-serif;
                font-size: 42pt; 
                line-height: 1.1;
                margin-bottom: 20pt;
                color: #1a1a1a;
                text-transform: uppercase;
                letter-spacing: -1px;
            }}
            
            .subtitle {{
                font-family: 'Inter', sans-serif;
                font-size: 14pt;
                color: #666;
                margin-bottom: 60pt;
            }}

            /* Fix Section Collisions */
            h2 {{ 
                font-family: 'Montserrat', sans-serif;
                font-size: 24pt; 
                margin-top: 60pt; /* Large top margin to prevent collision */
                margin-bottom: 20pt;
                color: #1a1a1a;
                border-bottom: 3px solid #1a1a1a;
                padding-bottom: 10pt;
                page-break-before: always;
                clear: both;
            }}
            
            h3 {{ 
                font-family: 'Montserrat', sans-serif;
                font-size: 16pt; 
                margin-top: 35pt; 
                margin-bottom: 12pt;
                color: #34495e;
            }}
            
            p {{ margin-bottom: 18pt; text-align: justify; }}
            
            /* Data Visualization / Tables */
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 40pt 0;
                font-family: 'Inter', sans-serif;
                font-size: 10pt;
                box-shadow: 0 0 20px rgba(0,0,0,0.05);
            }}
            
            th {{ 
                background-color: #1a1a1a; 
                color: #ffffff;
                font-weight: 600; 
                text-transform: uppercase;
                letter-spacing: 1px;
                padding: 15pt; 
                border: 1px solid #1a1a1a;
            }}
            
            td {{ 
                padding: 12pt; 
                border-bottom: 1px solid #eee;
                border-left: 1px solid #f9f9f9;
                border-right: 1px solid #f9f9f9;
            }}
            
            tr:nth-child(even) {{ background-color: #fcfcfc; }}
            
            blockquote {{
                margin: 30pt 0;
                padding: 20pt;
                background: #f8f9fa;
                border-left: 5px solid #1a1a1a;
                font-style: italic;
                color: #555;
            }}

            .source-link {{
                font-family: 'Inter', sans-serif;
                font-size: 8.5pt;
                color: #3498db;
                word-break: break-all;
                display: block;
                margin-top: 5pt;
            }}
        </style>
    </head>
    <body>
        <div class="report-title-page">
            <div style="font-size: 12pt; font-family: 'Inter'; letter-spacing: 3px; color: #888; margin-bottom: 20pt;">COLOSSAL FORGE INTELLIGENCE</div>
            <h1>{re.sub(r'# ', '', md_text.split('\n')[0]) if md_text.startswith('# ') else 'Deep Research Report'}</h1>
            <div class="subtitle">PREPARED FOR BOSS FÚLVIO | JANUARY 2026</div>
            <div style="margin-top: auto; font-size: 10pt; color: #aaa;">CONFIDENTIAL STRATEGIC ANALYSIS</div>
        </div>
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
        'margin-top': '0in', # Managed by @page CSS
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'javascript-delay': 1000
    }
    
    try:
        pdfkit.from_file(temp_html, output_pdf, options=options)
        print(f"✅ Luxury PDF Rendered successfully.")
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
