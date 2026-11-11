# ALG14 (YBR070C, UniProt P38242) notes

## Activity / role
- Membrane anchor for the catalytic subunit Alg13 [PMID:16100110 "We show that Alg14 functions as a membrane anchor that recruits Alg13 to the cytosolic face of the ER, where catalysis of GlcNAc2-PP-dol occurs."]; necessary and sufficient [PMID:16100110 "demonstrating that Alg14 is both necessary and sufficient for the ER localization of Alg13"]
- Required for the activity of the second LLO step, EC 2.4.1.141 [PMID:16100113 "Immunoprecipitating Alg13p from solubilized extracts resulted in the formation of GlcNAc(2)-PP-Dol but required Alg14p for activity"]; [PMID:15615718 "In vitro studies demonstrate that these proteins are required for transfer of [3H]GlcNAc from UDP-[3H]GlcNAc onto dolichyl-PP-GlcNAc."]
- Forms a complex with Alg7 and Alg13 [PMID:19129246 "Here, we show that the Alg7p, Alg13p, and Alg14p glycosyltransferases form a functional multienzyme complex."]

## Localization / topology
- Lumenal N-terminus, cytosolic C-terminus [PMID:17686769 "We provide evidence that Alg14 contains a C-terminal cytosolic tail and an N terminus that resides within the ER lumen."]
- Enriched near lipid droplets in oleate [PMID:39025454 "We found that Alg14 colocalized strongly with LDs"]
- Peroxisome call comes from a TEF2-overexpression screen [PMID:35563734 "expressed from the constitutive and strong TEF2 promoter"]. ALG14 is not named in the main text.

## Curation observations
- 'cytoplasmic side of Golgi membrane' IDA (PMID:16100110): the paper says ER, so MODIFY to GO:0098554.
- protein binding (Alg13) changed to protein-membrane adaptor activity (GO:0043495).
- YeastPathways gives ALG14 the EC 2.4.1.141 reaction. That is correct as contributes_to, because Alg13 is the catalytic subunit.
