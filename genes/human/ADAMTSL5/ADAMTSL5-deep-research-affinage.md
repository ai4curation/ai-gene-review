---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADAMTSL5
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q6ZMM2
self_evaluation_pairwise: tie
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
gates_passed: False
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADAMTSL5 (human)

> ⚠️ **CAUTION — trust gate(s) tripped; review before using:**
>
> - Affinage's own head-to-head self-evaluation scored this record `pairwise = tie` (not `win`) vs the curated UniProt reference — treat the narrative with extra scepticism.

## Current model (mechanistic narrative)

ADAMTSL5 is a secreted, N-glycosylated extracellular matrix glycoprotein that associates with fibrillin microfibrils and also functions as a disease-relevant signaling modulator and autoantigen [PMID:23010571, PMID:33197513, PMID:26621454]. As a matrix component, it binds both fibrillin-1 and fibrillin-2, co-localizes with fibrillin microfibrils in fibroblast cultures, and binds heparin through its C-terminal netrin-like (NTR) module, which can be proteolytically released [PMID:23010571]. In hepatocellular carcinoma, ADAMTSL5 sustains oncogenic receptor tyrosine kinase signaling: its depletion lowers expression and/or phosphorylation of MET, EGFR, PDGFRβ, IGF1Rβ, and FGFR4 while raising AXL, and its overexpression confers tumorigenicity to MET-sensitized hepatocytes, with its own expression linked to gene-body CpG island hypermethylation [PMID:33197513]. In psoriasis, ADAMTSL5 is an HLA-C*06:02–presented melanocyte autoantigen whose VRSRRCLRL peptide is recognized by an autoreactive Vα3S1/Vβ13S1 CD8+ TCR, driving IL-17A responses [PMID:26621454]; the structural basis of this recognition is an extensive complementary electrostatic interface between negatively charged TCR residues and exposed arginines of the self-peptide and the HLA-C*06:02 α1 helix [PMID:37330172]. This TCR is polyspecific, also responding to environmental peptides from wheat, microbiota, and pathogens, providing a route by which environmental antigens may trigger the ADAMTSL5-directed autoimmune response [PMID:38524140].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0008289 lipid binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0031012 extracellular matrix, GO:0005576 extracellular region
- **pathway (Reactome):** R-HSA-1474244 Extracellular matrix organization, R-HSA-168256 Immune System, R-HSA-1643685 Disease
- **partners:** FBN1, FBN2
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2015 | High | ADAMTSL5 was identified as an HLA-C*06:02-presented melanocytic autoantigen recognized by a Vα3S1/Vβ13S1 T cell receptor (TCR) reconstituted from an epidermal CD8+ T cell clone of a psoriasis patient. Melanocytes are the skin-specific target cells expressing ADAMTSL5, and ADAMTSL5 stimulation induced IL-17A in CD8+ T cells from psoriasis patients only. | PMID:26621454 | The Journal of experimental medicine |
| 2012 | High | ADAMTSL5 is a secreted, N-glycosylated ~60 kDa glycoprotein that binds both fibrillin-1 and fibrillin-2 (the first ADAMTS family member shown to bind both), co-localizes with fibrillin microfibrils in the extracellular matrix of cultured fibroblasts, and binds heparin via its C-terminal netrin-like (NTR) module. Proteolytic release of the NTR module was also observed. Alternative splicing at the 5' end generates two transcripts encoding different signal peptides but the same mature protein, with differing translational efficiency. | PMID:23010571 | Matrix biology : journal of the International Society for Matrix Biology |
| 2023 | High | The crystal structure of the psoriatic Vα3S1/Vβ13S1 TCR in complex with HLA-C*06:02 presenting the ADAMTSL5 peptide (VRSRRCLRL) was determined. TCR docking involves an extensive complementary charge network between negatively charged TCR residues and exposed arginine residues from the ADAMTSL5 self-peptide and the HLA-C*06:02 α1 helix. Mutagenesis and activation assays confirmed these electrostatic interactions are functionally critical. | PMID:37330172 | The Journal of biological chemistry |
| 2020 | High | ADAMTSL5 maintains the function of key oncogenic signaling pathways in hepatocellular carcinoma (HCC). ADAMTSL5 depletion reduced expression and/or phosphorylation of receptor tyrosine kinases MET, EGFR, PDGFRβ, IGF1Rβ, and FGFR4, and increased AXL expression. Conversely, ADAMTSL5 overexpression conferred tumorigenicity to pre-tumoural hepatocytes sensitized by modest MET receptor expression. ADAMTSL5 expression correlates with gene body CpG island hypermethylation at its locus. | PMID:33197513 | Journal of hepatology |
| 2024 | Medium | Multiple environmental peptides (from wheat, Saccharomyces cerevisiae, microbiota, tobacco, and pathogens) activate the same psoriatic Vα3S1/Vβ13S1 TCR that recognizes ADAMTSL5, as demonstrated by lymphocyte stimulation experiments. HLA-C*06:02 tetramers loaded with ADAMTSL5 or wheat peptides showed the same CD8+ T cell population can recognize both, establishing TCR polyspecificity as a mechanism by which environmental antigens may trigger the ADAMTSL5-directed autoimmune response. | PMID:38524140 | Frontiers in immunology |
| 2016 | Medium | ADAMTSL5 protein is expressed not only in epidermal melanocytes but also in keratinocytes throughout the epidermis and in some dermal blood vessels and perivascular dermal cells in psoriatic skin, as shown by immunohistochemistry with three different antibodies. | PMID:27857980 | Journal of pigmentary disorders |
| 2017 | Medium | ADAMTSL5 and LL37 protein levels are significantly increased in lesional psoriatic skin and are co-expressed by dendritic cells, macrophages, and some T cells in the dermis. ADAMTSL5 expression is significantly downregulated following treatment with IL-17 or TNF-α blockade, indicating that psoriasis-related cytokines feed-forward induction of ADAMTSL5. | PMID:28482118 | Experimental dermatology |

## Citations

- PMID:23010571
- PMID:26621454
- PMID:27857980
- PMID:28482118
- PMID:33197513
- PMID:37330172
- PMID:38524140
