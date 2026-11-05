# gbdR (PA5380, Q9HTI4) review notes

AraC-family transcriptional activator, 367 aa: N-terminal DJ-1/PfpI-like
(class I glutamine amidotransferase-like) effector domain and C-terminal
AraC-type HTH domain (residues 227-325). PANTHER PTHR43130 (AraC-family
regulator). Reviewed UniProt entry. 44% identical to CdhR (PA5389).

## Literature (no deep-research provider available; own reading)

- Wargo et al. 2008 (abstract only). Transposon screen for growth on glycine
  betaine (GB); gbdR identified as a predicted AraC regulator required for
  growth on GB and DMG and for induction of the GB/DMG catabolic genes
  [PMID:17951379 "Our screen also identified a predicted AraC"; "that is
  required for growth on GB and DMG and for the induction of gbcA, gbcB, and
  dgcAB in response"]. The catabolic steps are performed by GbcAB (GB to DMG)
  and DgcAB (DMG to sarcosine), not by GbdR.
- Wargo et al. 2009 (full text read). GbdR is required for GB/DMG induction of
  plcH and pchP transcription; MBP-GbdR binds the plcH and pchP promoters in
  EMSA, and a 2-bp promoter mutation abolishes binding and induction
  [PMID:19103776 "Here we report that the induction of plcH and pchP
  transcription by glycine betaine is mediated by GbdR, an AraC family
  transcription factor."; "In electrophoretic mobility shift assays, a
  GbdR-maltose binding protein fusion bound specifically to both the plcH and
  pchP promoters."]. Effects on PlcH and PchP enzyme activity are downstream of
  transcriptional induction; GbdR does not act on the enzymes.
- Hampel et al. 2014 (full text read). GbdR regulon: 26 genes from 12
  promoters, 11 bound in vitro; DNase I footprint on plcH; consensus site;
  choE added [PMID:24097953 "Here we show that GbdR activation regulates
  transcription of 26 genes from 12 promoters, 11 of which have measureable
  binding to GbdR in vitro ."]. Direct control of all steps from GB to
  pyruvate [PMID:24097953 "as it directly regulates transcription of the genes
  involved in all steps of conversion from GB to pyruvate"].

## PseudoCAP IBA-seed assessment

Other seeds' experimental support queried live in QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000111456 | GO:0006355 regulation of DNA-templated transcription | 4 | 50 (13 taxa) | GO:0006355, IDA, PMID:17951379 (PseudoCAP) | SOUND | Abstract states GbdR is required for induction of the GB/DMG catabolic genes; later papers show direct promoter binding. Term correct (the IDA code is generous for a genetics abstract, but the claim is true). | P. aeruginosa ArgR G3XCU2 (CollecTF EXP/IMP/IPI), S. coelicolor AdpA Q9L062 (CollecTF EXP), P. aeruginosa CdhR Q9HTH5 (PseudoCAP IMP) | Yes; ArgR and AdpA have experimental support |
| PTN000111456 | GO:0006355 regulation of DNA-templated transcription | 4 | 50 (13 taxa) | GO:0006355, IMP, PMID:24097953 (PseudoCAP) | SOUND | Full text: regulon defined, direct EMSA binding to 11 promoters, footprint. | as above | Yes |

The node term is the generic AraC-regulator process and suits a 13-taxon
clade of AraC activators. No PSEUDOCAP defect on the seed rows and no
GO_CENTRAL defect on PTN000111456. CdhR (Q9HTH5) shares this node and is being
reviewed in parallel; no node-level defect needs recording there.

### Other PseudoCAP rows (not seeds)

| term | verdict | defect |
|---|---|---|
| GO:0031457 glycine betaine catabolic process (IMP, PMID:17951379) | WRONG (regulator annotated to the process its targets perform) | PSEUDOCAP WRONG_TERM, CONFIRMED (abstract says gbdR encodes a regulator required for induction; PMID:24097953 full text shows direct transcriptional control). Repoint to GO:0009896. |
| GO:0010518 positive regulation of phospholipase activity (IMP, PMID:19103776) | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED (full text): GbdR induces plcH transcription; it does not modulate PlcH activity. |
| GO:0010922 positive regulation of phosphatase activity (IMP, PMID:19103776) | WRONG | PSEUDOCAP WRONG_TERM, CONFIRMED (full text): GbdR induces pchP transcription. |
| GO:0009896 positive regulation of catabolic process | SOUND | none; no GB-specific regulation term exists. |
| GO:0045764 positive regulation of amino acid metabolic process | SOUND, non-core | none (DMG, sarcosine, glycine, serine catabolic genes are direct targets). |
