# sipS (Bacillus subtilis 168, UniProt P28628) - curation notes

## Deep research status

Automated deep research could not be generated on 2026-11-13:

- `just deep-research BACSU sipS --provider perplexity` failed: "Provider 'perplexity' not available. Available: falcon, openscientist, claude_code".
- `just deep-research BACSU sipS --provider falcon` failed: "falcon: 403 Failed to authenticate -- the API key is missing, invalid, or lacks access to this endpoint".
- `just deep-research BACSU sipS --provider openai` failed: "Provider 'openai' not available".

These notes are therefore a manual summary of the cached publications (all abstract-only:
PMID:1639057, PMID:7876097, PMID:8951809, PMID:9694797, PMID:10982814, PMID:9823656) and the
UniProt record.

## Identity

- SipS (signal peptidase of subtilis) is a 184-residue type I signal peptidase (S26A family)
  [PMID:1639057 "The sipS (signal peptidase of subtilis) gene, which encodes an SPase of Bacillus subtilis, was cloned in Escherichia coli and was also found to be active in E.coli"].
- Overproduction increases precursor processing in vivo
  [PMID:1639057 "Its overproduction in B.subtilis resulted in increased rates of processing of a hybrid beta-lactamase precursor"].
- N-terminal single TM anchor (19-39), catalytic domain outside the membrane (UniProt FT).

## Catalytic mechanism

- Ser43 and Lys83 form the proposed catalytic dyad; Asp153 also critical
  [PMID:7876097 "three other residues (serine 43, lysine 83, and aspartic acid 153) were critical for activity"];
  [PMID:7876097 "A model envisaging a catalytic serine-lysine dyad in prokaryotic type I signal peptidases is proposed to accommodate our observations"].
  This places SipS among serine-type (S26, LexA-like) peptidases.
- Purified SipS cleaves pro-OmpA nuclease A in vitro
  [PMID:10982814 "In this work we have, for the first time, successfully isolated Bacillus subtilis type I signal peptidase (SipS)"];
  [PMID:10982814 "certain mutants in the c-region of the signal peptide result in alternate site cleavage by both Lep and SipS enzymes"].

## Physiological role and paralogs

- B. subtilis has five chromosomal type I SPases (SipS, SipT, SipU, SipV, SipW)
  [PMID:9694797 "consisting of five chromosomal genes, denoted sipS, sipT, sipU, sipV, and sipW"].
- SipS alone is not essential, but it is needed for efficient secretion of several proteins
  [PMID:8951809 "in the absence of SipS the rate of processing of several preproteins was reduced, and four of the seven major secreted proteins of B. subtilis were hardly detectable in the growth medium"].
- SipS and SipT are the major SPases; the double mutant is not viable
  [PMID:9694797 "only cells lacking both SipS and SipT were not viable, which may be caused by jamming of the secretion machinery with secretory preproteins"].
- sipS transcription is DegS-DegU controlled, coinciding with secretory-enzyme expression
  [PMID:8951809 "the growth phase-dependent transcription of sipS is controlled by the DegS-DegU two-component regulatory system"].

## Curation decisions (summary)

- GO:0009003 signal peptidase activity: ACCEPT (core MF).
- GO:0004252 serine-type endopeptidase activity: KEEP_AS_NON_CORE, as for E. coli LepB. It is
  an accurate catalytic-class term (Ser-Lys dyad), but it is not an ancestor of GO:0009003
  (signal peptidase activity is_a endopeptidase activity only), so it cannot be refined to the
  core term; it records mechanism rather than the substrate-defined core activity.
- GO:0008236 serine-type peptidase activity: MODIFY to GO:0004252 (true descendant).
- GO:0008233 peptidase activity: MODIFY to GO:0009003 (true descendant).
- GO:0006508 proteolysis and GO:0051604 protein maturation: MODIFY to GO:0016485 protein
  processing (true descendant of both). GO:0006465 signal peptide processing is obsolete in
  current GO (OLS, checked 2026-11-13: obsoleted because it represented the molecular function
  GO:0009003), so it is not used.
- GO:0016020 membrane: MODIFY to GO:0005886 plasma membrane.
- GO:0005886 plasma membrane (IEA): ACCEPT.
