# HMOX1 (Heme oxygenase 1 / HO-1 / HSP32) — review notes

UniProt: P09601 (HMOX1_HUMAN), 288 aa, chromosome 22. HGNC:5013. EC 1.14.14.18.

## Core biology (from UniProt P09601)

- **Molecular function.** HMOX1 catalyzes the oxidative cleavage of heme at the alpha-methene
  bridge carbon, released as carbon monoxide (CO), to generate biliverdin IXalpha, while
  releasing the central heme iron chelate as ferrous iron
  [file:human/HMOX1/HMOX1-uniprot.txt "Catalyzes the oxidative cleavage of heme at the alpha-methene bridge carbon, released as carbon monoxide (CO), to generate biliverdin IXalpha, while releasing the central heme iron chelate as ferrous iron"].
  It is the **rate-limiting** enzyme of heme catabolism.
- **Catalytic reaction (Rhea:RHEA:21764, EC 1.14.14.18).** heme b + 3 reduced [NADPH--hemoprotein
  reductase] + 3 O2 = biliverdin IXalpha + CO + Fe(2+) + 3 oxidized [NADPH--hemoprotein reductase]
  + 3 H2O + H(+). Electrons for catalysis are supplied by NADPH--cytochrome P450 reductase (CPR).
- **Cytoprotection.** "Affords protection against programmed cell death and this cytoprotective
  effect relies on its ability to catabolize free heme and prevent it from sensitizing cells to
  undergo apoptosis" [file:human/HMOX1/HMOX1-uniprot.txt]. Downstream protective mediators:
  biliverdin/bilirubin (antioxidant), CO (signaling/anti-apoptotic), and iron sequestration into
  ferritin.
- **Cofactor/substrate binding.** Heme b binding sites at residues 18, 25 (axial Fe ligand His25),
  134, 183 (UniProt FT BINDING). Asp-140 is important for catalytic activity; D140 mutants are
  inactive as heme oxygenase but gain peroxidase activity [PMID:11121422].
- **Subcellular location.** Endoplasmic reticulum membrane; Single-pass type IV (tail-anchored)
  membrane protein; C-terminal TM anchor (266–288); catalytic domain faces the **cytosol**
  [file:human/HMOX1/HMOX1-uniprot.txt "Endoplasmic reticulum membrane ... Single-pass type IV membrane protein ... Cytoplasmic side"];
  [PMID:22419571 "heme-oxygenase 1 is membrane-bound and faces the cytosol"]. A soluble ~30 kDa form
  arises by proteolytic removal of the membrane anchor [PMID:7703255].
- **Oligomerization.** Homodimer / higher-order homooligomer; oligomerization via the TM segment is
  crucial for stability and function in the ER [PMID:19556236].
- **Induction.** "Heme oxygenase 1 activity is highly inducible by its substrate heme and by various
  non-heme substances such as heavy metals, bromobenzene, endotoxin, oxidizing agents and UVA"
  [file:human/HMOX1/HMOX1-uniprot.txt]. Canonical inducer axis is NRF2 (NFE2L2)–KEAP1 via ARE in the
  HO-1 promoter (e.g. [PMID:26403645], [PMID:18202225]).
- **Disease.** Heme oxygenase 1 deficiency (HMOX1D, MIM:614034): persistent hemolytic anemia with
  marked erythrocyte fragmentation and intravascular hemolysis, endothelial damage, iron deposition,
  asplenia, nephritis, growth retardation. First human case [PMID:9884342].

## Evidence for specific GO annotations

- **heme oxygenase (decyclizing) activity (GO:0004392).** Directly demonstrated for human HO-1:
  truncated hHO-1 "converts heme to biliverdin when reconstituted with rat liver cytochrome P450
  reductase" [PMID:7703255]; full-length hHO-1 degrades heme releasing free iron and CO
  [PMID:17915953]; D140 mutagenesis abolishes heme oxygenase activity [PMID:11121422]. This is the
  well-supported CORE molecular function.
- **heme binding (GO:0020037).** Substrate/cofactor; heme-binding sites resolved crystallographically
  [PMID:12842469 via UniProt FT]; direct binding characterized [PMID:17915953]. CORE.
- **heme catabolic process (GO:0042167) / heme oxidation (GO:0006788).** Direct process terms for the
  catalytic activity; well supported [PMID:7703255, PMID:17915953]. CORE BP.
- **protein homodimerization activity (GO:0042803) / structural molecule activity (GO:0005198) /
  identical protein binding (GO:0042802).** All from [PMID:19556236] (homo-oligomerization via TM
  segment). Homodimerization is real and functionally relevant (stability in ER). `structural
  molecule activity` (GO:0005198) is a mis-typing of the oligomerization observation — HO-1 is an
  enzyme, not a structural/scaffolding molecule; MARK_AS_OVER_ANNOTATED. Homodimerization kept as
  non-core.
- **intracellular iron ion homeostasis (GO:0006879).** HO-1 releases Fe2+ from heme and its
  overexpression reroutes iron into ferritin, reducing redox-active "loose" iron [PMID:22989377,
  PMID:17915953]. Reasonable downstream consequence; KEEP_AS_NON_CORE.
- **negative regulation of ferroptosis (GO:0110076).** IMP from [PMID:26403645]: knockdown of HO-1
  (with NQO1/FTH1) promoted ferroptosis; NRF2 target. Note HO-1 can be double-edged for ferroptosis
  (iron release), but the cited paper supports a protective role. KEEP_AS_NON_CORE.
