# narL (E. coli K-12, P0AF28) curation notes

## Deep research status

- 2026-10-23: `just deep-research ECOLI narL --provider perplexity` failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist").
- 2026-10-23: `just deep-research ECOLI narL --provider falcon` failed
  ("Exception: Failed to authenticate").
- No deep-research file exists; these notes were compiled manually from the
  cached publications (mostly abstract-only) and the UniProt record.

## Identity and architecture

- 216 aa NarL, response regulator of the NarX/NarQ-NarL two-component system.
  UniProt: N-terminal receiver (REC) domain 8..124, phosphorylation site Asp59
  (4-aspartylphosphate; PROSITE-ProRule inference), C-terminal LuxR/FixJ-type
  HTH domain 149..214 with H-T-H motif 173..192 [file:ECOLI/narL/narL-uniprot.txt].
- UniProt function: "This protein activates the expression of the nitrate
  reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses
  the transcription of the fumarate reductase (frdABCD) operon in response to a
  nitrate/nitrite induction signal transmitted by either the NarX or NarQ
  proteins." [file:ECOLI/narL/narL-uniprot.txt]
- PANTHER PTHR43214:SF38; InterPro IPR039420 WalR-like, IPR000792 LuxR-type HTH.

## Phosphorylation (receiver activity)

- NarX autophosphorylates and transfers phosphate to NarL; NarX also
  dephosphorylates NarL-P [PMID:8473280 "Incubation of the labeled NarX with
  purified NarL resulted in the transient phosphorylation of NarL."].
- Cytoplasmic domains of both NarX and NarQ phosphorylate NarL; NarQ transfers
  faster, NarX is the stronger phosphatase; NarL also autophosphorylates with
  acetyl phosphate [PMID:8051011 "Each protein transferred its phosphoryl group
  to purified NarL protein"; "NarL was autophosphorylated with acetyl phosphate
  but not with ATP as a substrate"].
- D59N is a recessive null [PMID:2066339 "This change, narL502(D59N), was a
  recessive null allele, which is consistent with the hypothesis that NarL
  requires phosphorylation for activation."].
- Genetics: narX narQ double mutants lose all nitrate regulation, and all
  regulation requires narL [PMID:1508040].
- Conclusion: GO:0000156 phosphorelay response regulator activity is well
  supported (biochemistry + Asp59 genetics) but absent from GOA; proposed as NEW.

## Structure / mechanism

- Unphosphorylated NarL: output domain packs against receiver, occluding the
  DNA-recognition surface ("telephone receiver" model) [PMID:8780507;
  PMID:9521685].
- NarL C-terminal domain-DNA co-crystal: binds as a dimer with a new
  dimerization interface, bends DNA [PMID:12352954].

## DNA binding and regulation

- Binds TACYYMT heptamers; 7-2-7 inverted repeats preferred, but NarL (unlike
  NarP) also recognizes other heptamer arrangements [PMID:9302020; PMID:7854119;
  PMID:8736541].
- Activator: narGHJI, fdnGHI, nirB (with FNR) [PMID:8736541; PMID:7854119].
- Repressor: frdABCD, dmsABC, ynfEFGHI (binds -10 overlapping site at ynfE,
  forms NarL-FNR-RNAP-promoter complex) [PMID:19251855; PMID:7854119 (nrf
  repression by nitrate); PMID:9696769 (antagonizes NarP activation at napF)].

## Interactions

- NarX-NarL interaction (IntAct; PMID:21078995 abstract is about NarX
  phosphatase mechanism; the specific binary interaction data are in the full
  text). Generic protein binding -> REMOVE per policy.
- Self interaction: IPI from PMID:12352954 (dimer on DNA) and PMID:26635367
  (RcsB heterodimer study; NarL self-interaction presumably from the
  two-hybrid/control data in the full text, not visible in the cached abstract).

## Location

- Cytosolic proteomics (PMID:18304323) - soluble cytosolic regulator; NarL
  itself is not named in the cached main text (supplementary table).
