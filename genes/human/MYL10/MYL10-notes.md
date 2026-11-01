# MYL10 evidence notes

Human UniProt Q9BUA6 has a three-experiment ZNF76 interaction linked to [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), “A reference map of the human binary protein interactome.” This is a binary interaction observation, not a demonstrated core light-chain mechanism. Calcium binding is supported by conserved EF-hand coordinating positions and the curated PAINT assertion.

The human mitochondrial GOA annotation is IDA under GO_REF:0000054 (expressed fusion proteins in living cells). Its propagation through an IBA containing the human target among the supporting entities is normal phylogenetic grounding. Neither the fusion-protein experiment nor the IBA proves a mitochondrial targeting peptide or an endogenous mitochondrial motor role. Retain the location as non-core rather than second-guessing the experiment.

The selected horse protein is 212 aa; human Q9BUA6 is 226 aa. Global alignment gives 166/192 identities (86.5%), with 85.0% human and 90.6% horse paired coverage. Differences and gaps concentrate in the variable N-terminal region; inspect the full alignment rather than treating percent identity as proof of completeness. The conserved EF-hand core supports family placement. No horse-specific physiological experiment was identified in the initial search, and the horse UniProt record is unreviewed; a completed human Falcon report has been inspected without a separate horse-specific Edison job.

## Human deep research

The completed Falcon report emphasizes the distinction between MYL10 and MYH10/MYLK, and between conserved RLC-family inference and direct human biochemistry. It retrieves murine precursor-B-cell PLRLC expression (Oltz et al., DOI10.1002/j.1460-2075.1992.tb05341.x) and a mouse optic-nerve-regeneration screen (Lindborg et al., DOI10.1016/j.celrep.2021.108777). These are leads for organism-specific functions, not grounds to assign human B-cell signaling or horse neural repair. Direct calcium affinity and endogenous myosin partners remain unresolved. The report's assertion that no organellar localization evidence exists misses the human fusion-protein IDA/PAINT record; retain that curator-supplied localization and its limits instead of treating an incomplete search as refutation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: the benchmark accession Q9BUA6 is the canonical Swiss-Prot entry (MYL10_HUMAN, 226 aa, MANE Select ENST00000223167 / NP_612412.2). It is not a fragment, isoform or alternative gene model. Its ~60-residue N-terminal extension (MLLRLVSNSWPQ...) precedes the conserved RLC core and is a real feature of the canonical product (cf. the novel N-terminal sequences of mouse PLRLC transcripts described by Oltz et al. 1992 [PMID:1628631]).

Phylogenetic placement (checked from PANTHER 19.0 classification files and QuickGO IBA rows):
- PANTHER PTHR23049:SF36 "MYOSIN REGULATORY LIGHT CHAIN 10": human MYL10, mouse Myl10 (Q62082), rat, cow, frog, zebrafish (zgc:110679), chicken MYL10, and chicken MLC-2B cardiac (P02611, a protein-sequenced heart myosin light chain).
- Human paralogs: MYL2 SF9, MYL7 SF39, MYL5 SF8, MYL9 SF34, MYL11 SF10, MYL12A SF57, MYL12B SF58.
- IBA nodes on MYL10: calcium ion binding from PTN000549442 (donor MYL2 P10916; shared with MYL2, MYL7, MYLPF); cytoplasm from deep node PTN001495767; mitochondrion from PTN002746160 (MYL10-subfamily node, grounded on the human LIFEdb IDA).
- The nonmuscle RLC node PTN000549437 (MYL9, MYL12A/B) carries myosin heavy chain binding (GO:0032036) and myosin II complex (GO:0016460); these were NOT propagated to the sarcomeric node containing MYL10. MYL2-branch heart/myofibril terms (PTN002746142) also not propagated to MYL10. Treated as deliberate; no NEW terms added. Raised as a suggested question.

Sequence: EF-hand 1 loop residues 97-108 = DQNRDGFIDKED, a canonical Ca-coordinating loop (identical to MYL2 DQNRDGFIDKND except position 11). N-terminal phosphorylation motif RKRAEGTASSNVFSMF aligns with MYL2 KKRAGGANS(15)NVFSMF (MYL2 Ser15 phosphorylated per UniProt P10916). Inspected by hand; no new bioinformatics file written.

Mitochondrion: mouse Myl10 has an HDA mitochondrion annotation from MitoCarta [PMID:18614015], independent of the human GFP-fusion IDA. Kept as non-core.

Changes from previous version: removed horse-specific wording that had been copied into the human reasons; GO:0005515 ZNF76 IPI changed KEEP_AS_NON_CORE -> REMOVE (protein-binding policy); cytosol rows KEEP_AS_NON_CORE -> ACCEPT (correct soluble compartment; Reactome smooth-muscle context noted as not MYL10-specific); description rewritten; references added (PMID:1628631, PMID:18614015, deep research file); suggested questions/experiments added; status COMPLETE.

Relative: no characterised MYL10 ortholog beyond expression (mouse Myl10, PMID:1628631) and a CRISPR regeneration screen. Nearest characterised paralog by PAINT placement is human MYL2 (P10916), the experimental donor of the shared PTN000549442 node; no human MYL2 review exists in the repo.

Family review interpro/panther/PTHR23049/PTHR23049-review.yaml groups MYL10 under a single generic "Myosin regulatory light chains" subfamily label without naming SF36 or separating sarcomeric from nonmuscle RLC branches; not a contradiction, but it under-resolves the placement. No modules/ files mention MYL10.
