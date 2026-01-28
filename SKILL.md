---
name: nano-pdf
description: Edit PDFs with natural-language instructions using the nano-pdf CLI.
---

# Nano-PDF: The Beauty PDF Creator

This skill provides a standalone engine for transforming Markdown research results into professionally formatted, high-resolution PDFs.

## Capabilities
- **Retina Quality**: Uses Puppeteer (via browser tool) with high device scale factors for sharp typography.
- **Styled Sections**: Automatically applies GitHub-style themes with custom professional spacing.
- **Standalone CLI**: Can be called with a markdown file to produce a PDF instantly.

## Usage
1.  **Generate Report**: Research results saved as `report.md`.
2.  **Render (WeasyPrint)**: `/home/clawdbot/clawd/skills/deep-research/venv/bin/python3 scripts/render_v4.py report.md --output final.pdf`.
    -   *Note: This V4 engine uses WeasyPrint for guaranteed 2.5cm margins and professional typography.*

## Why a Separate Repo?
This decouples the **Gathering of Intelligence** (Deep Research Protocol) from the **Presentation of Intelligence** (Nano-PDF). 
