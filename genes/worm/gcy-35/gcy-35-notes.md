# gcy-35 (O02298) curation notes

Deep research: `just deep-research-falcon worm gcy-35 --fallback perplexity-lite` was attempted
(2026-10-08); both falcon and perplexity-lite exited with code 137 and no file was produced.
Review is based on cached publications and PubMed searches.

## Key findings
- GCY-35 heme (H-NOX) binds O2, unlike NO-sGCs [PMID:15220933 "The GCY-35 haem domain binds molecular oxygen, unlike the haem domains of classical nitric-oxide-regulated guanylate cyclases."]
- GCY-35/GCY-36 act as alpha-like/beta-like sGC subunits in URX [PMID:15203005 "We show that GCY-35 and GCY-36 act as alpha-like and beta-like sGC subunits"]
- URX activation by O2 rise requires gcy-35/gcy-36; sGCs are instructive [PMID:19323996 "The sGCs are instructive O2 sensors, as forced expression of URX sGC genes causes BAG neurons to detect O2 increases."]
- No in vitro reconstitution of worm sGC activity as of 2009 [PMID:19323996 "Testing these models will require biochemical reconstitution of C. elegans sGC activity, which has not yet been accomplished."]
- In vivo O2-evoked cGMP rise in URX [PMID:23940325 "We show that a rise in O2 can evoke a tonic increase in cGMP that requires an atypical O2-binding soluble guanylate cyclase"]
- PDL-1 targets prenylated GCY-35 to URX dendritic endings [PMID:25505325 "PDL-1 promotes localization of GCY-33 and GCY-35"]
- GLB-5 inhibits GCY-35 via H-NOX interactions [PMID:26791224]

## Decisions
- NO/CO binding (IDA, Gray 2004, abstract-only cache): KEEP_AS_NON_CORE (in vitro heme ligands; no NOS in worm).
- Defense response to Gram-negative bacterium (IGI, Meisel 2014): KEEP_AS_NON_CORE; behavioral effect of O2 preference on hypoxic PA14 lawn.
- NEW detection of oxygen (GO:0003032): GCY-35 is the O2-binding receptor itself. Comparator: GLB-5 (O2-binding globin in the same neurons) carries GO:0003032 in WormBase.
