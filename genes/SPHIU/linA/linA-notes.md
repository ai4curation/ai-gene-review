# Notes: linA (gamma-HCH dehydrochlorinase, Sphingobium indicum UT26)

Part of the category-4 counter-example set in
`projects/NONPHYSIOLOGICAL_REACTIONS.md`. Reviewing it surfaced the project's
most actionable GO finding.

## The finding: a bulk obsoletion caught a well-characterized enzyme

LinA has **no molecular function annotation in GOA at all**. The specific term
GO:0018830 gamma-hexachlorocyclohexane dehydrochlorinase activity was obsoleted
in go-ontology#28108, a bulk action over 160 leaf catalytic terms selected for:
leaf status, a partial EC xref, zero annotations, no RHEA xref, and no
MetaCyc/KEGG xref. The obsoletion comment reads "This term was obsoleted
because there is no evidence that this specific activity exists."

For this term that statement is wrong. The activity has:

- Tn5-mutant genetics in a host that grows on lindane as sole carbon source
  [PMID:7686793 "Pseudomonas paucimobilis UT26 grows on gamma-hexachlorocyclohexane (gamma-HCH) as a sole source of carbon and energy."].
- In vitro complementation showing LinA is required for both pathway steps
  [PMID:7686793 "An in vitro complementation test with a crude extract from UT64 plus partially purified LinA protein showed that LinA was essential not only for the first-step reaction (gamma-HCH to gamma-pentachloro-cyclohexene; gamma-PCCH), but also for the second-step reaction (gamma-PCCH to compound B) of gamma-HCH degradation in UT26."].
- Mechanistic and stereochemical characterization by GC-MS, NMR, CD and
  modelling
  [PMID:11099497 "LinA requires the presence of a 1,2-biaxial HCl pair on a substrate molecule."],
  which explains the isomer specificity (alpha, gamma, delta but not beta,
  whose substituents are all equatorial).
- A UniProt-recorded reaction, RHEA:45480, which has no GO term.

**The selection criteria tracked curation coverage, not evidence.** "Zero
annotations" and "no Rhea xref" were both true of this term at the time and
both are properties of the annotation pipeline rather than of the biology. The
sibling GO:0018833 DDT-dehydrochlorinase activity survived the same action only
because it had an EC number and a Rhea mapping.

Proposed in the review: restore the term under GO:0016848 carbon-halide lyase
activity with a skos:exactMatch to RHEA:45480, and interim-annotate GO:0016848
as NEW so the gene is not left with nothing.

Follow-up for the project: audit the other 159 terms from #28108 against
current UniProt catalytic activity records and Rhea mappings.

## Other notable points

- Cofactor-independent lyase; no metal, no redox cofactor. Scytalone
  dehydratase-like fold.
- Periplasmic (experimentally, ECO:0000269) but not N-terminally processed, so
  the export route is unidentified. Unusual enough to record as a knowledge gap.
- Ancestral substrate unknown. The requirement is permissive (a 1,2-biaxial
  H-Cl pair, no cofactor), so a natural polychlorinated alicyclic compound
  would satisfy it; none has been tested. Lindane dates from the 1940s, so
  either the activity predates it or it arose within decades.