- **response to oxidative stress (GO:0006979).** IMP [PMID:9884342] (patient LCL hypersensitive to
  oxidative injury) + IBA. Core stress-response consequence; KEEP_AS_NON_CORE (it is a downstream
  physiological role, not the MF).
- **Angiogenesis / smooth-muscle / leukocyte / chemokine / NF-kB / LDL / nicotine / heat / wound
  healing terms.** These are pleiotropic downstream physiological consequences of HO-1
  induction/products (CO, biliverdin, iron) in specific cell/disease contexts. Mostly TAS/IDA/IMP/IGI
  from individual papers. Keep as NON_CORE (they are genuine observations but not the enzyme's core
  molecular role). `structural molecule activity` and `regulation of transcription by RNA polymerase
  II` are over-annotations (HO-1 is not a transcription factor; the ISS to P06762/rat is a weak
  transfer).
- **enzyme binding (GO:0019899).** ISS from rat HO-1 (P06762) re CPR interaction [PMID:15516695];
  HO-1 does functionally dock with NADPH-CPR. Generic; KEEP_AS_NON_CORE (the specific, informative MF
  would be an oxidoreductase/electron-acceptor interaction with CPR). Could support a proposed
  more-specific term but kept conservatively.

## Protein-binding (GO:0005515) IPI annotations — over-annotation flags

- Many bare `protein binding` IPI annotations from high-throughput interactome screens:
  - PMID:21044950 (POT1, YFP-complementation telomere screen) — HTP; not an informative function.
  - PMID:32296183 (HuRI reference binary interactome) — 25 partners (AQP6, ARL13B, CD79A, COQ9,
    CPLX4, CRB3, CYB561, CYBRD1, ELOVL4/5/6, ERGIC3, FAM174A, FAM209A, FAM210B, GPR152, JAGN1,
    MSMO1, PDZK1IP1, SEC11C, SLC16A7, STX1A, TLCD4, TM4SF19, TMEM14B). Most are ER/membrane proteins
    co-detected in the assay; likely reflect membrane co-localization, not specific function.
  - PMID:32353859, PMID:32838362, PMID:33060197, PMID:36217030, PMID:35239449 — SARS-CoV-2 ORF3a
    (P0DTC3) interactome studies. HMOX1–ORF3a interaction is real and reported in UniProt
    (host-virus), promotes ORF3a-induced autophagy [PMID:35239449]. Non-core; MARK_AS_OVER_ANNOTATED
    the bare `protein binding` (the specific host-virus interaction is captured in notes/UniProt).
  - PMID:21597468 (eEF1Bδ, P29692-2) — eEF1BδL binds NRF2 and induces HO-1; the IPI captures a
    HO-1/eEF1Bδ association context. Non-core.
  All bare `protein binding` IPIs: MARK_AS_OVER_ANNOTATED (never REMOVE per policy).
- `identical protein binding (GO:0042802)` [PMID:19556236]: real homo-oligomerization — MODIFY toward
  the more informative `protein homodimerization activity` (GO:0042803), which is separately
  annotated. Keep non-core.

## Localization annotations

- ER membrane (GO:0005789) — strongly supported experimental core location [PMID:19556236,
  PMID:27184847, PMID:22419571]; ACCEPT/KEEP.
- ER (GO:0005783) — parent of ER membrane; KEEP_AS_NON_CORE (less specific).
- perinuclear region of cytoplasm (GO:0048471) [PMID:22503972] — IDA; plausible ER-associated
  perinuclear staining; non-core.
- nucleus / nucleoplasm (GO:0005634, GO:0005654) — reported nuclear translocation of a cleaved HO-1
  fragment under stress (sub-pool). ISS from rat (P06762) and Ensembl/Reactome. KEEP_AS_NON_CORE
  (secondary, context-specific).
- mitochondrial outer membrane (GO:0005741) — Reactome TAS; reported stress relocalization sub-pool;
  KEEP_AS_NON_CORE.
- cytosol (GO:0005829) — Reactome TAS; the soluble/cleaved form and the cytosol-facing active site
  are consistent with this; KEEP_AS_NON_CORE.
- plasma membrane (GO:0005886) IBA — not a substantiated HO-1 location for human; likely PANTHER
  tree artifact (some family members). Weak; KEEP_AS_NON_CORE (not removing IBA).
- extracellular region / extracellular space (GO:0005576) TAS [PMID:18307065] — pre-eclampsia serum
  HO-1; HO-1 is intracellular, secretion is atypical/context-specific; KEEP_AS_NON_CORE.
- membrane (GO:0016020) TAS [PMID:3345742] — generic parent of ER membrane; MARK_AS_OVER_ANNOTATED
  (uninformative given specific ER membrane annotations).

## Core function summary

1. Heme oxygenase (decyclizing) activity (GO:0004392) — rate-limiting oxidative cleavage of heme to
   biliverdin IXalpha + CO + Fe2+, using O2 and electrons from NADPH-CPR. MF core; BP: heme catabolic
   process (GO:0042167) / heme oxidation (GO:0006788); location: ER membrane (GO:0005789).
2. Heme binding (GO:0020037) — substrate/cofactor binding required for catalysis.
3. Protein homodimerization activity (GO:0042803) — homo-oligomerization via the C-terminal TM anchor,
   required for stability/function in the ER (structural/enzymatic support role, non-core but real).
</content>
</invoke>
