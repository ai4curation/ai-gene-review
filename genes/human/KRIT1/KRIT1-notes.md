# KRIT1 evidence notes

[PMID:21633110](https://pubmed.ncbi.nlm.nih.gov/21633110/), DOI [10.1091/mbc.E11-02-0157](https://doi.org/10.1091/mbc.E11-02-0157), directly establishes GTP-dependent Rap1 effector binding and junctional recruitment. [PMID:17916086](https://pubmed.ncbi.nlm.nih.gov/17916086/) supports microtubule/PIP2 interactions. [PMID:23317506](https://pubmed.ncbi.nlm.nih.gov/23317506/) gives the ICAP1 competition structure, and [PMID:20332120](https://pubmed.ncbi.nlm.nih.gov/20332120/) links CCM1 to VE-cadherin/Par polarity organization. These supply the molecular scaffold mechanism, independently of the Falcon synthesis. The early PMID:9285558 two-hybrid speculation that KRIT1 might regulate Krev-1 does not establish GEF/GAP catalysis; use the directly demonstrated small-GTPase binding function.

[PMID:20616044](https://pubmed.ncbi.nlm.nih.gov/20616044/) reports inhibition of endothelial proliferation, apoptosis, migration, lumen formation and sprouting. The same biology supports the broad horse developmental-process GOA rows, but does not establish spermatogenic piRNA production. ROS/FOXO1/SOD2 effects in [PMID:20668652](https://pubmed.ncbi.nlm.nih.gov/20668652/) are regulatory phenotypes rather than intrinsic redox catalysis.

The horse record is719 aa and aligns at 98.5% identity across 719 paired residues to736 aa human KRIT1. The N-terminal interaction motifs and C-terminal FERM scaffold are retained; see the full alignment for the internal 17 aa gap. The initial horse search returned studies mentioning conserved KRIT1 structures but no horse-specific functional assay. Human Falcon research is complete; no separate horse Edison was selected.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Sources: UniProt O00522 record, cached publications (several newly cached: PMID:22577140, PMID:26540726, PMID:11741838, PMID:26417067, PMID:11854171), the falcon deep-research file, the PTHR13283 PAINT table and QuickGO.

**Identity.** O00522 is the reviewed canonical human KRIT1 entry (736 aa, isoform 1 displayed; isoforms 2 and 3 are splice variants VSP_015800 / VSP_043327). It is not a fragment, isoform or alternative gene model. The previous version of this review contained text copied from the horse (A0A9L0SR44) review ("the selected horse sequence ..."), and the notes above also describe the horse sequence; that horse-specific text has been removed from the human YAML.

**Evolutionary placement.** PANTHER PTHR13283 (KREV INTERACTION TRAPPED 1-RELATED) contains KRIT1 (SF11) and FRMD8 (SF10/SF13), with distinct functions (KRIT1: CCM/Rap1 junctional adaptor; FRMD8: iRhom/ADAM17 stabilization). O00522 is in SF11 with mouse Krit1 (Q6S5J6), bovine KRIT1 and zebrafish krit1 (F1REV3), per interpro/panther/PTHR13283/PTHR13283-entries.csv and the UniProt PANTHER cross-reference; no disagreement. PAINT nodes: PTN002665063 (Bilateria; microtubule binding, redox homeostasis, regulation of polarity, A/P axis specification), PTN002665064 (vertebrates; negative regulation of angiogenesis), PTN004412369 (Eukaryota, family-wide; plasma membrane). KRIT1-specific functions are not transferred to FRMD8 or vice versa.

**Key mechanistic evidence.**
- Rap1 effector: [PMID:21633110 "native KRIT1 protein binds the effector loop of Rap1A but not H-Ras in a GTP-dependent manner"]; FERM F1/F2 co-crystal [PMID:22577140 "We report the 1.95 Å co-crystal structure of KRIT1 FERM domain in complex with Rap1."]. Rap1 binding releases KRIT1 from microtubules to junctions, where it suppresses Rho kinase. Earlier failure to detect Rap1 binding with full-length krit1 [PMID:11741838] is superseded.
- HEG1/CCM2 adaptor: [PMID:23007647 "CCM1/KRIT1 links this complex to endothelial cell (EC) junctions and maintains junctional integrity in part by inhibiting RhoA"]; CCM2 PTB binds the third NPX(Y/F) motif [PMID:25525273].
- ICAP1 antagonism: [PMID:23317506 "KRIT1 directly competes with integrin β1 to bind ICAP1"], i.e. positive regulation of integrin activation, not integrin activation itself.
- Microtubule and PI(4,5)P2 binding [PMID:17916086].
- Downstream outputs: endothelial quiescence and anti-angiogenic effects [PMID:20616044]; polarity [PMID:20332120]; ROS via FOXO1/SOD2 [PMID:20668652].

**Decisions changed from the previous version.**
- GO:0005515 rows: legacy KEEP_AS_NON_CORE was against the protein-binding policy. RAP1A row → MODIFY small GTPase binding; PMID:23007647 CCM2/HEG1 rows → MODIFY protein-macromolecule adaptor activity; CDH5 row → MODIFY cadherin binding; remaining rows REMOVE (interactions real, terms uninformative).
- GO:0009948 A/P axis specification (IBA): was UNDECIDED, now REMOVE. The only seed is a ZFIN acts_upstream_of_or_within IGI from PMID:26540726 (secondary body-axis abnormalities in ccm2l/ccm2 morphants). That is an organismal knockdown phenotype, not participation in axis specification.
- GO:0033622 integrin activation → MODIFY to GO:0033625 positive regulation of integrin activation.
- GO:0045765 regulation of angiogenesis → MODIFY to GO:0016525 (already carried).
- Cytoplasm and cytoskeleton → MODIFY to microtubule cytoskeleton; anchoring junction → MODIFY to adherens junction.
- GO:0016525 rows were ACCEPT with a "non-core" reason (mismatch); now consistently KEEP_AS_NON_CORE. GO:2000114 rows also moved to KEEP_AS_NON_CORE (polarity loss follows from junction disorganization).
- Extracellular region (tear proteomics HDA) → MARK_AS_OVER_ANNOTATED.
- NEW: GO:0035024 negative regulation of Rho protein signal transduction (PMID:21633110, PMID:23007647). Comparator check: HEG1 (IMP) and RASIP1 (IMP, IBA), the other junctional members of the HEG1-Rap1 module, carry this term in GOA; KRIT1 itself is the regulator, not a substrate.
- Considered and not added: GO:0045217 cell-cell junction maintenance (neither HEG1 nor RASIP1 carries it; left out to stay conservative).

**Relative for next review.** Mouse Krit1 (Q6S5J6, MGI:1930618): same PANTHER subfamily SF11 and an experimental seed of PTN002665063/PTN002665064. No genes/mouse/Krit1 review exists. Zebrafish krit1 (santa, F1REV3) is the other characterized ortholog.

**PANTHER family review.** interpro/panther/PTHR13283/PTHR13283-review.yaml places O00522 in SF11 (agrees). Its SF11 `description` repeats the family-level KRIT1-versus-FRMD8 contrast instead of describing the KRIT1 subfamily; that is a wording issue, not a placement disagreement. Not edited here.

**Modules.** No module under modules/ covers the CCM complex or endothelial Rap1/HEG1 junction signaling. dmel_stripak_complex.yaml mentions Ccm3/PDCD10 but not KRIT1.
