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

## Follow-up review refinements (inline items)
- **gene_symbol**: changed from the accession `F6LAX4` to the UniProt/NCBI gene name
  `LOC123103357` (the actual locus symbol; the accession remains the `id`).
- **cytosol (GO:0005829)**: the F6LAX4 UniProt record's GO cross-references include
  `GO:0005829; C:cytosol; IBA:GO_Central`, but the fetched GOA snapshot dropped it and kept
  only the ARBA IEA `cytoplasm`. Cytosol is the more specific, GO_Central-supported compartment,
  so the cytoplasm annotation was changed to `MODIFY` with proposed replacement GO:0005829, and
  `core_functions.locations` updated to cytosol + nucleus.
- **Biological process (BP)**: deliberately none. Checked GO_Central annotations on the human
  ortholog PPP2R1A (P30153, in the GOA WITH/FROM column) via QuickGO: its only IBA BP terms are
  `GO:0051225 spindle assembly` and `GO:0051754 meiotic sister chromatid cohesion, centromeric` —
  animal mitosis/meiosis-specific functions that GO_Central correctly did NOT propagate to the
  plant ortholog. Inventing a BP for wheat F6LAX4 would be unsupported; the scaffold's role is
  fully captured by MF (regulator activity) + complex membership + localization. Documented as a
  comment above `core_functions` in the YAML.

## Notes on evidence
- No PMIDs in GOA (only GO_REFs); `fetch-gene-pmids` found nothing to cache.
- Entry is TrEMBL/PE3; all functional inference is by homology (IBA + ARBA IEA). Decisions rest on
  the unambiguous, deeply conserved domain architecture and family assignment, not on wheat-specific
  experiments.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Re-examined every annotation against PAINT node placement,
a new phylogeny and cached literature.

### Identity
- F6LAX4 (587 aa) is a full-length A subunit (Arabidopsis PP2AA1-3 are 587-588 aa, human PPP2R1A 589 aa).
  It is the longest wheat PTHR10648:SF4 entry; the other wheat entries for LOC123103357/LOC123120841
  (A0A341VDM8 583, A0A341UW13 562, A0A341WDI6 558, A0A3B6MQ20 578, A0A3B6KFF3 571, A0A3B6MQ25 407 aa)
  are shorter isoforms or homoeolog models. F6LAX4 is the canonical product, not a fragment or isoform.

### Phylogeny (file:WHEAT/F6LAX4/F6LAX4-bioinformatics/RESULTS-rereview.md)
- New script `phylogeny_rereview.py` (MAFFT + NJ, 21 sequences). F6LAX4 groups with grass A subunits;
  eudicot A subunits (tomato + Arabidopsis PP2AA1/RCN1, PP2AA2, PP2AA3) form their own group, so the
  three Arabidopsis paralogs are eudicot-specific and F6LAX4 is a co-ortholog of all three
  (identity 85.2% RCN1, 89.8% PP2AA2, 88.6% PP2AA3; 59.3% human PPP2R1A).
- PANTHER subfamily discrepancy: grass/Amborella/moss A subunits are in SF4 with fly, worm, yeast and
  Dictyostelium scaffolds; Arabidopsis PP2AA1 is SF29 and PP2AA2/3 SF36. Sequence identity shows this
  is an HMM-boundary artefact, not functional divergence. The PTHR10648 family review
  (interpro/panther/PTHR10648/PTHR10648-review.yaml) records F6LAX4 in SF4 and does not discuss this
  split; no disagreement on placement, but its SF4 description is wheat-only.

### PAINT nodes (interpro/panther/PTHR10648/PTHR10648-paint.tsv)
- PTN000068663 (Eukaryota): GO:0000159, GO:0005634, GO:0005829 IBDs -> covers F6LAX4.
- PTN000068596: GO:0005737, GO:0019888 and GO:0140378 protein complex scaffold activity (IBD 2026-06-03,
  seed P30153). F6LAX4 receives GO:0019888 from this node, so GO:0140378 is expected to propagate;
  added as NEW (IBA).
- PTN000068664: spindle assembly / meiotic centromeric cohesion BP IBDs on an animal/fungal subclade;
  not propagated to F6LAX4 — deliberate, so no BP added.
- PTN000068762: IRD NOT cytosol on Arabidopsis PP2AA3 leaf only; does not cover grasses.

### Changes vs previous review
- GO:0000159, GO:0019888: ACCEPT (unchanged), now supported by PMID:17174897 and the human PPP2R1A
  curated UniProt function text instead of only the deep-research file.
- GO:0005634 nucleus: ACCEPT, now supported by PMID:22404109 (Arabidopsis A1/A2/A3 in nucleus and cytosol).
- GO:0005737 cytoplasm: MODIFY -> GO:0005829 cytosol (unchanged action; PMID:22404109 support).
- GO:0032991 protein-containing complex: MARK_AS_OVER_ANNOTATED -> TOO_GENERAL (true, entailed by GO:0000159).
- NEW GO:0140378 protein complex scaffold activity; core function MF switched to it, with
  GO:0019888 as a second core function; in_complex GO:0000159 added.
- Description rewritten to drop Arabidopsis-specific BRI1/BZR1 claims stated as if they were wheat
  functions, and to record co-orthology.

### Relative to review next
- Arabidopsis PP2AA1/RCN1 (Q38845), the best genetically characterised co-ortholog; no review in repo
  (Drosophila Pp2A-29B is reviewed; human PPP2R1A review is DRAFT).

### Modules
- modules/dmel_pp2a_holoenzymes.yaml (PP2A complex, fly-specific); modules/brassinosteroid_signaling.yaml
  and modules/auxin_polar_transport.yaml mention PP2A in plants but do not model the A subunit.
