# GTPBP1 (GP-1) — research notes

UniProt: O00178. TRAFAC-class translation-factor GTPase, GTPBP1 subfamily; closely related to eEF1A, eRF3, Hbs1.

## Core function (PMID:30108131, Zinoviev et al. 2018)
- GTPBP1 has **eEF1A-like elongation activity**: forms ternary complexes with GTP + aa-tRNA and delivers cognate aa-tRNA to the ribosomal A site in a GTP-dependent manner.
  [PMID:30108131 "GTPBP1 possesses eEF1A-like elongation activity, delivering cognate aminoacyl-transfer RNA (aa-tRNA) to the"]
- After GTP hydrolysis, peptide bond formation is NOT rapid; GTPBP1 retains aa-tRNA, delaying A-site accommodation → ribosome stalling → triggers quality-control programs, e.g. recruiting the **exosome** to degrade faulty mRNAs in elongation complexes.
  [file:human/GTPBP1/GTPBP1-uniprot.txt "after GTP hydrolysis, which is not immediately followed by rapid peptide bond formation, GTPBP1 likely retains aa-tRNA in the A site and promotes exosomal degradation of faulty mRNAs engaged in 80S elongation complexes"]
- Can also deliver deacylated tRNA to the A site (relevant under stress).
- aa-tRNA binding stabilizes GTP binding and stimulates GTP hydrolysis.
- Interacts with exosome subunits (EXOSC2/3/5) and HNRNPD/R, SYNCRIP; involved in circadian mRNA stability (by similarity).
- Disease: NEDFET1 (autosomal recessive neurodevelopmental disorder) [PMID:38118446].

## Annotations
- IDA-supported (PMID:30108131): GTPase activity, GTP binding, tRNA binding (GO:0000049), alpha-aminoacyl-tRNA binding (GO:1904678), translation elongation factor activity (GO:0003746), cytoplasmic translation (GO:0002181), RNA surveillance (GO:0071025).
- Exosome (cytoplasmic exosome RNase complex GO:0000177) part_of (IEA/ISS) — GTPBP1 associates with but is not a stoichiometric core exosome subunit; better as a functional association. Mark over-annotated/keep non-core.
- PMID:9070279 (original GP-1 cloning, IFN-gamma induced): immune response, signal transduction, GTP binding — TAS. Immune response/signal transduction are dated, indirect; keep non-core / over-annotated.
- HDA RNA binding (PMID:22658674 mRNA interactome) — consistent with tRNA/RNA binding; keep non-core.

## Action plan
- Core MF: GO:0003746 translation elongation factor activity (eEF1A-like aa-tRNA delivery); GO:0003924 GTPase activity. Core BP: GO:0071025 RNA surveillance / GO:0061014 positive regulation of mRNA catabolic process.
- translational elongation GO:0006414 / cytoplasmic translation: keep as the elongation-factor context (accept/non-core).
