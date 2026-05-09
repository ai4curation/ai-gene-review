# Dnajb11 curation notes

Deep research status: `just deep-research-falcon mouse Dnajb11 --fallback perplexity-lite` was first run on 2026-05-03 and timed out after 600 seconds; the requested `perplexity-lite` fallback failed with a 401 insufficient-quota error. Per course correction, `just deep-research-falcon mouse Dnajb11 --timeout 1800 --fallback perplexity-lite` was then run one gene at a time and succeeded, producing `Dnajb11-deep-research-falcon.md`.

Core evidence: Dnajb11/ERdj3 is an endoplasmic reticulum DnaJ/Hsp40 co-chaperone for BiP/Hspa5, supporting secretory-protein folding, maturation, and quality control. UniProt names the protein "ER-associated Hsp40 co-chaperone" and places it in the "Endoplasmic reticulum lumen".

Falcon synthesis: The Falcon report verifies the same identity and core function, describing DNAJB11/ERdj3 as a soluble ER-luminal Hsp40/J-domain co-chaperone for BiP/HSPA5 that uses its HPD-containing J-domain to regulate BiP ATPase/client handling. It also highlights tetrameric assembly, Sec61/ER homeostasis connections, stress-induced secretion, and disease contexts such as PC1 processing in cystic kidney disease [file:mouse/Dnajb11/Dnajb11-deep-research-falcon.md].

BiP cochaperone evidence: Marcinowski et al. studied BiP substrate discrimination and state that "A major BiP cochaperone in antibody folding, ERdj3, modulated the conformational space of BiP in a nucleotide-dependent manner" [PMID:21217698].

ABBP2/apobec-1 evidence: The apoB mRNA editing paper states that ABBP-2 "binds to apobec-1" and that "Down-regulation of ABBP-2 expression in cultured cells inhibits endogenous apobec-1-mediated apoB mRNA editing" [PMID:11584023]. However, UniProt cautions that N-terminal GFP-tagged Dnajb11/ERdj3 failed ER targeting in the cited work, likely making the reported cytosolic/nuclear APOBEC1 interaction and apoB mRNA-editing annotations artifactual or unsupported for native Dnajb11 [file:mouse/Dnajb11/Dnajb11-uniprot.txt].

PRTG/neurogenesis evidence: The protogenin paper identifies ERdj3 as a PRTG ligand and reports that "Addition of purified ERdj3 protein into the P19 differentiation assay reduced neurogenesis" [PMID:20335479]. This supports a secreted/context-specific signaling role, not the core molecular function.

Curation rule: GO:0051082 unfolded protein binding is not the preferred term for DnaJ co-chaperone activity; GO:0044183 protein folding chaperone better captures the Hsp40 co-chaperone role. GO:0005515 protein binding is too generic when the evidence is BiP/Hsp70 or context-specific partners, and APOBEC1 binding should be removed because the native-protein evidence is compromised.
