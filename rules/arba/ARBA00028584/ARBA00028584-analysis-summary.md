# ARBA00028584 Rule Analysis Summary

## Rule Overview
- **Rule ID**: ARBA00028584
- **GO Term**: GO:0005778 (peroxisomal membrane)
- **Condition Sets**: 9 distinct condition sets
- **Created**: 2021-10-20
- **Last Modified**: 2025-05-15

## Condition Set Mapping

Based on enriched FunFam labels from ARBA00028584.enriched.json:

| CS | Domain(s) | Taxon | Target Protein | Assessment |
|----|-----------|-------|----------------|------------|
| 1 | IPR010482 (DysF domain) | Fungi | PEX23/24/28/29/30/31/32 | WELL-FOUNDED |
| 2 | FF:000800 (ABCD1 NBD) | Glires | ABCD1 | WELL-FOUNDED, scope too narrow |
| 3 | FF:000109 (PEX13 SH3) | Chordata | PEX13 | WELL-FOUNDED |
| 4 | FF:000033 + FF:000199 + FF:000007 (NBR1) | None | NBR1 | PROBLEMATIC |
| 5 | FF:000036 (ABCD3 TMD) + FF:000636 (ABCD3 NBD) | Rodentia | ABCD3 | WELL-FOUNDED, scope too narrow |
| 6 | FF:000023 + FF:000045 (PMP34) | Eukaryota | SLC25A17/PMP34 | WELL-FOUNDED |
| 7 | FF:000296 (PEX14) | Muridae | PEX14 | WELL-FOUNDED, scope too narrow |
| 8 | FF:000266 (PEX12) | Craniata | PEX12 | WELL-FOUNDED |
| 9 | FF:000477 (DECR2) | Metazoa | DECR2 | DEBATABLE |

## Key Findings

### Correction of Previous Review
The initial review (commit c34df74cb) recommended DEPRECATION based on claims of "biological
incoherence" and "severe" false positive risk. This recommendation was based on a review that:

1. **Lacked actual condition set data** -- the review YAML had `condition_sets: []`
2. **Made factually incorrect claims** -- e.g., claiming the rule targets "TECPR1 DysF domains"
   (it restricts DysF to Fungi, specifically capturing PEX23-32, not TECPR1)
3. **Mischaracterized NBR1** -- called it a "nuclear protein" when it is a cytoplasmic autophagy
   receptor with documented peroxisomal association during pexophagy
4. **Had no real references** -- cited "Protein localization knowledge base" instead of PMIDs
5. **Performed no quantitative analysis** -- no domain overlap, no protein count verification

### Actual Assessment

The rule is **largely biologically sound**. Seven of nine condition sets target well-established
peroxisomal membrane proteins with published experimental evidence:

- **PEX23-32** (CS1): Fungal peroxisomal membrane peroxins with DysF domains (PMID:36462131)
- **ABCD1** (CS2): Peroxisomal very long-chain fatty acid transporter (PMID:35908918)
- **PEX13** (CS3): Peroxisomal import docking complex component (PMID:36541703)
- **ABCD3** (CS5): Peroxisomal branched-chain fatty acid transporter (PMID:35908918)
- **PMP34/SLC25A17** (CS6): Peroxisomal cofactor transporter (PMID:22185573)
- **PEX14** (CS7): Peroxisomal import docking complex component (PMID:37493040)
- **PEX12** (CS8): Peroxisomal RING finger E3 ligase (established peroxin)

### Issues Requiring Modification

1. **CS4 (NBR1)**: NBR1 is a cytoplasmic autophagy cargo receptor recruited to peroxisomes
   during pexophagy. It is NOT a resident peroxisomal membrane protein. GO:0005778 is
   inappropriate; GO:0005776 (autophagosome) is more accurate for its primary localization.

2. **CS9 (DECR2)**: DECR2 is a peroxisomal 2,4-dienoyl-CoA reductase. While UniProt carries
   GO:0005778 via Reactome, DECR2 lacks transmembrane domains and is likely a soluble
   peroxisomal matrix enzyme. GO:0005782 (peroxisomal matrix) may be more appropriate.

3. **Taxonomic restrictions too narrow**: PEX14 (Muridae), ABCD1 (Glires), ABCD3 (Rodentia)
   are all broadly conserved proteins with restrictive taxonomic scopes.

## Recommendation: MODIFY (not DEPRECATE)

Remove CS4 (NBR1), review CS9 (DECR2), and broaden taxonomic restrictions for CS2, CS5, and CS7.
