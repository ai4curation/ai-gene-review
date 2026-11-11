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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not use ProtNLM2 output. Sources were the UniProt record, the GOA rows, PANTHER/PAINT data, the falcon deep-research file, and seven newly cached full-text Glorund papers.

### Identity of the benchmark accession

- Q8INJ6 is **Glorund isoform C**, 179 aa, TrEMBL, from FlyBase transcript CG6946-RC. It is not the canonical product. The long product is **Q9VGH5**, 586 aa, TrEMBL, covering isoforms A/B/D. Q8IG99 (SD14463p, 359 aa) is a cDNA covering the C-terminal half. None of the glo entries is Swiss-Prot reviewed.
- `glo-bioinformatics/compare_isoforms_rereview.py` produced `RESULTS-rereview.md` and `results-rereview.json`. Residues 1-168 of Q8INJ6 are identical to Q9VGH5. Q8INJ6 then ends in the unique tail ILRYSAARLLK.
- Using the qRRM boundaries of PMID:35699205 (qRRM1 45-141, qRRM2 142-234, qRRM3 475-562), isoform C keeps all of qRRM1, only residues 142-168 of qRRM2, and nothing of the Gly/Asn-rich region or qRRM3.
- Functional consequence: Warden et al. 2023 [PMID:37427795 "nos was not detected in immunoprecipitates of GFP-Glo mutants with only a single intact qRRM"] and ["at least two qRRMs are required for TCE recognition and translational repression of nos in vivo"]. Isoform C alone is therefore not expected to repress nanos. Its qRRM1 should still bind G-tract RNA [PMID:28380354 "Each qRRM domain bound independently to G-tract RNA"]. It also lacks most of qRRM2, the dFMRP-binding domain [PMID:35699205 "Glo's qRRM2 domain specifically and directly interacts with dFMRP"].
- GOA attaches the FlyBase gene-level annotations to both Q8INJ6 and Q9VGH5. Only Q9VGH5 carries the PAINT IBA rows: RNA binding, nucleoplasm, ribonucleoprotein complex and GO:0043484, from PTN000360053 and PTN000359854. I reviewed the FlyBase rows as claims about the glo gene and stated in each reason whether the claim can apply to the isoform-C product.

### Evolutionary placement

- PANTHER 19.0 places glo (Q9VGH5) in **PTHR13976:SF76 "AT27789P"**, with C. elegans hrpf-2 (Q8MXR2) and plant proteins (At3g20890, two poplar genes). It is **not** in the vertebrate hnRNP F/H subfamilies (SF32 HNRNPF, SF33 HNRNPH2, SF36 HNRNPH3, SF60 HNRNPH1) or the ESRP subfamilies (SF30, SF37). Fly fusilli, the ESRP ortholog, is in SF25.
- The name "hnRNP F/H homolog" therefore reflects shared qRRM architecture and conserved G-tract-binding residues [PMID:28380354 "the residues in hnRNP F that mediate interaction with G-tract RNA are conserved in Glo"]. It does not mean subfamily-level orthology. I made no subfamily-specific transfer from human hnRNP F/H, such as splicing of particular targets. The only phylogenetic support used is the PAINT node PTN000360053, which spans the clade and gives RNA binding.
- The family review (`interpro/panther/PTHR13976/PTHR13976-review.yaml`) lists Q8INJ6 as a representative of one lumped "ESRP, hnRNP H/F and related" subfamily. That conflicts with PANTHER, which separates glo (SF76) from ESRP and hnRNP F/H. The family review also uses the isoform accession rather than Q9VGH5. Both points are recorded here; the family file was not edited.

### Annotation decisions (gene-level claims)

- GO:0003676 nucleic acid binding (IEA): MODIFY to RNA binding.
- GO:0003723 RNA binding (IEA): ACCEPT. qRRM1, which isoform C retains, binds RNA directly.
- GO:0003729 mRNA binding (ISS, PMID:10908586): ACCEPT on direct evidence (PMID:16516833, PMID:28380354, PMID:37427795). The cited survey does not mention Glo (reference marked MISCITED).
- GO:0005515 protein binding x2 (Hrp48, Hfp): REMOVE under the protein-binding policy. The interactions are real and RNase-resistant.
- GO:0006417 regulation of translation: MODIFY to GO:0017148 negative regulation of translation.
- GO:0007311 maternal D/V specification, GO:0060810 mRNA localization in pattern specification, and GO:0045451 oskar mRNA localization: KEEP_AS_NON_CORE. These are genuine germline requirements but downstream of otu splicing and G-tract-mode RNA regulation.
- GO:0051276 chromosome organization: MARK_AS_OVER_ANNOTATED. Glo does none of the chromosome-organization work; Otu-104 partly rescues the phenotype.
- GO:0032991 protein-containing complex x2: KEEP_AS_NON_CORE.
- GO:0042060 wound healing (HMP, screen): UNDECIDED. Only the abstract is available, and it does not mention glo.
- NEW: GO:0003730 mRNA 3'-UTR binding, GO:0000900 mRNA regulatory element binding translation repressor activity, GO:0005634 nucleus, and GO:0005737 cytoplasm. All are gene-level and stated not to be demonstrated for isoform C.
- I did not propose terms for the lipid-storage RNAi (PMID:33537463, PMID:41837177) or testis overexpression (PMID:39092172) phenotypes. They are organismal or downstream phenotypes.

### Relative to review next

Q9VGH5, the long canonical product of the same gene (same_gene_canonical), has no review in the repo. Its folder would be `genes/DROME/glo__Q9VGH5`. That review should cover the IBA rows (RNA binding, nucleoplasm GO:0005654, ribonucleoprotein complex GO:1990904, GO:0043484 regulation of RNA splicing) that are absent from Q8INJ6.
