# qkr58E-1 evidence notes

## Identity and evidence

Q9W255 is native qkr58E-1-PA, 396 residues. UniProt documents KH domain 111–209 and FlyBase lists distinct shorter PC/PD products. The exact accession retains the RNA-binding domain.

[PMID:18981222](https://pubmed.ncbi.nlm.nih.gov/18981222/) reports affinity-purified fly spliceosomal B and C complexes and mass spectrometry. FlyBase specifically assigns qkr58E-1 to these complexes; the cached abstract describes the experiment but does not reproduce the gene table. Those curated experimental assignments are retained, not rejected because the abstract omits a protein name. [PMID:25294944](https://pubmed.ncbi.nlm.nih.gov/25294944/) full text is cached and describes blinded protein-trap localization followed by gene assignment; the target-specific nuclear row is available through GOA.

Broad RNA binding and regulation of gene expression are supported, with more precise existing terms available. The fungal BBP paragraph overreaches the available evidence in claiming necessity and exact branch-site/tract/3′-site recognition: those individual claims remain UNC. No target-specific binding motif is inferred from the generic KH fold.

The primary [PMC spliceosome table](https://pmc.ncbi.nlm.nih.gov/articles/PMC2612486/) was additionally checked through its indexed table text: “KHDRBS2 | gi|24658086 | CG3613 | QKR58E-1”. This independently identifies the target in the experimental protein list. The directly opened PMC endpoint presents a browser challenge, so this is an inspected indexed table excerpt, not a claim that the local abstract cache contains the full table.

## Provider research assessment and primary follow-up

The completed Falcon synthesis identified direct RNP-network and selected-splice-event evidence. The full cached PMID:26294687 was read: QKR58E-1 coassociates with specific RNAs and spliceosome-related proteins, with reciprocal RNA-binding relationships involving SYP and QKR54B. The assay recovers complexes without crosslinking, so it does not prove direct contact for every RNA. PMID:27919077 is abstract-only in the publication cache; the publisher HTML and extracted Extended Data text are retained locally. Extended Data Figure 10b explicitly lists Qkr58E-1 knockdown among perturbations affecting fl(2)d splicing; panels g/h describe YT521-B interaction with and without RNase. This supports selected splicing regulation without assigning methylation-reader or writer activity. The report’s statement that direct localization was not found is incomplete: the original curated HDA nuclear annotation from PMID:25294944 is retained. The exact fungal branch-site motif remains unestablished.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Q9W255 is qkr58E-1-PA (FBpp0071754), 396 aa, the longest of three FlyBase polypeptides (PC 357 aa, A0A0B4LGB9; PD 379 aa, A0A0B4LG88) and the gene-centric reference proteome canonical. It is not a fragment or alternative model. It keeps the full KH domain (111-209; SMART SM00322, PROSITE PS50084, CDD cd22384 KH-I_KHDRBS).

**Evolutionary placement.** PANTHER 19.0 puts Q9W255 in PTHR11208:SF140 "GH05812P-RELATED". This subfamily is fly-only in the reference proteomes: qkr58E-1, qkr58E-2, qkr58E-3, nsr, CG10384, CG4021 and CG3927 (`.cache/panther/PTHR19.0_fruit_fly`). The QuickGO descendants of PAINT node PTN000879731 (the IBA source for GO:0000381) include all seven SF140 fly genes, qkr54B (SF42) and the vertebrate KHDRBS1/2/3 (SF30/SF34/SF29). So PTN000879731 is the KHDRBS (Sam68/SLM) clade, and qkr58E-1 is a fly lineage-specific paralog within it, despite the "quaking-related" name. QKI/How sit in SF125, and SF1 sits in SF45. Functions specific to the QKI subfamily (QKI RNA-element recognition, myelination) and the SF1 branchpoint role must not be transferred. The mRNA binding IBA comes from the deeper STAR node PTN000129548. PMID:26294687 describes "Mice bearing mutations in the orthologs of qkr54B and qkr58E-1" (meaning quaking), but that rests on the name and is not supported by the PANTHER placement.

**Evidence re-checked.** PMID:26294687 (full text): RIP-seq and AP-MS of tagged QKR58E-1. Targets are enriched for UCGs ("QKR58E-1 shows among the strongest enrichment for UCGs"), for 5' UTR binding and for 3' UTR extension RNAs. Protein partners include CG2807/SF3B1, CG16941/SF3A1 and LARK, and there are reciprocal RNA links with SYP and QKR54B. Lence et al. 2016 (PMID:27919077; local text file:DROME/qkr58E-1/qkr58E-1-nature20568.txt): Ext. Data Fig. 10b shows that knockdown changes fl(2)d splicing, and 10h is a co-IP with YT521-B with or without RNase T1. The legend does not give the RNase result. The Falcon report says the interaction is RNA-independent and that knockdown affected only a subset of six further events, but I could not verify either claim in the locally cached text, so both were removed from the description.

**Changes vs previous review.**
- GO:0000398 (IC) and the spliceosome CC rows (GO:0071011, GO:0071013; HDA) changed from ACCEPT to KEEP_AS_NON_CORE. The curator assignments are trusted, but co-purification does not make this KHDRBS-clade regulator a core spliceosome component. `in_complex: precatalytic spliceosome` was removed from core_functions.
- GO:0000381 IBA kept as ACCEPT, now justified by placement at node PTN000879731.
- GO:0003676 and GO:0003723 IEA kept as MODIFY to GO:0003729 mRNA binding. GO:0003729 IBA and both nucleus rows kept as ACCEPT.
- Fixed a nucleus supporting_text that did not support the claim and replaced it with the CPTI blinded-characterisation quote. Added PMID:27919077 to references with a reference_review on each publication. Added suggested questions and experiments.

**Relative to review next.** Human KHDRBS1/Sam68 (Q07666) is an experimental donor of the PTN000879731 IBA and the best-characterised member of the KHDRBS clade. The repo has no KHDRBS1 review (no genes/*/KHDRBS*). Its relation is clade-level co-orthology: the fly SF140 expansion and the vertebrate KHDRBS1/2/3 triplication both descend from PTN000879731.

**Family review.** interpro/panther/PTHR11208/PTHR11208-review.yaml agrees on subfamily SF140 and its representative. Its SF140 description is a copy of the family coherence text and does not mention the KHDRBS-clade placement. No module in modules/ covers qkr58E-1.
