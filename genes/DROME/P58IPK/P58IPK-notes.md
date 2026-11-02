# P58IPK (Q9VHA8): evidence and ProtNLM claim review

P58IPK is a DNAJC3-family cochaperone with tetratricopeptide repeats, an N-terminal signal peptide, and a C-terminal J domain. It assists protein folding in the endoplasmic reticulum through chaperone and unfolded-client interactions. Its secretory targeting is compatible with an ER-lumen cochaperone, while stable ER-membrane attachment is not established.

Exact input: [Q9VHA8](https://www.uniprot.org/uniprotkb/Q9VHA8/entry), 498 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [P58IPK-predictions-source.json](P58IPK-predictions-source.json). Source features: [P58IPK-uniprot.txt](P58IPK-uniprot.txt), with an exact extraction in [P58IPK-sequence-evidence.json](P58IPK-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR051727; DnaJ_C3_Co-chaperones.
DR   InterPro; IPR001623; DnaJ_domain.
DR   InterPro; IPR036869; J_dom_sf.
DR   InterPro; IPR011990; TPR-like_helical_dom_sf.
DR   InterPro; IPR019734; TPR_rpt.
FT   SIGNAL          1..36
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          396..463
FT                   /note="J"
FT                   /evidence="ECO:0000259|PROSITE:PS50076"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | J domain-containing protein | CNN | IPR001623 and the domain feature at residues 396-463 identify a J domain independently of ProtNLM. The name accurately describes architecture without establishing an intrinsic ATPase. |
| Location | Membrane (SL-0162) | UNC | The exact record has a cleavable signal peptide but no retained transmembrane helix. An ER-lumen cochaperone may interact with membrane-associated machinery; no stable membrane localization is established, so the broad membrane claim is unresolved. |
| Location | Endoplasmic reticulum membrane (SL-0097) | UNC | ER targeting is supported but ER membrane and ER lumen are different locations. The J/TPR protein has no retained transmembrane segment in the source record; an ER membrane assignment needs direct association/topology evidence and cannot be validated by the ARBA ER sentence. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0005783 endoplasmic reticulum (IBA): **ACCEPT**. An N-terminal signal peptide and DNAJC3-family J/TPR architecture support the phylogenetically curated ER annotation.
- GO:0005783 endoplasmic reticulum (IEA): **ACCEPT**. The signal peptide and DNAJC3 architecture support ER targeting. The ARBA sentence in UniProt is not treated as experimental localization evidence.
- GO:0012505 endomembrane system (HDA): **KEEP_AS_NON_CORE**. PMID:19317464 is a proteomic localization study; the exact source is abstract-only in the cache. The assignment is retained as compatible high-throughput evidence and does not establish membrane insertion.
- GO:0034975 protein folding in endoplasmic reticulum (IBA): **ACCEPT**. The signal peptide, TPR-repeat substrate-binding architecture, and J domain support the existing IBA role in ER protein folding.
- GO:0051087 protein-folding chaperone binding (IBA): **ACCEPT**. The DNAJC3-family protein contains a J domain at residues 396-463 and TPR repeats. This supports the existing phylogenetic inference of protein-folding-chaperone interaction without calling the protein an ATPase.
- GO:0051787 misfolded protein binding (IBA): **ACCEPT**. The TPR/J architecture supports the existing IBA misfolded-protein-binding inference; binding and delivery to a chaperone are distinct from independent ATP-driven folding.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `P58IPK-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output and prediction-evidence files were not consulted for this section.

### Identity
- Q9VHA8 (498 aa) is the full-length FlyBase product of FBgn0037718 (CG8286). It is not an isoform, fragment or alternative gene model. The only other fly PTHR44140 entry, Q7K3H7, has an identical sequence (LD25575p cDNA; source of the PANTHER family name "LD25575P"). No Swiss-Prot entry exists for the fly gene. [file:DROME/P58IPK/P58IPK-bioinformatics/RESULTS-rereview.md]
- Architecture: signal peptide 1..36 (SignalP), five PROSITE TPR repeats, J domain 396..463 with HPD at 424-426. H424 corresponds to P58 H422, the residue required for the BiP interaction in mouse P58/DNAJC3 [PMID:18923430 "interactions with P58's J-domain, which are mediated by invariant residues BiP R197 and P58 H422"].

### Evolutionary placement (PANTHER 19 tree, PTHR44140)
- New analysis: `P58IPK-bioinformatics/rereview_analysis.py`, output `rereview_output.txt`, summary `RESULTS-rereview.md`.
- Fly P58IPK and vertebrate DNAJC3 are orthologs joined at the Bilateria speciation node PTN000637047. The fly gene is labelled PTHR44140:SF2 and human DNAJC3 SF3 only because the SF3 boundary is drawn at a vertebrate duplication (PTN001531906; DNAJC3 versus teleost dnajc3b/prkri, SF1). SF2 is a grade containing the ancestral nodes and all non-vertebrate members, including yeast JEM1 (a more distant, Opisthokont-level relative; 29% identity vs 45% for DNAJC3).
- All four PAINT IBDs (ER, protein-folding chaperone binding, misfolded protein binding, protein folding in ER) are on the Eukaryota root PTN001941043. The mammalian eIF2-alpha kinase inhibitor activity (protein kinase inhibitor activity on human DNAJC3) was not placed on any ancestral node, a deliberate PAINT omission; it is not transferred.

### Literature
- Deo et al. 2024 (PMID:39242711, full text cached) is the only fly-specific primary study. Overexpressed HA-tagged P58IPK co-immunoprecipitated with HTT103Q-GFP in yeast [PMID:39242711 "HA bands were seen in the input and IP lanes of mutant 103Q with CG5001 and P58IPK whereas the negative controls show no bands in the IP"] and reduced HTT103Q aggregation in yeast, S2 cells and hemocytes. This is overexpression with an artificial cytoplasmic client; used only as corroboration of misfolded-client binding. No NEW process annotation (e.g. negative regulation of protein aggregation) is proposed: it is a heterologous-client overexpression effect, and FlyBase has not annotated from this paper.
- The deep-research claim of "cytoplasmic" localization rests on colocalization of the overexpressed protein with cytoplasmic HTT aggregates; it does not establish endogenous localization and conflicts with the signal peptide. Recorded as a suggested question.

### Annotation decisions (re-review)
- GO:0005783 ER (IBA, IEA): ACCEPT. ER lumen is likely but not shown; PAINT placed the general term (JEM1 is membrane-associated), so no refinement.
- GO:0012505 endomembrane system (HDA): KEEP_AS_NON_CORE. As precise as the proteomics evidence allows.
- GO:0034975 protein folding in ER (IBA): ACCEPT.
- GO:0051087 protein-folding chaperone binding (IBA): ACCEPT; core.
- GO:0051787 misfolded protein binding (IBA): ACCEPT; core.
- Changes vs previous version: description and core functions rewritten with orthology grounding; supporting evidence now cites the ortholog mechanism paper (PMID:18923430), the fly study (PMID:39242711) and the new tree analysis instead of only InterPro lines; status DRAFT -> COMPLETE. No action changed.

### Relative and family
- Closest characterised relative by tree placement: human DNAJC3 (Q13217), review at genes/human/DNAJC3/DNAJC3-ai-review.yaml (status COMPLETE).
- PANTHER family review interpro/panther/PTHR44140/PTHR44140-review.yaml lists P58IPK under SF2, agreeing with UniProt. It does not note that SF2 is paraphyletic with respect to SF3/SF1; this is a description gap rather than a placement disagreement.
- No module under modules/ mentions DNAJC3/P58IPK/PTHR44140.
