---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASB2
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96Q27
self_evaluation_pairwise: win
faith_pct: 75.0
n_discoveries: 14
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASB2 (human)

## Current model (mechanistic narrative)

ASB2 is the substrate-recognition subunit of an ECS-type (Elongin BC–Cullin5–Rbx1) E3 ubiquitin ligase that drives polyubiquitination of bound substrates and their proteasomal degradation, coupling extracellular and developmental signals to targeted proteolysis [PMID:15590664]. Through this complex ASB2 recognizes a substrate repertoire that includes the actin cross-linkers filamin A and filamin B, whose degradation inhibits cell spreading and underlies retinoic acid-induced myeloid differentiation [PMID:18799729], the BMP effector SMAD9, the cytoskeletal protein desmin, and NOX4 [PMID:34845242, PMID:40641155, PMID:41662915]. ASB2 can also bridge non-canonical cullin assemblies, interacting with both Elongin BC–Cul5 and Skp2–Skp1–Cul1 to mediate degradation of E2A and JAK2 [PMID:21119685]. Its transcription is directly induced by multiple signaling inputs—retinoic acid via RARα binding to a promoter RARE/RXRE element [PMID:11566180], Notch [PMID:30116272], the AHR [PMID:33717133], and FLI1 [PMID:34763718]—positioning ASB2 as a signal-responsive effector that regulates hematopoietic differentiation [PMID:18799729, PMID:11682484], NF-κB pathway activity through IκBα and RelB control [PMID:30116272, PMID:34763718], NK cell migration [PMID:33717133], BMP signaling during cardiogenesis [PMID:34845242], and skeletal muscle mass, where it acts as a negative regulator downstream of TGF-β/follistatin [PMID:27182554, PMID:40641155].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016874 ligase activity, GO:0060089 molecular transducer activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology
- **partners:** ELOB, ELOC, CUL5, RBX1, CUL1, SKP2, NDP52
- **complexes:** ECS (Elongin BC–Cullin5–Rbx1) E3 ubiquitin ligase, Skp2–Skp1–Cul1 (SCF) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | ASB2 interacts with the Elongin BC complex and assembles with Cullin5 and Rbx1 to form an ECS-type E3 ubiquitin ligase complex that stimulates polyubiquitination by the E2 ubiquitin-conjugating enzyme Ubc5. | PMID:15590664 | The Journal of biological chemistry |
| 2008 | High | ASB2 targets filamin A and filamin B for proteasomal degradation; knockdown of endogenous ASB2 in leukemia cells delays retinoic acid-induced differentiation and filamin degradation, while ASB2 expression induces filamin degradation and inhibits cell spreading. | PMID:18799729 | Blood |
| 2001 | Medium | ASB2 expression in myeloid leukemia cells induces growth inhibition and chromatin condensation, recapitulating early commitment events of retinoic acid-induced differentiation; ASB2 mRNA is a retinoic acid-induced target gene in APL cells with expression enhanced by PML-RARα. | PMID:11682484 | The Journal of biological chemistry |
| 2001 | Medium | RARα binds to a functional RARE/RXRE element in the ASB2 gene promoter, directly driving ASB2 transcription in response to all-trans retinoic acid. | PMID:11566180 | FEBS letters |
| 2010 | Medium | Notch signaling transcriptionally activates ASB2, which promotes ubiquitination and degradation of E2A (via Skp2) and JAK2 (by direct binding); ASB2 bridges non-canonical cullin-based complexes by interacting with Elongin B/C–Cul5 and also with the F-box protein Skp2–Skp1–Cul1, and dominant-negative Cul1 or Cul5, or their siRNA knockdown, protects E2A and JAK2 from ASB2-mediated degradation. | PMID:21119685 | Cell research |
| 2018 | Medium | ASB2α induces degradation of IκBα, leading to dissociation of IκBα from NF-κB and consequent NF-κB activation in T-ALL cells downstream of Notch1. | PMID:30116272 | Cellular & molecular biology letters |
| 2021 | High | ASB2 acts as the E3 ubiquitin ligase for SMAD9 (but not SMAD1 or SMAD5), targeting it for proteasomal degradation; this regulates BMP signaling during cardiogenesis, and Asb2 knockdown in zebrafish causes thinned ventricular wall and dilated ventricle that are rescued by simultaneous Smad9 knockdown. | PMID:34845242 | Scientific reports |
| 2021 | Medium | AHR directly regulates the ASB2 gene promoter, and AHR agonist (FICZ) induces ASB2-dependent filamin A degradation in NK cells; ASB2 knockdown inhibits filamin A degradation and reduces NK cell migration, while filamin A reduction restores migration capacity. | PMID:33717133 | Frontiers in immunology |
| 2021 | Medium | ASB2 downregulation in GCB DLBCL cells inhibits the alternative NF-κB pathway via downregulation of RelB and increased IκBα, and ASB2 is a direct transcriptional target of FLI1 (identified by ChIP-seq and RNA-seq after FLI1 silencing). | PMID:34763718 | Journal of experimental & clinical cancer research |
| 2016 | Medium | ASB2 expression in skeletal muscle is repressed by follistatin (a TGF-β network modulator), and forced ASB2 overexpression reduces skeletal muscle mass, establishing ASB2 as a negative regulator of muscle mass downstream of TGF-β signaling. | PMID:27182554 | JCI insight |
| 2025 | Medium | Skeletal muscle-specific deletion of Asb2 increases muscle mass and strength; desmin was identified as a substrate of the ASB2 E3 ligase, with its preservation proposed to mediate the muscle hypertrophy phenotype. | PMID:40641155 | Journal of cachexia, sarcopenia and muscle |
| 2026 | Medium | The autophagy receptor NDP52 recruits ASB2 to bind NOX4, mediating K48-linked ubiquitination and autophagic/proteasomal degradation of NOX4, thereby suppressing ferroptosis in cardiomyocytes; this was demonstrated in isoproterenol-induced (in vitro) and TAC-induced (in vivo) heart failure models. | PMID:41662915 | Free radical biology & medicine |
| 2024 | Low | ASB2 E3 ligase activity mediates K48-linked ubiquitination and degradation of CRYAB p.Arg120Gly aggregates in cardiomyocytes downstream of JAK1-STAT3 signaling; Asb2 knockdown abolishes the ability of ruxolitinib (JAK1/2 inhibitor) to clear CRYAB aggregates via the ubiquitin-proteasome system. | PMID:bio_10.1101_2024.10.11.615348 | bioRxiv |
| 2024 | Low | CHPF regulates SMAD9 activity via its mediation of ASB2; ASB2 ubiquitinates SMAD9, and CHPF's regulatory effect on SMAD9 in colorectal cancer cells is exerted through modulation of ASB2. | PMID:38591191 | Histology and histopathology |

## Citations

- PMID:11566180
- PMID:11682484
- PMID:15590664
- PMID:18799729
- PMID:21119685
- PMID:27182554
- PMID:30116272
- PMID:33717133
- PMID:34763718
- PMID:34845242
- PMID:38591191
- PMID:40641155
- PMID:41662915
- PMID:bio_10.1101_2024.10.11.615348
