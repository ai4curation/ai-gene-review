# MTH_1559 (O27601) notes

Methanothermobacter thermautotrophicus Delta H, formylmethanofuran dehydrogenase subunit B
(FwdB) of the tungsten isoenzyme Fwd. Unreviewed TrEMBL entry (PIRNR-based name and EC),
no gene symbol; locus name used as symbol.

## Literature search (2026-11-07)

Deep-research providers were unavailable. Same search as for MTH_1557 (see
MTH_1557-notes.md): web search for the Wagner 2016 structure and the Hochheimer/Thauer
operon papers, and PubMed E-utilities "formylmethanofuran dehydrogenase AND tungsten" (21
hits screened). Cached and read: PMID:27846502, PMID:30120799, PMID:8575452,
PMID:8954165, PMID:9818358, PMID:8161283, PMID:8147868, PMID:8125106. All except
PMID:30120799 are abstract only. No study of the Delta H protein itself was found; the
biochemistry is on strain Marburg (now *M. marburgensis*) and *M. wolfeii*.

## CO2-reducing half: FwdB(D) is a W-formate dehydrogenase module

- [PMID:27846502 "Catalysis is separately performed by subunits FwdBD (FwdB and FwdD), which are related to tungsten-containing formate dehydrogenase, and subunit FwdA, a binuclear metal center carrying amidohydrolase."]
- [PMID:27846502 "CO2 is first reduced to formate in FwdBD, which then diffuses through a 43-angstrom-long tunnel to FwdA, where it condenses with methanofuran to formyl-methanofuran."]
- FwdD is the "cap" domain, separate from FwdB: [PMID:30120799 "The most important variation in these structures is that the contiguous C‐terminal “cap” domain (in blue ) found in the first three proteins exists as a separate FwdD subunit in the T. wolfeii enzyme."]
- Sequence motifs: [PMID:8575452 "FwdB was found to contain sequence motifs characteristic for molybdopterin-dinucleotide-containing enzymes indicating that this subunit harbors the active site."]
- Fmd counterpart: [PMID:8954165 "The fmdB gene was found to encode the molybdopterin-dinucleotide-binding subunit harboring the enzyme's active site; FmdB is thus functionally equivalent to FwdB."] (Mo isoenzyme FmdB is a separate gene, MTH_917-919 cluster; not this entry.)

So FwdB enables the formate dehydrogenase-type reaction (CO2 + 2e- + 2H+ = formate) and
contributes_to the overall EC 1.2.7.12 activity (pattern 16), which needs FwdA. GO has only
acceptor-specific formate dehydrogenase terms (NAD+, NADP+, F420, quinone, cytochrome);
none fits a tungsten enzyme fed by a [4Fe-4S] relay (ultimately reduced ferredoxin). A
generic "formate dehydrogenase activity" term is proposed.

## Metal / cofactor (pattern 17)

- Tungsten is held by a pterin cofactor, not as a free ion: [PMID:8161283 "to contain per mol 0.4 mol tungsten, < 0.05 mol molybdenum, 8 mol non-heme iron, 8 mol acid-labile sulfur and molybdopterin guanine dinucleotide."] (W isoenzyme, strain Marburg).
- Review: [PMID:30120799 "the metal coordinated to two equivalents of a pyranopterin‐containing cofactor that chelates the metal via an enedithiolate side chain."] and [PMID:30120799 "both Mo‐ and W‐containing enzymes have cysteine coordinated to the metal."]
- Bioinformatics (file:METTH/MTH_1559/MTH_1559-bioinformatics/RESULTS.md): M. wolfeii FwdB
  (5T5I chain B) 97.9% identical to O27601; W ligand Cys118 maps to Cys123 of O27601; the
  single [4Fe-4S] cluster ligands Cys9/12/16/35 map to Cys14/17/21/40.
- Correct GO term for the W-bis(pterin) is GO:0043546 molybdopterin cofactor binding,
  whose definition covers tungsten (W-molybdopterin). Not "tungstate binding" (GO:1901359,
  free anion) and not a metal ion binding term. Added NEW. Also NEW GO:0051539 4Fe-4S
  cluster binding (one cluster in FwdB).

## Selenocysteine keyword is wrong for this entry

- UniProt KW "Selenocysteine {ECO:0000256|PIRNR:PIRNR005646}". The O27601 sequence has no U,
  and the W ligand is Cys123 (Cys118 in M. wolfeii). The review states the Fwd/Fmd enzymes
  use Cys. The PIRNR rule should not add the keyword to Cys-type FwdB members. Recorded as
  a UNIPROT source defect on the UniRule row (same rule/PIRNR family).

## GOA rows

- GO:0003954 NADH dehydrogenase activity, GO:0016020 membrane, GO:0022904 respiratory
  electron transport chain: all three from TreeGrafter node PTN002875529 in PTHR43105
  (RESPIRATORY NITRATE REDUCTASE; subfamily SF14 FORMATE DEHYDROGENASE H). These are the
  terms of a membrane-bound respiratory NADH-oxidising complex; Fwd is a soluble
  cytoplasmic complex that uses no NAD(H) and builds no membrane gradient (pattern 14).
  The PTN node content itself was not inspected (PANTHER API not reached). REMOVE all three.
- GO:0015948 methanogenesis (InterPro2GO IPR016457): correct but general; MODIFY to GO:0019386,
  which the gene already carries.
- GO:0016491 oxidoreductase activity (IPR006656): correct but general; MODIFY to the
  proposed formate dehydrogenase term.
- GO:0018493 formylmethanofuran dehydrogenase activity, enables (UniRule): complex activity
  on a subunit (pattern 16); MARK_AS_OVER_ANNOTATED, core function contributes_to, UniProt
  WRONG_QUALIFIER defect (as for frhA).
- GO:0019386 (UniRule): ACCEPT.

## Rhea

- EC 1.2.7.12: RHEA:19841 (N-formylmethanofuran + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O =
  methanofuran + 2 reduced [2Fe-2S]-[ferredoxin] + CO2 + H(+)), from the Rhea REST API and
  the UniProt CATALYTIC ACTIVITY line.
