# Reproducible LNP1 interaction and localization provenance audit

## Bottom line

Human LNP1 is UniProtKB **A1A4G5** (178 aa; HGNC symbol `LNP1`; synonym
`NP3`). It is not lunapark/LNPK, UniProtKB **Q9C0E8** (428 aa; HGNC symbol
`LNPK`; historical synonym `LNP`). The accessions are independently resolved in
[`results/uniprot_identities.tsv`](results/uniprot_identities.tsv).

Two informative molecular-function annotations are defensible as non-core,
high-throughput/interaction-derived claims:

1. `GO:0071889` **14-3-3 protein binding**, IPI, PMID:33961781. BioPlex recovered
   six 14-3-3 genes with LNP1 in both 293T and HCT116 cells. The raw
   accession-level protein-group rows are `P27348` (YWHAQ), `P31946-2` (YWHAB), `P61981` (YWHAG),
   `P62258` and `P62258-2` (YWHAE), `P63104` and the unreviewed truncated
   proteoform `E7ESK7` (YWHAZ), and `Q04917` (YWHAH). These identifiers record
   the source assignments; they do not establish isoform-specific detection or
   isoform-exclusive biology.
2. `GO:1990782` **protein tyrosine kinase binding**, IPI, PMID:23503679, with
   `UniProtKB:P07948` (LYN). PLATO discovery was followed by a targeted
   GST-LYN pull-down/Western validation in which Figure 2c labels LNP1.

Both annotations must retain an explicit limitation: the assays establish
physical co-association under the tested conditions, not an endogenous pathway,
substrate relationship, or purified-protein binding mechanism. AP-MS in
particular does not distinguish direct contact from a bridged/co-complex
association.

No informative GO annotation follows from the HuRI LNP1-GPRIN2 pair or the
LNP1-GAPDH crosslink. A generic `protein binding` annotation would add no useful
function. Complex Portal CPX-12224 is explicitly machine-learning predicted and
must not be asserted as an experimentally isolated, stable 28-member complex.

## Evidence audit

### BioPlex 3.0 / PMID:33961781

The official December 2019 BioPlex no-filter bait-prey tables, not only a
canonicalized interaction export, were checked. Exact source rows are retained
in
[`results/bioplex_LNP1_14-3-3_source_rows.tsv`](results/bioplex_LNP1_14-3-3_source_rows.tsv).

| Family gene | 293T prey accession(s) | HCT116 prey accession(s) |
|---|---|---|
| YWHAQ | P27348 | P27348 |
| YWHAB | P31946-2 | P31946-2 |
| YWHAG | P61981 | P61981 |
| YWHAE | P62258, P62258-2 | P62258 |
| YWHAZ | P63104 | P63104, E7ESK7 |
| YWHAH | Q04917 | Q04917 |

The source therefore contains six 14-3-3 genes, but eight distinct accession-level
protein-group strings across the two cell lines. `E7ESK7` is a current unreviewed, 137-aa
YWHAZ sequence; it is not a seventh 14-3-3 gene. IntAct collapses the YWHAB,
YWHAE, and YWHAZ source proteoforms to canonical gene-level accessions.

The twelve IntAct records (six pairs in each cell line) use:

- `MI:0007` anti tag coimmunoprecipitation;
- `MI:0914` association, not `MI:0915` physical association;
- `MI:1060` spoke expansion;
- LNP1 as bait (`MI:0496`) and each 14-3-3 protein as prey (`MI:0498`);
- IntAct miscore 0.35.

This repeated family-selective AP-MS pattern supports an IPI annotation to
`14-3-3 protein binding` under normal GO interaction-evidence practice, but it
does not by itself prove direct binary binding. hu.MAP3 and AlphaFold3 add a
testable structural hypothesis, not independent direct experimental evidence.

### PLATO LYN interaction / PMID:23503679

BioGRID records both stages with exact identities LYN/P07948 and LNP1/A1A4G5:

