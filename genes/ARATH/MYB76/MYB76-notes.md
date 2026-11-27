# MYB76 review notes

- 2026-10-28: fetch-gene resolved Q9SPG5 (MYB76_ARATH; TAIR AT5G07700; GeneID 830663). 14 GOA rows.
- Deep research API unavailable; manual research in MYB76-deep-research-manual.md.
- Key papers: PMID:18042203 (abstract only; positive regulator, transactivation), PMID:20348214
  (full text; independent induction of AGSL, spatial distribution), PMID:23792303 (abstract;
  cannot activate alone from native promoter in leaves), PMID:23943862 (abstract; MYC2/3/4
  interaction), PMID:23144921 (full text; drought up, aphid down).
- PMID:23115560 (trichome paper) swaps the HAG numbers ("MYB29 (PMG2/HAG2), and MYB76 (HAG3)");
  the correct assignment is MYB76 = HAG2, MYB29 = HAG3 [PMID:18042203 title].
- Decisions: the core MF is DNA-binding transcription activator activity (RNA pol II
  specific), so the ISS GO:0003700 row is MODIFIED to GO:0001228; GO:0006355 IEA MODIFIED to
  GO:0045944. Generic ARBA response terms MODIFIED to the specific stimulus terms already
  carried (response to wounding, response to insect). IEP stimulus rows kept as non-core.
- IMP row PMID:21418358 (Stotz 2011): abstract mentions only myb28; MYB76 mutant data presumably
  in full text; regulation of glucosinolate biosynthesis is independently established for MYB76,
  so ACCEPT and defer to TAIR.
- No NEW process terms: no further process supported beyond expression/phenotype.

## 2026-10-28 correction (PR #5675 review)

The ISS GO:0003700 row now MODIFYs to GO:0001216 DNA-binding transcription activator activity, and the
GO:0006355 IEA row to GO:0045893 positive regulation of DNA-templated transcription, rather than the
RNA polymerase II-specific GO:0001228 and GO:0045944 noted above. Polymerase specificity has not been
tested, and the MYB28 review uses the same terms for the same claim from PMID:18042203. The core
function uses the same two terms.
