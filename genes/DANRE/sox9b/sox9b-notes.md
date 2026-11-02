# sox9b (Q9DFH1) curation notes

## 2026-09-27 — initial review (DANRE_DUPLICATION project, pair sox9a/sox9b)

### Identity and protein
- TGD co-ortholog of SOX9 with sox9a; 407 aa, HMG box 91-159. HMG box 98.6% identical to Sox9a/human SOX9; whole protein 56.8% identical to human SOX9 (see file genes/DANRE/sox9a/sox9a-bioinformatics/RESULTS.md). Sox9b is the more diverged copy, with divergence concentrated C-terminal to the HMG box.
- [PMID:11180959 "Both Sox9a and Sox9b proteins bind to the HMG consensus DNA sequences in vitro."]
- Nuclear protein: [PMID:27565026 "As can be seen in Figure 6A, Sox9b co-localized to nuclear mCherry within CACs."]

### Alleles (important for interpreting annotations)
- b971 is a multi-gene deletion: [PMID:19210963 "The b971 mutant allele of sox9b used in this study deletes sox9b and some surrounding genes including sox8"]; [PMID:22719264 "the chromosomal deletion which underlies the b971 lesion removes eleven other genes, greatly limiting the use of this allele to study the function of Sox9b."]
- fh313 nonsense allele (K68 stop, before the HMG box) used by Delous 2012, Manfroid 2012, Huang 2016.
- Lin et al. 2021 (no PMID; via sox9b-deep-research-falcon.md): CRISPR sox9b frameshift alleles reported grossly normal cartilage. Unverified here; possible genetic compensation.

### Copy-specific functions (sox9a not expressed / not required)
- Ducts: [PMID:22719264 "As in wild-type, sox9a expression appears to be excluded from the digestive organs in sox9bfh313 mutants, suggesting that sox9a expression does not compensate for the reduction of Sox9b function in these mutants."]
- Retina: [PMID:19210963 "In contrast, sox9a mutant retinas had no obvious defects, even though sox9a is expressed in the inner nuclear layer at 68 hpf"]
- Heart: [PMID:23775563 "Furthermore, sox9b is required for PE, epicardium, and valve formation."]; cardiomyocyte requirement [PMID:30224706 "We generated a dominant-negative sox9b (dnsox9b) to inhibit sox9b target gene expression and used the Gal4/UAS system to drive dnsox9b specifically in cardiomyocytes."]
- Endocrine progenitors: [PMID:27565026 "Importantly, Sox9b activity is necessary and sufficient for RA signaling to impart this effect."]
- Liver regeneration: [PMID:24315993 "this process required Notch signaling and, in turn, activation of Sox9b in cholangiocytes."]
- Oocytes: [PMID:15939378 "sox9b was expressed in a complementary fashion in the ooplasm of oocytes"]
- Dosage sensitivity: [PMID:18784347 "Loss of a single copy of the sox9b gene in sox9b(+/-) heterozygotes increased sensitivity to jaw malformation by TCDD."]

### Annotation decisions
- regeneration (IMP, PMID:24315993): MODIFY -> GO:0097421 liver regeneration.
- melanocyte and iridophore differentiation (IMP, PMID:15689370): UNDECIDED (abstract-only; b971 deletion caveat).
- hepaticobiliary system development and pancreas development: ACCEPT (copy-specific core).
- heart valve, proepicardium, epicardium, retina, endocrine pancreas, beta-cell differentiation, otic, fin, palate: KEEP_AS_NON_CORE.
- oligodendrocyte differentiation IBA: KEEP_AS_NON_CORE (expressed in glial progenitor domains; not tested directly).
- NEW GO:0001228 (as for sox9a).
- Deep research file arrived during the review and was used (Lin 2021 caveat, Gawdzik 2018 lead).
