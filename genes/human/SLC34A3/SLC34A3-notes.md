# SLC34A3 / NaPi-IIc curation notes

Deep research with falcon and the perplexity-lite fallback was unavailable in this checkout, so this review was assembled from cached primary publications, UniProt, Reactome, the PTHR10010 PAINT export, and the merged sibling reviews for SLC34A1 and SLC34A2.

## Core transporter function

SLC34A3 is human NaPi-IIc, the type IIc renal sodium/phosphate cotransporter. Segawa et al. cloned the human and rat cDNAs and showed that type IIc cRNA expression in Xenopus oocytes produces sodium-dependent inorganic phosphate uptake [PMID:11880379, "Microinjection of type IIc cRNA into Xenopus oocytes demonstrated sodium-dependent P(i) cotransport activity"]. The UniProt catalytic-activity block records the same human reaction as 2 Na+(out) + phosphate(out) = 2 Na+(in) + phosphate(in), with evidence from the Segawa paper.

The sodium/phosphate activity, sodium-dependent phosphate transport, and transmembrane phosphate transport rows are therefore core. The broader direct IDA rows to `GO:0006814 sodium ion transport` and `GO:0006817 phosphate ion transport` are true but less precise than the transmembrane processes already present in this review.

## Location

NaPi-IIc acts at the proximal-tubule apical brush-border membrane. UniProt curates human SLC34A3 to the apical cell membrane by similarity to rat Q8K4R8, and the Segawa rat immunohistochemistry localized type IIc protein to the apical membrane of proximal tubular cells [PMID:11880379, "the type IIc protein was shown to be localized at the apical membrane of the proximal tubular cells"].

The Reactome plasma-membrane rows are refined to apical plasma membrane because both cached SLC34A3 Reactome entries say the transporter is apical in proximal tubules. The bare InterPro `GO:0016020 membrane` row is marked too general now that the review retains apical plasma membrane and brush-border membrane.

## Phosphate homeostasis and HHRH

Bergwitz et al. mapped hereditary hypophosphatemic rickets with hypercalciuria to SLC34A3: affected members carried biallelic truncating, missense, or deletion variants, including a c.228delC allele predicted to truncate NaPi-IIc in the first membrane-spanning domain [PMID:16358214, "supports the conclusion that this disease is caused by SLC34A3 mutations affecting both alleles"]. The paper concluded that NaPi-IIc has a key role in phosphate homeostasis, consistent with a direct renal phosphate-conservation role [PMID:16358214, "NaP(i)-IIc has a key role in the regulation of phosphate homeostasis"].

## Family and PAINT

The PAINT rows in `PTHR10010-paint.tsv` are coherent for the human family. `PTN000000493` carries the NaPi-II transporter activity, phosphate homeostasis and sodium-dependent phosphate transport assertions; `PTN001293650` carries apical/brush-border/vesicle localization. The compact PANTHER 19 tree cached at `.cache/panther_trees/19.0/PTHR10010.json.gz` places all three human proteins in the relevant node reaches: SLC34A1 in `PTHR10010:SF21`, SLC34A2 in `PTHR10010:SF23` and SLC34A3 in `PTHR10010:SF35`.

SLC34A1 and SLC34A2 were already reviewed and retain the same family-level sodium/phosphate symporter activity, apical/brush-border localization, and sodium-dependent phosphate transport rows. Their vesicle IBA rows are kept as non-core trafficking pools, so the SLC34A3 vesicle IBA was kept as non-core for consistency.
