# F6LAX4 (Triticum aestivum) — review notes

## Identity
- UniProt: **F6LAX4** (TrEMBL, unreviewed; secondary AC A0A9R1HFG5)
- Organism: *Triticum aestivum* (bread wheat), NCBI:txid4565
- Gene name (UniProt): `LOC123103357` (GeneID 123103357); synonym `LOC123120841`
- EnsemblPlants models: TraesCS5A02G168400.5 (chr 5A), TraesCS5B02G165200.3 (5B), TraesCS5D02G172700.4 (5D)
  → homoeolog set across the A/B/D subgenomes (hexaploid wheat).
- SubName (UniProt): "Protein phosphatase 2A structural subunit"
- Length 587 aa, MW 65,502 Da (~65 kDa → classic PR65/A-subunit size)
- PE 3 (inferred from homology). No experimental references; only a genomic submission + EnsemblPlants identification.

## Domain architecture / family
- Family (UniProt SIMILARITY): "phosphatase 2A regulatory subunit A family" (ARBA00038332).
- PANTHER **PTHR10648** = "Serine/threonine-protein phosphatase PP2A 65 kDa regulatory subunit";
  subfamily **PTHR10648:SF4** = PP2A regulatory subunit A, beta-isoform-related.
- InterPro: IPR051023 (PP2A_Regulatory_Subunit_A), IPR054573 (PP2A/SF3B1-like HEAT),
  IPR016024/IPR011989 (ARM-type fold / ARM-like), IPR000357 + IPR021133 (HEAT, HEAT type 2).
- Pfam PF02985 (HEAT) + PF22646 (PPP2R1A-like HEAT). SUPFAM SSF48371 (ARM repeat). Gene3D 1.25.10.10.
- FunFam FF:000062 = "Ser/Thr protein phosphatase 2A regulatory subunit A alpha isoform".
- PROSITE: 12 HEAT_REPEAT matches; UniProt FT lists ~13 HEAT repeats spanning essentially the
  whole protein (aa 10–587). This is the hallmark architecture of the PP2A scaffolding **A subunit**
  (PR65 / PPP2R1A): an entirely α-helical, horseshoe-shaped solenoid of ~15 HEAT repeats with no
  catalytic activity — a pure protein–protein interaction scaffold.

## Functional interpretation (family-level, by homology)
PP2A is a major Ser/Thr phosphatase that functions as a heterotrimeric holoenzyme:
- **A (scaffolding/structural) subunit** — PR65 / PPP2R1A; this protein. HEAT-repeat solenoid that
  binds the catalytic (C) subunit on its C-terminal HEAT repeats and a regulatory (B/B'/B'') subunit
  on its N-terminal HEAT repeats, holding the holoenzyme together and positioning substrates.
- **C (catalytic) subunit** — PPP2CA/B, the phosphatase active site.
- **B (regulatory) subunits** — B/B55, B'/B56, B''/PR72, B'''/striatin families; confer substrate
  specificity and localization.

The A subunit has no catalytic activity itself; functionally it is annotated as a phosphatase
**regulator/structural** subunit because by scaffolding the C and B subunits it is required for
holoenzyme assembly and thereby modulates phosphatase activity (GO:0019888 protein phosphatase
regulator activity; note GO:0008601 "PP2A regulator activity" is obsolete and merged into
GO:0019888 — verified via QuickGO).

In plants, the A (scaffolding) subunits are a small family. The best-characterized ortholog is
*Arabidopsis* **RCN1 / PP2AA1** (plus PP2AA2, PP2AA3), which scaffolds PP2A holoenzymes acting in
auxin transport/signaling, ABA responses, ethylene signaling, and brassinosteroid/BIN2 regulation.
Wheat F6LAX4 is a direct ortholog (PTHR10648 A-subunit clade), so the conserved core role is as the
**structural scaffold of the PP2A holoenzyme**.

## GOA annotations (5; all IBA or IEA — no experimental evidence)
1. GO:0000159 protein phosphatase type 2A complex — IBA (part_of), GO_REF:0000033 → **ACCEPT** (core; defining complex for the A subunit).
2. GO:0019888 protein phosphatase regulator activity — IBA (enables), GO_REF:0000033 → **ACCEPT** (core MF; standard for A/B subunits; no more specific term exists).
3. GO:0005634 nucleus — IEA/ARBA (located_in), GO_REF:0000117 → **ACCEPT** (PP2A holoenzymes act in both nucleus and cytoplasm; consistent with IBA nucleus from GO_Central).
4. GO:0005737 cytoplasm — IEA/ARBA (located_in), GO_REF:0000117 → **ACCEPT** (PP2A is predominantly cytoplasmic/cytosolic).
5. GO:0032991 protein-containing complex — IEA/ARBA (part_of), GO_REF:0000117 → **MARK_AS_OVER_ANNOTATED**
   (true but uninformative root-level term; fully subsumed by the more specific GO:0000159 already present).

## Notes on evidence
- No PMIDs in GOA (only GO_REFs); `fetch-gene-pmids` found nothing to cache.
- Entry is TrEMBL/PE3; all functional inference is by homology (IBA + ARBA IEA). Decisions rest on
  the unambiguous, deeply conserved domain architecture and family assignment, not on wheat-specific
  experiments.
