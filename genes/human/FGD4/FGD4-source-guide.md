# FGD4 source guide

The review preserves all 25 imported source contexts, their qualifiers and supporting-entity order, nine original reference objects, and three natural splice records. Database mechanisms are documented in the accompanying database source guide. The molecular core is nucleotide exchange in small-GTPase signaling, with cytosol as an explicitly modeled compartment. Additional cortical recruitment is described without inventing another imported localization row.

| Source | Original evidence inspected | Boundary |
| --- | --- | --- |
| [PMID:17564959](https://pmc.ncbi.nlm.nih.gov/articles/PMC1950914/) | Expression Constructs; selected cell/imaging Methods; Results; Figures 2–7 captions; Discussion | Human genetics; functional microscopy uses rat full-length frabin and engineered truncations. No purified exchange assay, natural human splice-product assay or figure-pixel review. |
| [PMID:17564972](https://pmc.ncbi.nlm.nih.gov/articles/PMC1950925/) | Main genetic and expression/overexpression text; Figures 1–3 captions | Rodent nerve/rat Schwann cells; construct species not explicit in the inspected passage. Formation and localization are distinct claims. |
| [PMID:15133042](https://pubmed.ncbi.nlm.nih.gov/15133042/) | PubMed identity/abstract and separately retrieved author-uploaded original Methods and signaling/localization Results | Endogenous human-cell evidence is distinguished from tagged constructs of unspecified species and from purified exchange kinetics. |
| PMID:8969170 | Selected original Methods, biochemical Results and captions, described in the database source guide | Human FGD1 DH–PH fragment; a paralog source, not a human FGD4 assay. |
| PMID:12913069 | Selected original Methods/Results, Figures 3–7 captions and Table 1, described in the database source guide | Mouse Fgd1 targeting; shared catalytic function does not establish each FGD4 compartment. |
| PMID:14702039; PMID:17974005 | Preserved cDNA-resource abstract/body and official UniProt bibliography | Exact target clone mapping and functional activity were not independently established. |
| PMID:24275569 | Preserved human liver phosphoproteome abstract | Exact target peptide/site and protein-group join remain unverified. |

The primary originals for the first three publications were inspected separately from unchanged abstract-only normal caches. For the Chen author-uploaded original, the bounded indexed text includes Methods at lines 384–919, Results/captions at 1105–1262 and Discussion at 1334–1513; selected additional figure 4–5 text was also inspected. This does not claim a continuous whole-paper read. [Author-uploaded original](https://www.researchgate.net/publication/8572857_Phosphatidylinositol_3-Kinase_and_Frabin_Mediate_Cryptosporidium_parvum_Cellular_Invasion_via_Activation_of_Cdc42).

The short natural products remain sequence records without inferred biochemical equivalence. PANTHER ancestry and canonical sequence identity concern the 766-residue target, not every splice product. Reactome generic GEF-set membership supports the imported compartment; it does not add RAC or RhoA/B/C exchange activity to FGD4.

No new publication quotation is added under the [standing project instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). Reference-title validation and source identity checks must not be described as quotation validation when zero snippets were compared.

The current ontology explicitly includes an exchange-defined process, GO:0090630 activation of GTPase activity, as a strict descendant of GO:0043087. It describes activation by replacing GDP with GTP, so the existing row 19 is refined to that term without asserting GAP activity or faster GTP hydrolysis. The core uses GO:0032489 regulation of Cdc42 protein signal transduction, a strict descendant of the broader GO:0051056 already retained in the imported rows. Actual target CDC42 catalyst membership supports this specificity. No new annotation is added, and no historical term-merge claim is inferred from IDs absent from the API response. See [ontology evidence](FGD4-ontology-evidence.yaml).
