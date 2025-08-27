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
        
        with open(file_path, 'r') as f:
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
    
    def _flatten_annotation(self, annotation: ExistingAnnotation, gene_review: GeneReview) -> Dict[str, Any]:
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
        row['protein_id'] = gene_review.id
        row['gene_symbol'] = gene_review.gene_symbol
        row['taxon_id'] = gene_review.taxon.id if gene_review.taxon else None
        row['taxon_label'] = gene_review.taxon.label if gene_review.taxon else None
        
        # Term information
        if annotation.term:
            row['term_id'] = annotation.term.id
            row['term_label'] = annotation.term.label
            row['term_description'] = annotation.term.description
            row['term_ontology'] = annotation.term.ontology
        else:
            row['term_id'] = None
            row['term_label'] = None
            row['term_description'] = None
            row['term_ontology'] = None
        
        # Evidence information
        row['evidence_type'] = annotation.evidence_type
        row['negated'] = annotation.negated
        
        # Original reference information
        if annotation.original_reference_id:
            ref_id = annotation.original_reference_id
            row['original_reference_id'] = ref_id
            
            # Find the matching reference in the parent's references list
            original_reference_title = self._find_reference_title(gene_review, ref_id)
            row['original_reference_title'] = original_reference_title
        else:
            row['original_reference_id'] = None
            row['original_reference_title'] = None
        
        # Supporting entities
        if annotation.supporting_entities:
            row['supporting_entities'] = '; '.join(annotation.supporting_entities)
        else:
            row['supporting_entities'] = None
        
        # Extensions (flattened)
        if annotation.extensions:
            extension_strs = []
            for ext in annotation.extensions:
                if ext.predicate and ext.term:
                    ext_str = f"{ext.predicate}({ext.term.id}:{ext.term.label})"
                    extension_strs.append(ext_str)
            row['extensions'] = '; '.join(extension_strs) if extension_strs else None
        else:
            row['extensions'] = None
        
        # Review information (prefixed with review_)
        if annotation.review:
            review = annotation.review
            row['review_summary'] = review.summary
            row['review_action'] = review.action if review.action else None
            row['review_reason'] = review.reason
            row['review_supporting_text'] = review.supporting_text
            
            # Proposed replacement terms
            if review.proposed_replacement_terms:
                replacement_strs = []
                for term in review.proposed_replacement_terms:
                    replacement_strs.append(f"{term.id}:{term.label}")
                row['review_proposed_replacement_terms'] = '; '.join(replacement_strs)
            else:
                row['review_proposed_replacement_terms'] = None
            
            # Additional reference IDs
            if review.additional_reference_ids:
                row['review_additional_reference_ids'] = '; '.join(review.additional_reference_ids)
            else:
                row['review_additional_reference_ids'] = None
        else:
            row['review_summary'] = None
            row['review_action'] = None
            row['review_reason'] = None
            row['review_supporting_text'] = None
            row['review_proposed_replacement_terms'] = None
            row['review_additional_reference_ids'] = None
        
        return row
    
    def _find_reference_title(self, gene_review: GeneReview, ref_id: str) -> Optional[str]:
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
    
    def export_to_csv(self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]) -> None:
        """
        Export existing_annotations from multiple files to CSV.
        
        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output CSV file
        """
        df = self.export_from_files(file_paths)
        df.to_csv(output_path, index=False)
    
    def export_to_tsv(self, file_paths: List[Union[str, Path]], output_path: Union[str, Path]) -> None:
        """
        Export existing_annotations from multiple files to TSV.
        
        Args:
            file_paths: List of paths to gene review YAML files
            output_path: Path for the output TSV file
        """
        df = self.export_from_files(file_paths)
        df.to_csv(output_path, sep='\t', index=False)