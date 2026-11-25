# PP_3108 (Tke2) notes: review via dashboard protein NZ_SPUT01000035.1_2

Source: https://gene-annotate-dashboard.kbase.us/review/NZ_SPUT01000035.1_2 (P. putida strain KB3, WP_135192713.1, 1409 aa, tier A).
The exact-sequence UniProt entries were deleted, so the review is filed on KT2440 PP_3108 (Q88I91, 1385 aa). The two are 89.9% identical over 1381 aligned pairs.
Analysis: `PP_3108-bioinformatics/` (BERIL run `projects/hackathon/runs/20261030T211644Z-pp3108-tke2-windowed-identity`).

## Conclusion

PP_3108 is Tke2, the PAAR-Rhs "specialized" effector of the KT2440 K1-T6SS. It is encoded in the vgrG1 operon (PP_3106 VgrG1, PP_3107 DUF1795/Eag chaperone, PP_3108 Tke2, PP_3109 Tki2). Bernal et al. 2017 (PMID:28045455) established three things:
- Tke2 is secreted in a K1-T6SS-dependent manner.
- It is toxic when expressed in E. coli.
- Tki2 neutralises it.

Its C-terminal toxin is an HNH/colicin E7-like nuclease domain. That assignment comes from the domain alone; no nuclease assay has been done.

## The dashboard protein is a toxin-swapped allele

Identity along the length is not uniform:

| Query region | Identity to PP_3108 |
|---|---|
| prePAAR 1-58 | 100% |
| PAAR 59-148 | 98.9% |
| Rhs/YD shell 149-1253 | 95.6% |
| C-terminal toxin after DPIGL (1254-1409) | 25% |
| LHH domain 1313-1409 | 21.6%, no significant local similarity (z = 3.3) |

- **Toxin domains.** The query's toxin domain hits Pfam LHH (PF14411) at E = 2.7e-13. The PP_3108 C-terminus does not hit LHH significantly; InterPro places it in the colicin/pyocin DNase superfamily instead.
- **Immunity genes.** The gene downstream of the query (WP_223271142.1) sits in the tki2 position but is not detectably related to Tki2 (18% identity, z = 2.4).
- **Delivery partners.** The Eag chaperone (100% identical to PP_3107) and VgrG (76.2% identical to PP_3106) are conserved.

**Filing on PP_3108 is valid for the delivery and secretion function, but not for the toxin function.** The Tke2 toxicity and Tki2 data, and the colicin-like DNase fold, do not transfer to the query. For the query's LHH toxin, only a domain-level nuclease prediction exists. The dashboard ID is recorded as an alias on PP_3108 with this caveat in the description.

**PAAR motif.** PF05488 is present at residues 69-140 (E = 6e-21), and class I prePAAR (PF25799) at 1-58. The prePAAR region is strongly hydrophobic (residues 13-64). UniProt/Phobius predicts two TM helices there; DeepTMHMM calls the protein globular. This is the class I prePAAR, TMD-containing effector organisation that needs an Eag chaperone, and an Eag gene sits next to it. InterPro labels PF25799 "Double-stranded DNA deaminase toxin A prePAAR motif" after the protein where it was first described. That label implies nothing about deaminase activity, and the dashboard call correctly rejected it.

## Dashboard verdict

**Supported.** The call reads "PAAR-containing Rhs-family type VI secretion system effector protein", with GO:0033103 protein secretion by the T6SS. Both are correct. The GO term is scored COR (2): it is novel, since GOA has only an IEA endonuclease annotation. A more informative annotation would be: "PAAR-Rhs T6SS effector (K1-T6SS Tke2 locus, vgrG1 operon) with a C-terminal LHH-family nuclease toxin domain; toxin differs from KT2440 Tke2; cognate immunity protein WP_223271142.1 (predicted)".

The rationale's statement that the 89.7%-identical homolog is "Tke2" is true but misleading, because the identity is concentrated in the delivery module. The call was right not to assign a nuclease or deaminase activity.

The STRING partners PP_3107/PP_3106/PP_4084 were transferred from PP_3108. PP_3107 and PP_4084 are DUF1795/Eag chaperones and PP_3106 is VgrG1, so they corroborate T6SS delivery and say nothing about the toxin.

## Caveats

- The locus-tag mapping tke2 = PP_3108 is inferred from operon order (vgrG1 operon: PP3104, PP3105, VgrG1, EagR adaptors, Tke2, Tki2; PMID:36748579) and from the UniProt and PaperBLAST mapping. The papers do not state the locus tag in the main text.
- There is no Tke2-specific competition phenotype. Killing was shown for the T6SS as a whole, so GO:0031640 is IC.
- Fitness: `just fetch-fitness` failed, because no FEBA source was reachable. The dashboard evidence holds no fitness data for this protein; its only FB homolog is a P. syringae YD-repeat protein with no measurements.
- PMID:33693029 (Rsm RAP-seq) lists PP_3108 among Rsm-bound RNAs only in its supplement. It bears on regulation, not function, and is not cited.

## Status: DRAFT

What would close it out: (1) a decision on whether the KB3 toxin-swapped allele seen by the dashboard should be reviewed as a separate entry, since the review describes KT2440 Tke2 and the KB3 C-terminal toxin cassette and immunity gene differ; (2) KT2440 fitness data for PP_3108 from the BERDL Fitness Browser copy, which could not be fetched here. Neither is expected to change the GO terms for KT2440 Tke2. (Added after PR #5755 review.)
