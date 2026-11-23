# PEA15 evidence notes

[PMID:23575685](https://pubmed.ncbi.nlm.nih.gov/23575685/), DOI [10.1038/ncomms2687](https://doi.org/10.1038/ncomms2687), solves PEA15 bound to ERK2: “occupying two key docking sites of ERK2”. This supports a direct kinase-regulatory role, not intrinsic kinase activity. [PMID:10442631](https://pubmed.ncbi.nlm.nih.gov/10442631/) reports “PED/PEA-15 co-precipitated with both FADD and FLICE.” and inhibition of death-receptor apoptotic signaling.

[PMID:9670003](https://pubmed.ncbi.nlm.nih.gov/9670003/), DOI [10.1093/emboj/17.14.3858](https://doi.org/10.1093/emboj/17.14.3858), is cached as abstract-only after publisher XML/HTML/PDF retrieval failed. It describes cloned human PEA15 transfection into L6 cells, with increased surface GLUT1 but inhibited insulin-stimulated glucose transport and GLUT4 surface recruitment. This establishes regulation of transport; it does not automatically establish the more general directed-movement process GO:0008643 or an intrinsic transporter activity. QuickGO definitions checked 2026-09-08 distinguish this from GO:0046325 negative regulation of glucose import.

Horse A0A9L0RWM8 contains all 130 human residues at 100% identity plus an N-terminal extension of 46 aa. The conserved core strongly supports mechanistic transfer, but the extension could affect localization or regulation and is not experimentally characterized. It is not evidence of a different enzyme or transporter fold. Horse UniProt is unreviewed; no horse-specific functional source was identified in the initial literature search, so human research is prioritized.

## Research synthesis

The human Falcon synthesis integrates direct ERK binding, phosphorylation-dependent signaling and the PLD1/PKC pathway underlying glucose-transport regulation. The primary PMID:9670003 establishes effects on glucose uptake, but the supported regulatory role should not be equated with an intrinsic glucose carrier. The 46-residue horse N-terminal extension preserves the complete human core while leaving possible effects on N-terminal trafficking regulation unresolved.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: benchmark accession Q15121 is the reviewed canonical human PEA15 (isoform 1, 130 aa, DED 3-81, ERK-binding C-terminal tail ~121-129). Not a fragment or alternative gene model. Isoform 2 (Q15121-2) carries a 21-aa N-terminal extension (VSP_056174) and is not the benchmark target. The previous version of this review contained text about the horse sequence A0A9L0RWM8 (46-aa N-terminal extension) pasted into human annotation reasons; that was removed, since the human canonical product is the subject here.

Evolutionary placement: PANTHER PTHR48169:SF1 (ASTROCYTIC PHOSPHOPROTEIN PEA-15), the PEA15 orthologue clade (human, mouse Q62048, rat, hamster, orangutan). Sister subfamilies are CFLAR (SF3) and caspase-8/10 (SF7). The family review interpro/panther/PTHR48169/PTHR48169-review.yaml places Q15121 in SF1, which agrees with UniProt. The IBA for GO:1902042 comes from PTN008298780 with human (IDA) and mouse (MGI:104799) donors. Only the anti-apoptotic process was propagated at that node; ERK-regulatory terms were not, and no IBA is relied on for them. ERK function is supported here by human experimental data alone.

Key evidence:
- ERK anchoring/regulation [PMID:23575685 "PEA-15 uses a bipartite binding mode, occupying two key docking sites of ERK2"; "PEA-15 binding protects ERK2 from dephosphorylation"; "results in the failure of the PEA-15 L123K mutant to prevent ERK nuclear translocation"]. Reactome R-HSA-5675206 describes PEA15 as a cytoplasmic anchor for activated MAPKs.
- Anti-apoptosis [PMID:10442631 "PED/PEA-15 co-precipitated with both FADD and FLICE"; "Thus, PED/PEA-15 is an endogenous protein inhibiting FAS and TNFR1-mediated apoptosis."].
- Glucose uptake (overexpression phenotype) [PMID:9670003], kept as non-core.
- Microtubule association is reported only as background in the mouse cDNA paper [PMID:8662970 "PEA-15, a protein kinase C substrate associated with microtubules"].

Changes:
- 11 bare GO:0005515 rows handled per the protein-binding policy: ERK1/2 rows MODIFY to GO:0051019 MAP kinase binding; FADD to GO:0035877 death effector domain binding; CASP8 to GO:0089720 caspase binding; TERF2IP (BiFC screen) REMOVE.
- MAPK cascade (IEA) MODIFY to GO:0070372 regulation of ERK1 and ERK2 cascade, because PEA15 is a regulator and not a cascade component.
- regulation of apoptotic process (IEA) MODIFY to GO:1902042 (already carried).
- microtubule associated complex (NAS) MODIFY to GO:0015630 microtubule cytoskeleton, because no defined complex exists.
- glucose import regulation KEEP_AS_NON_CORE.
- NEW: GO:0019887 protein kinase regulator activity and GO:0042308 negative regulation of protein import into nucleus, both IDA from PMID:23575685. PEA15 itself performs the anchoring step, so it passes the participation test.

Relative for next review: mouse Pea15 (Q62048, MGI:104799), the same SF1 subfamily and an IBA donor. No mouse review is in the repo.
