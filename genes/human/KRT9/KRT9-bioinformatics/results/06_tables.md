## T1 Domain architecture and composition (01_KRT9_domains.tsv)

| domain | start | end | length | pct_G | pct_S | pct_G_plus_S | pct_aromatic_FYW | pct_charged_DEKR | shannon_entropy_bits | top_residues |
|---|---|---|---|---|---|---|---|---|---|---|
| Head | 1 | 152 | 152 | 48 | 21.7 | 69.7 | 13.2 | 5.92 | 2.44 | G:73,S:33,F:13,R:8 |
| Coil 1A | 153 | 188 | 36 | 0 | 8.33 | 8.33 | 5.56 | 33.3 | 3.64 | E:5,L:5,N:4,K:3 |
| Linker 1 | 189 | 207 | 19 | 5.26 | 5.26 | 10.5 | 21.1 | 21.1 | 3.26 | Y:4,K:3,P:2,A:2 |
| Coil 1B | 208 | 299 | 92 | 3.26 | 2.17 | 5.43 | 3.26 | 34.8 | 3.77 | L:14,D:12,E:9,K:7 |
| Linker 12 | 300 | 322 | 23 | 13 | 4.35 | 17.4 | 0 | 21.7 | 3.52 | T:3,G:3,N:3,V:3 |
| Coil 2 | 323 | 461 | 139 | 3.6 | 7.91 | 11.5 | 3.6 | 29.5 | 3.78 | E:22,Q:19,L:16,I:11 |
| Tail | 462 | 623 | 162 | 56.8 | 22.2 | 79 | 6.79 | 8.03 | 2.08 | G:92,S:36,Y:9,E:5 |
| full length | 1 | 623 | 623 | 28.4 | 14 | 42.4 | 7.22 | 18.6 | 3.61 | G:177,S:87,E:42,L:41 |

## T2 Coiled-coil register per coil segment (01_KRT9_architecture.json)

| segment | start | end | length | n_core_positions | core_fraction_apolar_LIVMFAYWC | n_discontinuities |
|---|---|---|---|---|---|---|
| Coil 1A | 153 | 188 | 36 | 11 | 0.818 | 0 |
| Coil 1B | 208 | 299 | 92 | 27 | 0.704 | 0 |
| Coil 2 | 323 | 461 | 139 | 40 | 0.75 | 2 |

| segment | after_residue | before_residue | position_before | position_after | residues_to_insert_to_restore_heptad | class | residues_from_segment_end | context |
|---|---|---|---|---|---|---|---|---|
| Coil 2 | 342 | 343 | b | b | 1 | skip (1-residue insertion equivalent) | 119 | KNRKDIENQYETQI |
| Coil 2 | 405 | 406 | a | e | 4 | stutter (4-residue insertion / 3-residue deletion equivalent) | 56 | EDTKNRYCGQLQMI |

## T3 Disease-set variants (02_variants_merged.tsv, 04_conservation_per_residue.tsv)

| variant | ref check | domain | heptad | offset from 1A start | offset to coil 2 end | UniProt disease | ClinVar classification | ClinVar review status | gnomAD AC | gnomAD AF | type I identity | ortholog identity | other keratin genes with disease variant at column | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| p.Met157Arg | OK | Coil 1A | a | 4 | 304 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Lys | OK | Coil 1A | a | 4 | 304 | EPPK1 | Pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Thr | OK | Coil 1A | a | 4 | 304 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Val | OK | Coil 1A | a | 4 | 304 | EPPK1 | Pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Leu160Phe | OK | Coil 1A | d | 7 | 301 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 7 | ClinVar;UniProt |
| p.Leu160Pro | OK | Coil 1A | d | 7 | 301 | - | Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 7 | ClinVar |
| p.Leu160Val | OK | Coil 1A | d | 7 | 301 | EPPK1 | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 7 | ClinVar;UniProt |
| p.Asn161His | OK | Coil 1A | e | 8 | 300 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Ile | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Lys | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Ser | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | criteria provided, multiple submitters, no conflicts | 2 | 1.37e-06 | 1 | 1 | 11 | ClinVar;UniProt;gnomAD |
| p.Asn161Tyr | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Arg163Gln | OK | Coil 1A | g | 10 | 298 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 5 | 3.10e-06 | 1 | 1 | 6 | ClinVar;UniProt;gnomAD |
| p.Arg163Gly | OK | Coil 1A | g | 10 | 298 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 6 | ClinVar |
| p.Arg163Leu | OK | Coil 1A | g | 10 | 298 | - | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 6 | ClinVar |
| p.Arg163Pro | OK | Coil 1A | g | 10 | 298 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 6 | ClinVar;UniProt |
| p.Arg163Trp | OK | Coil 1A | g | 10 | 298 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 6 | ClinVar;UniProt |
| p.Tyr167Asn | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167Asp | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167Ser | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167delinsTrpLeu | OK | Coil 1A | d | 14 | 294 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 4 | ClinVar;UniProt |
| p.Leu168Ser | OK | Coil 1A | e | 15 | 293 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 0.8 | 8 | ClinVar;UniProt |
| p.Val171Gly | OK | Coil 1A | a | 18 | 290 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Val171Met | OK | Coil 1A | a | 18 | 290 | EPPK1 | Pathogenic | no assertion criteria provided | 1 | 6.84e-07 | 1 | 1 | 4 | ClinVar;UniProt;gnomAD |
| p.Gln172Pro | OK | Coil 1A | b | 19 | 289 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 0 | 0.7 | 2 | ClinVar;UniProt |
| p.Cys406Arg | OK | Coil 2 | e | 253 | 55 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 835 | 5.17e-04 | 0.333 | 0.889 | 0 | ClinVar;UniProt;gnomAD |
| p.Tyr454His | OK | Coil 2 | d | 301 | 7 | EPPK1 | Pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 5 | ClinVar;UniProt |
| p.Leu458Phe | OK | Coil 2 | a | 305 | 3 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 6 | 4.10e-06 | 0.889 | 1 | 8 | ClinVar;UniProt;gnomAD |
| p.Leu458Pro | OK | Coil 2 | a | 305 | 3 | EPPK1 | (no ClinVar record) |  | 0 |  | 0.889 | 1 | 8 | UniProt;gnomAD |
| p.Tyr558Ter | OK | Tail |  | 405 | -97 | - | Pathogenic | criteria provided, single submitter | 0 |  |  | 0.7 | 0 | ClinVar |

