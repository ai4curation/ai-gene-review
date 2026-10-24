---
title: Next 20 fly genes — metabolic enrichment
species: [DROME]
tags: [EVALUATION, ML_PREDICTIONS]
autolink_gene_symbols: false
---
# Next 20 fly genes: metabolic enrichment

**This cohort adds 20 distinct fly genes with an emphasis on metabolic enzymes, metabolite transport and compartmental targeting.** Glycan processing, cyclic-nucleotide turnover, phosphoinositide and pyrimidine metabolism, redox chemistry and mitochondrial functions are represented. Two noncatalytic enzyme-fold comparators help distinguish an informative family name from an unsupported catalytic claim.

**Status: selected; reviews have not started for this cohort.** The first 41-gene cohort and its results remain separate.

[20-gene selection and review questions](fly-benchmark/next20/cohort.csv) · [Exact emitted predictions](fly-benchmark/next20/prediction-statements.csv) · [Sequences](fly-benchmark/next20/sequences.fasta) · [Source manifest](fly-benchmark/next20/manifest.json) · [Reproduction](fly-benchmark/next20/README.md) · [First fly cohort](fly.md)

## Selection and coverage

The published species subset has already supplied all 41 of its GO/function-bearing genes. Joining the original 28,553-record XML export to a current UniProt fly taxonomy index identifies **123 fly accessions**, including **29 absent from the published list**. All 29 additional accessions return predictions through the live API. The combined records map to 119 FlyBase genes; duplicate accessions for the same gene are not counted as new genes.

The next 20 comprise nine of those additional entries and eleven remaining published entries. There is **no FlyBase-gene overlap with the first 41**. The nine additional entries are currently Swiss-Prot records; the eleven published entries are TrEMBL. Record status and existing annotations guide research leads, not correctness judgments.

| Review tier | Genes | Scope |
|---|---:|---|
| GO/function-bearing | 3 | alpha-Man-Ia, Pde4 and scaf: three GO claims and one function paragraph |
| Localization without GO/function text | 12 | Compartment, topology and protein-name claims |
| Name-only | 5 | Gpdh3, CG18547, CG6830, Serinc and CG42331: naming specificity and exact-product identity |
| **Total** | **20** | **Three GO claims, one paragraph, 16 localization statements and 20 protein names** |

The protein names and UniProt SL locations are actual outputs, not converted into invented GO predictions. A name-only record can still expose a wrong paralog or over-specific enzyme designation, but its assessment is not a GO accuracy result. Selection is retrospective and deliberately enriched for biochemical questions; it is not a random fly-proteome sample.

## Selected genes

Symbols link to FlyBase. Pde4 is the current FlyBase symbol for the classic **dunce/dnc** locus, named dnc in the frozen UniProt record. The exact accession is retained for every candidate.

