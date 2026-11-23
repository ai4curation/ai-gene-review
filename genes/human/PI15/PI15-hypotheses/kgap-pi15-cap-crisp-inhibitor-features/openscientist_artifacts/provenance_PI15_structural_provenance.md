# PI15 (O43692) structural provenance tables

## Table 1. TM-align style structural comparison (AlphaFold model, query = PI15 domain)

| query               | ref                  |   ref_len |   TMscore |   aligned |   core_lt5A |   core_RMSD |
|:--------------------|:---------------------|----------:|----------:|----------:|------------:|------------:|
| PI15_CAP(66-211)    | stecrisp_CAP(1WVR_A) |       221 |     0.764 |       131 |         123 |        1.81 |
| PI15_CAP(66-211)    | triflin(1XTA_A)      |       220 |     0.759 |       131 |         122 |        1.83 |
| PI15_CAP(66-211)    | Ves_v_5(1SMB_A)      |       147 |     0.552 |       128 |         101 |        2.71 |
| PI15_CAP(66-211)    | Na-ASP-2(1XX2_A)     |       359 |     0.206 |       146 |          21 |        3.79 |
| PI15_CAP(66-211)    | PSTI_Kazal(1TGS_I)   |        56 |     0.168 |        32 |          20 |        3.25 |
| PI15_CAP(66-211)    | APP_Kunitz(1EAW_B)   |        56 |     0.163 |        10 |          10 |        0.84 |
| PI15_CAP(66-211)    | OMTKY3_Kazal(1CHO_I) |        53 |     0.158 |        29 |          18 |        3.29 |
| PI15_CAP(66-211)    | BPTI_Kunitz(5PTI_A)  |        58 |     0.123 |        21 |          13 |        3.18 |
| PI15_Cterm(212-258) | Na-ASP-2(1XX2_A)     |       359 |     0.164 |        47 |          16 |        3.43 |
| PI15_Cterm(212-258) | PSTI_Kazal(1TGS_I)   |        56 |     0.141 |        18 |          14 |        3.02 |
| PI15_Cterm(212-258) | OMTKY3_Kazal(1CHO_I) |        53 |     0.139 |        15 |          12 |        2.42 |
| PI15_Cterm(212-258) | BPTI_Kunitz(5PTI_A)  |        58 |     0.133 |        27 |          11 |        2.79 |
| PI15_Cterm(212-258) | Ves_v_5(1SMB_A)      |       147 |     0.125 |        25 |          19 |        3.82 |
| PI15_Cterm(212-258) | stecrisp_CAP(1WVR_A) |       221 |     0.122 |        47 |          10 |        3.04 |
| PI15_Cterm(212-258) | triflin(1XTA_A)      |       220 |     0.121 |        47 |          10 |        3.05 |
| PI15_Cterm(212-258) | APP_Kunitz(1EAW_B)   |        56 |     0.115 |        16 |          11 |        2.82 |


## Table 2. Canonical P1 reactive-site-loop scan of all Arg/Lys in mature PI15 (61-258)

Reference spread among four experimentally determined canonical loops: 0.26-0.62 A RMSD.

| label   |   resi | aa   |   loop_rmsd | best_tmpl   |   probe_clash |   outward |        rsa |   plddt |
|:--------|-------:|:-----|------------:|:------------|--------------:|----------:|-----------:|--------:|
| PI15    |    131 | R    |        1.37 | APPI_R15    |             5 |      19.4 | 0.840831   |   87.38 |
| PI15    |    202 | R    |        1.52 | BPTI_K15    |             5 |      25.7 | 0.688832   |   95.5  |
| PI15    |    128 | R    |        1.55 | OMTKY3_L18  |            29 |       8.7 | 0.198009   |   95.56 |
| PI15    |    133 | R    |        1.61 | BPTI_K15    |             5 |      27.4 | 0.850552   |   92.69 |
| PI15    |    164 | R    |        1.69 | APPI_R15    |            11 |      27.6 | 0.370223   |   97.06 |
| PI15    |    203 | R    |        1.83 | PSTI_K18    |             6 |      13.1 | 0.588249   |   95.25 |
| PI15    |    224 | K    |        1.96 | OMTKY3_L18  |             3 |       7.1 | 0.502482   |   98.19 |
| PI15    |     80 | K    |        2.08 | PSTI_K18    |             7 |       7.1 | 0.624328   |   98.19 |
| PI15    |    214 | K    |        2.22 | OMTKY3_L18  |             5 |       6.4 | 0.222243   |   98.25 |
| PI15    |    160 | R    |        2.26 | OMTKY3_L18  |             5 |       2.4 | 0.588776   |   96.81 |
| PI15    |    183 | R    |        2.27 | APPI_R15    |             5 |       8.5 | 0.4268     |   98.62 |
| PI15    |    147 | K    |        2.51 | PSTI_K18    |             3 |       2.4 | 0.675404   |   98.19 |
| PI15    |    119 | R    |        2.74 | PSTI_K18    |             5 |      18.2 | 0.632726   |   95.06 |
| PI15    |    140 | K    |        2.88 | PSTI_K18    |             4 |      15.5 | 0.395032   |   98.38 |
| PI15    |     78 | R    |        2.98 | PSTI_K18    |            58 |      -8.2 | 0.00611005 |   98.81 |
| PI15    |     99 | K    |        3.11 | PSTI_K18    |             3 |      11   | 0.514027   |   96.69 |


## Table 3. Current GO annotations for UniProtKB:O43692 (QuickGO, retrieved 2026-11-23)

| go         |   name | aspect             | ev   | ref            | src        | wf                                                                                                                                                                  | qual         |
|:-----------|-------:|:-------------------|:-----|:---------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| GO:0060090 |    nan | molecular_function | IBA  | GO_REF:0000033 | GO_Central | MGI:1916536;PTN000036124                                                                                                                                            | enables      |
| GO:0005576 |    nan | cellular_component | IBA  | GO_REF:0000033 | GO_Central | CAL0000174557;CAL0000185546;CAL0000190649;FBgn0250842;MGI:1916536;MGI:1921366;MGI:1926142;PTN000036124;S000001721;S000003614;S000003615;A5D8T8;O43692;P54108;Q6UXB8 | is_active_in |
| GO:0005576 |    nan | cellular_component | IEA  | GO_REF:0000120 | UniProt    | IPR018244;SL-0243                                                                                                                                                   | located_in   |
| GO:0005576 |    nan | cellular_component | EXP  | PMID:8882727   | UniProt    | nan                                                                                                                                                                 | located_in   |
| GO:0070062 |    nan | cellular_component | HDA  | PMID:23533145  | UniProt    | nan                                                                                                                                                                 | located_in   |


## Table 4. Disulfide connectivity in the AlphaFold model

| bond | Cys-Cys | S-S distance (A) | domain |
|---|---|---|---|
| 1 | 108-191 | 2.03 | CAP |
| 2 | 157-161 | 2.04 | CAP |
| 3 | 165-170 | 2.04 | CAP |
| 4 | 186-209 | 2.04 | CAP |
| 5 | 229-240 | 2.03 | C-terminal Cys-rich |
| 6 | 232-245 | 2.02 | C-terminal Cys-rich |


C-terminal domain pattern is 1-3 / 2-4, matching neither Kunitz (1-6,2-4,3-5), Kazal (1-5,2-4,3-6) nor WAP (1-6,2-7,3-5,4-8).
