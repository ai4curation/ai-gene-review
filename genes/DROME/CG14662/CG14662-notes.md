# CG14662 (Q9VN74): evidence and ProtNLM claim review

CG14662 is a 550-residue leucine-rich-repeat protein with two predicted hydrophobic membrane-spanning segments. It is a plausible membrane interaction protein, while ligand recognition, membrane topology, and physiological function remain unresolved.

Exact input: [Q9VN74](https://www.uniprot.org/uniprotkb/Q9VN74/entry), 550 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG14662-predictions-source.json](CG14662-predictions-source.json). Source features: [CG14662-uniprot.txt](CG14662-uniprot.txt), with an exact extraction in [CG14662-sequence-evidence.json](CG14662-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR032675; LRR_dom_sf.
FT   TRANSMEM        29..50
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   TRANSMEM        421..447
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein supplies no testable activity claim. The LRR fold suggests an interaction scaffold without specifying ligands. |
| Location | Membrane (SL-0162) | COR | Two independently called Phobius transmembrane segments support the broad membrane hypothesis. The result remains a sequence-based localization inference; it does not identify topology or organelle residence. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. A leucine-rich-repeat scaffold can mediate many interactions and does not establish a specific receptor or ligand-binding activity.
- GO:0005575 cellular_component (ND): **UNDECIDED**. Two Phobius hydrophobic segments at residues 29-50 and 421-447 suggest membrane insertion. The source GOA unknown-component placeholder and sequence-level inference do not resolve localization or topology experimentally.
- GO:0008150 biological_process (ND): **ACCEPT**. Neither an LRR domain nor membrane-spanning architecture identifies the pathway in which this protein acts.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG14662-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: all three existing (ND) annotations, the description and the core functions were re-examined without consulting any ProtNLM2 output.

**Identity.** Q9VN74 is the single annotated product of CG14662 (FBgn0037291), 550 aa, sequence version 1, and the only UniProt entry for the gene. It is not a fragment, isoform or alternative gene model; Dolan et al. 2007 report the same 550-aa length [PMID:17868438 "CG14662550SS, 6LRR, TM"]. UniProt lists the gene name as CT34440 (an old annotation id); the folder keeps the FlyBase symbol CG14662.

**Literature.** The Dolan et al. 2007 full text (cached, PMC2235866) is the only peer-reviewed source naming the gene. It is a computational catalogue entry in the LRR_Only singleton table, where singletons are described as [PMID:17868438 "genes with no recognizable orthologue in the other species (fly or mouse) and no recognizable paralogue in their own species"]. The falcon report's other source (2024 dissertation) mentions CG14662 only as a neighbour of the CG2022 GWAS hit; not used.

**Sequence analysis** (new script `CG14662-bioinformatics/sequence_features_rereview.py`, results in `RESULTS-rereview.md`): two hydrophobic segments (28-54, 418-448) matching Phobius TM 29-50 and 421-447; a 28-residue N-terminus with 9 K/R before the first segment (suggests an uncleaved signal anchor, N-in, rather than Dolan's cleaved SS); all 7 N-glycosylation sequons between the two segments; LRR superfamily region 35-282; Ser/Thr-rich disordered stretch 291-336 (48% S+T); Cys-rich juxtamembrane region 337-420 (10 Cys); 103-residue cytoplasmic tail with YxxΦ motifs at 475 and 546; no TIR or catalytic domain.

**Evolutionary placement.** InterPro reports a weak PANTHER HMM match (PTHR24365 TOLL-LIKE RECEPTOR, subfamily SF541 "PROTEIN TOLL-RELATED", residues 190-452, score 0.032), but Q9VN74 is absent from PANTHER 19.0's own fruit-fly classification (SF541 fly members there: Tl, Tehao). No PAINT/IBA annotation exists. OrthoDB places CG14662 in one orthogroup restricted to Brachycera (63 genes, 62 species, identical from Eukaryota to Brachycera level). No ortholog or paralog with experimental characterisation was identified by phylogenetic placement; Toll/Tehao functions are not transferred (no TIR domain, placement not supported by PANTHER classification). No PANTHER family review exists under interpro/panther/PTHR24365/ (only metadata and an entries listing), so there is no subfamily-placement disagreement to report beyond the HMM-vs-classification discrepancy noted above. No module in modules/ includes this gene; modules/dmel_toll_signaling.yaml is not applicable.

**Annotation decisions (revised).**
- GO:0003674 molecular_function (ND): ACCEPT (unchanged). No activity is known.
- GO:0005575 cellular_component (ND): MODIFY to GO:0016020 membrane (was UNDECIDED). Two independently recovered TM segments with glycosylation sequons in the intervening region support integral membrane residence. Plasma membrane is not asserted because no localisation data exist.
- GO:0008150 biological_process (ND): ACCEPT (unchanged).

**Core functions.** Left empty: no molecular function can be asserted. Added a BIOLOGY knowledge gap, suggested questions (signal anchor vs signal peptide; ligand; meaning of the PANTHER HMM hit) and experiments (endogenous tagging/topology, null allele, interaction screen). The description was rewritten as a standalone summary of the predicted architecture and the absence of functional data.

**Relative.** none_found: no characterised ortholog (orthogroup confined to Brachycera) and no characterised paralog by phylogenetic placement (Dolan singleton; PANTHER classification omits the protein).
