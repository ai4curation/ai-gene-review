# sdf-9 (eak-5, Y44A6D.4; UniProt G5EGA9) curation notes

## Provenance / process

- Deep research via falcon was not attempted: the falcon provider is known to fail for this
  batch (HTTP 402). No `-deep-research-*.md` file exists; notes below are from the cached
  primary literature plus a local sequence analysis.
- PubMed search ("sdf-9 elegans OR eak-5 elegans") returned 5 PMIDs: 12783794, 16839187,
  17660545, 15509773, 21209831. Cached 17660545 (Jensen et al. 2007, SDF-9/DAF-2) and
  15509773 (NCR-1/NCR-2; abstract does not mention sdf-9, not cited). 21209831 is a broad
  DAF-16 target RNAi screen, not used.
- Full text available: PMID:16839187 (Hu et al. 2006, PLoS Genet) only. PMID:12783794
  (Ohkura et al. 2003) and PMID:17660545 (Jensen et al. 2007) are abstract-only in cache.

## Identity and sequence

- 345 aa; single PTP catalytic domain (PROSITE PRU00160, residues 33-284); PANTHER
  PTHR19134:SF561. No transmembrane segment, no N-myristoylation motif
  [PMID:16839187 "Neither SDF-9 nor EAK-6 possesses an N-myristoylation motif or a predicted transmembrane domain."].
- Catalytic cysteine absent: [PMID:16839187 "Whereas SDF-9 does not retain the canonical catalytic cysteine residue found in all known PTPs and is therefore predicted to be catalytically inactive"].
- Own residue check (file:worm/sdf-9/sdf-9-bioinformatics/RESULTS.md): PTP1B `HCSAGIGRSG`
  aligns gap-free to SDF-9 `QSARGSSRAG` (222-231). Catalytic Cys -> **Ser223** (UniProt
  CAUTION says "lysine at position 223"; the sequence has serine - the CAUTION text is wrong
  about the substituting residue, which matches the PTHR19134 family review's note). Also
  His214 -> Gln, P-loop Ser222 -> Ala, pTyr-loop Tyr46 -> Val. Arg221 (P-loop) retained.
- Hu et al. count: [PMID:16839187 "15 are conserved in EAK-6 and 13 are conserved in SDF-9"] of 19
  invariant vertebrate PTP residues.
- No direct phosphatase assay on SDF-9 is reported; PNPP assays were done on EAK-6 (inactive)
  [PMID:16839187 "revealed no hydrolytic activity on the substrate p-nitro-phenylphosphate (PNPP)"].

## Molecular function (what is it, if not a phosphatase?)

- Hypotheses only: substrate-trap-like pTyr binding / adaptor.
  [PMID:16839187 "Thus, EAK-6 and SDF-9 may be inactive phosphatase homologs that bind to tyrosine phosphoproteins."]
- But experimental tests were negative (unpublished data within the paper):
  [PMID:16839187 "epitope-tagged SDF-9 and EAK-6 did not coprecipitate tyrosine phosphoproteins after exposure of transfected cultured 293T cells to IGF-1"]
  and no phosphoinositide binding
  [PMID:16839187 "radiolabeled SDF-9 and EAK-6 synthesized in vitro did not bind to phosphoinositides immobilized on nitrocellulose"],
  and no direct EAK-4/SDF-9/EAK-6 interaction in 293T coIP.
- Jensen et al. 2007 propose a DAF-2 interaction / adaptor role, from genetics (abstract only)
  [PMID:17660545 "We propose that SDF-9 stabilizes the active phosphorylated state of DAF-2 or acts as an adaptor protein to enhance insulin-like signaling."].
- Conclusion: MF is unknown. No GO MF term is supportable; do not propose phosphotyrosine
  binding (the only test was negative).

## Localization and expression

- Expressed only in the two XXXL/R head cells [PMID:12783794 "we identified these cells as XXXL/R cells"].
- Plasma membrane (GFP fusion) [PMID:16839187 "EAK-4::GFP, SDF-9::GFP, and EAK-6::GFP fusion proteins localize to the plasma membrane of XXX."];
  independent of DAF-2 signalling [PMID:16839187 "indicating that its localization does not require normal levels of DAF-2/InsR signaling"].
- Ohkura 2003 (UniProt) gives "Cytoplasm" plus dendrite-like structure; abstract does not state
  this, full text not cached. The two are compatible (peripheral membrane protein at the cell
  cortex of XXX cells).

## Biological process

- Dauer: sdf-9 mutants form dauer-like larvae resembling daf-9/daf-12 Daf-c; enhanced by
  cholesterol deprivation [PMID:12783794 "Like these mutants, the dauer-constitutive phenotypes of sdf-9 mutants were greatly enhanced by cholesterol deprivation."].
- Acts with DAF-9 (dafachronic acid synthesis) [PMID:12783794 "suggested that SDF-9 increases the activity of DAF-9 or helps the execution of the DAF-9 function"].
- Insulin pathway (eak screen): phenotypes suppressed by daf-16; act in parallel to akt-1;
  eak-4, sdf-9, eak-6 same pathway/complex [PMID:16839187 "indicating that EAK-4, SDF-9, and EAK-6 function in the same pathway or complex"].
- Model: [PMID:16839187 "In XXX, SDF-9 may function with DAF-9/CYP27A1 to promote the synthesis and/or secretion of dafachronic acids"].
- Partial dauers, alae but no pharyngeal remodelling.

## Decisions summary

- NOT PTP activity (IKR): ACCEPT - well supported by residue loss.
- No positive PTP IBA/IEA rows exist in GOA for sdf-9 (PAINT already withholds GO:0004725 from
  SF561), so no REMOVE needed for PTP activity.
- IBA signal transduction: KEEP_AS_NON_CORE (true but uninformative).
- CC rows: accept PM IDA; cytoplasm EXP accept with caveat; IEA PM accept; IEA cytoplasm keep non-core.
- dauer larval development IMP/IGI/IEA: ACCEPT (standard WormBase usage; gene acts as negative
  regulator of dauer entry).
- No NEW annotations: insulin receptor signalling participation is not shown (genetic placement
  only, "upstream of or in parallel to"). Raised as question.

## Implication for PTHR19134 family review

- Confirms SDF-9 as a valid exception to family-wide GO:0004725 (Ser at catalytic Cys
  position 223, plus loss of His and P-loop Ser/Thr). GOA already carries NOT|enables
  GO:0004725 (IKR) for sdf-9, consistent with the family review. Note EAK-6 (same SF561)
  retains Cys but showed no PNPP activity and has other invariant-residue substitutions.
