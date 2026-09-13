# rgn (M9PFV8): evidence and ProtNLM claim review

Regeneration is a secretory-pathway C-type-lectin-domain protein implicated in imaginal-disc regeneration. Genetic perturbation affects blastema formation and growth, while its ligand specificity and the relationship between the 808-residue isoform and its inferred trans-Golgi localization remain unresolved.

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

## Annotation decisions

- GO:0005802 trans-Golgi network (IBA): **UNDECIDED**. The IBA is a curated phylogenetic assertion. The 808-residue record contains an N-terminal signal peptide and a C-type lectin domain; those features establish secretory-pathway compatibility but do not distinguish soluble secretion from Golgi residence.
- GO:0030140 trans-Golgi network transport vesicle (IBA): **UNDECIDED**. A signal peptide and lectin fold do not identify a trans-Golgi transport vesicle. No exact-isoform localization experiment or resolved ancestral assertion is available in the inspected evidence.
- GO:0030246 carbohydrate binding (IEA): **UNDECIDED**. Several proteins retain this fold without the canonical carbohydrate-binding activity. The exact target has no mapped ligand-binding assay.
- GO:0030246 carbohydrate binding (ISS): **UNDECIDED**. PMID:16475980 directly assays DL1 and discusses Drosophila lectins. It supplies useful family biology but does not establish carbohydrate binding by the long Rgn isoform; target-specific ligand or conserved-binding-site evidence is required.
- GO:0042246 tissue regeneration (IEP): **KEEP_AS_NON_CORE**. PMID:18485344 reports rgn expression in regenerating blastema cells. Expression alone does not define a molecular function; the accompanying genetic evidence supports the biological role.
- GO:0042246 tissue regeneration (IMP): **ACCEPT**. The full text of PMID:18485344 maps rgn alleles to CG6014 and reports altered blastema regeneration after genetic perturbation. The gene-level process is well supported although the molecular mechanism and isoform contributions remain unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `rgn-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