## T4 Missense variants per domain (03_domain_distribution.tsv)

| domain | length | ClinVar P/LP | UniProt disease | disease set (union) | disease positions | gnomAD missense (not in disease set) | gnomAD missense positions | gnomAD missense AC | gnomAD synonymous | gnomAD in-frame indels | gnomAD in-frame indel AC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Head | 152 | 0 | 0 | 0 | 0 | 243 | 127 | 8614 | 91 | 16 | 35 |
| Coil 1A | 36 | 20 | 17 | 24 | 8 | 27 | 18 | 547 | 19 | 0 | 0 |
| Linker 1 | 19 | 0 | 0 | 0 | 0 | 26 | 14 | 362 | 9 | 2 | 10 |
| Coil 1B | 92 | 0 | 0 | 0 | 0 | 114 | 62 | 1425 | 34 | 0 | 0 |
| Linker 12 | 23 | 0 | 0 | 0 | 0 | 31 | 20 | 222 | 12 | 0 | 0 |
| Coil 2 | 139 | 1 | 4 | 4 | 3 | 171 | 107 | 7146 | 74 | 0 | 0 |
| Tail | 162 | 0 | 0 | 0 | 0 | 193 | 123 | 2090 | 85 | 18 | 1115 |
| full length | 623 | 21 | 21 | 28 | 11 | 805 | 471 | 20406 | 324 | 36 | 1160 |

## T5 Enrichment tests (03_enrichment_tests.tsv)

| case_set | level | region | region_length | case_in | case_out | control_in | control_out | fisher_odds_ratio | fisher_p_two_sided | binomial_p_vs_length_fraction_greater |
|---|---|---|---|---|---|---|---|---|---|---|
| disease | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 24 | 4 | 11 | 794 | 433 | 5.64e-34 | 2.59e-32 |
| disease | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 8 | 3 | 6 | 463 | 206 | 7.27e-12 | 1.71e-10 |
| disease | variants | helix termination segment (last 20 of Coil 2) | 20 | 3 | 25 | 21 | 784 | 4.48 | 0.0429 | 0.0597 |
| disease | positions | helix termination segment (last 20 of Coil 2) | 20 | 2 | 9 | 14 | 455 | 7.22 | 0.0481 | 0.0468 |
| disease | variants | both boundary segments (20+20 residues) | 40 | 27 | 1 | 32 | 773 | 652 | 3.02e-33 | 1.67e-31 |
| disease | positions | both boundary segments (20+20 residues) | 40 | 10 | 1 | 20 | 449 | 224 | 1.95e-12 | 1.23e-11 |
| disease | variants | Coil 1A (whole) | 36 | 24 | 4 | 27 | 778 | 173 | 2.87e-28 | 3.13e-26 |
| disease | positions | Coil 1A (whole) | 36 | 8 | 3 | 17 | 452 | 70.9 | 2.45e-09 | 1.75e-08 |
| disease | variants | rod coils (1A+1B+2) | 267 | 28 | 0 | 312 | 493 | inf | 6.40e-12 | 4.97e-11 |
| disease | positions | rod coils (1A+1B+2) | 267 | 11 | 0 | 185 | 284 | inf | 4.44e-05 | 8.96e-05 |
| disease | variants | heptad a/d positions of rod coils | 78 | 15 | 13 | 93 | 712 | 8.83 | 1.73e-07 | 2.16e-07 |
| disease | positions | heptad a/d positions of rod coils | 78 | 6 | 5 | 51 | 418 | 9.84 | 6.28e-04 | 0.00101 |
| clinvar_plp | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 20 | 1 | 11 | 796 | 1447 | 2.35e-31 | 2.75e-29 |
| clinvar_plp | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 8 | 1 | 6 | 465 | 620 | 4.05e-13 | 9.86e-12 |
| clinvar_plp | variants | helix termination segment (last 20 of Coil 2) | 20 | 1 | 20 | 22 | 785 | 1.78 | 0.451 | 0.496 |
| clinvar_plp | positions | helix termination segment (last 20 of Coil 2) | 20 | 1 | 8 | 15 | 456 | 3.8 | 0.265 | 0.255 |
| clinvar_plp | variants | both boundary segments (20+20 residues) | 40 | 21 | 0 | 33 | 774 | inf | 1.81e-27 | 9.10e-26 |
| clinvar_plp | positions | both boundary segments (20+20 residues) | 40 | 9 | 0 | 21 | 450 | inf | 4.14e-12 | 1.85e-11 |
| clinvar_plp | variants | Coil 1A (whole) | 36 | 20 | 1 | 27 | 780 | 578 | 2.65e-26 | 3.42e-24 |
| clinvar_plp | positions | Coil 1A (whole) | 36 | 8 | 1 | 17 | 454 | 214 | 1.43e-10 | 1.06e-09 |
| clinvar_plp | variants | rod coils (1A+1B+2) | 267 | 21 | 0 | 314 | 493 | inf | 3.80e-09 | 1.87e-08 |
| clinvar_plp | positions | rod coils (1A+1B+2) | 267 | 9 | 0 | 187 | 284 | inf | 2.82e-04 | 4.88e-04 |
| clinvar_plp | variants | heptad a/d positions of rod coils | 78 | 11 | 10 | 94 | 713 | 8.34 | 9.80e-06 | 1.24e-05 |
| clinvar_plp | positions | heptad a/d positions of rod coils | 78 | 5 | 4 | 52 | 419 | 10.1 | 0.00173 | 0.0025 |
| uniprot | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 17 | 4 | 11 | 794 | 307 | 1.32e-24 | 2.16e-22 |
| uniprot | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 7 | 3 | 6 | 463 | 180 | 1.81e-10 | 3.87e-09 |
| uniprot | variants | helix termination segment (last 20 of Coil 2) | 20 | 3 | 18 | 21 | 784 | 6.22 | 0.0203 | 0.0286 |
| uniprot | positions | helix termination segment (last 20 of Coil 2) | 20 | 2 | 8 | 14 | 455 | 8.12 | 0.0403 | 0.0391 |
| uniprot | variants | both boundary segments (20+20 residues) | 40 | 20 | 1 | 32 | 773 | 483 | 3.57e-25 | 2.79e-23 |
| uniprot | positions | both boundary segments (20+20 residues) | 40 | 9 | 1 | 20 | 449 | 202 | 2.84e-11 | 1.75e-10 |
| uniprot | variants | Coil 1A (whole) | 36 | 17 | 4 | 27 | 778 | 122 | 3.91e-20 | 4.27e-18 |
| uniprot | positions | Coil 1A (whole) | 36 | 7 | 3 | 17 | 452 | 62 | 3.43e-08 | 2.21e-07 |
| uniprot | variants | rod coils (1A+1B+2) | 267 | 21 | 0 | 312 | 493 | inf | 3.52e-09 | 1.87e-08 |
| uniprot | positions | rod coils (1A+1B+2) | 267 | 10 | 0 | 185 | 284 | inf | 1.09e-04 | 2.09e-04 |
| uniprot | variants | heptad a/d positions of rod coils | 78 | 10 | 11 | 93 | 712 | 6.96 | 6.47e-05 | 8.91e-05 |
| uniprot | positions | heptad a/d positions of rod coils | 78 | 5 | 5 | 51 | 418 | 8.2 | 0.00293 | 0.00449 |

