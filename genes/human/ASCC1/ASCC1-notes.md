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
