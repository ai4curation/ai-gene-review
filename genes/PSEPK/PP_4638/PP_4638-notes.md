# PP_4638 curation notes

## Evidence

The UniProt record transfers an MTHFR name and RHEA:19821 but Q88E30 is 495
residues long, has PF12225/IPR022026 at residues 378-461, and lacks the
IPR004620/TIGR00676 bacterial MetF signatures found in Q88D51
[file:PSEPK/PP_4638/PP_4638-uniprot.txt
"DR   InterPro; IPR022026; DUF5981."; "DR   Pfam; PF12225; DUF5981; 1."].

The reproducible comparison finds only 26.50% identity over 200 aligned
residues between Q88E30 and Q88D51, versus 41.89% identity over 265 residues
between Q88D51 and experimentally characterized E. coli MetF
[file:PSEPK/PP_4638/PP_4638-bioinformatics/RESULTS.md
"Current InterPro matches support an MTHFR-like FAD-linked catalytic domain in
PP_4638"; "They do not independently support the specific NADH-dependent
GO:0106312 activity"].

Most importantly, PP_4638 had no significant phenotype across 101 KT2440
fitness experiments, while PP_4977 metF tracked metH at r = 0.96
[PMID:33534785
"which suggests that PP_4638 did not provide MTHFR activity in these growth
conditions"]. The reverse-direction MTHFR paper concerns BAK65950.1, not
PP_4638, and is used only as a functional-diversity comparator
[PMID:40016375 "Type 4 MTHFRs constitute a distinct family of enzymes"].

## Assessment

The evidence supports an FAD-binding MTHFR-like fold, not equivalence to MetF.
The NADH-specific activity is removed. The broad MTHFR activity,
methionine-process row, and tetrahydrofolate interconversion remain undecided
because the data do not exclude condition-specific methionine involvement or
noncanonical folate chemistry. PP_4638 is therefore not a representative of
either MTHFR reaction leaf in the reusable module.