### T5b Window-size sensitivity, disease set, variant level

| region | region_length | case_in | case_out | control_in | control_out | fisher_odds_ratio | fisher_p_two_sided | binomial_p_vs_length_fraction_greater |
|---|---|---|---|---|---|---|---|---|
| helix initiation segment (first 10 of Coil 1A) | 10 | 12 | 16 | 10 | 795 | 59.6 | 7.62e-14 | 7.01e-15 |
| helix termination segment (last 10 of Coil 2) | 10 | 3 | 25 | 9 | 796 | 10.6 | 0.00612 | 0.01 |
| helix initiation segment (first 15 of Coil 1A) | 15 | 20 | 8 | 11 | 794 | 180 | 2.81e-26 | 1.11e-26 |
| helix termination segment (last 15 of Coil 2) | 15 | 3 | 25 | 13 | 792 | 7.31 | 0.0142 | 0.0292 |
| helix initiation segment (first 20 of Coil 1A) | 20 | 24 | 4 | 11 | 794 | 433 | 5.64e-34 | 2.59e-32 |
| helix termination segment (last 20 of Coil 2) | 20 | 3 | 25 | 21 | 784 | 4.48 | 0.0429 | 0.0597 |
| helix initiation segment (first 25 of Coil 1A) | 25 | 24 | 4 | 17 | 788 | 278 | 1.99e-31 | 5.32e-30 |
| helix termination segment (last 25 of Coil 2) | 25 | 3 | 25 | 26 | 779 | 3.6 | 0.0692 | 0.101 |
| helix initiation segment (first 30 of Coil 1A) | 30 | 24 | 4 | 24 | 781 | 195 | 4.09e-29 | 4.09e-28 |
| helix termination segment (last 30 of Coil 2) | 30 | 3 | 25 | 30 | 775 | 3.1 | 0.0945 | 0.15 |

## T6 gnomAD constraint (03_statistics.json)

| metric | value |
|---|---|
| pLI | 5.47e-08 |
| oe_lof | 0.661 |
| oe_lof_lower | 0.503 |
| oe_lof_upper | 0.88 |
| obs_lof | 34 |
| exp_lof | 51.4 |
| lof_z | 2.06 |
| oe_mis | 0.953 |
| oe_mis_lower | 0.898 |
| oe_mis_upper | 1.01 |
| obs_mis | 753 |
| exp_mis | 790 |
| mis_z | 0.566 |
| oe_syn | 1.01 |
| obs_syn | 292 |
| exp_syn | 290 |
| syn_z | -0.0821 |

| set | n_variants | total_allele_count | cumulative_allele_frequency | homozygotes | max_af | max_af_variant | by_consequence |
|---|---|---|---|---|---|---|---|
| plof_HC_pass | 84 | 247 | 2.33e-04 | 1 | 2.05e-05 | 17-41568626-TG-T | frameshift_variant:42, splice_acceptor_variant:6, splice_donor_variant:10, stop_gained:26 |
| plof_HC_pass_without_loftee_flags | 79 | 237 | 2.20e-04 | 1 | 2.05e-05 | 17-41568626-TG-T | frameshift_variant:40, splice_acceptor_variant:6, splice_donor_variant:10, stop_gained:23 |

ClinVar truncating records:

| variant | domain | classification | review_status | conditions | gnomad_ac |
|---|---|---|---|---|---|
| p.Lys170Ter | Coil 1A | not provided | no classification provided | not provided | 0 |
| p.Asn303fs | Linker 12 | Uncertain significance | criteria provided, single submitter | not provided | 0 |
| p.Glu381Ter | Coil 2 | Uncertain significance | no assertion criteria provided | Prostate cancer | 0 |
| p.Gln428Ter | Coil 2 | Uncertain significance | criteria provided, single submitter | Epidermolytic palmoplantar keratoderma, 1 | 0 |
| p.His550fs | Tail | Uncertain significance | no assertion criteria provided | not provided | 0 |
| p.Tyr558Ter | Tail | Pathogenic | criteria provided, single submitter | not provided | 0 |
| p.Gly584fs | Tail | Uncertain significance | criteria provided, single submitter | not provided | 0 |

Disease-set variants present in gnomAD:

