# BBS5 (Q8N3I7) review notes

## Gene identity
- Human BBS5, HGNC:970, UniProt Q8N3I7, 341 aa, gene ID 129880.
- Member of the "BBS5 family"; contains two pleckstrin-homology (PH)-like domains (InterPro IPR014003 BBS5_PH; Pfam PF07289 BBL5; SMART SM00683 DM16 x2; CDD cd00900 PH-like). [UniProt Q8N3I7 cross-references]
- Core subunit of the BBSome (8-subunit complex: BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP10/BBIP1). [PMID:17574030; UniProt SUBUNIT]
- Loss of function causes Bardet-Biedl syndrome 5 (BBS5; MIM:615983), autosomal recessive ciliopathy: retinopathy, obesity, polydactyly, hypogenitalism, renal malformation, intellectual disability. [UniProt; PMID:15137946, PMID:18203199, PMID:21344540]

## Core function evidence
- **BBSome subunit (GO:0034464, part_of)**: BBS5 was identified as one of the seven (later eight) core BBSome proteins by tandem affinity purification + mass spec. [PMID:17574030 "we identify a complex composed of seven highly conserved BBS proteins. This complex, the BBSome..."]. Multiple independent IDA/IPI confirmations (PMID:20080638, PMID:24550735, PMID:19081074 ComplexPortal CPX-1908). Strong, well-supported. CORE.
- **Phosphoinositide / PI3P binding (GO:0032266, enables)**: Nachury et al. 2007 showed BBS5 binds phosphoinositides. [PMID:17574030 RP line "BINDING TO PHOSPHOINOSITIDES"; UniProt SUBUNIT "Binds to phosphoinositides"]. The two PH-like domains are consistent with a lipid/membrane-binding role contributing to BBSome membrane association. IDA from PMID:17574030 + IBA. The specific PI3P term is a reasonable representative; note original assay reported binding to phosphoinositides broadly. CORE molecular function.
- **Ciliary membrane (GO:0060170, located_in)**: BBSome localizes to the ciliary membrane. [PMID:17574030 "...but also to the membrane of the cilium."]; ComplexPortal IDA PMID:19081074. ACCEPT.
- **Ciliary basal body (GO:0036064)**: BBSome/BBS5 localizes to basal bodies/centriolar satellites. [PMID:17574030 "localizes to nonmembranous centriolar satellites in the cytoplasm"]; UniProt subcellular location "cilium basal body", "centriolar satellite". ACCEPT.
- **Cilium assembly / ciliogenesis (GO:0060271, involved_in)**: BBSome required for ciliogenesis. [PMID:17574030 "the BBSome is required for ciliogenesis but is dispensable for centriolar satellite function"]. IMP from PMID:17574030. ACCEPT as core BP.

## Localization annotations
- Cytosol/cytoplasm (GO:0005829, GO:0005737): HPA IDA + Reactome TAS + UniProt subcell mapping. BBSome assembles in cytoplasm before ciliary entry; consistent. KEEP (non-core / accept).
- Centriolar satellite (GO:0034451): consistent with PMID:17574030 and UniProt. ACCEPT.
- Cilium (GO:0005929): HPA IDA + Ensembl IEA. ACCEPT (parent of ciliary membrane).
- Axoneme (GO:0005930): Ensembl IEA projected from mouse. BBSome traffics within cilium along the axoneme via IFT; plausible but weaker. KEEP_AS_NON_CORE / accept as IEA.

