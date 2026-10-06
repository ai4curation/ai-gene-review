# FCA (At4g16280, UniProt O04425) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: UniProt O04425 FCA_ARATH, At4g16280 (gene_exact search returned a single reviewed entry).
- Deep research (falcon) failed (HTTP 429); review built from cached primary literature.
- FCA: two RRMs + WW domain; nuclear RNA-binding protein [PMID:12805228 "We show that FCA is a nuclear RNA-binding protein and that its WW domain is required for this autoregulation."]
- WW domain binds FY (Pfs2p/WDR33) [PMID:12809608 "We have identified FY as a protein partner for this domain."]
- Autoregulation by proximal polyadenylation in intron 3 [PMID:12805228 "We demonstrate here that FCA negatively regulates its own expression by ultimately promoting cleavage and polyadenylation within intron 3."]
- FLC repression needs FLD (LSD1 homolog) [PMID:17996704 "Here, we show that FCA requires FLOWERING LOCUS D (FLD), a homolog of the human lysine-specific demethylase 1 (LSD1) for FLC downregulation."]
- Proximal antisense (COOLAIR) polyadenylation triggers silencing [PMID:19965720 "A specific RNA-binding protein directs their activity to a proximal antisense polyadenylation site."]
- FCA binds nascent COOLAIR and interacts with CLF [PMID:31032401 "We report that the RNA binding protein FCA interacts with the PRC2 subunit CURLY LEAF (CLF) and binds nascent COOLAIR transcripts to allow deposition of H3K27me3 at FLC."]
- Liquid-like nuclear bodies, FLL2 [PMID:31043738 "We thus conclude that FCA localizes to nuclear bodies with liquid-like properties, suggesting that FCA can undergo liquid-liquid phase separation in vivo."]
- FCA does NOT bind ABA [PMID:19078995 "However, we find that FCA does not bind ABA"].

## Decisions
- NEW: lncRNA binding (GO:0106222, COOLAIR) and mRNA alternative polyadenylation (GO:0110104). FCA does the step (binds RNA and recruits FY/CPSF to the proximal site), so the participation test is met.
- Cytoplasm IBA/ISM and RNP complex IBA (PABP-seeded node) flagged as over-annotation/removal.
- Bare protein-binding rows removed (interactions themselves not disputed).
