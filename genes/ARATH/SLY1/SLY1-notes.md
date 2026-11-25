# SLY1 / SLEEPY1 (At4g24210, UniProt Q9STX3) curation notes

## Identity
- `just fetch-gene ARATH SLY1` first resolved to the wrong protein: Q9SL48 (SEC1-family transport protein SLY1, At2g17980). Deleted and refetched by accession: `just fetch-gene ARATH Q9STX3 --alias SLY1`.
- Q9STX3 GID2_ARATH "F-box protein GID2" (AltName Protein SLEEPY 1); Name=GID2, Synonyms=SLY1; At4g24210. gene_symbol set to SLY1 (TAIR symbol).
- PANTHER PTHR47750 (F-BOX PROTEIN SNE) per UniProt; PAINT IBDs in GOA come from older PTHR12874 nodes PTN000305657 (eukaryotic F-box) and PTN001767709 (land-plant GID2/SLY1; rice GID2 Q7XAK4).

## Key findings (with provenance)
- F-box protein, positive regulator of GA signaling [PMID:12724538 "Positional cloning of SLY1 revealed that it encodes a putative F-box protein"; "sly1 mutations cause a significant increase in RGA protein accumulation even after GA treatment"; "an rga null allele partially suppresses the sly1-10 mutant phenotype"].
- Direct DELLA binding via GRAS domain [PMID:15155881 "SLY1 interacts directly with RGA and GA INSENSITIVE (GAI, a closely related DELLA protein) via their C-terminal GRAS domain"]; nuclear [PMID:15155881 "SLY1 is a nuclear-localized F-box component of the SCF SLY1 E3 ubiquitin ligase"].
- SCF composition and substrate specificity [PMID:15161962 "SLY1 is a subunit of an Arabidopsis SCF SLY1 E3 ubiquitin ligase complex that contains the highly conserved ASK1/2 and AtCUL1 subunits"; "SLY1 (the wild-type form) and sly1gar2-1 both confer substrate specificity on this complex via specific binding to the DELLA proteins"].
- GA-GID1 promotes RGA-SLY1 interaction [PMID:17194763 "the GA-GID1 complex promotes the interaction between RGA and the F-box protein SLY1"].
- SNE/SLY2 paralog partially redundant [PMID:15308775; PMID:21163960 "The FLAG-SLY1 fusion protein was found to coimmunoprecipitate with the GA receptor HA-GA-INSENSITIVE DWARF1b (GID1b)"].
- Cryo-EM: [PMID:40542507 "RGA interacts with GID1A and SLY1 through nonoverlapping binding surfaces"]; [PMID:40768360 "Contrary to prior models, SLY1 binds the GRAS domain"].
- Seed dormancy/germination: [PMID:17384169 "Unlike ga1-3, the GA-insensitive sly1 mutants show variable seed dormancy"].
- Falcon report (SLY1-deep-research-falcon.md) concurs: "SLY1 is a substrate-recognition adaptor, not a gibberellin-metabolizing enzyme or transporter".

## Curation decisions
- DELLA protein-binding IPIs from focused studies: MODIFY -> GO:1990756 ubiquitin-like ligase-substrate adaptor activity. Other protein-binding rows (ASK2, GID1A/B, HT screens): REMOVE per policy.
- regulation of GA signaling (IEA InterPro): MODIFY -> GO:0009939 positive regulation.
- cytoplasm IBA: KEEP_AS_NON_CORE (experimentally nuclear).
- Core: GO:1990756; GA signaling (GO:0009740) + SCF-dependent proteasomal catabolism (GO:0031146); nucleus; SCF complex.
