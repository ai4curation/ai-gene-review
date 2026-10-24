# MYL10 evidence notes

Human UniProt Q9BUA6 has a three-experiment ZNF76 interaction linked to [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/), “A reference map of the human binary protein interactome.” This is a binary interaction observation, not a demonstrated core light-chain mechanism. Calcium binding is supported by conserved EF-hand coordinating positions and the curated PAINT assertion.

The human mitochondrial GOA annotation is IDA under GO_REF:0000054 (expressed fusion proteins in living cells). Its propagation through an IBA containing the human target among the supporting entities is normal phylogenetic grounding. Neither the fusion-protein experiment nor the IBA proves a mitochondrial targeting peptide or an endogenous mitochondrial motor role. Retain the location as non-core rather than second-guessing the experiment.

The selected horse protein is 212 aa; human Q9BUA6 is 226 aa. Global alignment gives 166/192 identities (86.5%), with 85.0% human and 90.6% horse paired coverage. Differences and gaps concentrate in the variable N-terminal region; inspect the full alignment rather than treating percent identity as proof of completeness. The conserved EF-hand core supports family placement. No horse-specific physiological experiment was identified in the initial search, and the horse UniProt record is unreviewed; a completed human Falcon report has been inspected without a separate horse-specific Edison job.

## Human deep research

The completed Falcon report emphasizes the distinction between MYL10 and MYH10/MYLK, and between conserved RLC-family inference and direct human biochemistry. It retrieves murine precursor-B-cell PLRLC expression (Oltz et al., DOI10.1002/j.1460-2075.1992.tb05341.x) and a mouse optic-nerve-regeneration screen (Lindborg et al., DOI10.1016/j.celrep.2021.108777). These are leads for organism-specific functions, not grounds to assign human B-cell signaling or horse neural repair. Direct calcium affinity and endogenous myosin partners remain unresolved. The report's assertion that no organellar localization evidence exists misses the human fusion-protein IDA/PAINT record; retain that curator-supplied localization and its limits instead of treating an incomplete search as refutation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research HORSE MYL10 --provider falcon` failed (Edison/falcon "Failed to authenticate"); no horse deep-research file was produced. Literature was read directly instead: PMID:1628631 (abstract only) and PMID:33657370 (full text cached), plus the existing human MYL10 falcon report.

### Identity of the benchmark accession
- A0A9L0TJE1 (212 aa) is the product of the Ensembl canonical transcript ENSECAT00000140463 of horse gene ENSECAG00000022094 (MYL10) and matches RefSeq XP_070088660.1 / GeneID 100060444 (Ensembl REST lookup, 2026-10-20). It is not a fragment.
- The horse gene has four unreviewed UniProt entries (A0A9L0TJE1 212 aa, A0A9L0R871 202 aa, F6XM32 171 aa, A0A3Q2H4N1 147 aa). All share the same ~150-aa light-chain core; they differ in the N-terminal segment (alternative 5' exons) and F6XM32 has an alternative C-terminus that replaces the last EF-hand region [file:HORSE/MYL10/MYL10-bioinformatics/RESULTS-rereview.md "| F6XM32 | 171 | 16 | `MAPRRARKRAEGAAS` | False |"]. No reviewed horse MYL10 entry exists, so A0A9L0TJE1 is the most complete and canonical model.
- The N-terminal segment of A0A9L0TJE1 (res. 1-60, basic, MobiDB disordered) is not conserved with human (MLLRLVSNSW...), mouse (MGQSSLDHGV...) or rat; mouse PLRLC transcripts are likewise reported to use alternative promoters/processing at the 5' end (human falcon report, Oltz 1992).
- Human Q9BUA6 carries a 34-aa insertion (res. 58-91, SLALSPRLERNGMISAHCNLCLTGSSNSPASASQ) just before EF-hand 1 that mouse, rat and horse lack; horse is the more typical RLC structure here. This is why the earlier human-horse global alignment had only 85% human coverage.

### Evolutionary placement
- UniProt and the PANTHER 19.0 member index place A0A9L0TJE1 in PTHR23049 at family level only (no subfamily assigned to this 2023 entry). Human, mouse, rat and cow MYL10 are PTHR23049:SF36 (MYOSIN REGULATORY LIGHT CHAIN 10).
- New analysis `compare_sequences_rereview.py` → `RESULTS-rereview.md`: core identity 98.7% to mouse/rat MYL10, 98.0% to human MYL10, 83.6% to MYL2 (closest paralog), ≤69% to MYL5/MYL7/MYL9/MYL12A/B. NJ on core distances groups horse with the MYL10 orthologs, sister to MYL2. So horse A0A9L0TJE1 belongs in SF36; no conflict with the PTHR23049 family review, which lists it with human MYL10 under a single "Myosin regulatory light chains" grouping without a subfamily id.

### Annotation decisions
- Calcium ion binding (IBA PTN000549442 from MYL2; IEA InterPro): ACCEPT. EF-hand 1 loop DQNRDGFIDKED conserved, PROSITE EF_HAND_1 match.
- Cytoplasm (IBA, deep RLC node): ACCEPT. Curators did not propagate a myosin-complex term; none added.
- Mitochondrion (IBA PTN002746160 from human IDA GO_REF:0000054; IEA Compara): KEEP_AS_NON_CORE. Caveat: single fusion-protein observation, and the N-terminal segment where a targeting signal would reside is not conserved human vs horse.
- No NEW terms. The mouse pre-B expression/IL-7 induction (PMID:1628631) and the optic-nerve regeneration phenotype (PMID:33657370, "Literature regarding the function of Myl10 is scarce") are expression and organismal-phenotype data, not process participation.

### Relative
Human MYL10 (Q9BUA6, same SF36 subfamily and PAINT node, the donor of the mitochondrion IBA). Its review is status IN_PROGRESS, does not cite the MYL10 literature, and does not note its human-specific insertion, so it needs a full review. Mouse Myl10 (Q62082) has no review in the repo either.