| variant | gnomad_ac | gnomad_af | gnomad_homozygotes | clinvar |
|---|---|---|---|---|
| p.Asn161Ser | 2 | 1.37e-06 | 0 | Pathogenic |
| p.Arg163Gln | 5 | 3.10e-06 | 0 | Pathogenic/Likely pathogenic |
| p.Val171Met | 1 | 6.84e-07 | 0 | Pathogenic |
| p.Cys406Arg | 835 | 5.17e-04 | 5 | Conflicting classifications of pathogenicity |
| p.Leu458Phe | 6 | 4.10e-06 | 0 | Conflicting classifications of pathogenicity |

Ten most frequent gnomAD missense variants:

| variant | domain | gnomad_ac | gnomad_af | clinvar | disease_set |
|---|---|---|---|---|---|
| p.Ser82Asn | Head | 5419 | 0.00336 | Likely benign | no |
| p.Arg374Trp | Coil 2 | 3780 | 0.00234 | Conflicting classifications of pathogenicity | no |
| p.Ser366Gly | Coil 2 | 1317 | 8.16e-04 | Conflicting classifications of pathogenicity | no |
| p.Cys406Arg | Coil 2 | 835 | 5.17e-04 | Conflicting classifications of pathogenicity | yes |
| p.Arg233Cys | Coil 1B | 634 | 3.93e-04 | Conflicting classifications of pathogenicity | no |
| p.Asp180Glu | Coil 1A | 455 | 2.82e-04 | Benign/Likely benign | no |
| p.Arg34His | Head | 342 | 2.12e-04 | Uncertain significance | no |
| p.Gly507Arg | Tail | 331 | 2.09e-04 | Uncertain significance | no |
| p.Gly507Val | Tail | 331 | 2.09e-04 | Uncertain significance | no |
| p.Arg446Trp | Coil 2 | 295 | 1.83e-04 | Uncertain significance | no |

## T7 Conservation by region (04_region_conservation.tsv)

| region | n_residues | mean_typeI_identity | mean_all_keratin_identity | mean_ortholog_identity | n_invariant_in_typeI | n_positions_with_other_keratin_disease_variant |
|---|---|---|---|---|---|---|
| helix initiation segment (first 20 of Coil 1A) | 20 | 0.744 | 0.589 | 0.86 | 10 | 18 |
| helix termination segment (last 20 of Coil 2) | 20 | 0.61 | 0.573 | 0.783 | 6 | 13 |
| other rod coil residues | 227 | 0.482 | 0.354 | 0.786 | 21 | 30 |
| disease-variant positions | 12 | 0.838 | 0.607 | 0.924 | 8 | 10 |
| Head | 152 | 0.33 | 0.302 | 0.75 | 9 | 15 |
| Coil 1A | 36 | 0.678 | 0.542 | 0.806 | 15 | 27 |
| Linker 1 | 19 | 0.324 | 0.21 | 0.647 | 0 | 1 |
| Coil 1B | 92 | 0.523 | 0.386 | 0.804 | 10 | 5 |
| Linker 12 | 23 | 0.411 | 0.292 | 0.813 | 1 | 8 |
| Coil 2 | 139 | 0.459 | 0.348 | 0.778 | 12 | 29 |
| Tail | 162 | 0.286 | 0.265 | 0.719 | 23 | 3 |

## T8 Conservation and cross-keratin disease variants at disease-set positions (04_variant_conservation.tsv)

