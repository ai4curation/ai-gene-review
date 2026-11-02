# PSD1 (YNL169C, P39006) notes

## Identity
- Mitochondrial phosphatidylserine decarboxylase proenzyme, EC 4.1.1.65; type I PSD; autocatalytic LGST cleavage into beta/alpha (pyruvoyl) chains [UniProt:P39006].

## Evidence
- Cloning, null allele, second PSD inferred [PMID:8407984 "Analysis of lipid synthesis and enzyme activity in null mutants indicates that there are two PSD genes."]
- PS decarboxylated in IM by Psd1; majority of PE [PMID:23124206 "In yeast, the majority of PE is produced from phosphatidylserine (PS) by a mitochondrion-located PS decarboxylase, Psd1p."]
- Topology: beta in IM, alpha in IMS [PMID:22984266 "we report that in yeast the Psd1 β-subunit (Psd1β) is integrated into the mitochondrial inner membrane and serves as an anchor for the intermembrane space-localized α-subunit (Psd1α)"].
- Autocatalysis needs only the Ser [PMID:25829489 "only the serine residue is absolutely required for Psd1p autocatalysis and function"].
- Dual ER targeting [PMID:29290583 "our analysis indicates that the TMR of Psd1 is both necessary and sufficient for dual targeting of Psd1 to mitochondria and ER membranes"]; ER-Psd1 at LD biogenesis sites [PMID:34818062 "Here, we show that Psd1 can target on the ER membrane to a subset of LDs, particularly under conditions that promote LD biogenesis."]
- Downstream PE-dependent phenotypes: complex III [PMID:30926815 "Our work supports a specific role of IM-synthesized PE in complex III activity"], fusion and s-Mgm1 [PMID:23045528 "The loss of Psd1 also impairs the biogenesis of s-Mgm1, a protein essential for mitochondrial fusion"].

## Curation decisions
- Core: GO:0004609 + PE biosynthesis at IM; second core for ER pool.
- Autoprocessing accepted (self-cleavage). Complex III electron transport and regulation of protein processing marked over-annotated (indirect, via PE). Mitochondrial fusion and LD formation kept non-core. Cytosol RCA removed.
