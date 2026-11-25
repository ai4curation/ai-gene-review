# MPK18 (At1g53510, Q9C5C0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: MPK18 is being reviewed as the experimentally characterised Arabidopsis relative
of melon A0A1S3BTE3 (co-ortholog of the MPK18/MPK19 pair in a MAFFT/NJ tree of all 20
Arabidopsis MPKs; `file:CUCME/A0A1S3BTE3/A0A1S3BTE3-bioinformatics/RESULTS.md`). No
ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon ARATH MPK18 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" and the perplexity-lite fallback also
failed (HTTP 403). No deep-research file exists. The review is built from the UniProt
record and the cached publications listed below.

### Evolutionary placement

- PANTHER 19.0: MPK18 = PTHR24055:SF420 "MITOGEN-ACTIVATED PROTEIN KINASE 18" (PANTHER
  Arabidopsis classification file). Its closest paralogs MPK19 (SF200) and MPK20 (SF392)
  are in separate subfamilies [file:CUCME/A0A1S3BTE3/A0A1S3BTE3-bioinformatics/RESULTS.md
  "In PANTHER, MPK18, MPK19 and MPK20 sit in three different subfamilies (SF420, SF200, SF392)."].
- Plant MAPK group D: activation loop TDY (residues 187-189; checked in the UniProt
  sequence), catalytic D151, VAIK K54, Gly-rich loop IGKGSYGVV (31-39). Long C-terminal
  extension with MobiDB-lite disordered regions (414-483, 510-544) typical of group D.
- IBA rows (protein Ser/Thr kinase activity, intracellular signal transduction, nucleus,
  cytoplasm) come from PTN000622075, a deep MAPK node with donors from yeasts, animals,
  Dictyostelium, moss and Arabidopsis. MPK18 itself (AT1G53510) is a donor for the nucleus
  and cytoplasm IBAs (its own IDA rows), which is expected, not circular.

### What is established experimentally in Arabidopsis (MPK18 itself)

- Interaction with the dual-specificity MAPK phosphatase PHS1 (Y2H; BiFC in cytoplasm) and
  in vitro dephosphorylation of phospho-MPK18 by PHS1 [PMID:19392697 "in vitro
  dephosphorylation assays indicated that phospho-MPK18 can be dephosphorylated by
  recombinant PHS1"]. Abstract only in cache.
- mpk18 mutants: defects in microtubule-related functions, moderately stabilized
  microtubules; mpk18 partially suppresses phs1-1 root phenotypes [PMID:19392697].
- MKKK20 binds MPK18 (Y2H, BiFC nucleus + cytoplasm) and phosphorylates it in vitro,
  including on the activation-loop TXY motif (anti-pERK); MKK3 does not interact with or
  phosphorylate MPK18 -> proposed non-canonical MKKK20-MPK18 module bypassing a MAPKK
  [PMID:28848569 "MPK18 alone did not display autophosphorylation activity but was a good
  substrate for the MKKK20"].
- GFP-MPK18 (35S, transient in onion epidermis) is nuclear and cytoplasmic [PMID:28848569
  "All three kinases were observed both in the cytoplasm and the nucleus"].
- mkkk20/mpk18 double mutant analysis places MKKK20 upstream of MPK18 in oryzalin-sensitive
  root growth/skewing [PMID:28848569].
- High-throughput Y2H partners: DELLAs GAI, RGA, RGL2 and BRX (PMID:32612234, abstract
  only), GAI and RGA (PMID:21798944, AI-1 interactome map). No functional follow-up.

### What is NOT established experimentally

- MPK18's own protein kinase activity has not been demonstrated: recombinant MPK18 did not
  autophosphorylate or phosphorylate MBP, and no MPK18 substrate is known [PMID:28848569
  "When incubated together, MKK3 and MPK18 did not show any reciprocal kinase activity nor
  did they phosphorylate MBP"]. MAP kinase activity is therefore inferred from family
  membership and intact catalytic residues (strong inference, but an inference).
- No MAPKK is known to activate MPK18; participation in a canonical three-tier MAPK
  cascade (GO:0000165 definition requires MAP3K -> MAP2K -> MAPK) is not shown.
- How MPK18 affects microtubules (substrates, e.g. MAPs) is unknown.

### Annotation decisions (summary)

- MAP kinase activity (IEA, ISS): ACCEPT as core, explicitly inferred.
- protein Ser/Thr kinase activity (IBA): TOO_GENERAL (entailed by MAP kinase activity).
- protein serine kinase activity (IEA Rhea): ACCEPT, non-entailed sister of MAP kinase
  activity in GO; reaction curated by UniProt.
- ATP binding: KEEP_AS_NON_CORE.
- MAPK cascade (IEA): UNDECIDED - only non-canonical MKKK20->MPK18 phosphorylation known.
- signal transduction (IC, IEA): TOO_GENERAL (intracellular signal transduction accepted).
- intracellular signal transduction (IBA): ACCEPT.
- cortical microtubule organization (IMP): MODIFY -> regulation of microtubule
  cytoskeleton organization (GO:0070507); no "regulation of cortical microtubule
  organization" term exists (term search). A signalling kinase whose loss stabilises MTs
  modulates MT organization rather than building it.
- cytoplasm: ACCEPT; nucleus: KEEP_AS_NON_CORE (transient overexpression only).
- protein binding: PHS1 -> MODIFY protein phosphatase binding (GO:0019903; enzyme-substrate
  relationship supported by dephosphorylation assay); MKKK20 -> MODIFY protein kinase
  binding (GO:0019901; substrate of MKKK20); HT-Y2H DELLA/BRX rows -> REMOVE (uninformative).

### Transfer guidance for A0A1S3BTE3

Transferable (family-level): MAP kinase activity, ATP binding, TDY dual-phosphorylation
activation, intracellular signal transduction. MPK18-specific findings (PHS1 regulation,
MKKK20 module, microtubule phenotype) are subfamily-level (SF420) and should not be
transferred unless the melon protein is placed in SF420.
