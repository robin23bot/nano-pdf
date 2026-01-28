#!/usr/bin/env python3
import argparse
import os
import markdown
import re
from weasyprint import HTML, CSS

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a professional PDF using WeasyPrint.
    Uses LaTeX-inspired academic typography and clean layout.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf} via WeasyPrint...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # Convert MD to HTML
    html_body = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc', 'tables'])

    # --- LATEX-INSPIRED ACADEMIC DESIGN ---
    # - Using Computer Modern-like fonts or high-quality Serifs
    # - LaTeX standard margins and justified text
    # - Section numbering and academic table style
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Fira+Code:wght@400;500&family=Montserrat:wght@300;400;700&display=swap');
            
            @page {{
                size: A4;
                margin: 3cm 2.5cm;
                @bottom-center {{
                    content: counter(page);
                    font-family: 'Montserrat', sans-serif;
                    font-size: 10pt;
                    color: #333;
                }}
            }}
            
            body {{
                font-family: 'Libre Baskerville', serif;
                font-size: 11pt;
                line-height: 1.8;
                color: #1a1a1a;
                margin: 0;
                padding: 0;
                text-rendering: optimizeLegibility;
            }}
            
            .report-title-page {{
                text-align: center;
                margin-top: 8cm;
                margin-bottom: 8cm;
                page-break-after: always;
            }}
            
            .brand {{
                font-family: 'Montserrat', sans-serif;
                font-weight: 300;
                font-size: 12pt;
                letter-spacing: 6px;
                color: #666;
                text-transform: uppercase;
                margin-bottom: 3cm;
            }}
            
            h1 {{ 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 34pt; 
                margin-bottom: 0.5cm;
                line-height: 1.2;
            }}
            
            h2 {{ 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 22pt; 
                margin-top: 2.5cm;
                margin-bottom: 1cm;
                border-bottom: 0.5pt solid #ccc;
                padding-bottom: 10px;
                page-break-before: always;
            }}
            
            h3 {{ 
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 16pt; 
                margin-top: 1.5cm; 
                color: #2c3e50;
            }}
            
            p {{ 
                margin-bottom: 15pt; 
                text-align: justify; 
                hyphens: auto;
            }}
            
            /* LaTeX-style code blocks */
            pre, code {{
                font-family: 'Fira Code', monospace;
                background-color: #f8f9fa;
                font-size: 9.5pt;
            }}
            
            pre {{
                padding: 15pt;
                border: 0.5pt solid #ddd;
                border-radius: 2px;
                overflow: hidden;
            }}

            /* Academic Tables */
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 30pt 0;
                border-top: 1.5pt solid #1a1a1a;
                border-bottom: 1.5pt solid #1a1a1a;
            }}
            
            th {{ 
                border-bottom: 1pt solid #1a1a1a;
                padding: 12pt; 
                text-align: left;
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: 10pt;
                text-transform: uppercase;
            }}
            
            td {{ 
                padding: 12pt; 
                vertical-align: top;
                border-bottom: 0.5pt solid #eee;
            }}
            
            tr:last-child td {{ border-bottom: none; }}
            
            blockquote {{
                margin: 20pt 0;
                padding: 0 20pt;
                border-left: 3pt solid #1a1a1a;
                font-style: italic;
                color: #444;
            }}
        </style>
    </head>
    <body>
        <div class="report-title-page">
            <div class="brand">Colossal Forge Intelligence</div>
            <h1>{re.sub(r'# ', '', md_text.split('\n')[0]) if md_text.startswith('# ') else 'Research Report'}</h1>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 11pt; color: #888; margin-top: 1cm;">
                Commissioned by Boss Fúlvio<br>
                January 2026
            </div>
        </div>
        <div class="report-content">
            {html_body}
        </div>
    </body>
    </html>
    """

    HTML(string=styled_html).write_pdf(output_pdf)
    print(f"✅ LaTeX-Inspired Masterpiece Rendered.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="report.pdf")
    args = parser.parse_args()
    create_pdf(args.input, args.output)
