# glo (Q8INJ6): evidence and ProtNLM claim review

Glorund is an RNA-binding regulator of translation and RNA processing in Drosophila oogenesis. The Q8INJ6 isoform-C record is a short 179-residue RRM-containing product, whereas gene-level experiments establish repression of nanos translation, association with Hrp48 and Half-pint, and roles in oocyte RNA localization. Which of these activities and localizations are retained by this short isoform remains unresolved.

Exact input: [Q8INJ6](https://www.uniprot.org/uniprotkb/Q8INJ6/entry), 179 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [glo-predictions-source.json](glo-predictions-source.json). Source features: [glo-uniprot.txt](glo-uniprot.txt), with an exact extraction in [glo-sequence-evidence.json](glo-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR050666; ESRP.
DR   InterPro; IPR012677; Nucleotide-bd_a/b_plait_sf.
DR   InterPro; IPR035979; RBD_domain_sf.
DR   InterPro; IPR000504; RRM_dom.
FT   DOMAIN          49..129
FT                   /note="RRM"
FT                   /evidence="ECO:0000259|PROSITE:PS50102"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | RRM domain-containing protein | CNN | IPR000504 and the domain feature at residues 49-129 independently establish the RRM in the exact 179-residue sequence. This limited domain claim remains sound despite uncertainty about full-length Glorund functions. |
| Location | Nucleoplasm (SL-0190) | UNC | PMID:19013444 discusses nuclear and cytoplasmic Glorund, but the localization is not mapped to the short 179-residue Q8INJ6 isoform. A nuclear-splicing role at the locus does not independently establish nucleoplasmic residence of this product. |
| Location | Nucleus (SL-0191) | UNC | Nuclear Glorund is reported in the literature, but the exact Q8INJ6 isoform is short and requires construct mapping. Broad nuclear residence of this product remains unresolved rather than refuted. |

## Literature evidence

- [PMID:19013444](https://pubmed.ncbi.nlm.nih.gov/19013444/): “whereas Glo and Hrp48 are both nuclear and cytoplasmic”
- [PMID:19013444](https://pubmed.ncbi.nlm.nih.gov/19013444/): “Here we show that Glorund is part of a complex containing the hnRNP protein Hrp48 and the splicing factor Half-pint”
- [PMID:16516833](https://pubmed.ncbi.nlm.nih.gov/16516833/): “Here we identify a Drosophila hnRNP, Glorund, that interacts specifically with stem-loop III.”

## Annotation decisions

- GO:0003676 nucleic acid binding (IEA): **MODIFY**. The exact product retains an RRM at residues 49-129 and belongs to the experimentally characterized RNA-binding Glorund locus. RNA binding is a reasonable domain-level inference without transferring a specific mRNA target.
- GO:0003723 RNA binding (IEA): **ACCEPT**. The 179-residue product contains an intact annotated RRM at residues 49-129. This supports broad RNA binding but does not identify its target RNAs or establish full-length Glorund activity.
- GO:0003729 mRNA binding (ISS): **UNDECIDED**. PMID:10908586 surveys RNA-binding proteins at gene/family level; the exact Q8INJ6 product has only a short RRM-containing architecture and no isoform-mapped mRNA binding assay is established.
- GO:0005515 protein binding (IPI): **UNDECIDED**. PMID:19013444 identifies a Glorund-Hrp48-Half-pint complex. The 179-residue isoform needs construct mapping before these gene-level interactions can be assigned to it.
- GO:0005515 protein binding (IPI): **UNDECIDED**. The full-text complex experiments in PMID:19013444 establish Glorund-associated interactions, but do not establish retention of the interaction surfaces in the exact 179-residue product.
- GO:0006417 regulation of translation (IMP): **UNDECIDED**. PMID:16516833 demonstrates Glorund-dependent nanos translational repression. Q8INJ6 contains a short RRM-bearing sequence and requires construct or isoform mapping before that activity is transferred.
- GO:0007311 maternal specification of dorsal/ventral axis, oocyte, germ-line encoded (IMP): **UNDECIDED**. PMID:19013444 establishes Glorund roles in oocyte patterning; the responsible experimental products are not mapped to Q8INJ6 in the inspected evidence.
- GO:0032991 protein-containing complex (IPI): **UNDECIDED**. The Glorund-Hrp48-Half-pint complex in PMID:19013444 is real gene-level evidence; incorporation of the 179-residue isoform is unestablished.
- GO:0032991 protein-containing complex (IPI): **UNDECIDED**. The Glorund-Hrp48-Half-pint complex in PMID:19013444 is real gene-level evidence; incorporation of the 179-residue isoform is unestablished.
- GO:0042060 wound healing (HMP): **UNDECIDED**. PMID:19884309 is an epithelial-repair genetic screen and the cache is abstract-only. Neither the precise experiment nor isoform-specific contribution can be verified from that source.
- GO:0045451 germ plasm oskar mRNA localization (IMP): **UNDECIDED**. PMID:19013444 establishes a Glorund-dependent mRNA-localization phenotype; an intact RRM alone does not show that the 179-residue isoform executes this process.
- GO:0051276 chromosome organization (IMP): **UNDECIDED**. PMID:19013444 connects Glorund complexes and ovarian-tumor splicing to chromosome organization. The phenotype should not be transferred to the short isoform without construct mapping.
- GO:0060810 intracellular mRNA localization involved in pattern specification process (IMP): **UNDECIDED**. The locus-level data in PMID:19013444 support Glorund biology, while the sequence represented by Q8INJ6 requires specific mapping to the assayed protein.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `glo-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.
