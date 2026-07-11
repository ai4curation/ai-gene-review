# YFH7 (P43591 / YFR007W / AIM12) — research notes

Species: *Saccharomyces cerevisiae* (S288c), NCBITaxon:559292
UniProt: P43591 (YFH7_YEAST); ORF YFR007W; SGD S000001903; aliases AIM12.
Length: 353 aa; MW 39,885. Structures: PDB 2GA8 (1.77 Å), 2GAA (1.95 Å).

## Deep research provenance

`just deep-research-falcon yeast YFH7 --fallback perplexity-lite` was attempted twice
(2026-07-05) and timed out both times (Edison/falcon exit 143 after ~5 min; no output
file produced). Per project guidance I did NOT fabricate a `-deep-research-*.md` file.
These notes are compiled directly from: (1) the cached UniProt record
(`YFH7-uniprot.txt`), (2) the three cached primary publications
(`publications/PMID_18004758.md`, `PMID_12868057.md`, `PMID_19300474.md`), and (3) the
completed, reproducible bioinformatics analysis in `YFH7-bioinformatics/RESULTS.md`.

## What is KNOWN

### Enzyme / fold identity (well established, experimental + structural)
- YFH7 is an **ATP-dependent kinase** of the P-loop NTPase superfamily. The 2008 crystal
  structure paper solved the fold and did enzymology:
  [PMID:18004758 "Structural and ligand binding analysis combined with enzymatic assays suggest that YFH7 is an ATP-dependent small molecule kinase with new substrate specificity."]
- Fold assignment: weak similarity to the **PRK/URK/PANK** (phosphoribulokinase / uridine
  kinase / bacterial pantothenate kinase) subfamily of P-loop kinases, with the
  characteristic core, lid, and NMP(bind) subdomains:
  [PMID:18004758 "yeast YFH7 is a yeast-specific protein showing weak similarity with the phosphoribulokinase/uridine kinase/bacterial pantothenate kinase (PRK/URK/PANK) subfamily of P-loop containing kinases."]
- A **~100-residue insertion** distinguishes YFH7 from other family members and forms an
  "additional alpha/beta domain of novel topology":
  [PMID:18004758 "A large insertion of about 100 residues distinguishes YFH7 from other members of the family."]
- Measured biophysical parameter: **KM = 1178 µM for ATP** (UniProt BIOPHYSICOCHEMICAL
  PROPERTIES, ECO:0000269|PubMed:18004758). This anchors the IDA ATP-turnover annotation.

### ATP-binding site / motifs (structure + sequence)
- UniProt BINDING 31..39 = ATP (ChEBI:30616), ECO:0000250.
- Bioinformatics (`YFH7-bioinformatics/RESULTS.md`): canonical **Walker A / P-loop
  `GSPGSGKS` at residues 31–38**, matching `[AG]-x(4)-G-K-[ST]`; and the URK-family
  diagnostic **second block `VILEG` at 263**. Both diagnostic blocks are retained →
  catalytic scaffold intact, not an obviously degenerate pseudokinase.
- Domain xrefs: IPR027417 (P-loop NTPase), Gene3D 3.40.50.300, SUPFAM SSF52540 (fold in
  three discontinuous segments 22–54 / 156–204 / 233–349, gap ~55–155 = the insertion),
  PANTHER **PTHR10285 "URIDINE KINASE"**, CDD cd00009 (AAA). UniProt: "Belongs to the
  YFH7 family."

### Conservation
- The **fold/family is ancient and pan-eukaryotic** (eggNOG KOG2702 at Eukaryota;
  OrthoDB group at Eukaryota; PANTHER PTHR10285 URK family reaches into bacteria).
- The **specific YFH7 protein is lineage-restricted**: bioinformatics UniRef50 cluster
  common taxon = *Saccharomycetaceae* (budding yeasts), UniRef90 narrows to
  *Saccharomyces* sensu stricto (`YFH7-bioinformatics/RESULTS.md`). Consistent with the
  paper's "yeast-specific protein" language.

