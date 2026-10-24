# A0A674PKV4 (Takifugu rubripes gas7a) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Identity
- A0A674PKV4 (401 aa, TrEMBL, PE 4) is one of three UniProt entries from the single fugu
  Ensembl gene ENSTRUG00000029588 (gas7a): A0A674PKV4 (ENSTRUT00000065002, 401 aa),
  A0A674NVV7 (ENSTRUT00000068268, 392 aa), A0A674NLH4 (ENSTRUT00000080391, 357 aa).
  None is reviewed; A0A674PKV4 is the longest model, so it is an alternative gene model
  (isoform) of fugu gas7a, not a fragment, and there is no reviewed canonical fugu entry.
  [file:TAKRU/A0A674PKV4/A0A674PKV4-bioinformatics/RESULTS-rereview.md]
- Architecture: N-terminal ~90 aa poorly conserved, WW-FCH linker (PF16623), F-BAR 121-381,
  ~20 aa C-terminal tail. Aligns to human GAS7 O60861 residues 43-476 at 72.5% identity and
  to mouse Gas7 Q60780 1-421 at 73.9%. No SH3 domain; no canonical WW motif detected.
  Mouse/human GAS7 isoforms differ in exactly these N-terminal modules
  [PMID:31628328 "In addition to the F-BAR domain, GAS7b possess a WW domain, and GAS7cb and GAS7c possesses a WW and an SH3 domain, while GAS7d contains only the F-BAR domain."].
- PANTHER PTHR23065:SF57 (GROWTH ARREST-SPECIFIC PROTEIN 7), same subfamily as human,
  mouse and rat GAS7 (interpro/panther/PTHR23065/PTHR23065-entries.csv). Family review
  interpro/panther/PTHR23065/PTHR23065-review.yaml records the same SF57 placement; no
  disagreement.

### Evolutionary source of the GOA rows
All 7 GOA rows are TreeGrafter IEA (GO_REF:0000118) from PANTHER:PTN007729058. Matching
term sets in PTHR23065-paint.tsv show three ancestral IBD nodes feed them:
- PTN002747256 (Eukaryota): cytoplasm, plasma membrane; many seeds across the family.
- PTN000552124 (Bilateria): clathrin-coated pit, clathrin-coated vesicle, clathrin coat
  assembly, clathrin-dependent endocytosis. Seeds are FCHO2 (MGI:3505790, Q0JRZ9), FCHO1
  (O14526) and C. elegans fcho-1 only. No GAS7 seed.
- PTN001890901 (Chordata): neuron projection morphogenesis, seeded by mouse Gas7
  (MGI:1202388).
The clathrin terms therefore come from the muniscin (FCHO) branch. FCHO function at
clathrin-coated pits depends on parts GAS7 lacks: the C-terminal muHD
[PMID:22484487 "Precise deposition of FCHO1 at clathrin foci therefore depends, in part, on the C-terminal μHD."]
and an AP2-activating linker motif
[PMID:25303366 "amino acid motif, found in both FCHo and SGIP proteins, that directly binds AP2."].
No GAS7 experimental study reports clathrin-pit localization or a role in clathrin-mediated
endocytosis; the GAS7 paper explicitly contrasts phagocytosis with clathrin endocytosis and
shows GAS7 sheets on flat membranes [PMID:31628328]. I treat the clathrin terms as
over-annotation (functional divergence of the GAS7 lineage from the FCHO-defined node),
not as demonstrably false: MARK_AS_OVER_ANNOTATED, not REMOVE.

### GAS7 biology (mammalian orthologs, same subfamily)
- Mouse gas7 knockdown impedes Purkinje neurite outgrowth; overexpression promotes
  neurite-like outgrowth [PMID:9736752].
- Gas7 binds N-WASP via WW-Pro and recruits Arp2/3 for membrane protrusions/neurites
  [PMID:20150425]. Because A0A674PKV4 lacks a canonical WW motif, this WW-dependent step
  is not transferred to this model.
- GAS7 F-BAR forms 2D sheets on flat plasma membrane at phagocytic cups and is needed for
  macrophage phagocytosis [PMID:31628328]. Not proposed as NEW for fugu (macrophage-only,
  WW-containing GAS7b, and PAINT has not placed phagocytosis on the GAS7 node).

### Decisions
- cytoplasm: KEEP_AS_NON_CORE. plasma membrane: ACCEPT (F-BAR membrane binding is core).
- clathrin-coated pit / clathrin-coated vesicle / clathrin coat assembly /
  clathrin-dependent endocytosis: MARK_AS_OVER_ANNOTATED.
- neuron projection morphogenesis: ACCEPT (PAINT GAS7-specific node seeded by mouse Gas7).
- No NEW annotations.

### Relative
No reviewed canonical fugu gas7a product exists, so the relative is the experimentally
characterised ortholog in the same subfamily that seeds the GAS7 PAINT node: mouse Gas7
(Q60780, MGI:1202388). No genes/mouse/Gas7 or genes/human/GAS7 review exists.

### Modules
No module contains GAS7. Context only: modules/phagocytic_engulfment.yaml (mammalian GAS7
phagocytic cup role) and modules/synaptic_vesicle_endocytosis.yaml (uses PTHR23065 for the
PACSIN branch, a different subfamily).
