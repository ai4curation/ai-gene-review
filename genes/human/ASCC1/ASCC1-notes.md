# ASCC1 review notes

## Deep research status

Attempted `just deep-research-falcon human ASCC1 --fallback perplexity-lite` on
2026-06-03. Falcon timed out after the wrapper's 600-second provider timeout, and
the configured `perplexity-lite` fallback failed with a Perplexity API 401 quota
error. No `ASCC1-deep-research-falcon.md` or fallback provider report was
created. This review therefore uses the cached primary literature, UniProt/GOA,
Reactome entries, and the PN projection report directly.

## Summary

ASCC1 encodes the p50 subunit of the human ASC-1/ASCC complex. The strongest
evidence supports two connected nuclear roles:

- transcription coactivation as part of ASC-1, with the endogenous complex
  required for AP-1, SRF, and NF-kappaB transactivation [PMID:12077347 "these
  results suggest that the endogenous hASC-1 complex appears to play an
  essential role in AP-1, SRF, and NF-kappaB transactivation"].
- accessory/regulatory participation in ALKBH3-ASCC DNA alkylation repair,
  where ASCC1 interacts through ASCC3 and coordinates proper ASCC recruitment
  during alkylation damage [PMID:29997253 "ASCC1 coordinates the proper
  recruitment of the ASCC complex during alkylation"].

Human loss-of-function genetics supports biological importance in neuromuscular
development, but the immediate molecular interpretation remains ASC-1/ASCC
complex dysfunction rather than an independent developmental signaling activity
[PMID:26924529 "Our findings indicate that the dysfunction of a transcriptional
coactivator complex can result in a clinical syndrome affecting the
neuromuscular system."].

## Proteostasis PN projection

The PN projection report proposes two candidate additions for ASCC1:
GO:0006515 protein quality control for misfolded or incompletely synthesized
proteins and GO:0072344 rescue of stalled cytosolic ribosome, from
`Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv
"ASCC1		GO:0072344	rescue of stalled cytosolic ribosome"].

I did not promote these to ASCC1 GO annotations. The ASCC1-specific literature
reviewed here supports nuclear ASCC transcription and alkylation-damage repair,
not cytosolic ribosome rescue. The key ASCC alkylation-damage paper says ASCC1
loss affects ASCC3/ASCC2 recruitment and MMS sensitivity [PMID:29997253 "ASCC1
knockout through a CRISPR/Cas9 approach results in alkylation damage sensitivity
in a manner epistatic with ASCC3."]. The broader ASCC pathway paper ties ASCC
foci to alkylated nucleotides, elongating RNA polymerase II, splicing factors,
and K63-linked ubiquitin signaling rather than ribosome rescue [PMID:29144457
"These foci associate with alkylated nucleotides, and coincide spatially with
elongating RNA polymerase II and splicing components."].

Conservative PN decision: treat the ASCC1 ribosomal-rescue/RQC projection as
unsupported by ASCC1-specific evidence in this review. It remains a suggested
expert question rather than a proposed annotation.

## Annotation decisions

- Accepted nuclear and nuclear-speck localization. PMID:29997253 directly says
  ASCC1 is present at nuclear speckle foci before damage and leaves those foci
  after alkylation [PMID:29997253 "ASCC1 is present at nuclear speckle foci
  prior to damage, but leaves the foci in response to alkylation."].
- Accepted DNA alkylation repair and DNA repair complex participation. PMID
  22055184 establishes ALKBH3 association with ASCC and a repair mechanism
  [PMID:22055184 "Our data provide a molecular mechanism by which ALKBH3
  collaborates with ASCC to maintain genomic integrity in a cell-type specific
  manner."]. PMID:29144457 establishes an alkylation-specific ubiquitin pathway
  and ASCC1/ASCC3 complex association [PMID:29144457 "Mass spectrometric
  analysis of ASCC2-associated proteins revealed the constitutive association of
  ASCC3 and ASCC1"].
- Removed DNA replication. The cited ASCC1 paper supports alkylation damage
  repair, not DNA replication. The related ASCC pathway paper reports foci in
  G1/early S and distinct from PCNA, which is insufficient for direct DNA
  replication curation [PMID:29144457 "These foci were also distinct from
  GFP-PCNA or BMI-1"].
- Marked generic protein binding annotations as over-annotated. ASCC1 physical
  interactions are real, especially with ASCC3, but GO:0005515 is less useful
  than ASCC complex membership and DNA alkylation repair [PMID:29997253 "ASCC1
  interacts with the ASCC complex through the ASCC3 helicase subunit."].
- Marked RNA binding as over-annotated rather than core. PMID:29997253 supports
  a putative RNA-binding motif requirement, but does not itself demonstrate
  direct ASCC1 RNA binding [PMID:29997253 "a function that appears to depend on a
  putative RNA-binding motif near the ASCC1 C terminus."]. PMID:29144457 shows
  direct ssRNA binding for ASCC3, not ASCC1 [PMID:29144457 "Purified ASCC3 bound
  to ssRNA in vitro"].

## Falcon deep research findings (2026-06-07)

A Falcon (Edison Scientific) deep research report was generated on 2026-06-07
(`ASCC1-deep-research-falcon.md`), superseding the earlier failed Falcon attempt
noted above. Synthesis of KEY findings, emphasizing what is NEW relative to the
existing COMPLETE review:

- NEW (most material): Direct, sequence-selective RNA binding by ASCC1 is now
  experimentally demonstrated. Chinnam et al. 2024 (PMID:38750793, J Biol Chem)
  solved crystal/SAXS structures and showed by EMSA that ASCC1 binds
  CGCG-containing RNA (detectable at ~60 nM), abolished by a KH GXXG->GDDG
  mutation, with no shift on the corresponding DNA. This is the first DIRECT
  ASCC1 RNA-binding evidence and partially addresses the prior caveat that
  only ASCC3 (not ASCC1) had shown direct nucleic-acid binding. The existing
  GO:0003723 RNA binding annotation (currently MARK_AS_OVER_ANNOTATED) is now
  better supported as a genuine molecular activity, though physiological
  endogenous RNA targets remain undefined. Note PMID:38750793 is not in the
  local publications cache, so it is added as a statement-only reference and
  NOT used to flip the existing IEA annotation's action.

- NEW (domain architecture): ASCC1 uniquely couples an N-terminal KH-like domain
  (with a newly named helix-clasp-helix / HCH nucleotide-binding motif) to a
  C-terminal two-histidine (2H) phosphodiesterase (PDE) / "RNA ligase-like"
  module with two HXT motifs [PMID:38750793]. This sharpens the prior generic
  "RNA-ligase-like region" description into a defined KH-HCH + 2H-PDE
  architecture.

- PROVISIONAL/CAUTION (enzymology): The 2H-PDE domain is structurally present
  but NO catalytic activity was detected on a tested 2-5A substrate by human or
  Alvinella ASCC1 (positive control VP3-CTD cleaved >95%); an atypical conserved
  active-site histidine rotamer implies a noncanonical substrate
  [PMID:38750793]. Do NOT assert a specific PDE reaction/substrate. No GO
  catalytic-activity annotation is warranted at present.

- CONFIRMS: ASCC1 is a regulatory/accessory subunit of the ASC-1/ASCC complex
  (with ASCC2, ASCC3, TRIP4); ASCC3 directly binds ASCC1 and scaffolds the
  ASCC1-ASCC2 association (ASCC1 and ASCC2 do not bind directly). ASCC1 localizes
  to nuclear speckles (co-localizing with PRP8) and leaves foci on alkylation
  damage; ASCC1 loss dysregulates ASCC2/ASCC3 recruitment and causes MMS
  hypersensitivity epistatic with ASCC3 (Soll 2018, PMID:29997253; Soll 2019
  thesis). All already captured in the review.

- NEW (pathway context, complex-level): The ASC-1/ASCC complex has expanding
  translation-linked roles. Kito et al. 2023 (PMID:37092320, EMBO J) found ASCC
  (ASCC1/2/3, TRIP4) associates with scanning ribosomes and promotes translation
  initiation on a subset of transcripts (ASCC3-driven). Miscicka et al. 2024
  (PMID:38366554, Nucleic Acids Res) reconstituted ASCC-mediated ribosome
  disassembly downstream of ZNF598 ubiquitination and report ASCC1 is
  DISPENSABLE for the cytoplasmic ribosome-splitting step while remaining
  essential for the nuclear DNA-repair function. This is complex-level / ASCC3-
  and ASCC2-centric evidence and supports the existing conservative decision NOT
  to add cytosolic ribosome-rescue (RQC) GO annotations to ASCC1 specifically;
  it strengthens the suggested expert question on this point.

- NEW (disease mechanism): Voraberger et al. 2023 (PMID:37455927, Front
  Endocrinol) gives a SMABF2 bone-mechanism: ASCC1 knockdown in hMSCs suppresses
  osteoblastogenesis (>90% reduced mineralization) and increases adipogenesis,
  with downregulation of RUNX2/SERPINF1 and reduced TGF-beta/SMAD3 signaling,
  framing ASCC1 as a pro-osteoblastogenic / anti-adipogenic regulator. This is
  downstream/pleiotropic disease-phenotype data; it elaborates the SMABF2 link
  (PMID:26924529) but does not by itself justify a new core molecular-function
  GO annotation. Captured as a reference and supporting context only.

- PROVISIONAL (biomarker): Chinnam 2024 TCGA analysis (~7000 tumors) reports
  ASCC1 mRNA overexpression in 7/15 tumor types and a poor-prognosis association
  in pancreatic adenocarcinoma (HR ~3.7) [PMID:38750793]. Exploratory
  bioinformatic association only; not annotation-relevant.

Net curation effect: add four genuinely-new primary references (PMID:38750793,
PMID:37092320, PMID:38366554, PMID:37455927) as statement-only entries
(full_text_unavailable), refine the GO:0003723 RNA binding review.reason to note
the now-direct CGCG RNA-binding evidence (without changing the action), and add
targeted suggested questions/experiments. No existing annotation action changed.
