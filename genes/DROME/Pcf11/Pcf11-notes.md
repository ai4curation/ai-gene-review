# Pcf11 (C0P8M6): evidence and ProtNLM claim review

The C0P8M6 Pcf11 record encodes an 86-residue protein consisting largely of a CTD-interacting domain. Full-length Drosophila Pcf11 participates in RNA polymerase II transcription termination, but the activities and intracellular distribution of this short translation product are unresolved.

Exact input: [C0P8M6](https://www.uniprot.org/uniprotkb/C0P8M6/entry), 86 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Pcf11-predictions-source.json](Pcf11-predictions-source.json). Source features: [Pcf11-uniprot.txt](Pcf11-uniprot.txt), with an exact extraction in [Pcf11-sequence-evidence.json](Pcf11-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR006569; CID_dom.
DR   InterPro; IPR008942; ENTH_VHS.
DR   InterPro; IPR045154; PCF11-like.
FT   DOMAIN          11..86
FT                   /note="CID"
FT                   /evidence="ECO:0000259|PROSITE:PS51391"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | CID domain-containing protein | CNN | IPR006569 identifies a CID domain at residues 11-86 in the exact 86-residue product. This modest domain claim is supported without transferring full-length Pcf11 activity. |
| Location | Cytoplasm (SL-0086) | UNC | Cytoplasmic localization of the 86-residue product is not demonstrated. Full-length Pcf11 localization and function cannot settle the compartment of this exact short record. |
| Location | Nucleus (SL-0191) | UNC | Nuclear residence is plausible for a CID-containing Pcf11-derived product but remains unresolved for this 86-residue sequence. A mapped construct or isoform localization experiment is needed. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0000993 RNA polymerase II complex binding (IEA): **UNDECIDED**. A CID hit spanning residues 11-86 supports CTD-interaction potential but does not demonstrate RNA polymerase II complex binding by the exact 86-residue product.
- GO:0003723 RNA binding (IDA): **UNDECIDED**. PMID:16387654 concerns Pcf11 biochemical activity. The exact benchmark product is only 86 residues and requires construct or isoform mapping before the experimental RNA-binding result can be attributed to it.
- GO:0003729 mRNA binding (IEA): **UNDECIDED**. The truncated domain-bearing record cannot be assumed to retain full-length Pcf11 RNA-binding activity; exact-product or mapped-construct evidence is needed.
- GO:0006369 termination of RNA polymerase II transcription (IEA): **UNDECIDED**. A single 86-residue CID-containing product may not execute the full-length protein function. This is an isoform-resolution limitation and not evidence against the experimentally established gene-level role.
- GO:0010467 gene expression (IEA): **UNDECIDED**. The broad computational annotation cannot establish that the 86-residue product is produced or functionally contributes to gene expression in vivo.
- GO:0031124 mRNA 3'-end processing (IEA): **UNDECIDED**. The source sequence lacks most of the full-length Pcf11 architecture; domain presence does not establish assembly into the processing machinery.
- GO:0032991 protein-containing complex (IEA): **UNDECIDED**. The 86-residue sequence has a CID-family segment but no exact-product demonstration of complex incorporation.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Pcf11-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Identity of the benchmark accession

- C0P8M6 (cDNA MIP05908p, 86 aa, PE 2) is identical in sequence to E1JH69, "Pcf11 cleavage and polyadenylation factor subunit, isoform C" (86 aa). It is the short Pcf11-RC product, not the canonical gene product. See `Pcf11-bioinformatics/RESULTS-rereview.md` (new script `compare_isoforms_rereview.py`).
- It shares only residues 1-62 with the 573-aa RB product (Q8IGR2) and the 1953-aa long product (A1Z9W4, reference proteome). Residues 63-86 are a unique tail. The CID spans 11-146 in the longer products, so C0P8M6 keeps about 38% of it and lacks every C-terminal region (RNA-binding zinc-finger region, Cbc/Clp1-binding region).
- Gallicchio et al. 2024 [PMID:39111825 "PCF11 has a CID (Pol II C-terminal binding domain) present in both the PCF11-long and the 63 kDa PCF11-RB isoforms but only partially present in the short protein encoded by PCF11-RC."] and [PMID:39111825 "no protein product corresponding to PCF11-RC was observed despite a seemingly high level of the PCF11-RC transcript isoform detected by snRNA-seq of Drosophila testis tissue"].
- No reviewed (Swiss-Prot) Drosophila Pcf11 exists. The canonical gene-centric product is A1Z9W4 (1953 aa, UP000000803). It has no review in the repo, so it is the relative to review next (genes/DROME/Pcf11__A1Z9W4).

### Evolutionary placement

- All Drosophila Pcf11 entries, human PCF11 (O94913), mouse Pcf11 (G3X9Z4) and yeast PCF11 (P39081) fall in PANTHER PTHR15921:SF3. They are orthologs in one subfamily, so family-level functions (CTD binding, RNA binding by the zinc fingers, CFII with Clp1/Cbc, termination) are inherited by the full-length fly protein. The question for C0P8M6 is not subfamily placement but domain truncation.
- No IBA rows exist for C0P8M6. The family review `interpro/panther/PTHR15921/PTHR15921-review.yaml` agrees with SF3 placement and already cautions that the 86-residue product cannot be assumed to carry full-length functions. There is no disagreement. One minor point: its sole representative member is this fragment rather than a full-length protein.
- No module in `modules/` references Pcf11 or PTHR15921.

### Changes to annotation actions

- The four InterPro2GO rows (RNA polymerase II complex binding, mRNA binding, termination of Pol II transcription, mRNA 3'-end processing) and the two ARBA rows (gene expression, protein-containing complex) changed from UNDECIDED to MARK_AS_OVER_ANNOTATED. Each is true of the gene, but the family signature is being transferred to a product that lacks the structural basis for the activity and has not been detected as a protein.
- The RNA binding IDA row (PMID:16387654, FlyBase gene-level) stays UNDECIDED. The experimental result is valid for the gene and is not second-guessed, but it cannot be attributed to this exact product.
- Removed the UniProt DR/FT quotes as row support, because they restate classification. Replaced them with the Genes Dev paper and the new isoform comparison. The UniProt reference is kept, with a note.
- The description was rewritten to state the isoform identity. core_functions is left empty on purpose: no activity can be assigned to the RC product. Added one BIOLOGY knowledge gap (is RC translated?) and a matching experiment.
- Newly cached: PMID:39111825, PMID:22690379, PMID:40896257, PMID:40015272. The last two are not cited.
