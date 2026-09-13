# DNAJC4 (Q9NNZ3) research notes

## Identity
- DnaJ homolog subfamily C member 4; AltNames DnaJ-like protein HSPF2; MEN1 candidate protein 18 (MCG18).
- 241 aa. Contains a J domain (aa 34-99) [file:human/DNAJC4/DNAJC4-uniprot.txt "DOMAIN 34..99 /note=\"J\""].
- Has a predicted single-pass transmembrane helix (TRANSMEM 156..175) and is annotated as a membrane / single-pass membrane protein [file:human/DNAJC4/DNAJC4-uniprot.txt "SUBCELLULAR LOCATION: Membrane ... Single-pass membrane protein"].
- Tissue: HPA "Tissue enhanced (testis)"; Pharos Tdark (very poorly characterized).
- PAN-GO: 0 GO annotations based on evolutionary models (i.e. family-level functional inference is weak).

## Function status
- A J-domain protein, so by family it is an HSP70 (DnaJ/HSP40) co-chaperone, but there is essentially NO direct experimental characterization of its activity. UniProt does not even provide a FUNCTION comment.
- The original cloning paper is available only as a cached abstract. It establishes
  that MCG18/DNAJC4 contains a J domain and predicts a membrane-spanning region, but
  reports no folding, unfolded-protein-response, client-binding, HSP70-binding, or
  ATPase assay [PMID:9473517, "The MCG18 cDNA is predicted to encode a 241 amino acid
  product that has partial homology to Escherichia coli dnaJ in that it contains the
  J domain."]. The NAS/TAS process annotations are therefore retained cautiously as
  non-core family-level assertions, not as demonstrated DNAJC4 activities.

## Interactions (GOA / IntAct)
- HTT (huntingtin, P42858); NbExp=12 [file:human/DNAJC4/DNAJC4-uniprot.txt "Q9NNZ3; P42858: HTT; NbExp=12"]. From Huntingtin-interactome screens (PMID:17500595 = Kaltenbach et al., HTT interactors).
- WFS1 (wolframin, O76024); NbExp=3 [file:human/DNAJC4/DNAJC4-uniprot.txt "Q9NNZ3; O76024: WFS1; NbExp=3"]. From PMID:32814053 (neurodegeneration interactome).
- These are high-throughput / focused interactome screens; "protein binding" (GO:0005515) is uninformative; partners (HTT, WFS1) do not define a chaperone client repertoire.

## Curation judgment
- GO:0030544 Hsp70 protein binding is retained as a deliberately hedged core
  prediction from the canonical J domain and intact HPD motif, consistent with the
  treatment of similarly uncharacterized J proteins in this repository. It is not a
  claim of direct biochemical validation [file:human/DNAJC4/DNAJC4-uniprot.txt
  "LHPDRDPGNP"]. GO:0051082 is formally obsolete, and its
  current consider terms, GO:0044183 protein folding chaperone and GO:0140309
  unfolded protein holdase activity, require activities that have not been assayed
  for DNAJC4. GO:0001671 ATPase activator activity also remains unverified.
- Membrane localization: predicted single-pass TM; reasonable to KEEP_AS_NON_CORE / ACCEPT as predicted.
- Protein binding IPI (HTT, WFS1): MARK_AS_OVER_ANNOTATED because the generic term
  adds no mechanistic information, while preserving the interaction provenance.
- response to unfolded protein (TAS) and protein folding (NAS): family/inference-level; keep as non-core.

## 2026-08-28 dedicated annotation re-review

- The current GOA export has 8 physical rows and 7 exact qualifier-aware
  signatures: 3 membrane-localization signatures, 2 protein-binding signatures,
  and 2 process signatures. The PMID:32814053 signature collapses two physical IPI
  rows with different WITH/FROM partners (WFS1 and HTT). Every signature is reviewed
  exactly once, with no pending or undecided action.
- DNAJC4 is a member of PANTHER PTHR44825:SF1. The current family cache contains
  human DNAJC4, mouse Dnajc4, and Drosophila DnaJ-60, but has no PAINT annotation
  file; GOA contains no IBA row or PTN identifier for DNAJC4. No phylogenetic
  function was inferred from the family name or its unchecked generated description.
- PMID:17500595 has cached full text and supports a large-scale HTT-interactor
  screen. PMID:32814053 is abstract-only and describes the network-level screen but
  does not name DNAJC4 in the abstract. The IPI rows were not rejected; only the
  uninformative generic `protein binding` function was marked over-annotated.
- PMID:9473517 is now cached abstract-only, correcting the earlier note that it was
  unavailable. Its identifier and title are verified, and its evidentiary boundary
  is recorded explicitly in the review.
