# FGD4 database source guide

The canonical review contains the decisions. [The source index](FGD4-database-source-index.yaml) preserves each imported source key and points to its review; it does not duplicate the decision text. [The phylogeny evidence](FGD4-phylogeny-evidence.yaml) records the actual target path and sequence comparison. [The product map](FGD4-database-product-map.yaml) separates the three natural products from experimental fragments.

| Source group | Exact evidence locator and boundary |
| --- | --- |
| GO_REF:0000033 | PTHR12673 v19, target PTN002489344; ancestors PTN000292731 and PTN000292819; four literal positive IBD rows and exact canonical 766-residue MSA match. All descendant experiments were not independently reread. |
| GO_REF:0000024 | Official P52734 mouse Fgd1 and P98174 human FGD1; PMID:12913069 Results/Figure 4 and Figures 5–7/Table 1; PMID:8969170 Methods and exchange/actin Results/Figures 1–3. These are FGD1 paralogs, not FGD4 orthologs. |
| GO_REF:0000002 | Actual Q96M96 InterPro match response: IPR000219 206–393, IPR037742 423–516, IPR000306 551–620. Read the entry GO mappings together with domain descriptions; PH alone is not an enzyme assay. |
| GO_REF:0000044 | Actual UniProt SL-0090 and SL-0286 vocabulary records and reviewed target location comments. These are mapping sources, not HPA images. |
| GO_REF:0000117 | Actual ARBA00027280 condition branch 4: target DH FunFam 1.20.900.10:FF:000013 plus Primates; output GO:0051056. |
| Reactome:R-HSA-205039 | 205039 → catalyst 204987 → set 194849 → FGD4 entity 3000215, cytosol. Generic GEF-set membership does not establish FGD4 RAC specificity. |
| Reactome:R-HSA-419166 | 419166 → catalyst 194957 → set 194849 → FGD4 entity 3000215, cytosol. Do not transfer the event title’s RhoA/B/C substrates. |
| Reactome:R-HSA-9013159 | 9013159 → catalyst 9013228 → established CDC42-GEF set 9013227 → FGD4 entity 3000215. This is actual catalytic membership, not cargo. |
| Reactome:R-HSA-9012999 | 9012999 → CDC42 cycle 9013148 → 9013159 and the route above. Only the target branch was expanded. |

Target corroboration was read in PMID:17564959 Methods defining rat constructs, Results with Figures 5–7 and Discussion of the patient-fibroblast comparison, and PMID:17564972 functional Results/Figure 3. Figure captions and text were read; this lane did not independently inspect their figure pixels or supplements. Original full text was available separately from the immutable normal caches. The six complete target bibliography assessments supplied by ROOT are retained as whole objects; their source-specific access limitations remain visible in the canonical references.

The normal source pool contains all thirteen intake dependencies plus the two adopted FGD1 donor publications. The donor normal caches retain their original availability metadata. The existence of separately recovered original text does not rewrite an abstract-only cache. No new supporting_text or annotations were added.

The current ontology explicitly includes an exchange-defined process, GO:0090630 activation of GTPase activity, as a strict descendant of GO:0043087. It describes activation by replacing GDP with GTP, so the existing row 19 is refined to that term without asserting GAP activity or faster GTP hydrolysis. The core uses GO:0032489 regulation of Cdc42 protein signal transduction, a strict descendant of the broader GO:0051056 already retained in the imported rows. Actual target CDC42 catalyst membership supports this specificity. No new annotation is added, and no historical term-merge claim is inferred from IDs absent from the API response. See [ontology evidence](FGD4-ontology-evidence.yaml).
