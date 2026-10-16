# snap-1 (UniProt Q18921, TrEMBL) — alpha-soluble NSF attachment protein (alpha-SNAP), C. elegans

## Identity
- Unreviewed TrEMBL entry, alpha-SNAP (SNAP family, PANTHER PTHR13768:SF8); UniProt function text from RuleBase (ER-Golgi transport, peripheral membrane protein) (from `snap-1-uniprot.txt`). Note: despite the name, SNAP-1 is unrelated to SNAP-25/RIC-4; it is the adaptor that binds cis-SNARE complexes and recruits and stimulates NSF-1.

## Function
- No primary worm paper on snap-1 function is cited by GOA. The PAINT rows (soluble NSF attachment protein activity, SNARE complex disassembly, intracellular protein transport) reflect the conserved alpha-SNAP role, which the exocytosis module realises for the worm as the alpha-SNAP annoton (NSF/alpha-SNAP disassembly of the cis-SNARE complex). The canonical post-fusion step at worm synapses is NSF-mediated cis-SNARE disassembly [PMID:12973353 "UNC-18 could bind and protect syntaxin after N-ethyl-maleimide–sensitive factor (NSF)-mediated disassembly of the cis-SNARE complex."], for which alpha-SNAP is the obligate co-factor in all systems examined.
- Cell-fusion genetics implicate the NSF/SNAP machinery in the worm: nsf-1 is required cell-autonomously for anchor-cell fusion [PMID:16769048 "We find that nsf-1 is required cell-autonomously in the AC for its fusion with the utse."].

## Expression regulation
- snap-1 is among IRE-1/XBP-1-dependent UPR-regulated genes by microarray (HEP) [PMID:16184190 "About 84% of i-UPR genes (170 out of 202 genes) were regulated by both ire-1 and xbp-1 (Figure 3A; Table S1)."]; regulation by the UPR is not participation in it.

## Curation notes
- All functional rows are inferred (IBA/IEA); the only experimental row is the HEP UPR-expression annotation, which is an over-annotation of involvement.

## Deep research
The falcon run overran the wrapper's 600 s client timeout (reported as a failure) but the provider still wrote `snap-1-deep-research-falcon.md` after 615 s, so the report is present and was used. Its worm-specific content, absent from GOA:
- Identity and essentiality: Published worm literature pairs *snap-1* with the chromosome V lethal locus *let-408* and annotates its product as alpha-soluble NSF attachment protein (α-SNAP). [file:worm/snap-1/snap-1-deep-research-falcon.md]
- Phenotypes: **snap-1 RNAi** was associated with defective embryonic osmotic integrity; the **tm2068 deletion** is reported as sterile/lethal. [file:worm/snap-1/snap-1-deep-research-falcon.md]
- Mechanism (family-level, not measured in worm): it recognizes assembled SNARE complexes, recruits/positions NSF, and enables NSF-driven, ATP-dependent SNARE disassembly and recycling. ATP hydrolysis is performed by NSF, not SNAP-1. [file:worm/snap-1/snap-1-deep-research-falcon.md]

The report itself notes that the phenotype summary carries no penetrance, staging or rescue data and that no direct worm trafficking assay exists, and that no 2023-2024 snap-1-specific worm study was found. No new annotation is proposed from it: lethality establishes that SNAP-1 is necessary, not which processes it performs.
