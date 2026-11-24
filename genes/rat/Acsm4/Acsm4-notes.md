# Acsm4 (rat, Q7TN78, O-MACS) curation notes

## Session 2026-11-02

### Sources and deep research
- Deep research: `deep_research_wrapper.py rat Acsm4 perplexity` failed ("Provider 'perplexity' not available. Available: openscientist, claude_code"). No `-deep-research-<provider>.md` file was created.
- `mod-description-deep-research rat Acsm4` returned `no_curated: 1`: RGD has no curated gene description, so no `-deep-research-rgd.md` was written.
- The only primary paper on Acsm4 is PMID:12709059 (Oka et al. 2003). The cache has the abstract only.

### Biology
- O-MACS is a medium-chain acyl-CoA synthetase. Its expression is restricted to the olfactory epithelium (OE), in zone 1. [PMID:12709059 "RT-PCR analysis demonstrated that the o-macs gene is expressed only in the OE, unlike other MACS family genes."]
- Activity: [PMID:12709059 "Recombinant O-MACS protein tagged with c-Myc and His6 demonstrated an acyl-CoA synthetase activity for fatty acid activation"]. UniProt records C6-C12 substrates (hexanoate, octanoate, decanoate, dodecanoate; EC 6.2.1.2) as ECO:0000269 from this paper.
- Location: [PMID:12709059 "protein localization to mitochondria like other MACS family proteins"]. There is a transit peptide at residues 1-22 (ECO:0000255).
- Role: the authors only speculate. [PMID:12709059 "may play important roles in processing odorants in a zone-specific manner, or the zonal patterning of the OE during development"]

### Key curation issue: synthase vs synthetase
- GO:0004321 fatty-acyl-CoA synthase activity is the fatty acid synthase reaction (EC 2.3.1.86). Acsm4 is an acyl-CoA synthetase, a ligase (EC 6.2.1.2).
- The RGD IDA row from PMID:12709059 is the only seed of the PAINT IBD on PTHR43605 root node PTN001944787 (`PTHR43605	PTN001944787	GO:0004321	F	IBD	false	RGD:727928`). That IBD sends the wrong term to every family member, including mouse and human ACSM4 and the PSEPK PP_2213 precedent.
- Both rat rows are marked REMOVE. Source defects are recorded: GO_CENTRAL on PTN001944787 (CONFIRMED) and RGD on the IDA row (PROBABLE, since only the abstract was read).

### Other decisions
- GO:0006633 fatty acid biosynthetic process (IBA): MARK_AS_OVER_ANNOTATED. The seeds are MGI IDAs on Acsm1/Acsm3 from PMID:11470804, which says the products are [PMID:11470804 "utilized mainly for oxidation"]. A ligase makes acyl-CoA, not fatty acid. The likely intended term is GO:0046949 fatty-acyl-CoA biosynthetic process.
- GO:0006637 acyl-CoA metabolic process: MODIFY to GO:0046949.
- GO:0015645 fatty acid ligase activity: MODIFY to GO:0031956, which the gene already carries.
- GO:0005549 odorant binding (NAS): MARK_AS_OVER_ANNOTATED. The paper offers it only as a hypothesis, and enzyme substrate engagement is not annotated as a binding function. It is not removed, because the RGD curator saw the full text.
- Mitochondrial matrix (IBA, PTN001292823; seeds Acsm3 and bovine ACSM1, both matrix by fractionation [PMID:11470804 "Subcellular fractionation revealed that both MACS1 and Sa protein are localized in the mitochondrial matrix."]): ACCEPT. The core function location stays at mitochondrion because the matrix location has not been tested on Acsm4 itself.
