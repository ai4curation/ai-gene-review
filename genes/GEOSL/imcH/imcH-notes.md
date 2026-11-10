# ImcH (Q747K6, GSU3259) — curation notes

Geobacter sulfurreducens PCA inner-membrane multiheme c-type cytochrome, Swiss-Prot
(IMCH_GEOSL), 507 aa, NapC/NirT/NrfH superfamily, three predicted transmembrane
helices and seven CXXCH/CXXXCH heme-c motifs (sequence scan of the cached UniProt
entry gives motifs at residues 132, 157, 206, 312, 429, 449, 487).

## Discovery and genetics (Levar et al. 2014, PMID:25425235)

Transposon mutagenesis for loss of Fe(III)-citrate reduction hit GSU3259 eighteen
times [PMID:25425235 "In a modified transposon mutagenesis protocol (21), 18
independent mutants containing insertions in the locus GSU3259 which were unable to
grow with soluble Fe(III) citrate as the electron acceptor were found"]. Domain
content and family assignment [PMID:25425235 "a region of NapC/NirT homology, and up
to 7 c-type heme binding motifs"].

Localization is experimental, from a chromosomally His-tagged allele fractionated on
a sucrose gradient with succinate dehydrogenase as the inner-membrane marker
[PMID:25425235 "ImcH was detected only in fractions with SDH activity."]. This is the
basis of the EXP `GO:0005886 plasma membrane` row (bacterial plasma membrane = inner
membrane), and it agrees with the Swiss-Prot `SUBCELLULAR LOCATION: Cell inner
membrane` statement that the IEA row maps from.

Phenotype is potential-dependent rather than acceptor-class-dependent: the deletion
cannot reduce Fe(III) citrate, Fe(III)-EDTA or Mn(IV) birnessite (all > +0.1 V vs
SHE) but still reduces ferrihydrite and goethite [PMID:25425235 "ΔimcH::Kanr cells
also could not reduce laboratory-synthesized Mn(IV) oxides (birnessite)"]; growth on
fumarate is unaffected [PMID:25425235 "growth with fumarate as the electron acceptor
was unaffected"], so the lesion is specific to extracellular respiration and not a
general respiratory or assembly defect. Poised electrodes separate the variable
cleanly: no growth at +0.24, +0.1 or 0 V, growth at -0.1 V. The authors' model has
ImcH as the high-potential exit from the quinone pool [PMID:25425235 "cells typically
route electron flux out of the quinone pool via an ImcH-dependent pathway for
reduction of high-potential acceptors"].

## Mineral-by-mineral confirmation (Levar et al. 2017, PMID:28045456)

Across 17 XRD-characterized mineral preparations, ΔimcH fails on freshly precipitated
(higher-potential) phases and recovers as the phases age or Fe(II) accumulates
[PMID:28045456 "ΔimcH cultures lacking the high-potential pathway demonstrated a
substantial lag, remaining near background for 7 days"]. Growth yield is higher when only the
ImcH pathway operates [PMID:28045456 "the yield of cells forced to use only the ImcH pathway was 170% of
the wild-type using both pathways during complete reduction of Fe(III)."]. The same paper is explicit that the quinone-pool step was, at that date,
inferred rather than shown [PMID:28045456 "although it is important to note that
direct roles for ImcH and CbcL in the movement of electrons out of the quinone pool
have not been demonstrated"]. That caveat is what the 2023 biochemistry addresses.

## Biochemistry of the purified protein (Pimenta et al. 2023, PMID:37779214)

Recombinant ImcH produced in *S. oneidensis* and purified: seven c-type hemes by
iron quantification, no signal-peptide cleavage, monomer/dimer equilibrium. Menadiol
(a soluble menaquinone analogue) reduces the protein, though only partially
(~2 of 7 hemes), as also seen for CymA. Hemes titrate low, from -150 to -358 mV.
Surface plasmon resonance and 1D 1H NMR identify the periplasmic triheme PpcA as the
preferred partner (K_D ≈ 2.7 µM), and cyclic voltammetry shows continuous electron
transfer from electrode-bound ImcH to PpcA in solution. Proton release is to the same
side as the electrons, i.e. the protein is electroneutral. Together these give both
half-reactions of a menaquinol:cytochrome c oxidoreductase in vitro, which is why
this review adds `GO:0008121 quinol-cytochrome-c reductase activity` as a NEW row —
with the caveat (recorded in the row's `reason`) that no single-turnover
quinol-oxidation/PpcA-reduction assay has been reported, and that the in vivo
quinone-pool step still rests on genetics plus the structural quinone site.

## Pathway context (CbcL, CbcBA)

ImcH is one of at least three inner-membrane routes out of the menaquinol pool, used
in distinct potential windows: CbcL below about -0.1 V (PMID:26407054) and CbcBA near
-0.21 V (PMID:34423503). The windows matter for the annotation: ImcH is not *the*
Geobacter quinol dehydrogenase, it is the high-potential one, and no GO term captures
that conditionality.

## GO annotation calls

- Two `GO:0005886` rows (EXP and IEA/SubCell): both ACCEPT. The EXP row is a direct
  fractionation result; the IEA row maps the curated `Cell inner membrane` statement
  and agrees with it. GO has no bacterial "inner membrane" term distinct from plasma
  membrane, so no MODIFY is available.
- `GO:0009055 electron transfer activity` (IBA, node PANTHER:PTN001251186, seeded by
  TorC and TorY of *E. coli* and CymA of *S. oneidensis*): TOO_GENERAL (was ACCEPT; see
  the correction note below). The node sits
  at taxon:2 (Bacteria) in the PAINT file; ImcH is a NapC/NirT/NrfH member by UniProt
  SIMILARITY, by PROSITE MULTIHEME_CYTC and by the published structural comparison
  with NrfH, so it is inside the clade, and it has direct electron-transfer evidence
  of its own. The node placement is sound; the term is simply entailed by the
  `GO:0008121` row asserted below, which is its direct `is_a` child.
- `GO:0019645 anaerobic electron transport chain` (IBA, same node, seeded by TorC and
  TorY): ACCEPT, core. ImcH itself performs a step of the chain (it carries the
  electrons), not merely enabling one.
- NEW `GO:0020037 heme binding` (IDA): seven covalently bound c-hemes measured on the
  purified protein; no GOA row covers the cofactor.
- NEW `GO:0008121 quinol-cytochrome-c reductase activity` (IDA): see the caveat above.

Rejected NEW candidates: a metal-reductase term (ImcH does not contact the metal —
the periplasmic and outer-surface cytochromes do, and the metal phenotype is
necessity, not participation in the terminal reduction); `GO:0009061 anaerobic
respiration` (ancestor-level relative to GO:0019645 already asserted); a
response-to-redox-potential term (the sensing/regulatory entity is unidentified, and
imcH is constitutively expressed, so ImcH is the switched-past component rather than
the sensor); `GO:0048038 quinone binding` — the quinone site is real to the extent the
evidence goes, but the evidence is a structural model superposed on NrfH plus the
conserved protonatable residues around heme 1, not a bound-ligand structure or a binding
measurement, and menadiol reduction of the protein shows reduction occurs without
localising the site [PMID:37779214 "Based on the ImcH model, it seems that these two
proteins have similar menaquinone‐binding sites, close to heme 1, immediately following
the transmembrane domain, and with an unusual coordination."]. Model-only evidence makes
`NEW` the wrong call; the pocket-mutagenesis entry in `suggested_experiments` is where
the question belongs, and the site itself is cited in the `GO:0008121` row as part of the
topology argument rather than as an annotation of its own. `GO:0005887 integral component
of plasma membrane` was likewise declined, for the reasons recorded in the `GO:0005886`
IEA row.

## Correction note (review feedback, PR #5640)

Two errors found in review and corrected: (i) the `GO:0008121` row had claimed the term
is "not an ancestor or descendant" of the `GO:0009055` row — it is in fact a direct
`is_a` child of it (verified against the QuickGO is_a ancestor closure of GO:0008121,
which contains GO:0009055, GO:0015078, GO:0015399, GO:0015453, GO:0016491, GO:0016679 and
GO:0022857), so the `GO:0009055` IBA row is now `TOO_GENERAL` and the two core functions
are collapsed into one; (ii) `GO:0008121` is also `is_a GO:0015078 proton transmembrane
transporter activity`, which asserts the proton translocation PMID:37779214 refutes for
ImcH. The term is kept, since it is the only one naming both the quinol donor and the
cytochrome c acceptor and `GO:0016681` is obsolete, with the mismatch recorded in the
row's `reason`, in `suggested_questions` and as a `proposed_new_terms` entry for an
electroneutral menaquinol:cytochrome c oxidoreductase activity under `GO:0016679`. This
is the same resolution reached for the family member CymA in the parallel SHEON/cymA
review.

## Note on the CMMMech grounding

CMMMech records (`asbolane`, `akaganeite`, `feitknechtite`, `pyrochroite`,
`rhodium`, `chromite-ore-processing-residue`) cite Q747K6 as a representative protein
example with `functional_role` phrasings such as "required for extracellular electron
transfer to high-redox-potential Fe(III)/Mn(IV) acceptors". For Fe(III) chelates,
Mn(IV) birnessite and high-potential electrodes that is supported by the deletion
phenotypes above. Two qualifications are worth recording:

- The akaganeite record's `supports: support` claim is the only one anchored to an
  experiment that actually manipulated *imcH* (Levar et al. 2017, akaganeite at
  pH 6.8/6.3). The `rhodium` and `chromite-ore-processing-residue` entries correctly
  flag `supports: partial` with the explanation that individual cytochrome genes were
  not mutated; there is no published evidence that ImcH is involved in Rh(III)
  reduction, and its role there is an extrapolation from redox potential alone.
- "Required for extracellular electron transfer to ... acceptors" is right only inside
  the high-potential window; the same strains reduce low-potential Fe(III) oxides
  without ImcH via CbcL/CbcBA. A reader of the record alone could take ImcH to be
  required for Geobacter metal reduction generally, which the primary literature
  contradicts. No CMMMech file was edited as part of this review.
