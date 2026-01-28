#!/usr/bin/env python3
import argparse
import os
import markdown
import pdfkit
import re

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a professional PDF. 
    Strict adherence to layout, margins, and font consistency.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf}...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Convert MD to HTML
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc', 'tables'])

    # --- PRODUCTION GRADE DESIGN SYSTEM ---
    # Using local fonts or standard safe web stacks to avoid rendering failures
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            /* Reset and Base */
            * {{ box-sizing: border-box; }}
            
            @page {{
                size: A4;
                margin: 2cm;
            }}
            
            body {{
                font-family: 'Helvetica', 'Arial', sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #1a1a1a;
                margin: 0;
                padding: 0;
                background-color: white;
            }}
            
            .report-container {{
                max-width: 100%;
                margin: 0 auto;
            }}

            /* Cover Page - Minimalist and Clean */
            .cover-page {{
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                border: 1px solid #eee;
                padding: 4cm 2cm;
                page-break-after: always;
            }}
            
            .brand {{
                font-size: 14pt;
                letter-spacing: 4px;
                color: #666;
                margin-bottom: 2cm;
                text-transform: uppercase;
            }}
            
            h1 {{ 
                font-size: 32pt; 
                line-height: 1.2;
                margin-bottom: 1cm;
                color: #000;
                font-weight: bold;
            }}
            
            .subtitle {{
                font-size: 12pt;
                color: #888;
                margin-bottom: 4cm;
            }}

            /* Content Sections */
            h2 {{ 
                font-size: 20pt; 
                margin-top: 2cm;
                margin-bottom: 0.5cm;
                color: #000;
                border-bottom: 2px solid #333;
                padding-bottom: 10pt;
                page-break-before: always;
            }}
            
            h3 {{ 
                font-size: 14pt; 
                margin-top: 1cm; 
                margin-bottom: 0.3cm;
                color: #2c3e50;
                font-weight: bold;
            }}
            
            p {{ margin-bottom: 12pt; text-align: left; }}
            
            ul, ol {{ margin-bottom: 12pt; padding-left: 20pt; }}
            li {{ margin-bottom: 6pt; }}

            /* Tables - Clean & Balanced */
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 20pt 0;
                font-size: 10pt;
            }}
            
            th {{ 
                background-color: #f2f2f2; 
                color: #333;
                font-weight: bold; 
                border: 1px solid #ccc; 
                padding: 10pt; 
                text-align: left;
            }}
            
            td {{ 
                border: 1px solid #eee; 
                padding: 10pt; 
                vertical-align: top;
            }}
            
            tr:nth-child(even) {{ background-color: #fafafa; }}

            .footer-info {{
                position: fixed;
                bottom: 0;
                width: 100%;
                text-align: right;
                font-size: 8pt;
                color: #ccc;
            }}
        </style>
    </head>
    <body>
        <div class="cover-page">
            <div class="brand">Colossal Forge Intelligence</div>
            <h1>{re.sub(r'# ', '', md_text.split('\n')[0]) if md_text.startswith('# ') else 'Strategic Analysis Report'}</h1>
            <div class="subtitle">Prepared for Boss Fúlvio | 2026</div>
            <div style="margin-top: auto; font-size: 9pt; color: #bbb;">CONFIDENTIAL | INTERNAL USE ONLY</div>
        </div>
        <div class="report-container">
            {html_content}
        </div>
    </body>
    </html>
    """

    temp_html = "final_render.html"
    with open(temp_html, 'w') as f:
        f.write(styled_html)

    # Simplified options to avoid wkhtmltopdf collision bugs
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
    }
    
    try:
        pdfkit.from_file(temp_html, output_pdf, options=options)
        print(f"✅ Production PDF Rendered.")
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
