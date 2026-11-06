# Msed_2055 (A4YIE3) notes — methylmalonyl-CoA mutase, B12-binding (beta, small) subunit

Automated deep research was unavailable for this gene, so there is no
`*-deep-research-*.md` file. The literature below was found manually (Europe PMC
search for "Msed_2055" and for Metallosphaera + methylmalonyl-CoA mutase, 2026-11-01).
Cited PMIDs are cached in `publications/`. Conventions follow the sibling review
`genes/METS5/Msed_0638/` (catalytic alpha subunit).

## Identity and sequence

- UniProt A4YIE3 (TrEMBL, unreviewed), 155 aa, "Cobalamin B12-binding domain protein".
  PROSITE PS51332 B12-binding domain at residues 20-148; InterPro IPR006158
  (Cobalamin-bd), IPR036724 (Cobalamin-bd_sf), IPR006159 (Acid_CoA_mut_C); NCBIfam
  TIGR00640 (acid_CoA_mut_C); CDD cd02071 (MM_CoA_mut_B12_BD); PANTHER PTHR48101:SF3.
  ARBA cofactor annotation adenosylcobalamin
  [file:METS5/Msed_2055/Msed_2055-uniprot.txt "Name=adenosylcob(III)alamin; Xref=ChEBI:CHEBI:18408;"].
- The protein is only the Rossmann-type B12-binding domain, the domain that sits at the
  C-terminus of canonical bacterial and human MCM alpha chains. It has no TIM-barrel
  substrate-binding domain; that is in the separately encoded Msed_0638.
- Motif scan (`Msed_2055-bioinformatics/RESULTS.md`): DXHXXG at D31-G36 (DGHDRG),
  SIL at 78 and GG at 108, matching the reported DXHXXG-SXL-GG motif. His33 is the
  candidate lower axial cobalt ligand.

## Literature

- Ramos-Vera et al. 2011 made the genomic assignment:
  [PMID:21169482 "M. sedula as well as the other autotrophic members of the Sulfolobales clearly encode MCMs in their genome (e.g., small subunit Msed_2055 and large subunit Msed_0638)."]
  and noted the overlapping MeaB/ArgK-like gene:
  [PMID:21169482 "Msed_2056 (ArgK-like) overlaps with the ORF encoding the small MCM subunit (cobalamin B12-binding domain protein Msed_2055), indicating the potential for cotranscription"].
  Their general statement that in bacterial MCMs "the small subunit binds the substrate
  and the cofactor" does not fit M. sedula, where the substrate-binding barrel is on the
  large subunit (see Msed_0638 notes).
- Han et al. 2012 (abstract-only in cache) is the primary biochemical paper:
  [PMID:22752162 "the gene for the coenzyme B(12)-binding subunit of MCM (MCM-β) is located remotely (Msed_2055)"];
  [PMID:22752162 "The expression of all three genes was significantly upregulated under autotrophic compared to heterotrophic growth conditions, implying a role in CO(2) fixation."];
  [PMID:22752162 "soluble, active MCM was produced only if MCM-α and MCM-β were coexpressed"];
  [PMID:22752162 "MCM is a heterotetramer (α(2)β(2))"];
  [PMID:22752162 "The conserved coenzyme B(12)-binding motif (DXHXXG-SXL-GG) was identified in M. sedula MCM-β."].
  No direct cobalamin-binding measurement on isolated MCM-beta is stated in the abstract.
- Cracan and Banerjee 2012 (full text) review the acyl-CoA mutase family and place the
  M. sedula enzyme among split-subunit mutases:
  [PMID:22803641 "A variant arrangement has been reported for MCM from Metallosphaera sedula that exhibits a split organization (Fig. 2) with one subunit being homologous to the substrate-binding domain and the second, to the AdoCbl-binding domain in the α-subunit of the canonical MCM"];
  the same split is seen in isobutyryl-CoA mutase
  [PMID:22803641 "subunit B (IcmB and HcmB, respectively) binds AdoCbl"];
  and the cobalt ligation mode
  [PMID:22803641 "Cobalamin is bound to all these enzymes in the “base-off/His-on” conformation, in which the side chain of the histidine in a conserved DXHXXG motif, serves as the axial ligand to cobalt"].
- Berg et al. 2007 [PMID:18079405] defined the 3HP/4HB cycle (abstract-only; does not
  mention MCM). Loder et al. 2016 [PMID:27771364] model the cycle using Han 2012 data;
  not cited here as it adds nothing specific to Msed_2055.
- Leyn et al. 2015 (PMID:25939834, regulons of autotrophic cycle genes) was cached but is
  abstract-only and the abstract does not name Msed_2055; not cited.

## Annotation reasoning

- GO:0031419 cobalamin binding (IEA, InterPro): ACCEPT, core. This is the subunit's own
  activity: the domain, the His-on motif and the paper's own naming ("coenzyme
  B12-binding subunit") all point to it. Inferred, not measured on the isolated subunit.
- GO:0016853 isomerase activity (IEA, IPR006159): a whole-complex catalytic term on a
  cofactor-binding subunit (ARCHAEA pattern 16; cf. pattern 8 proteasome alpha). The
  mutase is an isomerase, and the subunit does do part of the work (it holds the
  AdoCbl whose Co-C homolysis starts the radical rearrangement, and supplies the axial
  His), but it does not catalyse alone. MODIFY to GO:0004494 methylmalonyl-CoA mutase
  activity, to be carried as contributes_to (core_functions), on the experimental
  ground that activity needs both subunits [PMID:22752162].
- GO:0046872 metal ion binding: His33 coordinates the cobalt of cobalamin, so the term is
  not false, but the metal is bound only as part of the cofactor and cobalamin binding
  is the informative statement. KEEP_AS_NON_CORE, as in the human MTR review (the human
  MMUT review accepted it).
- NEW GO:0015977 carbon fixation (IDA, PMID:22752162), as for Msed_0638. Participation
  test: the subunit supplies the cofactor-binding domain the catalytic step depends on
  (the "cofactor" shape). Comparator: Msed_0638 and the other cycle enzymes carry the
  same term in their reviews. GO:0043427 (Chloroflexus cycle) is not used; the proposed
  term "carbon fixation by 3-hydroxypropionate/4-hydroxybutyrate cycle" (Msed_0709) is
  reused.

## Module

- `modules/hydroxypropionate_hydroxybutyrate_cycle.yaml` mcm annoton already models the
  alpha2beta2 complex with Msed_2055 (A4YIE3) as mcm_small, function GO:0031419, and the
  complex function GO:0004494. This agrees with the review; no change needed.
