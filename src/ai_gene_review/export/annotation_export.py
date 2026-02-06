"""Annotation exporter for gene review data.

Exports flattened annotation data to multiple formats:
- JSON (for general use)
- JSONL (one JSON object per line)
- DuckDB (queryable database)
- data.js (for browser app)

Example:
    >>> from ai_gene_review.export import AnnotationExporter
    >>> from pathlib import Path
    >>> exporter = AnnotationExporter()
    >>> files = list(Path('genes').glob('**/*-ai-review.yaml'))
    >>> # Get flat data as list of dicts
    >>> data = exporter.export_from_files(files)
    >>> # Export to various formats
    >>> exporter.export_to_json(files, 'output.json')
    >>> exporter.export_to_jsonl(files, 'output.jsonl')
    >>> exporter.export_to_duckdb(files, 'output.duckdb')
    >>> exporter.export_to_datajs(files, 'app/data.js')
"""

import json
import re
import yaml
from pathlib import Path
from typing import Dict, List, Any, Union, Optional

from ai_gene_review.datamodel.gene_review_model import GeneReview, ExistingAnnotation


class AnnotationExporter:
    """Export gene review annotations to multiple formats.

    The core method `export_from_files()` returns a list of flat dictionaries,
    one per annotation. This can then be exported to various formats.
    """

    def __init__(self):
        """Initialize the annotation exporter."""
        pass

    def export_from_file(self, file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        Export existing_annotations from a single gene review file to list of dicts.

        Args:
            file_path: Path to the gene review YAML file

        Returns:
            List of dictionaries with one dict per existing annotation
        """
        file_path = Path(file_path)

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        # Parse into GeneReview model
        gene_review = GeneReview.model_validate(data)

        return self._flatten_existing_annotations(gene_review)

    def export_from_files(
        self, file_paths: List[Union[str, Path]]
    ) -> List[Dict[str, Any]]:
        """
        Export existing_annotations from multiple gene review files to list of dicts.

        This is the core method - returns flat data that can be used for any output format.

        Args:
            file_paths: List of paths to gene review YAML files

        Returns:
            Combined list with one dict per existing annotation from all files
        """
        all_annotations = []

        for file_path in file_paths:
            try:
                annotations = self.export_from_file(file_path)
                all_annotations.extend(annotations)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue

        return all_annotations

    # ========== Output Format Methods ==========

    def export_to_json(
        self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]
    ) -> int:
        """
        Export existing_annotations from multiple files to JSON.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output JSON file

        Returns:
            Number of annotations exported
        """
        annotations = self.export_from_files(file_paths)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(annotations, f, indent=2, default=str)

        return len(annotations)

    def export_to_jsonl(
        self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]
    ) -> int:
        """
        Export existing_annotations to JSONL (one JSON object per line).

        JSONL is useful for streaming processing and is easily loaded by DuckDB.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output JSONL file

        Returns:
            Number of annotations exported
        """
        annotations = self.export_from_files(file_paths)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            for ann in annotations:
                f.write(json.dumps(ann, default=str) + "\n")

        return len(annotations)

    def export_to_duckdb(
        self,
        file_paths: List[Union[str, Path]],
        output_path: Union[str, Path],
        table_name: str = "annotations",
        include_redundancy: bool = True,
        go_adapter: str = "sqlite:obo:go",
    ) -> int:
        """
        Export existing_annotations to a DuckDB database.

        Creates a queryable database that supports SQL queries like:
            SELECT taxon_label, is_swissprot, "review.action", COUNT(*)
            FROM annotations
            WHERE original_reference_id = 'GO_REF:0000043'
            GROUP BY ALL

        If include_redundancy=True, also creates a `redundant_with` table showing
        which annotations are redundant with more specific annotations.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output DuckDB file
            table_name: Name of the table to create (default: 'annotations')
            include_redundancy: Whether to compute and include redundancy table
            go_adapter: OAK adapter string for GO ontology (default: sqlite:obo:go)

        Returns:
            Number of annotations exported
        """
        try:
            import duckdb
            import pandas as pd
        except ImportError as e:
            raise ImportError(
                "duckdb and pandas are required for DuckDB export. "
                "Install with: uv add duckdb pandas"
            ) from e

        annotations = self.export_from_files(file_paths)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Remove existing file if present
        if output_path.exists():
            output_path.unlink()

        # Convert to DataFrame for DuckDB ingestion
        df = pd.DataFrame(annotations)  # noqa: F841 (used by DuckDB SQL)

        conn = duckdb.connect(str(output_path))

        # Create table from DataFrame
        conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")

        # Create useful indexes
        conn.execute(f"CREATE INDEX idx_gene ON {table_name}(gene_symbol)")
        conn.execute(f"CREATE INDEX idx_taxon ON {table_name}(taxon_label)")
        conn.execute(f"CREATE INDEX idx_action ON {table_name}(\"review.action\")")
        conn.execute(f"CREATE INDEX idx_ref ON {table_name}(original_reference_id)")
        conn.execute(f"CREATE INDEX idx_term ON {table_name}(term_id)")

        # Compute and add redundancy table if requested
        if include_redundancy:
            try:
                redundancies = self.compute_redundancy(annotations, go_adapter)
                if redundancies:
                    redundancy_df = pd.DataFrame(redundancies)  # noqa: F841 (used by DuckDB SQL)
                    conn.execute("CREATE TABLE redundant_with AS SELECT * FROM redundancy_df")
                    conn.execute("CREATE INDEX idx_red_gene ON redundant_with(gene_symbol)")
                    conn.execute("CREATE INDEX idx_red_general ON redundant_with(general_term_id)")
                    conn.execute("CREATE INDEX idx_red_specific ON redundant_with(specific_term_id)")
                    print(f"  Created redundant_with table with {len(redundancies)} relationships")
            except Exception as e:
                print(f"  Warning: Could not compute redundancy: {e}")

        conn.close()

        return len(annotations)

    def compute_redundancy(
        self,
        annotations: List[Dict[str, Any]],
        go_adapter: str = "sqlite:obo:go",
    ) -> List[Dict[str, Any]]:
        """
        Compute redundancy relationships between annotations.

        An annotation A1 is redundant with A2 if:
        - They refer to the same gene (protein_id)
        - A1 != A2
        - A2's term is more specific than A1's term (A2 is_a/part_of A1)
        - Or A2's term regulates A1's term

        Args:
            annotations: List of flattened annotation dicts
            go_adapter: OAK adapter string for GO ontology

        Returns:
            List of redundancy relationship dicts with fields:
            - gene_symbol, protein_id
            - general_annotation_id, general_term_id, general_term_label
            - specific_annotation_id, specific_term_id, specific_term_label
            - relationship: EXACT, ISA_PARTOF, REGULATES
        """
        try:
            from oaklib import get_adapter
        except ImportError as e:
            raise ImportError(
                "oaklib is required for redundancy computation. "
                "Install with: uv add oaklib"
            ) from e

        print(f"  Loading GO ontology from {go_adapter}...")
        adapter = get_adapter(go_adapter)

        # Build closure caches
        print("  Building is_a/part_of closure cache...")
        isa_partof_closure = self._build_closure_cache(
            adapter,
            predicates=["rdfs:subClassOf", "BFO:0000050"]  # is_a, part_of
        )

        print("  Building regulates closure cache...")
        regulates_closure = self._build_closure_cache(
            adapter,
            predicates=["RO:0002211", "RO:0002212", "RO:0002213"]  # regulates, neg_reg, pos_reg
        )

        # Group annotations by gene
        by_gene: Dict[str, List[Dict]] = {}
        for ann in annotations:
            gene_key = ann.get("protein_id") or ann.get("gene_symbol")
            if gene_key and ann.get("term_id"):
                by_gene.setdefault(gene_key, []).append(ann)

        redundancies = []
        genes_checked = 0

        print(f"  Checking {len(by_gene)} genes for redundancy...")
        for gene_key, gene_anns in by_gene.items():
            genes_checked += 1
            if genes_checked % 100 == 0:
                print(f"    Checked {genes_checked}/{len(by_gene)} genes...")


            # Check each pair
            for ann1 in gene_anns:
                term1 = ann1.get("term_id")
                if not term1:
                    continue

                for ann2 in gene_anns:
                    term2 = ann2.get("term_id")
                    if not term2 or ann1["id"] == ann2["id"]:
                        continue

                    # Check if term2 is more specific than term1
                    relationship = None

                    if term1 == term2:
                        # Same term - only redundant if different evidence/reference
                        if ann1.get("evidence_type") != ann2.get("evidence_type") or \
                           ann1.get("original_reference_id") != ann2.get("original_reference_id"):
                            relationship = "EXACT"
                    elif term2 in isa_partof_closure.get(term1, set()):
                        # term2 is_a/part_of term1, so term1 is more general
                        relationship = "ISA_PARTOF"
                    elif term2 in regulates_closure.get(term1, set()):
                        # term2 regulates term1
                        relationship = "REGULATES"

                    if relationship:
                        redundancies.append({
                            "gene_symbol": ann1.get("gene_symbol"),
                            "protein_id": ann1.get("protein_id"),
                            "general_annotation_id": ann1["id"],
                            "general_term_id": term1,
                            "general_term_label": ann1.get("term_label"),
                            "specific_annotation_id": ann2["id"],
                            "specific_term_id": term2,
                            "specific_term_label": ann2.get("term_label"),
                            "relationship": relationship,
                        })

        print(f"  Found {len(redundancies)} redundancy relationships")
        return redundancies

    def _build_closure_cache(
        self,
        adapter,
        predicates: List[str],
    ) -> Dict[str, set]:
        """
        Build a cache mapping each term to its descendants via specified predicates.

        Args:
            adapter: OAK adapter
            predicates: List of predicate CURIEs to traverse

        Returns:
            Dict mapping term_id -> set of descendant term_ids
        """
        from collections import defaultdict

        # Get all edges for the predicates
        closure: Dict[str, set] = defaultdict(set)

        # Use the adapter's ancestors method which handles transitivity
        # We'll iterate over GO terms and cache their ancestors
        try:
            # Get all GO terms
            for term in adapter.entities():
                if not term.startswith("GO:"):
                    continue
                # Get ancestors via the predicates
                for ancestor in adapter.ancestors(term, predicates=predicates):
                    if ancestor != term and ancestor.startswith("GO:"):
                        # ancestor -> {descendants}
                        closure[ancestor].add(term)
        except Exception as e:
            print(f"    Warning: Error building closure: {e}")

        return dict(closure)

    def export_to_datajs(
        self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]
    ) -> int:
        """
        Export existing_annotations to data.js for the browser app.

        Creates a JavaScript file that sets window.searchData to the annotation array.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output data.js file

        Returns:
            Number of annotations exported
        """
        annotations = self.export_from_files(file_paths)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            f.write("window.searchData = ")
            json.dump(annotations, f, indent=2, default=str)
            f.write(";\n")
            f.write("window.dispatchEvent(new Event('searchDataReady'));\n")

        return len(annotations)

    # ========== Internal Helper Methods ==========

    def _flatten_existing_annotations(
        self, gene_review: GeneReview
    ) -> List[Dict[str, Any]]:
        """
        Flatten existing_annotations from a GeneReview into list of dicts.

        Args:
            gene_review: The parsed GeneReview object

        Returns:
            List of flattened annotation dictionaries
        """
        if not gene_review.existing_annotations:
            return []

        annotations = []

        for annotation in gene_review.existing_annotations:
            flat_annotation = self._flatten_annotation(annotation, gene_review)
            annotations.append(flat_annotation)

        return annotations

    def _flatten_annotation(
        self, annotation: ExistingAnnotation, gene_review: GeneReview
    ) -> Dict[str, Any]:
        """
        Flatten a single existing annotation into a dictionary.

        Args:
            annotation: The ExistingAnnotation object
            gene_review: The parent GeneReview object

        Returns:
            Flattened dictionary with all relevant fields
        """
        row: Dict[str, Any] = {}

        # Create a unique ID for this annotation
        if gene_review.id and annotation.term and annotation.term.id:
            row["id"] = (
                f"{gene_review.id}_{annotation.term.id}_{annotation.evidence_type or 'NA'}"
            )
        else:
            row["id"] = f"{gene_review.id}_annotation_{id(annotation)}"

        # Parent object information
        row["protein_id"] = gene_review.id
        row["gene_symbol"] = gene_review.gene_symbol
        row["product_type"] = gene_review.product_type if gene_review.product_type else "PROTEIN"
        row["status"] = gene_review.status if gene_review.status else None
        row["taxon_id"] = gene_review.taxon.id if gene_review.taxon else None
        row["taxon_label"] = gene_review.taxon.label if gene_review.taxon else None
        row["tags"] = gene_review.tags if gene_review.tags else []

        # Swiss-Prot status (read from uniprot.txt file)
        row["is_swissprot"] = self._is_swissprot(gene_review)

        # Add link fields
        # For ncRNAs, link to RNAcentral; for proteins, link to UniProt
        if gene_review.product_type and gene_review.product_type not in ["PROTEIN", "PSEUDOGENE"]:
            # ncRNA - use RNAcentral URL (keep field name as uniprot_link for compatibility)
            row["uniprot_link"] = f"https://rnacentral.org/rna/{gene_review.id}" if gene_review.id else None
        else:
            # Protein or pseudogene - use UniProt URL
            row["uniprot_link"] = f"https://www.uniprot.org/uniprotkb/{gene_review.id}" if gene_review.id else None
        row["pathway_link"] = self._generate_pathway_link(gene_review)
        row["review_html_link"] = self._generate_review_html_link(gene_review)

        # Deep research methods available for this gene
        row["deep_research"] = self._find_deep_research_methods(gene_review)

        # Term information
        if annotation.term:
            row["term_id"] = annotation.term.id
            row["term_label"] = annotation.term.label
            row["term_description"] = annotation.term.description
            row["term_ontology"] = annotation.term.ontology
        else:
            row["term_id"] = None
            row["term_label"] = None
            row["term_description"] = None
            row["term_ontology"] = None

        # Evidence information
        row["evidence_type"] = annotation.evidence_type
        row["negated"] = annotation.negated or False

        # Isoform-specific annotation flag
        # True if this annotation was made on a specific isoform (e.g., P19544-1)
        row["is_for_isoform"] = bool(annotation.isoform) if hasattr(annotation, 'isoform') else False
        row["isoform_id"] = annotation.isoform if hasattr(annotation, 'isoform') and annotation.isoform else None

        # Original reference information
        if annotation.original_reference_id:
            ref_id = annotation.original_reference_id
            row["original_reference_id"] = ref_id

            # Find the matching reference in the parent's references list
            original_reference_title = self._find_reference_title(gene_review, ref_id)
            row["original_reference_title"] = original_reference_title
        else:
            row["original_reference_id"] = None
            row["original_reference_title"] = None

        # Supporting entities
        if annotation.supporting_entities:
            row["supporting_entities"] = "; ".join(annotation.supporting_entities)
        else:
            row["supporting_entities"] = None

        # Extensions (as string for simplicity)
        if annotation.extensions:
            extension_strs = []
            for ext in annotation.extensions:
                if ext.predicate and ext.term:
                    ext_str = f"{ext.predicate}({ext.term.id}:{ext.term.label})"
                    extension_strs.append(ext_str)
            row["extensions"] = "; ".join(extension_strs) if extension_strs else None
        else:
            row["extensions"] = None

        # Review information (flattened with dot notation for compatibility)
        if annotation.review:
            review = annotation.review
            row["review.summary"] = review.summary
            row["review.action"] = review.action if review.action else None
            row["review.reason"] = review.reason

            # Flatten supported_by field
            if review.supported_by:
                supporting_texts = []
                reference_ids = []
                for sup in review.supported_by:
                    if sup.supporting_text:
                        supporting_texts.append(sup.supporting_text)
                    if sup.reference_id:
                        reference_ids.append(sup.reference_id)
                row["review.supporting_text"] = " | ".join(supporting_texts) if supporting_texts else None
                row["review.supporting_reference_ids"] = "; ".join(reference_ids) if reference_ids else None
            else:
                row["review.supporting_text"] = None
                row["review.supporting_reference_ids"] = None

            # Proposed replacement terms
            if review.proposed_replacement_terms:
                replacements = []
                for term in review.proposed_replacement_terms:
                    replacements.append(f"{term.id}:{term.label}")
                row["review.proposed_replacement_terms"] = "; ".join(replacements)
            else:
                row["review.proposed_replacement_terms"] = None

            # Additional reference IDs
            if review.additional_reference_ids:
                row["review.additional_reference_ids"] = "; ".join(
                    review.additional_reference_ids
                )
            else:
                row["review.additional_reference_ids"] = None
        else:
            row["review.summary"] = None
            row["review.action"] = None
            row["review.reason"] = None
            row["review.supporting_text"] = None
            row["review.proposed_replacement_terms"] = None
            row["review.additional_reference_ids"] = None

        return row

    def _find_deep_research_methods(self, gene_review: GeneReview) -> List[str]:
        """
        Find which deep research methods are available for a gene.

        Looks for files matching pattern: GENE-deep-research[-METHOD].md
        If no METHOD suffix, assumes 'openai'.

        Args:
            gene_review: The GeneReview object

        Returns:
            List of method names (e.g., ['openai', 'perplexity', 'gemini'])
        """
        if not gene_review.gene_symbol:
            return []

        methods = []

        # Find the gene directory
        gene_dir = self._find_gene_directory(gene_review)
        if not gene_dir or not gene_dir.exists():
            return []

        # Pattern: GENE-deep-research[-METHOD].md
        gene_symbol = gene_review.gene_symbol
        pattern = re.compile(
            rf"^{re.escape(gene_symbol)}-deep-research(?:-([a-zA-Z0-9-]+))?\.md$"
        )

        for file_path in gene_dir.iterdir():
            if not file_path.is_file():
                continue
            match = pattern.match(file_path.name)
            if match:
                method = match.group(1)
                if method is None:
                    methods.append("openai")
                else:
                    methods.append(method)

        return sorted(set(methods))

    def _is_swissprot(self, gene_review: GeneReview) -> Optional[bool]:
        """
        Determine if the protein is in Swiss-Prot (reviewed) or TrEMBL (unreviewed).

        Reads the cached uniprot.txt file and checks the first line for
        "Reviewed;" (Swiss-Prot) or "Unreviewed;" (TrEMBL).

        Args:
            gene_review: The GeneReview object

        Returns:
            True if Swiss-Prot, False if TrEMBL, None if unknown
        """
        gene_dir = self._find_gene_directory(gene_review)
        if not gene_dir:
            return None

        # Look for the uniprot.txt file
        uniprot_file = gene_dir / f"{gene_review.gene_symbol}-uniprot.txt"
        if not uniprot_file.exists():
            return None

        try:
            with open(uniprot_file, "r") as f:
                first_line = f.readline()
                if "Reviewed;" in first_line:
                    return True
                elif "Unreviewed;" in first_line:
                    return False
        except Exception:
            pass

        return None

    def _find_gene_directory(self, gene_review: GeneReview) -> Optional[Path]:
        """
        Find the directory for a gene based on its taxon.

        Args:
            gene_review: The GeneReview object

        Returns:
            Path to the gene directory, or None if not found
        """
        if not gene_review.gene_symbol:
            return None

        organism_mapping = {
            "NCBITaxon:9606": "human",
            "NCBITaxon:10090": "mouse",
            "NCBITaxon:559292": "yeast",
            "NCBITaxon:4896": "pombe",
            "NCBITaxon:7227": "fly",
            "NCBITaxon:6239": "worm",
            "NCBITaxon:10116": "rat",
            "NCBITaxon:3702": "ARATH",
        }

        gene_symbol = gene_review.gene_symbol

        # Try mapped organism directory first
        if gene_review.taxon and gene_review.taxon.id:
            organism_dir = organism_mapping.get(gene_review.taxon.id)
            if organism_dir:
                gene_path = Path("genes") / organism_dir / gene_symbol
                if gene_path.exists():
                    return gene_path

        # Search all organism directories
        genes_root = Path("genes")
        if genes_root.exists():
            for org_path in genes_root.iterdir():
                if org_path.is_dir():
                    gene_path = org_path / gene_symbol
                    if gene_path.exists():
                        return gene_path

        return None

    def _find_reference_title(
        self, gene_review: GeneReview, ref_id: str
    ) -> Optional[str]:
        """
        Find the title of a reference by its ID in the gene review's reference list.

        Args:
            gene_review: The GeneReview object
            ref_id: The reference ID to find

        Returns:
            The reference title if found, None otherwise
        """
        if not gene_review.references:
            return None

        for ref in gene_review.references:
            if ref.id == ref_id:
                return ref.title

        return None

    def _generate_pathway_link(self, gene_review: GeneReview) -> Optional[str]:
        """
        Generate a relative pathway link for the gene review.

        Args:
            gene_review: The GeneReview object

        Returns:
            Relative pathway link if pathway file exists, None otherwise
        """
        if not gene_review.gene_symbol:
            return None

        # We need to determine the organism/species directory from the taxon
        # This is a heuristic mapping - we'll use common patterns
        organism_mapping = {
            "NCBITaxon:9606": "human",
            "NCBITaxon:10090": "mouse",
            "NCBITaxon:559292": "yeast",
            "NCBITaxon:4896": "pombe",
            "NCBITaxon:7227": "fly",
            "NCBITaxon:6239": "worm",
            "NCBITaxon:8355": "rat",  # Xenopus tropicalis -> rat directory used
        }

        # Try to map taxon to organism directory
        organism_dir = None
        if gene_review.taxon and gene_review.taxon.id:
            organism_dir = organism_mapping.get(gene_review.taxon.id)

        # If no mapping found, try to infer from common patterns
        if not organism_dir:
            # Look for pathway file in multiple possible locations
            possible_paths = [
                f"../genes/human/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
                f"../genes/mouse/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
                f"../genes/yeast/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
                f"../genes/pombe/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
                f"../genes/fly/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
                f"../genes/worm/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html",
            ]

            # Check if any of these files exist
            for path in possible_paths:
                # Convert relative path to absolute to check existence
                abs_path = Path("genes") / path.replace("../genes/", "")
                if abs_path.exists():
                    return path

            # If none found, try organism codes (BPZF4, ARATH, etc.)
            # This is for bacterial/other organism codes
            gene_symbol = gene_review.gene_symbol
            for org_path in Path("genes").iterdir():
                if org_path.is_dir() and org_path.name not in ["human", "mouse", "yeast", "pombe", "fly", "worm", "rat"]:
                    possible_file = org_path / gene_symbol / f"{gene_symbol}-pathway.html"
                    if possible_file.exists():
                        return f"../genes/{org_path.name}/{gene_symbol}/{gene_symbol}-pathway.html"

            return None

        # Use mapped organism directory
        pathway_path = f"../genes/{organism_dir}/{gene_review.gene_symbol}/{gene_review.gene_symbol}-pathway.html"

        # Check if the file exists
        abs_path = Path("genes") / organism_dir / gene_review.gene_symbol / f"{gene_review.gene_symbol}-pathway.html"
        if abs_path.exists():
            return pathway_path

        return None

    def _generate_review_html_link(self, gene_review: GeneReview) -> Optional[str]:
        """
        Generate a relative link to the gene review HTML page.

        Args:
            gene_review: The GeneReview object

        Returns:
            Relative link to the review HTML if it exists, None otherwise
        """
        if not gene_review.gene_symbol:
            return None

        # We need to determine the organism/species directory from the taxon
        # This is a heuristic mapping - we'll use common patterns
        organism_mapping = {
            "NCBITaxon:9606": "human",
            "NCBITaxon:10090": "mouse",
            "NCBITaxon:559292": "yeast",
            "NCBITaxon:4896": "pombe",
            "NCBITaxon:7227": "fly",
            "NCBITaxon:6239": "worm",
            "NCBITaxon:8355": "XENTR",  # Xenopus tropicalis
            "NCBITaxon:3702": "ARATH",  # Arabidopsis thaliana
        }

        # Try to map taxon to organism directory
        organism_dir = None
        if gene_review.taxon and gene_review.taxon.id:
            organism_dir = organism_mapping.get(gene_review.taxon.id)

        # If no mapping found, try to find the review file in all directories
        if not organism_dir:
            # Look for review file in multiple possible locations
            possible_paths = [
                f"../genes/human/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/mouse/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/yeast/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/pombe/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/fly/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/worm/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
                f"../genes/XENTR/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html",
            ]

            # Check if any of these files exist
            for path in possible_paths:
                # Convert relative path to absolute to check existence
                abs_path = Path("genes") / path.replace("../genes/", "")
                if abs_path.exists():
                    return path

            # If none found, try organism codes (BPZF4, ARATH, etc.)
            # This is for bacterial/other organism codes
            gene_symbol = gene_review.gene_symbol
            for org_path in Path("genes").iterdir():
                if org_path.is_dir():
                    possible_file = org_path / gene_symbol / f"{gene_symbol}-ai-review.html"
                    if possible_file.exists():
                        return f"../genes/{org_path.name}/{gene_symbol}/{gene_symbol}-ai-review.html"

            return None

        # Use mapped organism directory
        review_path = f"../genes/{organism_dir}/{gene_review.gene_symbol}/{gene_review.gene_symbol}-ai-review.html"

        # Check if the file exists
        abs_path = Path("genes") / organism_dir / gene_review.gene_symbol / f"{gene_review.gene_symbol}-ai-review.html"
        if abs_path.exists():
            return review_path

        return None


# Backwards compatibility alias
JSONExporter = AnnotationExporter
