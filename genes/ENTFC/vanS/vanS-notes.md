# vanS (Enterococcus faecium, Q06240) — curation notes

## Literature search record

No deep-research provider key exists here and there is no model organism
database description for Enterococcus. `just fetch-fitness ENTFC vanS` was not
attempted; no fitness data set exists for this organism.

Sources checked:

- `genes/ENTFC/vanS/vanS-uniprot.txt` (Swiss-Prot Q06240): FUNCTION (which
  records the activation controversy explicitly), CATALYTIC ACTIVITY (EC
  2.7.13.3), ACTIVITY REGULATION, SUBCELLULAR LOCATION, INDUCTION, PTM, the two
  transmembrane helices (21-41, 76-96), the histidine-kinase domain (161-376),
  the low-affinity ATP-binding region and the autophosphorylated His164.
- The three GOA-cited publications: PMID:8494882, PMID:8664263 (both
  abstract-only) and PMID:30677074 (full text available and read).
- Fetched for the activation question: PMID:28511809 (full text), the paper on
  the other side of it, and PMID:1556077 for the in vivo genetics.
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04: `GO:0000155
  phosphorelay sensor kinase activity` is an `is_a` **descendant** of `GO:0004673
  protein histidine kinase activity`; `GO:0016772` is an ancestor of
  `GO:0004673`; `GO:0007165 signal transduction` is an ancestor of `GO:0000160
  phosphorelay signal transduction system`; `GO:0016020 membrane` is an ancestor
  of `GO:0005886 plasma membrane`.

## What VanS does

VanS is the membrane sensor of the two-component system that switches the
resistance operon on. Three catalytic activities are attributed to it, and the
first two are directly measured.

Autophosphorylation on a histidine:
[PMID:8494882 "The MBP-VanS fusion protein displayed an ATP-dependent autophosphorylation on a histidine residue with a rate of 0.17 min-1 and a phosphorylation stoichiometry of 10-15%."]

Phosphotransfer to VanR, with a large kinetic preference for its cognate partner:
[PMID:8494882 "32P-PhosphoMBP-VanS transferred the phosphoryl group to VanR."]
[PMID:8664263 "The corresponding kxfer of 96 min-1 for phosphotransfer from P-VanS to VanR required quench kinetics."]
[PMID:8664263 "A KM of 3 microM was estimated for VanR, leading to a 10(4)-fold preference in kxfer/KM for phosphotransfer to VanR compared to PhoB."]
[PMID:8664263 "No phosphotransfer was detachable to three other E. coli response regulators, OmpR, ArcB, or CreB, providing some sense of the selectivity against two-component regulatory system cross-talk."]

Dephosphorylation of phospho-VanR, which is how the resting state is enforced:
[PMID:30677074 "In the absence of vancomycin, VanS dephosphorylates VanR, thereby maintaining it in a transcriptionally inactive state."]
[PMID:30677074 "Hence, three distinct catalytic activities are associated with VanSA: autophosphorylation, phosphotransfer, and dephosphorylation."]
and the full-length protein has all three:
[PMID:30677074 "Both detergent- and amphipol-solubilized VanSA display all the enzymatic activities expected for a sensor histidine kinase, with amphipol reconstitution providing a marked boost in overall activity relative to detergent solubilization."]
with a constitutively-active-type mutant behaving as predicted:
[PMID:30677074 "A putative constitutively activated VanSA mutant (T168K) was constructed and purified, and was found to exhibit the expected reduction in phosphatase activity"]

## The activation signal is contested, and the review does not take a side

The primary literature is split on this point, which is why no small-molecule
activator is asserted here.

Against direct activation, with full-length protein in two solubilisation
systems:
[PMID:30677074 "In both detergent and amphipol solutions, VanSA's enzymatic activities were found to be insensitive to vancomycin, even at levels many times higher than the antibiotic's minimum inhibitory concentration."]
[PMID:30677074 "This result argues against direct activation of VanSA via formation of a binary antibiotic-kinase complex, suggesting instead that either additional factors are required to form a functional signaling complex, or that activation does not require direct interaction with the antibiotic."]

