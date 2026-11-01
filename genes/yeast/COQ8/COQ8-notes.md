# COQ8 (ABC1/YGL119W, UniProt P27697) – review notes

## Role in CoQ biosynthesis
- COQ8 = ABC1; null mutants lack Q and accumulate HHB [PMID:11279158 "abc1/coq8 null mutants are defective in Q biosynthesis and accumulate 3-hexaprenyl-4-hydroxybenzoic acid as the predominant intermediate"]; mitochondrial, processed on import [PMID:11279158 "Abc1/Coq8p localizes to the mitochondria, and is proteolytically processed upon import"].
- Peripheral protein on the matrix side of the inner membrane [PMID:21296186 "The results show that Coq8p is a peripherally associated membrane protein located on the matrix side of the inner membrane"]; [PMID:18801050 "Localization studies identify Coq8p as a soluble mitochondrial protein, with characteristics of a protein of the matrix or associated with the inner mitochondrial membrane"].
- Overexpression stabilizes the CoQ synthome in coq null mutants (PMID:24406904, PMID:22593570).
- Coq3/Coq5/Coq7 phosphorylation depends on Coq8 [PMID:21296186 "Coq3p, Coq5p, and Coq7p were phosphorylated in a Coq8p-dependent manner"] – historically interpreted as Coq8 being a protein kinase.

## Biochemistry (supersedes the protein-kinase model)
- [PMID:27499294 "Although COQ8 was predicted to be a protein kinase, we demonstrate that it lacks canonical protein kinase activity in trans"].
- [PMID:27499294 "Instead, COQ8 has ATPase activity and interacts with lipid CoQ intermediates"].
- Purified Coq8 (NΔ41) autophosphorylates only in cis; autophosphorylation sites are dispensable in vivo [PMID:27499294 "mutating Coq8NΔ41 autophosphorylation sites did not inhibit respiratory yeast growth"].
- ADP-selective nucleotide pocket; A-rich loop A-to-G mutation enables autophosphorylation but impairs CoQ biosynthesis (ADCK3 paper PMID:25498144, with in vivo Coq8p structure-function tests).

## GO implications
- protein kinase activity (IMP, PMID:22593570) is contradicted by direct in vitro assays (PMID:27499294) and by UniProt's NOT annotation -> REMOVE.
- Core MF: ATP hydrolysis activity (GO:0016887) + lipid binding (GO:0008289), acting on the matrix face of the inner membrane in CoQ biosynthesis. The module deliberately asserts no MF for Coq8; this review accepts ATPase and lipid binding as the experimentally demonstrated activities, while how they drive CoQ synthesis remains unresolved.
- COQ8 is absent from YeastCyc pathways (no reactions in the summary file).
- PomBase GO-CAM 662af8fa00000408 types S. pombe coq8 with GO:0004672 protein kinase activity (positively regulating coq3) – disagrees with PMID:27499294.