- interaction 868448: high-throughput `Affinity Capture-Luminescence` discovery;
- interaction 868526: low-throughput `Affinity Capture-Western` validation.

The full paper's Figure 2c visibly labels LNP1, shows an LNP1 band in input and
GST-LYN pull-down, and no corresponding band in the GST-Pep control. The assay
used tagged LNP1 expressed in 293T lysate and bacterially produced GST-LYN; it
supports physical association but not endogenous interaction, LYN-dependent
phosphorylation, or a physiological LYN pathway.

### hu.MAP3 / PMID:40425816

The official hu.MAP3 page for `huMAP3_06971.1` labels the cluster **Very High**
confidence and reports these LNP1 edges:

| Pair | hu.MAP3 score | ProteomeHD / interface-overlap shown for this pair |
|---|---:|---|
| LNP1-YWHAE | 0.986 | blank / blank |
| YWHAZ-LNP1 | 0.985 | blank / blank |
| YWHAH-LNP1 | 0.984 | blank / blank |
| YWHAG-LNP1 | 0.982 | blank / blank |
| YWHAQ-LNP1 | 0.981 | blank / blank |
| LNP1-YWHAB | 0.980 | blank / blank |
| SFN-LNP1 | 0.964 | blank / blank |

hu.MAP3 is a machine-learning integration of AP-MS, co-fractionation MS,
proximity-labeling, and related features; BioPlex is among its inputs. Its score
is an estimated co-complex/interacting probability. The paper's LNP1-YWHAE
AlphaFold3 model is predictive (reported ipTM 0.73 and pTM 0.64), not an
experimental binding validation.

There is also a residue-numbering warning. Current A1A4G5 residues 110-115 are
`KFSESF`. The paper states Ser114 but writes `KFpSESF`, which places the
phosphate on the first serine (current S112); correct S114 notation would be
`KFSEpSF`. The cited phosphoproteome source reports S114. Do not turn this
internally inconsistent motif typography or the AlphaFold model into a
residue-specific functional annotation.

The exact official PMID:31819260 Supplementary Table S2 row is retained in
[`results/raw/pmid31819260_A1A4G5_S114_source_row.tsv`](results/raw/pmid31819260_A1A4G5_S114_source_row.tsv).
It records A1A4G5 residue 114 as serine, localization probability 0.844585, and
two spectral counts. This substantiates site detection only; it does not assign
the kinase, demonstrate 14-3-3 binding, or resolve the motif-numbering conflict.

### Complex Portal CPX-12224

The official API returns:

```json
"predictedComplex": true
"evidenceType": {"identifier": "ECO:0008004", "description": "machine-learning predicted complex"}
```

It cross-references `huMAP3_06971.1` as an identical object, lists 28
participants (including A1A4G5 and all seven human 14-3-3 genes), and gives null
stoichiometry for every participant. This is a predicted clustering result, not
primary IPI evidence and not a basis for an `in_complex: CPX-12224` assertion.

### HuRI / PMID:32296183

The unresolved IntAct participant `ccsb orf id: 6830` is not LNP1 and is not an
unknown protein. Official Supplementary Table 2 maps it as follows:

```text
6830	ENST00000374317.1	ENSP00000363436.1	ENSG00000204175.5	GPRIN2
54500	ENST00000383693.7	ENSP00000373191.3	ENSG00000206535.7	LNP1
```

Current UniProt maps GPRIN2 to reviewed accession `O60269`. Supplementary Table
9 contains exactly one GPRIN2-LNP1 pair, detected in screen 1 and assay v1:

```text
ENSG00000204175	ENSG00000206535	1	0	0	0	0	0	0	0	0	1	0	0
```

IntAct exposes three records for that one pair (`MI:1356` validated two hybrid,
`MI:1112` two hybrid prey pooling, and `MI:0397` two hybrid array), all typed
`MI:0915` physical association with miscore 0.56. This is credible binary Y2H
evidence, but no specific molecular function or biological process is known;
therefore it does not justify a useful GO annotation.

