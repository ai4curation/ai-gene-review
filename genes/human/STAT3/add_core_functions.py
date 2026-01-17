#!/usr/bin/env python3
"""
Add core_functions section to STAT3 review.
"""

import yaml
from pathlib import Path

# Load the review file
review_path = Path("/Users/cjm/repos/ai-gene-review/genes/human/STAT3/STAT3-ai-review.yaml")
with open(review_path) as f:
    data = yaml.safe_load(f)

# Add core_functions section
data["core_functions"] = [
    {
        "molecular_function": {
            "id": "GO:0000981",
            "label": "DNA-binding transcription factor activity, RNA polymerase II-specific"
        },
        "summary": "STAT3 is a transcription factor that binds DNA at GAS (gamma-activated sequence) elements in target gene promoters to regulate transcription.",
        "supporting_evidence": [
            "file:human/STAT3/STAT3-deep-research-falcon.md"
        ]
    },
    {
        "molecular_function": {
            "id": "GO:0042803",
            "label": "protein homodimerization activity"
        },
        "summary": "STAT3 forms homodimers via reciprocal SH2 domain-phosphotyrosine (Y705) interactions, which is essential for nuclear translocation and DNA binding.",
        "supporting_evidence": [
            "file:human/STAT3/STAT3-deep-research-falcon.md"
        ]
    },
    {
        "biological_process": {
            "id": "GO:0007259",
            "label": "cell surface receptor signaling pathway via JAK-STAT"
        },
        "summary": "STAT3 is activated by tyrosine phosphorylation (Y705) by JAK kinases (JAK1/2/3, TYK2) in response to cytokine receptor engagement, particularly IL-6 family cytokines.",
        "supporting_evidence": [
            "file:human/STAT3/STAT3-deep-research-falcon.md"
        ]
    },
    {
        "biological_process": {
            "id": "GO:0070106",
            "label": "interleukin-6-mediated signaling pathway"
        },
        "summary": "IL-6 signaling through IL-6Rα/gp130 is the canonical STAT3-activating pathway. IL-6 engagement leads to JAK activation, STAT3 Y705 phosphorylation, dimerization, nuclear translocation, and transcriptional activation of target genes including MYC, CCND1, BCL-XL, and VEGF.",
        "supporting_evidence": [
            "file:human/STAT3/STAT3-deep-research-falcon.md"
        ]
    },
    {
        "biological_process": {
            "id": "GO:0048708",
            "label": "astrocyte differentiation"
        },
        "summary": "STAT3 activation promotes astrocyte differentiation and gliogenesis, switching neural progenitor cells from neurogenesis to gliogenesis during development.",
        "supporting_evidence": [
            "file:human/STAT3/STAT3-deep-research-falcon.md"
        ]
    }
]

# Add aliases
data["aliases"] = ["APRF", "Acute-phase response factor"]

# Write output
with open(review_path, "w") as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)

print(f"Added core_functions section with {len(data['core_functions'])} entries")
print("Added aliases")
print(f"File written to {review_path}")
