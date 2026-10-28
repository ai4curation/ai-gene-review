# SIL1 (Silaffin-1), *Cylindrotheca fusiformis* — review notes

UniProt: Q9SE35 (SIL1_CYLFU), Swiss-Prot, 265 aa precursor, PE:1 (evidence at
protein level). NCBITaxon:2853.

## Summary of what this protein is

SIL1 encodes the silaffin-1 **precursor**. It is not an enzyme in the usual
sense: it is a post-translationally hypermodified, highly repetitive polycationic
polypeptide that is proteolytically processed into a set of short peptides
(silaffin-1A1, -1A2, -1B) which precipitate silica from silicic acid solution
within seconds. The protein is a structural and templating component of the
diatom silica cell wall (frustule), not a catalyst with a measurable turnover
number.

Architecture from the UniProt record (Q9SE35 feature table):

- 1–19 signal peptide (ECO:0000255)
- 20–107 acidic propeptide (`PRO_0000032597`); UniProt explicitly flags that
  it is unknown whether this acidic N-terminal chain is functional or is merely
  a propeptide (`CC -!- DOMAIN`)
- 108–136 silaffin-1B (`PRO_0000032598`)
- 141–158 silaffin-1A2 (`PRO_0000032600`)
- 163–177, 182–196, 201–215, 220–234, 239–253 — five copies of silaffin-1A1
  (`PRO_0000032602`, `_604`, `_606`, `_608`, `_610`)
- seven atypical/canonical repeats R1–R7 over 108–257, with a declared
  `19 X 7 AA` consensus `S-S-K-K-S-G-S-Y-S-G-S-K-G-S-K-R-R-[IL]-L`
- cleavage occurs on pairs of basic residues (KW `Cleavage on pair of basic
  residues`), consistent with the RR/KR motifs flanking each repeat

So one *sil1* transcript yields **many** mineralization peptides from one
precursor — the repeats are the functional units, and the mature peptides share
the Q9SE35 accession. This is the POMC-style case the repo models with
`functional_isoforms` / `CLEAVAGE_PRODUCT` rather than separate gene folders.

## The silica-precipitating activity

