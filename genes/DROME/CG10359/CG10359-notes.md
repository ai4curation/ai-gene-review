# CG10359 (B7Z0B2): evidence and ProtNLM claim review

CG10359 is a 485-residue secretory-pathway protein with a fibrinogen-like C-terminal domain. Its architecture supports an extracellular interaction role, while ligand specificity, membrane association, and receptor-mediated signaling remain uncertain.

Exact input: [B7Z0B2](https://www.uniprot.org/uniprotkb/B7Z0B2/entry), 485 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG10359-predictions-source.json](CG10359-predictions-source.json). Source features: [CG10359-uniprot.txt](CG10359-uniprot.txt), with an exact extraction in [CG10359-sequence-evidence.json](CG10359-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR036056; Fibrinogen-like_C.
DR   InterPro; IPR014716; Fibrinogen_a/b/g_C_1.
DR   InterPro; IPR002181; Fibrinogen_a/b/g_C_dom.
DR   InterPro; IPR050373; Fibrinogen_C-term_domain.
FT   SIGNAL          1..23
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          263..477
FT                   /note="Fibrinogen C-terminal"
FT                   /evidence="ECO:0000259|PROSITE:PS51406"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Fibrinogen C-terminal domain-containing protein | CNN | PROSITE PS51406 and InterPro IPR002181 independently identify the fibrinogen C-terminal domain at residues 263-477. The domain name is accurate without implying a vertebrate coagulation function. |
| Location | Secreted (SL-0243) | CNN | A Phobius signal peptide at residues 1-23 together with the extracellular fibrinogen-like domain supports secretion. Existing curated extracellular-matrix localization is compatible; secretion does not independently establish matrix binding or a GPCR interaction. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0001664 G protein-coupled receptor binding (ISS): **UNDECIDED**. The ISS assertion is a curated transfer rather than an experiment on this protein. Its fibrinogen-like domain and signal peptide support extracellular biology but do not identify a GPCR partner or establish conserved receptor binding.
- GO:0007186 G protein-coupled receptor signaling pathway (ISS): **UNDECIDED**. The sequence supports a secretory fibrinogen-domain protein but does not establish the receptor or pathway represented by this ISS annotation.
- GO:0008061 chitin binding (ISS): **UNDECIDED**. The extracellular fold permits diverse ligands; target-specific binding or a resolved transfer from a characterized chitin-binding ortholog is needed.
- GO:0016020 membrane (ISS): **UNDECIDED**. The human FIBCD1 source is a type 2 transmembrane receptor, whereas fly CG10359 has a predicted signal peptide and soluble FReD region. Peripheral membrane binding remains possible, but the source/target architecture mismatch leaves the ISS transfer unresolved.
- GO:0031012 extracellular matrix (IBA): **MODIFY** to GO:0005576 extracellular region. PTN000441162 puts `GO:0031012` at a taxon-unrestricted PTHR19143 node, and the cached evidence does not provide the tree divergence or loss evidence needed for a confident propagation failure. PMID:42009678 now supports CG10359/B7Z0B2 as a circulating larval secretome protein assigned to muscle, heart, wing disc and neurons, with a predicted CG10359-Mew interaction in imaginal discs; this supports a broad extracellular placement but not confirmed matrix residence.

## Research assessment

The Falcon report identifies PMID:24675716 as a primary CG10359 lead. The full text describes CG10359 as a predicted angiopoietin homolog and reports a negative deficiency result in the tested protection assay; it does not establish a receptor-binding function. The peer-reviewed PMID:42009678 secretome paper replaces the earlier preprint-only evidence, explicitly states that retained isoform B7Z0B2 was identified from muscle, heart, wing disc and neurons, and predicts muscle-secreted CG10359 binding to imaginal-disc Mew. This supports secretion into larval blood and a possible extracellular receptor interaction, not stable extracellular-matrix residence or receptor specificity.

Provider output: [CG10359-deep-research-falcon.md](CG10359-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-09-28 IBA rereview

Read the cached full texts for PMID:24675716, PMID:35916241, and PMID:42009678 and rechecked the sole CG10359 IBA against `interpro/panther/PTHR19143/PTHR19143-paint.tsv`. The `GO:0031012` row traces to `PANTHER:PTN000441162`, a taxon-unrestricted PAINT matrix-localization node. Because current target evidence supports secretion and extracellular interaction but not matrix retention, and because the PAINT row itself is not refuted by branch-length or target-loss evidence, the IBA is now a `MODIFY` to the broader GO:0005576 extracellular region with `TERM_SCOPING_PROBLEM`.

No `NEW` annotations were added. The 2022 dFibcd1 paper is perturbational and compares the fly FReD structurally to vertebrate FIBCD1, but the CS-4S/GAG binding assays are on vertebrate FIBCD1. The 2026 secretome map identifies CG10359/B7Z0B2 as a circulating larval blood protein and argues for secretion, which is still broader and less specific than the extracellular-matrix component propagated by PAINT.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing GOA row, the description and core functions were re-examined against the cached
literature (PMID:24675716, PMID:35916241, PMID:42009678; donor papers PMID:19710473 for FIBCD1 (already cached) and newly cached
PMID:21037097 for FCN1), the PANTHER 19.0 classification and the PTHR19143 PAINT file. No ProtNLM2 output was
opened or used.

### Identity of the benchmark accession

B7Z0B2 is one of four unreviewed UniProt entries for FBgn0035452; there is no Swiss-Prot entry. It is the longest
product (485 aa). B7Z0B3 (459 aa), Q9VZN7 (460 aa) and Q95S38 (460 aa, cDNA) lack a 26-residue internal segment
(B7Z0B2 residues 144-169) upstream of the FReD; all keep the signal peptide and the single FReD, and none has a
transmembrane segment [file:DROME/CG10359/CG10359-bioinformatics/RESULTS-rereview.md, "B7Z0B2 is therefore a
full-length isoform of the gene, not a fragment;"]. B7Z0B2 is the PANTHER/GOA representative and is the isoform
detected in the larval secretome [PMID:42009678 "We removed B7Z0B3 (CG10359) from muscle, because B7Z0B2 (CG10359)
was identified from muscle/heart/wingdisc/neurons."]. Not a fragment or problematic gene model.

### Evolutionary placement

- PANTHER: PTHR19143:SF327 "FI21813P1-RELATED", members 8 fly paralogs + 1 C. elegans protein, none characterised.
- Human FIBCD1 (Q8N539) is in SF45 (vertebrate only); human FCN1 (O00602) is in SF377.
- FReD-only MAFFT/NJ tree (`CG10359-bioinformatics/fred_tree_rereview.py`, new files only; nothing pre-existing
  overwritten): CG10359 groups with fly SF327 paralogs Q8IRM2/Q9W302; FReD identity to FIBCD1 41%, about the same
  as MFAP4/FGL1 (40%), FCN1 38%. No ortholog-level link to FIBCD1 or ficolins. Tree has no bootstrap; deep order
  unresolved.
- PAINT: only IBD reaching CG10359 is the root ECM node PTN000441162. The signaling-receptor-binding IBD
  (PTN000441539) is chordate-restricted and the cell-matrix adhesion IBD (PTN009036378) does not reach CG10359;
  treated as deliberate.
- PMID:35916241 calls CG10359 a "potential orthologue" of FIBCD1, based on InterPro domain similarity and AlphaFold
  fold comparison, not a phylogeny. This disagrees with PANTHER, which separates them; the subfamily split was
  followed.

### Annotation decisions (changes from the 2026-09-28 state)

- GO:0001664 GPCR binding (ISS from FCN1): UNDECIDED -> REMOVE. Donor function is M-ficolin docking on GPR43
  [PMID:21037097]; ficolin-specific, cross-subfamily, CG10359 lacks the collagen-like region.
- GO:0007186 GPCR signaling pathway (ISS from FCN1): UNDECIDED -> REMOVE. Same donor/basis; the only receptor
  proposed from fly data is integrin alpha Mew [PMID:42009678]; Tie-ligand test negative [PMID:24675716].
- GO:0008061 chitin binding (ISS from FIBCD1): UNDECIDED -> MARK_AS_OVER_ANNOTATED. Plausible in insects but
  only a cross-subfamily domain transfer; no binding assay on CG10359; pocket not examined.
- GO:0016020 membrane (ISS from FIBCD1): UNDECIDED -> REMOVE. FIBCD1 membrane location comes from its type II TM
  anchor [PMID:19710473], which no CG10359 isoform has; CG10359 is a secreted hemolymph protein.
- GO:0031012 ECM (IBA, PTN000441162): MODIFY -> GO:0005576 extracellular region retained (TERM_SCOPING_PROBLEM).
- Core function: added a location-only entry (extracellular region) with no molecular_function, since no activity
  is established. RNAi NMJ/climbing phenotypes [PMID:35916241] are organismal and are not used for process terms.
- No NEW annotations. The Mew interaction is a FlyPhoneDB2 prediction and does not justify an integrin-binding term.

### Relative to review next

Not a fragment, so the canonical-product rule does not apply. SF327 has no characterised member, and no fly
paralog in PTHR19143 other than scabrous (SF444, distant) has experimental data. The closest characterised
relative that has been explicitly proposed as the ortholog and is the donor of the chitin/membrane transfers is
human FIBCD1 (Q8N539, SF45): a family member, not a PANTHER-supported ortholog. No FIBCD1 review exists in the repo.

### Family review and modules

`interpro/panther/PTHR19143/PTHR19143-review.yaml` lists B7Z0B2 under SF327; placement agrees with PANTHER. Its
SF327 text discusses only the angiopoietin-like framing (PMID:24675716) and does not mention the FIBCD1-orthology
claim of PMID:35916241 or the secretome data. modules/ contains no module for CG10359 (`fibrinolysis.yaml` and
`coagulation_cascade.yaml` mention fibrinogen but concern the vertebrate clotting proteins and do not apply).
