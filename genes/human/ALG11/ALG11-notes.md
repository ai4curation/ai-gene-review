# ALG11 (human) review notes

UniProt: Q2TAA5 (ALG11_HUMAN). HGNC:32456. Gene synonym GT8. EC 2.4.1.131.

## Core biology (verified)

ALG11 is the ER **alpha-1,2-mannosyltransferase** of the dolichol-linked oligosaccharide
(LLO) assembly pathway. It uses GDP-mannose as the sugar donor and adds the **fourth and
fifth mannose residues** onto Man3GlcNAc2-PP-dolichol, producing **Man5GlcNAc2-PP-dolichol**,
the final cytoplasmic-face LLO intermediate. These are the last two mannose additions on the
cytosolic side of the ER membrane before the glycan is flipped into the ER lumen by RFT1.
The Man5GlcNAc2-PP-dolichol product is then the substrate for ALG3 (next enzyme).

- UniProt FUNCTION: "Catalyzes, on the cytoplasmic face of the endoplasmic reticulum, the
  addition of the fourth and fifth mannose residues to the dolichol-linked oligosaccharide
  chain, to produce Man(5)GlcNAc(2)-PP-dolichol core oligosaccharide" [file:human/ALG11/ALG11-uniprot.txt].
- Reactome R-HSA-4551297: "transfers the fourth and fifth mannoses (Man) to the N-glycan
  precursor in an alpha-1,2 orientation. These additions are the last two on the cytosolic
  side of the ER membrane before the N-glycan is flipped to the luminal side of the membrane."
- Topology: single-pass ER membrane protein, N-terminal TM helix (aa 20-40), catalytic domain
  cytoplasmic. Belongs to glycosyltransferase group 1 family / GT4 subfamily; CDD GT4_ALG11-like;
  InterPro IPR038013 (ALG11), IPR001296 (Glyco_trans_1).

## Disease

Deficiency causes **ALG11-CDG (congenital disorder of glycosylation type Ip / CDG1P; MIM:613661)**.
PMID:20080937 (Rind et al. 2010): homozygous c.T257C (p.L86S), patient fibroblasts accumulate
Man3GlcNAc2-PP-dolichol and Man4GlcNAc2-PP-dolichol, deficient in elongating
Man3GlcNAc2-PP-dolichol; retroviral rescue with WT hALG11 and yeast alg11-delta complementation
confirmed causality. Multisystem disorder (hypotonia, seizures, developmental retardation).
Additional CDG1P variants Y279S, Q318P, L381S, E398K (PMID:22213132, Thiel et al. 2012 — not cached).

## Annotation-by-annotation decisions (GOA has 14 lines)

MF GO:0004377 (GDP-Man:Man(3)GlcNAc(2)-PP-Dol a-1,2-MT activity): IBA, IEA, IDA -> ACCEPT (core MF;
  IDA in PMID:20080937 characterises activity, L86S reduces it). This is the exact GOA MF term used
  in core_functions.
BP GO:0006488 (dolichol-linked oligosaccharide biosynthetic process): IBA + IMP -> ACCEPT (core BP).
BP GO:0006487 (protein N-linked glycosylation): IMP -> ACCEPT (core BP; LLO precursor feeds N-glyc).
CC GO:0005789 (ER membrane): IBA, IEA, IDA, TAS -> ACCEPT (core CC; IDA localization in patient/control fibroblasts).
MF GO:0016757 (glycosyltransferase activity): IEA InterPro -> ACCEPT (correct but general parent; IEA allowed broader).
MF GO:0000026 (alpha-1,2-mannosyltransferase activity): TAS Reactome -> ACCEPT (correct less-specific parent).
MF GO:0005515 (protein binding): IPI, PMID:33961781 BioPlex, with P06280/GLA -> MARK_AS_OVER_ANNOTATED
  (bare, uninformative; single high-throughput AP-MS pull-down; not a functional interaction).
CC GO:0016020 (membrane): HDA, PMID:19946888 -> MARK_AS_OVER_ANNOTATED (generic; ALG11 not the subject,
  YTS NK-cell membrane-proteome MS survey; superseded by specific ER membrane).

## Reference notes
- PMID:20080937 abstract-only in cache (full_text_available: false) but abstract is rich and
  directly supports MF/BP/CC/disease. HIGH relevance, VERIFIED.
- PMID:19946888 (NK membrane proteome) — LOW relevance, correctly cited for HDA membrane.
- PMID:33961781 (BioPlex) — LOW relevance, correctly cited for the IPI but uninformative.
- Reactome R-HSA-4551297 — HIGH relevance, TAS.
