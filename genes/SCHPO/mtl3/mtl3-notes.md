# mtl3 (SPBC215.13, UniProt O94317) — curation notes

## Identity and a critical name disambiguation

**mtl3** is the PomBase standard name for *S. pombe* systematic-name **SPBC215.13**,
UniProt **O94317** (entry name `YH5D_SCHPO`, 534 aa). PomBase product description
(verbatim): **"plasma membrane-associated serine-rich cell wall sensor Mtl1/Mtl3"**;
PomBase name description: **"S. cerevisiae Mid Two-Like"**; PomBase exact synonym: **mtl1**.
So the gene symbol string "mtl1"/"mtl3" here means **"Mid Two-Like"** (Mtl = *Mid Two-Like*),
i.e. this is a **Mid2-like cell-wall-integrity (CWI) stress sensor**.

**IMPORTANT — this is NOT the Mtr4-like RNA helicase.** The curation task described mtl3 as
"a Mtr4-like DExH RNA-helicase-family member related to the nuclear RNA-surveillance/MTREC
machinery." That description is a **name collision**: in *S. pombe* the **Mtr4-like helicase**
is a *different* gene, PomBase standard name **mtl1 = SPAC17H9.02** (an MTREC/NURS-complex
DExH-box RNA helicase; UniProt O60058), reviewed e.g. in
[PMID:24210919 "Mtr4-like protein coordinates nuclear RNA processing..."] and
[PMID:26089201 (MTREC targets CUTs), Nat Commun 6:7050]. The two share the abbreviation
"Mtl" but stand for entirely different things (Mid-Two-Like vs Mtr4-Like). The UniProt
record for O94317 is decisive: it is a **serine-rich GPI-anchored plasma-membrane/ER
precursor with a signal peptide and a single N-terminal transmembrane segment — there is
NO helicase domain, NO DExH/DEAD box, NO Walker A/B (P-loop) NTPase motif, and NO
arch/KOW domain**. All downstream reasoning below treats mtl3/SPBC215.13 strictly as the
Mid2-like cell-wall sensor.

## Domain / sequence analysis (inline, from the UniProt record O94317)

- 534 aa; MW 53.4 kDa. `PE 1: Evidence at protein level`.
- **Signal peptide** 1–22 (ECO:0000255) → secretory-pathway entry.
- **Single transmembrane segment** ~7–29 (TMHMM, PomBase) near the N-terminus.
- **GPI-anchor** predicted (KW GPI-anchor, Lipoprotein; PROPEP `?..534` "Removed in mature form",
  ECO:0000255) — C-terminal signal for GPI attachment; MOD:00818 (PomBase).
- **Two large disordered / low-complexity regions** (MobiDB-lite: 70–145 and 176–418;
  PomBase low-complexity: 62–89, 92–420, 426–445, 449–492, 501–517). The sequence is
  strikingly **serine-rich** (long runs of S/T/P), the hallmark of the O-mannosylated,
  cell-wall-facing ectodomain of fungal CWI mechanosensors.
- **N-glycosylation** at N31 and N426 (ECO:0000255; PMID:36408920 for the PSI-MOD sites).
- Subcellular location (UniProt): **Endoplasmic reticulum** (ECO:0000269|PubMed:16823372,
  ORFeome GFP localization) and **Cell membrane; Lipid-anchor, GPI-anchor** (ECO:0000305).
- **Catalytic competence:** none inferred — no enzymatic domain of any kind. This is a
  structural/signaling single-pass membrane glycoprotein, consistent with a cell-surface sensor.

Architecture summary: N-terminal signal peptide + single TM anchor → long serine/threonine-rich
(O-mannosylation-prone) extracellular ectodomain → C-terminal GPI-anchor addition. This is the
canonical architecture of fungal plasma-membrane cell-wall stress sensors (Wsc/Mid2/Mtl family).

## What is KNOWN (with provenance)

- **Localization:** external side of the plasma membrane / cell surface; GPI-anchored.
  [GOA GO:0009897 external side of plasma membrane, TAS PMID:12845604]; ER + cell membrane
  [UniProt, PubMed:16823372 ORFeome localization; PubMed:12845604 GPI prediction].
  PMID:12845604 is the genome-wide fungal-GPI-protein prediction study
  ["only 33 GPI candidates were identified" in Sz. pombe] — supports GPI/cell-surface class,
  abstract-only (full_text_available: false).
- **It is a member of the Mid2-like cell-wall sensor family** (PomBase name "Mid Two-Like";
  product "cell wall sensor Mtl1/Mtl3"). The *S. pombe* CWI sensor family (Wsc1, Mtl2, Mid2-like
  proteins) are single-pass, Ser/Thr-rich, O-mannosylated membrane sensors that signal to the
  Rho1 GTPase [PMID:23907979 Cruz et al. 2013 MicrobiologyOpen; Mtl2 and Wsc1 turn on Rho1p;
  family context, not mtl3-specific evidence].
