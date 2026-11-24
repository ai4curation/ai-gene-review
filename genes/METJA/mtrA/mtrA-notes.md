# mtrA (MJ0851, Q58261) notes

Methanocaldococcus jannaschii, tetrahydromethanopterin S-methyltransferase subunit A.
Round 5 of the ARCHAEA project.

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no `-deep-research-*.md` file was made.
Searches (WebSearch): "Wagner 2022 tetrahydromethanopterin methyltransferase MtrA cobamide
structure sodium pump"; "cryo-EM structure MtrA-H complex ... sodium pump"; "Gottschalk Thauer
... MtrA corrinoid"; "Hippler Thauer 1999 MtrH"; "Harms Thauer corrinoid-containing 23-kDa subunit
MtrA". There is no 2022 Wagner Mtr cryo-EM paper; the relevant structural papers are Wagner et al.
2016 (MtrA crystal structures, including M. jannaschii MtrA) and Aziz et al. 2024 (cryo-EM of the
Mtr complex). Cached and read: PMID:27324530 (full text), PMID:38530900 (full text),
PMID:11248186, PMID:10338124, PMID:8898900 (abstracts only).

No paper characterises the native M. jannaschii Mtr complex biochemically. The only experimental
work on this protein is the in vitro reconstitution and crystal structure of its soluble domain
(PMID:27324530).

## Biology

- Mtr is an eight-subunit membrane complex, MtrA-H, that couples methyl transfer from
  methyl-H4MPT to CoM with Na+ translocation [PMID:11248186 "catalyzed by a Na(+)-translocating
  membrane-associated multienzyme complex composed of eight different subunits"].
- MtrA carries the corrinoid prosthetic group that is methylated and demethylated; MtrH catalyses
  the first half-reaction [PMID:10338124 "The 23 kDa subunit MtrA harbors a corrinoid prosthetic
  group which is methylated and demethylated in the catalytic cycle. We report here that the 34 kDa
  subunit MtrH catalyzes the methylation reaction."; "shown to exhibit
  methyltetrahydromethanopterin:cob(I)alamin methyltransferase activity"].
- Demethylation of MtrA (methyl to CoM) is the Na+-dependent step [PMID:11248186 "demethylation
  being sodium ion-dependent"].
- Cobalt ligation: a His of MtrA coordinates Co(II) in the base-off/His-on form [PMID:8898900 "the
  Co(II) of the prosthetic group is coordinated by a histidine residue of the apoprotein"]. In the
  structure this is His84 [PMID:27324530 "In MtrA, His84 pointing from a protrusion of loop β3-α3
  towards the corrinoid ring, was coordinated to Co(III) via NE2"].
- Native cofactor in M. jannaschii is 5-hydroxybenzimidazolyl cobamide (factor III), not cobalamin
  [PMID:27324530 "including M. jannaschii and M. fervidus, contain 5-hydroxybenzimidazolyl cobamide
  (factor III) rather than 5-dimethylbenzimidazolyl cobamide (cobalamin)"]. The refolded M.
  jannaschii soluble domain binds cobalamin about 1:1 [PMID:27324530 "The only MtrA protein with an
  approximately 1:1 cobalamin:protein ratio was the soluble domain of the membrane-associated MtrA
  from M. jannaschii"], although the crystallised proteolytic fragment was cofactor-free ("colourless
  cobalamin-free crystals"; PDB 5L8X).
- Topology: one C-terminal TM anchor helix; MtrC, MtrD, MtrE are the polytopic subunits
  [PMID:27324530 "MtrC, MtrD and MtrE as integral membrane proteins with at least six transmembrane
  helices, MtrA, MtrB, MtrF and MtrG as peripheral proteins with one transmembrane helix anchor"].
  In the cryo-EM structure MtrA's C-terminal helix is part of the Mtr(ABFG)3 stalk and the soluble
  B12 domain is mobile [PMID:38530900 "For MtrA, only the C-terminal anchor helix MtrAc (178:238) was
  visible but not the soluble MtrA domain (MtrAs) carrying the B12 derivative."].
- Na+ binding site and pore are in MtrCDE (MtrE) [PMID:38530900 "Putative coenzyme M and Na+ were
  identified inside or in a side-pocket of a cytoplasmic cavity formed within MtrCDE."]. MtrA is
  proposed to drive the pump conformationally: methyl-cob(III)amide-MtrA binding induces the
  inward-facing state, cob(I)amide-MtrA the outward-facing state [PMID:38530900 "Hypothetically,
  strongly attached methyl-cob(III)amide (His-on) carrying MtrA induces an inward-facing
  conformation"]. MtrA is the energy-coupling element of the pump, not the ion path.

## Annotation judgements

- GO:0030269 (enables, IEA): whole-complex reaction (methyl transfer plus 2 Na+ translocation).
  Pattern 16. MtrA contributes (cobamide methyl carrier, intermediate of both half-reactions) but
  neither half-reaction is catalysed by MtrA alone (MtrH does the first). MARK_AS_OVER_ANNOTATED;
  contributes_to in core_functions. Same treatment as METS5 Msed_1375 / Msed_0148 (BCCP cofactor
  carrier).
- GO:0050897 cobalt ion binding (InterPro2GO IPR005778): the cobalt is the corrin cobalt, bound via
  His84 as part of binding the cobamide. Same argument as METAC mcrA (F430 nickel -> tetrapyrrole
  binding). Here a specific child exists: GO:0031419 cobalamin binding (is_a tetrapyrrole binding).
  Native cofactor is factor III, not cobalamin sensu stricto; GO:0031419's definition ("a corrin
  nucleus containing a cobalt atom") fits, and the protein binds cobalamin in vitro. MODIFY to
  GO:0031419. Question for GO: broaden to cobamide binding.
- GO:0006814 sodium ion transport (InterPro2GO) -> MODIFY to GO:0035725 (already carried).
- GO:0035725 (inter-ontology from GO:0030269): MtrA does work in the pump (energy-coupling
  conformational driver), like the nucleotide-binding subunit of an ABC transporter, but the
  mechanism is a hypothesis. KEEP_AS_NON_CORE.
- GO:0019386 methanogenesis from CO2: M. jannaschii is a hydrogenotrophic CO2-reducing methanogen.
  ACCEPT.
- GO:0006730 one-carbon metabolic process: not an ancestor of GO:0019386 in GO, so TOO_GENERAL
  does not apply; the reaction is literally a C1 transfer between C1 carriers. First ACCEPT (as for
  MOOTH acsD); revised to KEEP_AS_NON_CORE in the PR #6211 review, to match the other C1-carrier
  enzymes of the pathway (Ftr, Mtd, Hmd, Mer, MtrH), since the term is broad and the core process is
  GO:0019386.
- GO:0005886 plasma membrane: single C-terminal TM anchor, stalk helix in cryo-EM. ACCEPT.
- NEW: GO:0044677 methyl-tetrahydromethanopterin:coenzyme M methyltransferase complex (part_of),
  ISS from HAMAP subunit statement and the ortholog structure.

## Possible new pattern

InterPro2GO maps a cobamide-binding family signature (IPR005778 MtrA) to "cobalt ion binding"
(GO:0050897): the metal of a tetrapyrrole cofactor annotated as a free metal ion. This is the
corrinoid version of the F430 nickel case seen in mcrA (keyword KW-0479 -> metal ion binding).
