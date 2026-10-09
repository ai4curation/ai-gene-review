# RfC4 (P53034) curation notes

- RfC4 (Rfc40, CG14999) is the fly ortholog of human RFC2, an AAA+ small subunit of replication factor C.
- RFC function (general): [PMID:8999859 "It is a molecular matchmaker required for loading of proliferating cell nuclear antigen (PCNA) onto double-stranded DNA"]; [PMID:8999859 "for PCNA-dependent DNA elongation by DNA polymerases delta and epsilon"].
- Fly mutants: [PMID:11438670 "These mutations produce larval phenotypes consistent with a role in DNA replication"]; localization [PMID:11438670 "Though the DmRFC4 protein localizes to all replicating nuclei"]; checkpoint [PMID:11438670 "the mitotic defects in these two DmRfc4 alleles are the result of aberrant checkpoint control in response to DNA replication inhibition or damage to chromosomes"]. Cohesion defects are indirect: [PMID:11438670 "Thus the mitotic defects appear not to be the result of a direct role for RFC4 in chromosome structure"].
- Elg1 complex membership: [PMID:27198229 "identified peptides from all components of the Elg1 PCNA-unloader complex: Elg1, Rfc4, Rfc38, CG8142, and Rfc3"].
- PMID:24204884 (Elongin/Corto, wing veins), cited by FlyBase NAS/IPI rows for all Elg1-complex subunits, does not mention RFC/Elg1/PCNA (full text searched); flagged MISCITED.
- Protein binding IPI rows (14605208, 20353594, 38944040) are all with other RFC small subunits; removed as uninformative (complex membership already captured).
- Module-wide convention (RfC4, RfC38, RfC3, CG8142): contributes_to GO:0003689 ACCEPT; GO:0005663 and GO:0031391 ACCEPT; GO:0006261/GO:0006271/GO:0006272 ACCEPT; generic DNA/ATP binding, ATPase, DNA replication parent, DNA repair, cohesion, checkpoint KEEP_AS_NON_CORE.
- Deep research: falcon run launched; see deep-research file if present.
