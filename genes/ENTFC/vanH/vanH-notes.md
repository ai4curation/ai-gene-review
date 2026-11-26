# vanH (Enterococcus faecium, Q05709) — curation notes

## Literature search record

No deep-research provider key exists here, and there is no model organism
database gene description for Enterococcus. `just fetch-fitness ENTFC vanH` was
not attempted; no fitness data set exists for this organism.

Sources checked:

- `genes/ENTFC/vanH/vanH-uniprot.txt` (Swiss-Prot Q05709): FUNCTION, five
  CATALYTIC ACTIVITY blocks each with a stated physiological direction,
  BIOPHYSICOCHEMICAL PROPERTIES, the three ACT_SITE residues and the NAD-binding
  features, and the three EC numbers (1.1.1.28, 1.1.1.272, 1.1.1.345) with
  experimental evidence.
- The two GOA-cited publications: PMID:1931965 and PMID:9605319 (both
  abstract-only in the cache).
- Fetched for operon context: PMID:1556077, PMID:8852545, PMID:1503450.
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04:
  `GO:0047809 D-lactate dehydrogenase activity` and `GO:0140175 (2R)-2-hydroxyacid
  dehydrogenase (NAD+) activity` are both `is_a` ancestors of `GO:0008720
  D-lactate dehydrogenase (NAD+) activity`; `GO:0016616` is an ancestor of
  `GO:0008720` and of `GO:0050578`; `GO:0050578` is **not** an ancestor of
  `GO:0008720` (it is the NADP+ counterpart).

## What VanH does

VanH is the dehydrogenase that supplies the D-hydroxy acid the resistance ligase
needs. The normal cytoplasm has no useful pool of D-lactate, so the operon
carries its own D-specific reductase.

[PMID:1931965 "We report purification of VanH to homogeneity, characterization as a D-specific alpha-keto acid dehydrogenase, and comparison with D-lactate dehydrogenases from Leuconostoc mesenteroides and Lactobacillus leichmanii."]
[PMID:8852545 "Tn1546 encodes the VanH dehydrogenase which reduces pyruvate to D-lactate (D-Lac) and the VanA ligase which catalyses synthesis of the depsipeptide D-alanyl-D-lactate (D-Ala-D-Lac)."]

That VanH's product is what VanA uses in vivo is shown by the complementation
experiment in the other direction:
[PMID:1503450 "D-Lactate added to the culture medium restored the vancomycin resistance of a strain that does not produce the VanH dehydrogenase and therefore appears to be a substrate of VanA in vivo."]

The second paper is a protein-engineering and crystallisation study of a
thioredoxin-VanH fusion whose kinetics match the native enzyme:
[PMID:9605319 "Michaelis constants for NADPH, NADH, and pyruvate, of approximately 3.5 microM, 19.0 microM, and 1.5 mM, respectively, were comparable to those reported for the native VanH"]
[PMID:9605319 "Like native VanH, maximum activity of the fusion protein requires the presence of an anion (phosphate or acetate), however, in addition, a strongly reducing environment is needed for optimal efficacy."]

## Why several molecular-function terms are all correct here

This is a genuinely broad-specificity enzyme, and the annotation set reflects
that rather than duplicating one claim. UniProt gives it three EC numbers, each
with experimental evidence from both papers, and five Rhea reactions:

- `GO:0008720 D-lactate dehydrogenase (NAD+) activity` — the physiological
  reaction, RHEA:16369, EC 1.1.1.28.
- `GO:0140175 (2R)-2-hydroxyacid dehydrogenase (NAD+) activity` — the generic
  NAD-dependent reaction, RHEA:35643, EC 1.1.1.345. This is an ancestor of the
  lactate-specific term, but it is not merely the uninformative parent: the
  enzyme really does act on 2-oxocarboxylates generally, with the highest
  catalytic efficiency on pyruvate **and** 2-oxobutanoate, and that broader
  claim is not entailed by the lactate term.
- `GO:0050578 (2R)-2-hydroxyacid dehydrogenase (NADP+) activity` — the NADP
  counterpart, RHEA:35735, EC 1.1.1.272. The cofactor preference is slightly
  toward NADPH (K_m 3.5 µM versus 19 µM), so this is not a secondary activity.
- `GO:0047809 D-lactate dehydrogenase activity` — the cofactor-agnostic parent.
  GOA derives it from RHEA:62968, the **NADP+**-dependent lactate reaction, for
  which GO has no cofactor-specific child. So although it is formally an
  ancestor of `GO:0008720`, the row is carrying the NADP-lactate activity and is
  accepted rather than marked too general. The missing child is raised as a
  question.
- `GO:0016616` is the EC-class-level parent of all of these and says nothing
  they do not, so that row is marked `TOO_GENERAL`.

Note the direction: every UniProt reaction is written in the oxidation
direction with `PhysiologicalDirection=right-to-left`, i.e. the enzyme runs as a
reductase in the cell, consuming NAD(P)H and pyruvate to make D-lactate. The GO
terms are direction-neutral, so this does not affect the actions, but it is why
the core function is described as a reduction.

## Missing from GOA

Nothing in GOA connects vanH to antibiotic resistance, although the gene is
cotranscribed with vanA and vanX under VanS-VanR control and all three are
required
[PMID:1556077 "The distal part of the van cluster encodes VanH, VanA, and a third enzyme, VanX, all of which are necessary for resistance."].
`GO:0046677 response to antibiotic` is proposed as a `NEW` row: it is the most
specific available term, since GO has no glycopeptide-specific child, and
functionally equivalent resistance enzymes already carry it in this repository.
