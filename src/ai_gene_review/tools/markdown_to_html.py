#!/usr/bin/env python3
"""Convert markdown files with mermaid diagrams to standalone HTML."""
import re
import sys
from pathlib import Path
import markdown
from typing import Optional

def convert_markdown_to_html(
    input_file: Path, 
    output_file: Optional[Path] = None,
    include_mermaid_js: bool = True
) -> Path:
    """
    Convert markdown file with mermaid diagrams to HTML.
    
    Args:
        input_file: Path to markdown file
        output_file: Path to output HTML file (defaults to same name with .html)
        include_mermaid_js: Whether to include mermaid.js for client-side rendering
    
    Returns:
        Path to generated HTML file
    """
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if output_file is None:
        output_file = input_file.with_suffix('.html')
    
    content = input_file.read_text()
    
    # Process mermaid blocks for HTML
    def replace_mermaid(match):
        mermaid_code = match.group(1)
        # Keep the mermaid code for client-side rendering
        return f'''
<div class="mermaid">
{mermaid_code}
</div>'''
    
    # Replace mermaid code blocks with div elements
    processed_content = re.sub(
        r'```mermaid\n(.*?)\n```', 
        replace_mermaid, 
        content, 
        flags=re.DOTALL
    )
    
    # Convert markdown to HTML with extensions
    md = markdown.Markdown(extensions=[
        'extra',        # Tables, footnotes, etc.
        'codehilite',   # Syntax highlighting
        'toc',          # Table of contents
        'sane_lists',   # Better list handling
        'nl2br',        # Newline to <br>
    ])
    html_content = md.convert(processed_content)
    
    # Create full HTML document
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_file.stem}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .content {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 24px;
            margin-bottom: 16px;
        }}
        h1 {{ border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ border-bottom: 1px solid #ecf0f1; padding-bottom: 8px; }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin-left: 0;
            padding-left: 20px;
            color: #555;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        .mermaid {{
            text-align: center;
            margin: 30px 0;
            background: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
        }}
        .mermaid svg {{
            max-width: 100%;
            height: auto;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .toc {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 20px;
        }}
        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
        .toc > ul {{
            padding-left: 0;
        }}
    </style>
    {'''
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        // Initialize mermaid with custom settings
        mermaid.initialize({ 
            startOnLoad: true,
            theme: 'default',
            themeVariables: {
                primaryColor: '#3498db',
                primaryTextColor: '#fff',
                primaryBorderColor: '#2c3e50',
                lineColor: '#333',
                secondaryColor: '#ecf0f1',
                tertiaryColor: '#f39c12'
            },
            flowchart: {
                htmlLabels: true,
                curve: 'basis'
            }
        });
    </script>''' if include_mermaid_js else ''}
</head>
<body>
    <div class="content">
        {html_content}
    </div>
    <footer style="text-align: center; padding: 20px; color: #666;">
        <small>Generated from {input_file.name}</small>
    </footer>
</body>
</html>"""
    
    # Write HTML file
    output_file.write_text(html_template)
    print(f"✅ Generated HTML: {output_file}")
    
    return output_file

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_html.py <input.md> [output.html]")
        print("\nExample:")
        print("  python markdown_to_html.py genes/human/JAK1/JAK1-pathway.md")
        print("  python markdown_to_html.py input.md output.html")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    
    try:
        result = convert_markdown_to_html(input_file, output_file)
        print(f"Successfully converted {input_file} to {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()