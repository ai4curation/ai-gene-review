# CDKN2A (human) review notes

**Provenance note:** provider deep research for this gene failed (Falcon returned
HTTP 402 Payment Required; Perplexity was not configured). No
`CDKN2A-deep-research-*.md` file exists. This notes file is a manual literature
synthesis from the UniProt record (P42771), the cached publications in
`publications/`, and PubMed lookups, and it replaces the provider deep research
for this review.

## Locus and products

- CDKN2A (INK4a/ARF locus, 9p21) encodes two unrelated proteins from alternative
  first exons (1alpha, 1beta) spliced to a shared exon 2 read in different frames:
  p16INK4a (UniProt P42771, this review) and p14ARF (UniProt Q8N726, separate
  entry). UniProt CAUTION: the P42771 proteins "are completely unrelated in terms
  of sequence and function to tumor suppressor ARF (AC Q8N726) which is encoded by
  the same gene."
- [PMID:11278317 "The INK4a gene, one of the most often disrupted loci in human cancer, encodes
  two unrelated proteins, p16(INK4a) and p14(ARF) (ARF) both capable of inducing
  cell cycle arrest."]
- [PMID:9529249 "The INK4a-ARF locus encodes two unrelated proteins that both function in tumor
  suppression."]
- All GOA rows in `CDKN2A-goa.tsv` are on P42771 (p16INK4a). None carry an isoform
  column. Several rows, however, derive from ARF papers (see "ARF leakage" below).

## p16INK4a: molecular function

- Ankyrin-repeat protein of the INK4 family; binds CDK4 and CDK6 (monomeric and
  cyclin D-bound) and inhibits their kinase activity, preventing Rb phosphorylation.
  - [PMID:8259215 "demonstrate that p16
    binds to CDK4 and inhibits the catalytic activity of the CDK4/cyclin D enzymes."]
  - [PMID:9751050 "the INK4 inhibitors bind next
    to the ATP-binding site of the catalytic cleft, opposite where the activating
    cyclin subunit binds."]
  - [PMID:9751050 "The INK4
    inhibitors also distort the kinase catalytic cleft and interfere with ATP
    binding, which explains how they can inhibit the preassembled Cdk4/6-cyclin D
    complexes as well."]
  - [PMID:9751050 "Tumour-derived mutations in INK4a and Cdk4 map to interface
    contacts, solidifying the role of CDK binding and inhibition in the tumour
    suppressor activity of p16INK4a."]
  - [PMID:17909018 "the R24P variant is
    specifically defective for binding to CDK4 but remains able to associate with
    CDK6."] (familial melanoma variant; CDK4 binding loss is sufficient to phenocopy
    p16 deficiency in fibroblasts).
- Specificity: INK4 proteins inhibit cyclin D-CDK4/6 but not CDK2 or CDC1
  complexes [PMID:7739547 "specifically inhibit the kinase activities of
  CDK4 and CDK6, but do not affect those of cyclin E-CDK2, cyclin A-CDK2, or
  cyclin B-CDC2"] (this paper characterizes mouse p18/p19 INK4c/d by comparison
  with human p16).

## p16INK4a: biological roles

- G1 arrest dependent on functional Rb: [PMID:7603984 "we show that
  overexpression of p16ink4 in certain cell types will lead to an arrest in the G1
  phase of the cell cycle. In addition, we show that p16ink4 can only suppress the
  growth of human cells that contain functional pRB."]
- [PMID:10208428 "induced growth arrest, inhibited DNA synthesis, and prevented
  phosphorylation of the retinoblastoma protein (pRb) in cell lines expressing
  functional pRb."]
- Senescence effector: required for human fibroblast replicative senescence and
  RAS-induced senescence [PMID:14720514 "These data provide the
  first direct evidence that p16(INK4a) is necessary for the initiation of both
  telomere-dependent and telomere-independent senescence in human cells."]
- Oncogene-induced senescence: [PMID:9054499 "The arrest induced by ras is accompanied by
  accumulation of p53 and p16, and is phenotypically indistinguishable from
  cellular senescence. Inactivation of either p53 or p16 prevents ras-induced
  arrest in rodent cells"]
- Endothelial premature senescence via Rb: [PMID:16243918 "HUVECs transfected with p16-EGFP showed an increased proportion of senescent
  cells"]; [PMID:16243918 "suppression of Rb eliminated senescence initiated
  by either p16 or p21 overexpression."]
- Telomere-independent: [PMID:15149599 "These pathways do not affect expression of p16, which
  was upregulated in a telomere- and DNA damage-independent manner in a subset of
  cells."]
- SAHF: [PMID:16901784 "HMGA proteins cooperate with the
  p16(INK4a) tumor suppressor to promote SAHF formation and proliferative arrest"].
  Abstract does not state that p16 protein itself localizes to SAHFs; full text not
  available here.
- Biomarker of aging and senescent cells:
  [PMID:15520862 "expression of p16INK4a and Arf markedly increases in
  almost all rodent tissues with advancing age"];
  [PMID:22048312 "we made use of a
  biomarker for senescence, p16(Ink4a), to design a novel transgene, INK-ATTAC,
  for inducible elimination of p16(Ink4a)-positive senescent cells"]. Note: the
  senescence-marker role is about p16 *expression*; the protein's mechanistic
  contribution to senescence is enforcement of the G1 arrest via CDK4/6-Rb.

## Peripheral / single-study activities (p16)

- NF-kB p65 binding and repression of NF-kB transactivation upon overexpression
  [PMID:10353611 "Overexpression of
  INK4 molecules suppresses the transactivational ability of NF-kappaB
  significantly."]
- Integrin alphavbeta3-dependent spreading inhibited by p16 or CKI peptides
  [PMID:10205165 "Expression of full-length p16(INK4a) blocks alphavbeta3 integrin-dependent cell
  spreading on vitronectin but not collagen IV."]
- PCNA binding and pol delta inhibition (one affinity-proteomics study)
  [PMID:17955473 "p16(ink4a) interacts directly with the DNA
  polymerase delta accessory protein PCNA and thereby inhibits the polymerase
  activity."]
- Other binary interactors (ISOC2, BRG1/SMARCA4, GMNN, DEAF1, HNRNPU, CRELD2,
  TDRD7) from Y2H/microarray screens; functional relevance unclear.
- RNA binding: only from an mRNA interactome capture (HDA, PMID:22681889); no
  dedicated evidence.
- Nuclear import: p16 enters the nucleus; familial melanoma mutation increases nuclear
  accumulation via RanGDP/ankyrin-repeat code [PMID:24855949 "is acquired by the most common familial melanoma-associated CDKN2A
  mutation, leading to nuclear accumulation of mutant p16ink4a."]

## ARF (p14ARF, Q8N726) — separate product, not this entry

- [PMID:9529249 "We show here that
  ARF binds to MDM2 and promotes the rapid degradation of MDM2."]
- [PMID:9529248 "suggests that p19Arf functions mechanistically to prevent MDM2's neutralization
  of p53."]

### ARF leakage into P42771 annotations

- GO:0005515 IPI PMID:11278317 (spinophilin/PPP1R9B): paper is about ARF
  [PMID:11278317 "the
  human homologue of spinophilin/neurabin II, a regulatory subunit of protein
  phosphatase 1 catalytic subunit specifically interacts with ARF"]. Mapped to the
  p16 accession; belongs on Q8N726.
- GO:0034393 and GO:2000111 (ISS from mouse P51480, and Ensembl IEA projections of
  the same): source paper is a p19ARF knockout study
  [PMID:20381282 "p19(ARF) deficiency significantly attenuates
  apoptosis both in atherosclerotic lesions and in cultured macrophages and
  vascular smooth muscle cells"]. Mouse P51480 is the mouse p16 accession; the
  ISS and the Ensembl projection therefore carry an ARF phenotype onto p16 in both
  species. Should be on ARF (Q8N726 / mouse Q64364), not P42771.

## Curation decisions summary

- Core MF: GO:0004861 CDK serine/threonine kinase inhibitor activity (CDK4/6).
- Core BP: negative regulation of G1/S transition (GO:2000134), negative regulation
  of CDK activity, negative regulation of cell population proliferation, cellular
  senescence (incl. replicative and oncogene-induced).
- Generic protein binding: REMOVE, except CDK4/6 rows with direct inhibitory
  evidence, which are MODIFIED to GO:0004861.
- ARF-derived rows: REMOVE from P42771 (flag for transfer to Q8N726).
