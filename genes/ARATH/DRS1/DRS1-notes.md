# DRS1 (Q9SAI7): evidence and exact-input prediction review

DRS1 has direct Arabidopsis drought and ABA evidence, despite the generated research report failing to find it. Its proposed role as a specific 5-hydroxymethylcytosine reader is not established: the emitted donor carries an inferred WDR76 function, and the abundance and regulatory significance of genomic 5hmC in Arabidopsis are strongly limited by direct chemical measurements.

## Input identity and functional boundary

Q9SAI7 is AT1G80710/DRS1, a 516-residue WD40 protein placed in PTHR14773:SF0 (WD REPEAT-CONTAINING PROTEIN 76). The 2010 primary paper explicitly identifies AT1G80710 as DRS1 and tests two independent insertion alleles. This is distinct from ABD1 and XIW1. The emitted 5hmC donor Q4KLQ5 is Xenopus laevis wdr76, whose function text is marked ECO:0000250 and is not a direct binding assay.

## Biological evidence

- [PMID:18223036 — Characterization of Arabidopsis and rice DWD proteins and their roles as substrate receptors for CUL4-RING E3 ubiquitin ligases.](https://pubmed.ncbi.nlm.nih.gov/18223036/): 
- [PMID:20118918 — Rational association of genes with traits using a genome-scale gene network for Arabidopsis thaliana.](https://pubmed.ncbi.nlm.nih.gov/20118918/): Two independent Arabidopsis drs1 alleles have deficient water retention and ABA-insensitive transpiration, establishing the target-specific phenotype.

> An independent T-DNA allele (Salk_149366C) that we designate as drs1-2 exhibited the same phenotypes in relative water content following drought and ABA-insensitive water transpiration


> The mutant was insensitive to ABA on water loss whereas the wild type lost significantly less water in the presence of 10 μM ABA


> Drs1 is a WD-40 repeat family protein containing a DWD (DDB1 binding WD40) motif

- [PMID:27248496 — WDR76 Co-Localizes with Heterochromatin Related Proteins and Rapidly Responds to DNA Damage.](https://pubmed.ncbi.nlm.nih.gov/27248496/): Human WDR76 has chromatin-associated localization and a rapid DNA-damage response; these observations define homolog evidence, not an Arabidopsis assay.

> WDR76 co-localizes to puncta with the heterochromatin
> proteins CBX1 and CBX5

- [PMID:25380728 — 5-hydroxymethylcytosine is not present in appreciable quantities in Arabidopsis DNA.](https://pubmed.ncbi.nlm.nih.gov/25380728/): Sensitive assays constrain the amount of genomic 5hmC in the Arabidopsis tissues and genotypes tested, arguing against an assumed abundant canonical 5hmC signaling system.

> Enzymatic radiolabeling and mass spectrometry, the most
> sensitive methods for detection that we used, failed to detect
> 5-hydroxymethylcytosine in A. thaliana genomic DNA

## Exact non-GO claims

The complete emitted record is preserved in [DRS1-protnlm-source.json](DRS1-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> DNA damage-binding protein CMR1

UNC (CS 1) for the full functional name “DNA damage-binding protein CMR1”. A WDR76/CMR1-family relationship is supported, but DRS1-specific binding to damaged DNA has not been demonstrated. The name must not imply the yeast gene itself or substitute a conserved-family hypothesis for the experimentally established Arabidopsis identity. [PMID:20118918](https://pubmed.ncbi.nlm.nih.gov/20118918/); [human homolog study](https://pubmed.ncbi.nlm.nih.gov/27248496/).

### Function

> Specifically binds 5-hydroxymethylcytosine (5hmC), suggesting that it acts as a specific reader of 5hmC

UNC (CS 1). A selective 5hmC-reader function has not been demonstrated for DRS1. The frog Wdr76 donor text is itself an orthology inference. Moreover, sensitive Arabidopsis genomic-DNA assays found no appreciable 5hmC, limiting the proposed physiological reader context. These observations do not show that purified DRS1 cannot bind a synthetic 5hmC-containing DNA substrate, exclude trace oxidative products, or address RNA hydroxymethylcytosine. Thus the claim is not confidently scored as either correct or an absolute biochemical impossibility. [PMID:25380728](https://pubmed.ncbi.nlm.nih.gov/25380728/); [donor record](DRS1-5hmc-prediction-donor.json).

### Location

> Nucleus

CNN (CS 2). The broad nuclear location overlaps the existing IBA/ISM annotations and is consistent with the conserved WDR76/CMR1 branch and experimental nuclear/chromatin localization of the human homolog. This does not validate the more specific 5hmC reader or heterochromatin hypotheses. [PMID:27248496](https://pubmed.ncbi.nlm.nih.gov/27248496/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

PTHR14773 captures a WDR76-related repeat family with broad nuclear DNA/chromatin associations. Conserved localization and broad binding need to be separated from particular base recognition, checkpoint mechanisms and a plant drought phenotype. A DWD motif does not identify a ubiquitination substrate or prove membership in the precise CUL4 complex.

## Evidence limits

The DRS1/AraNet paper, the DWD-family paper and the Arabidopsis 5hmC study have cached full text. The genuine Falcon report missed the direct DRS1 paper and therefore its “no target-specific publication” conclusion is not adopted. The direct evidence supports physiology, while the proposed mechanistic connection through chromatin or a DDB1-CUL4 ligase remains open. The 2013 modified-base-reader study (PMID:23434322) is abstract-only in the cache and is not treated as a direct assay of DRS1.
