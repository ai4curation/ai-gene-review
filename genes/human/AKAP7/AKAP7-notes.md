# AKAP7 / AKAP15 / AKAP18 (O43687) — review notes

2026-10-03. PAINT no-IBA backlog. Provider: affinage (gates clear, strong recall this time).

## Scope first: this entry is the short isoforms only

O43687 holds **AKAP18α (AKAP15) and AKAP18β** — the short, N-terminally lipid-anchored,
plasma-membrane forms. The long cytosolic **γ/δ forms are a separate entry, Q9P0M2**:

> [file:genes/human/AKAP7/AKAP7-uniprot.txt "IsoId=Q9P0M2-1; Sequence=External;"]

That matters because much of the affinage narrative — the 2H phosphoesterase that degrades 2-5A
(RNase L antiviral function), and the USP4/SERCA2 work in heart — belongs to the long isoforms.
**None of it is imported here.**

## Outcome: 15 rows + 1 NEW → 5 MODIFY, 5 ACCEPT, 4 non-core, 1 UNDECIDED, 1 NEW

### Refinements (MODIFY)

- **`GO:0051018` PKA binding (IDA, TAS, IEA) → `GO:0034237` RII-subunit binding.** The cleanest
  comparator result of the campaign: AKAP1, AKAP5 and AKAP9 all carry `GO:0034237` (including IBA),
  and **so does mouse Akap7, by IDA**. Human AKAP7 was the outlier. Structural support is on this
  entry's own β isoform: [PMID:27102985 "Here, we elucidated the structure of an extended PKA-binding domain of AKAP18β bound to the D/D domain of the regulatory RIIα subunits of PKA."]
- **`GO:0008104` → `GO:0072659` protein localization to plasma membrane** — the paper names the
  destination; `GO:0072659` verified as a descendant of `GO:0008104` via OLS.
- **`GO:0006811` monoatomic ion transport (TAS) → `GO:0051924` regulation of calcium ion
  transport.** Participation test: an AKAP moves no ions; it regulates the channel that does.

### The NEW row

**`GO:0060090` molecular adaptor activity (IPI).** AKAP15 makes both contacts itself — RII on one
side, the CaV1 C-terminal leucine zipper on the other:
[PMID:14569017 "Site-directed mutagenesis studies reveal that AKAP15 directly interacts with the distal C terminus of the cardiac CaV1.2 channel via a leucine zipper-like motif."]
Comparator: AKAP5 and AKAP9 carry `GO:0060090` by IBA among others, so PAINT places it on the AKAP
lineage. Promoted to `core_functions.molecular_function`.

### Kept but non-core: the IKs rows

PMID:11299204 gives four IDAs (K⁺ transport regulation, membrane repolarization, response to cAMP,
action potential). The result is real, but read the framing:
[PMID:11299204 "coexpression of the neuronal A kinase anchoring protein (AKAP)79, a fragment of a cardiac AKAP (mAKAP), or cardiac AKAP15/18 restored cAMP regulation of KvLQT1/IsK complexes"]
— three unrelated AKAPs, interchangeable, in heterologous cells, with a modest effect. That shows
AKAP15/18 *can* confer cAMP regulation when supplied, which is a property of being an AKAP, not that
it is the IKs anchor in myocytes. Kept, demoted to non-core.

**`GO:0001508` action potential → UNDECIDED.** The abstract reports voltage-clamp currents and never
mentions action potentials. The full text might — publisher returns 403, no PMC copy — so per the
action definition it is UNDECIDED, not REMOVE.

## A genuine conflict, recorded not resolved

- [PMID:14569017 "Disruption of PKA anchoring to CaV1.2 channels via AKAP15 using competing peptides markedly inhibits the beta-adrenergic regulation of CaV1.2 channels via the PKA pathway in ventricular myocytes."]
- [PMID:23035250 "KO cardiomyocytes responded normally to adrenergic stimulation, as measured by whole-cell patch clamp or a fluorescent intracellular Ca(2+) indicator."]

The knockout deleted **all** isoforms. Both results stand; the open question is whether the peptides
hit other AKAPs or other AKAPs compensate in the knockout. Recorded as a BIOLOGY knowledge gap.

## Recall

Unusually, affinage outperformed GOA: it surfaced the CaV1.1 leucine-zipper paper (PMID:11733497),
the knockout negative, and the mossy-fiber LTP work — none cited by any GO annotation. My own PubMed
search added PMID:14569017 (CaV1.2), which became the anchor for the NEW row.

The mossy-fiber result is curated on mouse (`GO:0050804`, `GO:0098686`, IDA+IMP) but not human —
recorded as a CURATION gap, consistent with how I treated the analogous AKAIN1 case.

## Process

- Quotes checked whitespace-collapsed but otherwise character-exact: 24 distinct, 0 failures.
- GO_REF entries copied from the seeder.
- PR #3932's review bot failed on its usage quota ("session limit, resets 8pm UTC"), not on the
  PR; re-run after the reset.
