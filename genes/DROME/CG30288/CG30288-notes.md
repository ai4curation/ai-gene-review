# CG30288 (Q8IRK6): evidence and ProtNLM claim review

CG30288 is a predicted secreted S1-family serine endopeptidase. Its 282-residue sequence has an N-terminal signal peptide and retains the annotated histidine-aspartate-serine catalytic triad. Proteolytic potential is supported, while its preferred substrate and physiological role remain unresolved.

Exact input: [Q8IRK6](https://www.uniprot.org/uniprotkb/Q8IRK6/entry), 282 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG30288-predictions-source.json](CG30288-predictions-source.json). Source features: [CG30288-uniprot.txt](CG30288-uniprot.txt), with an exact extraction in [CG30288-sequence-evidence.json](CG30288-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR009003; Peptidase_S1_PA.
DR   InterPro; IPR001314; Peptidase_S1A.
DR   InterPro; IPR051487; Ser/Thr_Proteases_Immune/Dev.
DR   InterPro; IPR001254; Trypsin_dom.
DR   InterPro; IPR033116; TRYPSIN_SER.
FT   SIGNAL          1..23
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          43..275
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   ACT_SITE        83
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        132
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        225
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
```

At the annotated catalytic positions, direct indexing of the exact sequence gives: H83, D132, S225. These positions come from PROSITE features, not a new alignment; no substrate preference or assay result is inferred.

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Peptidase S1 domain-containing protein | CNN | The peptidase S1 domain at residues 43-275 is independently supported by PROSITE PS50240 and InterPro IPR001254. The name is a defensible structural assignment without substrate specificity. |
| Location | Secreted (SL-0243) | CNN | The predicted cleavable SignalP signal peptide and absence of a retained transmembrane segment support secretion; this is consistent with the existing phylogenetically curated extracellular annotation. |

## Literature evidence

- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad”

## Annotation decisions

- GO:0004252 serine-type endopeptidase activity (IBA): **ACCEPT**. The exact sequence contains the annotated H83 D132 S225 triad in its S1 domain; the IBA is consistent with this intact catalytic architecture.
- GO:0004252 serine-type endopeptidase activity (IEA): **ACCEPT**. PROSITE identifies an S1 domain with the retained annotated catalytic residues H83 D132 S225. This does not establish the narrower chymotrypsin substrate preference.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:30367934 classifies Drosophila serine proteases using the H-D-S triad and gene models. The exact source retains the annotated catalytic triad; no biochemical substrate specificity is inferred.
- GO:0005576 extracellular region (IBA): **ACCEPT**. SignalP predicts a cleavable signal peptide at residues 1-23 and no retained transmembrane segment is annotated. This architecture supports the curated IBA extracellular location.
- GO:0006508 proteolysis (IBA): **ACCEPT**. The intact S1 catalytic architecture supports broad proteolysis; the physiological substrate and tissue context remain unknown.
- GO:0006508 proteolysis (IEA): **ACCEPT**. A retained H-D-S triad supports a catalytic rather than merely fold-homologous S1 protein.
- GO:0008233 peptidase activity (IEA): **MODIFY**. The S1 domain and annotated H-D-S triad support serine-type endopeptidase activity.
- GO:0016787 hydrolase activity (IEA): **MODIFY**. S1 catalytic architecture supports serine-type endopeptidase activity.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG30288-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
