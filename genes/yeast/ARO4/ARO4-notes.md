# ARO4 (YBR249C, P32449) notes

Pathway context: DAHP synthase, step 1 of shikimate pathway (EC 2.5.1.54); Tyr-inhibited isozyme.

- Cloning, 76% similarity to Aro3, GCN4 control [PMID:1348717 "Here, we report the cloning and characterization of the ARO4 gene, encoding the second DAHPS, which is inhibited by tyrosine."].
- Redundant with ARO3 [PMID:1348717 "Mutations in both genes are necessary to cause aromatic amino acid (aa) auxotrophy"].
- Gly226 sets tyrosine regulation [PMID:12540830 "In the cavity of Aro4p at position 226 is a glycine residue, which is highly conserved in all other tyrosine-regulated DAHP synthases as well."].
- GO:0043085 positive regulation of catalytic activity (IMP, PMID:12540830, assigned by DisProt). Full text read on 2026-11-11 at PMC298692 (not cached locally). The relevant result is an N-terminal deletion of Aro4p itself [PMC298692 "Stable deletion of the N-terminal 20 amino acids resulted in an unregulated DAHP synthase with lowered activity in comparison to WT (11%)."]. Exchanging the internal extension gave a similar phenotype [PMC298692 "An exchange of the internal part of Aro4p (Tyr) including the two internal β sheets by the corresponding part of Aro3p (Phe) resulted in an unregulated low enzyme activity"]. So DisProt recorded a region of Aro4p (its N-terminal segment) that is needed for the full catalytic activity of the same polypeptide. It is an intramolecular structural requirement, not Aro4p regulating a catalytic activity as a biological process, and the paper reports no activation of any other enzyme. Verdict: MARK_AS_OVER_ANNOTATED (observation real, process term overstates it).
- Nucleus HDA (Huh; Tkach replication-stress screen) kept non-core.
