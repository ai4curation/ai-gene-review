# lhfpl5a notes (Danio rerio, LHFPL tetraspan subfamily member 5a; UniProt F1Q837)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Literature searched by hand (Europe PMC `(lhfpl5a OR lhfpl5b OR "lhfpl5" OR tmhs) AND zebrafish`).
Shared pair material also in `../lhfpl5b/lhfpl5b-notes.md`; pair analysis in
`lhfpl5a-bioinformatics/RESULTS.md`.

Accession F1Q837 (TrEMBL, 219 aa), ZFIN:ZDB-GENE-110131-8, Ensembl ENSDARG00000045023, chr11. Mutant:
astronaut (asn), allele tm290d, ENU nonsense K80X.

### Origin
- Phylogeny with gar: [PMID:32009898 "Phylogenetic analysis of the Lhfpl5 protein sequences supports the idea that duplicate lhfpl5 genes originated from the teleost WGD event (Figure 1A)."]
- Both kept in 13 teleost orders: [PMID:32009898 "In all 13 teleost orders surveyed, there are two lhfpl5 genes whose protein products cluster with either the lhfpl5a or lhfpl5b ohnolog groups."]
- Singh & Isambert ohnolog call cited: [PMID:32009898 "In all four teleost species surveyed, Singh and Isambert show that lhfpl5a and lhfpl5b are true ohnologs that arose from the teleost-specific WGD under the strictest criteria used in their study."]

### Protein
- [PMID:32009898 "Zebrafish Lhfpl5a and Lhfpl5b are 76% identical and 86% similar to one another (Needleman-Wunsch alignment)."]
- GFP-Lhfpl5a at stereocilia tips; functional (rescues tm290d): [PMID:32009898 "From these results we conclude that the hair bundle-localized GFP-Lhfpl5a protein is functional and can rescue the behavioral and MET channel defects in lhfpl5atm290d mutants."]
- Localization depends on Pcdh15a, Cdh23, Myo7aa: [PMID:32009898 "Taken together, our results using the GFP-Lhfpl5a transgene suggest that Pcdh15a, Cdh23, and Myo7aa all play distinct roles in Lhfpl5 localization in the bundle of zebrafish vestibular hair cells."]
- Needed for Pcdh15a transport: [PMID:28219986 "In contrast, EGFP-tagged Pcdh15a remained in the hair cell body of lhfpl5a mutants at all developmental stages, implying that Lhfpl5a is required for transport to the hair bundle."]
- Not needed for Tmc1/Tmc2b bundle targeting (differs from mouse): [PMID:32009898 "In contrast to what was observed in mouse cochlear hair cells, both Tmc1-GFP and Tmc2b-GFP are still targeted to the hair bundle in lhfpl5atm290d mutants"]

### Expression
- [PMID:32009898 "This divergence in lhfpl5 ohnolog expression continues at 5 dpf, with lhfpl5a found exclusively in the sensory patches of the ear and lhfpl5b restricted to lateral line hair cells (Figures 2E–J)."]
- Adult: [PMID:39484049 "Zebrafish HCs expressed ush1c, tmie, pcdh15a/b, and lhfpl5a, but not the paralog lhfpl5b, while mouse HCs expressed the orthologs Ush1c, Tmie, Pcdh15, and Lhfpl5, respectively."]
- Ear gene repressed by prdm1a in lateral line: [PMID:40825768 "To validate the expression of genes upregulated in prdm1a mutants, we performed HCRs for pvalb9, ckbb, s100a1, tmc2a, strc, kncn, lhfpl5a, tbx2a, and tbx2b and found them to all be strongly expressed in the lateral line hair cells of prdm1a mutants, but not sibling hair cells (Fig. 2i–p, Supplementary Fig. 2e–h)."]
- ZFIN/Bgee (expression_compare.py): lhfpl5a records are all inner-ear (maculae, from Prim-5); Bgee adds bulk testis/larva.

### Function
- [PMID:32009898 "These three tests confirmed that all sensory patches in the otic capsule are inactive in lhfpl5atm290d mutants."]
- Lateral line unaffected in lhfpl5a mutants (FM 1-43 labeling same as WT; hair-cell numbers normal).
- Original screen misread as downstream of transduction because lateral-line microphonics were normal
  [PMID:9491988 "Mutant astronaut and cosmonaut hair cells have relatively normal microphonics and thus appear to affect events downstream of mechanotransduction."]

### Annotation decisions
- GO:0061512 protein localization to cilium (IMP) → MODIFY to GO:0072659 protein localization to plasma membrane
  (stereocilia are not cilia; no stereocilium-specific protein localization term exists).
- GO:0060122 inner ear receptor cell stereocilium organization → KEEP_AS_NON_CORE (splaying follows loss of Pcdh15a).
- NEW: stereocilium tip (IDA, PMID:32009898).
