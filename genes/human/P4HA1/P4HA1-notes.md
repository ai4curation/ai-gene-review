# P4HA1 (Prolyl 4-hydroxylase subunit alpha-1) — review notes

UniProt: P13674 (P4HA1_HUMAN), 534 aa precursor (signal 1-17, chain 18-534). HGNC:8546. EC 1.14.11.2.

## Core identity and function

P4HA1 is the catalytic alpha-1 subunit of collagen prolyl 4-hydroxylase (C-P4H). The active
enzyme is an alpha2-beta2 heterotetramer in which the beta subunit is P4HB (the multifunctional
protein disulfide isomerase, PDI). The alpha subunits provide the catalytic and peptide-substrate-
binding activity; P4HB is a structural subunit that also retains the tetramer in the ER lumen via
its KDEL signal.

- [file:human/P4HA1/P4HA1-uniprot.txt "Catalyzes the post-translational formation of 4-hydroxyproline in -Xaa-Pro-Gly- sequences in collagens and other proteins."]
- [file:human/P4HA1/P4HA1-uniprot.txt "Heterotetramer of two alpha-1 chains and two beta chains (P4HB)(the beta chain is the multi-functional PDI), where P4HB plays the role of a structural subunit; this tetramer catalyzes the formation of 4-hydroxyproline in collagen."]
- [PMID:2543975 "Prolyl 4-hydroxylase ... an alpha 2 beta 2 tetramer, catalyzes the formation of 4-hydroxyproline in collagens by the hydroxylation of proline residues in peptide linkages."]
- [PMID:9211872 "Prolyl 4-hydroxylase (proline hydroxylase, EC 1.14.11.2) catalyzes the formation of 4-hydroxyproline in collagens. The vertebrate enzyme is an alpha2beta2 tetramer, the beta subunit of which is identical to protein disulfide-isomerase (PDI, EC 5.3.4.1)."]

## Catalytic mechanism / cofactors

It is a Fe(II)- and 2-oxoglutarate-dependent dioxygenase. Catalysis requires molecular O2, with
2-oxoglutarate decarboxylated to succinate + CO2, and requires ascorbate (vitamin C) to keep the
iron reduced.

- [file:human/P4HA1/P4HA1-uniprot.txt "Reaction=L-prolyl-[collagen] + 2-oxoglutarate + O2 = trans-4-hydroxy-L-prolyl-[collagen] + succinate + CO2"]
- [file:human/P4HA1/P4HA1-uniprot.txt "Name=Fe(2+); Xref=ChEBI:CHEBI:29033"] and Note "Binds 1 Fe(2+) ion per subunit."
- [file:human/P4HA1/P4HA1-uniprot.txt "Name=L-ascorbate; Xref=ChEBI:CHEBI:38290"]
- Fe2OG dioxygenase domain 411-519; Fe-binding residues 429, 431, 500; 2-OG binding 510.
- KW includes Dioxygenase, Oxidoreductase, Iron, Metal-binding, Vitamin C — supports GO:0005506
  iron ion binding, GO:0031418 L-ascorbic acid binding, GO:0016705 oxidoreductase (paired donors, O2).

## Subcellular location

