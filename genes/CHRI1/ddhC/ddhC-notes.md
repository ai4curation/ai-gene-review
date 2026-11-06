# ddhC (Q1QYW1, Csal_0990) curation notes

## 2026-11-04 review session

No provider deep research was generated in this session (no API keys), so the
review rests on the cached publications and the reviewed UniProt record.
Literature checked: PMID:32631860 (cached abstract only; PMC7440794 full text
could not be retrieved through Europe PMC or NCBI efetch, which returned only the
abstract) and PMID:22675587 (genome paper, full text cached).

- Recombinant DdhC is an active monomer with noncovalent FAD that uses both DMG
  and sarcosine and NAD+ or NADP+ [PMID:32631860, "The enzyme, existing as a
  monomer of 79 kDa with a noncovalently bound flavin adenine dinucleotide,
  utilized both DMG and sarcosine as substrates and exhibited dual coenzyme
  specificity, preferring NAD+ to NADP+"].
- Acceptor question. The abstract does not name ETF or ferredoxin as the DdhC
  acceptor. It says only "intermolecular electron transfer between DMGDH and
  other electron acceptors" [PMID:32631860]. UniProt (from the full text)
  treats NAD(P)+ as an enzyme-bound cofactor reoxidized by the [4Fe-4S]
  ferredoxin Csal_0991, and curates RHEA:74167 and RHEA:74155 (EC 1.5.7.3,
  ferredoxin acceptor) for DMG and sarcosine. ETF is downstream of Csal_0991,
  not a direct DdhC acceptor. The ExPASy ENZYME entry for EC 1.5.7.3, checked
  on 2026-11-04, is named "N,N-dimethylglycine/sarcosine dehydrogenase
  (ferredoxin)". It describes the native acceptor as a membrane-bound
  clostridial-type ferredoxin that passes electrons to ETF.
- GO has no EC 1.5.7.3 term. GO:0047865 (EC 1.5.8.4) and GO:0008480
  (EC 1.5.8.3) are ETF-acceptor terms, so neither is used. The existing parent
  GO:0033694 (CH-NH donors, iron-sulfur protein as acceptor) is the MODIFY
  target, and an NTR "N,N-dimethylglycine/sarcosine dehydrogenase (ferredoxin)
  activity" is proposed under it. The same NTR is used in the dgcA review.
- DdhC also acts on sarcosine in vitro, with similar kcat (UniProt). The
  disruption mutant still grows on sarcosine, so the in vivo role is the DMG
  step. The sarcosine activity is included in the NTR because EC 1.5.7.3
  covers both reactions; no separate sarcosine annotation is made.
- FMN binding (InterPro2GO from the OYE TIM barrel) is MARK_AS_OVER_ANNOTATED.
  Only FAD was found, and the curated cofactors are FAD and NAD(P)+.
- Possible UniProt citation error: the FUNCTION sentence on lack of activity
  toward TMA, histamine, GB and choline cites PubMed:22675587, the genome
  paper, which has no assays. This is recorded as a source defect
  (PROBABLE, repoint to PMID:32631860).
