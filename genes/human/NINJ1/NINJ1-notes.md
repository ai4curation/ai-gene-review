# NINJ1 review notes

Reviewer journal. Every assertion below is anchored to a verbatim quote from a cached
publication in `publications/`.

## Why this gene is in the contested-function batch

Two things are live for NINJ1 in 2025-2026:

1. **How** it ruptures the plasma membrane - the "membrane-disk cutting" model versus the
   "large pore" model. This peaked in 2023-24 and 2025-26 is mostly consolidation.
2. **Whether membrane rupture is all it does.** A 2026 paper shows PMR-deficient Ninj1
   mutants retain a haematopoietic function, i.e. a separable second role. That bears
   directly on the curation question of whether the 1990s cell-adhesion characterisation is
   core biology or history.

## The core function: plasma membrane rupture

Founding forward-genetic identification, and the key phenotype - cells still die, but they
do not disintegrate:
[PMID:33472215 "Ninj1-/- macrophages exhibited impaired PMR in response to diverse inducers
of pyroptotic, necrotic and apoptotic cell death, and were unable to release numerous
intracellular proteins including HMGB1 (a known DAMP) and LDH (a standard measure of PMR)."]
and [PMID:33472215 "Ninj1-/- macrophages died, but with a distinctive and persistent
ballooned morphology, attributable to defective disintegration of bubble-like herniations."].

Mechanism from the same paper: [PMID:33472215 "Mechanistically, NINJ1 used an
evolutionarily conserved extracellular domain for oligomerization and subsequent PMR."].

Oligomerisation is the activation step, not a by-product. An antibody that blocks it blocks
rupture: [PMID:37196676 "Here we describe an anti-NINJ1 monoclonal antibody that
specifically targets mouse NINJ1 and blocks oligomerization of NINJ1, preventing PMR."].
And glycine, the classical 30-year-old cytoprotectant, turns out to act at this step:
[PMID:36468682 "Next, we show that glycine prevents NINJ1 clustering by either direct or
indirect mechanisms."].

## The mechanistic dispute: disks vs pores

Degen et al. resolved the filament and the amphipathic-helix insertion mechanism:
[PMID:37198476 "A cryo-electron microscopy structure of NINJ1 filaments shows a tightly
packed fence-like array of transmembrane α-helices."] and
[PMID:37198476 "Our data thus suggest that, during lytic cell death, the extracellular
α-helices of NINJ1 insert into the plasma membrane to polymerize NINJ1 monomers into
amphipathic filaments that rupture the plasma membrane."].

The Wu lab reading is that the rings excise and shed membrane disks - explicitly *not*
a pore mechanism:
[PMID:38614101 "This structural observation suggests that NINJ1 can form membrane disks,
consistent with membrane fragmentation by recombinant NINJ1."] and
[PMID:38614101 "Therefore, NINJ1-mediated membrane disk formation is different from
gasdermin-mediated pore formation, resulting in membrane loss and plasma membrane rupture."].

The Dai lab agrees on solubilisation but keeps pores on the table, and explains why the
paralog NINJ2 cannot do this at all:
[PMID:39667936 "This structural feature and other evidence point to a PMR mechanism by which
NINJ1 filaments wrap around and solubilize membrane fragments and, less frequently, form
pores in the plasma membrane."].

**Curation consequence:** the disagreement is about *how* the activity is executed, not about
whether it exists. Every model is an instance of `GO:0140912 membrane destabilizing activity`
("Binding to a membrane and increasing its permeability"), so the dispute does not change the
action on any annotation. It is recorded in the `reason` and raised in `suggested_questions`.

The 2026 Genentech perspective (PMID:42350666, *Surveying the roles of NINJ1 in plasma
membrane rupture*, Deshpande I & Kayagaki N, Nat Struct Mol Biol 2026,
doi 10.1038/s41594-026-01834-3) was fetched but PubMed indexes **no abstract** for it and it
is not in PMC, so its content could not be retrieved. It is cited in `references` with
`full_text_unavailable: true` and `correctness: UNVERIFIED`, and **no claim in this review
rests on it**.

## NINJ1 is not pyroptosis-specific

The single activity is used by many death programs. Ferroptosis, and crucially only at the
terminal step: [PMID:38396301 "We report that NINJ1 oligomerizes during ferroptosis, and that
Ninj1-deficiency protects macrophages and fibroblasts from ferroptosis-associated PMR."] plus
[PMID:38396301 "Mechanistically, we find that NINJ1 is dispensable for the initial steps of
ferroptosis, such as lipid peroxidation, channel-mediated calcium influx, and cell swelling."].

And in 2026, with no known death program engaged at all:
[PMID:42270656 "In glucose-starved macrophages, NINJ1 ruptures membranes independently of
known cell death programs."] and
[PMID:42270656 "We show that glucose starvation induced by major fungal pathogens Candida
albicans and Candida auris causes macrophage lysis by activating NINJ1, the executioner of
membrane rupture during cell death."].

So `GO:0141201 pyroptotic cell death`, `GO:0097300 programmed necrotic cell death` and
`GO:0097707 ferroptosis` are all ACCEPTed, but each `reason` says explicitly that they are
*contexts* of one shared terminal effector, not evidence of pathway specificity.

## The adhesion question: core or historical?

The 1996-97 characterisation is real experimental work, not a naming accident:
[PMID:9261151 "Aggregation assays were used to demonstrate that ninjurin-mediated adhesion
requires divalent cations and is an energy-dependent process."] and
[PMID:9261151 "The critical domain for ninjurin-mediated homophilic adhesion was localized to
an 11-residue region (between Pro26 and Asn37) by mutagenesis and by employing synthetic
oligopeptides as competitive inhibitors of ninjurin-mediated adhesion."].

The motif is still a live handle - a peptide from it binds endogenous NINJ1:
[PMID:33028854 "Importantly, a pull-down assay revealed a direct binding between exogenously
delivered N-NAM and endogenous Ninj1 and it is N-terminal adhesion motif dependent."].

And the adhesion activity has a clean cell-biological readout in humans:
[PMID:22162058 "Moreover, Ninjurin-1 neutralization specifically abrogated the adhesion and
migration of human monocytes across BBB-ECs, without affecting lymphocyte recruitment."].

The decisive 2026 argument against calling it purely historical is that NINJ1 demonstrably
does non-lytic work:
[PMID:42481508 "Ninj1 deficiency reduced HSPC, neutrophil and erythrocyte numbers, whereas
PMR-deficient Ninj1 mutants demonstrated that this function is independent of PMR."].

**But be honest about the gap.** That paper attributes the HSPC function to WNT, not to
adhesion: [PMID:42481508 "Mechanistically, Ninj1 and Ninj2 cooperatively promoted early HSPC
amplification through canonical WNT signaling."]. It does not test the adhesion motif. So the
existence of a PMR-independent function is established; its identity with the adhesion
activity is *not*.

**Position taken:** both `GO:0140912 membrane destabilizing activity` and `GO:0098632
cell-cell adhesion mediator activity` are kept as core functions, with the unbridged gap
stated in the `reason` and in `suggested_questions` rather than papered over. There is also a
structural tension worth flagging: the same extracellular α1/α2 helices that mediate rupture
are adjacent to the adhesion determinant, so the two activities may be two uses of one
surface. `GO:0098631` (the parent, cell adhesion mediator activity) is MODIFYed to the
child, since what was shown is homophilic binding between cells, not adhesion to a substrate.

## Other calls

- `GO:0001530 lipopolysaccharide binding` (IDA, PMID:26677008) → **KEEP_AS_NON_CORE**, not
  removed. The result is genuine - [PMID:26677008 "Notably, pull-down assays using lysates
  from HEK293T cells transfected with human or mouse Ninjurin1 and biotinylated LPS
  (LPS-biotin) showed that LPS directly bound Ninjurin1."] - but it is one lab, in transfected
  HEK293T lysates, never reproduced, with no counterpart in any of the NINJ1 cryo-EM
  structures, and the implicated residues (81-100) lie outside the α1/α2 region that carries
  the characterised activity. The matching `GO:0034145` TLR4 ISS is demoted for the same
  reason, so the two stay consistent.
- `GO:0005576 extracellular region` (IEA) → **KEEP_AS_NON_CORE**, *not* over-annotated. I
  initially read this as a topology artefact, but UniProt annotates a genuine separate
  "Secreted ninjurin-1" chain generated by cleavage. Checking the UniProt record before
  calling it an error was the difference.
- `GO:0016020 membrane` (IEA/InterPro) → **MODIFY** to `GO:0005886 plasma membrane`.
- `GO:0005515 protein binding` (HuRI + Rolland interactome) → **MARK_AS_OVER_ANNOTATED**.
- `GO:0045766 positive regulation of angiogenesis` → KEEP_AS_NON_CORE, with a flag: the
  pro-angiogenic effect was produced by *suppressing* endogenous NINJ1 with the N-NAM peptide
  ([PMID:33028854 "We found that N-NAM promotes proliferation, migration, and tube formation
  of HUVECs and demonstrate that the suppression of endogenous Ninj1 is responsible for the
  N-NAM-mediated pro-angiogenic effects."]), so the *positive* direction is not the most
  transparent reading. Not corrected, because this is an experimental annotation whose full
  text the curator read and the rat orthology transfer agrees with it; the doubt is recorded
  instead.
- The mouse-ISS cluster (`GO:0097060` synaptic membrane, `GO:0042692` muscle cell
  differentiation, `GO:0071474` hyperosmotic response, `GO:0034113` heterotypic adhesion) →
  KEEP_AS_NON_CORE. UniProt records several of these as "By similarity" only.

## Proposed new term

GO has no term for **plasma membrane rupture** - only `GO:0019835 cytolysis`, which conflates
the active terminal step with lysis in general. The NINJ1 literature established exactly this
distinction and it is experimentally separable (gasdermin pores form, but rupture does not
follow, in Ninj1-null cells). Proposed with `GO:0019835` as parent.
