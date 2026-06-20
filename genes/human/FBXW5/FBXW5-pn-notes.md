# FBXW5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q969U6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW5/FBXW5-ai-review.yaml](FBXW5-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW5/FBXW5-ai-review.html
- Gene notes: missing - genes/human/FBXW5/FBXW5-notes.md
- GOA TSV: present - [genes/human/FBXW5/FBXW5-goa.tsv](FBXW5-goa.tsv)
- UniProt record: present - [genes/human/FBXW5/FBXW5-uniprot.txt](FBXW5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW5/FBXW5-deep-research-falcon.md](FBXW5-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW5 (FBW5) is a 566-residue F-box/WD40-repeat protein that serves as a substrate-recognition subunit for cullin-RING E3 ubiquitin ligases. Through its N-terminal F-box domain (residues 3-49) it binds SKP1 and assembles into the canonical SCF (SKP1-CUL1-RBX1) ligase as the SCF(FBXW5) complex, while its seven WD40 repeats form the substrate-docking surface and additionally allow it to act as a DDB1-binding WD40 (DWD) protein that joins the DDB1-CUL4A/B-RBX1 (DCX/CRL4) ligase as the DCX(FBXW5) complex; deleting the F-box abolishes SKP1 binding yet preserves DDB1/CUL4A bridging, demonstrating that substrate recognition resides in the WD40 repeats while the F-box mediates SCF assembly. As an adaptor, FBXW5 does not itself catalyze ubiquitin transfer (the RING subunit RBX1 recruits the E2) but selects substrates for ubiquitination, most often K48-linked polyubiquitination and proteasomal degradation. Its best-defined substrates are the centriolar cartwheel protein SASS6/HsSAS-6, whose S-phase degradation by SCF(FBXW5) restrains centriole reduplication; the actin-regulator EPS8, degraded during G2 to permit mitotic cell-shape changes; the tumor suppressor TSC2, polyubiquitinated by the DCX(FBXW5)/CRL4 complex to control TSC1-TSC2 complex turnover and mTOR signaling; and the kinesin-13 microtubule depolymerases (MCAK/KIF2C, KIF2A, KIF2B), whose SCF(FBXW5)-mediated degradation in G2 lowers their levels at basal bodies and licenses ciliogenesis in the subsequent G1/G0. Additional substrates reported in cancer and metabolic-disease models include the Rho-GAP tumor suppressor DLC1 (degraded by CRL4A(FBXW5) in non-small-cell lung cancer), the Hippo-pathway kinase LATS1 (degraded in gastric cancer, leading to YAP1 activation), the aquaporin AQP3 (degraded by SCF(FBXW5), tuning PDPK1-AKT-mTOR signaling and autophagic cell death in hepatocellular carcinoma), and the stress kinase ASK1/MAP3K5, which FBXW5 modifies with non-degradative Lys63-linked polyubiquitin chains to activate JNK/p38 MAPK signaling in steatohepatitis. SCF(FBXW5) activity toward SASS6 is inhibited by PLK4 phosphorylation of FBXW5 at Ser151, and FBXW5 itself is a cell-cycle-regulated protein degraded by the APC/C during mitosis and G1 (via a D-box at residues 303-311) and reaccumulating at the G1/S transition. TNFAIP8L1 competes with TSC2 for FBXW5 binding, stabilizing TSC2. FBXW5 has also been reported as a negative regulator of MAP3K7/TAK1 in IL-1B signaling. It is a predominantly cytoplasmic protein.
- Existing/core annotation action counts: ACCEPT: 24; KEEP_AS_NON_CORE: 16; NEW: 1

## PN Consistency Summary

- **Consistency:** UPS branch fully consistent — review has GO:1990756 as a NEW annotation (IDA, PMID:21725316) plus GO:0019005, GO:0080008 (CRL4/DCX), GO:0031146, centrosome-duplication and cilium-assembly roles. **Gap:** the PN ALP row (FBXW5 degrades SEC23B to restrain COPII-driven autophagosome formation; ULK1 phosphorylates SEC23B) is NOT represented anywhere in the review — no SEC23B substrate, no autophagy term, and the deep research (falcon) does not mention SEC23B/autophagy. The PN ALP node citing the eLife "ULK1-FBXW5-SEC23B nexus controls autophagy" paper is a substrate/process the review omits.
- **PN story / NEW pressure:** PN ALP asserts an autophagy-regulatory role absent from GO and from the review. The PN node itself declines to project a GO term (no_mapping; macroautophagy too_broad), so there is no over-reach at the node. But the SEC23B-autophagy axis is a genuine literature finding the review should at least note. Defensible candidate term if substantiated: GO:0010506 regulation of autophagy or GO:1903146 regulation of autophagy of mitochondrion — but the review has not assessed the eLife paper, so this is "candidate, needs source verification," not a confirmed ADD. UPS side: GO:1990756 verified real, correctly new_to_goa, already present in review.
- **Evidence alignment:** UPS PN cites PMID:15340381 (family review); review uses gene-specific PMID:21725316 (SASS6/PLK4, HIGH), PMID:18381890 (TSC2/CRL4, HIGH), PMID:34368969 (kinesin-13/cilia, HIGH). ALP PN cites an eLife SEC23B paper with NO overlap in the review's references — the most salient divergence.
- **Verdict:** MOSTLY CONSISTENT; one substrate gap. **Recommended edits:** [YAML] Note the PN ALP SEC23B/autophagy axis in FBXW5 notes/description and assess the eLife "ULK1-FBXW5-SEC23B nexus" paper; if it supports a direct SCF(FBXW5)→SEC23B degradation event, consider adding it as a substrate (and a regulation-of-autophagy non-core process) — verify the PMID first. [REF] add the eLife SEC23B reference.

## Full Consistency Review

- **UniProt:** Q969U6 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (high quality)
- **PN placement (2 rows):** ALP: `Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input|COPII vesicle component regulator` ; UPS: `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40`. **PN-node mapping:** ALP entirely no_mapping/context_only (GO:0016236 macroautophagy held too_broad); UPS group=mapped GO:1990756.
- **Consistency:** UPS branch fully consistent — review has GO:1990756 as a NEW annotation (IDA, PMID:21725316) plus GO:0019005, GO:0080008 (CRL4/DCX), GO:0031146, centrosome-duplication and cilium-assembly roles. **Gap:** the PN ALP row (FBXW5 degrades SEC23B to restrain COPII-driven autophagosome formation; ULK1 phosphorylates SEC23B) is NOT represented anywhere in the review — no SEC23B substrate, no autophagy term, and the deep research (falcon) does not mention SEC23B/autophagy. The PN ALP node citing the eLife "ULK1-FBXW5-SEC23B nexus controls autophagy" paper is a substrate/process the review omits.
- **PN story / NEW pressure:** PN ALP asserts an autophagy-regulatory role absent from GO and from the review. The PN node itself declines to project a GO term (no_mapping; macroautophagy too_broad), so there is no over-reach at the node. But the SEC23B-autophagy axis is a genuine literature finding the review should at least note. Defensible candidate term if substantiated: GO:0010506 regulation of autophagy or GO:1903146 regulation of autophagy of mitochondrion — but the review has not assessed the eLife paper, so this is "candidate, needs source verification," not a confirmed ADD. UPS side: GO:1990756 verified real, correctly new_to_goa, already present in review.
- **Mapping strategy:** Both nodes correct. UPS group GO:1990756 matches review MF (not broader/narrower). ALP no_mapping is the right conservative call given the multi-member container; do not project macroautophagy (TRAPP-like overpropagation, per rationale).
- **Evidence alignment:** UPS PN cites PMID:15340381 (family review); review uses gene-specific PMID:21725316 (SASS6/PLK4, HIGH), PMID:18381890 (TSC2/CRL4, HIGH), PMID:34368969 (kinesin-13/cilia, HIGH). ALP PN cites an eLife SEC23B paper with NO overlap in the review's references — the most salient divergence.
- **Verdict:** MOSTLY CONSISTENT; one substrate gap. **Recommended edits:** [YAML] Note the PN ALP SEC23B/autophagy axis in FBXW5 notes/description and assess the eLife "ULK1-FBXW5-SEC23B nexus" paper; if it supports a direct SCF(FBXW5)→SEC23B degradation event, consider adding it as a substrate (and a regulation-of-autophagy non-core process) — verify the PMID first. [REF] add the eLife SEC23B reference.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW5/FBXW5-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Regulation of autophagophore membrane composition | ER membrane input | COPII vesicle component regulator
- UniProt: Q969U6
- In branches: ALP, UPS
- Notes: Targets SEC23B for proteasomal degradation by ubiquitination which interferes with promotion of autophagosome formation by COPII. ULK1 phosphorylates SEC23B to inhibit its degradation.
- PN references (titles):
    - The ULK1-FBXW5-SEC23B nexus controls autophagy | eLife (elifesciences.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input|COPII vesicle component regulator
        status=no_mapping scope= GO=[]
        rationale: This PN leaf groups upstream regulators of COPII contribution to autophagophore membrane input. The two-member set does not support one crisp shared GO term beyond broad vesicle-coating or kinase context.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition|ER membrane input
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Regulation of autophagophore membrane composition
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q969U6
- In branches: ALP, UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
