# MFF notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable). Review based on cached publications, UniProt and PubMed.

- MFF is the main outer-membrane DRP1 receptor [PMID:21149567 "Mff is an essential factor for mitochondrial recruitment of Drp1 during mitochondrial fission in mammalian cells."].
- Tail-anchored in the outer membrane, also on peroxisomes [PMID:18353969 "Mff and Fis1 are both tail anchored in the mitochondrial outer membrane"]; [PMID:23921378 "Fis1 and Mff are Drp1 receptor/effector proteins of mitochondria and peroxisomes."].
- Cytoplasmic domain is a dimer [PMID:23530241 "the cytoplasmic domain of Mff is a dimer"].
- Core MF chosen: GO:0043495 protein-membrane adaptor activity (covers mitochondria and peroxisomes; GO:0180050 is a mitochondria-only child). Generic protein-binding rows removed; the PMID:21149567 row modified to GO:0043495.

## GO:0005096 across the full human carrier set

The `suggested_questions` entry asserts two things about the human carriers of `GO:0005096`
GTPase activator activity: that none of the four mammalian outer-membrane DRP1 receptors carries
the term, and that the only self-assembling dynamin-family GTPase that does is DRP1 itself. Both
are claims about every human carrier, so they are sourced from QuickGO over the whole set rather
than from the gene folders in this repository, which hold 35 carriers out of 2958 human folders.
Query run 2026-10-14:

```
curl -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0005096&taxonId=9606&geneProductType=protein&qualifier=enables&limit=100&page=1'
```

`numberOfHits` 2122 over 22 pages of 100, across **1772 distinct `geneProductId` accessions** and
**486 distinct gene symbols**. The two counts differ because a gene is annotated under more than
one accession, so they are not interchangeable and the review text says symbols. Three checks over
that set:

- the only dynamin-superfamily member is `DNM1L` itself. Checked against `DNM1`, `DNM2`, `DNM3`,
  `DNM1L`, `OPA1`, `MFN1`, `MFN2`, `MX1`, `MX2`, `EHD1`-`EHD4`, `GBP1`-`GBP7` and `ATL1`-`ATL3`;
  only `DNM1L` matches.
- none of the four mammalian outer-membrane DRP1 receptors carries the term. `MFF`, `MIEF1`
  (MID51), `MIEF2` (MID49) and `FIS1` are all absent from the 486.
- the filter does exclude negated rows, so "positive enables" is accurate. `ARFGEF1` is absent
  from the 486 symbols and its accession `Q9Y6D5` is absent from all 1772 ids, and the only
  `qualifier` value anywhere in the 2122 results is `enables`. `ARFGEF1-goa.tsv` carries a
  `NOT|enables GO:0005096` row by IDA and no positive row, so this is the control that ties the
  in-corpus arithmetic (35 symbols with a row, 34 positive) to the query.

The 35 folders in this repository are not the carrier set, which is why the claim is sourced from
the query rather than from them: `ARHGAP1`, `ARHGAP5`, `ARHGAP35`, `RACGAP1`, `RABGAP1` and `TSC2`
are each in the QuickGO result and none has a folder here. The five dispositions the question
lists (DNM1L, ARHGAP11B, ARHGAP36, AGFG1, AGFG2) remain claims about this repository's own reviews
and are scoped to it in the question text.

**What these checks do not establish**, recorded because the first version of this section
overreached. Check one asks which carriers *are* dynamin-family GTPases; check two asks whether
DRP1's own receptors carry the term. Neither reaches the broader claim that no carrier is a
receptor or adaptor for *any* self-assembling dynamin-family GTPase - DNM1, DNM2, DNM3, OPA1, the
mitofusins, the EHDs and the atlastins each have their own partners, and none of them is covered
here. No further query can close that gap either, because "is a receptor or adaptor for a
dynamin-family GTPase" is not a field any annotation set returns; establishing it would mean
classifying 486 gene products by a property GO does not record. The review text therefore asserts
only the two checked claims, which is what the MFF case needs.
