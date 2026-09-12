# Notes: mphA (MphA, macrolide 2'-phosphotransferase I; UniProt Q47396)

Curated alongside MphB (UniProt A0A0H3EUF3) to capture the MphA vs MphB substrate-specificity contrast.

## Identity
- UniProt: Q47396 (TrEMBL, unreviewed), 301 aa. Organism: *Escherichia coli* (NCBITaxon:562). PE 1 (protein level).
- Gene name mphA / mph(A) / mph2. The canonical, heavily-studied E. coli macrolide 2'-phosphotransferase I.
- NCBIfam HMM: NF000254 (macrolide_MphA) — curated MphA-specific HMM (cf. NF000242 macrolide_MphB).
- CDD cd05152 (MPH2); Pfam PF01636 (APH); InterPro IPR002575 / IPR011009 (kinase-like); PANTHER PTHR21310.
- 3D structure: PDB 5IGH, 5IGI (MPH(2')-I with guanosine + azithromycin), from Fong et al. 2017.
- Only electronic GO term: GO:0016740 transferase activity (IEA:UniProtKB-KW) — over-general. GOA export EMPTY.

## Function & the key MphA vs MphB distinction
- MphA = macrolide 2'-phosphotransferase I (MPH(2')I). Phosphorylates the desosamine 2'-OH of macrolides
  using a purine NTP (GTP/ITP/ATP, GTP favored) → inactive macrolide 2'-O-phosphate → resistance.
- SUBSTRATE SPECIFICITY (the granular point, beyond GO MF GO:0050073):
  - MphA: HIGH on 14-membered macrolides, EXTREMELY LOW on 16-membered. Also active on 15-membered
    (azithromycin).
    [PMID:2478074 "MPH(2') is an inducible intracellular enzyme which showed high levels of activity with 14-member-ring macrolides and extremely low levels with 16-member-ring macrolides."]
    [PMID:17302923 "The mph(A) gene was unique in conferring resistance to azithromycin."]
  - MphB (contrast): HIGH on BOTH 14- and 16-membered (adds spiramycin/josamycin/tylosin), constitutive.
    [PMID:1330822 "MPH(2')II ... showed high levels of activity with both 14-member-ring and 16-member-ring macrolides."]
- REGULATION: MphA is INDUCIBLE by erythromycin via the TetR-family repressor MphR(A); MphB is constitutive.
  [PMID:10960087 "The synthesis of macrolide 2'-phosphotransferase I [Mph(A)], which inactivates erythromycin, is inducible by erythromycin."]
- GENETIC CONTEXT: high-level erythromycin resistance from the native determinant needs mphA + mrx (accessory
  hydrophobic/membrane protein).
  [PMID:8619599 "the expression of high-level resistance to erythromycin requires two genes, mphA and mrx, which encode macrolide 2'-phosphotransferase I and an unidentified hydrophobic protein, respectively."]
- Cofactor/metal: GTP/ITP/ATP donors; EDTA/iodine/divalent-cation inhibition (metal-dependent), pI 5.3, MW ~34 kDa.
  [PMID:2478074 "Purine nucleotides, such as GTP, ITP, and ATP, were effective as cofactors in the inactivation of macrolides."]

## GO calls (NEW; GOA empty)
- MF: GO:0050073 macrolide 2'-kinase activity (IDA, PMID:2478074; structure PMID:28416110).
- BP: GO:0046677 response to antibiotic (IMP, PMID:8619599; regulation PMID:10960087; azithromycin PMID:17302923).
- substrates (core_function, ChEBI, 14-/15-membered only): erythromycin (CHEBI:48923), oleandomycin
  (CHEBI:16869), clarithromycin (CHEBI:3732), roxithromycin (CHEBI:48844), azithromycin (CHEBI:2955).
  Deliberately EXCLUDES 16-membered (josamycin/tylosin/spiramycin) — the discriminator from MphB.

