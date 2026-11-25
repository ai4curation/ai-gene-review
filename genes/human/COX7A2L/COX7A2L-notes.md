# COX7A2L notes

## Setup

- Ran `just fetch-gene human COX7A2L`, creating the review stub, GOA table, UniProt flat file, PANTHER
  PTHR10510 metadata, and missing seeded publications.
- Ran `just fetch-gene-pmids human COX7A2L`; all seeded PMIDs were present after the fetch.
- Tried `just deep-research-falcon human COX7A2L --fallback perplexity-lite`; Falcon was unavailable in this
  environment and the fallback Perplexity path required `agentapi`, which was absent. This file is the manual
  synthesis rather than a provider deep-research artifact.
- Added PMID:33727070 manually because UniProt's COX7A2L function text cites it as a follow-up human SCAFI
  complexome study.

## Functional Synthesis

COX7A2L/SCAFI is a small cytochrome c oxidase VIIa-like protein with a cleavable mitochondrial targeting
sequence and a single predicted transmembrane helix. The best-supported direct function is not autonomous
cytochrome-c oxidase activity, but an adaptor role at the inner mitochondrial membrane. Human COX7A2L binds
primarily free complex III and, to a lesser extent, complex IV, "to specifically promote the stabilization of
the III2+IV supercomplex without affecting respirasome formation" [PMID:27545886].

The 2018 human knockout work strengthens that split: "COX7A2L-KO cells lack SC III2+IV" but have "normal de
novo complex IV biogenesis" and normal steady-state respirasome levels [PMID:30428348]. PMID:33727070's
abstract adds that SCAFI ablation preferentially loses CIII2+IV and a minor subset of respirasomes, but also
states that in wild-type HEK293T cells the majority of respirasomes contained COX7A2 rather than SCAFI.
Together, these papers argue for CIII2+IV/specific respiratory supercomplex assembly as the direct COX7A2L
process.

The older GO:0004129 cytochrome-c oxidase activity TAS row traces to the cloning paper that named COX7RP.
That paper reports that EB1 "encodes a 114-amino-acid protein similar to the cytochrome c oxidase subunit
VIIa" [PMID:9418891]. It does not measure oxidase activity.

PMID:31023583 connects this gene to the 66b5638000001589 GO-CAM context: "The PERK-eIF2α-ATF4 axis
increases supercomplex assembly factor 1 (SCAF1 or COX7A2L), promoting SCs and enhanced mitochondrial
respiration." The cached abstract is enough to support stress-induced SCAF1 expression but not enough to
distinguish CIII2+IV, minor SCAFI-dependent respirasomes, and canonical COX7A2-dependent respirasomes.

## GO-CAM 66b5638000001589 Consistency

The model's COX7A2L activity node correctly uses `GO:0030674` protein-macromolecule adaptor activity with
complex III and complex IV as inputs and occurs in the mitochondrial inner membrane. Its `part_of`
`GO:0097250` mitochondrial respirasome assembly edge is the remaining mismatch: this gene review modifies the
four GOA `GO:0097250` rows to the broader existing `GO:0033108` mitochondrial respiratory chain complex
assembly term, with a CIII2+IV-specific supercomplex assembly NTR, because GO:0097250 is defined for assembly
of complexes I, III, and IV into a respirasome.

Record for the final GO-CAM consistency PR after this gene PR merges:

- `gomodel:66b5638000001589/66b5638000001650` should be revisited. Consider replacing `part_of GO:0097250`
  with a CIII2+IV respiratory supercomplex assembly term after GO adds one, or otherwise documenting that the
  GO-CAM process term is broader/different than the direct COX7A2L process in PMID:27545886 and
  PMID:30428348.
