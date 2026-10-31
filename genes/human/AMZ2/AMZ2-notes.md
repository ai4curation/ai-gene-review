# AMZ2 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- AMZ2 (archaemetzincin-2, Q86W34) belongs to the archaemetzincin family (peptidase M54).
- **The only activity/expression paper is withdrawn.** UniProt's CAUTION line says PMID:15972818 was retracted; the withdrawal notice is PMID:30808005. Affinage's narrative (activity, testis/heart Northern blot) rests on it, so I take no claim from affinage.
- **The catalytic motif is intact.** See `AMZ2-bioinformatics/RESULTS.md`: HEIGHIFGLRH keeps all three zinc histidines. Its paralog AMZ1 has Asn at the third. So the InterPro metallopeptidase prediction is structurally sound for AMZ2 but unconfirmed experimentally.
  - Archaeal family members are inactive in standard assays (PMID:22937112, full text), with possible conditional activity.
- **Decisions:**
  - Peptidase, metallopeptidase and proteolysis IEAs: ACCEPT, as family-level predictions.
  - HPA nucleoplasm IDA: ACCEPT, but no nuclear function is inferred from it.
  - No core function; WHOLLY_DARK gap.
- PMID:37459044 (2023) is a single consanguineous patient with vacuolated sperm heads, homozygous p.Thr174Ala, with AMZ2 protein absent from sperm. It is a candidate gene only, so I propose no spermatogenesis process term.
- Companion review: AMZ1 (PR #4051), where the same withdrawn paper led to UNDECIDED, because AMZ1 also lacks the third zinc His.

## 2026-10-04 round 2 (reviewer comments on #4053)

- **Testis expression:** now cited to PMID:17074343 and to UniProt's TISSUE SPECIFICITY line (down-regulated in testes with maturation arrest or SCOS), which is independent of the withdrawn paper. The description no longer implies testis enrichment.
- **CarG:** the bacterial archaemetzincin CarG is inactive and acts as a transcriptional-regulator subdomain (PMID:22937112). Added as a suggested question on what the HPA nucleoplasm signal means.
- **GO:0008270 zinc ion binding:** deliberately not added as NEW. Metallopeptidase activity (GO:0008237) already implies the catalytic zinc, and the structural Cys4 zinc site rests only on archaeal structures, not on AMZ2 data.
- **Description:** now says the family includes some bacteria. `RESULTS.md` gives the command that regenerates `results.tsv`.
