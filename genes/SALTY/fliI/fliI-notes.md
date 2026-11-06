# fliI (Salmonella Typhimurium LT2, P26465, STM1972) - review notes

## Identity
- UniProt P26465, gene fliI (syn. flaAIII, flaC), locus STM1972. 456 aa. InterPro IPR005714
  (T3SS ATPase FliI/YscN), IPR020005 (FliI clade 1); PANTHER PTHR15184:SF81 "FLAGELLUM-SPECIFIC
  ATP SYNTHASE". PDB 2DPY (FliI 19-456, ADP), 5B0O, 5KP0.
- UniProt RecName "Flagellum-specific ATP synthase", EC 7.1.2.2 (H+-transporting two-sector ATPase),
  catalytic activity by PROSITE-ProRule only. The FUNCTION text ("catalytic subunit of a protein
  translocase ... or a proton translocase involved in local circuits at the flagellum") is taken
  verbatim from the 1991 sequence paper hypothesis [PMID:1646201 "We hypothesize that FliI is either
  the catalytic subunit of a protein translocase for flagellum-specific export or a proton
  translocase involved in local circuits at the flagellum."]. The proton-translocase alternative was
  never supported. The appropriate EC for the export ATPase is 7.4.2.8 (protein-secreting ATPase).

## Biochemistry (this protein)
- Discovered via filament-regrowth screen; fliI mutants cannot regrow filaments -> flagellum-specific
  export [PMID:1646201 "flhA, fliH, fliI, and fliN mutants showed no or greatly reduced regrowth"].
- Walker/catalytic mutants (K188, D272, Y363) abolish flagellation; anti-F1-beta antibody
  cross-reacts [PMID:8491729 "Site-directed mutagenesis of residues in FliI that correspond to
  catalytically important residues in the F1 beta subunit resulted in loss of flagellation"].
- Purified His-FliI: Mg2+-dependent ATPase, kcat 0.16 s-1, Km 0.3 mM; insensitive to F/V/P-type
  ATPase inhibitors [PMID:8943245 "The activity was not affected by inhibitors of the F-, V- or
  P-type ATPases"].
- Oligomerises in presence of ATP to a sixfold ring (~10 nm) with positive cooperativity; phospholipids
  enhance [PMID:12787361 "FliI ring structure has sixfold symmetry"; "oligomerization and enzyme
  activity are coupled"].
- Crystal structure (ADP form) resembles F1 alpha/beta; hexamer model on alpha3beta3gamma
  [PMID:17202259 "despite the apparently different functions of these proteins"].
- FliJ (gamma-like coiled coil) binds centre of FliI6 ring and promotes ring formation [PMID:21278755].
- FliH binds FliI, inhibits ATPase (negative regulator) [PMID:10998179].
- FliH/FliI/FliJ soluble complex binds substrates and delivers to FlhA/FlhB [PMID:10712687].
- FliI binds the export chaperone FliT (C-terminal truncation FliT94 binds strongly) [PMID:20421493].
- Two pools: FliI6 ring in the C ring and cytoplasmic FliH2FliI [PMID:26916245]; ring docks via
  FliH-FlhA and FliH-FliN [PMID:33846530].

## Energetics
- FliH-FliI dispensable given FlhA/FlhB bypass mutations; PMF essential; ATP hydrolysis releases
  FliH-FliI from substrate [PMID:18216858]. Proton-driven exporter [PMID:18216859].
- Export gate by itself is a proton-protein antiporter; FliH-FliI brings about FliJ-FlhA binding
  turning it into an efficient delta-psi driven exporter [PMID:21934659].
- E211D: ATPase ~100x lower but >80% cells motile [PMID:25531309].
- Increased PMF / substrate levels bypass ATPase [PMID:25393010].
- In vitro inverted-vesicle reconstitution: ATP hydrolysis by FliI can drive export without PMF;
  FlhA has ion-channel activity [PMID:29946050].
- FliH/FliI help FlhA impose strict export order [PMID:38531947].

## ATP-synthase-family GO rows
- GO:0046933 (IBA, contributes_to) and GO:0045259 (IBA) from PANTHER:PTN008558586. Per
  projects/CONSERVED_FUNCTION_RECOVERY/f_type_atp_synthase/node_placement.tsv, PTN008558586 is a DUPLICATION node whose
  children are PTN000390097 (FliI/SctN clade: SF9, SF62, SF81) and PTN008558588 (F1-beta clade).
  All seeds (E. coli AtpD P0ABB4, human ATP5F1B, yeast ATP2, S. pombe atp2, etc.) are in the F1-beta
  branch. The IBD therefore sits one node too deep: above the duplication that created the
  export-ATPase paralog. P26465 (SF81) inherits it only via the paralog branch, which has no Fo
  partner and a demonstrably different function (inhibitor-insensitive, export-coupled ATPase).
  -> REMOVE both. No IRD/NOT exists at PTN000390097 in the cached PAINT table.
- GO:0015986 IEA GO_REF:0000108 inferred from GO:0046933 -> REMOVE.
- No InterPro2GO IPR013380/IPR004100 rows on this entry.

## Decisions summary
- ACCEPT: ATP binding, ATP hydrolysis activity, cytoplasm, T3SS protein secretion, T3SS complex,
  flagellum assembly, identical protein binding (hexamer).
- KEEP_AS_NON_CORE: flagellum-dependent motility (downstream of assembly).
- REMOVE: 2x protein binding (FliT, FliJ; uninformative), GO:0046933, GO:0045259, GO:0015986.
- NEW: GO:0008564 protein-exporting ATPase activity; GO:0120102 bacterial-type flagellum secretion
  apparatus.


## 2026-11-06 comparative flagellar audit

All 15 inherited rows, including NEW GO0008564 and GO0120102, and the genuine Falcon report remain payload-frozen. Broad ATPase and complex claims are refined rather than retained merely as redundant. The description separates native PMF-supported export, mutant bypass and 2018 IMV reconstitution (PMID29946050). Catalytic mutations differ in phenotype; the unqualified assertion that all catalytic mutations abolish flagellation was removed. SJW versus LT2 backgrounds remain explicit: reference-protein identity does not make every Salmonella assay a native LT2 measurement.

Existing genuine Falcon report retained without refresh.

All original annotation payloads, including any inherited NEW proposals, are preserved. Only reviewer-authored judgments and synthesis were updated. Identity bridges and construct limits are recorded under analysis/module_audits/bacterial_flagellar_assembly_export/comparative-panel/.


## 2026-11-06 PR6138 round-1 clarification

Accepted the independently supported ATP-hydrolysis and type III secretion-complex rows alongside the export activity and flagellar location. Current GO lacks the formerly implied hierarchy links; absence of an edge does not mean the export reaction lacks ATP hydrolysis. PMID8943245 directly measures Salmonella ATPase activity, and PMID29946050 reconstitutes ATP-dependent export. No original annotation payload or inherited NEW action changed.

Ontology definitions and ancestor URLs, primary-source scope and reviewer disagreements are recorded in `analysis/module_audits/bacterial_flagellar_assembly_export/round1-consultation.md`.
