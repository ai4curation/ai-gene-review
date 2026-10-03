# guca1c notes (Danio rerio, guanylate cyclase activator 1C, zGCAP3; UniProt Q8UUX9)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Literature found by hand through Europe PMC; pair analysis in
`guca1c-bioinformatics/RESULTS.md`.

Accession Q8UUX9 (TrEMBL, 188 aa), ZFIN:ZDB-GENE-030829-1, Ensembl ENSDARG00000030758, chr15. Paralog guca1d
(zGCAP4, chr21). PANTHER TGD_tree pair (PTHR23055, GUCA1C co-orthologs); Ensembl Compara places the
guca1c/guca1d duplication at Osteoglossocephalai, with one gar ortholog (ENSLOCG00000009269, LG3) for both.

### Name mapping (checked against ZFIN aliases.txt, see RESULTS.md section 0)
- gcap1 = guca1aa (formerly guca1a); gcap2 = guca1b; **gcap3 = guca1c**; **gcap4 = guca1d**;
  gcap5 = guca1ab.1 (formerly guca1e); gcap7 = guca1g. guca1ab.2 (formerly guca1e.2) has no GCAP number.
- Lamb & Hunt call zGCAP3/zGCAP4 "GCAP3a/GCAP3b":
  [PMID:30257895 "A third isoform, GCAP3 (encoded by GUCA1C), occurs in many species, and is expressed only in cones, at least in human and zebrafish [28]; in the latter species, both 3R duplicates (zGCAP3 and zGCAP4, here referred to as GCAP3a and GCAP3b) are cone-specific [24,28,29]."]
- Morales-Camara: [PMID:32422965 "Two orthologous genes—guca1c and guca1d—have been identified in the zebrafish genome on chromosomes 15 and 21, respectively."]

### Expression
- All cone types, not rods: [PMID:11860507 "These results suggest that zGCAP3 is expressed in all four types of cone photoreceptors, but not in rods."]
- Onset 3-4 dpf: [PMID:19168097 "Transcripts of three cone specific guanylate cyclase-activating proteins (zGCAP3, zGCAP4 and zGCAP7) were also detected at 3-4 dpf."]
- Protein: [PMID:22212098 "Using affinity purified antibodies immunoreactivity towards zGCAP3 was weakly detected in the outer and strongly in the inner segments of cone cells as well as in the outer plexiform layer, to a lesser degree also in the inner plexiform and ganglion cell layer of the zebrafish retina."]
- Molar excess over zGC3: [PMID:23940527 "Although transcription and protein expression levels of zGC3 are similar to that of the cyclase regulator guanylate cyclase-activating protein 3 (zGCAP3), we surprisingly found that zGCAP3 is present in a 28-fold molar excess over zGC3 in zebrafish retinae."]
- My reanalysis of adult photoreceptor scRNA-seq (GSE175929, PMID:34462505): guca1c in 100% of cones of every
  type, 57-75 CP10K, about ten times guca1d; rod signal is at the ambient level of gnat2
  (`guca1c-bioinformatics/scrna_output.txt`).
- E-ERAD-475 whole embryo: guca1c 3 TPM, guca1d 5-8 TPM at 3-5 dpf (larval retina is a small fraction of the body).

### Function
- Ca2+-dependent GC activation: [PMID:11860507 "In the GC assay, GCAPs display the expected properties, modulating ROS GCs in a Ca 2+ -dependent manner stimulating at low and inhibiting at high [Ca 2+ ] ( Fig. 9B )."]
- High Ca2+ sensitivity group: [PMID:21829700 "The IC50 values of zGCAPs could be separated in two groups; one group consisting of zGCAP1, 2, and 3 had IC50 values around 30 nM free [Ca2+], the second group of zGCAP4, 5 and 7 had IC50 values between 180 and 520 nM centered around 400 nM (Table 2 and Figure 3)."]
- Native membranes: [PMID:23940527 "The highest activities were measured with zGCAP3 indicating that zGCAP3 is indeed a major activator of zGCs in native zebrafish retinae."]
- Morpholino knockdown, no behavioural defect: [PMID:23940527 "No significant differences in behavioral responses among wild type, morphants and control morphants were found, indicating that a loss of zGCAP3 has no consequences in primary visual processing in the larval retina despite its prominent expression pattern."]
  Authors propose zGCAP4 as substitute: [PMID:23940527 "A good substitute for zGCAP3 might be zGCAP4, because its transcripts are also detected at 3.5 dpf [8] and it is a strong activator of membrane bound GCs with a similar apparent affinity for GCs [17], [20]."]
- CRISPR knockout (NMD-type allele; mRNA below 40% of wild type):
  [PMID:32422965 "We observed that guca1c mRNA levels in homozygous mutant larvae (6 dpf) were less than 40% of the value determined in their wild-type littermates (Figure 5A), in accordance with our hypothesis."]
  Phenotype: [PMID:32422965 "One of the most interesting phenotypic findings in guca1c KO animals was the upregulation of GFAP in Müller cells, and the evidence of apoptosis in some ganglion, indicating the existence of gliosis and glaucoma-like alterations associated with GCAP3 LoF."]
  Caveats: anti-human GUCA1C antibody; the signals vanish in the knockout, [PMID:32422965 "These immunosignals were absent in the KO retina and the negative control, demonstrating their specificity (Figure 7B,C, respectively)."]
  but the rod and ciliary-epithelium staining conflicts with cone-only transcript data; guca1d compensation not tested:
  [PMID:32422965 "Because there is no evidence of functional divergence among these genes, we prioritized guca1c LoF analysis in our study, although possible compensatory phenotypic effects by guca1d on a guca1c KO background cannot be disregarded."]
  No GOA row derives from this paper; I did not propose NEW rows from it.

### Annotation decisions
- Ca2+ binding (IBA, 3 IDA, IEA, ISS): ACCEPT.
- GO:0008048 (IBA, 4 IDA): ACCEPT (core). GO:0030250 ISS: ACCEPT (parent).
- GO:0009966 regulation of signal transduction (IBA, deep NCS node): KEEP_AS_NON_CORE.
- core_functions: GO:0008048; process GO:0031284 positive regulation of guanylate cyclase activity; location
  photoreceptor inner segment (antibody, abstract).
