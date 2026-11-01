# murQ (yfeU, b2428, P76535) notes

## 2026-10-31 — initial review

No deep-research file. Sources: UniProt P76535, PMID:15983044, PMID:16452451,
PMID:18837509, PMID:15901686 (abstracts only in cache), PMID:18723630 (full text).

### Activity
- MurNAc 6-phosphate etherase (EC 4.2.1.126; RHEA:26410): MurNAc-6P + H2O ->
  GlcNAc-6P + D-lactate [PMID:15983044 "Purified MurQ-His6 fusion protein and extracts of cells expressing murQ both catalyze the cleavage of MurNAc 6-phosphate, with GlcNAc 6-phosphate and D-lactate being the primary products."].
- Mechanism: syn elimination of lactate to an alpha,beta-unsaturated aldehyde, then syn
  addition of water; C3-O bond cleaved; Glu83 (proton donor) and Glu114 essential
  [PMID:18837509 "Putative active site acid/base residues are probed by mutagenesis, and Glu83 and Glu114 are found to be crucial for catalysis."].
  KM 1.2 mM, kcat 5.7 s-1; homodimer (UniProt, from PMID:18837509).
- Net reaction is hydrolysis of an ether bond; mechanism and EC class are lyase. Both
  existing MF terms (GO:0016803 ether hydrolase, GO:0016835 carbon-oxygen lyase) are
  true but general. GO has no term for EC 4.2.1.126 (checked go.db for EC/RHEA xrefs and
  label "etherase"): NTR proposed.
- SIS domain (55-218); GCKR-like family, MurNAc-6-P etherase subfamily; homolog of the
  N-terminal domain of human glucokinase regulatory protein.

### Pathways
- Required for growth on MurNAc as sole carbon source; ΔmurQ accumulates MurNAc-6P
  [PMID:15983044 "A murQ deletion mutant could not grow on MurNAc as the sole source of carbon and energy but could be complemented by expressing murQ from a plasmid."].
- Only MurNAc-P etherase in E. coli; with AnmK required for anhMurNAc from the medium or
  own murein [PMID:16452451 "MurQ is the only MurNAc-P etherase in Escherichia coli"].
- AnmK phosphorylates anhMurNAc to MurNAc-P, then the etherase gives GlcNAc-P
  [PMID:15901686]. GlcNAc-6P enters the nag pathway (NagA, NagB) to fructose-6P or is
  reused for UDP-GlcNAc synthesis.
- Low constitutive murQ expression suffices for recycling; high-level expression (after
  MurR release by MurNAc-6P, plus cAMP-CAP) needed for growth on MurNAc [PMID:18723630].

### GO term notes
- GO:0097173 (MurNAc catabolic) and GO:0097175 (anhMurNAc catabolic) are not under
  amino sugar catabolic process (GO:0046348) in GO; they sit under carboxylic acid
  catabolic process. So the amino sugar rows are MODIFIED to these terms rather than
  TOO_GENERAL.
- No "peptidoglycan recycling" term; GO:0009254 peptidoglycan turnover is the
  existing term.
- IPI protein binding (PMID:18837509, EcoliWiki): almost certainly the homodimer;
  UniProt SUBUNIT "Homodimer" is attributed to this paper. MODIFY to GO:0042803.
