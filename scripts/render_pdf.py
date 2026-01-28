#!/usr/bin/env python3
import argparse
import os
import markdown
import pdfkit
import re

def create_pdf(markdown_file, output_pdf):
    """
    Renders Markdown to a professional, Retina-quality PDF with design-standard margins.
    Implements full verification check.
    """
    print(f"🎨 Rendering {markdown_file} to {output_pdf}...")
    
    with open(markdown_file, 'r') as f:
        md_text = f.read()

    # --- THE "STUPIDITY" CHECK (Internal Content Verification) ---
    # Use word boundaries (\b) to avoid false positives like "toward" (to-ward)
    forbidden_terms = ["ukraine", "russia", r"\bwar\b", "nuclear"]
    found_bugs = []
    for term in forbidden_terms:
        if re.search(term, md_text, re.IGNORECASE):
            found_bugs.append(term)
            
    if found_bugs:
        print(f"🛑 BUG DETECTED: Report contains cross-contamination terms: {found_bugs}")
        return False

    # Convert MD to HTML
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc'])

    # PRODUCTION-GRADE CSS
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
            
            @page {{
                size: A4;
                margin: 2.54cm;
            }}
            
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #1a1a1a;
                margin: 0;
                padding: 0;
            }}
            
            h1 {{ font-size: 28pt; margin-bottom: 20pt; color: #000; border-bottom: 1px solid #eee; padding-bottom: 10pt; }}
            h2 {{ font-size: 18pt; margin-top: 25pt; margin-bottom: 10pt; color: #333; }}
            h3 {{ font-size: 14pt; margin-top: 15pt; }}
            
            p {{ margin-bottom: 12pt; text-align: justify; }}
            
            table {{ 
                width: 100%; 
                border-collapse: collapse; 
                margin: 20pt 0;
                page-break-inside: avoid;
            }}
            
            th {{ background-color: #f8f9fa; font-weight: 600; border: 1px solid #dee2e6; padding: 10pt; text-align: left; }}
            td {{ border: 1px solid #dee2e6; padding: 10pt; vertical-align: top; }}
            
            code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 4px; font-family: monospace; }}
            
            a {{ color: #0066cc; text-decoration: none; word-break: break-all; }}
            
            .header {{ text-align: right; font-size: 9pt; color: #999; margin-bottom: 40pt; border-bottom: 1px solid #eee; padding-bottom: 10pt; }}
        </style>
    </head>
    <body>
        <div class="header">Deep Research Report | January 2026</div>
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
        'margin-top': '1in',
        'margin-right': '1in',
        'margin-bottom': '1in',
        'margin-left': '1in',
        'encoding': "UTF-8",
        'no-outline': None,
        'quiet': '',
        'enable-local-file-access': None
    }
    
    try:
        pdfkit.from_file(temp_html, output_pdf, options=options)
        print(f"✅ Final PDF rendered with standard margins and verified content.")
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
