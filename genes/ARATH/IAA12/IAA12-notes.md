# IAA12 / BODENLOS (At1g04550; Q38830) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt Q38830 IAA12_ARATH, synonym BDL. Correct.

### Function
- bdl is a domain II (degron) gain-of-function: "the bodenlos phenotype results from an amino-acid exchange in the conserved degradation domain of IAA12"; "BODENLOS and MONOPTEROS interact in the yeast two-hybrid assay" [PMID:12101120].
- Embryo phenotype: "BDL is involved in auxin-mediated processes of apical-basal patterning in the Arabidopsis embryo" [PMID:10068632].
- TPL co-repressor: "TOPLESS (TPL) can physically interact with IAA12/BODENLOS (IAA12/BDL)" and TPL "is required for IAA12/BDL repressive activity"; "tpl-1 can suppress the patterning defects of the bdl-1 mutant" [PMID:18258861].
- Aux/IAA domain I = active, transferable repression domain with LxLxL motif [PMID:14742873].
- Receptors: "all TIR1/AFB proteins interact with BDL, and BDL is stabilized in triple mutant plants" [PMID:15992545]; IAA12 needs high auxin to bind TIR1/AFB2 in yeast [PMID:22466420].
- Specificity: "stabilization of BDL/IAA12 or its sister protein IAA13 prevents MP/ARF5-dependent embryonic root formation" [PMID:15889151]; MP and BDL act in the proembryo to specify the hypophysis [PMID:16459305].

### Decisions
- GO:0003700 (ISS, TF catalogue) -> MODIFY to GO:0003714 transcription corepressor activity (no DNA-binding domain).
- GO:0000976 IBA and Y1H IPI -> MARK_AS_OVER_ANNOTATED (indirect promoter association via ARFs).
- Protein binding: ARF partners -> GO:0140297; Aux/IAA partners -> GO:0046982; unrelated HT partners -> REMOVE.
- NEW: GO:0009734 auxin-activated signaling pathway (IAA12 is the co-receptor/substrate that does the signalling step).

## Nuclear auxin repressor audit (2026-10-26)

IAA12–ARF5 interaction is directly reported by PMID:12101120; EAR-dependent TPL recruitment and required TPL repression are explicit in PMID:18258861. The latter remains abstract-only after real refresh attempts, so no additional unseen assay is asserted. The bdl developmental phenotypes reflect a stabilized gain-of-function allele, not a gene deletion. Native root/vascular anatomy is not generalized to Marchantia. Inherited NEW signaling and ligase-binding rows are preserved on their direct primary evidence (PMID:15992545; co-receptor specificity PMID:22466420), not counted as new coverage.

All 61 baseline rows were assessed, with original term/evidence/reference/partner fields and flags preserved. Bare GO:0005515 removal follows the explicit repository exception: it does not deny the measured interaction. Each affected reason identifies its original source, partner and assay context. Independently grounded functional ARF/SCF interactions are refined; homotypic binding is retained as non-core. Neither receptor-dependent degradation nor a loss-of-function phenotype alone licenses a new protein-catabolic-process annotation on an Aux/IAA substrate. No new rows were added in this audit.

The prior cis-regulatory-binding rejection inferred an unproved ARF bridge in a yeast one-hybrid screen. Normal publisher supplement retrieval found IAA12/AT1G04550 → AT5G12870 (MYB46 promoter), SupplementaryTable2 Sheet1 row445, with one of LacZ/HIS reporters activated. Table5 confirms the AUX-IAA clone. The Methods state: [PMID:25533953 "the screen was repeated to confirm the results and each clone was sequenced to reconfirm identity"]. This supports retaining non-core promoter association, with no claim that every Aux/IAA is an autonomous DNA-binding transcription factor. PAINT inheritance is respected; no node defect or lineage-specific loss is inferred from a missing canonical DNA-binding domain.

Provider provenance: parent ran actual Falcon and Perplexity-lite attempts; both authentication/provider attempts failed. Logs are .cache/module-audit-logs/auxin-fetch/ARATH-IAA12-provider.log. No provider report was fabricated. Normal gene-publication caching succeeded. Primary sources, not provider prose or GOA rows, support the decisions. CrY2H-seq correction PMID:36690743 changes the first author surname, not the interaction data. The detailed row-by-row audit is generated under IAA12-source-analysis/annotation-audit.yaml.

Final actions: ACCEPT=4, KEEP_AS_NON_CORE=8, MODIFY=6, NEW=2, REMOVE=41.

Original source distribution:

- GO_REF:0000002: 1 rows.
- GO_REF:0000033: 3 rows.
- GO_REF:0000120: 1 rows.
- GO_REF:0000122: 1 rows.
- PMID:10068632: 1 rows.
- PMID:11118137: 1 rows.
- PMID:12101120: 2 rows.
- PMID:15992545: 2 rows.
- PMID:18258861: 3 rows.
- PMID:21734647: 15 rows.
- PMID:22096563: 2 rows.
- PMID:25533953: 1 rows.
- PMID:32612234: 28 rows.