| position | residue | heptad | typeI_identity | typeI_residue_counts | ortholog_identity | ortholog_residue_counts | aligned_residues_other_keratins | n_other_keratin_genes_with_disease_variant_at_column | hotspot_rank_by_genes | other_keratin_disease_variants |
|---|---|---|---|---|---|---|---|---|---|---|
| 157 | M | a | 1 | M:27 | 1 | M:10 | KRT10:M,KRT14:M,KRT16:M,KRT17:M,KRT12:M,KRT1:I,KRT5:I | 8 | 3 | KRT14:M119I(EBS1C);KRT14:M119T(EBS1A);KRT14:M119V(EBS1B and EBS1C);KRT6A:I167N(PC3);KRT16:M121T(PC1);KRT10:M150R(EHK2A);KRT10:M150T(EHK2A);KRT13:M108T(WSN2);KRT2:I182N(IBS);KRT17:M88K(PC2);KRT17:M88T(PC2 and SM);KRT12:M129T(MECD1);KRT12:M129V(MECD1) |
| 160 | L | d | 1 | L:27 | 1 | L:10 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:L,KRT5:L | 7 | 6 | KRT14:L122F(EBS1A and EBS1B);KRT6A:L170F(PC3);KRT16:L124H(PC1);KRT16:L124P(PC1);KRT16:L124R(PC1);KRT13:L111P(WSN2);KRT5:L175F(EBS2A);KRT17:L91P(PC2);KRT12:L132P(MECD1);KRT12:L132V(MECD1) |
| 161 | N | e | 1 | N:27 | 1 | N:10 | KRT10:N,KRT14:N,KRT16:N,KRT17:N,KRT12:N,KRT1:N,KRT5:N | 11 | 1 | KRT86:N114D(MNLIX1);KRT86:N114H(MNLIX1);KRT14:N123K(EBS1A);KRT14:N123S(EBS1A);KRT6A:N171D(PC3);KRT6A:N171K(PC3);KRT6A:N171S(PC3);KRT6A:N171Y(PC3);KRT6A:171(PC3);KRT1:N188K(EHK1);KRT1:N188S(EHK1);KRT1:N188T(EHK1);KRT16:N125D(PC1);KRT16:N125G(PC1);KRT16:N125S(FNEPPK1 and PC1);KRT10:N154H(EHK2A);KRT13:N112S(WSN2);KRT5:N176S(EBS2A);KRT2:N186D(IBS);KRT2:N186K(IBS);KRT2:N186Y(IBS);KRT17:N92D(PC2);KRT17:N92H(SM);KRT17:N92S(PC2);KRT74:N148K(ADWH) |
| 163 | R | g | 1 | R:27 | 1 | R:10 | KRT10:R,KRT14:R,KRT16:R,KRT17:R,KRT12:R,KRT1:Q,KRT5:K | 6 | 8 | KRT14:R125C(EBS1A);KRT14:R125G(EBS1A);KRT14:R125H(EBS1A);KRT14:R125S(EBS1A);KRT16:R127C(FNEPPK1 and PC1);KRT16:R127P(PC1);KRT10:R156C(EHK2A);KRT10:R156H(EHK2A);KRT10:R156L(EHK2A);KRT10:R156P(EHK2A);KRT10:R156S(EHK2A);KRT13:R114C(WSN2);KRT13:R114H(WSN2);KRT17:R94C(PC2 and SM);KRT17:R94H(SM and PC2);KRT17:R94P(PC2);KRT12:R135G(MECD1);KRT12:R135I(MECD1);KRT12:R135S(MECD1);KRT12:R135T(MECD1) |
| 167 | Y | d | 1 | Y:27 | 1 | Y:10 | KRT10:Y,KRT14:Y,KRT16:Y,KRT17:Y,KRT12:Y,KRT1:F,KRT5:F | 4 | 14 | KRT14:Y129D(EBS1A);KRT10:Y160D(EHK2A);KRT10:Y160N(EHK2A);KRT10:Y160S(EHK2A);KRT13:Y118D(WSN2);KRT17:Y98D(PC2) |
| 168 | L | e | 1 | L:27 | 0.8 | L:8,M:2 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:I,KRT5:I | 8 | 5 | KRT14:L130P(EBS1A);KRT6A:I178N(PC3);KRT16:L132P(PC1);KRT10:L161S(EHK2A);KRT13:L119P(WSN2);KRT5:I183M(EBS2A);KRT5:I183T(EBS2D);KRT17:L99P(PC2);KRT12:L140Q(MECD1);KRT12:L140R(MECD1) |
| 171 | V | a | 1 | V:27 | 1 | V:10 | KRT10:V,KRT14:V,KRT16:V,KRT17:V,KRT12:V,KRT1:V,KRT5:V | 4 | 13 | KRT14:V133L(EBS1C and EBS1B);KRT14:V133M(EBS1C);KRT5:V186E(EBS2C);KRT5:V186L(EBS2B);KRT5:V186M(EBS2B);KRT17:V102M(PC2);KRT12:V143L(MECD1) |
| 172 | Q | b | 0 | R:25,H:2 | 0.7 | Q:7,R:2,L:1 | KRT10:R,KRT14:R,KRT16:R,KRT17:R,KRT12:R,KRT1:R,KRT5:R | 2 | 24 | KRT14:R134P(EBS1B);KRT5:R187P(EBS2C) |
| 406 | C | e | 0.333 | S:10,C:9,G:3,A:3,V:1,T:1 | 0.889 | C:8,S:1 | KRT10:C,KRT14:C,KRT16:C,KRT17:C,KRT12:C,KRT1:E,KRT5:E | 0 | 86 |  |
| 454 | Y | d | 1 | Y:27 | 1 | Y:9 | KRT10:Y,KRT14:Y,KRT16:Y,KRT17:Y,KRT12:Y,KRT1:Y,KRT5:Y | 5 | 10 | KRT14:Y415C(EBS1C);KRT14:Y415H(EBS1B);KRT6A:Y465H(PC3);KRT6A:Y465S(PC3);KRT1:Y482C(EHK1);KRT10:Y449C(EHK2A);KRT12:Y429C(MECD1);KRT12:Y429D(MECD1) |
| 458 | L | a | 0.889 | L:24,I:3 | 1 | L:9 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:L,KRT5:L | 8 | 4 | KRT86:L410P(MNLIX1);KRT14:L419Q(EBS1A);KRT6A:L469P(PC3);KRT6A:L469R(PC3);KRT1:L486P(EHK1);KRT16:L421P(PC1);KRT2:L484P(IBS);KRT17:L388P(PC2);KRT17:L388R(PC2);KRT12:L433R(MECD1) |
| 558 | Y |  |  |  | 0.7 | Y:7,S:1,G:1,V:1 | KRT10:-,KRT14:-,KRT16:-,KRT17:-,KRT12:-,KRT1:-,KRT5:- | 0 |  |  |

### T8b Alignment columns with disease variants in the most keratin genes (04_hotspot_columns.tsv)

| rank_by_genes | KRT9_position | KRT9_residue | KRT9_domain | n_keratin_genes_with_disease_variant | n_disease_variants | genes |
|---|---|---|---|---|---|---|
| 1 | 161 | N | Coil 1A | 12 | 30 | KRT1;KRT10;KRT13;KRT14;KRT16;KRT17;KRT2;KRT5;KRT6A;KRT74;KRT86;KRT9 |
| 2 | 463 | E | Tail | 10 | 12 | KRT14;KRT2;KRT3;KRT5;KRT6A;KRT6B;KRT6C;KRT81;KRT83;KRT86 |
| 3 | 157 | M | Coil 1A | 9 | 17 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT2;KRT6A;KRT9 |
| 4 | 458 | L | Coil 2 | 9 | 12 | KRT1;KRT12;KRT14;KRT16;KRT17;KRT2;KRT6A;KRT86;KRT9 |
| 5 | 168 | L | Coil 1A | 9 | 11 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT5;KRT6A;KRT9 |
| 6 | 160 | L | Coil 1A | 8 | 12 | KRT12;KRT13;KRT14;KRT16;KRT17;KRT5;KRT6A;KRT9 |
| 7 | 450 | E | Coil 2 | 8 | 10 | KRT1;KRT14;KRT2;KRT4;KRT5;KRT81;KRT83;KRT86 |
| 8 | 163 | R | Coil 1A | 7 | 23 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT9 |
| 9 | 451 | I | Coil 2 | 7 | 11 | KRT1;KRT10;KRT12;KRT14;KRT2;KRT5;KRT6A |
| 10 | 454 | Y | Coil 2 | 6 | 9 | KRT1;KRT10;KRT12;KRT14;KRT6A;KRT9 |
| 11 | 164 | L | Coil 1A | 6 | 9 | KRT13;KRT16;KRT17;KRT5;KRT6A;KRT71 |
| 12 | 166 | S | Coil 1A | 6 | 6 | KRT1;KRT14;KRT16;KRT17;KRT5;KRT6A |
| 13 | 171 | V | Coil 1A | 5 | 8 | KRT12;KRT14;KRT17;KRT5;KRT9 |
| 14 | 167 | Y | Coil 1A | 5 | 7 | KRT10;KRT13;KRT14;KRT17;KRT9 |
| 15 | 457 | L | Coil 2 | 4 | 5 | KRT1;KRT14;KRT6A;KRT86 |

