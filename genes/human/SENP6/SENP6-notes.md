# SENP6 (human, Q9GZR1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: SENP6 is the closest experimentally characterised relative of S. pombe ulp2
(O13769). Both are in PANTHER PTHR46896 (SENP6 in SF1, ulp2 in SF3). This review is of SENP6
in its own right, so that its experimental findings can serve as the reference for any transfer.
No ProtNLM2 files were opened.

### Deep research
- `just deep-research-falcon human SENP6 --fallback perplexity-lite` failed. Falcon returned
  403 Forbidden on Edison auth (`/auth/login`), and the perplexity-lite fallback timed out. No
  deep-research file was produced. The review relies on cached primary literature, listed below.

### Evolutionary grounding (QuickGO IBA rows queried by PAINT node, withFrom=PANTHER:PTN...)
- PTN002930416 is a deep node covering SENP6, SENP7 (including fish senp7/senp7b), the fly
  members and many fungal Ulp2 orthologs (ULP2 in taxon 4922, ulp2_2 in 5627). It carries
  GO:0016926 protein desumoylation, GO:0070139 SUMO-specific endopeptidase activity, nucleus
  and cytoplasm. Function inherited at this node is the part that is transferable to S. pombe
  ulp2.
- PTN002930429 is a vertebrate SENP6-only node (SENP6 orthologs, fish senp6a/senp6b). It
  carries GO:0090169 regulation of spindle assembly and GO:0090234 regulation of kinetochore
  assembly, with human SENP6 IMP (PMID:20212317) as the donor. PAINT did NOT place these at
  PTN002930416. I treat that omission as deliberate: the kinetochore and spindle roles are
  SENP6-subfamily claims and should not be transferred to SENP7 or to fungal Ulp2.

### Experimentally established for human SENP6
- Activity: isopeptidase (deSUMOylase) for SUMO2/3 chains. It prefers three or more SUMO2/3
  moieties [PMID:17000875 "SUSP1 acts preferentially against substrates bearing three or more
  SUMO2/3 moieties"], cleaves di- and poly-SUMO2/3 with purified enzyme [PMID:18799455], and
  cleaves mixed SUMO1-SUMO2/3 chains [PMID:21148299]. Precursor processing is weak
  [PMID:18799455 "SENP6 and SENP7 exhibit lower rates for processing pre-SUMO1, pre-SUMO2, or
  pre-SUMO3 in comparison with SENP2"; PMID:17000875 "SUSP1 has little processing activity"].
  SUMO2/3 specificity depends on the Loop1 insertion [PMID:21878624, PMID:24424631].
- Location: nucleoplasm, with minimal cytoplasmic signal [PMID:17000875], plus a chromatin
  fraction [PMID:37735495].
- Substrates and processes: CENP-I and the CENP-H/I/K inner kinetochore, antagonising RNF4
  [PMID:20212317]; group deSUMOylation of the CCAN and Mis18 complex [PMID:31485003]; CENP-C and
  CENP-I hyper-SUMOylation on SENP6 loss [PMID:31980633]; MIS18BP1 [PMID:30631152]; PML nuclear
  bodies [PMID:21148299]; RPA70 [PMID:20705237]; DNA damage response proteins (BRCA1-BARD1,
  53BP1, BLM, ERCC1-XPF) [PMID:37735495]; cohesin and chromatin residency via an N-terminal
  multi-SIM region [PMID:31597105, abstract only]; NEMO in TLR signalling [PMID:23825957];
  RXRalpha with SUMO1 [PMID:16912044, abstract only].

### Decisions
- GO:0070139 (defined as cleavage within SUMO, i.e. precursor maturation): KEEP_AS_NON_CORE on
  both rows. This matches the ulp2 review's handling. NEW GO:0016929 deSUMOylase activity is
  the core MF.
- Cysteine-type peptidase activity → MODIFY to GO:0016929. Proteolysis → MODIFY to GO:0016926.
  Protein modification by small protein removal → MODIFY to GO:0016926.
- Protein sumoylation (UniPathway IEA) → REMOVE. SENP6 is a deconjugase.
- Cytoplasm IBA → MARK_AS_OVER_ANNOTATED. Human SENP6 is not a donor, and direct imaging
  shows it is nucleoplasmic.
- Protein binding (CENP-I IPI) → REMOVE under the protein-binding policy.
- Regulation of kinetochore assembly → ACCEPT (SENP6 deSUMOylates the kinetochore subunits).
  Regulation of spindle assembly → KEEP_AS_NON_CORE (secondary to the kinetochore defect).
- No NEW process terms were added. SUMO polymer binding (GO:0032184) via the multi-SIM region is
  plausible but rests on an abstract-only source, so it is raised as a question and an
  experiment instead.

### Completion check (2026-10-21)
- All 17 GOA rows carry a considered action. GO:0070139 and GO:0016929 definitions and GO:0016929
  ancestry (is_a GO:0008234 cysteine-type peptidase activity) re-checked in OLS4.
  `just validate human SENP6` passes. History record:
  history/genes/human/SENP6/2026-10-21T112256Z-claude-code-801dcf.yaml.
