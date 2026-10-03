# sel-12 (C. elegans) review notes

- UniProt: P52166 (PSN_CAEEL), "Presenilin sel-12"; ORF F35H12.3; 444 aa; 8 TM helices; catalytic Asp226 (TM6) and Asp364 (TM7); PAL motif 410-412.
- PANTHER: PTHR10202 (PRESENILIN); subfamily PTHR10202:SF13 (PRESENILIN HOMOLOG).
- IBA nodes: PTN000024429 (endopeptidase activity, membrane protein ectodomain proteolysis, gamma-secretase complex); PTN000024430 (Notch signaling pathway, protein processing, calcium ion homeostasis, amyloid-beta formation).
- Paralogs: hop-1 (redundant presenilin), spe-4 (sperm-specific).

## Key findings
- Identified as a lin-12(gf) suppressor acting in receiving cells [PMID:7566091 "we identified a new gene, sel-12, which appears to function in receiving cells to facilitate signalling mediated by lin-12 and glp-1."]
- Acts upstream of the active ICD [PMID:9716525 "Reducing sel-12 activity can suppress the effects of elevated lin-12 activity when LIN-12 is activated by missense mutations but not when LIN-12 is activated by removal of the extracellular and transmembrane domains."]
- SEL-12::GFP perinuclear (ER/Golgi) [PMID:9716525]
- Redundant with HOP-1; sel-12 single mutants primarily affect pi cell induction [PMID:11518514]
- Neuronal: AIY neurite morphology and thermotaxis memory; human PS1 rescues [PMID:10917532]
- SEL-10 (F-box) physically complexes with SEL-12; sel-10 loss suppresses sel-12 Egl [PMID:9861048]
- Presenilins not required for SUP-17-dependent BMP signaling [PMID:28068334]
- APL-1 lacks amyloid-beta region [PMID:8265668 "APL-1 does not appear to contain the beta-amyloid peptide."] -> amyloid-beta formation IBA is taxonomically inappropriate for worm.

## Review decisions (summary)
- Core MF: GO:0042500 aspartic endopeptidase activity, intramembrane cleaving; BP GO:0007220 Notch receptor processing; complex GO:0070765 gamma-secretase complex; ER/Golgi membrane.
- REMOVE: amyloid-beta formation (IBA; with propagation_review LINEAGE_OR_TAXON_MISMATCH); protein binding x2 (uninformative); egg-laying behavior (InterPro IEA).
- MODIFY: positive regulation of Notch signaling pathway (IGI) -> Notch receptor processing.
- MARK_AS_OVER_ANNOTATED: detection of temperature stimulus (AIY interneuron defect, not sensation); egg-laying behavior IMP.
- UNDECIDED: regulation of TGF-beta receptor signaling pathway (IGI PMID:9716525; abstract suggests negative genetic tests with other membrane-protein genes, and PMID:28068334 finds presenilins dispensable for BMP signaling).
- membrane protein ectodomain proteolysis IBA kept as non-core (gamma-secretase performs intramembrane cleavage; PSEN1 carries the term by IDA -> convention).

## Deep research
- Falcon deep research completed (sel-12-deep-research-falcon.md). Consistent with the review. Additional points:
  - "SEL-12-containing gamma-secretase catalyzes the final transmembrane cleavage (S3 cleavage), releasing the LIN-12 intracellular domain from its membrane anchor"
  - Catalytic D226A mutant abolishes Notch-related (egg-laying) function (Ashkavand et al. 2025, not cached).
  - Gamma-secretase-independent restraint of ER-to-mitochondria calcium transfer (Norman lab 2020-2025, not cached); supports keeping the calcium ion homeostasis IBA as non-core.
  - sel-12 ubiquitous; hop-1 low in larvae, needed in adult germline; spr-5 loss derepresses hop-1 and suppresses sel-12.