## T9 AlphaFold pLDDT by domain (05_alphafold_plddt_by_domain.tsv)

| domain | start | end | mean_plddt | min_plddt | max_plddt | fraction_plddt_ge_90 | fraction_plddt_ge_70 | fraction_plddt_lt_50 |
|---|---|---|---|---|---|---|---|---|
| Head | 1 | 152 | 34.7 | 26.9 | 64.2 | 0 | 0 | 0.974 |
| Coil 1A | 153 | 188 | 86.3 | 65.9 | 95.8 | 0.444 | 0.972 | 0 |
| Linker 1 | 189 | 207 | 68.5 | 52.6 | 91.1 | 0.0526 | 0.474 | 0 |
| Coil 1B | 208 | 299 | 94.1 | 74.1 | 97.4 | 0.913 | 1 | 0 |
| Linker 12 | 300 | 322 | 52.6 | 32.8 | 82.9 | 0 | 0.13 | 0.522 |
| Coil 2 | 323 | 461 | 92.7 | 62.4 | 97.8 | 0.863 | 0.986 | 0 |
| Tail | 462 | 623 | 38.5 | 29.8 | 59.3 | 0 | 0 | 0.963 |
| full length | 1 | 623 | 62 | 26.9 | 97.8 | 0.355 | 0.443 | 0.507 |

## T10 Templates (05_templates.tsv)

Keratin type I / type II heterodimers:

| template | resolution_A | chain_gene | partner_chain | partner_keratin_gene | partner_description | template_first_resnum | template_last_resnum | target_start | target_end | n_aligned_pairs | identity_to_target | target_domains_covered | n_disease_positions_covered | pubmed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6E2J:B | 2.39 | KRT10 | A | KRT1 | Keratin, type II cytoskeletal 1 | 195 | 294 | 200 | 299 | 100 | 0.64 | Coil 1B:92,Linker 1:8 | 0 | 3.10e+07 |
| 6EC0:B | 2.98 | KRT10 | A | KRT1 | Keratin 1 | 195 | 294 | 200 | 299 | 100 | 0.64 | Coil 1B:92,Linker 1:8 | 0 | 3.10e+07 |
| 4ZRY:A | 3.3 | KRT10 | B | KRT1 | Keratin, type II cytoskeletal 1 | 350 | 455 | 355 | 460 | 106 | 0.557 | Coil 2:106 | 3 | 2.76e+07 |
| 6UUI:X | 2.07 | KRT10 | C | KRT1 | Keratin, type II cytoskeletal 1 | 350 | 455 | 355 | 460 | 106 | 0.547 | Coil 2:106 | 3 | 3.22e+07 |
| 6JFV:A | 2.6 | KRT14 | B | KRT5 | Keratin, type II cytoskeletal 5 | 330 | 419 | 369 | 458 | 90 | 0.589 | Coil 2:90 | 3 | 3.20e+07 |
| 6JFV:C | 2.6 | KRT14 | D | KRT5 | Keratin, type II cytoskeletal 5 | 330 | 421 | 369 | 460 | 92 | 0.598 | Coil 2:92 | 3 | 3.20e+07 |
| 3TNU:A | 3 | KRT14 | B | KRT5 | Keratin, type II cytoskeletal 5 | 332 | 421 | 371 | 460 | 90 | 0.611 | Coil 2:90 | 3 | 2.27e+07 |

Non-keratin IF homodimers aligned without gaps and covering disease-set positions:

| template | resolution_A | chain_gene | partner_chain | partner_keratin_gene | partner_description | template_first_resnum | template_last_resnum | target_start | target_end | n_aligned_pairs | identity_to_target | target_domains_covered | n_disease_positions_covered | pubmed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6YF5:A | 1.83 | LMNA | B |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 6YF5:B | 1.83 | LMNA | A |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 6YF5:C | 1.83 | LMNA | D |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 6YF5:D | 1.83 | LMNA | C |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 6YSH:A | 2.83 | LMNA | B |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 6YSH:B | 2.83 | LMNA | A |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 3.26e+07 |
| 8I33:A | 1.62 | LMNA | C |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:B | 1.62 | LMNA | D |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:C | 1.62 | LMNA | A |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:D | 1.62 | LMNA | B |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 3G1E:A | 1.83 | VIM | B |  | Vimentin | 102 | 131 | 152 | 181 | 30 | 0.533 | Coil 1A:29,Head:1 | 8 | 1.94e+07 |
| 3G1E:B | 1.83 | VIM | A |  | Vimentin | 102 | 131 | 152 | 181 | 30 | 0.533 | Coil 1A:29,Head:1 | 8 | 1.94e+07 |
| 1GK4:A | 2.3 | VIM | B |  | VIMENTIN | 329 | 406 | 383 | 460 | 78 | 0.295 | Coil 2:78 | 3 | 1.19e+07 |
| 1GK4:B | 2.3 | VIM | A |  | VIMENTIN | 329 | 406 | 383 | 460 | 78 | 0.295 | Coil 2:78 | 3 | 1.19e+07 |
| 1GK4:C | 2.3 | VIM | D |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 1.19e+07 |
| 1GK4:D | 2.3 | VIM | C |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 1.19e+07 |
| 1GK4:E | 2.3 | VIM | F |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 1.19e+07 |
| 1GK4:F | 2.3 | VIM | E |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 1.19e+07 |
| 1GK6:A | 1.9 | VIM | B |  | VIMENTIN | 355 | 406 | 409 | 460 | 52 | 0.288 | Coil 2:52 | 2 | 1.19e+07 |
| 1GK6:B | 1.9 | VIM | A |  | VIMENTIN | 355 | 406 | 409 | 460 | 52 | 0.288 | Coil 2:52 | 2 | 1.19e+07 |

