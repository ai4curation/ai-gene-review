# SUN2 review notes

## 2026-09-27 (claude-code)

- Identity: human SUN2 / UNC84B / RAB5IP (Q9UH99), type II inner nuclear membrane protein, SUN-domain family.
- Core: SUN-KASH binding across the perinuclear space (LINC complex) [PMID:18396275 "the KASH domains of Nesprins 1, 2 and 3 interact promiscuously with luminal domains of Sun1 and Sun2"]; trimeric SUN2 binds three KASH peptides [PMID:22632968 "The SUN2 domain is rigidly attached to a trimeric coiled coil that prepositions it to bind three KASH peptides."].
- Nucleoplasmic side: lamin A binding [PMID:19933576 "SUN1 and SUN2 interact with lamin A, but lamin A is only required for NE localization of SUN2"].
- Neuronal nucleokinesis (mouse; redundant with SUN1) [PMID:19874786 "These results indicate that SUN1 and SUN2 are essential and mutually redundant for the normal radial neuronal migration in the cerebral cortex."].
- Decisions: GO:0034993 (meiotic LINC) rows MODIFY to non-meiotic parent GO:0106094 (evidence is mostly somatic nesprin-1/2/3 complexes); protein binding rows with nesprin partners MODIFY to GO:0140444, lamin rows to GO:0005521, HTP/viral/targeting-machinery rows REMOVE; TAS microtubule binding and mitotic spindle organization (from worm UNC-84 paper) REMOVE; endosome membrane (overexpressed rab5ip, PMID:10818110) MARK_AS_OVER_ANNOTATED.
- Deep research (falcon) consistent: SUN2 as non-catalytic LINC structural adaptor; 2023-2024 work on luminal disulfide regulation and nuclear actin/RNAPII coupling noted but not used for annotation.
- Module check (modules/nucleokinesis.yaml): GO:0140444 in nuclear inner membrane for SUN1/SUN2 and GO:0106094 LINC complex agree with this review.
