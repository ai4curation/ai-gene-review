# cueR (PA4778, Q9HV30) review notes

No deep-research provider was available; notes below come from the UniProt
record, the cached publication and PubMed (full text of PMID:20233934 was not
returned by the PubMed MCP, so abstract only).

## Function

- MerR-family Cu(+)-sensing regulator; LasR activates cueR, and CueR directly binds
  and activates five promoters [PMID:20233934 "show that the protein directly binds
  to and activates five promoters controlling the expression of 11 genes"].
- Disruption increases copper sensitivity [PMID:20233934 "Using gene disruptions, we
  show that PA4778, along with 7 of 11 gene targets of PA4778, increases the
  sensitivity of P. aeruginosa to elevated copper concentrations"].
- UniProt (curated, PubMed:31790504): also represses H2-T6SS, azu and oprC under
  copper-rich conditions; metallated by CopZ1/CopZ2 (PubMed:30718281).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001575588 | GO:0006355 regulation of DNA-templated transcription | 9 | 114 (31 taxa) | GO:0045893 positive regulation of DNA-templated transcription, IMP, PMID:20233934 (PseudoCAP) | SOUND | The abstract states direct promoter binding and activation by PA4778 itself, plus disruption phenotypes; the row is about CueR's own regulatory activity, not a downstream phenotype. The node term is the generic MerR-family process, right for a clade of activators and repressors. | E. coli CueR P0A9G4, ZntR P0ACS5, BluR P75989; Xanthomonas SoxR Q8P6Y4; M. tuberculosis HspR O06302; B. subtilis TnrA Q45666; S. coelicolor HspR P40183; PAO1 BrlR Q9HUT5 | Yes; E. coli CueR and ZntR alone carry strong experimental support. No GO_CENTRAL defect. Shared with brlR (see brlR notes; same verdict, no defect). |
| PTN001249777 | GO:0045893 positive regulation of DNA-templated transcription | 3 | 26 (13 taxa) | same row | SOUND | As above. The CueR/ZntR metal-sensor clade are classical MerR activators, so the positive-regulation node term suits the clade. | E. coli CueR P0A9G4, ZntR P0ACS5 | Yes. No GO_CENTRAL defect. |

PseudoCAP defects from this gene: none.
