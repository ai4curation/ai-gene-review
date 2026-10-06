# ade5 (SPCC569.08c, UniProt Q9UUK7) notes

Fetch: correct accession fetched (PUR3_SCHPO, Q9UUK7, 207 aa). Naming traps: S. pombe ade5 = GAR transformylase = ortholog of S. cerevisiae ADE8 (genes/yeast/ADE8); UniProt lists "ade8" as a synonym [UniProt:Q9UUK7 "Name=ade5; Synonyms=ade8; ORFNames=SPCC24E4.01, SPCC569.08c;"] while PomBase ade8 (SPBC14F5.09c) is a different gene. S. cerevisiae ADE5,7 corresponds to S. pombe ade1.

## Evidence
- [UniProt:Q9UUK7 "SIMILARITY: Belongs to the GART family. {ECO:0000305}."]; catalytic reaction RHEA:15053; active site 122.
- No S. pombe experimental annotations in GOA; no cached S. pombe literature.

## Decisions
- Core MF GO:0004644, BP GO:0006189, cytoplasm (IBA; the PomBase GO-CAM uses cytosol).
- Adenine biosynthetic process ISO MODIFIED to GO:0006189 (same as genes/yeast/ADE8).
- PomBase also uses ade5 in GO-CAM 6870555700003085 (pteridine/folate metabolism, cytosolic) as a 10-formyl-THF consumer.
