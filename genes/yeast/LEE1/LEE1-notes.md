# LEE1 (YPL054W) — Gene Review Notes

Systematic name: YPL054W. SGD standard name: LEE1. SGD ID: S000005975. UniProt: Q02799.
Organism: *Saccharomyces cerevisiae* (S288c), NCBITaxon:559292.

This is an UNDERSTUDIED ("dark") gene. Primary deliverable is an honest `knowledge_gaps`
section, with `description`/`core_functions` grounded strictly in domain architecture,
orthology, and the (sparse) literature. No invented function.

## Summary of what is KNOWN vs NOT known

### KNOWN (well-supported)
- **301-aa protein** with **two CCCH-type (C3H1) zinc fingers**: ZN_FING 87–114 (C3H1-type 1)
  and ZN_FING 123–145 (C3H1-type 2) [UniProt Q02799, FT ZN_FING records; PROSITE PS50103 ZF_C3H1 x2;
  SMART SM00356 ZnF_C3H1 x2]. Pfam PF00642 (zf-CCCH) and PF18044 (zf-CCCH_4).
- **Zinc/metal-binding is domain-defensible**: CCCH zinc fingers coordinate Zn2+ via 3 Cys + 1 His.
  KW: Metal-binding, Zinc, Zinc-finger. LEE1 was independently identified as one of 582 known/potential
  zinc-binding proteins in a proteome-wide bioinformatic+MS survey of the yeast zinc proteome
  [PMID:30358795 "The yeast zinc proteome of 582 known or potential zinc-binding proteins was identified
  using a bioinformatics analysis that combined global domain searches with local motif searches."] —
  this is the source of the RCA GO:0008270 (zinc ion binding) annotation.
- **Phosphoprotein**: phosphoserine at Ser-21, Ser-30, Ser-282 detected in large-scale phosphoproteomics.
  Ser-21/30/282 are Cdk1-substrate-related sites [PMID:19779198, "Global analysis of Cdk1 substrate
  phosphorylation sites"]. N-terminal region (1–25) is disordered (MobiDB-lite), polar-residue biased.
- **PANTHER family**: PTHR11224 MAKORIN-RELATED; subfamily **PTHR11224:SF10** (IP09428P-RELATED)
  [interpro/panther/PTHR11224 cached data]. eggNOG KOG1039.
- **Viable null**; documented deletion phenotypes at SGD (all from high-throughput screens): altered
  chemical resistance/accumulation, decreased competitive fitness, increased sporulation efficiency;
  overexpression -> increased invasive growth, decreased vegetative growth [SGD YPL054W phenotype summary,
  yeastgenome.org]. ~74 interactors / 82 interactions at BioGRID, essentially all high-throughput; 0
  curated GO function/process/component annotations at BioGRID [thebiogrid.org/36126].

### NOT known (the real knowledge gaps)
- **Molecular function beyond zinc coordination is unknown.** No experimental demonstration of a
  catalytic or binding activity. CCCH zinc fingers are canonically **nucleic-acid (frequently RNA)
  binding** modules, so RNA/nucleic-acid binding is a reasonable domain-based hypothesis — but there is
  no direct experimental evidence (LEE1 was not specifically reported as a hit in the yeast RNA
  interactome-capture datasets I checked).
- **Whether LEE1 is a ubiquitin ligase is unresolved — and there is a strong biological argument
  against it.** See "Makorin/E3-ligase over-propagation" below.
- **Biological process is unknown.** SGD/GO: biological_process = ND. Deletion phenotypes are
  pleiotropic HTP-screen readouts, not a defined pathway.
- **Subcellular localization is unknown** (GO cellular_component = ND).
- **What (if anything) it binds** (RNA? DNA? which targets?) is unknown.

## Makorin / E3-ligase over-propagation analysis (the central curation issue)

The GOA annotations `ubiquitin protein ligase activity` (GO:0061630) and the ubiquitination process
terms (`protein ubiquitination` GO:0016567, `protein polyubiquitination` GO:0000209) all trace to the
**MAKORIN family (PANTHER PTHR11224 / InterPro IPR045072 MKRN-like)**:

- IBA (GO_REF:0000033): propagated from PANTHER node PTN000131854, seeded (IBD) from
  **UniProtKB:Q9UHC7 (human MKRN1)**, **UniProtKB:Q13064 (human MKRN3)**, **MGI:1914277 (mouse Mkrn2)**
  [PTHR11224-paint.tsv]. All three seed proteins are metazoan **makorins that possess a catalytic RING
  domain**.
- IEA (GO_REF:0000002 / InterPro): from IPR045072 (MKRN-like) and IPR041367 ("E3 ligase, CCCH-type
  zinc finger").

**Makorins are RING-finger E3 ubiquitin ligases**: their domain architecture is multiple CCCH zinc
fingers + a **C3HC4 RING** domain that is the actual ubiquitin-transfer (catalytic) module.

**Critical finding: LEE1 has NO RING domain.** Its full InterPro/Pfam complement is only CCCH zinc
fingers (IPR000571, IPR036855, IPR041367, PF00642, PF18044) plus MKRN-like (IPR045072). Direct
InterPro API query on Q02799 returns **no zf-C3HC4 / RING-type (IPR001841) signature**
[EBI InterPro API entry/all/protein/uniprot/Q02799, verified 2026-07-05: "this protein does not
contain a RING domain"]. LEE1 is 301 aa; the metazoan makorin seeds are longer (MKRN1/2/3 ~400+ aa)
and carry the RING.

LEE1's PANTHER subfamily **SF10** is heterogeneous — it contains true RING-makorins (plant MKRN,
*C. elegans* lep-2, rice MKRN) AND poxvirus host-range factor p28 — so subfamily membership does not
confer the ligase function. **Because the catalytic RING module is absent in LEE1, propagating
"ubiquitin protein ligase activity" to it is a domain-based over-annotation** (the specific catalytic
domain required for the function is not present). This is a Type-6-style paralog/subfamily
over-propagation of a catalytic activity onto a protein lacking the catalytic domain.

Curation consequence:
- GO:0061630 (ubiquitin protein ligase activity), both IBA and IEA -> **MARK_AS_OVER_ANNOTATED**
  (RING absent; catalytic activity not supportable). Per project rules, I do not REMOVE IBA outright,
  but flag as over-annotation on biological grounds (no catalytic domain).
- GO:0016567 (protein ubiquitination) IBA and GO:0000209 (protein polyubiquitination) IEA -> the
  associated *process* likewise over-propagated from the ligase function -> **MARK_AS_OVER_ANNOTATED**.
- GO:0046872 (metal ion binding) IEA / GO:0008270 (zinc ion binding) RCA -> domain-defensible ->
  **ACCEPT** (zinc binding is real per CCCH fingers; keep zinc as the more specific term). Metal ion
  binding is the generic parent; keep but note zinc is more precise.
- GO:0005575 (cellular_component ND), GO:0008150 (biological_process ND) -> **ACCEPT** as
  root/ND placeholders (correctly signal "unknown"; standard practice to keep ND roots).

## References checked
- PMID:30358795 — Wang et al. 2018 Metallomics, yeast zinc proteome. Abstract-only cached; supports
  LEE1 as a (predicted) zinc-binding protein; source of RCA zinc-binding annotation. Relevance MEDIUM,
  VERIFIED (title matches PubMed; supports zinc-binding classification, not a specific function).
- PMID:19779198 — Holt et al. 2009 Science, Cdk1 substrate phosphosites (UniProt ref for phosphosites).
- SGD YPL054W (yeastgenome.org) — "Zinc-finger protein of unknown function"; phenotype summary.
- BioGRID 36126 — 74 interactors, HTP only, 0 curated GO.
- InterPro Q02799 (EBI API) — domain complement; confirms NO RING.
- PANTHER PTHR11224 (cached) — MAKORIN-RELATED family; SF10; IBA seeds are RING makorins.

## Domain reasoning for core_functions / description
- Confident: zinc ion binding (GO:0008270) via 2 CCCH zinc fingers — the ONLY molecular activity
  supportable.
- Reasonable hypothesis (NOT asserted as core; put in knowledge_gaps): nucleic-acid / RNA binding
  (GO:0003676 / GO:0003723), the canonical role of CCCH zinc-finger tandems.
- NOT supportable: ubiquitin ligase activity (no RING), specific transcription-factor role.

## Falcon deep research (LEE1-deep-research-falcon.md) — corroborating findings

Falcon deep research completed (~28 min). It strongly corroborates the analysis above and adds
grounded, literature-anchored findings (citations are DOI/deep-research style; primary PMIDs noted):

- **Nitrogen catabolite repression (NCR) target**: Godard et al. 2007 (PMID:17308034,
  Mol Cell Biol 27:3065-3086) highlighted LEE1/YPL054W as one of only a few differentially
  expressed regulator-encoding genes of unknown function among nitrogen-responsive genes, and
  described it as "a protein containing two tandem repeats of the CCCH-type zinc finger domain"
  with "further experiments will be required to determine the functions" (per falcon, quoting the
  full text; the LEE1-specific text is in the full text, NOT in the abstract-only cached record,
  so it cannot be used as a verbatim supporting_text quote). This is an EXPRESSION/regulation
  observation, not a molecular-function assignment.
- **Minisatellite stability screen**: Alver et al. 2013 — lee1Δ/ypl054wΔ appeared in a
  stationary-phase minisatellite (ade2-h7.5 reporter) stability screen, hinting at a role in
  genome repeat stability under that assay. HTP-screen level evidence.
- **CCCH parallel to Cth2**: Godard et al. noted LEE1's CCCH domain is shared with Cth2, a
  characterized yeast tandem-CCCH RBP that binds 3' ends of mRNAs and accelerates their decay
  (iron-deficiency regulon). Supports the RNA-binding hypothesis (still unproven for LEE1).
- **Cytoplasmic localization**: reported from the Huh et al. 2003 global GFP study via SGD
  (database-supported, not primary-re-read). Consistent with post-transcriptional RNA regulation.
- **No RING / no ligase demonstrated**: falcon explicitly states makorin RING E3 ligase activity
  is a metazoan-homolog feature and "direct ligase activity has not been demonstrated for yeast
  Lee1" — consistent with my MARK_AS_OVER_ANNOTATED call on the ubiquitin-ligase terms. Best RQC
  E3 in yeast is Hel2 (ZNF598 homolog); LEE1's contribution unexplored.

Provenance policy: I do NOT add falcon-sourced supporting_text quotes to supporting_text fields
(validator skips file: quotes; fabrication risk). Godard 2007 (PMID:17308034) added to references
with correctness UNVERIFIED because the LEE1-specific claim is not verifiable in the cached
abstract-only record. These findings inform the description prose and knowledge_gap boundaries
(reviewer synthesis), not verbatim-quoted supporting_text.
