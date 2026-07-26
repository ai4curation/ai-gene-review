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

The max3 OpenScientist gene report found no PP_4977-specific biochemical or
structural study and independently recapitulates the target record's compact
NADH-linked MetF assignment. Its unsaved 40.7% alignment and exact residue
mapping, imported non-KT2440 auxotrophy/essentiality and transcriptional
regulation, universal bacterial/eukaryotic cofactor shorthand, and
"housekeeping" division from PP_4638 are not used as target-level evidence
[file:PSEPK/metF/metF-deep-research-openscientist.md
"No PP_4977-specific biochemical or structural study exists"].

The refreshed max3 pathway report maps PP_4977 to the compact NADH-linked
MetF branch and separately holds PP_4638 uncertain. Its assertion that KT2440
has no MetE is false (PP_4637 is outside this batch and owned by PR #2080), so
that downstream statement is not used
[file:projects/P_PUTIDA/deep-research/PSEPK__folate_one_carbon_interconversion__ppu00670-deep-research-openscientist.md
"NADH-linked compact MetF"].

## Assessment

The combined bacterial-family, reaction, and organism-level fitness evidence
supports Q88D51 as the physiological NADH-linked MetF. The exact catalytic
activity is accepted, the correct broad NAD(P)H parent is retained as non-core, and
the obsolete/broad methionine-metabolism row is modified to live
GO:0071265 (L-methionine biosynthetic process). The fitness evidence supports
pathway placement but is not a direct enzyme assay.
