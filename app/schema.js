window.searchSchema = {
  "name": "GeneAnnotationReviewSchema",
  "description": "Browse AI reviews",
  "title": "Gene Annotation Review Browser",
  "id": "https://example.org/gene-annotation-review",
  "searchableFields": [
    "gene_symbol",
    "protein_id",
    "term_label",
    "term_id",
    "taxon_label",
    "original_reference_title",
    "review.supporting_text"
  ],
  "searchPlaceholder": "Search annotations...",
  "facets": [
    {
      "field": "review.action",
      "label": "Review Action",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "gene_symbol",
      "label": "Gene Symbol",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "taxon_label",
      "label": "Species",
      "type": "string",
      "sortBy": "count"
    },
    {
      "field": "term_ontology",
      "label": "Ontology Aspect",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "evidence_type",
      "label": "Evidence Code",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "original_reference_title",
      "label": "Title",
      "type": "string",
      "sortBy": "count"
    },
    {
      "field": "term_label",
      "label": "Term",
      "type": "string",
      "sortBy": "count"
    },
    {
      "field": "negated",
      "label": "Negated",
      "type": "boolean",
      "sortBy": "alphabetical"
    }
  ],
  "displayFields": [
    {
      "field": "gene_symbol",
      "label": "Gene",
      "type": "string"
    },
    {
      "field": "uniprot_link",
      "label": "Uniprot",
      "type": "url"
    },
    {
      "field": "protein_id",
      "label": "Protein",
      "type": "string"
    },
    {
      "field": "term_label",
      "label": "GO Term",
      "type": "string"
    },
    {
      "field": "term_id",
      "label": "GO ID",
      "type": "curie"
    },
    {
      "field": "evidence_type",
      "label": "Evidence",
      "type": "string"
    },
    {
      "field": "pathway_link",
      "label": "Pathway",
      "type": "url"
    },
    {
      "field": "review.summary",
      "label": "Summary",
      "type": "string"
    },
    {
      "field": "review.action",
      "label": "Action",
      "type": "string"
    },
    {
      "field": "review.reason",
      "label": "Reason",
      "type": "string"
    },
    {
      "field": "review.supporting_text",
      "label": "Ref Text",
      "type": "string"
    },
    {
      "field": "review.supporting_reference_ids",
      "label": "RefIDs",
      "type": "curie"
    },
    {
      "field": "review.proposed_replacement_terms",
      "label": "Replacements",
      "type": "string"
    }
  ]
};
window.dispatchEvent(new Event('searchDataReady'));
