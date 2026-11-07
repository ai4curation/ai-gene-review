# MTH_1557 (O27599) notes

Methanothermobacter thermautotrophicus Delta H, tungsten formylmethanofuran dehydrogenase
subunit A (FwdA). Unreviewed TrEMBL entry, no gene symbol; locus name used as symbol.

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no deep-research file exists. Searches: web
search ("Wagner Ermler Shima 2016 formylmethanofuran dehydrogenase tungsten structure";
"Hochheimer Thauer tungsten formylmethanofuran dehydrogenase operon"; "FwdA binuclear zinc
amidohydrolase") and PubMed E-utilities ("formylmethanofuran dehydrogenase AND tungsten",
21 hits; titles screened). Cached with `just fetch-pmid`:

- PMID:27846502 Wagner, Ermler, Shima 2016 Science. Crystal structure of the W enzyme
  Fwd(ABCDFG) from *Methanothermobacter wolfeii* (not Delta H). Abstract only.
- PMID:30120799 Niks & Hille 2019 review of Mo/W formate and formylmethanofuran
  dehydrogenases. Full text.
- PMID:8575452 Hochheimer et al. 1995. Sequences of fwdABCD from "Methanobacterium
  thermoautotrophicum" (strain not named in the abstract; the Marburg group's biochemistry
  used strain Marburg, now *M. marburgensis*). Abstract only.
- PMID:8954165 Hochheimer et al. 1996. fmdECB operon; FmdA = FwdA. Abstract only.
- PMID:9818358 Hochheimer et al. 1998. fwdHFGDACB and fmdECB operons in M. wolfei and M.
  thermoautotrophicum; fwd constitutive, fmd induced by molybdate. Abstract only.
- PMID:8161283 Bertram et al. 1994. W isoenzyme purified from strain Marburg. Abstract only.
- PMID:8147868 Wasserfallen 1994. Fmd from strain Marburg, cytosolic, forward reaction
  shown. Abstract only.
- PMID:8125106 Bertram et al. 1994. Substrate specificity and EPR of Fmd/Fwd isoenzymes
  (M. barkeri, M. thermoautotrophicum, M. wolfei). Abstract only.

No study of the Delta H Fwd protein itself was found; all biochemistry is on strain
Marburg (*M. marburgensis*) or *M. wolfeii*. The Delta H locus order MTH_1553-1559 matches
fwdHFGDACB, with MTH_1557 at the fwdA position.

## Two active sites, two half reactions

- [PMID:27846502 "Catalysis is separately performed by subunits FwdBD (FwdB and FwdD), which are related to tungsten-containing formate dehydrogenase, and subunit FwdA, a binuclear metal center carrying amidohydrolase."]
- [PMID:27846502 "CO2 is first reduced to formate in FwdBD, which then diffuses through a 43-angstrom-long tunnel to FwdA, where it condenses with methanofuran to formyl-methanofuran."]
- Review confirms the old carbamate model is superseded: [PMID:30120799 "the binding site for methanofuran was some 40 Å removed from the tungsten center, with the two sites connected via a hydrophobic tunnel through which formate, once generated from CO 2 at the tungsten center, diffused to the methanofuran binding site where it was incorporated into product."]

So FwdA performs the C-N bond forming half reaction, formate + methanofuran =
N-formylmethanofuran + H2O. Written in the hydrolytic direction this is
RHEA:24686 (N-formylmethanofuran + H2O = methanofuran + formate; no EC number). GO has no
term for it; the nearest existing term is GO:0016811 (hydrolase activity, acting on
carbon-nitrogen (but not peptide) bonds, in linear amides). Formylmethanofuran is an
N-substituted formamide, a linear amide. A term is proposed. FwdA neither binds the
tungsten-pterin nor reduces CO2, so on FwdA the overall EC 1.2.7.12 activity is
contributes_to (pattern 16).

## Metal site (bioinformatics)

- Wagner abstract says "binuclear metal center" but does not name the metal. PDB 5T5I
  (the structure deposited with that paper) has two ZN per FwdA chain. Mapping in
  file:METTH/MTH_1557/MTH_1557-bioinformatics/RESULTS.md: M. wolfeii FwdA vs O27599 are
  95.3% identical end to end; the Zn ligands His57, His59, carboxylysine KCX178, His231,
  His271 and Asp385 are all conserved in O27599 at the same positions.
- This is a protein-bound metal site (not a cofactor-held metal as in pattern 17), so zinc
  ion binding is a genuine MF; added as NEW (ISS-type inference from the ortholog
  structure). The crystal metal is Zn; in vivo metal identity was not tested in Delta H.

## Shared subunit of the Mo isoenzyme

- [PMID:8954165 "It is therefore proposed that FmdA and FwdA are encoded by the same gene namely fwdA in the fwd operon."] and the fmd operon lacks fmdA. Review: [PMID:30120799 "The implication is that subunits encoded by the constitutively expressed fwd operon are incorporated into the mature Mo‐containing enzyme under the conditions in which the latter is expressed."]
- So FwdA (MTH_1557) is likely part of both Fwd (GO:0044675) and Fmd (GO:0044676). Only the
  Fwd complex membership is added as NEW; Fmd membership is a proposal (strain not stated
  in the abstract) and raised as a question.
- GO:0044675 definition ("four polypeptides") is outdated: the structure is FwdABCDFG.

## Location

- [PMID:8147868 "Formylmethanofuran dehydrogenase was purified 30-fold from the cytosolic fraction of cell extract of Methanobacterium thermoautotrophicum (Marburg)"] (Mo/W mixture, strain Marburg). The enzyme is a soluble crystallised complex, FwdA has no TM segment. Cytoplasm added (IC), consistent with frhA/mcrA.

## GOA rows

- GO:0016787 hydrolase activity (ARBA) and GO:0016810 hydrolase activity, C-N non-peptide
  (InterPro2GO IPR011059, composite domain of metallo-dependent hydrolases): both true but
  general. FwdA's reaction is a linear-amide C-N bond (formyl amide), so MODIFY both to
  GO:0016811, with the specific reaction proposed as a new term.

## PANTHER

- PTHR11647 (HYDRANTOINASE/DIHYDROPYRIMIDINASE FAMILY MEMBER), subfamily PTHR11647:SF1
  (COLLAPSIN RESPONSE MEDIATOR PROTEIN). The subfamily name is from the eukaryotic CRMP
  (pseudo-amidohydrolase) members; FwdA sits there by fold only. No GOA rows derive from it.