The founding observation [PMID:10550045 "A set of polycationic peptides (called
silaffins) isolated from diatom cell walls were shown to generate networks of
silica nanospheres within seconds when added to a solution of silicic acid."].
The same paper establishes that the activity depends on the lysine modifications,
not on the peptide backbone alone [PMID:10550045 "The first lysine bears a
polyamine consisting of 6 to 11 repeats of the N-methyl-propylamine unit. The
second lysine was identified as epsilon-N,N-dimethyl-lysine. These modifications
drastically influence the silica-precipitating activity of silaffins."].

The chemical structure work assigns the activity specifically to the *sil1* gene
product [PMID:11349130 "Two silica-precipitating peptides, silaffin-1A(1) and-1A(2),
both encoded by the sil1 gene from the diatom Cylindrotheca fusiformis, were
extracted from cell walls and purified to homogeneity."] and confirms the in vitro
activity of the purified peptides [PMID:11349130 "In vitro, both peptides
precipitate silica nanospheres within seconds when added to a monosilicic acid
solution."]. Note the verbatim typographic quirk "and-1A(2)" in the cached
abstract — quoted as-is.

Native-state extraction showed the peptides are additionally and essentially
phosphorylated [PMID:12386330 "Each serine residue was phosphorylated, and this
high level of phosphorylation is essential for biological activity."], giving a
zwitterionic peptide that self-assembles [PMID:12386330 "The zwitterionic
structure of native silaffins enables the formation of supramolecular
assemblies."]. This matters for how the function should be described: the
active species is a **self-assembled polyanionic/polycationic aggregate**, and
the earlier HF-extracted ("natSil"/dephosphorylated) preparations were missing a
modification required for the native activity.

The mechanistic reading in the literature is templating/acceleration rather than
catalysis [PMID:11106386 "It is probably this structural element that
accelerates silicic acid polymerization and promotes production of nanosphere
networks."]. Note the hedge ("probably") — this is the authors' inference, not a
demonstrated mechanism.

## Localization

Silaffins are cell wall (biosilica) components, and are so tightly held that
they require HF dissolution of the wall to release [PMID:11106386 "The silaffins
are tightly associated with the biosilica so that they can only be solubilized
after dissolution of the cell wall in hydrogen fluoride (HF)."]. This is direct
evidence for a cell-wall / external encapsulating structure location.

In vivo, silica deposition happens in the **silica deposition vesicle (SDV)**, an
intracellular acidic compartment; UniProt's PTM note refers to it ("may also
control the silica colloid size within the silica deposition vesicle (SDV)").
GO has **no** term for the SDV (OLS search in `go` for "silica deposition
vesicle" returns zero classes), so the SDV cannot be annotated — see
`proposed_new_terms` in the review. I did not annotate an SDV location, because
the cited work demonstrates the mature location (biosilica/cell wall), not a
direct SDV localization experiment for this protein.

## GO annotation status — a genuine, total gap

**Q9SE35 has zero GO annotations.** `just fetch-gene CYLFU SIL1` produced a
`SIL1-goa.tsv` with a header row and no data, and a direct QuickGO query
(`.../annotation/search?geneProductId=Q9SE35`) returns `"numberOfHits":0`.
So this review has no existing annotations to adjudicate; its whole content is
`NEW` rows plus proposed terms. This is unusual, and worth stating plainly:
it is not that curators looked at silaffin-1 and declined to annotate it, it is
that a well-characterized Swiss-Prot entry with PE:1 and four primary papers has
never been annotated at all. There is no PANTHER family for it either
(`fetch-gene` reported "No PANTHER family found in UniProt data"), which is
consistent — silaffins are lineage-restricted and compositionally biased, so
they sit outside the usual family-propagation machinery.

### Ontology gaps that block a faithful annotation

Two terms that this protein needs do not exist, verified via OLS against `go`:

1. **No MF for silica polycondensation / biosilica nucleation.** The only
   silica-related MF in GO is `GO:0015115` silicate transmembrane transporter
   activity, which is a transporter and plainly wrong here. Searching `go` for
   "silica" returns only `GO:0034021` response to silicon dioxide and
   `GO:0071251` cellular response to silicon dioxide — both response terms, also
   wrong. Per CLAUDE.md, rather than forcing an ill-fitting id I left
   `molecular_function` unset on the core function and used
   `proposed_molecular_function` against a `proposed_new_terms` entry.
2. **No CC for the silica deposition vesicle**, as above.

A third, softer issue: `GO:0031214` biomineral tissue development is the obvious
"biomineralization" BP, but it is_a `GO:0009888` tissue development and its
ancestors run through multicellular-organism development. A unicellular diatom
has no tissue, so I did not use it. `GO:0042546` cell wall biogenesis is the
honest BP here. For the location I used `GO:0030312` external encapsulating
structure rather than `GO:0005618` cell wall, because `GO:0005618` carries an
explicit "Not to be used for manual annotation" instruction directing curators
to a lineage-specific child, and the children it lists (bacterial, plant-type,
fungal-type, S-layer) have no diatom option. The missing diatom child is
recorded as a proposed term.

## CMMMech cross-check (biosilica / silica precipitation)

CMMMech grounds Q9SE35 in `data/records/anatase.yaml`, in the
`inp_silaffin_templated_anatase_graph` causal graph, as node
`sil1_mineralization_peptide`. The source is Ping et al. 2016 (Chem. Sci. 7:6330–6336,
DOI 10.1039/C6SC02311H), an engineered *E. coli* surface-display construct: the
InaZ ice-nucleation anchor fused to the synthetic Sil-1 peptide
`SSKKSGSYSGSKGSKRRIL`, used to template amorphous titanium oxide from TALH,
which becomes anatase only after 600 °C calcination.

Two observations, recorded here rather than as `source_defects` (per the brief,
`source_defects` is for GOA/UniProt/InterPro, not for CMMMech's own fields):

1. **The CMMMech node description overstates the biology.** It describes the
   SIL1 node as "C-terminal silaffin peptide domain **catalyzing** titanium
   precursor condensation". Nothing in the silaffin literature supports
   *catalysis*, and the activity demonstrated for silaffin-1 is on **silicic
   acid → silica**, not on titanium. CMMMech's own `evidence` block is
   appropriately careful (`supports: partial`, non-engineered controls absent),
   and the record-level `functional_role` says "nucleates", which is better.
   The mismatch is confined to the node `description` field. UniProt's own
   `CC -!- FUNCTION` line unfortunately uses the same loose word ("Catalyzes the
   polymerization of silica spheres"), so CMMMech may simply have inherited it.
   I did not propagate "catalyzes" into this review.
2. **The grounded peptide is a repeat-consensus synthetic peptide, not the
   protein.** `SSKKSGSYSGSKGSKRRIL` is the R3–R7 consensus
   (`S-S-K-K-S-G-S-Y-S-G-S-K-G-S-K-R-R-[IL]-L`), chemically **synthesized** and
   therefore carrying **none** of the polyamine, methylation, hydroxylation or
   phosphorylation modifications that [PMID:10550045] and [PMID:12386330] show
   are required for the native silica-precipitating activity. The grounding to
   Q9SE35 is correct as a sequence provenance statement, which is all CMMMech's
   `annotation_note` claims. But any inference from the Ping et al. result back
   to the *in vivo* function of the diatom protein would be unsound in both
   directions: the construct is unmodified, heterologous, surface-displayed, and
   mineralizing a different element. Nothing from Ping et al. 2016 entered this
   review as evidence.

I did not edit CMMMech.

## Review decisions

No existing annotations, so no ACCEPT/MODIFY/REMOVE calls. Three `NEW` rows,
kept deliberately narrow:

- `GO:0030312` external encapsulating structure (CC, IDA, PMID:11106386) — the
  HF-requirement result is direct evidence of integration into the wall.
- `GO:0042546` cell wall biogenesis (BP, IDA, PMID:10550045) — silaffin-1
  peptides themselves perform the silica precipitation step that builds the
  wall, so the participation test in CLAUDE.md is satisfied: this gene product
  does the work, it is not merely required for or consumed by the process.
- `GO:0005199` structural constituent of cell wall (MF, IDA, PMID:11106386) —
  the tight, HF-resistant association with biosilica supports a structural role
  in the wall. This is the *structural* half of the function; the
  *precipitating* half has no GO term and is left to `proposed_new_terms`.

I considered and rejected a `NEW` row for `GO:0031214` biomineral tissue
development (wrong branch: tissue/multicellular, see above) and for any
polyamine-biosynthesis term (the polyamine modification is installed on SIL1 by
other, unidentified enzymes — SIL1 is the *substrate* of that modification, which
is exactly the non-participation case CLAUDE.md warns about).
