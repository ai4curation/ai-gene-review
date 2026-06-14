# fosB notes

## 2026-06-13 AMR GO-gap review

Selected because the project deliberately excluded FosB from the FosA/glutathione transferase mapping. That was the right call: FosB is a Gram-positive thiol-S-transferase, not a glutathione transferase. UniProt A8Z522 names the protein "Metallothiol transferase FosB" and says it confers fosfomycin resistance by adding a thiol cofactor to fosfomycin [file:genes/STAAT/fosB/fosB-uniprot.txt]. The SaFosB mechanism paper directly supports the substrate distinction: it says bacillithiol is the preferred physiological thiol substrate, and that SaFosB is a divalent-metal-dependent bacillithiol-S-transferase conferring fosfomycin resistance [PMID:23256780].

Current GOA gives `GO:0016765` plus magnesium binding, cytoplasm, and response to antibiotic. That is not wrong, but it hides the clinically relevant activity. The right follow-up is a GO term request for a FosB-compatible fosfomycin bacillithiol-S-transferase / fosfomycin thiol-S-transferase activity. This should not be represented with `GO:0004364` glutathione transferase activity.
