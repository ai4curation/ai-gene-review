# A0A8B8L1Z3 (Abrus precatorius LOC113860185) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open or use any ProtNLM2 prediction file.

### Identity
- UniProt A0A8B8L1Z3 is an unreviewed TrEMBL entry (PE 4) of 474 aa, from RefSeq
  XP_027348664.1 (gene LOC113860185).
- It is not a fragment or an isoform. Its length matches the full-length Arabidopsis
  SF19 relative EIP9/SDJ1 (At5g64360, 464 aa), and the J domain (70-135) sits at the
  same N-terminal position.
- GOA has no annotations for this accession, so `existing_annotations` holds only the
  proposed NEW rows.

### Evolutionary placement
- PANTHER 19.0 places it in PTHR45496:SF19.
- The only Arabidopsis member of SF19 is At5g64360 (Q9FMF3). The same gene is called
  EIP9 in [PMID:21700722], DNAJ1 in [PMID:30523112] and SDJ1 in [PMID:30589221].
- Paralog subfamilies: SDJ2 (At2g01710) is in SF1, SDJ3 (At1g62970) in SF10, and
  ADMETOS (At4g11940) in SF32.
- PAINT node PTN002896004 (taxon:3398, flowering plants) is seeded from all four of
  these subfamilies, so the Abrus protein descends from it. The node carries:
  - nucleus (GO:0005634);
  - GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific.
- Global alignment identity of the query to its relatives:
  - SF19 members: 0.46 to EIP9/SDJ1 and 0.53 to the Populus proteins;
  - other subfamilies: 0.17-0.36.
  - See `A0A8B8L1Z3-bioinformatics/RESULTS-rereview.md`.
- The J domain has no HPD motif (`...LALLLEPHRNPF...`). EIP9/SDJ1, SDJ3 and ADMETOS also
  lack HPD; SDJ2 is the only one that has it.

### Literature on the relatives
- Harris et al. 2018 [PMID:30523112 "Ectopic recruitment of DNAJ1 enhanced gene
  transcription in plants, yeast, and mammals."]: SUVH1 and SUVH3 bind methylated DNA and
  recruit DNAJ1/DNAJ2 ["DNAJ1 and DNAJ2 lack any discernible methyl-binding domain, but they
  are robustly associated with SUVH1 and SUVH3"].
- Zhao et al. 2019 [PMID:30589221 "We demonstrate that the SUVH-SDJ complex components
  have transcriptional activation activity."].
- Park et al. 2011 [PMID:21700722 "EMF1-EIP9 heterodimers were localized in the nucleus"
  (abstract wording: "EMF1-EIP1, EMF1-EIP6 and EMF1-EIP9 heterodimers were localized in the
  nucleus")]: eip9 mutants flower early. This is an organismal phenotype and is not
  transferred.
- Miao et al. 2021 [PMID:34185870]: sdj1/2/3 triple mutants are hypomethylated at a
  subset of RdDM sites. This shows the SDJs are needed for methylation there, not that
  they take part in it, so no RdDM process term is proposed.

### Changes from the previous version
- Description rewritten. The old text claimed a "conserved HPD motif" (it is absent) and
  a cytoplasmic or ER-excluded Hsp70 cochaperone role. It also leaned on the IPR053052
  "Imprinting Balance Regulator" name, which is an unchecked LLM-generated InterPro
  description derived from ADMETOS.
- Core function changed:
  - before: protein folding chaperone / protein folding / cytoplasm;
  - after: transcription coactivator activity (GO:0003713) / positive regulation of
    DNA-templated transcription / nucleus.
- Added NEW rows (ISS, relying on the PTN002896004 placement) for nucleus and for
  transcription coactivator activity.
- The coactivator term deliberately replaces PAINT's GO:0001228 (DNA-binding
  transcription activator activity). SDJ proteins have no DNA-binding domain and reach DNA
  only when SUVH1/SUVH3 recruit them. SDJ2 already has an IDA for GO:0003713. This is
  raised as a suggested question for the PAINT node.
- Not transferred:
  - flowering time (an organismal phenotype);
  - gene silencing by RdDM (necessity-only evidence);
  - SUVH1/SUVH3 binding (bare protein binding).
- The deep-research (falcon) report is generic J-domain material and missed the SDJ
  literature. It is kept in the references but no longer used as support.

### Family review
- interpro/panther/PTHR45496/PTHR45496-review.yaml lists the target as the SF19
  representative and leaves functional coherence UNKNOWN.
- No disagreement about the subfamily placement.
- The family file's preferred name "ADMETOS-related" puts ADMETOS (SF32) first. The
  characterized function relevant to SF19 is the SUVH-SDJ transcriptional activation of
  SDJ1, so that summary could be improved. The family file was not edited.

### Modules
- No module in modules/ covers the SUVH-SDJ complex or RdDM-linked anti-silencing.