ER lumen. The alpha subunit lacks a KDEL/retention signal; ER retention of the tetramer is conferred
by P4HB.
- [file:human/P4HA1/P4HA1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen."]
- [PMID:2543975 "The alpha-subunit does not have this C-terminal sequence, and thus one function of the beta-subunit in the prolyl 4-hydroxylase tetramer appears to be to retain the enzyme within this cell organelle."]

## Structure / domains / dimerization

- Peptide-substrate-binding domain (PSB) is a TPR domain with functional aromatic (Tyr) residues
  (Y210, Y213, Y247 mutagenesis strongly reduces substrate affinity); TPR repeat 205-238.
- N domain (1-143) mediates alpha-alpha dimerization via an antiparallel coiled-coil four-helix bundle.
- [PMID:24207127 "The α subunit contains an N domain (1-143), a peptide-substrate-binding-domain (PSB, 144-244) and a catalytic domain (245-517)."]
- [PMID:24207127 "It is shown that the N domain has an important role in the assembly of the C-P4H tetramer, by forming an extended four-helix bundle that includes an antiparallel coiled-coil dimerization motif between the two α subunits."]
- This dimerization underlies the GO:0042802 "identical protein binding" annotation (IPI vs P13674,
  PMID:24207127) — i.e., alpha-alpha homodimerization within the tetramer. Functionally meaningful,
  but subsidiary to the catalytic core function (KEEP_AS_NON_CORE).

## Isoforms / type I vs type II enzyme

Two enzyme isotypes exist: type I (P4HA1/alphaI) and type II (P4HA2/alphaII). They do NOT form mixed
alphaI-alphaII-beta2 tetramers. P4HA1 also undergoes alternative splicing (3 isoforms; mutually
exclusive exons VSP_004504, plus VSP_044578 in isoform 3).
- [PMID:9211872 "The results of coexpression in insect cells argued strongly against the formation of a mixed alpha(I)alpha(II)beta2 tetramer."]
- [PMID:2543975 "mutually exclusive alternative splicing of primary transcripts of one gene."]

## Biological process

The defining process is peptidyl-proline hydroxylation to 4-hydroxy-L-proline, which is essential for
collagen triple-helix stability (4-Hyp stabilizes the helix; under-hydroxylated collagen is thermally
unstable). Downstream, this supports collagen biosynthesis and collagen fibril organization.
GO annotations include GO:0030199 collagen fibril organization (IBA), which is a reasonable
downstream/process role for the modifying enzyme; keep as non-core (the enzyme modifies procollagen
but the assembly of fibrils is performed by other machinery — accept as involved_in, non-core).

## Existing GO annotation triage

Core MF:
- GO:0004656 procollagen-proline 4-dioxygenase activity — IDA (PMID:9211872), TAS (PMID:2543975),
  IBA, IEA. ACCEPT (core). Direct catalytic activity demonstrated.
Cofactor/mechanism MF (accept, non-core supporting features):
- GO:0005506 iron ion binding (IEA, InterPro) — ACCEPT, supported by Fe2OG domain + COFACTOR Fe(2+).
- GO:0031418 L-ascorbic acid binding (IEA, UniProtKB-KW Vitamin C) — ACCEPT.
- GO:0016705 oxidoreductase, paired donors with O2 (IEA, InterPro) — ACCEPT (parent of the precise
  dioxygenase activity).
CC:
- GO:0005788 ER lumen (IEA SubCell, TAS Reactome x2) — ACCEPT (core location).
- GO:0005783 endoplasmic reticulum (IEA, IDA-HPA, TAS PMID:2543975) — ACCEPT (parent of ER lumen).
- GO:0016222 procollagen-proline 4-dioxygenase complex (IBA, IEA) — ACCEPT (the alpha2-beta2 C-P4H
  complex). This is the relevant complex CC.
- GO:0016020 membrane (HDA, PMID:19946888 — NK cell membrane proteome MS) — over-annotation. P4HA1 is
  a soluble ER-lumenal protein; a membrane HDA from a bulk membrane-fraction proteomics screen is a
  likely co-fractionation artifact (or ER-membrane association of the secretory machinery). Do not
  REMOVE an experimental annotation on weak grounds → MARK_AS_OVER_ANNOTATED (HDA, not core; not the
  documented soluble ER-lumen localization).
MF protein binding (IPI):
- GO:0005515 protein binding, IPI vs HTT (PMID:17500595, Htt-fragment interactome) — KEEP_AS_NON_CORE;
  bare protein binding; the HTT interaction is in UniProt INTERACTION but unrelated to catalytic core.
- GO:0005515 protein binding, IPI vs P4HA2/O15460 (PMID:30021884, histone XL-MS) — KEEP_AS_NON_CORE;
  high-throughput, partner is paralog P4HA2; uninformative bare term.
- GO:0005515 protein binding, IPI vs P4HA2/O15460 (PMID:40205054, multimodal cell map) — KEEP_AS_NON_CORE.
- GO:0042802 identical protein binding, IPI vs P13674 (PMID:24207127) — KEEP_AS_NON_CORE; this is the
  alpha-alpha homodimerization within the tetramer (structurally demonstrated), functionally real but
  subsidiary to catalytic core.

## Tumor/hypoxia biology (context, not core)

P4HA1 is induced by hypoxia (HIF target) and is implicated in ECM remodeling / tumor progression in
several cancers. No such BP annotations are present in this GOA; if added they should be non-core.
(Not in the cached pubs; noted for completeness.)

## Falcon deep-research findings (incorporated 2026-06)

- P4HA1 acts as a downstream effector in a fibro-inflammatory remodeling cascade: an
  IL-10/JAK2/STAT3/HIF1alpha/TMEM45A/P4HA1 signaling axis was elucidated in SLE-associated
  pleural remodeling; P4HA1 knockdown blocks IL-10-induced increases in collagen-I, fibronectin
  and alpha-SMA. [PMID:39563376 "the IL-10/JAK2/STAT3/HIF1α/TMEM45A/P4HA1 signaling axis was elucidated to mediate pleural remodeling and thickening"]
- Metabolic α-ketoglutarate supply (from CAF-derived lactate) increases P4HA1-dependent collagen
  4-hydroxylation, driving a collagen→DDR1 loop in prostate cancer metastasis (already in review as
  PMID:38907027 / Ippolito 2024). Falcon corroborates 2-oxoglutarate availability as a functional
  lever on enzymatic output.
- P4HA1 is overexpressed in esophageal squamous cell carcinoma (~68.7% of cases by IHC, negative in
  adjacent tissue) and is an independent prognostic factor (OS/PFS). Cancer biomarker context, non-core.
  [PMID:38134053 "P4HA1 was highly expressed in esophageal squamous cell carcinoma (68.7%), while it was negatively expressed in paracancerous tissues"]
- Family-level (all three C-P4HA alpha subunits, P4HA1/2/3) prognostic analysis in HNSCC: higher combined
  expression of the three is a superior prognostic indicator, and the deleterious effect is antagonized by
  LLGL2 via occludin. [PMID:39394821 "a higher expression of all three C-P4HAs ... is a superior prognostic indicator"]
- Yang 2024 is a dedicated P4HA1-focused review mapping its roles across fibrosis-related diseases and
  cancers, hypoxia/HIF-linked induction, ECM remodeling, and targeting strategies (siRNA, small-molecule
  P4H inhibitors). [PMID:39568592 "P4HA1 ... the synthesis and secretion of collagen are related to the sustained activation of P4HA1"]
- Falcon reiterates non-collagen/collagen-like substrates beyond fibrillar procollagen (MBL — already in
  review as PMID:35368589; plus reported X-Pro-Gly substrates such as AGO2 Pro700, elastins, prion protein,
  conotoxins per the Mezentsev 2024 lung-cancer biomarker review). The AGO2/elastin/conotoxin claims are
  secondary (review-level) and not added as primary references here.
- HIF-PHD inhibitors (roxadustat, vadadustat) can off-target inhibit collagen prolyl 4-hydroxylation of
  collagen-like domains (MBL) — already captured via PMID:35368589 (Bhute 2020). Clinically relevant
  isoenzyme-selectivity caveat for the P4HA/PHD field.
