# LEU4 notes (YNL104C, P06208)

- Major alpha-isopropylmalate synthase, EC 2.3.3.13 [UniProt:P06208]; first committed step of the Leu branch.
- Two forms by alternative initiation [PMID:3275644 "indicate that two forms of hybrid protein are produced and that only the larger form is targeted to the mitochondria"]; short form functional and cytosolic [PMID:3275644 "the short form is functional in leucine biosynthesis, is inhibited by leucine with an apparent inhibitor constant of approximately 0.4 mM, and exists as a cytoplasmic dimer"].
- Paralog specialisation [PMID:25841022 "Here, we show that the Leu4 homodimer is a leucine-sensitive isoform, while the Leu9 homodimer is resistant to such feedback inhibition."]; heterodimers [PMID:25841022 "Bimolecular fluorescent complementation analysis showed that Leu4-Leu9 heterodimeric isozymes are formed in vivo."]
- Compartment logic [PMID:25841022 "α-IPM is then transported from the mitochondria to the cytosol by the yeast oxaloacetate/sulfate carrier Oac1"].
- Redundancy [PMID:10790691 "A mutant in which both ORF YOR108w and LEU4 gene have been deleted proved to be leucine auxotrophic and alpha-isopropylmalate synthase (alpha-IPMS)-negative."]

## Curation observations
- YeastPathways RCA places the IPMS step in cytosol; true only for the minor short form. Kept non-core.
- Protein binding rows (Leu4-Leu9) -> MODIFY to GO:0046982 protein heterodimerization activity.
- Zinc ion binding (RCA, zinc proteome) kept non-core; physiological metal not established.
