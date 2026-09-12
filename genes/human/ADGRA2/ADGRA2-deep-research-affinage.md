---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADGRA2
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q96PE1
self_evaluation_pairwise: win
faith_pct: 85.71428571428571
n_discoveries: 10
citation_count: 10
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADGRA2 (human)

## Current model (mechanistic narrative)

ADGRA2 (GPR124/TEM5) is an endothelial adhesion GPCR that functions as a cell-autonomous regulator of CNS-specific angiogenesis and blood-brain barrier formation, as established by global and endothelial-specific knockout mice that die embryonically with defective forebrain and spinal cord vascularization, failed vessel invasion of the neuroepithelium, and loss of barrier markers including Glut-1 [PMID:21421844]. Its CNS angiogenic role is mediated through canonical Wnt signaling: ADGRA2 acts as a co-receptor that, together with FZD5, FZD8, LRP6, and RECK, drives WNT7B-mediated synergistic β-catenin signaling downstream of β-catenin stabilization, correlating with increased β-catenin acetylation [PMID:28289266]. ADGRA2 and RECK traffic to the plasma membrane independently and meet at the cell surface, with the leucine-rich repeat domain required for correct receptor trafficking [PMID:27979830, PMID:27979884]. At the membrane, ADGRA2 promotes adhesion and cytoskeletal remodeling by coupling Gβγ to a Rho-GEF module: it forms direct complexes with Elmo/Dock and intersectin-1, activates Rac and Cdc42, and concentrates with phospho-Elmo and ITSN1 at lamellipodia to direct polarity during migration [PMID:28600358]. ADGRA2 also mediates Rac-dependent contact inhibition of endothelial proliferation [PMID:19853600] and is required for VEGF-induced tumor angiogenesis [PMID:24730523]. The receptor is proteolytically shed by MMP-9 and by thrombin—the latter requiring cell-surface protein disulfide-isomerase—to expose a cryptic RGD motif that engages integrin αvβ3 and supports survival of growth-factor-deprived endothelial cells [PMID:16982628, PMID:22013897]. Its C-terminal PDZ-binding motif recruits the scaffold hDlg to the membrane [PMID:15021905].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060089 molecular transducer activity, GO:0098772 molecular function regulator activity, GO:0098631 cell adhesion mediator activity
- **localization:** GO:0005886 plasma membrane
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** RECK, ELMO1, ITSN1, DLG1, ITGAV, ITGB3, LRP6, FZD8
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | Global or endothelial-specific deletion of GPR124 (ADGRA2) in mice causes embryonic lethality associated with defective angiogenesis of the forebrain and spinal cord, failure of blood vessel invasion into neuroepithelium, loss of BBB properties (including Glut-1 expression), and impaired cerebral cortex expansion, establishing ADGRA2 as a cell-autonomous endothelial regulator of CNS-specific vascularization and BBB formation. | PMID:21421844 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | High | TEM5 (ADGRA2) is proteolytically shed from endothelial cells during capillary morphogenesis as a soluble fragment (sTEM5) by MMP-9. Further proteolytic processing exposes a cryptic RGD motif that directly engages integrin αvβ3, and this interaction promotes survival of growth-factor-deprived endothelial cells. sTEM5 also binds glycosaminoglycans, and glycosaminoglycan-bound processed sTEM5 retains αvβ3-mediated pro-survival activity. | PMID:16982628 | The Journal of biological chemistry |
| 2004 | Medium | The PDZ domains of hDlg (human Discs large) directly bind the C-terminal PDZ-binding motif of TEM5 (ADGRA2), and hDlg co-localizes with TEM5 in endothelial cells of embryonic liver, suggesting hDlg is scaffolded to the plasma membrane via TEM5. | PMID:15021905 | Oncogene |
| 2009 | Medium | TEM5 (ADGRA2) expression in endothelial cells is induced during capillary morphogenesis by the small GTPase Rac (not Rho), as shown by pharmacological inhibitor dissection. TEM5 mediates contact inhibition of endothelial cell proliferation: blockade with a soluble extracellular domain or inhibitory antibody abolished contact inhibition, resulting in multilayered islands and increased vessel density. | PMID:19853600 | Experimental cell research |
| 2012 | High | Thrombin directly cleaves TEM5 (ADGRA2) 5 and 34 residues downstream of its RGD motif, generating a shed N-terminal 60 kDa fragment (N60) containing an open RGD conformation. Cell-surface protein disulfide-isomerase (PDI) is required for this shedding: PDI inhibition abrogated N60 release, while addition of reduced PDI enhanced cleavage and dissociation of the N60–C50 disulfide-linked heterodimer. | PMID:22013897 | The Biochemical journal |
| 2017 | High | GPR124 (ADGRA2) promotes cell adhesion and activates Rac and Cdc42 GTPases. It forms direct complexes with the Rho-GEFs Elmo/Dock and intersectin-1 (ITSN1), and Gβγ interacts with the C-terminal tail of GPR124 to promote GPR124–Elmo complex formation. GPR124 activates the Elmo–Dock complex as measured by Elmo phosphorylation on a conserved C-terminal tyrosine. Small fragments of Elmo or ITSN1 that bind GPR124 block GPR124-induced cell adhesion. Endogenous phospho-Elmo and ITSN1 co-localize with GPR124 at lamellipodia of adhering endothelial cells where GPR124 contributes to polarity during wound healing. | PMID:28600358 | The Journal of biological chemistry |
| 2017 | Medium | WNT7B-mediated synergistic β-catenin signaling requires GPR124 (ADGRA2) together with FZD5, FZD8, LRP6, and RECK as co-receptors. Synergistic signaling occurs downstream of β-catenin stabilization and correlates with increased lysine acetylation of β-catenin. | PMID:28289266 | Journal of cell science |
| 2016 | Medium | The LRR (leucine-rich repeat) domain of Adgra2 (GPR124) is required for proper receptor trafficking to the plasma membrane; loss of a single LRR unit causes receptor mis-trafficking and functional loss. Adgra2 trafficking to the plasma membrane occurs independently of Reck, and Reck reaches the plasma membrane independently of Adgra2, indicating the two partners traffic separately and meet at the cell surface. | PMID:27979830 | Biology open |
| 2016 | Medium | An ENU-induced splice site mutation in adgra2 (gpr124), not in sorbs3 as previously attributed, underlies the ouchless zebrafish phenotype, which includes dorsal root ganglia formation defects and highly penetrant cerebrovascular defects. The aberrant transcript encodes a receptor missing one LRR unit. | PMID:27979884 | Development (Cambridge, England) |
| 2014 | Medium | GPR124 (ADGRA2) is required for VEGF-induced tumor angiogenesis: siRNA silencing of GPR124 in human endothelial cells inhibited xenograft tumor angiogenic vessel formation, tumor growth, and VEGF-induced endothelial processes including cell–cell interaction, permeability, migration, invasion, and tube formation in vitro. | PMID:24730523 | Current molecular medicine |

## Citations

- PMID:15021905
- PMID:16982628
- PMID:19853600
- PMID:21421844
- PMID:22013897
- PMID:24730523
- PMID:27979830
- PMID:27979884
- PMID:28289266
- PMID:28600358
