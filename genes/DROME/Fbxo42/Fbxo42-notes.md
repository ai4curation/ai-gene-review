# Fbxo42 (Q9W281): evidence and ProtNLM claim review

Fbxo42 is the substrate-recognizing F-box subunit of an SCF ubiquitin ligase. In Drosophila oocytes, SCF-Fbxo42 downregulates the PP2A-B56 phosphatase subunit and promotes assembly and maintenance of the synaptonemal complex. Its F-box and kelch-like architecture support substrate recognition and complex assembly rather than intrinsic ubiquitin transfer.

Exact input: [Q9W281](https://www.uniprot.org/uniprotkb/Q9W281/entry), 667 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Fbxo42-predictions-source.json](Fbxo42-predictions-source.json). Source features: [Fbxo42-uniprot.txt](Fbxo42-uniprot.txt), with an exact extraction in [Fbxo42-sequence-evidence.json](Fbxo42-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR036047; F-box-like_dom_sf.
DR   InterPro; IPR001810; F-box_dom.
DR   InterPro; IPR052821; F-box_only_SRC.
DR   InterPro; IPR015915; Kelch-typ_b-propeller.
FT   DOMAIN          21..70
FT                   /note="F-box"
FT                   /evidence="ECO:0000259|PROSITE:PS50181"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | F-box domain-containing protein | CNN | The F-box at residues 21-70 is independently supported by IPR001810, and PMID:33382409 directly establishes an SCF-Fbxo42 complex. The architecture name is correct but less informative than the known substrate-adaptor function. |
| Location | Nucleus (SL-0191) | UNC | A role in nuclear meiotic chromosome organization does not by itself establish nuclear localization of the adaptor. The inspected experiments establish SCF association and a PP2A-B56-dependent phenotype; direct localization of Fbxo42 to nuclei is needed to resolve this claim. |

## Literature evidence

- [PMID:33382409](https://pubmed.ncbi.nlm.nih.gov/33382409/): “Our biochemical and genetic evidence suggests that Fbxo42 promotes synaptonemal complex assembly by negatively controlling the level of the protein phosphatase PP2A-B56.”

## Annotation decisions

- GO:0019005 SCF ubiquitin ligase complex (IBA): **ACCEPT**. PMID:33382409 identifies Fbxo42 as an SCF substrate-recognition subunit; the IBA is concordant with direct target evidence and is not circular.
- GO:0019005 SCF ubiquitin ligase complex (IDA): **ACCEPT**. Biochemical interaction and genetic analyses in PMID:33382409 establish the Fbxo42 SCF complex in Drosophila ovaries.
- GO:0019005 SCF ubiquitin ligase complex (ISM): **ACCEPT**. The independent F-box domain at residues 21-70 and direct complex evidence in PMID:33382409 support the computational annotation.
- GO:0031146 SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (ISM): **ACCEPT**. PMID:33382409 shows that SCF-Fbxo42 downregulates PP2A-B56 in the pathway promoting synaptonemal-complex assembly. The protein is the substrate adaptor rather than the catalytic ubiquitin-transfer enzyme.
- GO:1905088 positive regulation of synaptonemal complex assembly (IMP): **ACCEPT**. The full text of PMID:33382409 documents impaired assembly and maintenance after Fbxo42 depletion and connects this phenotype to PP2A-B56 regulation.
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IBA): **ACCEPT**. F-box-mediated SCF incorporation and substrate-recognition evidence support the IBA; they do not establish intrinsic ubiquitin ligase catalysis by Fbxo42 alone.
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IPI): **ACCEPT**. PMID:33382409 identifies Fbxo42 as a substrate-recognizing SCF subunit and PP2A-B56 as the regulated target. This is more informative than generic protein binding.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Fbxo42-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
