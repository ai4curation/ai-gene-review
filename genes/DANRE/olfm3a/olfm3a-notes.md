# olfm3a notes

## Setup and provenance

- Fetched with `just fetch-gene` on A8KB73 (TrEMBL, ZGC cDNA AAI53994.1, 457 aa); 6 GOA rows
  (2 IBA, 2 IEA, 2 ND root-term placeholders), none with a PMID. ZFIN ZDB-GENE-080219-11,
  Ensembl ENSDARG00000071493, chromosome 24 (an alternate-contig copy ENSDARG00000110039 also
  exists).
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid. Literature searched by hand via Europe PMC (`olfm3a`, `olfm3b`,
  `(olfm3 OR noelin-3 OR optimedin) AND zebrafish`, `olfm3 OR optimedin OR "olfactomedin 3"`).
- DANRE_DUPLICATION batch 3 (random draw 10 of seed 20260928); paralog olfm3b.

## Zebrafish literature

No functional study of either copy. The only specific mention is a single-cell atlas of larval
brain, where olfm3a is one of the effector genes shared by glutamatergic clusters
[PMID:34895465 "The first case was a glutamatergic pair cluster from different brain regions: tectal glutamatergic Cluster 1 and hindbrain glutamatergic Cluster 31 shared effector gene profiles including camk2n1a/stmn4/cbln2b/olfm3a/cd63, but differentially expressed TF profiles, atf5b/bhlhe41/lhx1a and ddit3/cebpb/lef1, respectively (Figure 3C)."].
ZFIN has no curated wild-type expression for olfm3a or olfm3b (checked in the ZFIN
wildtype-expression download, 2026-09-28).

## Mammalian OLFM3 (optimedin, noelin-3)

- Secreted olfactomedin-domain glycoprotein of retina, brain and anterior eye
  [PMID:12019210 "Optimedin and noelin are both expressed in brain and retina."];
  [PMID:12019210 "Both optimedin and myocilin are localized in Golgi and are secreted proteins."];
  binds myocilin via the OLF domain and homodimerizes via the N-terminus
  [PMID:12019210 "The C-terminal olfactomedin domains are essential for interaction between optimedin and myocilin, while the N-terminal domains of both proteins are involved in the formation of protein homodimers."].
- Pax6 target with two promoters [PMID:16115881 "There are two major splice variants of the Optimedin mRNA, Optimedin A and Optimedin B, transcribed from different promoters."].
- Overexpression in PC12 cells changes adhesion [PMID:17054946 "Expression of optimedin induced Ca(2+)-dependent aggregation of NGF-stimulated PC12 cells and this aggregation was blocked by the expression of N-cadherin siRNA."].
- Forms heteromers with Olfm1/Olfm2 [PMID:21228389 "Results of the present interaction study show that Olfm1, OLFM2, and Olfm3 proteins form heterodimers in the CLs and CM."].
- Noelins 1-3 are extracellular AMPA-receptor complex constituents; triple KO reduces synaptic
  AMPARs [PMID:37591201 "Knock out of Noelins1-3 profoundly reduced AMPARs in synapses onto excitatory and inhibitory (inter)neurons, decreased their density and clustering in dendrites, and abolished activity-dependent synaptic plasticity."].
  Olfm3 single KO is mild [PMID:37591201 "The behavior of Noe3 KO mice appears normal and preliminary assessment of the brain sections found no defects."];
  Noe3 transcripts are sparse and interneuron-biased in hippocampus.
- OLFM3 co-immunoprecipitates with GluA1/GluA2 and raises seizure susceptibility in mouse
  [PMID:32850838 "We found that OLFM3 co-immunoprecipitation with GluA1 and GluA2."].
- IBA donors for "signal transduction" are myocilin (mouse, human) and mouse Olfm1; no OLFM3
  member donates.

## Own analyses

`olfm3a-bioinformatics/pair_analysis.py` (RESULTS.md, output.txt). Key points:
- olfm3a vs olfm3b 83.2% identity; to human OLFM3 isoform Q96PB7-3 (458 aa) 83.8% / 81.0%.
  Both zebrafish entries have the N-terminus of Q96PB7-3, not of the 478-aa canonical isoform.
- OLF domain 86.6% / 85.0% identical to human; all 6 human cysteines kept in both; the two
  calcium-site residues described for Olfm1 kept in both; N-glycosylation sequons at identical
  positions in the two copies.
- Relative-rate test vs gar not significant (21 vs 32).
- E-ERAD-475: olfm3a rises from prim-25 to 9-11 TPM in larvae; olfm3b stays at 0-1 TPM
  through day 5.
- Synteny: abca4a is ~125 kb from olfm3a (chr24) and its teleost paralogue abca4b ~140 kb from
  olfm3b (chr2); several other chr24/chr2 teleost paralogue pairs (hs6st1, plppr4, agl, hccs).
  Ensembl Compara nonetheless places the olfm3a/olfm3b node at Gnathostomata (PANTHER: TGD_tree).
- Bgee: olfm3a brain, retina, larva, bone; olfm3b brain, intestine, early embryo/blastula,
  ovary, tail, bone (low scores). Gar OLFM3 highest in brain, ovary, eye.

## Curation decisions

Location rows (extracellular region, synapse) accepted; signal transduction IBA marked
over-annotated (donors are myocilin/Olfm1; no OLFM3 evidence). ND rows accepted as accurate
records of absent curated data. No NEW terms.
