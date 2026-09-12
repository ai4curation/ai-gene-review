# FBXL17 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UF56
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL17/FBXL17-ai-review.yaml](FBXL17-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL17/FBXL17-ai-review.html
- Gene notes: missing - genes/human/FBXL17/FBXL17-notes.md
- GOA TSV: present - [genes/human/FBXL17/FBXL17-goa.tsv](FBXL17-goa.tsv)
- UniProt record: present - [genes/human/FBXL17/FBXL17-uniprot.txt](FBXL17-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL17.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL17.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL17/FBXL17-deep-research-falcon.md](FBXL17-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL17 (F-box/LRR-repeat protein 17; also F-box only protein 13) is a substrate-recognition subunit of a SKP1-CUL1-F-box (SCF/CRL1) E3 ubiquitin ligase complex. Through its N-terminal F-box motif it binds SKP1, docking it onto the CUL1-RBX1 catalytic scaffold, while its C-terminal leucine-rich repeat (LRR) domain provides substrate selectivity. FBXL17 performs a distinctive dimerization quality-control (DQC) function: its LRR recognizes a conserved, non-consecutive degron exposed at the interface of aberrantly paired BTB-domain dimers, so that the SCF(FBXL17) ligase selectively ubiquitinates and clears mismatched or compromised BTB homo/heterodimers for proteasomal degradation. A well-characterized physiological substrate is the BTB transcriptional repressor BACH1, whose turnover by SCF(FBXL17) relieves repression of NRF2 target genes such as HMOX1 during the oxidative-stress response. Structural work shows that FBXL17 does not bind the intact BACH1 BTB homodimer; instead, when the dimer interface is destabilized (for example by oxidation or S-nitrosylation under oxidative/nitrosative stress), the FBXL17 LRR engages the weakened dimer and remodels it into a stably bound BTB monomer that is then ubiquitinated, distinguishing FBXL17 from FBXO22, which reads an intact cross-protomer BTB degron. FBXL17 also targets the Hedgehog-pathway regulator SUFU for nuclear ubiquitination and degradation (at Lys257, favored by SUFU dephosphorylation), releasing GLI transcription factors for proper Hedgehog signal transduction, and additional clients include the arginine methyltransferase PRMT1 (via a p300-acetylated K228 "acetyl-degron" triggering K48-linked polyubiquitination) and the long spastin isoform SPAST-M1 (recognized through its N-terminal BTB-like domain), as well as reported BTB partners such as KLHL12 and KBTBD8. The DQC activity is important for the differentiation, function, and survival of neural crest and neuronal cells. FBXL17 is present in both cytoplasm and nucleus, with the nuclear pool acting on substrates such as SUFU, BACH1, and SPAST-M1.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 11; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL17 is the SCF(FBXL17) substrate receptor. Multiple validated substrates: BACH1 (PMID:24035498), SUFU (PMID:27234298), and the hallmark **dimerization quality control (DQC)** of aberrant BTB dimers (PMID:30190310, IDA). Falcon adds the 2024 remodeling/monomerization mechanism (vs FBXO22 reading intact dimers), PRMT1 acetyl-degron, and SPAST-M1 — well-grounded; non-canonical recognition consistently captured. No contradictions.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real); GOA carries only `protein binding` (IPI) as MF. Review adds GO:1990756 as NEW IDA; bare protein binding (SKP1, BACH1, SUFU, KLHL12, SPAST) kept non-core. Correct. The distinctive DQC biology IS a genuine gap: review maps it to GO:0006515 (protein QC for misfolded/incomplete proteins, verified real) but flags that this does not capture quaternary-structure/dimer-interface surveillance, and proposes a NEW BP "dimerization quality control of BTB-domain protein assemblies" (candidate, UNVERIFIED — not yet a real GO ID; defensible, well-justified, parent GO:0006515). Conclusion: adaptor MF ADDED correctly; DQC NEW term is a strong candidate awaiting GO submission.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses three primary PMIDs (24035498, 27234298, 30190310, all verified) + falcon. Strong, gene-specific evidence; benign divergence from placeholder.
- **Verdict:** CONSISTENT / ACCEPT mapping. No YAML edits required. **Flag: non-canonical (DQC) recognition** — noted in brief; group GO:1990756 still valid. DQC NEW BP term is candidate/unverified (worth proposing to GO).

## Full Consistency Review

- **UniProt:** Q9UF56 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`.
- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL17 is the SCF(FBXL17) substrate receptor. Multiple validated substrates: BACH1 (PMID:24035498), SUFU (PMID:27234298), and the hallmark **dimerization quality control (DQC)** of aberrant BTB dimers (PMID:30190310, IDA). Falcon adds the 2024 remodeling/monomerization mechanism (vs FBXO22 reading intact dimers), PRMT1 acetyl-degron, and SPAST-M1 — well-grounded; non-canonical recognition consistently captured. No contradictions.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real); GOA carries only `protein binding` (IPI) as MF. Review adds GO:1990756 as NEW IDA; bare protein binding (SKP1, BACH1, SUFU, KLHL12, SPAST) kept non-core. Correct. The distinctive DQC biology IS a genuine gap: review maps it to GO:0006515 (protein QC for misfolded/incomplete proteins, verified real) but flags that this does not capture quaternary-structure/dimer-interface surveillance, and proposes a NEW BP "dimerization quality control of BTB-domain protein assemblies" (candidate, UNVERIFIED — not yet a real GO ID; defensible, well-justified, parent GO:0006515). Conclusion: adaptor MF ADDED correctly; DQC NEW term is a strong candidate awaiting GO submission.
- **Mapping strategy:** Gene does not change the group node, but is the strongest **non-canonical F-box** in the set — it recognizes a quaternary degron via dimerization-quality-control, not a linear/single-protomer degron. Adaptor MF (GO:1990756) still applies (it does form a productive SCF and ubiquitinates substrates), so the group mapping holds. Substrates validated → not orphan. Catalysis correctly excluded from sub-nodes.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review uses three primary PMIDs (24035498, 27234298, 30190310, all verified) + falcon. Strong, gene-specific evidence; benign divergence from placeholder.
- **Verdict:** CONSISTENT / ACCEPT mapping. No YAML edits required. **Flag: non-canonical (DQC) recognition** — noted in brief; group GO:1990756 still valid. DQC NEW BP term is candidate/unverified (worth proposing to GO).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL17/FBXL17-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9UF56
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001611, IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
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
