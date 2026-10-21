# CG8841 (Q0E9B5): evidence and ProtNLM claim review

CG8841 is an HID1/Ecm30-family protein associated by phylogenetic and similarity inference with Golgi organization, intracellular protein transport, and secretory-granule maturation. Its likely role is in secretory-pathway membrane organization rather than DNA recombination, despite the historical Dmc1 alias; its molecular activity is unresolved.

Exact input: [Q0E9B5](https://www.uniprot.org/uniprotkb/Q0E9B5/entry), 837 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG8841-predictions-source.json](CG8841-predictions-source.json). Source features: [CG8841-uniprot.txt](CG8841-uniprot.txt), with an exact extraction in [CG8841-sequence-evidence.json](CG8841-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR026705; HID1/Ecm30.
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Protein HID1 | CNN | IPR026705 independently establishes the HID1/Ecm30 family. The current UniProt name itself is ProtNLM-derived and contributes no independent evidence; the diagnostic family assignment is the support. |
| Location | Nucleus (SL-0191) | UNC | The supported biology is Golgi/secretory-pathway organization with a cytosolic pool. That does not establish nuclear residence or prove that a nuclear pool is absent; the nuclear claim remains unsupported. |
| Location | Cytoplasm (SL-0086) | LSP | Curated cytosol and Golgi annotations provide more specific cytoplasmic locations and are biologically coherent with HID1-family secretory-pathway function. The broad cytoplasm claim is supported without invoking ARBA. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0000138 Golgi trans cisterna (IBA): **ACCEPT**. IPR026705 identifies the HID1/Ecm30 family and the IBA locates the protein in the Golgi secretory pathway. No target-specific architectural conflict is apparent.
- GO:0003674 molecular_function (ND): **ACCEPT**. HID1-family secretory-pathway participation does not establish an intrinsic enzyme activity or a specific binding reaction.
- GO:0005794 Golgi apparatus (ISS): **ACCEPT**. The HID1/Ecm30 domain supports the existing ISS Golgi annotation; this is an inferred location rather than a direct fly imaging result.
- GO:0005797 Golgi medial cisterna (IBA): **ACCEPT**. The specific IBA is compatible with HID1-family Golgi organization and no target-specific evidence of localization loss is established.
- GO:0005829 cytosol (IBA): **ACCEPT**. HID1-family membership supports a protein cycling or associating with cytosolic faces of secretory membranes; the curated IBA is retained as an inference rather than direct localization.
- GO:0006886 intracellular protein transport (ISS): **ACCEPT**. The existing ISS fits the protein's Golgi/secretory-pathway architecture and inferred organization role.
- GO:0007030 Golgi organization (IBA): **ACCEPT**. The HID1/Ecm30-family assignment is coherent with the curated IBA Golgi-organization assertion and does not require catalytic activity.
- GO:0016020 membrane (IBA): **ACCEPT**. A retained transmembrane helix is not required for peripheral membrane association; HID1-family biology and the existing IBA support the broad membrane term.
- GO:0061792 secretory granule maturation (IBA): **ACCEPT**. HID1-family placement is consistent with a role in Golgi-dependent maturation of secretory cargo. The evidence establishes participation by phylogenetic inference rather than an intrinsic catalytic mechanism.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG8841-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q0E9B5 is the single 837-aa UniProt entry for FlyBase CG8841 (FBgn0033713); the three RefSeq
proteins (NP_610760.1, NP_725131.1, NP_725132.1) map to this one sequence, so the benchmark accession is
the canonical full-length product, not a fragment or isoform. The "Dmc1" gene name in UniProt is a
submitter-imported label; the protein is unrelated to the DMC1 recombinase.

Evolutionary placement: PANTHER PTHR21575:SF12 (PROTEIN HID1), the same subfamily as human HID1 (Q8IV36),
mouse/rat Hid1, Dictyostelium hid1, S. pombe hid3/SPAC17A5.16 and S. cerevisiae ECM30
(interpro/panther/PTHR21575/PTHR21575-entries.csv). The family review
(interpro/panther/PTHR21575/PTHR21575-review.yaml) lists Q0E9B5 as the SF12 representative; no
disagreement. IBAs descend from PTN000491103 (eukaryote node; Golgi cisternae, cytosol, membrane, Golgi
organization; negated only in Schizosaccharomyces clades, taxon:4895) and PTN001090684 (secretory granule
maturation, seeded by MGI Hid1).

New bioinformatics (CG8841-bioinformatics/RESULTS.md): global alignment gives ~69% identity to
human/mouse/rat HID1, ~26-30% to the fungal SF12 members; Gly2 myristoylation motif (MGNTDSKL)
conserved; extra length is the disordered acidic segment 570-705, not a missing domain.

Literature: no Drosophila CG8841 study found (web search 2026-10-21). Ortholog evidence cached and used:
PMID:21337012 (human HID1 medial/trans Golgi + cytosol, peripheral, myristoylation-dependent),
PMID:27751232 (mouse Hid1 beta-cell KO blocks immature-granule homotypic fusion),
PMID:29074564 (rat KO: LDCV formation, cargo sorting, TGN acidification, V-ATPase a2 mislocalization),
PMID:21115972 (C. elegans HID-1 in DCV neurosecretion; N-terminal myristoyl motif needed for membranes),
PMID:40899782 (S. pombe SPAC17A5.16 mutant lacks stacked Golgi).

Decisions (changes from the previous draft, which cited only the InterPro line for every row):
- GO:0000138, GO:0005797 (IBA): ACCEPT, now supported by PMID:21337012 + RESULTS.
- GO:0005794 Golgi apparatus (ISS): ACCEPT -> MODIFY to medial/trans cisterna (already carried).
- GO:0016020 membrane (IBA): ACCEPT -> MODIFY to GO:0000139 Golgi membrane.
- GO:0005829 cytosol (IBA): ACCEPT -> KEEP_AS_NON_CORE (reservoir pool).
- GO:0006886 intracellular protein transport (ISS): ACCEPT -> KEEP_AS_NON_CORE (mechanism unresolved).
- GO:0007030 Golgi organization (IBA): ACCEPT -> KEEP_AS_NON_CORE (ancestral, distant fungal seed).
- GO:0061792 secretory granule maturation (IBA): ACCEPT (core).
- GO:0003674 ND: ACCEPT.
No NEW terms: dense core granule biogenesis is suggested by rat data but PAINT propagated only
secretory granule maturation; treated as deliberate.

Relative to review next: human HID1 (Q8IV36), same PANTHER subfamily SF12, seed of both the ISS rows and
PTN000491103; no review in the repo (no genes/human/HID1).
