# SCGB3A1 (Q96QR1) curation notes

## Identity
- Secretoglobin family 3A member 1; synonyms HIN-1 (high in normal-1), UGRP2, PnSP-2, cytokine HIN-1.
- 104 aa precursor; signal peptide 1-20 (protein-sequenced), mature chain 21-104 [file:human/SCGB3A1/SCGB3A1-uniprot.txt "SIGNAL 1..20" / "CHAIN 21..104"].
- Secreted; disulfide-linked homodimer (interchain Cys78, by similarity) [file:human/SCGB3A1/SCGB3A1-uniprot.txt "Homodimer; disulfide-linked"].
- Belongs to secretoglobin family, UGRP subfamily [file:human/SCGB3A1/SCGB3A1-uniprot.txt "Belongs to the secretoglobin family. UGRP subfamily."].
- Closest paralog SCGB3A2 (UGRP1); both NKX2-1/TTF-1 lung targets.

## Expression / localization
- Highly expressed in lung and prostate; also mammary gland, spleen, pancreas, testis, liver [PMID:11481438; file:human/SCGB3A1/SCGB3A1-uniprot.txt "Highly expressed in lung and prostate"]. Airway epithelium / submucosal glands [PMID:12406855]. In mammary gland localizes to luminal epithelial cells [file:human/SCGB3A1/SCGB3A1-uniprot.txt "specifically localizes to luminal epithelial cells"].
- Secreted; detected in colostrum (proteomics, PMID:16502470) and parotid-gland exosomes (PMID:19199708). HPA: group enriched (cervix, lung, salivary gland).

## Molecular function / mechanism
- Secreted, cytokine-like protein with no significant homology to known proteins [PMID:11481438 "HIN-1 is a putative cytokine with no significant homology to known proteins"].
- Acts as a secreted ligand: ligand-binding studies show high-affinity cell-surface HIN-1 binding on epithelial cells (receptor still unidentified) [PMID:16266985 "high-affinity cell surface HIN-1 binding on epithelial cells"]. This receptor-mediated activity supports a cytokine-like secreted-signaling role, so cytokine activity is retained as KEEP_AS_NON_CORE rather than removed.
- Mechanism of growth suppression is inhibition of PI3K/AKT: "mitogen-induced phosphorylation and activation of AKT are inhibited in HIN-1-expressing cells" and "expression of constitutively activate AKT abrogates HIN-1-mediated growth arrest" [PMID:16266985], placing AKT downstream of HIN-1. Also inhibits Rb phosphorylation / cell-cycle re-entry and induces apoptosis [PMID:16266985]. -> supports MODIFY of generic signal transduction (IEA) to GO:0051898 negative regulation of PI3K/AKT signaling.
- Growth-inhibitory / candidate tumor suppressor: reintroduction into breast cancer cells inhibits growth [PMID:11481438 "Reintroduction of HIN-1 into breast cancer cells inhibits cell growth"]; potent inhibitor of growth, migration and invasion [PMID:16266985 "potent inhibitor of anchorage-dependent and anchorage-independent cell growth, cell migration, and invasion"].

## Deep research (OpenScientist)
- An OpenScientist deep-research report (SCGB3A1-deep-research-openscientist.md) was present and used as LEADS only. It surfaced the Krop et al. 2005 AKT-mechanism study (PMID:16266985) and promoter-hypermethylation-across-cancers literature; the load-bearing claims were verified against the primary abstracts before use. Not used as sole evidence for any annotation.

## Disease association (verified)
- Epigenetically silenced tumor suppressor. HIN-1 expression is down-regulated in ~94% of breast carcinomas and ~95% of preinvasive lesions (DCIS/LCIS), with promoter hypermethylation in >90% of breast cancer cell lines and ~74% of primary tumors [PMID:11481438 "HIN-1 expression is significantly down regulated in 94% of human breast carcinomas and in 95% of preinvasive lesions", "accompanied by hypermethylation of its promoter in the majority of breast cancer cell lines (>90%) and primary tumors (74%)", "candidate tumor suppressor gene that is inactivated at high frequency in the earliest stages of breast tumorogenesis"]. HIN-1/SCGB3A1 promoter methylation is subsequently a well-documented event also in prostate, lung and other carcinomas (family/literature context; primary datum here is the breast study).

## Myoblast fusion annotation (IBA)
- GO:1901741 positive regulation of myoblast fusion (IBA) on the human gene is inherited from PAINT node PTN002165930, seeded by the mouse Scgb3a1 IMP annotation (acts_upstream_of_or_within) from PMID:23844157, an RNAi screen of 134 mouse cytokine genes in C2C12 myoblast differentiation that flagged Scgb3a1 among candidate myogenic regulators [PMID:23844157 "we undertook an RNAi screen of 134 mouse cytokine genes for their involvement in the differentiation of C2C12 myoblasts", "29 cytokines as strong candidates for"]. This is a knockdown/perturbation screen hit (necessity, not demonstrated participation); retained as KEEP_AS_NON_CORE for the human protein — a plausible conserved role but not the characterized core function, and not refutable from available data.

## Annotation decisions (summary)
- GO:0005576 extracellular region (IBA/IDA/HDA/IEA): ACCEPT — core; secreted protein, concordant across phylogenetic, direct and proteomic evidence.
- GO:0070062 extracellular exosome (HDA): KEEP_AS_NON_CORE — valid proteomic sub-localization, peripheral.
- GO:0005125 cytokine activity (NAS): KEEP_AS_NON_CORE — high-affinity cell-surface receptor binding (PMID:16266985) supports a cytokine-like secreted-ligand activity, but the receptor is unidentified and the specific immune-cytokine GO term is loosely grounded; non-core.
- GO:0007165 signal transduction (IEA, logically inferred from GO:0005125): MODIFY -> GO:0051898 negative regulation of PI3K/AKT signaling — the generic term is refined to the verified AKT-inhibitory mechanism (PMID:16266985).
- GO:0005515 protein binding (IPI, with RHBDD2 isoform, binary interactome): REMOVE — bare uninformative protein binding from a high-throughput Y2H interactome, per protein-binding policy.
- GO:0030308 negative regulation of cell growth (NAS): ACCEPT — growth-inhibitory activity on breast cancer cells, the central verified function.
- GO:0042127 regulation of cell population proliferation (NAS): MODIFY -> GO:0008285 negative regulation of cell population proliferation — the undirected parent is less specific than the verified negative-direction finding.
- GO:1901741 positive regulation of myoblast fusion (IBA): KEEP_AS_NON_CORE (see above).