### Nuclear XL-MS / PMID:30021884

Supplementary Table S2 contains one DSSO interlink in a TX100-insoluble U2OS
nuclear fraction. It assigns LNP1 leading residue Lys124 and GAPDH leading
residue Lys145 (the GAPDH peptide also maps to P04406-2 residue 103), score
95.05 and Q-value 0.02. IntAct represents it as A1A4G5-P04406, `MI:0030`
cross-linking study, `MI:0915` physical association, miscore 0.40.

This is residue-proximity evidence in an intact-nucleus preparation, but it is a
single high-throughput crosslink and does not establish a selective GAPDH-binding
function, normal nuclear-speck residence, or a physiological pathway. The paper
itself highlights difficulty filtering nonspecific contacts and validating novel
PPIs. Do not add a generic protein-binding row.

### Human Protein Atlas cellular-component boundary

The current HPA XML entry uses one antibody, `HPA047926`, with **Approved** (not
Enhanced/Supported) reliability. Exact cell-line calls are:

| Cell line | Calls |
|---|---|
| PC-3 | nuclear speckles; vesicles; cytosol |
| U2OS | vesicles |

Thus vesicular staining is shared across the two assayed lines, whereas nuclear
speckles and cytosol are PC-3-only calls. These data support a cautious,
cell-line-qualified description of vesicular staining, not constitutive nuclear
speck or cytosol localization. The XML labels the call `vesicles` while attaching
`GO:0043231`, whose current GO label is the broader **intracellular
membrane-bounded organelle**; do not silently treat that HPA identifier as a
precise current `vesicle` term. Given the single Approved antibody, none of these
locations should be promoted to a core function without orthogonal validation.

## Annotation recommendations

| Proposed action | Evidence | Recommendation |
|---|---|---|
| NEW `GO:0071889` 14-3-3 protein binding | IPI, PMID:33961781 | Defensible as non-core. Use six gene-level supporting entities: `P27348`, `P31946-2`, `P61981`, `P62258`, `P63104`, `Q04917`. Retain duplicate raw protein-group rows `P62258-2` and `E7ESK7` here as provenance rather than inflating six gene interactions to eight WITH/FROM entries. State AP-MS/co-association limitation. |
| NEW `GO:1990782` protein tyrosine kinase binding | IPI, PMID:23503679 | Defensible as non-core with `UniProtKB:P07948`. State tagged pull-down limitation; do not infer phosphorylation/substrate activity. |
| LNP1-GPRIN2 | HuRI Y2H, PMID:32296183 | Physical/binary evidence is real, but add no GO row because only generic protein binding follows. |
| LNP1-GAPDH | XL-MS, PMID:30021884 | Physical proximity evidence is real, but add no GO row; single crosslink has no specific functional interpretation. |
| CPX-12224 membership | ECO:0008004 | Do not assert `in_complex`; it is machine-learning predicted with unknown stoichiometry. |
| S114-dependent 14-3-3 mechanism | hu.MAP3/AlphaFold3 | Treat as a hypothesis. Do not annotate residue-specific mechanism until targeted experiments resolve S112 versus S114 and demonstrate dependence. |
| HPA locations | one Approved antibody | Use only as contextual/non-core localization evidence; retain cell-line boundaries. |

## Validator-safe verbatim source text

The following strings are exact substrings of the indicated cached publication
files and can be copied without paraphrase into `supporting_text`.

**PMID:23503679**

> GSTLYN precipitation and western blot analysis confirmed binding for five of seven novel candidates tested (Figure 2c).

**PMID:33961781**

> In contrast, affinity-purification mass spectrometry (AP-MS) enables enrichment and detection of even low-abundance proteins, though exogenous expression of tagged baits is required, and extensive sample preparation has limited scalability while precluding recovery of transient interactions ( Gingras et al., 2007 ).

**PMID:40425816**

> We also identify LNP1, an uncharacterized protein, as associated with members of the 14-3-3 complex (huMAP3_06971.1).

