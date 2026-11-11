# Bicdl1 (mouse, A0JNT9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Bicdl1 (BICDR-1) is the experimental reference for horse BICDL1 (F6SAQ3); both sit in
PANTHER PTHR32123:SF12, and mouse Bicdl1 (MGI:1922915) seeds the GO:0055107 IBD at PAINT node
PTN001281025. No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon mouse Bicdl1 --fallback perplexity-lite` failed (falcon and
the perplexity-lite fallback both timed out at the 600 s limit). The review was written from the cached
full texts instead.

Evidence established with the mouse protein:
- Direct, GTP-dependent Rab6A/B binding via the C-terminus; K512 required [PMID:20360680 "showed that lysine 512 is required for binding to Rab6"].
- KIF1C tail binding [PMID:20360680 "Both full-length BICDR-1 and an N-terminal region of BICDR-1, amino acids 1–353, interact with the C-terminal tail domain of Kif1C"].
- Dynein/dynactin co-IP and pericentrosomal recruitment [PMID:20360680 "BICDR-1 precipitates the major dynein/dynactin subunits"].
- siRNA loss of pericentrosomal Rab6 vesicle clustering (Vero cells) [PMID:20360680 "in the absence of BICDR-1, Rab6-positive vesicles no longer cluster around the centrosomal region"].
- Recombinant mouse BICDR1 recruits two dyneins and gives faster motility [PMID:29420470 "both BICDR1 and HOOK3 preferentially recruit two"]; two adaptors bound on microtubules [PMID:36071160 "We found that two adaptors occupy the complex"].

Not mouse evidence: neural development phenotypes in vivo come from zebrafish morpholinos; the mammalian
neurite phenotype is from sustained (over)expression and is inhibitory.

Decisions: protein binding rows -> kinesin binding / small GTPase binding (MODIFY); neuron projection
development -> negative regulation of neuron projection development (MODIFY, non-core, indirect);
cytoskeleton -> centrosome (MODIFY); Golgi to secretory granule transport kept non-core (BICDR-1 does
not sort cargo or affect exocytosis; its role is microtubule-based transport); vesicle transport along
microtubule accepted as core process; NEW cytoskeletal motor activator activity (IDA, PMID:29420470)
and dynein complex binding (IDA, PMID:36071160). Comparator check: human BICD2 carries
GO:0070840 dynein complex binding but not GO:0140660 in QuickGO (queried 2026-10-21), raised as a
suggested question.
