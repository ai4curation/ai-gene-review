# AGO4 review notes


## 2026-09-20 full-gene IBA re-review

All 83 annotations assessed, including the IBA RNA-endonuclease claim, all binding/processing/complex rows, both source NOT process rows, localization evidence, and every Reactome cytosol row. Cytoplasmic RISC localization is supported independently of individual pathway reactions; specialized nucleus and membrane contexts remain non-core.

Existing OpenScientist report: AGO4-hypotheses/function-hypothesis-go-0004521/openscientist.md. The substantive findings are conserved active-site substitutions (Gly671 and Arg809) and retained TNRC6 recruitment. Cached UniProt sequence inspection confirms Gly671 and Arg809; primary PMID:15260970 supports absence of slicing. This does not refute RISC loading, guide/passenger unwinding or mRNA decay.

PMID:19966796 and PMID:22795694 full text show loading and slicing-independent activation by AGO4. PMID:18771919 full text directly reports comparable mRNA reduction by all four tethered AGOs. PMID:19383768 demonstrates all four AGOs bind TNRC6. Broad RNA binding, miRNA processing, pre-miRNA processing and mRNA catabolism restored to ACCEPT; one TNRC6 generic-binding row replaced with molecular adaptor activity.

QuickGO checked 2026-09-20: GO:0035196 is a process leading to generation of a functional miRNA and includes cleavage; GO:0031054 is conversion of a pre-miRNA transcript to mature miRNA. Neither definition restricts participation to the nuclease. URLs: https://www.ebi.ac.uk/QuickGO/term/GO:0035196 and https://www.ebi.ac.uk/QuickGO/term/GO:0031054.

Pending distinct adjudication: do later AGO4 decay/targeting experiments contradict the broad source NOT GO:0035279 and NOT GO:0090625 assertions, or does the original PMID:15260970 assay justify a narrower scope? The 2004 cache is abstract-only. Both source negations remain unchanged, with review UNDECIDED. Root owns the new focused report.

Verified the proximate IBA PANTHER nodes from cached WITH/FROM fields and revised structured propagation metadata to match final decisions; no relationship-field reasoning, donor-count argument, or invented topology reconstruction was used.

## 2026-09-21: focused decay report incorporated

Read the complete new OpenScientist report and CSV evidence/decision tables. Verified PMID:19838187 against PubMed and read cached full text: all four tethered human AGOs accelerate biphasic deadenylation in mouse NIH3T3 cells; guide recruitment is bypassed. The primary paper does not itself establish direct deadenylase recruitment by co-IP.

Live QuickGO retains both original BHF-UCL NOT IDA rows, contrary to the report. Both formal GO definitions describe guide-directed target cleavage; GO:0035279 has related deadenylation synonyms, which do not automatically override its definition. Thus the report supports mechanistic separation, but its blanket anti-NOT verdict is too strong. Both negations remain UNDECIDED with original source metadata preserved, pending ontology clarification and original full assay text. Snapshot: projects/IBA_REVIEW/rereview-2026-09-20/ago4-term-check.json. No replacement positive assertion or duplicate research run.
