# CG42404 (Q9VFA8): evidence and ProtNLM claim review

CG42404 is a 1133-residue VWFC-domain protein with a predicted membrane-spanning segment near its N terminus. Its extracellular-domain-like architecture and membrane association are compatible with a cell-surface interaction protein, but ligand specificity, topology, and biological activity are unresolved.

Exact input: [Q9VFA8](https://www.uniprot.org/uniprotkb/Q9VFA8/entry), 1133 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG42404-predictions-source.json](CG42404-predictions-source.json). Source features: [CG42404-uniprot.txt](CG42404-uniprot.txt), with an exact extraction in [CG42404-sequence-evidence.json](CG42404-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR042378; IDD.
DR   InterPro; IPR001007; VWF_dom.
FT   TRANSMEM        103..125
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   DOMAIN          27..92
FT                   /note="VWFC"
FT                   /evidence="ECO:0000259|PROSITE:PS50184"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | VWFC domain-containing protein | CNN | The VWFC domain at residues 27-92 is supported independently by PROSITE PS50184 and InterPro IPR001007. This validates the domain name without specifying a von Willebrand factor function. |
| Location | Membrane (SL-0162) | CNN | The Phobius transmembrane segment at residues 103-125 supports the broad membrane location already represented by curated IBA. It does not establish secretion as a soluble protein. |
| Keyword | Signal (KW-0732) | UNC | The source record contains an internal transmembrane segment but no cleavable signal-peptide feature. A signal anchor can route a membrane protein without a cleaved N-terminal signal peptide; the emitted Signal keyword requires a resolved N terminus and topology. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. A VWFC domain does not specify a ligand or a receptor activity for this fly product.
- GO:0005575 cellular_component (ND): **MODIFY**. The exact record carries a Phobius transmembrane segment at residues 103-125 and a curated IBA membrane annotation. The broad membrane term is supported without identifying a particular organelle.
- GO:0008150 biological_process (ND): **ACCEPT**. Domain and topology evidence do not establish a developmental or signaling pathway.
- GO:0016020 membrane (IBA): **ACCEPT**. A predicted membrane-spanning segment at residues 103-125 is consistent with the existing phylogenetically curated membrane annotation; specific topology and tissue function are unresolved.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG42404-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all four GOA rows, the description and core functions without consulting any ProtNLM2 output.

### Identity
- Q9VFA8 (1133 aa, TrEMBL, PE 4) is the full-length product of FBgn0259823/CG42404 and the only UniProt entry of that length for the gene. The other two UniProt entries for the gene are short fragments/alternative products: Q8MRY6 (145 aa, cDNA SD12744p) and A0A0C4DHG7 (105 aa). The benchmark accession is therefore the canonical product, not an isoform or fragment.
- Position 106 is an unknown residue (X) inside the Phobius TM helix (103-125), a sequence ambiguity in the deposited record.
- The first ~26 residues are hydrophobic and directly precede the VWFC domain, but no SIGNAL feature is annotated; topology is unresolved.

### Evolutionary placement
- PANTHER PTHR15256 (INTEGRAL MEMBRANE PROTEIN DGCR2/IDD), subfamily SF6, the same (only) subfamily as human DGCR2 P98153 and mouse Dgcr2 P98154 (interpro/panther/PTHR15256/PTHR15256-entries.csv; UniProt DR PANTHER line).
- New analysis `CG42404-bioinformatics/compare_dgcr2_rereview.py` / `RESULTS-rereview.md`: fly residues 28-200 align to human DGCR2 270-455 at 34.7% identity, covering VWFC, TM, a basic juxtamembrane segment (RLRQRK vs RLRQRR) and a PPPYE (PPxY-type) motif. The fly protein lacks the LDL-A and C-type lectin domains of vertebrate DGCR2, and has a ~900-residue fly-specific disordered C-terminal extension.
- PAINT node PTN000391897 propagates only GO:0016020 membrane (donor MGI:892866 mouse Dgcr2, experimental membrane from PMID:8630060 [PMID:8630060 "it encodes membrane-bound C-type lectin"]). The vertebrate process terms (human DGCR2 cognition IMP; mouse response to xenobiotic IDA) were not propagated by PAINT; treated as a deliberate decision.
- Mouse Dgcr2 knockdown impairs radial migration of cortical projection neurons and DGCR2 associates with the Reelin complex [PMID:29305086 "we identified Dgcr2 as a novel member of the Reelin complex"]. These are not transferred to the fly protein.

### Literature
- Falcon deep research found only inclusion of CG42404 in wing gain-of-function/RNAi screening tables (Cruz 2009, Molnar 2012) with no specific phenotype; no mechanistic study.

### Decisions
- GO:0003674 ND: ACCEPT (no activity known; no MF propagated by PAINT).
- GO:0005575 ND: MODIFY -> GO:0016020 membrane (TM helix + IBA).
- GO:0008150 ND: ACCEPT (no process established; vertebrate DGCR2 neural-migration roles not transferred).
- GO:0016020 IBA: ACCEPT (target inside SF6 clade, retains the TM helix).
- Description rewritten to state family membership, the conserved VWFC-TM-PPxY core and the missing LDL-A/CTLD modules. Core function: membrane-located, activity unknown, with a BIOLOGY knowledge gap.

### Relative to review next
- Mouse Dgcr2 (P98154), same PANTHER subfamily SF6 and the PAINT donor (MGI:892866); no review exists in genes/mouse or genes/human (human DGCR2 P98153 also unreviewed).
- PANTHER family review interpro/panther/PTHR15256/PTHR15256-review.yaml agrees on subfamily placement (SF6 lists Q9VFA8 as representative). No disagreement. No module in modules/ references DGCR2/PTHR15256 or CG42404.
