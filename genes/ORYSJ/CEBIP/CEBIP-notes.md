# CEBIP (rice, Q8H8C7) curation notes

## 2026-10-02 — initial review

Sources: UniProt record, falcon deep research (`CEBIP-deep-research-falcon.md`), cached publications.
Only PMID:21070404 has full text cached; the others are abstract-only.

### Identity and architecture
- 356-aa precursor with a 28-aa signal peptide; mature protein is heavily N-glycosylated [PMID:16829581 "CEBiP is actually a glycoprotein consisting of 328 amino acid residues and glycan chains"].
- C-terminal hydrophobic segment [PMID:16829581 "CEBiP was predicted to have a short membrane spanning domain at the C terminus"]. UniProt annotates a single-pass TM helix (336-356); GPI anchoring is proposed for LysM-RLPs in other species but has not been shown for rice CEBiP (deep research flags this too).
- Crystal structure: [PMID:27238968 "The structures reveal that OsCEBiP-ECD contains three tandem LysMs followed by a novel structure fold of cysteine-rich domain."]

### Molecular function: chitin binding / PRR
- Purified from plasma membrane by affinity [PMID:16829581 "a high-affinity binding protein for this elicitor was isolated from the plasma membrane of suspension-cultured rice cells"].
- Specificity [PMID:24395781 "Epitope mapping by NMR spectroscopy indicated the preferential binding of longer-chain chitin oligosaccharides, such as heptamer-octamer, to CEBiP, and also the importance of N-acetyl groups for the binding."]
- Sandwich dimer [PMID:24395781 "two CEBiP molecules simultaneously bind to one chitin oligosaccharide from the opposite side, resulting in the dimerization of CEBiP."]
- Major binding site in vivo [PMID:24173912 "CEBiP is the major CE-binding protein in rice cultured cells and leaves"].

### Receptor complex with OsCERK1
- [PMID:21070404 "However, it does appear that CEBiP plays a major role in chitin elicitor binding and that OsCERK1 functions as a signal transducer through its Ser/Thr kinase activity in rice."]
- Pre-formed CEBiP homo-oligomers; chitin-induced hetero-complex [PMID:21070404 "Once the system is activated by chitin oligosaccharides, a receptor complex including both CEBiP and OsCERK1 is transiently formed"].
- Downstream: OsCERK1 phosphorylates OsRacGEF1 [PMID:23601108 "OsRacGEF1 interacts with OsCERK1 and is activated when its C-terminal S549 is phosphorylated by the cytoplasmic domain of OsCERK1 in response to chitin."] -> kinase steps belong to OsCERK1, not CEBiP.

### Biological role
- RNAi: [PMID:16829581 "CEBiP plays a key role in the perception and transduction of chitin oligosaccharide elicitor in the rice cells"].
- Knockout: chitin-specific [PMID:24173912 "The response to peptidoglycan and lipopolysaccharides in cebip cells was not affected"]; resistance phenotype only with weakly virulent blast strain.
- Slp1: [PMID:22267486 "Slp1 competes with CEBiP for binding of chitin oligosaccharides"]; CEBiP silencing lets M. oryzae cause disease without Slp1.
- Arabidopsis orthologue LYM2/AtCEBiP binds chitin but does not signal [PMID:22891159 "AtCEBiP is biochemically functional as a chitin-binding protein but does not contribute to signaling"] -> do not transfer receptor/process terms between rice and Arabidopsis by orthology.
- Symbiosis: per deep research (Zhang et al. 2021 PNAS, not cached), CEBiP competes with OsMYR1 for OsCERK1; cebip mutants show increased early AM colonization. Indirect; not annotated.

### Decisions
- protein binding (IPI, OsCERK1) -> MODIFY to GO:0038187 pattern recognition receptor activity.
- plasma membrane (IEA) -> ACCEPT. chitin binding (IBA) -> ACCEPT.
- NEW: GO:0032491 detection of molecule of fungal origin; GO:0002752 cell surface PRR signaling pathway (CEBiP performs the ligand-binding initiation step; comparators OsCERK1, AtCERK1, AtLYK5).
- Not added: defense response to fungus / innate immune response (outcome-level; necessity evidence, and blast phenotype is weak in knockout).
- UniProt cites PMID:24964058 for CEBiP-LYP4/LYP6 interaction, but the abstract reports OsCERK1-LYP4/LYP6; full text not available, left UNVERIFIED.
