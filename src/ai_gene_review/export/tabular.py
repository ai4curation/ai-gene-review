"""Tabular exporter for gene review data."""

import yaml
from pathlib import Path
from typing import Dict, List, Any, Union, Optional
import pandas as pd

from ai_gene_review.datamodel.gene_review_model import GeneReview, ExistingAnnotation


class TabularExporter:
    """Export gene review data to tabular format, flattening existing_annotations."""

    def __init__(self):
        """Initialize the tabular exporter."""
        pass

    def export_from_file(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Export existing_annotations from a single gene review file to DataFrame.

        Args:
            file_path: Path to the gene review YAML file

        Returns:
            DataFrame with one row per existing annotation
        """
        file_path = Path(file_path)

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        # Parse into GeneReview model
        gene_review = GeneReview.model_validate(data)

        return self._flatten_existing_annotations(gene_review)

    def export_from_files(self, file_paths: List[Union[str, Path]]) -> pd.DataFrame:
        """
        Export existing_annotations from multiple gene review files to DataFrame.

        Args:
            file_paths: List of paths to gene review YAML files

        Returns:
            Combined DataFrame with one row per existing annotation from all files
        """
        all_dfs = []

        for file_path in file_paths:
            try:
                df = self.export_from_file(file_path)
                all_dfs.append(df)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue

        if not all_dfs:
            return pd.DataFrame()

        return pd.concat(all_dfs, ignore_index=True)

    def _flatten_existing_annotations(self, gene_review: GeneReview) -> pd.DataFrame:
        """
        Flatten existing_annotations from a GeneReview into tabular format.

        Args:
            gene_review: The parsed GeneReview object

        Returns:
            DataFrame with flattened annotation data
        """
        if not gene_review.existing_annotations:
            return pd.DataFrame()

        rows = []

        for annotation in gene_review.existing_annotations:
            row = self._flatten_annotation(annotation, gene_review)
            rows.append(row)

        return pd.DataFrame(rows)

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

        # Parent object information
        row["protein_id"] = gene_review.id
        row["gene_symbol"] = gene_review.gene_symbol
        row["taxon_id"] = gene_review.taxon.id if gene_review.taxon else None
        row["taxon_label"] = gene_review.taxon.label if gene_review.taxon else None

        # Add link fields
        row["uniprot_link"] = f"https://www.uniprot.org/uniprotkb/{gene_review.id}" if gene_review.id else None
        row["pathway_link"] = self._generate_pathway_link(gene_review)

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
        row["negated"] = annotation.negated
        
        # Derive method field from evidence type and reference
        row["method"] = self._derive_method(annotation.evidence_type, annotation.original_reference_id)

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

        # Extensions (flattened)
        if annotation.extensions:
            extension_strs = []
            for ext in annotation.extensions:
                if ext.predicate and ext.term:
                    ext_str = f"{ext.predicate}({ext.term.id}:{ext.term.label})"
                    extension_strs.append(ext_str)
            row["extensions"] = "; ".join(extension_strs) if extension_strs else None
        else:
            row["extensions"] = None

        # Review information (prefixed with review_)
        if annotation.review:
            review = annotation.review
            row["review_summary"] = review.summary
            row["review_action"] = review.action if review.action else None
            row["review_reason"] = review.reason
            
            # Flatten supported_by field
            if review.supported_by:
                supporting_texts = []
                reference_ids = []
                for sup in review.supported_by:
                    if sup.supporting_text:
                        supporting_texts.append(sup.supporting_text)
                    if sup.reference_id:
                        reference_ids.append(sup.reference_id)
                row["review_supporting_text"] = " | ".join(supporting_texts) if supporting_texts else None
                row["review_supporting_reference_ids"] = "; ".join(reference_ids) if reference_ids else None
            else:
                row["review_supporting_text"] = None
                row["review_supporting_reference_ids"] = None

            # Proposed replacement terms
            if review.proposed_replacement_terms:
                replacement_strs = []
                for term in review.proposed_replacement_terms:
                    replacement_strs.append(f"{term.id}:{term.label}")
                row["review_proposed_replacement_terms"] = "; ".join(replacement_strs)
            else:
                row["review_proposed_replacement_terms"] = None

            # Additional reference IDs
            if review.additional_reference_ids:
                row["review_additional_reference_ids"] = "; ".join(
                    review.additional_reference_ids
                )
            else:
                row["review_additional_reference_ids"] = None
        else:
            row["review_summary"] = None
            row["review_action"] = None
            row["review_reason"] = None
            row["review_supporting_text"] = None
            row["review_proposed_replacement_terms"] = None
            row["review_additional_reference_ids"] = None

        return row

    def _derive_method(self, evidence_type: Optional[str], reference_id: Optional[str]) -> str:
        """
        Derive the method field from evidence type and reference.
        
        Rules:
        - Experimental evidence codes (IDA, IPI, IMP, IGI, IEP, HTP, HDA, HMP, HGI, HEP) → "Experimental"
        - IEA → derive from reference (e.g., GO_REF:0000107 → "ARBA", GO_REF:0000002 → "InterPro2GO", etc.)
        - All other codes (IBA, ISS, IC, ISO, ISA, ISM, IGC, RCA, TAS, NAS, ND) → use code as-is
        
        Args:
            evidence_type: The evidence type code
            reference_id: The reference ID
            
        Returns:
            The derived method string
        """
        if not evidence_type:
            return "Unknown"
            
        # Define experimental evidence codes
        experimental_codes = {"IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
        
        if evidence_type in experimental_codes:
            return "Experimental"
        elif evidence_type == "IEA":
            # Map IEA references to specific methods
            if not reference_id:
                return "IEA"
            
            # Common IEA reference mappings
            iea_mappings = {
                "GO_REF:0000002": "InterPro2GO",
                "GO_REF:0000003": "EC2GO", 
                "GO_REF:0000004": "IEA",  # Generic IEA
                "GO_REF:0000043": "UniProtKB-KW",
                "GO_REF:0000044": "UniProtKB-SubCell",
                "GO_REF:0000104": "UniRule",
                "GO_REF:0000107": "ARBA",
                "GO_REF:0000108": "Ensembl",
                "GO_REF:0000116": "RHEA",
                "GO_REF:0000117": "ARBA",  # Also ARBA
                "GO_REF:0000118": "TreeGrafter",
                "GO_REF:0000119": "ARBA",  # Also ARBA
                "GO_REF:0000120": "Combined-IEA"
            }
            
            return iea_mappings.get(reference_id, "IEA-Other")
        else:
            # For all other evidence codes, use the code itself
            return evidence_type

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

    def export_to_csv(
        self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]
    ) -> None:
        """
        Export existing_annotations from multiple files to CSV.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output CSV file
        """
        df = self.export_from_files(file_paths)
        df.to_csv(output_path, index=False)

    def export_to_tsv(
        self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]
    ) -> None:
        """
        Export existing_annotations from multiple files to TSV.

        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output TSV file
        """
        df = self.export_from_files(file_paths)
        df.to_csv(output_path, sep="\t", index=False)
