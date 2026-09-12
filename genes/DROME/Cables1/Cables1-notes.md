# Cables1 (A0A0B4KF19): evidence and ProtNLM claim review

Cables1 is a cyclin-fold protein required for the organization of sensory and motile cilia in Drosophila. It is recruited to maturing sperm basal bodies, and its loss disrupts neuronal ciliary architecture and the central pair of sperm axonemal microtubules. Its molecular activity at the basal body remains unresolved.

Exact input: [A0A0B4KF19](https://www.uniprot.org/uniprotkb/A0A0B4KF19/entry), 746 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Cables1-predictions-source.json](Cables1-predictions-source.json). Source features: [Cables1-uniprot.txt](Cables1-uniprot.txt), with an exact extraction in [Cables1-sequence-evidence.json](Cables1-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR012388; CABLES1/2.
DR   InterPro; IPR036915; Cyclin-like_sf.
DR   InterPro; IPR006671; Cyclin_N.
FT   DOMAIN          621..699
FT                   /note="Cyclin N-terminal"
FT                   /evidence="ECO:0000259|Pfam:PF00134"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Cyclin N-terminal domain-containing protein | CNN | The cyclin N-terminal domain is independently supported by Pfam PF00134 at residues 621-699 in the source record. The domain name is accurate; it does not assert kinase activity or establish cell-cycle regulation. |
| Location | Nucleus (SL-0191) | UNC | Direct fly imaging supports basal-body recruitment in spermatogenesis (PMID:37317646). This does not demonstrate nuclear residence or exclude a nuclear pool in other tissues; the nuclear claim needs localization evidence for this exact product. |

## Literature evidence

- [PMID:37317646](https://pubmed.ncbi.nlm.nih.gov/37317646/): “TEX9, CCDC6, and CABLES1 are recruited to maturing basal bodies during Drosophila spermatogenesis.”
- [PMID:37317646](https://pubmed.ncbi.nlm.nih.gov/37317646/): “RNAi‐mediated depletion/deletion of CABLES1, CCDC6, CEP104, and TEX9 in Drosophila chordotonal neurons”

## Annotation decisions

- GO:0036064 ciliary basal body (IDA): **ACCEPT**. GFP-tagged Cables1 is recruited to maturing basal bodies during spermatogenesis in the full-text analysis of PMID:37317646; the relatively faint signal does not negate the localization.
- GO:0044458 motile cilium assembly (IMP): **ACCEPT**. Depletion and deletion produce sperm axonemal defects including loss of the central pair in PMID:37317646; this is a direct ciliogenesis phenotype.
- GO:0051726 regulation of cell cycle (IEA): **UNDECIDED**. IPR012388 establishes CABLES-family architecture. The direct fly evidence in PMID:37317646 concerns basal bodies and ciliary architecture; it does not establish regulation of cell-cycle progression by this protein.
- GO:1905515 non-motile cilium assembly (IMP): **ACCEPT**. Neuronal cilia show disorganization and shortened axonemes after Cables1 loss in PMID:37317646; the developmental assembly role is supported.

## Research assessment

The Falcon report misses PMID:37317646 and incorrectly presents fly Cables1 as lacking a localization or phenotype study. The full-text 2023 ciliogenesis paper explicitly examines Cables1/CG6191, including depletion/deletion and basal-body recruitment. Those primary experiments determine the biological assessment; mammalian CDK/cancer discussion is contextual and is not substituted for fly evidence.

Provider output: [Cables1-deep-research-falcon.md](Cables1-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.
