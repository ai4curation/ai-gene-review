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
  - L-glutamate transmembrane transport (ISS) → GO:0002037. The mouse donor row is acts_upstream_of_or_within; the ISS turned it into involved_in.
  - Intrinsic apoptotic signalling (IDA) → GO:1902177 positive regulation of oxidative stress-induced intrinsic apoptotic signaling pathway.
  - RNF185 binding → ubiquitin protein ligase binding [PMID:29481911].
- REMOVE: MIEF1 protein binding (policy).
- NEW:
  - ER tubular network organization (IDA, PMID:40209949).
  - Transporter inhibitor activity (ISO from rat, PMID:11242046).
