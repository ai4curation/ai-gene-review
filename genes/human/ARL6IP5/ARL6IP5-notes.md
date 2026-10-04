# ARL6IP5 (GTRAP3-18 / JWA / PRAF3) review notes

## Sources
- The affinage record self-scored as a pairwise "tie", so it was read sceptically. Its core claims were checked against the cached papers: EAAC1 binding (PMID:11242046), ER exit (PMID:18167356), Rab1 and ER-to-Golgi transport (PMID:18363836), and ER shaping (PMID:40209949). Many "JWA" findings are cancer cell-line signalling phenotypes and were not used.
- Rat Arl6ip5 (Q9ES40, RGD:708572) and mouse Arl6ip5 (Q8R5J9, MGI:1929501) donor annotations were checked in QuickGO.
- The UniProt "Associated with microtubules" claim traces to Chin. Sci. Bull. 48:1828 (2003), which has no PMID and could not be read, so the cytoskeleton row is UNDECIDED.

## Decisions
- ACCEPT:
  - Membrane (IBA, HDA) and ER membrane (IEA, ISS); the ER membrane is the core location [PMID:18167356 "GTRAP3-18 and JM4 are resident endoplasmic reticulum (ER) proteins."].
  - Negative regulation of transport (IBA).
  - Negative regulation of L-glutamate import across plasma membrane (IEA, ISS).
- KEEP_AS_NON_CORE:
  - Plasma membrane, cytoplasm and presynaptic cytosol (minor pools).
  - Three arsenic-trioxide knockdown IMP rows.
- MODIFY:
  - Protein transport (IDA) → GO:7770035 negative regulation of ER to Golgi vesicle-mediated transport. GO:0070862 negative regulation of protein exit from ER is obsolete.
  - L-glutamate transmembrane transport (ISS) → GO:0002037. The mouse donor evidence shows negative modulation of EAAT3 uptake, not glutamate translocation by ARL6IP5.
  - Intrinsic apoptotic signalling (IDA) → GO:1902177 positive regulation of oxidative stress-induced intrinsic apoptotic signaling pathway.
  - RNF185 binding → ubiquitin protein ligase binding [PMID:29481911].
- REMOVE: MIEF1 protein binding (policy).
- NEW:
  - ER tubular network organization (IDA, PMID:40209949).
  - Transporter inhibitor activity (ISO from rat, PMID:11242046).

## Review round 1 (PR #4181)
- The IBA propagation reviews now name the PTN nodes (PTN000304728, PTN002656438), with the donor detail in the comments.
- The GO:0015813 propagation comment is re-grounded in biology rather than the GOA qualifier.
- ER-phagy is now covered: knockdown reduces FAM134B-mediated ER-phagy flux (PMID:40209949). It is in the description, the ER-shaping core function and a suggested question. No NEW process term: the evidence is knockdown flux only.
- NEW membrane bending activity (GO:0180020, IDA, PMID:40209949) is the MF of the ER-shaping core function.
- NEW small GTPase binding (GO:0031267, IPI, PMID:18363836) covers co-IP with endogenous Rab1, with rescue by excess Rab1. It anchors a third core function: Rab1-linked negative regulation of ER-to-Golgi transport (GO:7770035, label confirmed in QuickGO; GO:0070862 confirmed obsolete in OLS).
- Transporter-inhibitor core function now includes plasma membrane; plasma membrane rows accepted (EAAC1 engagement at the surface, PMID:17646425, PMID:18799673).
- Donor PMIDs cited in propagation comments are now cached and referenced.
- Deep-research findings set aside:
  - ER retention of POMC (PMID:28904020) and RANKL (PMID:26220341). Abstract-only, single studies; consistent with the ER-retention core function but not used for new terms.
  - JWA-XRCC1 base-excision repair (PMID:19208635). A nuclear DNA-repair role for an ER multi-pass protein needs independent confirmation; not annotated.
  - The UniProt "taurine" function is by similarity to rodent work not in the cache; not annotated.
