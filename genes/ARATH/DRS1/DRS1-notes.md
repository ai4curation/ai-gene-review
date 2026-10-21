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

## 2026-10-14 — UNDECIDED rows resolved

Heterochromatin (IBA), Cul4-RING E3 ubiquitin ligase complex (ISS) and regulation of DNA damage checkpoint (IBA) are now KEEP_AS_NON_CORE. There is no target-specific evidence of divergence from the WDR76/CMR1 node. DRS1 carries the DWD motif, and the cached WDR76 paper states that WDR76 associates with Cul4-DDB1 and that yeast CMR1 is involved in a DNA damage checkpoint. All three remain untested in Arabidopsis.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM-derived files in this folder (`DRS1-protnlm-*`, `DRS1-5hmc-prediction-donor.json`) were not opened or used.

### Identity

Q9SAI7 is the single UniProt product of AT1G80710/DRS1 (516 aa; EMBL AEE36439.1, RefSeq NP_178186.1). It is an unreviewed TrEMBL entry but is the canonical, full-length gene product, not an isoform or fragment. Its length matches the yeast ortholog Cmr1 (Q12510, 522 aa); human WDR76 (Q9H967, 626 aa) is longer at the N terminus. UniProt records WD repeats (PROSITE PS50082/PS50294, SMART SM00320 x4) and an N-terminal disordered region (31-102, MobiDB-lite). The UniProt FUNCTION line (5hmC reader) and the DNA-binding/DNA damage keywords are ARBA-only and were not used as evidence.

### Evolutionary grounding

PANTHER PTHR14773 has three subfamilies. DRS1, human WDR76 (Q9H967), mouse Wdr76, Xenopus wdr76 and yeast Cmr1 (Q12510) are all in PTHR14773:SF0 (interpro/panther/PTHR14773/PTHR14773-entries.csv), so they are orthologs and the PAINT node PTN000381277 (WDR76/CMR1) covers DRS1. Gallina et al. 2015 treat WDR76 as the Cmr1 ortholog [PMID:25817432 "WDR76 is the closest orthologue of Cmr1 in higher eukaryotes"]. The IBAs (DNA binding, nucleus, heterochromatin, regulation of DNA damage checkpoint) therefore descend from experimentally grounded donors:
- yeast Cmr1: nuclear, DNA binding in vitro, chromatin accumulation after UV [PMID:25817432 "Cmr1 was described as a histone-related protein11, with DNA-binding capacity in vitro and with the ability to accumulate on chromatin in response to ultraviolet irradiation"]; checkpoint adaptation defect [PMID:25817432 "Deletion of CMR1 causes increased chromosome loss and mutation rates, a defect in DNA-damage checkpoint adaptation"].
- human WDR76: chromatin association and stress foci [PMID:25817432 "WDR76 associated with chromatin in untreated cells and relocalized into nuclear foci under replication stress conditions"]; CBX1/CBX5 co-localization [PMID:27248496].

No plant member has been tested for any of these; no evidence of divergence exists either.

### Decisions (changes from the previous version)

- All actions retained. DNA binding (IBA) and nucleus (IBA, ISM) ACCEPT; heterochromatin, Cul4-RING complex (ISS) and checkpoint regulation KEEP_AS_NON_CORE; drought and ABA IMPs ACCEPT.
- Support for the DNA binding and nucleus rows was wrong in kind: it quoted the CBX co-localization and the DWD motif, neither of which addresses DNA binding. Replaced with Gallina et al. 2015 (yeast Cmr1 DNA binding, nuclear localization), now added as a reference.
- Checkpoint row now cites the Gallina primary result instead of the WDR76 paper's paraphrase of it.
- Added a second core function (conserved nuclear DNA-binding activity, phylogenetically inferred) alongside the drought/ABA core function.
- ABA row now also records that germination ABA response is unaffected, so the term should not be expanded to ABA signaling generally.
- ISS Cul4-RING: noted that the comparator PRL1 is not a DRS1 ortholog; the inference rests on the DWD motif plus the reported Cul4-DDB1 association of the ortholog WDR76.
- Description rewritten to state the subfamily placement and to separate inherited ortholog properties from the DRS1-specific phenotype.

### Relative to review next

Human WDR76 (Q9H967), same PANTHER subfamily (PTHR14773:SF0) and PAINT donor for heterochromatin/nucleus. Yeast Cmr1 (Q12510) is equally an ortholog and is the better-characterized donor. Neither has a review in the repo.

### Family review / modules

interpro/panther/PTHR14773/PTHR14773-review.yaml lists DRS1 as the SF0 representative; no disagreement on subfamily placement. Its SF0 description could add WDR76 and Cmr1 as experimentally characterized representatives. No module in modules/ covers DRS1, WDR76 or Cmr1.
