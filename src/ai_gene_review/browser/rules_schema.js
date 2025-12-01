window.searchSchema = {
  "name": "ARBARuleReviewSchema",
  "description": "Browse ARBA rule reviews",
  "title": "ARBA Rule Review Browser",
  "id": "https://example.org/arba-rule-review",
  "searchableFields": [
    "rule_id",
    "description",
    "status",
    "action",
    "go_term_ids",
    "go_term_labels",
    "parsimony_assessment",
    "literature_support"
  ],
  "searchPlaceholder": "Search rules...",
  "facets": [
    {
      "field": "status",
      "label": "Review Status",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "action",
      "label": "Review Action",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "parsimony_assessment",
      "label": "Parsimony",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "literature_support",
      "label": "Literature Support",
      "type": "string",
      "sortBy": "alphabetical"
    },
    {
      "field": "is_reviewed",
      "label": "Has Review",
      "type": "boolean",
      "sortBy": "alphabetical"
    },
    {
      "field": "go_term_labels",
      "label": "GO Term",
      "type": "array",
      "sortBy": "count"
    },
    {
      "field": "num_condition_sets",
      "label": "Condition Sets",
      "type": "integer",
      "sortBy": "count"
    },
    {
      "field": "num_entries",
      "label": "Entries",
      "type": "integer",
      "sortBy": "count"
    },
    {
      "field": "confidence",
      "label": "Confidence",
      "type": "integer",
      "sortBy": "count"
    }
  ],
  "displayFields": [
    {
      "field": "rule_id",
      "label": "Rule ID",
      "type": "string"
    },
    {
      "field": "review_link",
      "label": "Review",
      "type": "url"
    },
    {
      "field": "description",
      "label": "Description",
      "type": "string"
    },
    {
      "field": "status",
      "label": "Status",
      "type": "string"
    },
    {
      "field": "action",
      "label": "Action",
      "type": "string"
    },
    {
      "field": "go_term_ids",
      "label": "GO Terms",
      "type": "array"
    },
    {
      "field": "parsimony_assessment",
      "label": "Parsimony",
      "type": "string"
    },
    {
      "field": "literature_support",
      "label": "Literature",
      "type": "string"
    },
    {
      "field": "num_condition_sets",
      "label": "# Condition Sets",
      "type": "string"
    },
    {
      "field": "num_entries",
      "label": "# Entries",
      "type": "string"
    },
    {
      "field": "confidence",
      "label": "Confidence",
      "type": "string"
    }
  ]
};
window.dispatchEvent(new Event('searchDataReady'));
