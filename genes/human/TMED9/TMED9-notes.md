# TMED9 notes

Deep research (`just deep-research-falcon human TMED9 --fallback perplexity-lite`) failed in this
environment (no provider API keys); research done directly from cached publications and UniProt.

## Identity and topology
- p24alpha2 / p25 / GP25L2; EMP24/GP25L family; type I TM protein with lumenal GOLD domain and a
  cytoplasmic KKXX dilysine COPI-binding signal (UniProt Q9BVK6).
- Cycles in the early secretory pathway [PMID:12237308 "The p24 proteins belong to a highly conserved
  family of membrane proteins that cycle in the early secretory pathway."]

## Function
- Knockdown fragments Golgi, reduces ERGIC clusters, displaces COPI [PMID:18287528 "Silencing of
  Surf4/ERGIC-53 or p25 resulted in partial redistribution of coat protein (COP) I but not Golgi matrix
  proteins to the cytosol"].
- Cargo receptor: ER retention of PTPN2 TC48 [PMID:16595549 "Coexpression with p25 enhanced ER
  localization of TC48"]; traps misfolded MUC1-fs [PMID:31348885 "MUC1-fs is trapped in TMED9 cargo
  receptor-containing vesicles of the early secretory pathway"].

## Localization conclusion (surface benchmark)
- Intracellular: ER membrane, ERGIC membrane, cis-Golgi membrane, COPI vesicles. Not a plasma membrane
  protein; a surface pool appears only when the dilysine signal is mutated [PMID:18287528 "although it
  mislocalizes p24 family members to the cell surface"]. Exosome (HDA) and synaptic vesicle (IEA)
  calls marked as over-annotations.
