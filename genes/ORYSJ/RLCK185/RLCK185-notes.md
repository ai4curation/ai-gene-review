# RLCK185 (OsRLCK185, Q6I5Q6, Os05g0372100) - curation notes

## Sources
- Deep research: RLCK185-deep-research-falcon.md (Falcon); used for full-text details not in cached abstracts.
- Cached abstracts: PMID:23498959, PMID:28111288, PMID:28371870, PMID:30418086, PMID:37976240, PMID:24750441 (PBL27). Full text: PMID:38158656.
- PMIDs verified via PubMed MCP search "OsRLCK185" (16 hits).

## Identity
- RLCK subfamily VII Ser/Thr kinase; Arabidopsis counterpart PBL27 [PMID:24750441 "PBL27, an Arabidopsis ortholog of OsRLCK185, is an immediate downstream component of the chitin receptor CERK1"].

## Receptor step
- Identified as interactor of the Xoo effector Xoo1488 [PMID:23498959 "In response to chitin, OsRLCK185 associates with, and is directly phosphorylated by, OsCERK1 at the plasma membrane."].
- Silencing: [PMID:23498959 "Silencing OsRLCK185 suppressed peptidoglycan- and chitin-induced immune responses, including MAP kinase activation and defense-gene expression."]
- UniProt PTM: Ser-240/Thr-241/Thr-246 phosphorylated by CERK1 (deep research: triple mutant abolishes phosphorylation collectively).
- Also phosphorylated by OsSERK2 in the OsFLS2 complex [PMID:38158656 "Genetic evidence suggests that OsRLCK176 and OsRLCK185 may function downstream of the OsFLS2-mediated signaling pathway."].

## Substrates / MAPK link (rice, two independent groups)
- OsMAPKKKepsilon (OsMAPKKK24): [PMID:28111288 "OsRLCK185 interacts with and phosphorylates the C-terminal regulatory domain of OsMAPKKKε."]; [PMID:28111288 "Coexpression of phosphomimetic OsRLCK185 and OsMAPKKKε activates MAPK3/6 phosphorylation in Nicotiana benthamiana leaves."]
- OsMAPKKK18 (and Y2H with OsMAPKKK11): [PMID:28371870 "In vitro phosphorylation experiments showed that OsRLCK185 directly phosphorylates OsMAPKKK18."]
- OsDRE2a: [PMID:30418086 "OsDRE2a was phosphorylated by OsRLCK185."]
- OsRLK902-1/2 stabilise OsRLCK185 [PMID:37976240 abstract].
- Contrast with Arabidopsis: the PBL27-MAPKKK5 step is disputed (RLCK VII-4 redundancy); in rice the MAP3K link is supported by two independent labs with different MAP3K substrates.

## Curation decisions
- GO:0002768 EXP -> MODIFY to GO:0002752 (consistent with ORYSJ/CERK1, ARATH/PBL27, module).
- Kinase MF rows (EXP, IBA, IEA x2, EC, Rhea) ACCEPT; core MF GO:0004674.
- ATP binding, plasma membrane (IDA, IEA) ACCEPT.
- NEW GO:0043410 positive regulation of MAPK cascade: passes participation (phosphorylates the initiating MAP3K) and comparator (PBL27 carries GO:0043410 in GOA).
- No protein binding rows in GOA for this gene.
- Module agreement: chitin_perception annoton pbl27_kinase = GO:0004674 at plasma membrane, process GO:0002752 - matches. Module names MAPKKK5 as target; rice substrates are OsMAPKKKepsilon/OsMAPKKK18 (MAPKKK11/18 are MAPKKK5 orthologs).