## References cached
- PMID:2478074 — O'Hara et al. 1989, AAC. Original MPH(2')I purification + specificity. KEY.
- PMID:8619599 — Noguchi et al. 1995, AAC. mphA cloning; mphA+mrx requirement.
- PMID:10960087 — Noguchi et al. 2000, J Bacteriol. mphR(A) regulation (inducible).
- PMID:17302923 — Chesneau et al. 2007. Comparative phenotypes; mphA-unique azithromycin resistance.
- PMID:28416110 — Fong et al. 2017, Structure. MPH(2')-I crystal structures (5IGH/5IGI).
- PMID:29317655 — Pawlowski et al. 2018, Nat Commun. Mph phylogeny/specificity; MphA widespread in Gram-negatives.

Initial curation used primary literature directly; falcon deep research was subsequently run (see Update
below). `just` not installed in container — used `uv run ai-gene-review ...` directly.

## Update: falcon deep research (2026-06-12) — additional references incorporated

Falcon deep research completed (mphA-deep-research-falcon.md). New verifiable findings added:

- PMID:30177927 — Golkar et al. 2018, Front Microbiol. Review of enzyme-mediated macrolide resistance.
  KEY secondary-source confirmation of the MphA/MphB distinction and GTP donor:
  [PMID:30177927 "MPH(2′)-I can only efficiently inactivate 14- and 15-membered lactone macrolides, whereas MPH(2′)-II can additionally inactivate 16-membered lactone macrolides and the ketolide, telithromycin"]
  [PMID:30177927 "These MPHs all mediate the transfer of the γ-phosphate group from GTP onto the macrolide substrates"]
- PMID:38318209 — Wang et al. 2024, Infect Drug Resist. Contemporary mobile genetic context: mphA carried in
  an IS26/IS6100 composite transposon (IS26-mphA-mrx(A)-mphR(A)-IS6100), predominantly on IncF plasmids.
  [PMID:38318209 "the mphA-mrx(A)-mphR(A) operon conferring macrolide resistance was flanked by IS26 and IS6100, forming the IS26-mphA-mrx(A)-mphR(A)-IS6100 transposable structure"]

Other deep-research points (clinical/epidemiology, not added as GO-supporting): mphA is the major azithromycin
resistance determinant in Enterobacterales with high MICs (≥256 µg/mL); MphR(A) derepressed ~100× more
effectively by 14-membered than 16-membered macrolides; mphA alone = low-level, mphA+mrx = high-level
resistance (Noguchi 2000). The Golkar quote was also added to the MphB review to reinforce the I-vs-II contrast.

The "GTP exclusively" claim (deep research, attributed to Fong 2017 full text) was NOT asserted in the review —
cached Fong is abstract-only and O'Hara 1989 shows GTP/ITP/ATP all function (GTP listed first), so the review
states "GTP favored" rather than "exclusive" (verify-don't-trust).

## CARD/ARO provenance (mphA)

CARD entry https://card.mcmaster.ca/aro/3000316 — ARO:3000316, gene symbol mphA, name
"macrolide 2'-phosphotransferase I". AMR Gene Family: macrolide phosphotransferase (MPH);
Resistance Mechanism: antibiotic inactivation (ARO:0001004); Drug Class: macrolide antibiotic.
Curated drug list (= substrate scope): erythromycin, roxithromycin, clarithromycin, dirithromycin,
oleandomycin (14-membered), azithromycin (15-membered), plus telithromycin listed. Detection model:
Protein Homolog Model, BLASTP bitscore cutoff 500. Reference seqs: gb|BAA03776.1 / gb|D16251.1 (E. coli).
Note: unlike the MphB UniProt record, this Q47396 entry's *-uniprot.txt does NOT carry a `DR CARD` line,
so the ARO id was resolved from CARD by gene symbol (mphA = ARO:3000316). Consistent with the review's
14-/15-membered (not 16-membered) specificity. Featured in projects/ANTIMICROBIAL_RESISTANCE.md.
