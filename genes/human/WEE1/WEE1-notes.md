# WEE1: paired human–horse review notes

## Biological evidence

Human WEE1 is a nuclear CDK-inhibitory tyrosine kinase. Direct assays distinguish CDK1 Tyr15 phosphorylation from Thr14 phosphorylation. Mouse egg-activation experiments distinguish WEE2/Wee1B from WEE1/Wee1A: WEE2 depletion blocks pronuclear formation, whereas WEE1 depletion does not in that assay.

- [PMID:8428596: Human Wee1 kinase inhibits cell division by phosphorylating p34cdc2 exclusively on Tyr15.](https://pubmed.ncbi.nlm.nih.gov/8428596/) — abstract cached; full-text availability must be checked separately.
- [PMID:7743995: Regulation of the human WEE1Hu CDK tyrosine 15-kinase during the cell cycle.](https://pubmed.ncbi.nlm.nih.gov/7743995/) — abstract cached; full-text availability must be checked separately.
- [PMID:8348613: Human wee1 maintains mitotic timing by protecting the nucleus from cytoplasmically activated Cdc2 kinase.](https://pubmed.ncbi.nlm.nih.gov/8348613/) — abstract cached; full-text availability must be checked separately.
- [PMID:21454751: Protein tyrosine kinase Wee1B is essential for metaphase II exit in mouse oocytes.](https://pubmed.ncbi.nlm.nih.gov/21454751/) — full text cached.
- [PMID:37527245: Oocyte-specific Wee1-like protein kinase 2 is dispensable for fertility in mice.](https://pubmed.ncbi.nlm.nih.gov/37527245/) — full text cached.

## Exact horse model

The full646-residue horse protein closely matches human WEE1 at95.4% identity. Nuclear phosphorylation is supported. The specific female-pronucleus prediction has a plausible paralog-transfer explanation, but remains UNC: differential necessity does not exclude redundant participation. Broad meiotic claims likewise remain unresolved. Electronic Ser/Thr assignments are refined to the demonstrated tyrosine activity.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/WEE1/WEE1-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The2023Wee2 knockouts retain substantial fertility and support possible biological redundancy, so do not claim WEE2 is universally essential or WEE1 can never compensate. Check horse oocyte expression/perturbation before scoring broad meiosis. Separate kinase catalysis from regulation of a different phosphorylation reaction.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** P30291 is the reviewed canonical human WEE1 product (isoform 1, 646 aa; kinase domain 299-569, ACT_SITE 426, Mg2+ sites 342/431/463/465). It is not a fragment or alternative gene model. Isoform 2 (P30291-2, VSP_044959) lacks residues 1-214, i.e. the N-terminal regulatory region carrying the Ser53/Ser123 phosphodegrons, but keeps the kinase domain. No ProtNLM2 files were opened.

**Evolutionary placement.** PANTHER PTHR11042 (family label "EUKARYOTIC TRANSLATION INITIATION FACTOR 2-ALPHA KINASE ... RELATED"), subfamily SF72 "WEE1-LIKE PROTEIN KINASE", which holds vertebrate WEE1 (human, mouse P47810, rat Q63802, Xenopus wee1-a/b). WEE2 is SF75; Drosophila/plant/Dictyostelium Wee1 are SF185; yeast Wee1/Swe1 are SF196; worm wee-1.1/1.3 and PKMYT1-like are SF183. PAINT nodes: GO:0004713 at PTN008510964 (Eukaryota; seeds human WEE1, fly Wee1, Xenopus Wee2-A); GO:0010972 at PTN008510965 (Euteleostomi; seed human WEE1 only); GO:0004672, nucleus and cytoplasm at the family root PTN000113601. Human WEE1 seeds the root nucleus assertion but not the cytoplasm assertion. The PTHR11042 family review (interpro/panther/PTHR11042/) places human WEE1 in SF72, agreeing with UniProt; no subfamily disagreement.

**Literature used.** PMID:8428596 (exclusive CDK1 Tyr15 phosphorylation; Lys114 dead), PMID:7743995 (endogenous WEE1 phosphorylates several cyclin-CDKs on Tyr15; S/G2 rise, M-phase inactivation), PMID:7774574 (immunodepletion: WEE1 is the main CDK1-Tyr15 kinase in HeLa lysate), PMID:8348613 (nuclear; protects nucleus from cytoplasmically activated CDK1), PMID:15070733 (PLK1/CDK1 phosphodegrons, SCF-beta-TrCP), PMID:15837193 (kinase-domain structure, Ser/Thr-like fold), newly cached PMID:22907750 and PMID:20194642 (WEE1 restrains replication initiation; depletion causes S-phase DNA damage) and PMID:22885324 (H2B Tyr37 as a WEE1 substrate).

**Changes versus the previous version.**
- All 11 GO:0005515 rows -> REMOVE (repository protein-binding policy; WEE1 is the substrate/client of PLK1, beta-TrCP and 14-3-3; interactions not disputed).
- GO:0045740 positive regulation of DNA replication (Reactome TAS) -> MODIFY to GO:0032297 negative regulation of DNA-templated DNA replication initiation (sign correction; Reactome's own pathway summary describes WEE1 Tyr15 phosphorylation as inhibiting Cyclin A:CDK2; PMID:22907750).
- GO:0000086 and GO:0000278 -> MODIFY to GO:0010972 (WEE1 restrains rather than executes the transition; mitotic cell cycle is uninformative).
- GO:0005737 cytoplasm (IBA, IEA) -> MARK_AS_OVER_ANNOTATED (family-root inference whose seeds are other members; human WEE1 is experimentally nuclear). Propagation_review recorded.
- GO:0000287 and GO:0005524 -> KEEP_AS_NON_CORE (cofactor / ATP substrate of the core kinase).
- GO:0005730 nucleolus (HPA) kept UNDECIDED; the deep-research summary of McGowan & Russell 1995 full text says transfected WEE1 is excluded from nucleoli, which conflicts with the HPA call; full text not cached so not quoted.
- Tyrosine kinase rows (GO:0004713, GO:0004715), nucleus, nucleoplasm and GO:0010972 accepted; GO:2000134 kept as non-core.
- Core functions: (1) GO:0004715 in nucleus, negative regulation of G2/M; (2) GO:0004715, negative regulation of replication initiation via CDK2.
- H2B Tyr37 phosphorylation recorded in the description and as a suggested question, not as a NEW annotation.

**Relative to review next.** Mouse Wee1 (P47810, SF72, inside PAINT node PTN008510965 with human WEE1), the experimentally characterised SF72 ortholog in a model organism; no genes/mouse/Wee1 review exists. Note: a stray cache file publications/PMID_20679485.md (unrelated pombe Crb2 paper) was created by a mistaken lookup and is not cited.

**Modules.** modules/g2_m_transition.yaml and modules/cell_cycle_progression.yaml mention WEE1.
