# pyk3 (Q54I36, DDB_G0283699; DPYK3 / PkyA) notes

## Deep research status
- 2026-10-05: `just deep-research-falcon DICDI pyk3 --fallback perplexity-lite` FAILED.
  Falcon (Edison) returned `402 Payment Required`; fallback `perplexity-lite` not
  available (`Provider 'perplexity' not available`). No deep-research file was produced;
  review based on the four cached primary papers (two with full text) and UniProt.

## Sequence / domain architecture (UniProt Q54I36)
- 1338 aa; long disordered N-terminal region; two kinase-like domains:
  "Protein kinase 1" 693-1014 (pseudokinase, KII in Araki 2014) and "Protein kinase 2"
  1057-1309 (the catalytic TKL domain, KI). Pfam PF07714 x2; PANTHER PTHR44329 (TNNI3K-related / MLKL-like TKL).
- UniProt names it "dual specificity" with EC 2.7.12.1 but there is no experimental Ser/Thr evidence.

## Literature
- Adler et al. 1996 [PMID:8898113, abstract only]: DPYK3 cloned by phosphotyrosine-antibody
  expression screen; "C-terminal fragments ... shown to be autocatalytically phosphorylated
  at tyrosine residues"; tandem kinase-related domains.
- Lee et al. 2008 [PMID:18657170, abstract only]: dpyk3- (Ax4/Ax3 background) shows aberrant
  pattern formation (pstO zone not formed, prespore zone expanded), persistent STATc
  phosphorylation after DIF-1 -> "DPYK3 negatively regulates STATc during development in
  response to DIF-1 signaling". UniProt FUNCTION is based on this.
- Vu et al. 2014 [PMID:24587195, full text]: pyk3-, phg2- and double nulls (Ax2): reduced
  sorbitol/8-Br-cGMP/BHQ-induced transcription of STATc targets, reduced phospho-STATc
  (Tyr922), delayed GFP-STATc nuclear translocation; Pyk3 is not the PTP3 S448/S747 kinase
  ["These results exclude Pyk3 as a specific inhibitor of PTP3"]. No Pyk3 kinase assay in
  this paper (the IDA PTK annotation from it is weakly grounded; activity itself is well
  established elsewhere).
- Araki et al. 2014 [PMID:25143406, full text, MBoC]: key paper. Pyk2 and Pyk3 are
  redundant stress-activated STATc tyrosine kinases ("single null mutants are only marginally
  impaired, but the double mutant is nonactivatable"). Recombinant Pyk3 autophosphorylates
  on tyrosine; K1084A (TKL domain ATP-site) abolishes it ["Tyrosine phosphorylation of Pyk3
  was ablated when K1084 ..."]. GST-Pyk3-KI alone phosphorylates His-STATc on Y922; KII
  pseudokinase inhibits KI (JAK JH2-like). Myc-Pyk3 IP kinase assays: sorbitol/8Br-cGMP
  induce STATc kinase activity. pTyr-dependent binding of STATc SH2 domain to Pyk3 (R831A
  in STATc SH2 abolishes; Y922F has no effect). Pyk3 negligible activity on MBP (argues
  against broad Ser/Thr activity). Localization: cytosol at rest, moves to cortex with F-actin
  after sorbitol. Could not reproduce Lee 2008 DIF-1 phenotype in Ax2 (strain dependent).
  Double pyk2-/pyk3- development is highly stress sensitive.

## Synthesis
- Core MF: protein tyrosine kinase activity (STATc Tyr922 kinase; autophosphorylation).
- Core BP: positive regulation of / participation in the hyperosmotic-stress STATc pathway
  (Pyk3 is a JAK-analogous STAT-activating kinase).
- Location: cytosol, cell cortex (stress-induced).
- Pseudokinase domain: autoinhibitory (JH2-like).
- Ser kinase / dual specificity: unsupported (EC/Rhea mapping only).