## Interaction (protein binding GO:0005515) annotations
Numerous IPI GO:0005515 "protein binding" annotations from IntAct/affinity capture and HT interactome screens:
- PMID:17574030, 20080638, 22500027, 27173435, 29039417, 33961781 -> BBS9 (Q3SYG4), i.e. intra-BBSome partner. [UniProt INTERACTION: Q8N3I7-Q3SYG4 BBS9 NbExp=9]
- PMID:25416956 -> CRADD (P78560), KLC3 (Q6P597) [HT interactome, Rolland et al.]
- PMID:25552655 -> IQCB1/NPHP5 (Q15051): BBSome integrity / ciliary trafficking. [PMID:25552655 "NPHP5 ... interacts with the BBSome ... depletion ... leads to dissociation of BBS2 and BBS5 from the BBSome"]
- PMID:24550735 -> AZI1/CEP131 (Q9UPN4): regulates BBSome ciliary trafficking. [PMID:24550735]
- PMID:24939912 -> PKD1 (Q8TAM2): BBSome regulates ciliary trafficking of PKD1. [PMID:24939912; UniProt INTERACTION with PKD1]
- PMID:18762586 -> PCM1 (Q9NRI5): centriolar satellite context (SYSCILIA).
- PMID:16327777 -> CCDC28B (Q9BUN5): epistatic BBS modifier; pericentriolar. [PMID:16327777; UniProt "Interacts with CCDC28B"]
- PMID:33144677 -> DLEC1 (Q9Y238): DLEC1 interacts with BBS complex subunits in mouse spermatogenesis. [PMID:33144677 "DLEC1 interacted with ... Bardet-Biedl Syndrome (BBS) protein complex subunits"]
All map to uninformative "protein binding" (GO:0005515). Per curation guidelines, "protein binding" should be avoided in favor of more informative MF terms. These are valid experimental interaction records but the GO term itself is uninformative as a molecular function statement -> MARK_AS_OVER_ANNOTATED (keep evidence of interaction but flag as not an informative MF). None should be REMOVE'd (real experimental IPI data).

## Questionable / over-annotation candidates
- **RNA Pol II transcription factor binding (GO:0061629), IPI, PMID:22302990**: This paper is primarily about BBS7 having a nuclear role and interacting with PcG protein RNF2. [PMID:22302990 abstract "the BBS7 protein ... probably has a nuclear role ... BBS7 interacts physically with the polycomb group (PcG) member RNF2 ... our data supports a similar role for other BBS proteins"]. The with/from is Q99496 = RING2/RNF2. Evidence for BBS5 specifically is indirect ("similar role for other BBS proteins"). The full text may contain BBS5-specific data so do not REMOVE; but a transcriptional/nuclear MF is not a core BBS5 function and is at odds with the well-established cytoplasmic/ciliary role. Mark as over-annotated / non-core. UNDECIDED leaning over-annotation; choose MARK_AS_OVER_ANNOTATED with reasoning, since it is an isolated, weakly-supported claim contradicting the consensus localization.
- **Heart looping (GO:0001947), ISS, GO_REF:0000024** from zebrafish/Xenopus ortholog (Q7ZWB7): BBS ciliopathy phenotypes include laterality defects (Kupffer's vesicle), but this is a downstream developmental consequence, not a core molecular role. KEEP_AS_NON_CORE.
- **Melanosome transport (GO:0032402), ISS, GO_REF:0000024** (Q7ZWB7): BBS knockdown causes melanosome transport delay in zebrafish. [PMID:24550735 "melanosome transport delay"]. Phenotypic/developmental, ortholog-based ISS. KEEP_AS_NON_CORE.
- **Motile cilium assembly (GO:0044458), ISS, GO_REF:0000024** (A8HWI3): BBS5 functions mainly in primary (sensory) cilia; motile cilium role is via ortholog ISS. The IBA cilium assembly (GO:0060271) is the better-supported generic term. KEEP_AS_NON_CORE (do not over-claim motile specificity).

## Summary of core functions
1. MF: phosphoinositide (PI3P) binding via PH-like domains -> membrane association of the BBSome (GO:0032266).
2. CC: structural part of the BBSome (GO:0034464); acts at ciliary membrane (GO:0060170) and basal body (GO:0036064).
3. BP: BBSome-mediated cilium assembly / ciliary membrane protein trafficking (GO:0060271).
</content>
