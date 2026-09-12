# CG30287 (Q8MLV8): evidence and ProtNLM claim review

CG30287 is a predicted secreted S1-family serine endopeptidase with an intact annotated catalytic triad. The 284-residue product is also called SP224 and historically SPH37, but the latter name alone does not establish catalytic inactivity. Its physiological substrates and relationship to vertebrate PRSS55 remain unresolved.

Exact input: [Q8MLV8](https://www.uniprot.org/uniprotkb/Q8MLV8/entry), 284 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG30287-predictions-source.json](CG30287-predictions-source.json). Source features: [CG30287-uniprot.txt](CG30287-uniprot.txt), with an exact extraction in [CG30287-sequence-evidence.json](CG30287-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR009003; Peptidase_S1_PA.
DR   InterPro; IPR001314; Peptidase_S1A.
DR   InterPro; IPR051487; Ser/Thr_Proteases_Immune/Dev.
DR   InterPro; IPR001254; Trypsin_dom.
DR   InterPro; IPR018114; TRYPSIN_HIS.
DR   InterPro; IPR033116; TRYPSIN_SER.
FT   SIGNAL          1..21
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          42..282
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   ACT_SITE        82
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        136
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        232
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
```

At the annotated catalytic positions, direct indexing of the exact sequence gives: H82, D136, S232. These positions come from PROSITE features, not a new alignment; no substrate preference or assay result is inferred.

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Serine protease 55 | UNC | Serine-protease potential is supported by the intact annotated triad, but the vertebrate PRSS55-specific name exceeds the evidence. Q6UWB4 is a human PRSS55 source; a similarity hit without resolved orthology or conserved physiological function does not establish that precise identity in fly. |
| Location | Secreted (SL-0243) | CNN | The SignalP signal peptide at residues 1-21 and soluble S1-domain architecture support secretion, consistent with the curated extracellular IBA. This does not identify a reproductive substrate or PRSS55-specific function. |

## Literature evidence

- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad”

## Annotation decisions

- GO:0004252 serine-type endopeptidase activity (IBA): **ACCEPT**. H82 D136 and S232 are retained at the annotated catalytic sites in the S1 domain. The historical SPH37 alias is insufficient to call it a pseudoenzyme.
- GO:0004252 serine-type endopeptidase activity (IEA): **ACCEPT**. The exact record has an intact annotated H-D-S catalytic triad and a complete S1 domain, supporting the existing broad activity mapping.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:30367934 distinguishes SPs from SPHs using catalytic-residue conservation. The exact sequence has H82 D136 S232 at the annotated sites, supporting proteolytic potential despite older SPH naming.
- GO:0005576 extracellular region (IBA): **ACCEPT**. A SignalP signal peptide at residues 1-21 and a soluble mature S1-domain architecture support the curated IBA.
- GO:0006508 proteolysis (IBA): **ACCEPT**. The catalytic triad is retained in the S1 domain; no specific physiological substrate is established.
- GO:0006508 proteolysis (IEA): **ACCEPT**. The annotated H-D-S residues are present and no loss-of-catalysis conclusion follows from the historical SPH37 alias.
- GO:0008233 peptidase activity (IEA): **MODIFY**. The intact S1 catalytic architecture supports the more informative peptidase class.
- GO:0016787 hydrolase activity (IEA): **MODIFY**. The exact domain and catalytic residues support serine-type endopeptidase activity.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG30287-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
