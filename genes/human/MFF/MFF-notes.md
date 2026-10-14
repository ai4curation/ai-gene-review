# MFF notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable). Review based on cached publications, UniProt and PubMed.

- MFF is the main outer-membrane DRP1 receptor [PMID:21149567 "Mff is an essential factor for mitochondrial recruitment of Drp1 during mitochondrial fission in mammalian cells."].
- Tail-anchored in the outer membrane, also on peroxisomes [PMID:18353969 "Mff and Fis1 are both tail anchored in the mitochondrial outer membrane"]; [PMID:23921378 "Fis1 and Mff are Drp1 receptor/effector proteins of mitochondria and peroxisomes."].
- Cytoplasmic domain is a dimer [PMID:23530241 "the cytoplasmic domain of Mff is a dimer"].
- Core MF chosen: GO:0043495 protein-membrane adaptor activity (covers mitochondria and peroxisomes; GO:0180050 is a mitochondria-only child). Generic protein-binding rows removed; the PMID:21149567 row modified to GO:0043495.

## GO:0005096 across the full human carrier set

The `suggested_questions` entry asserts that no human carrier of `GO:0005096` GTPase activator
activity is a receptor or adaptor for a self-assembling dynamin-family GTPase, and that DNM1L is
the only self-assembling dynamin-family GTPase that carries the term. Both are claims about every
human carrier, so they are sourced from QuickGO over the whole set rather than from the gene
folders in this repository, which hold 35 carriers out of 2958 human folders. Query run 2026-10-14:

```
curl -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0005096&taxonId=9606&geneProductType=protein&qualifier=enables&limit=100&page=1'
```

`numberOfHits` 2122 over 22 pages of 100, giving 486 distinct symbols. Two checks over that set:

- the only dynamin-superfamily member is `DNM1L` itself. Checked against `DNM1`, `DNM2`, `DNM3`,
  `DNM1L`, `OPA1`, `MFN1`, `MFN2`, `MX1`, `MX2`, `EHD1`-`EHD4`, `GBP1`-`GBP7` and `ATL1`-`ATL3`;
  only `DNM1L` matches.
- no DRP1 receptor or adaptor carries the term. `MFF`, `MIEF1` (MID51), `MIEF2` (MID49) and
  `FIS1` are all absent from the 486.

The 35 folders in this repository are not the carrier set, which is why the claim is sourced from
the query rather than from them: `ARHGAP1`, `ARHGAP5`, `ARHGAP35`, `RACGAP1`, `RABGAP1` and `TSC2`
are each in the QuickGO result and none has a folder here. The five dispositions the question
lists (DNM1L, ARHGAP11B, ARHGAP36, AGFG1, AGFG2) remain claims about this repository's own reviews
and are scoped to it in the question text.
