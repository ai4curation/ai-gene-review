# metF curation notes

## Evidence

Q88D51 is a compact 295-residue bacterial MetF with EC 1.5.1.54/RHEA:19821,
IPR004620, TIGR00676, FAD, and NAD annotations
[file:PSEPK/metF/metF-uniprot.txt
"DE            EC=1.5.1.54"; "DR   InterPro; IPR004620; MTHF_reductase_bac.";
"DR   NCBIfam; TIGR00676; fadh2; 1."].

Price et al. directly analyzed KT2440 fitness data and reported that the
PP_4977 metF profile was nearly identical to metH (r = 0.96), whereas PP_4638
showed no significant phenotype across 101 experiments
[PMID:33534785
"The fitness pattern for metF from P. putida (PP_4977) is virtually identical
to that of the methionine synthase metH (PP_2375; r = 0.96)"].

## Assessment

The combined bacterial-family, reaction, and organism-level fitness evidence
supports Q88D51 as the physiological NADH-linked MetF. The exact catalytic
activity is accepted, the correct broad NAD(P)H parent is retained as non-core, and
the obsolete/broad methionine-metabolism row is modified to live
GO:0071265 (L-methionine biosynthetic process). The fitness evidence supports
pathway placement but is not a direct enzyme assay.
