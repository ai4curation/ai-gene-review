# CG17404 (Q9VGC0): evidence and ProtNLM claim review

CG17404 is a predicted secreted S1-family serine endopeptidase also known as SP149. Its catalytic histidine-aspartate-serine triad is retained, supporting proteolytic potential. Chymotrypsin-like substrate preference and specific equivalence to mammalian CTRL remain unresolved.

Exact input: [Q9VGC0](https://www.uniprot.org/uniprotkb/Q9VGC0/entry), 275 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG17404-predictions-source.json](CG17404-predictions-source.json). Source features: [CG17404-uniprot.txt](CG17404-uniprot.txt), with an exact extraction in [CG17404-sequence-evidence.json](CG17404-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR009003; Peptidase_S1_PA.
DR   InterPro; IPR001314; Peptidase_S1A.
DR   InterPro; IPR051487; Ser/Thr_Proteases_Immune/Dev.
DR   InterPro; IPR001254; Trypsin_dom.
DR   InterPro; IPR018114; TRYPSIN_HIS.
DR   InterPro; IPR033116; TRYPSIN_SER.
FT   SIGNAL          1..20
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          35..274
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   ACT_SITE        80
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        124
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        225
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
```

At the annotated catalytic positions, direct indexing of the exact sequence gives: H80, D124, S225. These positions come from PROSITE features, not a new alignment; no substrate preference or assay result is inferred.

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Chymotrypsin-like protease CTRL-1 | UNC | The exact target supports a serine-protease family assignment but not equivalence to human CTRL/P40313 or its substrate preference. A similarity-derived name and PROSITE class prediction do not resolve paralog-specific specificity. |
| Location | Secreted (SL-0243) | CNN | A SignalP signal peptide at residues 1-20 and soluble mature S1 architecture support secretion, consistent with the curated extracellular annotation. |

## Literature evidence

- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad”

## Annotation decisions

- GO:0004252 serine-type endopeptidase activity (IBA): **ACCEPT**. The S1 domain retains annotated H80 D124 S225, consistent with the existing phylogenetic activity inference.
- GO:0004252 serine-type endopeptidase activity (IEA): **ACCEPT**. The exact catalytic residues are retained; the narrower chymotrypsin name is not required to justify GO:0004252.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:12568721 is a comparative Drosophila SP/SPH analysis. Its abstract does not establish substrate specificity; the exact record independently retains the annotated catalytic H-D-S residues.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:30367934 separates catalytic proteases from homologs by H-D-S conservation. The annotated catalytic sites in the target retain all three residue types.
- GO:0005576 extracellular region (IBA): **ACCEPT**. A SignalP signal peptide at residues 1-20 and a soluble S1-domain architecture support the curated IBA location.
- GO:0006508 proteolysis (IBA): **ACCEPT**. The intact catalytic triad supports proteolytic potential without identifying a substrate or tissue-specific pathway.
- GO:0006508 proteolysis (IEA): **ACCEPT**. The exact S1 domain retains annotated catalytic residues rather than merely a protease-like fold.
- GO:0006508 proteolysis (ISM): **ACCEPT**. PMID:12568721 provides an SP/SPH classification framework and the exact target retains its annotated H-D-S catalytic triad; this is inferential evidence rather than a substrate assay.
- GO:0008233 peptidase activity (IEA): **MODIFY**. S1 architecture with annotated catalytic H80 D124 S225 supports the specific enzyme class.
- GO:0016787 hydrolase activity (IEA): **MODIFY**. The S1 catalytic architecture supports serine-type endopeptidase activity.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG17404-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
