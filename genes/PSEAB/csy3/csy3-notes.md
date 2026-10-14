# csy3 / Cas7f (Q02MM1) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this file
is my own literature journal. Every assertion carries an inline PMID plus a verbatim
quote from the cached record in `publications/`.

## What this protein is

PA14_33310, 342 aa, "CRISPR-associated protein Csy3" = **Cas7f, the backbone subunit**.
Six copies polymerise along the crRNA:
[PMID:32170016 "the maps exhibit an asymmetric spiral, with one Cas6f subunit in the
head, one Cas5f and one Cas8f in the tail, and six Cas7f comprising the spiral
backbone"], matching UniProt's stoichiometry
`Csy1(1),Csy2(1),Csy3(6),Cas6/Csy4(1)-crRNA(1)` and
[PMID:32170016 "The Csy complex is comprised of four types of Cas proteins (Cas5f-8f)
and a single 60-nt crRNA"]. A Csy3(6)·Cas6f(1)·crRNA(1) subcomplex also forms (UniProt
SUBUNIT), which is consistent with the IntAct Csy3–Cas6f pair behind GOA's two
`GO:0005515` rows (Q02MM1–Q02MM2, NbExp=12). Original PA14 biochemistry:
[PMID:21536913 "the Csy proteins (Csy1-4) assemble into a 350 kDa ribonucleoprotein
complex that facilitates target recognition by enhancing sequence-specific
hybridization between the CRISPR RNA and complementary target sequences"].

## What Cas7f does

**Binds and kinks the crRNA, non-sequence-specifically.**
[PMID:32170016 "Cas7f and crRNA form multiple hydrogen bonds, which mostly occur between
the arginine-rich region (F32, R34, R68, Q95, R168, Q247, Q276, K277, R283, S308, R350)
and the sugar-phosphate backbone of crRNA"] — backbone, not bases:
[PMID:32170016 "This finding indicates the nonsequence-specific crRNA recognition mode
of Cas7f"]. The kinking is the functional point, since it segments the guide:
[PMID:32170016 "The thumbs of the spiral backbone proteins (Cas7f) distort the crRNA at
6-nt intervals"].

**Pins the crRNA:target-DNA heteroduplex.** This is the step that makes the backbone an
active participant in target verification rather than a scaffold:
[PMID:28985564 "hairpin emanating from the adjacent Cas7f subunit threads through each
of these gaps spaced along the backbone, effectively pinning the RNA:DNA heteroduplex
to the Csy complex backbone"]. The structures are of the PA14 complex:
[PMID:28985564 "The structural studies we describe here are focused on the type I-F Csy
(CRISPR system yersinia) found in Pseudomonas aeruginosa"].

**Carries the DNA-binding surface of the backbone.**
[PMID:32170016 "a lysine-rich region of the Cas7f subunit (K76, K78, K84, and K256) has
been reported to be critical for DNA binding by the Csy complex"].

## The anti-CRISPR connection

Cas7f is the principal anti-CRISPR target surface of this system, which is why the
module calls it "the surface bound by AcrIF8 and related inhibitors":
[PMID:32170016 "The Acr proteins either bind to the Cas7f backbone (AcrF9, AcrF8) or
insert between the Cas7f and Cas8f subunits in the tail region (AcrF6)"] — and the
inhibitors compete for the very residues above:
[PMID:32170016 "a lysine-rich region of the Cas7f subunit (K76, K78, K84, and K256) has
been reported to be critical for DNA binding by the Csy complex"]. This is consistent
with the completed phage-side review `genes/BPZF4/AcrF8/AcrF8-ai-review.yaml`, which
records AcrIF8 contacting both the Cas7f backbone and the crRNA.

## In vivo

Csy3 is required for spacer acquisition — a gene-specific deletion, which is the
grounding for the CACAO IMP:
[PMID:26586803 "Deleting the csy3 gene (lane 6), or mutating the catalytic residue His29
of Csy4 nuclease (lane 7) that is needed for generation of mature crRNA also abolished
spacer acquisition"], in a system where
[PMID:26586803 "both modes require, in addition to Cas1 and Cas2, intact Csy complex, an
ortholog of the E. coli Cascade, and crRNA"].

Csy3 is *not* in the strict-requirement class for crRNA accumulation:
[PMID:21398535 "proteins Csy4 and Csy2 are essential for small CRISPR RNA (crRNA)
production in vivo, while the Csy1 and Csy3 proteins are not absolutely required for
production of these small RNAs"] — so its `GO:0043571` annotation is earned by the
acquisition phenotype, not by a crRNA-biogenesis phenotype.

## Curation decisions

- Both `GO:0005515 protein binding` rows (IPI, partner Cas6f) → MODIFY to
  `GO:0005198 structural molecule activity`. Cas7f *is* the structural element: six
  copies interlock thumb-into-palm through roughly 2,000 Å² interfaces, and the spiral
  they form runs from the Cas6f head to the Cas8f–Cas5f tail, which is the contact this
  IntAct record samples. Holding the complex together is the whole of what this
  subunit's protein–protein contacts do.

  **Aspect correction (follow-up).** My first pass proposed
  `part_of GO:0032991 protein-containing complex` as the replacement, reasoning from the
  E. coli comparator where all five Cascade subunits carry exactly that. That was wrong
  in form: these GOA rows carry `qualifier: enables`, so they are molecular-function
  rows, and a gene product cannot *enable* a cellular component. However
  well-supported complex membership is, it cannot be expressed by swapping a CC term
  into an `enables` MF row. The E. coli reviews were not making this mistake — their
  GOA already contained separate `part_of GO:0032991` rows, which they MODIFY to
  `GO:1990904`; their `enables GO:0005515` rows went to `GO:0005198` instead.
  Reconciled to the same convention:

  - **MODIFY the `enables` rows to `GO:0005198 structural molecule activity`** ("the
    action of a molecule that contributes to the structural integrity of a complex").
    Aspect-correct, and none of its 22 children fits a non-ribosomal ribonucleoprotein,
    so the parent is the right level. Each row is backed by the verbatim structural
    quote naming the contact this subunit actually makes.
  - **Carry complex membership on its own `NEW part_of GO:1990904 ribonucleoprotein
    complex` row.** PA14 has no `part_of` complex row for any Csy subunit, unlike all
    five E. coli Cascade subunits, so this is a real missing annotation rather than a
    reformulation. `GO:1990904` rather than the bare `GO:0032991` root because the
    60-nt crRNA is an integral component, not a ligand.
  - **`core_functions[].in_complex` → `GO:1990904`** for the same reason.
  - **Added a `proposed_new_terms` entry** for a "CRISPR RNA-guided surveillance
    complex" CC term under `GO:1990904`, identical in substance to the one the five
    E. coli Cascade reviews carry, so the two systems request one term rather than two.
    GO's entire CRISPR vocabulary is five BP terms (`GO:0099048`, `GO:0043571`,
    `GO:0098672` and the obsolete `GO:0110132`/`GO:0110133`); ComplexPortal models the
    type I-E complex as CPX-1005, GO does not.
- `GO:0043571 maintenance of CRISPR repeat elements`, IMP,
  `acts_upstream_of_or_within_positive_effect` → ACCEPT. A clean `csy3` deletion
  abolishes spacer acquisition. The hedged qualifier is appropriate: the requirement
  runs through complex integrity rather than through a Csy3 catalytic step.

## Gaps identified (missing annotations)

- `GO:0003723 RNA binding` (NEW, IDA, PMID:32170016). **Comparator:** casC (Cas7e,
  Q46899) carries `GO:0003723` by IDA (PMID:25103409), as do casA, casD and casE. The
  eleven-residue crRNA-backbone contact set is directly resolved here.
- `GO:0071667 DNA/RNA hybrid binding` (NEW, IDA, PMID:28985564). **Comparator:** this is
  precisely the term casC carries by IDA from PMID:25123481 — the Cas7 subunit of E.
  coli Cascade — and casD carries it too. The β-hairpin threading that pins the
  RNA:DNA heteroduplex is the same mechanism. Of all the proposals in this gene set,
  this is the one with the tightest subunit-to-subunit comparator match.
- `GO:0099048 CRISPR-cas system` (NEW, IDA). **Comparator:** all five E. coli Cascade
  subunits carry it by IDA (PMID:18703739); no PA14 Csy subunit does. Cas7f does work in
  the "target interference" stage named in the term's definition — it presents the guide
  in segments and holds the heteroduplex — rather than merely being required for it.
  Checked via QuickGO that `GO:0099048` is not an ancestor or descendant of
  `GO:0043571` or `GO:0051607`.

## Not proposed, and why

- `GO:0003677 DNA binding`. The lysine-rich patch is described as critical for DNA
  binding **by the Csy complex**, which is a contributes-to statement about the complex,
  not a demonstration that isolated Cas7f binds DNA. **Comparator:** E. coli casC does
  not carry a DNA-binding term either — it carries `GO:0071667`, which is what I propose.
  The complex-level dsDNA-binding activity is captured in `core_functions` as a
  `contributes_to_molecular_function` instead.
- `GO:0051607 defense response to virus`. No `csy3` allele has been assayed for phage
  resistance, and the PA14 locus-level evidence is contested (see `cas3-notes.md`).
- No molecular-function term exists for crRNA-guided target recognition; recorded as an
  ontology gap in `modules/crispr_cas_adaptive_immunity.yaml` and
  `modules/anti_crispr_suppression.yaml`, and raised in `suggested_questions` rather
  than filled with an ill-fitting id.
