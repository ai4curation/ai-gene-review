# FOXC1 source guide

The review covers 143 original QuickGO contexts represented by 141 stored annotations: 37 ACCEPT, 46 KEEP_AS_NON_CORE, 38 TOO_GENERAL, 5 MODIFY and 15 UNDECIDED. It contains one core function, no NEW annotations and no publication quotations. All 40 normal source files are preserved unchanged after acquisition.

The core is selective regulatory DNA binding and positive RNA polymerase II transcription in the nucleus. Developmental, growth, migration and differentiation effects retain their tissue and experimental context. The binding refinements describe supported partner classes; co-complex evidence is not silently promoted to purified binary binding.

## Deterministic projection

The genuine exporter produced 143 TSV rows and the genuine seed contained 141 annotation keys. Original raw rows 36/37 (FLNA, PMID:15684392) share stored row 45; rows 46/47 (DNA bending, PMID:7957066) share stored row 83. The full original objects, assigners, dates, WITH/FROM alternatives, extensions and raw-to-TSV-to-stored joins are retained in [FOXC1-contexts.json](FOXC1-contexts.json). No source-context deletion or guessed replacement was made.

Exactly three original singleton extension groups are serialized: raw 17/stored 16 and raw 99/stored 111 have input NCBI_Gene:2308 (FOXO1; RO:0002233); raw 40/stored 48 occurs in GO:0005634 (nucleus; BFO:0000066). Each expression contains one atom, so no OR/conjunction flattening is needed. Raw 51/stored 122 has no extension.

The target label FOXO1 is the official NCBI Gene:2308 symbol. Predicate labels follow the official Relation Ontology process-relations documentation and BFO term record. The source fields retain the original human target, evidence, qualifier, reference and supporting entities.

## Access and uncertainty

The [source evidence map](FOXC1-source-evidence.md) states original-reading scope separately from normal-cache availability. Original author/publisher/PMC sections sometimes provided stronger access than an unchanged abstract-only cache. A successful HTML response or a file named PDF/XLSX was not treated as source access when its content was a challenge page. Supplementary tables and image pixels are not claimed where uninspected.

Fifteen unresolved rows retain their specific missing evidence: the PMID:11237714 activation assertion; the three PMID:19793056 letter contexts; PMID:14506133 DNA bending; the separate PMID:25609649 PBX1 interaction; mouse negative Pol-II regulation and positive stem/progenitor differentiation; the lens-versus-cornea transfer; and PMID:25808752 core-promoter binding. Successful assays in other papers do not replay those source-specific contexts.

The authentic PMID:11237714 abstract foregrounds DSCAM, but full-text inaccessibility does not establish a wrong-gene error. Mouse Q61572 is Foxc1 and Q61850 is Foxc2; the renal paper directly studies Foxc1 as well as compound dosage. Donor identity or donor count alone does not invalidate a transfer.

## Products and phylogeny

The official reviewed Q12948 record has a 553-aa displayed sequence and no enumerated alternative natural products. Human patient substitutions, engineered deletions, inducible FOXC1 fusions, bacterial GST domains and partner products are not added as natural FOXC1 products.

All six PAINT origins were replayed against the actual tree, MSA and original IBD source. The two donor/date snapshot differences remain intact; the review does not turn an inherited function into a new annotation.

## Original context index