For direct activation, by spectroscopy and activity assay:
[PMID:28511809 "Results showed significant increases in the activity of VanSA in the presence of GPAs and decreases in activity in the presence of peptidoglycan components (Fig. 6)."]
[PMID:28511809 "suggest GPAs vancomycin and teicoplanin themselves and not peptidoglycan components are the activating ligands for VanSA"]

UniProt reports both, which is the right treatment: "Binds directly to, and
autophosphorylation activity is enhanced by, the glycopeptides vancomycin and
teicoplanin, in vitro (PubMed:28511809). However it has also been reported that
autophosphorylation, phosphate transfer to VanR and dephosphorylation of
phospho-VanR are all unaffected by the presence of vancomycin, in vitro
(PubMed:30677074)."

Nothing in the GOA row set depends on the answer, so no annotation action turns
on it. It is recorded as a reference-level `DISPUTED` judgement on both papers
and as a knowledge gap. Note also that PMID:28511809 itself frames the
mechanism as suppression of the phosphatase arm rather than stimulation of the
kinase arm, which is a third possibility that neither activity measurement
directly tests.

## Annotation issues

- **`GO:0004673 protein histidine kinase activity`, four rows (three EXP, one
  from the EC mapping), is the generic term.** `GO:0000155 phosphorelay sensor
  kinase activity` is its `is_a` child, is already annotated to this gene from
  the PANTHER mapping, and is what the assays actually show: autophosphorylation
  on a histidine followed by transfer to a cognate response regulator, with a
  ten-thousand-fold preference for VanR over PhoB and no transfer to three other
  regulators. All four rows are therefore modified to the specific child.
- **`GO:0004721 phosphoprotein phosphatase activity` is accepted.** The
  phosphatase arm is real and is what holds the operon off; the term is generic
  only because GO has no term for a response-regulator aspartyl-phosphate
  phosphatase, which the module also notes.
- **`GO:0016036 cellular response to phosphate starvation` is removed.** It comes
  from the same PANTHER node as three correct rows, but it is an
  over-propagation: UniProt places VanS in PANTHER:PTHR45453, whose official name
  is PHOSPHATE REGULON SENSOR PROTEIN PHOR. VanS senses a glycopeptide signal and controls a resistance operon; the
  phosphate regulon is a different system, and PMID:8664263 shows VanS does not
  even transfer phosphate to PhoB at a physiologically meaningful rate. The
  phosphate-starvation process term is inherited from the family's dominant
  member and is not a property of this protein.
- `GO:0016772` and `GO:0007165` are ancestors of terms asserted here and are
  marked `TOO_GENERAL`; `GO:0016020 membrane` is refined to `GO:0005886 plasma
  membrane`, the only membrane this organism has and the term already annotated
  from PANTHER.

The development GO-CAM model gomodel:671ae02600002832 attaches vancomycin as a
small-molecule activator (RO:0012001, CHEBI:28001) with direct-assay evidence
from PMID:8494882, a paper that assayed only the VanS cytosolic domain and never
tested vancomycin. That defect is recorded here as a `source_defects` entry on
the `GO:0000155` row (resource `GO_CAM`, `requested_change: CHECK`) and is also
raised as a question.

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0000155 / GO_REF:0000120: defect downgraded (evidence depth: ABSTRACT). Defect is on GO-CAM gomodel:671ae02600002832, not the GOA row. Model TTL confirms the edge and its ECO:0000314/PMID:8494882 evidence, but the predicate is RO:0012005 "is small molecule activator of" (not RO:0012001) and the model state is now "delete". "Never tested vancomycin" rests on the abstract only (no full text), so CONFIRMED -> PROBABLE; record id added, slot corrected, model state noted.