> LNP1 has a known phosphoserine site at Ser114 (Ochoa et al, 2020) in a motif reminiscent of 14-3-3 binding (KFpSESF vs RXY/FXpSXP (Yaffe et al, 1997)).

> Provided this, we used AlphaFold3 to model the interaction between LNP1 and YWHAE, a 14-3-3 subunit which had the highest hu.MAP3.0 score 0.986 to LNP1.

> This provides further evidence of LNP1’s association with the 14-3-3 complex.

**PMID:32296183**

> To map the reference interactome, we performed nine screens of Space III, followed by pairwise verification by quadruplicate retesting and sequence confirmation.

> The dataset, versioned HI-III-20 (Human Interactome obtained from screening Space III, published in 2020), contains 52,569 verified PPIs involving 8,275 proteins (Supplementary Table 9).

**PMID:30021884**

> Here we use crosslinking mass spectrometry (XL-MS) to chart the protein-protein interactions in intact human nuclei.

> The major challenge is represented by the ability to identify and filter out nonspecific interactions and by challenges in validating novel observed PPIs.

**HPA XML exact text**

> Mainly localized to vesicles. In addition localized to the nuclear speckles and cytosol.

> Immunofluorescent staining of human cell line PC-3 shows localization to nuclear speckles, vesicles and cytosol.

## Exact local-reference title and reusable snippets

Use this local reference identifier and title:

- id: `file:human/LNP1/LNP1-bioinformatics/RESULTS.md`
- title: `Reproducible LNP1 interaction and localization provenance audit`

The following sentences occur verbatim in this file and are suitable as
file-backed supporting text:

> Official BioPlex source rows identify P31946-2, not canonical P31946, as the YWHAB protein-group accession in both 293T and HCT116 LNP1 experiments.

> Official BioPlex source output contains both P62258 and P62258-2 YWHAE protein-group rows in 293T cells, while HCT116 contains P62258.

> IntAct classifies the BioPlex LNP1-14-3-3 records as MI:0007 anti tag coimmunoprecipitation, MI:0914 association, and MI:1060 spoke expansion rather than direct binary binding.

> BioGRID maps the validated PLATO pair to LYN/P07948 and LNP1/A1A4G5 and classifies interaction 868526 as Affinity Capture-Western.

> Official HuRI supplements map CCSB ORF 6830 to GPRIN2/O60269 and ORF 54500 to LNP1/A1A4G5, yielding one GPRIN2-LNP1 binary Y2H pair rather than self-binding.

> Complex Portal marks CPX-12224 as predictedComplex true with ECO:0008004 machine-learning predicted complex evidence and unknown participant stoichiometry.

> Human Protein Atlas antibody HPA047926 has Approved reliability and reports vesicles in PC-3 and U2OS, with nuclear-speck and cytosolic signal only in PC-3.

> Official PMID:31819260 Supplementary Table S2 records A1A4G5 Ser114 with localization probability 0.844585 and two spectral counts.

## Reproducibility and provenance

Run:

```bash
cd genes/human/LNP1/LNP1-bioinformatics
just check
```

The workflow uses Python's standard library, reads identifiers/URLs from
`config.json`, writes direct and filtered results under `results/`, records URL,
HTTP metadata, byte ranges, size, and SHA-256 for every retrieved source in
[`results/source_manifest.tsv`](results/source_manifest.tsv), and fails when an
expected identity or edge changes.

- [x] Source inputs, URLs, target identifiers, and the output directory come
      from CLI arguments or `config.json`; report filenames are deliberately
      fixed for this gene-specific LNP1 audit.
- [x] Tested an explicit confounder/control input: Q9C0E8 resolves to LNPK, not
      LNP1.
- [x] All requested interaction, complex, and localization analyses completed.
- [x] Direct API/database results and exact supplement rows are retained under
      `results/` and `results/raw/`.
- [x] Detailed source provenance and checksums are retained in the manifest.
