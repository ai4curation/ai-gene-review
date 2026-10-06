# ANKRD28 notes

- PP6 ankyrin-repeat scaffolding subunit (ARS-A). PP6 is a heterotrimer: PPP6C plus a SAPS subunit (PPP6R1/2/3) plus ARS (ANKRD28/44/52). PPP6R1 bridges the two other subunits [PMID:18186651 "PP6R1 acts as a scaffold with separate regions for binding to PP6 and to Ankrd28"].
- Functions: knockdown enhances TNF-induced IkBe degradation [PMID:18186651]; needed for PP6 in mitosis, with ANKRD44 [PMID:21187329]; knockdown raises pMOB1-T35 and shrinks focal adhesions [PMID:35512830, full text]. RAB40C-CUL5 ubiquitylates ANKRD28 for lysosomal degradation [PMID:35512830].
- PP1 targeting (as "PITK") [PMID:16564677, PMID:17023142; abstracts]. Nuclear foci, versus "exclusively in the cytoplasm" in PMID:17988990. Nucleoplasm kept as non-core.
- GO:0051894 positive regulation of FA assembly (IMP): every experimental arm supports the positive sign (knockdown shrinks FAs; knockdown reverses the RAB40C-KO enlargement). One intro sentence, "ANKRD28-containing PP6 complex inhibits FA formation", is a framing slip. Kept as non-core.
- 27 GO:0005515 rows:
  - DOCK1 → MODIFY to GO:0017124 SH3 domain binding.
  - PP6 subunits (PPP6C, PPP6R1/2/3; 16 rows) → REMOVE. They are co-members of one complex, already captured by GO:0008287/GO:0019888.
  - TNKS2 and nine HuRI screen partners → REMOVE.
- No IBA rows. The PANTHER xref places ANKRD28 in PTHR24173:SF74, whose name is "ANKYRIN REPEAT DOMAIN-CONTAINING PROTEIN 16"; I have not checked that placement.
- Affinage: trust gate tripped (pairwise tie); the narrative checks out against the abstracts.

## Round 2 (reviewer, PR #4108)

- Dropped the claim that ANKRD28 binds PPP6C only through PPP6R1. PMID:18186651 is abstract-only and shows separable PP6R1 surfaces, not the absence of a direct contact. The REMOVEs stand on the protein-binding policy alone.
- The focal-adhesion sign is resolved in the reason (see above), and the open-contradiction question is replaced.
- NEW GO:0008157 protein phosphatase 1 binding (IPI, PMID:16564677). UniProt's "selectively inhibits PPP1C" is not in the cached abstract and is not adopted.
- PMID:21187329 relevance raised to HIGH and PMID:27026398 to MEDIUM. The screen-paper notes now distinguish full-text from abstract-only caches.
- DOCK180/SH3 is not a core function: it rests on one abstract-only study, with no follow-up linking it to PP6.
