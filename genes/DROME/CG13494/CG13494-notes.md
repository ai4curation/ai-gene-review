# CG13494 (Q8MZA7): evidence and ProtNLM claim review

CG13494 is a 120-residue protein with a predicted transmembrane helix at residues 37-61. It is a plausible small membrane protein whose molecular activity and cellular role are unresolved.

Exact input: [Q8MZA7](https://www.uniprot.org/uniprotkb/Q8MZA7/entry), 120 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG13494-predictions-source.json](CG13494-predictions-source.json). Source features: [CG13494-uniprot.txt](CG13494-uniprot.txt), with an exact extraction in [CG13494-sequence-evidence.json](CG13494-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
FT   TRANSMEM        37..61
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein is suitably nonspecific but contains no testable functional hypothesis. |
| Location | Membrane (SL-0162) | COR | The 25-residue predicted transmembrane segment at residues 37-61 supports a membrane-associated product. This is sequence-based inference rather than measured localization and does not identify the membrane or topology. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG13494-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Identity
- Q8MZA7 is the only UniProt entry for FlyBase FBgn0034671 (UniProt REST `xref:flybase-FBgn0034671` returns Q8MZA7 alone, 120 aa, unreviewed). Q9W2B6 is a merged secondary accession. The benchmark accession is therefore the canonical full-length product: not an isoform, fragment or alternative gene model. OMA records it as the main isoform (transcript FBtr0071733).

### Literature
- No gene-specific publication. The falcon deep research ran exact searches for CG13494, FBgn0034671, Q8MZA7, AT17606p and AAM29281.1 and found none [file:DROME/CG13494/CG13494-deep-research-falcon.md "found **no gene-specific mechanistic paper or exact mention**"].
- UniProt Bgee line: "Expressed in mid-late elongation-stage spermatid (Drosophila) in testis and 21 other cell types or tissues" (a high-throughput expression summary, not functional evidence).

### Sequence and evolution (new analysis: CG13494-bioinformatics/analyze_rereview.py, RESULTS-rereview.md, results-rereview.json)
- Architecture: Ser/Thr-rich residues 1-36, Phobius TM helix 37-61, then a Gly/Cys/Asp-rich low-complexity tail (62-120: Gly 35.6%, Cys 28.8%, Asp 16.9%). 20 Cys in 120 residues.
- InterPro: no member-database match (API HTTP 204), so no PANTHER family or subfamily, and no PAINT node.
- Pfam CYSTM (PF12734, TM + Cys-rich module) does not match (score -42.3 bits, E = 1.0); the resemblance is compositional.
- eggNOG KOG4726 (UniProt xref) also contains human keratin-associated proteins and CRCT1, which is a Cys-rich low-complexity grouping, not evidence of homology. No function transferred.
- OMA HOG:F0655449 is rooted at the melanogaster group; 1:1 orthologs only in D. ficusphila, erecta, sechellia, simulans, yakuba and suzukii. This is a lineage-restricted, probably young, testis-expressed gene.

### Annotation decisions
- GOA has no annotation rows for Q8MZA7, so there is nothing to re-assess.
- No NEW annotations. Membrane (GO:0016020) would rest only on the Phobius TM prediction; I left it as a suggested question rather than asserting it. No MF or BP can be transferred because there is no characterised homolog.
- Description rewritten to cover architecture, lineage restriction and expression. core_functions stays empty, and a gene-level WHOLLY_DARK knowledge gap was added.

### Relative / family / modules
- No characterised relative exists (no PANTHER family, no ortholog outside the melanogaster group), so relation is none_found.
- No PANTHER family review is relevant (no PANTHER assignment). No modules/ or gocams/ entries mention CG13494, Q8MZA7 or FBgn0034671.