| Raw | Stored | Original context ID | GO | Evidence | Reference | Assigner |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 19 | UniProtKB:Q12948!28906821 | GO:0001654 | IDA | PMID:9792859 | MGI |
| 1 | 79 | UniProtKB:Q12948!28906822 | GO:0007507 | IDA | PMID:10474162 | MGI |
| 2 | 106 | UniProtKB:Q12948!28906823 | GO:0045893 | IDA | PMID:11237714 | MGI |
| 3 | 9 | UniProtKB:Q12948!28906824 | GO:0000976 | ISS | GO_REF:0000024 | BHF-UCL |
| 4 | 8 | UniProtKB:Q12948!28906825 | GO:0000976 | IEA | GO_REF:0000107 | Ensembl |
| 5 | 4 | UniProtKB:Q12948!28906826 | GO:0000976 | IDA | PMID:17210863 | UniProt |
| 6 | 5 | UniProtKB:Q12948!28906827 | GO:0000976 | IDA | PMID:19279310 | UniProt |
| 7 | 6 | UniProtKB:Q12948!28906828 | GO:0000976 | IDA | PMID:25786029 | UniProt |
| 8 | 7 | UniProtKB:Q12948!28906829 | GO:0000976 | IDA | PMID:27804176 | UniProt |
| 9 | 10 | UniProtKB:Q12948!28906830 | GO:0000977 | IDA | PMID:7957066 | NTNU_SB |
| 10 | 11 | UniProtKB:Q12948!28906831 | GO:0000978 | IBA | GO_REF:0000033 | GO_Central |
| 11 | 12 | UniProtKB:Q12948!28906832 | GO:0000978 | IEA | GO_REF:0000107 | Ensembl |
| 12 | 13 | UniProtKB:Q12948!28906833 | GO:0000981 | IBA | GO_REF:0000033 | GO_Central |
| 13 | 14 | UniProtKB:Q12948!28906834 | GO:0000981 | IEA | GO_REF:0000107 | Ensembl |
| 14 | 15 | UniProtKB:Q12948!28906835 | GO:0000981 | ISA | GO_REF:0000113 | NTNU_SB |
| 15 | 18 | UniProtKB:Q12948!28906836 | GO:0001228 | ISS | GO_REF:0000024 | UniProt |
| 16 | 17 | UniProtKB:Q12948!28906837 | GO:0001228 | IEA | GO_REF:0000107 | Ensembl |
| 17 | 16 | UniProtKB:Q12948!28906838 | GO:0001228 | IDA | PMID:17993506 | NTNU_SB |
| 18 | 27 | UniProtKB:Q12948!28906839 | GO:0003677 | IDA | PMID:11179011 | MGI |
| 19 | 28 | UniProtKB:Q12948!28906840 | GO:0003677 | IDA | PMID:15684392 | UniProt |
| 20 | 29 | UniProtKB:Q12948!28906841 | GO:0003677 | IDA | PMID:7957066 | MGI |
| 21 | 38 | UniProtKB:Q12948!28906842 | GO:0003700 | IEA | GO_REF:0000120 | UniProt |
| 22 | 30 | UniProtKB:Q12948!28906843 | GO:0003700 | IDA | PMID:11179011 | MGI |
| 23 | 31 | UniProtKB:Q12948!28906844 | GO:0003700 | IDA | PMID:11782474 | UniProt |
| 24 | 32 | UniProtKB:Q12948!28906845 | GO:0003700 | IDA | PMID:14506133 | UniProt |
| 25 | 33 | UniProtKB:Q12948!28906846 | GO:0003700 | IDA | PMID:14578375 | UniProt |
| 26 | 39 | UniProtKB:Q12948!28906847 | GO:0003700 | IMP | PMID:14578375 | UniProt |
| 27 | 34 | UniProtKB:Q12948!28906848 | GO:0003700 | IDA | PMID:15277473 | UniProt |
| 28 | 35 | UniProtKB:Q12948!28906849 | GO:0003700 | IDA | PMID:15299087 | UniProt |
| 29 | 36 | UniProtKB:Q12948!28906850 | GO:0003700 | IDA | PMID:15684392 | UniProt |
| 30 | 40 | UniProtKB:Q12948!28906851 | GO:0003700 | IMP | PMID:16449236 | UniProt |
| 31 | 41 | UniProtKB:Q12948!28906852 | GO:0003700 | IMP | PMID:17210863 | UniProt |
| 32 | 42 | UniProtKB:Q12948!28906853 | GO:0003700 | IMP | PMID:19279310 | UniProt |
| 33 | 43 | UniProtKB:Q12948!28906854 | GO:0003700 | IMP | PMID:19793056 | UniProt |
| 34 | 44 | UniProtKB:Q12948!28906855 | GO:0003700 | IMP | PMID:25786029 | UniProt |
| 35 | 37 | UniProtKB:Q12948!28906856 | GO:0003700 | IDA | PMID:27804176 | UniProt |
| 36 | 45 | UniProtKB:Q12948!28906857 | GO:0005515 | IPI | PMID:15684392 | UniProt |
| 37 | 45 | UniProtKB:Q12948!28906858 | GO:0005515 | IPI | PMID:15684392 | IntAct |
| 38 | 46 | UniProtKB:Q12948!28906859 | GO:0005515 | IPI | PMID:15684392 | IntAct |
| 39 | 47 | UniProtKB:Q12948!28906860 | GO:0005515 | IPI | PMID:15684392 | UniProt |
| 40 | 48 | UniProtKB:Q12948!28906861 | GO:0005515 | IPI | PMID:16449236 | IntAct |
| 41 | 49 | UniProtKB:Q12948!28906862 | GO:0005515 | IPI | PMID:18676636 | IntAct |
| 42 | 50 | UniProtKB:Q12948!28906863 | GO:0005515 | IPI | PMID:22190034 | IntAct |
| 43 | 51 | UniProtKB:Q12948!28906864 | GO:0005515 | IPI | PMID:25609649 | IntAct |
| 44 | 52 | UniProtKB:Q12948!28906865 | GO:0005515 | IPI | PMID:26565916 | UniProt |
| 45 | 82 | UniProtKB:Q12948!28906866 | GO:0008301 | IDA | PMID:14506133 | UniProt |
| 46 | 83 | UniProtKB:Q12948!28906867 | GO:0008301 | IDA | PMID:7957066 | UniProt |
| 47 | 83 | UniProtKB:Q12948!28906868 | GO:0008301 | IDA | PMID:7957066 | MGI |
| 48 | 104 | UniProtKB:Q12948!28906869 | GO:0043565 | IEA | GO_REF:0000002 | InterPro |
| 49 | 102 | UniProtKB:Q12948!28906870 | GO:0043565 | IDA | PMID:15277473 | UniProt |
| 50 | 103 | UniProtKB:Q12948!28906871 | GO:0043565 | IDA | PMID:7957066 | UniProt |
| 51 | 122 | UniProtKB:Q12948!28906872 | GO:0061629 | IPI | PMID:16449236 | UniProt |
| 52 | 128 | UniProtKB:Q12948!28906873 | GO:0140297 | IPI | PMID:15684392 | UniProt |
| 53 | 138 | UniProtKB:Q12948!28906874 | GO:1990841 | ISS | GO_REF:0000024 | UniProt |
| 54 | 137 | UniProtKB:Q12948!28906875 | GO:1990841 | IEA | GO_REF:0000107 | Ensembl |
| 55 | 1 | UniProtKB:Q12948!28906876 | GO:0000122 | ISS | GO_REF:0000024 | UniProt |
| 56 | 0 | UniProtKB:Q12948!28906877 | GO:0000122 | IEA | GO_REF:0000107 | Ensembl |
| 57 | 20 | UniProtKB:Q12948!28906878 | GO:0001657 | ISS | GO_REF:0000024 | UniProt |
| 58 | 21 | UniProtKB:Q12948!28906879 | GO:0001657 | ISS | GO_REF:0000024 | UniProt |
| 59 | 22 | UniProtKB:Q12948!28906880 | GO:0001756 | IEA | GO_REF:0000107 | Ensembl |
| 60 | 23 | UniProtKB:Q12948!28906881 | GO:0001822 | ISS | GO_REF:0000024 | UniProt |
| 61 | 24 | UniProtKB:Q12948!28906882 | GO:0001822 | ISS | GO_REF:0000024 | UniProt |
| 62 | 26 | UniProtKB:Q12948!28906883 | GO:0001958 | ISS | GO_REF:0000024 | UniProt |
| 63 | 25 | UniProtKB:Q12948!28906884 | GO:0001958 | IEA | GO_REF:0000107 | Ensembl |
| 64 | 77 | UniProtKB:Q12948!28906885 | GO:0006355 | IEA | GO_REF:0000002 | InterPro |
| 65 | 73 | UniProtKB:Q12948!28906886 | GO:0006355 | IDA | PMID:11782474 | UniProt |
| 66 | 74 | UniProtKB:Q12948!28906887 | GO:0006355 | IDA | PMID:14506133 | UniProt |
| 67 | 75 | UniProtKB:Q12948!28906888 | GO:0006355 | IDA | PMID:15299087 | UniProt |
| 68 | 76 | UniProtKB:Q12948!28906889 | GO:0006355 | IDA | PMID:15684392 | UniProt |
| 69 | 78 | UniProtKB:Q12948!28906890 | GO:0006357 | IBA | GO_REF:0000033 | GO_Central |
| 70 | 80 | UniProtKB:Q12948!28906891 | GO:0008283 | IDA | PMID:20406990 | UniProt |
| 71 | 81 | UniProtKB:Q12948!28906892 | GO:0008283 | IMP | PMID:22991501 | UniProt |
| 72 | 84 | UniProtKB:Q12948!28906893 | GO:0009653 | IBA | GO_REF:0000033 | GO_Central |
| 73 | 85 | UniProtKB:Q12948!28906894 | GO:0010628 | IEA | GO_REF:0000107 | Ensembl |
| 74 | 86 | UniProtKB:Q12948!28906895 | GO:0010718 | IMP | PMID:22991501 | UniProt |
| 75 | 88 | UniProtKB:Q12948!28906896 | GO:0014031 | ISS | GO_REF:0000024 | UniProt |
| 76 | 87 | UniProtKB:Q12948!28906897 | GO:0014031 | IEA | GO_REF:0000107 | Ensembl |
| 77 | 89 | UniProtKB:Q12948!28906898 | GO:0016477 | IDA | PMID:20406990 | UniProt |
| 78 | 90 | UniProtKB:Q12948!28906899 | GO:0016477 | IMP | PMID:22991501 | UniProt |
| 79 | 92 | UniProtKB:Q12948!28906900 | GO:0016525 | ISS | GO_REF:0000024 | UniProt |
| 80 | 91 | UniProtKB:Q12948!28906901 | GO:0016525 | IEA | GO_REF:0000107 | Ensembl |
| 81 | 94 | UniProtKB:Q12948!28906902 | GO:0021549 | ISS | GO_REF:0000024 | UniProt |
| 82 | 93 | UniProtKB:Q12948!28906903 | GO:0021549 | IEA | GO_REF:0000107 | Ensembl |
| 83 | 95 | UniProtKB:Q12948!28906904 | GO:0030154 | IBA | GO_REF:0000033 | GO_Central |
| 84 | 97 | UniProtKB:Q12948!28906905 | GO:0036438 | ISS | GO_REF:0000024 | UniProt |
| 85 | 96 | UniProtKB:Q12948!28906906 | GO:0036438 | IEA | GO_REF:0000107 | Ensembl |
| 86 | 99 | UniProtKB:Q12948!28906907 | GO:0038084 | ISS | GO_REF:0000024 | UniProt |
| 87 | 98 | UniProtKB:Q12948!28906908 | GO:0038084 | IEA | GO_REF:0000107 | Ensembl |
| 88 | 100 | UniProtKB:Q12948!28906909 | GO:0042475 | IMP | PMID:12614756 | UniProt |
| 89 | 101 | UniProtKB:Q12948!28906910 | GO:0043388 | IMP | PMID:26565916 | UniProt |
| 90 | 105 | UniProtKB:Q12948!28906911 | GO:0045618 | IMP | PMID:27907090 | UniProt |
| 91 | 107 | UniProtKB:Q12948!28906912 | GO:0045893 | IDA | PMID:15277473 | UniProt |
| 92 | 108 | UniProtKB:Q12948!28906913 | GO:0045893 | NAS | PMID:8499623 | UniProt |
| 93 | 109 | UniProtKB:Q12948!28906914 | GO:0045930 | IDA | PMID:12408963 | UniProt |
| 94 | 120 | UniProtKB:Q12948!28906915 | GO:0045944 | ISS | GO_REF:0000024 | BHF-UCL |
| 95 | 112 | UniProtKB:Q12948!28906916 | GO:0045944 | IMP | PMID:14578375 | UniProt |
| 96 | 110 | UniProtKB:Q12948!28906917 | GO:0045944 | IDA | PMID:16449236 | BHF-UCL |
| 97 | 113 | UniProtKB:Q12948!28906918 | GO:0045944 | IMP | PMID:16492674 | UniProt |
| 98 | 114 | UniProtKB:Q12948!28906919 | GO:0045944 | IMP | PMID:17210863 | UniProt |
| 99 | 111 | UniProtKB:Q12948!28906920 | GO:0045944 | IDA | PMID:17993506 | NTNU_SB |
| 100 | 115 | UniProtKB:Q12948!28906921 | GO:0045944 | IMP | PMID:19279310 | UniProt |
| 101 | 116 | UniProtKB:Q12948!28906922 | GO:0045944 | IMP | PMID:19793056 | UniProt |
| 102 | 117 | UniProtKB:Q12948!28906923 | GO:0045944 | IMP | PMID:25786029 | UniProt |
| 103 | 118 | UniProtKB:Q12948!28906924 | GO:0045944 | IMP | PMID:27804176 | UniProt |
| 104 | 119 | UniProtKB:Q12948!28906925 | GO:0045944 | IMP | PMID:27907090 | UniProt |
| 105 | 121 | UniProtKB:Q12948!28906926 | GO:0048341 | IEA | GO_REF:0000107 | Ensembl |
| 106 | 124 | UniProtKB:Q12948!28906927 | GO:0070098 | ISS | GO_REF:0000024 | UniProt |
| 107 | 123 | UniProtKB:Q12948!28906928 | GO:0070098 | IEA | GO_REF:0000107 | Ensembl |
| 108 | 125 | UniProtKB:Q12948!28906929 | GO:0071364 | IMP | PMID:16492674 | UniProt |
| 109 | 127 | UniProtKB:Q12948!28906930 | GO:0072010 | ISS | GO_REF:0000024 | UniProt |
| 110 | 126 | UniProtKB:Q12948!28906931 | GO:0072010 | IEA | GO_REF:0000107 | Ensembl |
| 111 | 129 | UniProtKB:Q12948!28906932 | GO:0160108 | IEA | GO_REF:0000117 | UniProt |
| 112 | 131 | UniProtKB:Q12948!28906933 | GO:1901491 | ISS | GO_REF:0000024 | UniProt |
| 113 | 130 | UniProtKB:Q12948!28906934 | GO:1901491 | IEA | GO_REF:0000107 | Ensembl |
| 114 | 133 | UniProtKB:Q12948!28906935 | GO:1901534 | ISS | GO_REF:0000024 | UniProt |
| 115 | 132 | UniProtKB:Q12948!28906936 | GO:1901534 | IEA | GO_REF:0000107 | Ensembl |
| 116 | 135 | UniProtKB:Q12948!28906937 | GO:1902038 | ISS | GO_REF:0000024 | UniProt |
| 117 | 134 | UniProtKB:Q12948!28906938 | GO:1902038 | IEA | GO_REF:0000107 | Ensembl |
| 118 | 136 | UniProtKB:Q12948!28906939 | GO:1904798 | ISS | GO_REF:0000024 | UniProt |
| 119 | 140 | UniProtKB:Q12948!28906940 | GO:1990869 | ISS | GO_REF:0000024 | UniProt |
| 120 | 139 | UniProtKB:Q12948!28906941 | GO:1990869 | IEA | GO_REF:0000107 | Ensembl |
| 121 | 54 | UniProtKB:Q12948!28906942 | GO:0005634 | IBA | GO_REF:0000033 | GO_Central |
| 122 | 2 | UniProtKB:Q12948!28906943 | GO:0000785 | ISA | GO_REF:0000113 | NTNU_SB |
| 123 | 3 | UniProtKB:Q12948!28906944 | GO:0000792 | IDA | PMID:15684392 | UniProt |
| 124 | 71 | UniProtKB:Q12948!28906945 | GO:0005634 | IEA | GO_REF:0000120 | UniProt |
| 125 | 56 | UniProtKB:Q12948!28906946 | GO:0005634 | IDA | PMID:11179011 | MGI |
| 126 | 57 | UniProtKB:Q12948!28906947 | GO:0005634 | IDA | PMID:11562355 | MGI |
| 127 | 58 | UniProtKB:Q12948!28906948 | GO:0005634 | IDA | PMID:11782474 | UniProt |
| 128 | 59 | UniProtKB:Q12948!28906949 | GO:0005634 | IDA | PMID:14506133 | UniProt |
| 129 | 60 | UniProtKB:Q12948!28906950 | GO:0005634 | IDA | PMID:14578375 | UniProt |
| 130 | 61 | UniProtKB:Q12948!28906951 | GO:0005634 | IDA | PMID:15277473 | UniProt |
| 131 | 62 | UniProtKB:Q12948!28906952 | GO:0005634 | IDA | PMID:15299087 | UniProt |
| 132 | 53 | UniProtKB:Q12948!28906953 | GO:0005634 | EXP | PMID:15684392 | UniProt |
| 133 | 63 | UniProtKB:Q12948!28906954 | GO:0005634 | IDA | PMID:16449236 | UniProt |
| 134 | 64 | UniProtKB:Q12948!28906955 | GO:0005634 | IDA | PMID:17210863 | UniProt |
| 135 | 65 | UniProtKB:Q12948!28906956 | GO:0005634 | IDA | PMID:19279310 | UniProt |
| 136 | 66 | UniProtKB:Q12948!28906957 | GO:0005634 | IDA | PMID:19793056 | UniProt |
| 137 | 67 | UniProtKB:Q12948!28906958 | GO:0005634 | IDA | PMID:20406990 | UniProt |
| 138 | 68 | UniProtKB:Q12948!28906959 | GO:0005634 | IDA | PMID:25786029 | UniProt |
| 139 | 69 | UniProtKB:Q12948!28906960 | GO:0005634 | IDA | PMID:26565916 | UniProt |
| 140 | 70 | UniProtKB:Q12948!28906961 | GO:0005634 | IDA | PMID:27804176 | UniProt |
| 141 | 55 | UniProtKB:Q12948!28906962 | GO:0005634 | IC | PMID:7957066 | UniProt |
| 142 | 72 | UniProtKB:Q12948!28906963 | GO:0005654 | IDA | GO_REF:0000052 | HPA |