- **Deletion phenotypes (mtl3Δ), curated in PomBase from a genome-wide phenomics screen**
  [PMID:37787768 Rodríguez-López et al. 2023 eLife, phenomics/ML dataset]:
  altered sensitivity/resistance to cell-wall/membrane and ionic stressors — sensitive to
  SDS + MgCl2, ethanol, lithium, cycloheximide; resistant to EGTA, KCl+SDS, MgCl2+SDS,
  tert-butyl hydroperoxide; loss of viability in stationary phase; increased vegetative
  growth; otherwise viable with normal morphology (FYPO terms listed in PomBase). These are
  the classic phenotypic signatures of a CWI/membrane stress sensor. NOTE: this is a
  large-scale dataset paper; it does not discuss mtl3 by name in the text, so no verbatim
  mtl3-specific quote is available — the annotations derive from the supplementary phenotype matrix.
- **Post-transcriptional regulation:** mtl3 mRNA is a target in a systematic RNA-stability /
  RNA-binding-protein study [PMID:25375137 Hasan et al. 2014 PLoS Genet]; PomBase records mtl3
  as a target-of (zfs1) mRNA-binding annotation. Again a systematic dataset (no in-text mtl3 prose).
- **Ortholog:** *S. japonicus* SJAG_00415 (also named mtl3) [PMID:21511999, PomBase ortholog annotation].
  Taxonomic distribution "Schizosaccharomyces specific" per PomBase.
- PomBase characterization status: **"biological role published"** (i.e. a biological role has
  been assigned, chiefly via the phenomics phenotype profile and family membership).

## What is NOT known (knowledge gaps)

- **No experimentally demonstrated molecular function.** GOA MF is GO:0003674 (ND). No ligand,
  no direct binding partner, no signaling-output assay published *for mtl3 specifically*. Its
  proposed role as a Rho1/CWI-pathway sensor is inferred from family membership and phenotypes,
  not shown directly for this protein.
- **No direct evidence of the signaling pathway it feeds** (Rho1 GEFs? Pmk1 MAPK? Mkh1–Pek1–Pmk1
  cascade?). Note the related sensors Mtl2/Wsc1 signal to Rho1 but were reported to act
  *independently of* Pmk1 MAPK [PMID:23907979]; whether mtl3 uses the MAPK-independent Rho1 route is unknown.
- **Redundancy / genetic relationships** with the other S. pombe cell-wall sensors (wsc1, mtl2,
  and any mid2-like paralog) are not established for mtl3.
- **No structure** (only AlphaFold model). No biochemistry (glycosylation confirmed only by
  prediction + one PSI-MOD dataset). The Ser/Thr-rich ectodomain O-mannosylation is inferred.
- Whether the ER localization (ORFeome GFP) is the mature steady-state site or an
  overexpression/trafficking artifact vs. the functional plasma-membrane pool is unresolved.

## Curation plan for the 5 GOA annotations

1. GO:0005783 endoplasmic reticulum (IEA, GO_REF:0000044, located_in) — KEEP_AS_NON_CORE.
   Supported by UniProt SubCell (ORFeome GFP, PubMed:16823372); plausible as secretory-pathway
   transit; not the primary functional site.
2. GO:0005886 plasma membrane (IEA, GO_REF:0000044, located_in) — ACCEPT (core location; but the
   more specific external-side term below is preferable). Keep; MF/location core is the cell surface.
3. GO:0003674 molecular_function (ND, GO_REF:0000015) — KEEP_AS_NON_CORE / accept the ND: honestly
   reflects that no MF has been experimentally determined. (ND root — cannot MODIFY to a specific
   MF without evidence; flag as knowledge gap rather than invent an MF.)
4. GO:0008150 biological_process (ND, GO_REF:0000015) — same: ND root reflects no assigned BP.
   A cell-wall-integrity/stress-response BP is *inferred* from phenotypes but not directly shown;
   do not over-annotate. Keep ND; note gap.
5. GO:0009897 external side of plasma membrane (TAS, PMID:12845604, is_active_in) — ACCEPT.
   Most specific, best-supported localization (GPI-anchored ectodomain on the outer PM face).

## Falcon deep-research corroboration (independent)

The falcon deep-research report (`mtl3-deep-research-falcon.md`, generated 2026-07-06 with the
correct O94317/SPBC215.13 context) independently reached the SAME identity and disambiguation:
it classifies mtl3/SPBC215.13 as a putative GPI-anchored, serine/threonine-rich cell-surface
glycoprotein of the "Mid two-like" family, and includes a dedicated section explicitly stating
that mtl3 is "functionally and structurally unrelated" to the Mtr4-like MTREC helicase Mtl1
"despite the superficial similarity in naming". It likewise notes that the symbol "mtl3" does
not appear in the retrieved primary literature (dark gene), so identity is anchored to the
systematic ID + UniProt accession. This is independent confirmation of the review's central
finding; no fabricated function was introduced.
