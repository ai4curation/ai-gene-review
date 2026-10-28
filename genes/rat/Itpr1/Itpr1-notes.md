# Itpr1 (rat) review notes

## Session 2026-10-28

- Fetched with `just fetch-gene rat Itpr1`; UniProt P29994 (RGD:2933, GeneID 25262), 133 GOA rows.
- Cached all GOA PMIDs plus PMID:19845505, PMID:20189985, PMID:21550988 (Taylor lab; rat IP3R1
  constructs) and three donor papers behind human ISO rows (PMID:16793548, PMID:28598420,
  PMID:10828023).
- No deep-research provider run; literature synthesis is in `Itpr1-deep-research-manual.md`.

### Key decisions

- Core: IP3-gated Ca2+ channel activity (GO:0005220) in the ER membrane, executing release of
  sequestered Ca2+ into cytosol by the ER (GO:1903514). Rat-specific bilayer, nuclear patch-clamp
  and cryo-EM data [PMID:15533917, PMID:22547632, PMID:36376291].
- Parent MF/BP terms (ion channel, calcium channel, intracellularly gated channel, ion transport,
  calcium ion transport, regulation of cytosolic Ca2+) -> MODIFY to the specific terms.
- "positive regulation of cytosolic calcium ion concentration" and "regulation of cytosolic calcium
  ion concentration": IP3R1 is the transporter, not a regulator; GO:0051209 is not an is_a child of
  GO:0007204 in the current GO, so these are MODIFY to the transport term.
- `calcium channel inhibitor activity` and `negative regulation of calcium-mediated signaling` ISO
  rows come from human ITPR1 IDA rows on PMID:16793548, a paper on IRBIT (AHCYL1) inhibiting the
  IP3R ["IRBIT suppresses the activation of IP3R by competing with IP3"]. The inhibitor is IRBIT,
  not ITPR1, so the human source rows look mis-attributed; removed here and flagged for an expert.
- `phosphatidylinositol binding` IBA/ISO/ISS: IP3 is a soluble inositol phosphate, not a
  phosphatidylinositol; MODIFY to inositol 1,4,5 trisphosphate binding.
- Secretory granule / transport vesicle / platelet dense granule membranes: contentious
  [PMID:19845505]; marked over-annotated.
- `calcineurin complex` (mouse ISO): IP3R1 co-precipitates with calcineurin but is not a subunit;
  marked over-annotated.
- Hypoxia rows (IEP, ISO, ARBA): expression change only; marked over-annotated.
- Bare protein binding rows: REMOVE, except syntaxin 1B -> MODIFY to SNARE binding.
- Physiological roles (liver regeneration, hepatocyte proliferation, neurite outgrowth, apoptosis,
  fertilization, epithelial fluid transport, TCR signalosome) kept as non-core.
- No NEW terms proposed.

## 2026-10-28 review-fix pass

- source_defects on the GO:0019855 and GO:0050849 rows: corrected_value is now the CURIE UniProtKB:O43865 (human AHCYL1/IRBIT, checked by UniProt REST), with the name moved to corrected_label.
