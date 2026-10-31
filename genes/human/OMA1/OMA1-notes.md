# OMA1: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/OMA1/OMA1-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of all 54 GOA rows for Q96E52. ProtNLM2 output was not consulted.

Identity: Q96E52 is the reviewed, canonical human OMA1 entry (524 aa, PANTHER PTHR22726:SF1). It is not a fragment or an alternative gene model. Isoform 2 (Q96E52-2, VSP_027958) differs only at the C-terminal tail (456..524) and keeps the catalytic HExxH motif (H327/E328/H331) and the third zinc ligand (E392). No GOA row is isoform-specific.

Evolutionary grounding:
- Metalloendopeptidase IBA comes from a deep node (PTN000506393) that includes yeast, plant and bacterial M48 members. Human OMA1 lies inside that clade, and the activity is also shown directly in human cells [PMID:20038677 "we show that this inducible cleavage is mediated by a zinc metalloprotease called OMA1"].
- The protein quality control and inner-membrane IBAs come from PTN000506394, the eukaryotic OMA1 clade (yeast + human). The yeast experimental basis is [PMID:12963738 "Both peptidases are integral parts of the inner membrane and mediate the proteolytic breakdown of a misfolded derivative of the polytopic inner membrane protein Oxa1."].
- Mouse Oma1 (Q9D8H7) is in the same subfamily (SF1), so the ISS/IEA transfers of autoprocessing and zymogen activation are sound. The organismal phenotypes are a separate question (below).

Key decisions (changes from the previous pass):
- glucose metabolic process and lipid metabolic process (IEA/ISS from mouse): REMOVE. Their only basis is knockout transcriptional changes [PMID:22433842 "ablation of OMA1 in mice results in marked transcriptional changes in genes of lipid and glucose metabolic pathways"]; OMA1 does none of the work of these pathways.
- diet-induced thermogenesis, energy homeostasis, positive regulation of cold-induced thermogenesis: MARK_AS_OVER_ANNOTATED. These are whole-animal knockout phenotypes, which is necessity evidence rather than participation.
- mitochondrial inner membrane fusion: MARK_AS_OVER_ANNOTATED. OMA1 regulates fusion by processing OPA1, and the cellular effect is negative (GO:0010637, accepted). Ge et al. [PMID:31922487] reconstituted OPA1 forms without OMA1.
- mitochondrial respiratory chain complex assembly: MARK_AS_OVER_ANNOTATED. "Required for stability" of supercomplexes is necessity evidence only.
- proteolysis: MODIFY to mitochondrial protein processing. cellular response to stress: MODIFY to integrated stress response signaling. mitochondrion and mitochondrial membrane: MODIFY to mitochondrial inner membrane.
- protein autoprocessing and zymogen activation: KEEP_AS_NON_CORE, changed from UNDECIDED. Support: [PMID:29545505 "OMA1 is a zinc metallopeptidase of the inner mitochondrial membrane that undergoes pre-activating proteolytic and auto-proteolytic cleavage after mitochondrial import."].
- protein quality control: KEEP_AS_NON_CORE (IBA kept; human evidence is about regulatory cleavage).
- Core: metalloendopeptidase in OPA1 processing / negative regulation of fusion, and DELE1 cleavage in HRI-mediated ISR signaling.
- Replaced the previous boilerplate (one long UniProt FUNCTION paragraph quoted on every row) with row-specific quotes from the primary papers.

Relative for next review: mouse Oma1 (Q9D8H7, same PANTHER subfamily PTHR22726:SF1; knockout and autocatalysis studies). It has no review in the repo. Yeast Oma1 (P36163; PMID:12963738) is the founding characterised member and is also unreviewed.

Family/modules: interpro/panther/PTHR22726/PTHR22726-review.yaml lists Q96E52 in SF1, which agrees with UniProt. Minor defect: the SF1 description is a copy of the family coherence_reason rather than a subfamily description. Module: modules/mitochondrial_upr.yaml (mammalian OMA1-DELE1-HRI branch).
