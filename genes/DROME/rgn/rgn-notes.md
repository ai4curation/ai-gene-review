# rgn (M9PFV8): evidence and ProtNLM claim review

Regeneration is a secretory-pathway C-type-lectin-domain protein implicated in imaginal-disc regeneration and intestinal epithelial repair. Genetic perturbation affects blastema formation, intestinal progenitor signaling and regenerative growth, while its ligand specificity and direct subcellular localization remain unresolved.

Exact input: [M9PFV8](https://www.uniprot.org/uniprotkb/M9PFV8/entry), 808 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [rgn-predictions-source.json](rgn-predictions-source.json). Source features: [rgn-uniprot.txt](rgn-uniprot.txt), with an exact extraction in [rgn-sequence-evidence.json](rgn-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR001304; C-type_lectin-like.
DR   InterPro; IPR016186; C-type_lectin-like/link_sf.
DR   InterPro; IPR016187; CTDL_fold.
FT   SIGNAL          1..23
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          70..199
FT                   /note="C-type lectin"
FT                   /evidence="ECO:0000259|PROSITE:PS50041"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | C-type lectin domain-containing protein | CNN | PROSITE identifies a C-type lectin-like domain at residues 70-199; PMID:18485344 independently describes the signal sequence and CTLD in Rgn. The domain claim is supported without assigning carbohydrate specificity. |
| Location | Secreted (SL-0243) | UNC | The signal peptide and lectin domain make secretion plausible, and PMID:18485344 independently discusses this architecture. However, the exact long isoform has curated trans-Golgi/vesicle assertions and no direct secretion assay; secretory-pathway entry does not establish release as a soluble extracellular protein. |

## Literature evidence

- [PMID:18485344](https://pubmed.ncbi.nlm.nih.gov/18485344/): “We identified three genes, regeneration (rgn), augmenter of liver regeneration (alr) and Matrix metalloproteinase-1 (Mmp1) expressed specifically in blastema cells during disc regeneration.”
- [PMID:41935796](https://pubmed.ncbi.nlm.nih.gov/41935796/): 2026 abstract-only evidence that Rgn deficiency in gut progenitors disrupts Notch signaling, insulin/TOR-linked redox control and intestinal stem-cell maintenance during epithelial repair.
- [PMID:42486707](https://pubmed.ncbi.nlm.nih.gov/42486707/): bibliographic cached corrigendum to PMID:41935796; the cache does not expose correction details.

## Annotation decisions

PAINT provenance: `just fetch-panther-paint PTHR23211` returned exactly one annotated node, `PTN000575073`, with two IBD rows for mammalian TGN38/TGOLN trans-Golgi localization.

- GO:0005802 trans-Golgi network (IBA): **UNDECIDED**. PANTHER:PTN000575073 propagates mammalian TGN38/TGOLN trans-Golgi localization within PTHR23211:SF0, which also contains M9PFV8; same-subfamily propagation and unresolved direct Rgn localization argue against a confident REMOVE even though the 808-residue fly CTLD protein has no target evidence for TGN38-like residence.
- GO:0030140 trans-Golgi network transport vesicle (IBA): **UNDECIDED**. The same PANTHER:PTN000575073 node propagates mammalian TGN38/TGOLN transport-vesicle residence, but Rgn has no direct evidence for TGN-derived vesicle localization and the SF0 assignment keeps the transfer unresolved rather than demonstrably wrong.
- GO:0030246 carbohydrate binding (IEA): **UNDECIDED**. Several proteins retain this fold without the canonical carbohydrate-binding activity. The exact target has no mapped ligand-binding assay.
- GO:0030246 carbohydrate binding (ISS): **UNDECIDED**. PMID:16475980 directly assays DL1 and discusses Drosophila lectins. It supplies useful family biology but does not establish carbohydrate binding by the long Rgn isoform; target-specific ligand or conserved-binding-site evidence is required.
- GO:0042246 tissue regeneration (IEP): **ACCEPT**. PMID:18485344 reports rgn expression in regenerating blastema cells, matching the tissue-regeneration process established by perturbation evidence in the same paper.
- GO:0042246 tissue regeneration (IMP): **ACCEPT**. The full text of PMID:18485344 maps rgn alleles to CG6014 and reports altered blastema regeneration after genetic perturbation, and the 2026 abstract in PMID:41935796 reports a progenitor-deficiency phenotype in gut epithelial repair. The gene-level process is well supported although the molecular mechanism and isoform contributions remain unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `rgn-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all six GOA rows, the description and core functions against PMID:18485344 (full text), PMID:41935796 (abstract), the falcon deep research, the UniProt record and a new sequence analysis (`rgn-bioinformatics/rgn_architecture.py`, `RESULTS.md`, `rgn_architecture_results.json`). ProtNLM2 output was not consulted.

### Identity
- M9PFV8 (808 aa; FlyBase isoforms B/C) is the longer of the two UniProt products of rgn/CG6014 (FBgn0261258). The other, Q9Y102 (800 aa; isoforms A/D), is identical except that it lacks YVQLISNS (M9PFV8 residues 160-167) inside the CTLD. Both entries are unreviewed (TrEMBL), neither is a fragment, and both share PTHR23211:SF0. The benchmark accession is therefore a full-length gene product, not a fragment. No reviewed canonical entry exists, so the same-gene-canonical rule does not apply.
- Architecture: signal peptide 1-23 (SignalP), CTLD 70-199 (PROSITE PS50041), long charged disordered tail (MobiDB-lite 244-808 in segments). No transmembrane segment: UniProt has no TRANSMEM feature, and a Kyte-Doolittle scan found none after residue 30.

### Evolutionary placement
- PANTHER puts Rgn in PTHR23211 "TGN38" (single subfamily SF0, together with TGOLN2/TGN38). PAINT has a single annotated node, PTN000575073 (taxon Eukaryota), with IBDs for trans-Golgi network and TGN transport vesicle, seeded by the vertebrate TGN38 proteins.
- Rgn lacks both determinants of TGN38 localization: the TM anchor and the cytoplasmic YQRL motif. Local alignment of Rgn to TGOLN2 (score 95) and rat TGN38 (79.5) falls within the composition-matched shuffle distributions (34.5% and 12% of shuffles score as high or higher) and maps to Rgn's charged disordered region. Rgn's CTLD aligns to REG1A (161), REG3A (101) and lectin-galC1 (81) well above every shuffle; these are all PTHR22803 proteins.
- Conclusion: no residue-level support was detected for the TGN38 grouping beyond compositional bias. This is a family-placement concern for PTHR23211 (see the PANTHER review, interpro/panther/PTHR23211/PTHR23211-review.yaml, which marks coherence UNKNOWN). Note that the CTLD similarity to REG proteins also does not make Rgn a REG ortholog. PANTHER separates them, and the McClure et al. "predicted ortholog of mammalian Reg" claim rests on BLAST of the CTLD alone.
- The CTLD keeps its cysteines (74, 91, 174, 190, 198) but lacks the EPN/QPD and WND motifs, and UniProt's PROSITE-ProRule caution says conserved residues are missing.

### Decisions (changes from the previous version)
- GO:0005802 trans-Golgi network (IBA): UNDECIDED -> REMOVE. Propagation is bad for this target because it lacks the TM and sorting determinants, and pairwise similarity to the seeds is not above shuffles.
- GO:0030140 TGN transport vesicle (IBA): UNDECIDED -> REMOVE, for the same reason.
- GO:0030246 carbohydrate binding (IEA, ISS): UNDECIDED -> MARK_AS_OVER_ANNOTATED. The fold is present but lacks the sugar/Ca2+ motifs. The ISS donor DL1 is in a different PANTHER family, and no ligand has been measured.
- GO:0042246 tissue regeneration (IEP, IMP): ACCEPT, unchanged. Supporting quotes were replaced by quotes that state the genetic requirement. GO has no more specific imaginal-disc regeneration term.
- I proposed no NEW terms. Notch-signalling and ISC-maintenance terms from the abstract-only gut paper were not added: the mechanism is unclear, and the paper reads as a necessity phenotype rather than participation.
- Description and core function were rewritten to state the architecture, the two isoforms, the absence of a TM segment and the unknown molecular activity.

### Relative to review next
- By PANTHER subfamily, Rgn's only experimentally characterised relatives are TGOLN2 (human O43493) and the rodent TGN38/Tgoln proteins (PTHR23211:SF0). None has a review in the repo. Given the placement concern above, TGOLN2 is a family member, not a demonstrated ortholog.
- Modules: none found under modules/ that include rgn, TGOLN2 or imaginal-disc regeneration.