## T11 Predicted heptad position vs observed partner contact (05_heptad_vs_contact.tsv)

| template_set | target_heptad | n_residue_observations | fraction_sidechain_contacting_partner | mean_rsa_in_dimer | mean_rsa_lost_on_dimerisation |
|---|---|---|---|---|---|
| keratin heterodimer | a | 101 | 0.871 | 0.177 | 0.328 |
| keratin heterodimer | b | 94 | 0 | 0.435 | 4.96e-04 |
| keratin heterodimer | c | 94 | 0 | 0.463 | 6.79e-04 |
| keratin heterodimer | d | 90 | 0.922 | 0.131 | 0.349 |
| keratin heterodimer | e | 95 | 0.537 | 0.402 | 0.0829 |
| keratin heterodimer | f | 95 | 0 | 0.485 | 0 |
| keratin heterodimer | g | 99 | 0.596 | 0.363 | 0.0783 |
| keratin heterodimer | a+d | 191 | 0.895 | 0.155 | 0.338 |
| keratin heterodimer | e+g | 194 | 0.567 | 0.382 | 0.0806 |
| keratin heterodimer | b+c+f | 283 | 0 | 0.461 | 3.90e-04 |
| non-keratin IF | a | 321 | 0.869 | 0.174 | 0.304 |
| non-keratin IF | b | 315 | 0.00952 | 0.45 | 0.00132 |
| non-keratin IF | c | 313 | 0.00958 | 0.461 | 0.00203 |
| non-keratin IF | d | 307 | 0.883 | 0.171 | 0.329 |
| non-keratin IF | e | 313 | 0.594 | 0.393 | 0.0876 |
| non-keratin IF | f | 311 | 0 | 0.487 | 0 |
| non-keratin IF | g | 311 | 0.547 | 0.372 | 0.0854 |
| non-keratin IF | a+d | 628 | 0.876 | 0.172 | 0.316 |
| non-keratin IF | e+g | 624 | 0.571 | 0.383 | 0.0865 |
| non-keratin IF | b+c+f | 939 | 0.00639 | 0.466 | 0.00112 |

## T12 Structural context of disease-set positions (05_variant_structure_summary.tsv)

| position | residue | domain | heptad | alphafold_plddt | keratin_template_residues | keratin_n_obs | keratin_n_contact_partner | keratin_mean_rsa_dimer | keratin_n_buried | nonkeratin_template_residues | nonkeratin_n_obs | nonkeratin_n_contact_partner | nonkeratin_mean_rsa_dimer | nonkeratin_n_buried | nonkeratin_n_interchain_salt_bridge | nonkeratin_n_interchain_hbond | nonkeratin_n_intrachain_salt_bridge | structural_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 157 | M | Coil 1A | a | 73.3 |  | 0 | 0 |  | 0 | L | 12 | 8 | 0.331 | 4 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 160 | L | Coil 1A | d | 79.7 |  | 0 | 0 |  | 0 | L | 12 | 10 | 0.215 | 8 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 161 | N | Coil 1A | e | 82.8 |  | 0 | 0 |  | 0 | N | 12 | 6 | 0.381 | 0 | 0 | 0 | 0 | interface in a minority of templates |
| 163 | R | Coil 1A | g | 85.6 |  | 0 | 0 |  | 0 | R | 12 | 4 | 0.453 | 0 | 0 | 0 | 5 | interface in a minority of templates |
| 167 | Y | Coil 1A | d | 88.9 |  | 0 | 0 |  | 0 | L;Y | 12 | 12 | 0.235 | 6 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 168 | L | Coil 1A | e | 89.4 |  | 0 | 0 |  | 0 | I | 12 | 9 | 0.283 | 6 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 171 | V | Coil 1A | a | 93.8 |  | 0 | 0 |  | 0 | V | 12 | 12 | 0.0717 | 12 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 172 | Q | Coil 1A | b | 91.6 |  | 0 | 0 |  | 0 | R | 12 | 0 | 0.523 | 0 | 0 | 0 | 7 | no partner contact in any template |
| 406 | C | Coil 2 | e | 96.2 | A;C | 5 | 0 | 0.476 | 0 | A | 6 | 0 | 0.424 | 0 | 0 | 0 | 0 | no partner contact in any template |
| 454 | Y | Coil 2 | d | 86.8 | Y | 5 | 4 | 0.274 | 3 | Y | 8 | 8 | 0.157 | 8 | 0 | 2 | 0 | interface (side chain contacts partner in majority of templates) |
| 458 | L | Coil 2 | a | 78.1 | L | 5 | 2 | 0.549 | 0 | L | 8 | 8 | 0.391 | 0 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 558 | Y | Tail |  | 33.5 |  | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 | 0 | 0 | 0 | no template coverage |

### T12b Contact partners per position (05_variant_structure_map.tsv; entry, chain:residue)

