# ARBA00067001 / ARBA00052213: which proteins do they annotate?

Script: `classify_rule_matches.py`
(`uv run python rules/arba/ARBA00067001/classify_rule_matches.py > rule_matches.tsv 2> summary.txt`).
It fetches entries live from UniProt REST, so counts can change between releases.
Output from the 2026-10-15 run: `rule_matches.tsv` (one row per entry) and `summary.txt`.

## The rules

Both rules have one condition set: CATH FunFam 3.40.50.720:FF:000411 (named
"Aspartate-semialdehyde dehydrogenase") AND taxon Archaea.

- ARBA00067001 assigns EC 1.2.1.75 in the recommended name, with no full-name text.
  UniProt displays it as "malonyl CoA reductase (malonate semialdehyde-forming)".
- ARBA00052213 assigns the catalytic activity
  "3-oxopropanoate + NADP(+) + CoA = malonyl-CoA + NADPH + H(+)" (RHEA:26446, EC 1.2.1.75).

## Results (2026-10-15)

40 archaeal UniProt entries match the FunFam. 38 carry evidence from both rules. The two
without rule evidence are the reviewed Swiss-Prot malonyl-CoA reductases, A4YEN2
(*Metallosphaera sedula* Msed_0709) and Q96YK1 (*Sulfurisphaera tokodaii* STK_21710),
which are curated rather than rule-annotated.

Classification of the 38 rule-annotated entries by conserved-domain (CDD) subfamily model:

| CDD class | Models | Entries | Interpretation |
|---|---|---|---|
| MCR-type | cd23940 ASADH_C_MCR and/or cd24150 ASADH_MCR_N | 17 | Malonyl-CoA reductases: name and activity correct |
| ASD-type | cd18130 ASADH_C_arch_fung_like and/or cd02315 ScASADH_like_N | 17 | Aspartate-semialdehyde dehydrogenases: name and activity incorrect |
| none | neither | 4 | Unclassified |

ASD-type entries include *M. sedula* A4YHF3 (Msed_1700), *S. tokodaii* Q971Y6 (STK_12420),
*Saccharolobus solfataricus* Q97ZL8 (SSO0874), *Sulfolobus acidocaldarius* Q4J8Z0
(Saci_1411) and *Saccharolobus islandicus* F0NEZ2 (SiRe_1205).

Every species with an ASD-type entry also has a second entry that is MCR-type or
unclassified, so in effect the rules name both paralogs of each genome "malonyl-CoA
reductase". The four unclassified entries (A0A8D5U5J5, A0AAT9GNW8, A0AAX4L5L8 and
Q4J6D4 Saci_2370) each come from a species whose other entry is ASD-type, which suggests
they are the MCR copies; this was not tested.

NCBIfam TIGR00978 (asd_EA) is present on all 19 MCR-type and all 17 ASD-type entries, so
it cannot separate them. The CDD models do, with no entry matching both.

## What follows

- About 45% of the proteins these rules annotate (17 of 38) receive a name and a
  catalytic activity that belong to their paralog.
- Adding the MCR-type CDD models as a required condition (or the ASD-type models as a
  negative condition) would remove all 17, leaving the 4 unclassified entries to check.
- No GO annotation derives from these rules today, because GO has no malonyl-CoA
  reductase activity term. If one is created (it is proposed in
  `genes/METS5/Msed_0709/Msed_0709-ai-review.yaml`), a Rhea-to-GO mapping for RHEA:26446
  would carry the error into GO for every ASD-type entry. The rules should be fixed first.

Evidence for the ASD assignment of Msed_1700 (gene context, sequence identity) is in
`genes/METS5/Msed_1700/Msed_1700-bioinformatics/RESULTS.md`.
