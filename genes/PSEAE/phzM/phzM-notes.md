# phzM (PA4209, Q9HWH2) notes

## Identity

- Phenazine-1-carboxylate N-methyltransferase, EC 2.1.1.327, 334 aa. Class I
  SAM-dependent methyltransferase of the cation-independent
  O-methyltransferase (COMT-like, Pfam Methyltransf_2 + Dimerisation) family;
  PANTHER PTHR43712:SF2. PE 1; crystal structure 2IP2 (1.8 A, unliganded).
- UniProt: [file:PSEAE/phzM/phzM-uniprot.txt "Converts phenazine-1-carboxylate (PCA) to 5-methylphenazine-1-carboxylate (5- methyl-PCA)."] (ECO:0000269 PMID:17253782); "In vitro, requires PhzS for activity."

## Biochemistry (PMID:17253782, full text cached)

- [PMID:17253782 "Incubations of PhzM with its presumed substrates, PCA, and SAM, yielded no detectable product and substrate concentrations were unchanged after extended incubations."]
- [PMID:17253782 "Pyocyanin formation required PhzM, PhzS, PCA, SAM, oxygen, and NADH consistent with a methyl transfer reaction and a flavin-mediated hydroxylation."]
- [PMID:17253782 "PhzM possesses the highly conserved DVGGGXG motif (residues 173–179) that defines the SAM binding site of methyltransferase enzymes suggesting that PhzM does indeed function as a methyltransferase."]
- [PMID:17253782 "The structure of PhzM contains no ligands and the active site is open and solvent exposed when compared to structures of similar enzymes."] So SAM binding is not seen directly; it is implied by the SAM requirement and the motif.
- [PMID:17253782 "Laser light scattering confirms that PhzM is a dimer in solution as well with a molecular mass of 73550 ± 490 for PhzM"]
- Methylation is at N5 of PCA, unlike the O-methylation done by its plant homologues (IOMT): [PMID:17253782 "PCA is methylated at N5 in the center of the molecule"].
- Transient PhzM-PhzS interaction inferred from dialysis and filtration experiments; no stable complex seen.
- Genetics: [PMID:11591691 "P. aeruginosa with insertionally inactivated phzM or phzS developed pyocyanin-deficient phenotypes."] (abstract only)
- Crystallization: [PMID:16946471 "PhzM, a dimeric S-adenosylmethionine-dependent methyltransferase, was purified and crystallized"] (abstract only).
- Regulation (not annotated here): Crc binds phzM mRNA (PMID:22562990); temperature-dependent phzM expression in strain M18 (PMID:19717631).

## Decisions

- GO:0008757 IDA (PseudoCAP, PMID:17253782) and IBA: ACCEPT, core. GO:0102168 (the specific reaction) is is_a GO:0008168 only in current GO, not GO:0008757 or GO:0008170, so GO:0008757 is not entailed by the specific term; ontology gap raised as a question.
- GO:0102168 IDA and IEA: ACCEPT, core.
- GO:0106220 pyocyanine biosynthetic process IDA: ACCEPT.
- GO:0008168 methyltransferase activity IEA: MODIFY to GO:0102168.
- GO:0008171 O-methyltransferase activity IEA (InterPro COMT_C): REMOVE; PhzM is an N-methyltransferase, so the family-level InterPro2GO mapping is wrong for this member.
- GO:0046983 protein dimerization activity IEA and GO:0042802 identical protein binding IDA (x2): MODIFY to GO:0042803.
- GO:0042803 protein homodimerization activity IDA (x2): KEEP_AS_NON_CORE.
- GO:1904047 S-adenosyl-L-methionine binding IDA: KEEP_AS_NON_CORE (true, but structural evidence is an unliganded structure; support is the SAM requirement and the motif).
- GO:0005515 protein binding IPI (PhzS): REMOVE per policy.

## PseudoCAP IBA-seed assessment

Tree analysis: `phzM-bioinformatics/RESULTS.md`.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002463933 | GO:0008757 S-adenosylmethionine-dependent methyltransferase activity | 1 (sole seed) | 80 (16 taxa); 64 GOA rows | GO:0008757 SAM-dependent methyltransferase activity, IDA, PMID:17253782 (PseudoCAP) | SOUND | Purified PhzM with PhzS converts PCA to pyocyanin only when SAM is present, and PhzM has the DVGGGXG SAM motif and a class I methyltransferase fold; the methyl transfer is PhzM's step, so the IDA is direct enough (PhzM alone is inactive, which is an activation requirement, not a missing activity). The node is the LUCA root of PTHR43712, mostly fungal and animal O-methyltransferases plus bacterial PhzM-like proteins; GO:0008757 is the right level because the clade mixes O- and N-methylation, so O-methyltransferase activity or the PhzM reaction would each be wrong for part of it. Flag: two fungal cluster coactivators (tpcD Q4WQZ4, mdpA C8VQ72) inherit the IBA; their catalytic status is unchecked. |

## Open questions

- How does PhzS activate PhzM? Is the 5-methyl-PCA intermediate channelled?
- Should GO:0102168 be placed under GO:0008757 and GO:0008170 N-methyltransferase activity?
- Are tpcD and mdpA catalytically dead PTHR43712 members (candidates for NOT annotations at their leaves)?
