# PISTILLATA (PI) — Gene Review Notes

UniProt: P48007 (PIST_ARATH); locus AT5G20240; 208 aa MADS-box (MIKC-type) transcription factor.
Taxon: Arabidopsis thaliana (NCBITaxon:3702).

## Summary of biology

PI is a B-class floral homeotic MADS-box transcription factor. Together with APETALA3 (AP3),
it specifies petal (whorl 2) and stamen (whorl 3) identity in the ABC model of flower
development. PI and AP3 function as an **obligate heterodimer**; neither protein is active as a
homodimer in vivo. The heterodimer binds CArG-box DNA sequences via the MADS domain and acts
within higher-order "floral quartet" complexes with SEPALLATA (SEP) and AP1/AGAMOUS proteins.

## Domain architecture (from UniProt P48007)

- MADS-box domain: residues 3–57 (DNA binding + dimerization).
- K-box domain: residues 84–170 (protein–protein interaction / dimerization specificity).
- Coiled coil: residues 75–117.
- PROSITE/Pfam: SRF-TF (PF00319), K-box (PF01486); MADS_MEF2-like.

## Evidence reviewed (provenance)

### Loss-of-function / floral organ identity
- UniProt FUNCTION/MISCELLANEOUS: "Mutations in PI cause transformation of petals into sepals
  and stamina into carpels." [UniProt P48007 CC MISCELLANEOUS]
- UniProt FUNCTION: "Probable transcription factor involved in the genetic control of flower
  development. Is required for normal development of petals and stamens in the wild-type flower.
  Forms a heterodimer with APETALA3 that is required for autoregulation of both AP3 and PI genes."
  [UniProt P48007 CC FUNCTION]
