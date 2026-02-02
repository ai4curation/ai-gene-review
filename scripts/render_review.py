#!/usr/bin/env python
"""
Render gene review YAML files as markdown using linkml-renderer.

This script provides a command-line interface to convert gene review YAML files
into markdown format for easier reading and sharing.
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Optional


def render_yaml_to_markdown(
    input_file: Path,
    output_file: Optional[Path] = None,
    schema_file: Optional[Path] = None
) -> Path:
    """
    Render a gene review YAML file to markdown.
    
    Args:
        input_file: Path to the YAML file to render
        output_file: Optional path for the output markdown file. 
                    If not specified, uses input filename with .md extension
        schema_file: Optional path to the LinkML schema file.
                    If not specified, uses the default gene_review.yaml schema
    
    Returns:
        Path to the generated markdown file
        
    Raises:
        FileNotFoundError: If input file or schema file doesn't exist
        subprocess.CalledProcessError: If linkml-render command fails
    """
    # Validate input file
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Set default output file if not specified
    if output_file is None:
        if input_file.name.endswith('-ai-review.yaml'):
            output_file = input_file.parent / input_file.name.replace('-ai-review.yaml', '-ai-review.html')
        else:
            raise ValueError(f"Input file does not end with -ai-review.yaml: {input_file}")
    
    # Set default schema file if not specified
    if schema_file is None:
        # Assume we're running from project root or scripts directory
        project_root = Path(__file__).parent.parent
        schema_file = project_root / "src" / "ai_gene_review" / "schema" / "gene_review.yaml"
        
        if not schema_file.exists():
            raise FileNotFoundError(
                f"Default schema file not found at {schema_file}. "
                "Please specify schema path with --schema"
            )
    else:
        if not schema_file.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_file}")
    
    # Build the linkml-render command
    cmd = [
        "linkml-render",
        str(input_file),
        "--schema", str(schema_file),
        "--output", str(output_file),
        "--config", "config/render.yaml",
        "--output-format", "html",
        "--root", "GeneReview"
    ]
    
    # Run the command
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully rendered {input_file} to {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error rendering file: {e}", file=sys.stderr)
        if e.stderr:
            print(f"Error details: {e.stderr}", file=sys.stderr)
        raise


def render_all_reviews(
    directory: Path,
    schema_file: Optional[Path] = None,
    pattern: str = "*-ai-review.yaml"
) -> list[Path]:
    """
    Render all gene review YAML files in a directory tree to markdown.
    
    Args:
        directory: Root directory to search for YAML files
        schema_file: Optional path to the LinkML schema file
        pattern: File pattern to match (default: *-ai-review.yaml)
    
    Returns:
        List of paths to generated markdown files
    """
    output_files = []
    
    # Find all matching YAML files
    yaml_files = list(directory.rglob(pattern))
    
    if not yaml_files:
        print(f"No files matching pattern '{pattern}' found in {directory}")
        return output_files
    
    print(f"Found {len(yaml_files)} files to render")
    
    # Render each file
    for yaml_file in yaml_files:
        try:
            output_file = render_yaml_to_markdown(yaml_file, schema_file=schema_file)
            output_files.append(output_file)
        except Exception as e:
            print(f"Failed to render {yaml_file}: {e}", file=sys.stderr)
            continue
    
    print(f"\nSuccessfully rendered {len(output_files)} out of {len(yaml_files)} files")
    return output_files


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Render gene review YAML files as markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Render a single file
  python render_review.py genes/human/CFAP300/CFAP300-ai-review.yaml
  
  # Render a single file with custom output
  python render_review.py genes/human/CFAP300/CFAP300-ai-review.yaml -o CFAP300-review.md
  
  # Render all review files in a directory
  python render_review.py --all genes/
  
  # Use a custom schema file
  python render_review.py genes/human/CFAP300/CFAP300-ai-review.yaml --schema my_schema.yaml
        """
    )
    
    parser.add_argument(
        "input",
        type=Path,
        nargs="?",
        help="Input YAML file or directory (when using --all)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output markdown file (only for single file rendering)"
    )
    
    parser.add_argument(
        "-s", "--schema",
        type=Path,
        help="Path to LinkML schema file (default: src/ai_gene_review/schema/gene_review.yaml)"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Render all *-ai-review.yaml files in the specified directory"
    )
    
    parser.add_argument(
        "--pattern",
        default="*-ai-review.yaml",
        help="File pattern to match when using --all (default: *-ai-review.yaml)"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.input:
        parser.error("Input file or directory is required")
    
    if args.all and args.output:
        parser.error("Cannot specify output file when using --all")
    
    try:
        if args.all:
            # Render all files in directory
            if not args.input.is_dir():
                parser.error(f"When using --all, input must be a directory: {args.input}")
            render_all_reviews(args.input, schema_file=args.schema, pattern=args.pattern)
        else:
            # Render single file
            if not args.input.is_file():
                parser.error(f"Input file not found: {args.input}")
            render_yaml_to_markdown(args.input, output_file=args.output, schema_file=args.schema)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()