# WSS1 (P38838, YHR134W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: WSS1 is the experimental donor (SGD:S000001176) for PAINT node PTN001503361 and for
the PomBase ISO transfers to S. pombe wss1 (Q9P7B5). This review was written without opening
any ProtNLM2 prediction file.

### Deep research

`just deep-research-falcon yeast WSS1 --fallback perplexity-lite` failed on 2026-10-21:
falcon raised "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401
(quota exceeded). No deep-research file was produced. The review rests on the cached primary
literature listed below, which I read directly.

### Evolutionary placement

- UniProt: PANTHER PTHR46622 / PTHR46622:SF1 (DNA-DEPENDENT METALLOPROTEASE WSS1); Pfam WLM
  PF08325; MEROPS M80.001; "Belongs to the peptidase M3 family. WSS1-like metalloprotease (WLM)
  subfamily".
- S. pombe wss1 (Q9P7B5) is in the same subfamily (PTHR46622:SF1). The S. pombe paralog Wss2
  (O94580) is in PTHR47795. See `genes/SCHPO/wss1/wss1-bioinformatics/RESULTS-rereview.md`.
  The zinc ligand spacing (HExxH plus a His six residues downstream) is the same in both
  PTHR46622:SF1 members: P38838 H115/E116/H119/H125.
- IBA rows come from PTN001503361 (donors SGD WSS1, CGD Wss1, and UniProtKB:Q381Y4 for
  nucleus). PAINT propagated metallopeptidase activity, nucleus and DNA repair. It did not
  propagate the SUMO ligase, SUMO binding, protein sumoylation or vacuole terms. I read that as
  a deliberate decision: those terms are lineage- or study-specific and are not inherited at
  the node.

### Experimental findings in S. cerevisiae (what is established in this species)

- DNA-dependent metalloendopeptidase. In vitro, Top1 and other substrates are cleaved
  directly and DNA-dependently; the E116Q mutant loses function; EDTA inactivates the enzyme
  [PMID:24998930 "in vitro assays indicate that substrates such as topoisomerase 1 are
  processed by the metalloprotease directly and in a DNA-dependent manner"]. ssDNA, thiol
  reagents and SUMO chains induce self-cleavage; o-phenanthroline inhibits it (PMID:26349035).
- DPC repair. wss1 deletion mutants accumulate DPCs and gross chromosomal rearrangements, and
  are sensitive to formaldehyde and to Top1-dependent damage (PMID:24998930). Wss1 acts in
  parallel with Tdp1 on Top1cc (PMID:26349035, PMID:34818558). Ubx5-Cdc48 assists Wss1
  (PMID:37144685). Ddi1 is a parallel DPC protease (PMID:31902667, PMID:31276951).
- Histone degradation under HU replication stress. Wss1 degrades core histones bound
  non-covalently to ssDNA; this does not need Cdc48 or SUMO binding (PMID:32130911).
- Zinc. Crystal structure of the protease domain (PDB 5XBN): Zn bound by His115, His119 and
  His125, with Glu116 as the catalytic base (PMID:28811590).
- SUMO. Wss1 binds SUMO and poly-SUMO through C-terminal SIMs (PMID:20516210, PMID:26349035).
  The isopeptidase activity reported in PMID:20516210 was not reproduced by Stingele et al. or
  by Balakirev et al. (UniProt CAUTION). Balakirev et al. report an "E3-like" SIM-dependent
  SUMO chain-extension activity in vitro. One lab reported it and nobody has repeated it.
- Localization. Nucleus, with a single focus near the nuclear membrane, present only in the
  mother cell (PMID:18336552). Nuclear staining (PMID:26349035). Vacuolar accumulation under
  genotoxic stress, e.g. 4-NQO, or Top1 overexpression in tdp1 cells (PMID:26349035).
- Genetics. High-copy suppressor of smt3-331 (PMID:11606525); the suppression requires protease
  activity and SIM2 (PMID:26349035). UV sensitivity and genetic interactions with RAD52, SGS1,
  TOF1 and others; two-hybrid with Psy2 and Tof1 (PMID:15598824). Defective sister chromatid
  recombination at replication-born DSBs (PMID:23357952).

### Decisions (summary)

- Core: metalloendopeptidase activity (GO:0004222); protein-DNA covalent cross-linking repair
  (GO:0106300); nucleus. Histone catabolic process is accepted as a direct proteolytic role.
- MODIFY the general IBA/IDA metallopeptidase rows to metalloendopeptidase, and the IBA DNA
  repair row to protein-DNA covalent cross-linking repair.
- SUMO binding: ACCEPT. Binding via the SIMs has been reproduced and mutationally mapped.
- SUMO ligase activity and protein sumoylation: KEEP_AS_NON_CORE. Single-lab, E3-like activity;
  PAINT did not propagate it.
- Translesion synthesis, SCR at replication-born DSBs, fungal-type vacuole, zinc ion binding:
  KEEP_AS_NON_CORE. Wss1 acts upstream of TLS and SCR by removing the protein part of the
  lesion; it does not synthesize DNA or catalyse strand exchange.
- Nuclear envelope: MARK_AS_OVER_ANNOTATED. The abstract places the focus "near the nuclear
  membrane", not in it.
- NEW: DNA binding (GO:0003677). It is central to the DNA-dependent mechanism and is supported
  by curated UniProt text (ECO:0000269, PubMed:24998930).
- Not added: protein autoprocessing (GO:0016540). Self-cleavage is well documented in vitro,
  but its physiological role (activation or turnover) is unclear. Noted here, not annotated.

### Transfer guidance (for orthologs in PTHR46622:SF1)

Safe to transfer: metalloendopeptidase activity, DPC repair, nucleus. The DNA binding and
histone degradation findings are mechanistically tied to the conserved WLM domain, but they
have been assayed only in S. cerevisiae (and SPRTN, a different family). Do not transfer: the
SUMO ligase and sumoylation terms (single study, not propagated by PAINT); the vacuole, nuclear
envelope and mother-cell focus (species-specific observations); TLS and SCR (indirect).
