# PTHR11654 (POT/PTR; plant NPF) — Arabidopsis member survey

Script: `npf_arabidopsis_survey.py` (run from repo root with
`uv run --with biopython python interpro/panther/PTHR11654/PTHR11654-bioinformatics/npf_arabidopsis_survey.py`).
All tables are regenerated from UniProt, the PANTHER geneinfo API (PANTHER 19),
QuickGO and the local `interpro/panther/panther.obo`; nothing is hard-coded.
Run date of the committed outputs: 2026-10-10 (first run 2026-10-06; the rerun added CC rows
and the global counts, and left the MF/BP rows, member table and motif table unchanged).

## 1. Membership and PANTHER subfamilies (`arath_npf_members.tsv`)

All 53 reviewed Arabidopsis NPF proteins (NPF1.1–NPF8.5) carry the UniProt cross-reference
`PANTHER; PTHR11654; OLIGOPEPTIDE TRANSPORTER-RELATED`. There is no separate PANTHER
family for the plant NPF: the plant proteins share one family with animal SLC15A1–4,
yeast PTR2 and bacterial DtpA–D.

PANTHER subfamilies are fine-grained ortholog groups and do **not** correspond to the
eight NPF clades of Léran et al. 2014. 45 subfamilies cover the 53 Arabidopsis members;
most hold a single Arabidopsis protein. Only five subfamilies hold more than one
Arabidopsis protein: SF327 (NPF2.1–2.5), SF381 (NPF2.6, NPF2.7), SF444 (NPF8.4, NPF8.5),
SF453 (NPF5.2, NPF5.3), SF647 (NPF5.13, NPF5.14). The PANTHER name of SF509, which contains
NPF8.1/PTR1, is "SOLUTE CARRIER FAMILY 15 MEMBER 4" (human SLC15A4 itself is in SF80).

## 2. GO annotations on the 53 members (`arath_npf_goa.tsv`, `arath_npf_goa_summary.tsv`)

650 rows: 177 MF, 268 BP and 205 CC. Electronic rows (IBA / IEA) by source:

| Term | Source | Members |
|---|---|---|
| GO:0022857 transmembrane transporter activity | IBA PTN008522918 (family root); IEA InterPro IPR000109 / IPR018456; ARBA00028127 | 47–53 |
| GO:0055085 transmembrane transport | IBA PTN008522918; IEA IPR000109 | 53 |
| GO:0006857 oligopeptide transport | IEA IPR018456 (PROSITE PS01022/PS01023 conserved site) | 23 |
| GO:0071916 dipeptide TM transporter activity, GO:0042937 tripeptide TM transporter activity, GO:0042938 dipeptide transport | IEA IPR044739 (= CDD cd17417, "NPF subfamily 5") | 14 (all NPF5 except NPF5.5, NPF5.9) |
| same three terms | IBA PTN001703849 | NPF8.1, NPF8.2 |
| GO:0042937 tripeptide TM transporter activity | IBA PTN001703614 | NPF5.2, NPF5.3 |
| GO:0015112 nitrate TM transporter activity; GO:0010167 response to nitrate | IBA PTN000183463 | NPF6.3, NPF6.4 |
| GO:0080054 low-affinity nitrate TM transporter activity | IEA ARBA00084141 | NPF5.10, 5.12, 5.13, 5.14, 5.15, 5.16 |
| GO:0016020 membrane (CC) | IBA PTN008522918 (family root) | 32 |
| GO:0005886 plasma membrane (CC) | IBA PTN000910018 | 18 (NPF1.1-1.3, NPF2.1-2.14, NPF3.1) |
| GO:0009705 plant-type vacuole membrane (CC) | IBA PTN001703971; IEA ARBA00085222 | NPF8.3, 8.4, 8.5 (IBA); NPF5.10, 5.12-5.16 (ARBA) |
| GO:0006950 response to stress | IEA ARBA00026300 | NPF6.2, NPF6.3 |

Experimental MF annotations in GOA cover nitrate (IDA/IMP on NPF1.1, 1.2, 2.3, 2.9, 2.12,
2.13, 5.11, 5.12, 5.16, 6.3, 7.2, 7.3), chloride (NPF2.4, 2.5), glucosinolate:H+ symport
(NPF2.10, 2.11), ABA (NPF4.6), K+:H+ antiport (NPF7.3) and di/tripeptides (NPF8.1, 8.2,
8.3; IGI on NPF5.2), plus a NOT nitrate TM transporter activity on NPF8.3.
GO:0080054 low-affinity nitrate TM transporter activity: IDA on NPF1.1, 1.2, 2.12, 2.13, 5.11, 5.12, 5.16
(each the only Arabidopsis protein in its PANTHER subfamily; see `arath_npf_members.tsv`).

Cellular component. PTN000910018 (plasma membrane) reaches 18 Arabidopsis members, all in
NPF1-NPF3; ten of them (NPF2.3, 2.4, 2.7-2.13, 3.1) also have their own IDA for plasma membrane.
PTN001703971 (plant-type vacuole membrane) reaches only NPF8.3, NPF8.4 and NPF8.5, each of which
also has IDA for that location. The other tonoplast members (NPF5.11, 5.12, 5.16 by IDA; NPF5.10,
5.12-5.16 by ARBA00085222) are not reached by either plant CC node, and no IBA puts a tonoplast
member at the plasma membrane.

Global counts (`global_electronic_counts.tsv`; QuickGO annotation search, exact GO id and
`withFrom` = mapping source, all taxa unless stated): IPR044739 → 4,180 annotations for each of
GO:0071916, GO:0042937 and GO:0042938; IPR018456 → 30,703 GO:0006857 annotations, 9,670 of
them in Viridiplantae (NCBITaxon:33090 and descendants); ARBA00084141 → 1,569 GO:0080054
annotations. These counts move with each GOA release.

## 3. TM1 ExxE[R/K] proton-coupling motif (`arath_npf_exxer.tsv`)

Residues aligned to NPF6.3 E41/E44/R45 (pairwise global alignment to Q05085; a coarse
proxy for a family MSA). The motif is intact in NPF1.1, 1.2, NPF2b (2.8–2.14), NPF3.1,
most NPF5, NPF6 and all NPF8. It is absent from NPF2a (NPF2.3–2.6 carry L-x-x-L/M-S/T;
NPF2.1, 2.2 and 2.7 align with a gap) and from all three NPF7 (Q-x-x-A-T). NPF4 members
carry E-x-x-E-N (no basic residue at position 5 of the motif), and NPF4.2/4.3/4.4 also lose
the first Glu. NPF1.3 carries Q-x-x-E-K, NPF5.8/5.9 A-x-x-E-R and NPF5.11 Q-x-x-E-R; NPF5.5 aligns with a gap
(inconclusive). These agree with the trigger review's statement that NPF2a and NPF7 lack
the motif, and add that NPF4 lacks the basic residue.

Interpretation limits: pairwise alignment can misplace TM1 in proteins with long or
divergent N-termini (gaps for NPF2.1, 2.2, 2.7, 5.5); motif absence is not evidence of
loss of transport, since NPF7.3 and NPF2.3/2.7 transport nitrate without it.
