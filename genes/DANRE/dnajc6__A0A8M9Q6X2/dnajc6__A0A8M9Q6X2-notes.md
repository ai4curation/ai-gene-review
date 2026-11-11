# dnajc6 (zebrafish auxilin, A0A8M9Q6X2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of A0A8M9Q6X2 in its own right, as the experimentally characterised reference
relative (same gene, UniProt gene-centric canonical) of A0A8M9QG43. No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon DANRE dnajc6 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient quota).
No deep-research file exists; the review is built from the literature below, read directly.

### Literature search

PubMed `(dnajc6 OR auxilin) AND zebrafish` returns two PMIDs: 20082716 (Bai et al. 2010) and
39245002 (a mangiferin transcriptome study, not relevant to dnajc6 function). PMID:20082716 is
therefore the only zebrafish experimental study of the protein.

### What is experimentally established for zebrafish dnajc6 (PMID:20082716, full text)

- Orthology: zAux (XP_001336673, 873 aa, chromosome 6) is the auxilin ortholog, distinct from gak
  [PMID:20082716 "However, while zAux is similar to zGAK, it is more similar to human and mouse auxilin proteins (Figure 2A)"].
- Localization, heterologous (HeLa, GFP-tagged, overexpressed): mostly cytosolic with perinuclear
  enrichment overlapping clathrin [PMID:20082716 "In cells expressing low levels of GFP-zGAK or GFP-zAux (marked by asterisks), GFP signals were mostly cytosolic and slightly enriched near the perinuclear regions."].
  ZFIN's cytosol and perinuclear-region IDA annotations come from this and sit on A0A8M9QG43, not on
  A0A8M9Q6X2.
- Overexpression produces clathrin-positive aggregates [PMID:20082716 "However, these cells also contained large GFP-positive aggregates (indicated by solid arrows and arrowheads) that were intensely clathrin-positive."].
- Cross-species functional rescue: GFP-zAux rescues the Drosophila dAux neurogenic eye phenotype and
  lethality, and the J domain is required [PMID:20082716 "these J-deletions failed to rescue the extra Elav-positive cell phenotype (Figure 4E &4F) and the lethality, suggesting that, like dAux, the J-domain is critical for the functions of these auxilin family proteins."].
- Expression: predominantly neural during embryogenesis (in situ).
- The morpholino Notch/neurogenesis phenotypes in this paper concern gak, not dnajc6, and are not
  transferred.

Isoform caveat: the paper's cDNA encodes 873 aa, while A0A8M9Q6X2 (XP_021332834.1) is 979 aa and
A0A8M9QG43 differs from it by 5 N-terminal residues.

### What is inferred (orthology / PAINT)

- PANTHER PTHR23172:SF4 (TYROSINE-PROTEIN PHOSPHATASE AUXILIN-RELATED), the same subfamily as
  mammalian auxilin. IBAs come from PTN000571055 (eukaryote-wide auxilin/GAK node: cytoplasm,
  vesicle, clathrin binding, clathrin-dependent endocytosis) and PTN002753975 (Euteleostomi node,
  mouse Dnajc6 donor: synaptic vesicle uncoating, postsynaptic density).
- Note: the local PAINT file `interpro/panther/PTHR23172/PTHR23172-paint.tsv` lists GO:0072318
  clathrin coat disassembly at PTN000571055, while GOA carries GO:0072583 for this gene, so the
  file and GOA may come from different releases. GO:0016191 is_a GO:0072318 and is_a GO:0072583
  (OLS hierarchicalAncestors), so no NEW clathrin coat disassembly row was added (it would be an
  ancestor of an accepted term).
- Mouse donor evidence (QuickGO, MGI:1919935): synaptic vesicle uncoating IMP/IDA PMID:20160091;
  postsynaptic density IDA PMID:17114649, a synaptosomal phosphoproteomics paper, so the PSD
  claim rests on fraction detection.

### Pseudophosphatase

UniRule UR000414225 assigns phosphoprotein phosphatase and hydrolase activity. Bovine auxilin
structure: P-loop lacks the final Arg of HCxxGxxR and no activity is detected
[PMID:20826345 "Differences at key residues in the catalytic cleft suggest that the PTEN-like region of auxilin will not have phosphatase activity, however, and indeed, no activity can be detected."].
`dnajc6-bioinformatics/ploop_check.py`: the zebrafish window 222-230 is TCSDGRAPS (Pro at the Arg
position, Thr at the His position). Zebrafish Cys223 aligns to human Cys164 (HCLDGRAAS). J-domain
HPD is intact (943-945). Both UniRule MF rows were removed.

### Actions summary

- REMOVE: GO:0004721, GO:0016787 (pseudophosphatase).
- MODIFY: GO:0005737 to GO:0005829 cytosol; GO:0031982 to GO:0030136 clathrin-coated vesicle.
- MARK_AS_OVER_ANNOTATED: GO:0014069 postsynaptic density (weak donor evidence).
- ACCEPT: GO:0030276 clathrin binding, GO:0016191 synaptic vesicle uncoating, GO:0072583
  clathrin-dependent endocytosis, GO:0030136 clathrin-coated vesicle.
- KEEP_AS_NON_CORE: GO:0098793 presynapse.
- For transfer: the zebrafish-experimental facts are cytosolic localization (heterologous system),
  clathrin co-aggregation, and J-domain-dependent rescue of Drosophila auxilin. Clathrin binding,
  Hsp70 co-chaperone activity and synaptic vesicle uncoating are orthology inferences.