### Cellular / phenotypic associations (indirect, high-throughput)
- Abundance: ~161 molecules/cell in log-phase SD medium (UniProt MISCELLANEOUS,
  ECO:0000269|PubMed:14562106).
- Localization: cytoplasm (GO IBA GO:0005737, GO_Central). No experimental yeast IDA
  localization in the cached record.
- **ER biogenesis screen**: *yfh7Δ* was recovered in a parallel deletion-mutant screen
  for genes required for ER (karmellae) biogenesis; UniProt encodes this as the FUNCTION
  hedge "could be involved in endoplasmic reticulum membrane assembly"
  (ECO:0000269|PubMed:12868057). Note: the cached PMID:12868057 abstract is a genome-wide
  screen; it does not itself assign a molecular mechanism to YFH7.
- **Mitochondrial-genome maintenance**: *yfh7Δ* increases the frequency of mitochondrial
  genome loss (petite frequency) in a computationally-driven quantitative screen; UniProt
  DISRUPTION PHENOTYPE "Increases frequency of mitochondrial genome loss"
  (ECO:0000269|PubMed:19300474). This is the source of the AIM ("Altered Inheritance of
  Mitochondria") alias. PMID:19300474 (full text cached) is a screen that assigns yeast
  ORFs a mitochondrial-biogenesis phenotype by petite-frequency assay; it does not
  determine YFH7's biochemical substrate.

## What is NOT known (the primary deliverable)

- **The physiological substrate / phosphoacceptor of YFH7 is unknown.** The crystallographers
  could only conclude "**new substrate specificity**" — i.e. it is a small-molecule kinase
  but they could not identify what it phosphorylates:
  [PMID:18004758 "...an ATP-dependent small molecule kinase with new substrate specificity."]
  No substrate has been identified since from sequence, structure, or the bioinformatics
  analysis here.
- **The pathway / biological process** in which YFH7 acts is undefined. The ER-biogenesis
  and mitochondrial-genome-loss associations are pleiotropic deletion-screen phenotypes,
  not a demonstrated molecular pathway; neither is corroborated by a mechanistic study.
- **Whether the in-vitro ATPase/ATP-turnover activity reflects productive substrate
  phosphorylation** (kinase turnover coupled to a real acceptor) vs. basal P-loop
  ATP hydrolysis is not resolved without the acceptor.

## Curation reasoning summary (for the ai-review)

- GO:0016301 kinase activity (ISS, PMID:18004758) — ACCEPT (core). Supported by the intact
  Walker A P-loop + retained URK second block + the paper's ATP-dependent-kinase conclusion.
  Kept general ("kinase activity") deliberately: no substrate is demonstrated, so a specific
  child (e.g. a named small-molecule kinase) would over-specify.
- GO:0016887 ATP hydrolysis activity (IDA, PMID:18004758) — ACCEPT (core MF). Directly
  measured ATP turnover (KM for ATP). This is the experimentally observed activity.
- GO:0016310 phosphorylation (ISS, PMID:18004758) — ACCEPT (BP, non-core-ish but the
  process directly entailed by kinase activity). Kept as-is.
- GO:0005737 cytoplasm (IBA) — ACCEPT/KEEP_AS_NON_CORE. Phylogenetic location call, plausible
  for a soluble P-loop kinase; not core to function.
- GO:0005575 cellular_component (ND) — this is the root "no data" placeholder. KEEP_AS_NON_CORE
  (it is the standard ND stub; nothing to remove, adds no information).
- ATP binding (GO:0005524) is present in UniProt DR (IEA UniProtKB-KW) but NOT in the GOA TSV
  rows. Final decision: add it explicitly as an `existing_annotation` with `action: NEW`
  (original_reference_id GO_REF:0000043, the UniProt-keyword mapping reference) AND include it
  in `core_functions`. Rationale: it is a genuine UniProt annotation and the mechanistic basis
  (Walker A P-loop) of the accepted kinase/ATP-hydrolysis activities, so recording it as a NEW
  annotation makes the provenance explicit rather than leaving it only in core_functions.
