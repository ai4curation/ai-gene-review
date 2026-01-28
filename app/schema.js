window.searchSchema = {
  "name": "GeneAnnotationReviewSchema",
  "description": "Browse AI reviews",
  "title": "Gene Annotation Review Browser",
  "id": "https://example.org/gene-annotation-review",
  "itemsPerPage": 50,
  "facetItemsToShow": 15,
  "customCss": ".sidebar { width: 340px; min-width: 340px; } .results-grid { grid-template-columns: 1fr; }",
  "searchableFields": [
    "gene_symbol",
    "protein_id",
    "status",
    "tags",
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
      "field": "status",
      "label": "Review Status",
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
      "field": "product_type",
      "label": "Gene Product Type",
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
      "field": "deep_research",
      "label": "Research",
      "type": "array",
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
    },
    {
      "field": "is_for_isoform",
      "label": "Isoform-Specific",
      "type": "boolean",
      "sortBy": "alphabetical"
    },
    {
      "field": "tags",
      "label": "Tags",
      "type": "array",
      "sortBy": "count"
    }
  ],
  "displayFields": [
    {
      "field": "gene_symbol",
      "label": "Gene",
      "type": "string"
    },
    {
      "field": "review_html_link",
      "label": "Review",
      "type": "url"
    },
    {
      "field": "uniprot_link",
      "label": "Link",
      "type": "url"
    },
    {
      "field": "protein_id",
      "label": "ID",
      "type": "string"
    },
    {
      "field": "product_type",
      "label": "Gene Product Type",
      "type": "string"
    },
    {
      "field": "status",
      "label": "Review Status",
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
      "field": "original_reference_id",
      "label": "Orig Ref",
      "type": "curie"
    },
    {
      "field": "original_reference_title",
      "label": "Orig Title",
      "type": "string"
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
    },
    {
      "field": "is_for_isoform",
      "label": "Isoform",
      "type": "boolean"
    },
    {
      "field": "isoform_id",
      "label": "Isoform ID",
      "type": "string"
    },
    {
      "field": "tags",
      "label": "Tags",
      "type": "array"
    }
  ]
};
window.dispatchEvent(new Event('searchDataReady'));
