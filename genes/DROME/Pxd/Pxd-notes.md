# Pxd (Q01603, CG3477) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Pxd was reviewed as the closest experimentally characterised relative (paralog) of
DROME/CG42331. No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon DROME Pxd --fallback perplexity-lite` failed: Falcon (Edison) returned
"Failed to authenticate" (403) and the Perplexity fallback returned 401 insufficient_quota. No
deep-research file exists. The literature below was found by PubMed searches ("Pxd AND
Drosophila", "chorion peroxidase Drosophila", "Drosophila melanogaster peroxidase dityrosine")
and cached with `just fetch-pmid`. All cached Pxd papers are abstract-only.

### Literature

- Ng et al. 1992: cloning of DmPO, 690 aa, similar to myeloperoxidase and thyroid peroxidase
  [PMID:1482687 "The deduced amino acid sequence reveals an overall homology to myeloeosinophil and thyroid peroxidase"].
- Konstandi et al. 2005, the key paper: recombinant Pxd makes di-tyrosine with H2O2 [PMID:15979004
  "in the presence of H2O2 was able to convert tyrosine residues to di-tyrosine moieties"]. Its mRNA
  is in follicle cells at stages 11-14 [PMID:15979004 "the Pxd mRNA is specifically expressed in
  follicle cells during the late stages of oogenesis 11-14"], and the protein is in the endochorion
  and ICL [PMID:15979004 "the Pxd peroxidase is selectively localized in the chorion structures and
  particularly in the endochorion and innermost chorionic layer (ICL)"]. The antibody was raised against
  Aedes peroxidase (anti-rAePO).
- Earlier work, before the gene was known: the chorion has an endogenous peroxidase that cross-links
  chorion proteins in late stage 14 [PMID:28305174 "normal crosslinking can be prevented with peroxidase inhibitors"].
  H2O2 comes from the follicle cells [PMID:18620142 "hydrogen peroxide is an endogenous, programmed product of the follicle cells"].
- Keramaris et al. 1991 proposed that S38 is the eggshell peroxidase (anti-HRP immunoreactivity)
  [PMID:1903086]. This is superseded by the Pxd identification and is recorded as DISPUTED.
- Bactrocera oleae bPxd (PMID:16741869) behaves the same way, but it is another species and its
  orthology rests on sequence similarity only, so it is background.
- drop-dead (PMID:37163052) is needed for vitelline membrane proteins to be cross-linkable; Pxd was
  not studied there.
- I found no Pxd mutant, RNAi or other genetic study. The in vivo requirement is untested.

### Phylogeny (Pxd-bioinformatics/RESULTS.md)

- The catalytic distal His185, Arg331 and proximal His437 are all retained.
- In the unfiltered PANTHER tree, Pxd (SF86) descends from the root node PTN000158755 (LUCA) and from
  only that one of the 15 PAINT IBD nodes in PTHR11475. So Pxd inherits peroxidase activity by IBA,
  and nothing else. Thiocyanate, iodide and halide activities, defense response to bacterium and the
  extracellular-region IBD are on vertebrate or other nodes that Pxd does not descend from.
- CG4009 is Pxd's closest paralog (PTN000158981, a duplication below a Diptera speciation node).
- The task brief calls the PTN008518854 polytomy (cardinal, CG42331 and Pxd/CG4009/CG10211)
  fly-specific. In the unfiltered tree its taxonomic range is Hexapoda-Crustacea. It only looks
  fly-specific in the species-filtered tree. It is still an arthropod-specific expansion with no
  vertebrate or nematode ortholog.
- The species-filtered tree drops PTN000158755 entirely, so the first draft of the script wrongly
  reported that Pxd does not inherit it. The script now uses the unfiltered tree for the ancestor path.

### Decisions

- GO:0140825 (IDA, IEA): ACCEPT; this is the core activity. The term is labelled lactoperoxidase,
  but its definition is the generic phenolic-donor reaction (EC 1.11.1.7), so it fits tyrosine
  oxidation. It does not imply halide or SCN- oxidation.
- GO:0004601 (IBA, IEA): MODIFY to GO:0140825, as a refinement. The IBA is sound.
- GO:0042600 egg chorion (IDA) and GO:0005576 extracellular region: ACCEPT.
- GO:0007306 egg chorion assembly (IC): ACCEPT. Pxd catalyses the cross-linking step, which is
  participation, not just a requirement.
- GO:0020037 heme binding: KEEP_AS_NON_CORE (a cofactor of the activity).
- GO:0006979 response to oxidative stress and GO:0098869 cellular oxidant detoxification:
  MARK_AS_OVER_ANNOTATED. Pxd consumes H2O2 that is produced on purpose, outside the cell, to build
  the eggshell.
- No NEW terms. I considered GO:0018149 peptide cross-linking, but the cross-linking of chorion
  proteins by Pxd itself was not shown directly (the recombinant assay used tyrosine), so it is
  raised as a question instead.

### For transfer to relatives (e.g. CG42331, CG4009)

- Experimentally established in Pxd: phenolic-donor peroxidase activity (tyrosine to di-tyrosine,
  on recombinant protein), chorion localisation, and expression in late follicle cells.
- Inferred only: heme binding, and the in vivo role in chorion hardening (biochemistry plus
  localisation, no genetics).
- The chorion-specific process role is tied to Pxd's expression in follicle cells, so it should not
  be transferred to paralogs without expression or localisation evidence for them.