| position | template_set | n_obs | partner_residues_within_4A | intrachain_salt_bridge_partners | interchain_hbond_candidates |
|---|---|---|---|---|---|
| 157 | non-keratin | 12 | 6YF5 A:L38, 6YF5 B:L38, 6YF5 C:L35, 6YF5 C:L38, 6YF5 D:L35, 8I33 A:D34, 8I33 A:L35, 8I33 B:L35, 8I33 B:L38, 8I33 C:L35, 8I33 C:L38, 8I33 D:L35, 8I33 D:L38 |  |  |
| 160 | non-keratin | 12 | 3G1E A:L110, 3G1E B:F114, 3G1E B:L110, 6YF5 A:L35, 6YF5 A:L38, 6YF5 A:L42, 6YF5 A:N39, 6YF5 B:L35, 6YF5 B:L38, 6YF5 B:L42, 6YF5 B:N39, 6YF5 C:L38, 6YF5 C:N39, 6YF5 D:L35, 6YF5 D:L38, 6YF5 D:N39, 8I33 A:L35, 8I33 A:L38, 8I33 B:L35, 8I33 B:L38, 8I33 B:L42, 8I33 B:N39, 8I33 C:L35, 8I33 C:L38, 8I33 C:L42, 8I33 C:N39, 8I33 D:L35, 8I33 D:L38 |  |  |
| 161 | non-keratin | 12 | 6YF5 A:L38, 6YF5 B:L38, 6YF5 C:L38, 6YF5 D:L38, 8I33 A:L38, 8I33 D:L38 |  |  |
| 163 | non-keratin | 12 | 3G1E B:F114, 6YF5 A:L42, 6YF5 C:L42, 8I33 C:I46, 8I33 C:L42 | 6YF5 B:E37, 6YF5 D:E37, 6YSH A:E37, 6YSH B:E37, 8I33 C:E37 |  |
| 167 | non-keratin | 12 | 3G1E A:F114, 3G1E A:L117, 3G1E B:F114, 3G1E B:L117, 6YF5 A:I46, 6YF5 A:L42, 6YF5 A:V49, 6YF5 B:I46, 6YF5 B:L42, 6YF5 B:V49, 6YF5 C:I46, 6YF5 D:I46, 6YF5 D:L42, 6YSH A:I46, 6YSH B:I46, 8I33 A:I46, 8I33 B:I46, 8I33 B:L42, 8I33 B:V49, 8I33 B:Y45, 8I33 C:I46, 8I33 C:V49, 8I33 D:L42 |  |  |
| 168 | non-keratin | 12 | 6YF5 A:Y45, 6YF5 B:Y45, 6YF5 C:Y45, 6YF5 D:Y45, 6YSH A:Y45, 6YSH B:Y45, 8I33 A:R41, 8I33 A:Y45, 8I33 C:Y45, 8I33 D:Y45 |  |  |
| 171 | non-keratin | 12 | 3G1E A:K120, 3G1E A:V121, 3G1E B:K120, 3G1E B:L117, 3G1E B:V121, 6YF5 A:R48, 6YF5 A:V49, 6YF5 A:Y45, 6YF5 B:R48, 6YF5 B:V49, 6YF5 B:Y45, 6YF5 C:R48, 6YF5 C:V49, 6YF5 C:Y45, 6YF5 D:L52, 6YF5 D:R48, 6YF5 D:V49, 6YF5 D:Y45, 6YSH A:R48, 6YSH A:V49, 6YSH B:R48, 6YSH B:V49, 8I33 A:L52, 8I33 A:V49, 8I33 A:Y45, 8I33 B:V49, 8I33 C:V49, 8I33 C:Y45, 8I33 D:L52, 8I33 D:R48, 8I33 D:V49, 8I33 D:Y45 |  |  |
| 172 | non-keratin | 12 |  | 3G1E A:D119, 3G1E B:E125, 6YF5 B:D47, 6YSH B:E53, 8I33 A:D47, 8I33 B:D47, 8I33 D:D47 |  |
| 406 | keratin | 5 |  |  |  |
| 406 | non-keratin | 6 |  |  |  |
| 454 | keratin | 5 | 3TNU B:I467, 3TNU B:L474, 3TNU B:R471, 3TNU B:Y470, 4ZRY B:I479, 4ZRY B:Y482, 6JFV B:I467, 6JFV B:L474, 6JFV B:R471, 6JFV D:I467, 6JFV D:R471 |  |  |
| 454 | non-keratin | 8 | 1GK4 A:R401, 1GK4 B:R401, 1GK4 C:I397, 1GK4 C:R401, 1GK4 C:Y400, 1GK4 D:I397, 1GK4 D:L404, 1GK4 D:R401, 1GK4 D:Y400, 1GK4 E:I397, 1GK4 E:L404, 1GK4 E:R401, 1GK4 E:Y400, 1GK4 F:L404, 1GK4 F:R401, 1GK4 F:Y400, 1GK6 A:E405, 1GK6 A:L404, 1GK6 A:R401, 1GK6 A:Y400, 1GK6 B:L404, 1GK6 B:R401, 1GK6 B:Y400 |  | 1GK4 OH-F:R401.NE, 1GK6 OH-A:E405.OE2, 1GK6 OH-A:R401.NE |
| 458 | keratin | 5 | 3TNU B:L474, 4ZRY B:L485 |  |  |
| 458 | non-keratin | 8 | 1GK4 A:L404, 1GK4 B:L403, 1GK4 B:L404, 1GK4 B:Y400, 1GK4 C:Y400, 1GK4 D:L403, 1GK4 E:L404, 1GK4 E:Y400, 1GK4 F:L404, 1GK4 F:Y400, 1GK6 A:L404, 1GK6 A:Y400, 1GK6 B:L404, 1GK6 B:Y400 |  |  |

## T0 Data sources (data/manifest.json)

| key | retrieved_utc | release | url |
|---|---|---|---|
| alphafold_P35527 | 2026-11-26T19:08:51Z |  | https://alphafold.ebi.ac.uk/api/prediction/P35527 |
| clinvar_KRT9 | 2026-11-26T19:08:50Z |  | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=KRT9%5Bgene%5D&retmax=10000&retmode |
| experimental_structure_check | 2026-11-26T19:09:33Z |  | search.rcsb.org + www.ebi.ac.uk/pdbe/api/mappings/best_structures |
| gnomad_KRT9 | 2026-11-26T19:08:51Z | gnomad_r4 | https://gnomad.broadinstitute.org/api |
| human_if_family | 2026-11-26T19:09:33Z | 202604 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29+AND+%28fami |
| human_keratins | 2026-11-26T19:08:18Z | 202604 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29+AND+%28fami |
| interpro_P35527 | 2026-11-26T19:08:51Z |  | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P35527?page_size=100 |
| panther_orthologs | 2026-11-26T19:08:28Z | 19 | https://pantherdb.org/services/oai/pantherdb/ortholog/matchortho?geneInputList=P35527&organism=9606&orthologTy |
| rcsb_if_entries | 2026-11-26T19:09:34Z |  | https://search.rcsb.org/rcsbsearch/v2/query + https://data.rcsb.org/graphql |
| uniprot_P35527 | 2026-11-26T19:08:17Z | 202604 | https://rest.uniprot.org/uniprotkb/P35527.json |