- PMID:2535466 (Bowman, Smyth, Meyerowitz 1989, "Genes directing flower development in
  Arabidopsis") is the classic genetic study establishing the homeotic mutant classes; the
  GOA IMP annotation to GO:0010093 (specification of floral organ identity) derives from this.
  Cached entry is abstract-only here, but this is a foundational experimental paper assigned by
  CACAO; supports specification of floral organ identity. (full text not in cache)

### AP3/PI heterodimerization and DNA binding
- UniProt SUBUNIT: "Forms a heterodimer with APETALA3, capable of binding to CArG-box sequences.
  AP3/PI heterodimer binds AP1 or SEP3 to form a ternary complex." [UniProt P48007 CC SUBUNIT]
- PMID:8643482 (Riechmann et al. 1996, PNAS) — "Dimerization specificity of Arabidopsis MADS
  domain homeotic proteins APETALA1, APETALA3, PISTILLATA, and AGAMOUS." Establishes AP3/PI
  obligate heterodimer (cited in UniProt as CHARACTERIZATION).
- PMID:15604664 (Yang & Jack 2004, Plant Mol Biol) — abstract-only. "the MADS domain that
  mediates DNA binding and dimerization, and the K domain that mediates protein protein
  interaction"; maps K-domain subdomains for PI/AP3 vs PI/SEP3 interactions. This is the
  IPI reference (WITH UniProtKB:O22456 = SEP3) underlying the GO:0005515 protein binding
  annotation. Supports protein dimerization / PPI but the generic "protein binding" term is
  uninformative.

### Nuclear localization requires AP3+PI co-expression
- PMID:8698240 (McGonigle, Bouhidel, Irish 1996, Genes Dev) — abstract-only but explicit:
  "Transient transformation assays of either the AP3-GUS or PI-GUS fusion protein alone resulted
  in cytoplasmic localization of GUS activity. However, coexpression of AP3-GUS with PI, or
  PI-GUS with AP3, resulted in nuclear localization of GUS activity." This is the basis for BOTH
  the IDA nucleus (GO:0005634) and IDA cytoplasm (GO:0005737) annotations: PI alone is cytoplasmic;
  PI+AP3 is nuclear. The functional (active) localization is nuclear; cytoplasmic localization
  reflects the monomer that has not heterodimerized.

### Direct target regulation (DNA binding in vivo)
- PMID:16640596 (Sundström et al. 2006, Plant J) — abstract-only but explicit: "Using chromatin
  immunoprecipitation, we show that the floral homeotic PISTILLATA (PI) protein ... has the
  ability to bind directly to the promoter region of AP1." This is the IDA reference for
  GO:0003677 (DNA binding). Note: in this case AP3/PI acts to *restrict/down-regulate* AP1.

### B-class genes sufficient for B function
- PMID:8565821 (Krizek & Meyerowitz 1996, Development) — "The Arabidopsis homeotic genes APETALA3
  and PISTILLATA are sufficient to provide the B class organ identity function." (UniProt FUNCTION)
- PMID:9489703 (Sablowski & Meyerowitz 1998, Cell) — AP3/PI activate NAP, an immediate target.
- PMID:11206550 (Honma & Goto 2001, Nature) — MADS complexes (incl. B+E) sufficient to convert
  leaves into floral organs (floral quartet evidence).
- PMID:18417639 (Mara & Irish 2008) — AP3/PI represses GATA21/GNC and GATA22/GNL.

### Phylogeny / family-level ISS and IBA
- PMID:12837945 (Parenicová et al. 2003) and PMID:11118137 (Riechmann et al. 2000) — MADS family /
  TF genome-wide analyses; basis for ISS GO:0003700 (DNA-binding transcription factor activity).
- GO_REF:0000033 IBA annotations (GO:0000978, GO:0000981, GO:0006357) from PANTHER tree
  PTN004327372 with SRF/MEF2/MADS reference members. These RNA Pol II-specific terms are derived
  from the broader SRF/MEF2 superfamily; PI is a plant MIKC MADS TF that regulates Pol II
  transcription, so these are biologically reasonable at family level.

### Secondary cell wall network — likely non-physiological Y1H hit
- PMID:25533953 (Taylor-Teeples et al. 2015, Nature, full text available) — large-scale
  yeast-one-hybrid (Y1H) gene regulatory network for secondary cell wall synthesis. The screen
  used a library of ~1,663 Arabidopsis TFs against xylem cell-wall gene promoters. The GOA IPI
  annotation GO:0000976 (transcription cis-regulatory region binding) with WITH AGI_LocusCode
  AT4G36890 (= IRX14, a xylan biosynthesis glycosyltransferase promoter) derives from PI being one
  of many TFs scored as binding a cell-wall promoter in this high-throughput Y1H screen.
  The paper text: "Each promoter interacted with an average of 38 different proteins, generating
  even more possibilities for combinatorial, redundant, or condition-specific gene regulation."
  PI is a floral organ-identity TF not normally expressed in root xylem; this Y1H hit is best
  treated as a non-core/over-annotated interaction (in vitro DNA-binding capacity, not an in vivo
  floral function). The MF "transcription cis-regulatory region binding" is itself biologically
  true for a MADS TF (PI does bind cis-regulatory CArG boxes), so the term is kept but framed as
  non-core given the screen context.

## Curation decisions rationale

- PI's CORE molecular functions: sequence-specific (CArG-box) cis-regulatory DNA binding,
  DNA-binding transcription factor activity, and AP3/PI heterodimerization (protein dimerization
  activity).
- PI's CORE biological process: specification of floral organ identity (petal + stamen), via
  RNA Pol II transcription regulation.
- PI's CORE location: nucleus (active heterodimer). Cytoplasm reflects the inactive monomer.
- Generic "protein binding" (GO:0005515) is uninformative and is marked over-annotated; the
  underlying biology (dimerization) is captured by GO:0046983.
- No experimental annotation is removed. IEA/electronic annotations that are correct are accepted;
  none are clearly wrong enough to REMOVE.

## GO term definitions verified (QuickGO API, 2026-06)
- GO:0000976 transcription cis-regulatory region binding: "Binding to a specific sequence of DNA
  that is part of a regulatory region that controls transcription of that section of the DNA."
- GO:0010093 specification of floral organ identity: "The process in which a floral organ
  primordium acquires its identity."