The JSON archive retains the complete original WITH/FROM and extension objects; this table is only an index.

## Review follow-up scope

The source-specific decisions distinguish an established biological function from an independently unresolved source assay. The P297S-letter and PMID:14506133 bending rows retain that uncertainty while explicitly acknowledging UniProt's curated attribution. This does not negate nuclear localization, transcriptional activation or DNA bending supported elsewhere.

The original [PMID:11782474 author-uploaded paper](https://www.researchgate.net/publication/11576656_FOXC1_Transcriptional_Regulation_Is_Mediated_by_N-_and_C-terminal_Activation_Domains_and_Contains_a_Phosphorylated_Transcriptional_Inhibitory_Domain), Results and Figure 5E plus the inhibitory-domain Discussion, distinguishes activation-domain-dependent attenuation from basal SV40 repression. The latter was not observed for the tested GAL4 DNA-binding-domain/inhibitory-region fusion. This narrows the interpretation of UniProt's activator-or-repressor summary without rejecting the experimentally supported inhibitory segment.

For NFIA (raw 39, stored 47), the positive nuclear-extract/probe-array association and the [reviewed NFIA identity/class](https://www.uniprot.org/uniprotkb/Q12857/entry) support GO:0061629. This is a partner-class refinement; the array is not a purified binary assay or the PBX1 co-immunoprecipitation experiment, and it did not establish NFIA-mediated inhibition. The other two supported generic associations remain non-core under the campaign policy where no evidence-backed functional subtype is established.

The two lens-transparency transfers (raw 84/85, stored 97/96) now carry probable WRONG_TERM queries, and stored 97 also records the exact UniProt mouse donor row Q61572!327843743. All request CHECK and remain NOT_REPORTED; no upstream report was sent and no corrected term was guessed. The Ensembl-assigned human IEA row uses resource OTHER with Ensembl named explicitly because the current schema has no ENSEMBL enum. The human ISS and original donor are assigned by UniProt. These queries concern corneal-versus-lens scope, not gene identity or a denial of the positive corneal experiments.

The original GO:1904798 row is a mouse Q61572 similarity transfer traced to PMID:25808752. It is not an experimental human PMID:26565916 row. The separate human evidence does not automatically establish the precise core-promoter scope. Official is_a ancestor queries for GO:0045944 and GO:0045893 exclude GO:0010628, preserving the existing distinction between positive gene expression and those specific transcription terms.
