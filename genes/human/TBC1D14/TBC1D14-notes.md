# TBC1D14 (human, Q9P2M4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised ortholog of the Atlantic cod model
GADMO/A0A8C5FPT8. No ProtNLM2 files were opened or used.

Deep research: `just deep-research-falcon human TBC1D14 --fallback perplexity-lite` failed
(Edison API 403 "Failed to authenticate"; perplexity-lite fallback timed out at 600 s). No
deep-research file exists. The review uses the cached full-text papers below.

### Evolutionary placement
- PANTHER PTHR47219:SF21 (TBC1 DOMAIN FAMILY MEMBER 14) [file:human/TBC1D14/TBC1D14-uniprot.txt].
- PAINT (interpro/panther/PTHR47219/PTHR47219-paint.tsv): GTPase activator activity is on the
  family-root node PTN000537561, which TBC1D14 does not seed. The TBC1D14-clade nodes
  PTN000538677 (autophagosome, recycling endosome; taxon:33213) and PTN008586039 (regulation of
  autophagosome assembly; taxon:33154) are seeded only by Q9P2M4. The curator gave these nodes no
  GAP term.
- Cod tbc1d14 models fall in the vertebrate TBC1D14 clade, separate from TBC1D12
  (genes/GADMO/A0A8C5FPT8/A0A8C5FPT8-bioinformatics/RESULTS-rereview.md). Fish tbc1d14 is assigned
  PANTHER SF15 (TBC1D12-like), which that tree does not support.
- Catalytic arginine R472 (IxxDxxR motif IKLDISR, 466-472) and glutamine Q508 (YxQ) are retained.

### Key findings
- No GAP activity: [PMID:22613832 "We then performed a GAP assay screen using a panel of 47 Rabs loaded with [32P]GTP but were unable to detect GAP activity with either recombinant GST-TBC1D14"].
- Binds active Rab11; Rab11 needed for its RE tubules [PMID:22613832 "However, the tubules formed by GFP-TBC1D14 were dependent on Rab11"].
- Binds ULK1 (Y2H, co-IP; residues 224-330 of the TBC domain) [PMID:22613832 "A yeast two-hybrid assay revealed an interaction between TBC1D14 and ULK1"].
- Depletion increases starvation-induced autophagy [PMID:22613832 "In cells in which TBC1D14 levels are substantially reduced, LC3 lipidation and turnover during starvation increase significantly."].
- Rab11-TRAPPIII bridge, RAB1 activation, ATG9 RE-to-Golgi traffic, ULK1-independent [PMID:26711178 "These data support a model where TBC1D14 acts as a bridge between a TRAPP complex and activated RAB11."; "However, TBC1D14 depletion resulted in a significant reduction in RAB1B bound to GFP"].
- Shiga toxin block on overexpression independent of catalytic residue [PMID:17562788 "However, these effects were not caused by Rab inactivation because the inactive point mutant gave a similar phenotype"].

### Decisions
- GTPase activator activity IBA: MARK_AS_OVER_ANNOTATED (target-specific negative biochemistry; root-node propagation).
- Protein binding: ULK1 -> protein kinase binding; RAB11B -> small GTPase binding; NXF1 (HuRI) REMOVE.
- Autophagosome (IDA, IBA): KEEP_AS_NON_CORE (partial LC3 colocalization only).
- Endosome IEA -> recycling endosome.
- NEW: molecular adaptor activity (IDA, PMID:26711178).
- Transfer guidance: established in human cells (no in vivo/animal data): Rab11 binding, TRAPPIII
  adaptor role, RE-to-Golgi transport, regulation of starvation-induced autophagosome formation,
  RE/Golgi localization. GAP activity is not established and should not be transferred.

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- Two GO:0005794 rows in the review (HPA IDA, UniProt SubCell IEA), matching the two in the current
  -goa.tsv; the third GO:0005794 occurrence in the review is the core_functions location, not a row.
  No GOA drift.
- Marker check: endogenous TBC1D14 colocalizes with GM130 and TGN46 in HEK293A cells, and the Golgi/TGN
  pool grows on starvation [PMID:22613832 "We found that endogenous TBC1D14 colocalizes with GM130, a
  cis/medial-Golgi marker, and TGN46, a TGN marker"]. The later paper says "Golgi stack" and shows
  TRAPPC4 and RAB1B partially with TBC1D14 at the Golgi; TBC1D14 depletion lowers RAB1B-GTP
  [PMID:26711178].
- Both rows stay ACCEPT (core), reasons extended with the check: the adaptor activity (Rab11 to TRAPPIII,
  RAB1 activation, RE-to-Golgi ATG9 step) is shown at the Golgi. Recruited, cycling pool of a peripheral
  protein (BICD2 pattern). No sub-compartment row: cis/medial (GM130), TGN (TGN46) and "Golgi stack"
  lines disagree. Neither row is is_active_in.