| Priority | Gene | Exact accession | Biological lead | Outputs beyond the protein name |
|---|---|---|---|---|
| 1 | [alpha-Man-Ia](https://flybase.org/reports/FBgn0259170) | [P53624](https://rest.uniprot.org/uniprotkb/protnlm/P53624) | Glycan metabolism | 1 GO, 1 paragraph, 1 location |
| 2 | [Pde4](https://flybase.org/reports/FBgn0000479) | [Q9W4S9](https://rest.uniprot.org/uniprotkb/protnlm/Q9W4S9) | Cyclic-nucleotide metabolism | 1 GO, 1 location |
| 3 | [CG3631](https://flybase.org/reports/FBgn0038268) | [Q95T10](https://rest.uniprot.org/uniprotkb/protnlm/Q95T10) | Proteoglycan biosynthesis | 1 location |
| 4 | [CG8745](https://flybase.org/reports/FBgn0036381) | [Q9VU95](https://rest.uniprot.org/uniprotkb/protnlm/Q9VU95) | PLP-enzyme substrate specificity | 1 location |
| 5 | [Ctns](https://flybase.org/reports/FBgn0039045) | [Q9VCR7](https://rest.uniprot.org/uniprotkb/protnlm/Q9VCR7) | Lysosomal metabolite transport | 1 location |
| 6 | [amon](https://flybase.org/reports/FBgn0023179) | [Q9VBC7](https://rest.uniprot.org/uniprotkb/protnlm/Q9VBC7) | Peptide processing | 2 location |
| 7 | [Mrm2](https://flybase.org/reports/FBgn0038737) | [Q9VDT6](https://rest.uniprot.org/uniprotkb/protnlm/Q9VDT6) | Mitochondrial RNA modification | 1 location |
| 8 | [CG6836](https://flybase.org/reports/FBgn0036834) | [Q9VVV2](https://rest.uniprot.org/uniprotkb/protnlm/Q9VVV2) | Organic-solute transport | 1 location |
| 9 | [NTPase](https://flybase.org/reports/FBgn0024947) | [O76268](https://rest.uniprot.org/uniprotkb/protnlm/O76268) | Nucleotide-sugar metabolism | 1 location |
| 10 | [Synj](https://flybase.org/reports/FBgn0034691) | [Q5U0V7](https://rest.uniprot.org/uniprotkb/protnlm/Q5U0V7) | Phosphoinositide metabolism | 2 location |
| 11 | [CG8353](https://flybase.org/reports/FBgn0032002) | [Q9VLR2](https://rest.uniprot.org/uniprotkb/protnlm/Q9VLR2) | Pyrimidine metabolism | 1 location |
| 12 | [Tango5](https://flybase.org/reports/FBgn0052675) | [Q7KVQ7](https://rest.uniprot.org/uniprotkb/protnlm/Q7KVQ7) | Lipid handling and autophagy | 1 location |
| 13 | [CG34117](https://flybase.org/reports/FBgn0083953) | [Q0KI97](https://rest.uniprot.org/uniprotkb/protnlm/Q0KI97) | Bioenergetic complex assembly | 1 location |
| 14 | [Gpdh3](https://flybase.org/reports/FBgn0263048) | [E1JIT1](https://rest.uniprot.org/uniprotkb/protnlm/E1JIT1) | Glycerophosphate and redox metabolism | Name only |
| 15 | [CG18547](https://flybase.org/reports/FBgn0037973) | [Q9VGF3](https://rest.uniprot.org/uniprotkb/protnlm/Q9VGF3) | Sugar-alcohol redox specificity | Name only |
| 16 | [CG6830](https://flybase.org/reports/FBgn0037934) | [Q9VGJ8](https://rest.uniprot.org/uniprotkb/protnlm/Q9VGJ8) | Steroid-associated kinase family | Name only |
| 17 | [Serinc](https://flybase.org/reports/FBgn0028399) | [M9PCT1](https://rest.uniprot.org/uniprotkb/protnlm/M9PCT1) | Membrane lipid biology | Name only |
| 18 | [CG42331](https://flybase.org/reports/FBgn0259233) | [Q9VC41](https://rest.uniprot.org/uniprotkb/protnlm/Q9VC41) | Peroxidase-family biology | Name only |
| 19 | [scaf](https://flybase.org/reports/FBgn0033033) | [Q7K5M0](https://rest.uniprot.org/uniprotkb/protnlm/Q7K5M0) | Catalytic versus noncatalytic protease-family control | 1 GO |
| 20 | [MESK2](https://flybase.org/reports/FBgn0043070) | [Q8T0V2](https://rest.uniprot.org/uniprotkb/protnlm/Q8T0V2) | Noncatalytic hydrolase-fold comparator | 1 location |

## Questions to prioritize

- **Catalytic specificity:** alpha-Man-Ia mannose trimming, Pde4 cyclic-nucleotide preference, NTPase nucleotide-diphosphate specificity, and the redox/kinase-family assignments of CG18547 and CG6830. Test the exact emitted name or activity, rather than treating the biological lead as a model prediction.
- **Compartment and topology:** distinguish a secretory enzyme's lumen-facing domain from membrane residence in alpha-Man-Ia and amon; examine the CG3631 Golgi-membrane claim, CG8745 ER-membrane claim and Mrm2 Cytoplasm claim. A location label can be too broad, too specific or mechanistically unsupported for different reasons.
- **Exact product and paralog identity:** the Gpdh3 record is 1,291 residues while its emitted name specifies glycerol-3-phosphate dehydrogenase 1. Its transcript and domain architecture need to be established before deciding whether this is a sound enzyme-family description or a paralog/model problem. Synj and Serinc also require explicit isoform checks.
- **Activity versus assembly or scaffold roles:** CG34117/FMC1 supplies an ATP-synthase-assembly comparison. scaf and MESK2 are enzyme-fold comparators; family membership alone must not imply catalysis. These are ordinary benchmark review cases, not new OpenScientist submissions.
- **Transporter specificity:** use Ctns, CG6836 and Tango5 to distinguish broad membrane/family assignments from substrate and mechanistic claims. Mammalian substrate names are leads to test, not automatic fly annotations.

Each row's bounded review question is preserved in the selection table. The four already submitted [OpenScientist hypotheses](fly-openscientist-selection.md) concern genes from the first cohort and do not overlap this selection.
