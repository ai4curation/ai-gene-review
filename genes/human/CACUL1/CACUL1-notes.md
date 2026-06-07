# CACUL1 (Q86Y37) review notes

## Identity
- UniProt: Q86Y37, CACL1_HUMAN. RecName: CDK2-associated and cullin domain-containing protein 1. AltName: Cdk-associated cullin 1 (CAC1). Synonyms C10orf46, CAC1. HGNC:23727. Gene on chr10. 369 aa, ~41 kDa.
- Contains a single Cullin/Cullin-repeat domain (Pfam PF00888 Cullin; InterPro IPR001373 Cullin_N, IPR016159 Cullin_repeat-like_dom_sf; Gene3D 1.20.1310.10 Cullin Repeats). N- and C-termini disordered (1-56, 342-369). UniProt SIMILARITY: "Belongs to the cullin family" {ECO:0000305}.
- Note: presence of a cullin-repeat-like domain does NOT establish that CACUL1 acts as a canonical CRL (cullin-RING ligase) scaffold; the cullin-repeat fold is structurally shared but CACUL1 is short (369 aa) compared to canonical cullins (~750-900 aa) and lacks a demonstrated RBX/neddylation module. No experimental evidence that CACUL1 nucleates a functional E3 ligase.

## Primary literature

### PMID:19829063 (Kong, Nan, Yin, Cell Cycle 2009) — the defining functional paper
- Identified CAC1/CACUL1 as a novel CDK2-associated protein. 369 aa protein containing a Cullin domain, physically associated with CDK2 [PMID:19829063 abstract, "this protein is physically associated with CDK2... we have designated it Cdk-Associated Cullin1, or CAC1"].
- Highly expressed in cancer tissues/cell lines; expression is cell-cycle-dependent (high in late G1 to S phase) [PMID:19829063 "CAC1 is expressed in a cell cycle-dependent manner and its expression is high in late G(1) to S phase"].
- RNAi knockdown inhibits cell proliferation and induces G1/S arrest [PMID:19829063 "Knockdown of CAC1 by RNAi inhibits cell proliferation and induces G(1)/S arrest"].
- CAC1 interacts with CDK2 and promotes CDK2 kinase activity [PMID:19829063 "CAC1 interacts with CDK2 and promotes the kinase activity of CDK2 protein... CAC1 is a novel cell cycle associated protein capable of promoting cell proliferation"].
- Supports: protein kinase binding (CDK2, IPI WITH UniProtKB:P24941), positive regulation of protein kinase activity, positive regulation of cell proliferation, G1/S transition involvement. All from a single lab; no structural/mechanistic detail on HOW CDK2 is activated.

### PMID:23178685 (Kim, Park, Moon, Um, Kim; FEBS Lett 2013) — nuclear receptor co-regulation
- Identified CAC1 as a novel ERα coregulator. The CoRNR box of CAC1 is required for binding to and inactivation of ERα [PMID:23178685 "The CoRNR box of CAC1 was required for the binding to and inactivation of ERα"].
- CAC1 associated with histone demethylase LSD1 (KDM1A) and suppressed LSD1-enhanced ERα activity; impaired recruitment of ERα and LSD1 to ERα-responsive promoter, increasing H3K9me3 [PMID:23178685 "CAC1 also associated with histone demethylase LSD1 and suppressed LSD1-enhanced ERα activity. CAC1 impaired recruitment of ERα and LSD1 to the ERα-responsive promoter, leading to greater H3K9me3 accumulation"].
- Concludes CAC1 functions as an ERα COREPRESSOR (not coactivator) associated with LSD1 [PMID:23178685 "CAC1, associated with LSD1, functions as an ERα corepressor"]. (Note: biological hint said "coactivator"; the primary paper actually shows corepressor/negative regulation of ERα. Other reports describe co-activator activity for AR; the directionality is context-dependent / not firmly established.)
- The IntAct interaction in UniProt (Q86Y37–P03372 ESR1, NbExp=5) corresponds to this ERα binding. The GOA protein-binding row PMID:23178685 WITH UniProtKB:P03372 (ESR1) is this interaction.

### PMID:28169274 (Hu et al., Nat Commun 2017) — ARMC5 paper, CACUL1 only an interactor
- This paper is about ARMC5 (Q96C12), not CACUL1. CACUL1 appears only as one of 16 ARMC5-binding partners identified by yeast-2-hybrid [PMID:28169274 "Yeast 2-hybrid assays identify 16 ARMC5-binding partners"; "To identify ARMC5-binding proteins, we conducted Y2H assays with human ARMC5 protein... as bait"].
- The GOA row PMID:28169274 protein binding WITH UniProtKB:Q96C12 (ARMC5) is this Y2H interaction. It is a bare binding datum with no functional characterization of CACUL1 itself. ARMC5 is implicated in T-cell function/adrenal homeostasis; CACUL1's role in that biology is unknown.

## GOA annotations (10 rows) summary
1. GO:0000082 G1/S transition of mitotic cell cycle — IBA (GO_REF:0000033, PANTHER PTN002927661). Phylogenetic transfer; experimental basis in PMID:19829063 (same gene).
2. GO:0019901 protein kinase binding — IBA (GO_REF:0000033). Phylogenetic; experimental basis (CDK2) in PMID:19829063.
3. GO:0006511 ubiquitin-dependent protein catabolic process — IEA (GO_REF:0000002, InterPro IPR001373 Cullin_N). Pure domain-transfer from the cullin fold; NO direct evidence CACUL1 participates in ubiquitin-dependent catabolism. Over-annotation risk.
4. GO:0031625 ubiquitin protein ligase binding — IEA (GO_REF:0000002, InterPro IPR001373). Pure domain-transfer; NO direct evidence. Over-annotation risk.
5. GO:0005515 protein binding — IPI PMID:23178685 (WITH ESR1/P03372). Bare; ERα interaction. Uninformative term.
6. GO:0005515 protein binding — IPI PMID:28169274 (WITH ARMC5/Q96C12). Bare; ARMC5 Y2H interactor. Uninformative term.
7. GO:0000082 G1/S transition — IMP PMID:19829063. RNAi knockdown causes G1/S arrest. Direct experimental.
8. GO:0008284 positive regulation of cell population proliferation — IMP PMID:19829063. Knockdown inhibits proliferation. Direct experimental.
9. GO:0019901 protein kinase binding — IPI PMID:19829063 (WITH CDK2/P24941). Direct experimental CDK2 binding.
10. GO:0045860 positive regulation of protein kinase activity — IMP PMID:19829063. CAC1 promotes CDK2 kinase activity. Direct experimental.

## Assessment for core function
- Best-supported (single lab, PMID:19829063): physical interaction with CDK2 (protein kinase binding) and promotion of CDK2 activity / G1/S progression / proliferation. Tentative core: poorly characterized cullin-domain protein implicated in CDK2-associated cell-cycle progression.
- Secondary (PMID:23178685): nuclear-receptor (ERα) co-regulation via LSD1, acting as a corepressor in that study. Real interaction (IntAct NbExp=5) but mechanistic role not firmly established; keep as non-core.
- Ubiquitin-ligase / proteasomal-degradation IEA terms rest only on cullin-domain homology and should be treated as over-annotations absent any direct evidence that CACUL1 is a functional CRL scaffold.
- "protein binding" rows are uninformative -> over-annotated; ESR1 binding could be MODIFY-able to nuclear receptor binding but per guidelines marking bare protein binding as over-annotated is the safer call here (specific informative MF for the CDK2 interaction is already separately captured as protein kinase binding).
