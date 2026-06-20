# DNAJC28 (C21orf55 / C21orf78) research notes

## Identity
- UniProt Q9NX36 (DJC28_HUMAN), 388 aa. HGNC:1297. Chromosome 21. Synonyms C21orf55, C21orf78.
- J-domain protein (HSP40/DnaJ family, subfamily C member 28). J domain at residues 51-115. Predicted coiled-coil 261-349.
- N-terminus (MNTMYVMMAQ ILRSHLIKAT VIPNRVKMLP...) resembles a mitochondrial-targeting presequence (basic/hydrophobic), consistent with the orchestrator note that DNAJC28 is a mitochondrial J-domain protein; this is a prediction, not experimentally confirmed in the UniProt record.

## Function (very limited)
- UniProt FUNCTION: "May have a role in protein folding or as a chaperone." — speculative/uncharacterized.
  [file:human/DNAJC28/DNAJC28-uniprot.txt "May have a role in protein folding or as a chaperone."]
- No experimental characterization of co-chaperone (HSP70 ATPase-stimulating) activity, substrate, or compartment of action.
- Phosphorylated at Thr-347 (large-scale phosphoproteomics, PMID:17693683).
- Tissue enhanced in testis (HPA); expressed in brain, testis, uterus, spleen, liver.

## GO annotations (only 2)
1. GO:0001659 temperature homeostasis (IBA, GO_REF:0000033, from PANTHER PTN001166000 / UniProtKB:F7DMN9).
   - Phylogenetically transferred; no experimental basis for DNAJC28 in temperature homeostasis. The PANTHER family node grouping is broad. Over-annotation / non-core.
2. GO:0005515 protein binding (IPI, PMID:24407287, WITH UniProtKB:Q9ULZ3 = PYCARD/ASC).
   - PMID:24407287 is a PML-ASC inflammasome paper; the DNAJC28-ASC interaction is an AgBase-curated high-throughput hit, not central to a chaperone function. Bare protein binding, uninformative. KEEP_AS_NON_CORE.

## Assessment
- DNAJC28 is a bona fide but essentially uncharacterized J-domain (HSP40) protein. The only defensible molecular-function inference is its J domain (co-chaperone / HSP70 binding), but even this is by domain prediction only.
- No reliable evidence for "temperature homeostasis" as a specific function.
- Core function: most honest description is an uncharacterized HSP40/J-domain co-chaperone, likely mitochondrial by sequence prediction. Mark questionable IBA process annotation as over-annotated; keep the interaction as non-core.
