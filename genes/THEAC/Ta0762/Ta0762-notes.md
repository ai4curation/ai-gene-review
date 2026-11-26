# Ta0762 (Q9HK44, Thermoplasma acidophilum) notes

## 2026-11-23: review created to carry the mevalonate-3-phosphate 5-kinase term request

Context: the mevalonate-pathway cross-species campaign reviewed the Thermoplasmatales mevalonate
3-kinase (genes/PICTO/PTO1356) and mevalonate 3,5-bisphosphate decarboxylase (genes/THEAC/Ta0893), and
both reviews request missing GO terms. Ta0762 catalyses the step between them, and its activity also has
no GO term, so this review records the third request in structured form.

### Literature search

- PubMed `"mevalonate-3-phosphate 5-kinase" OR "mevalonate 3-phosphate 5-kinase" OR
  "mevalonate-3-phosphate-5-kinase"`: one hit, PMID:24914732.
- PubMed `Ta0762`: no hits (the locus is named only in full texts).
- Full text of PMID:28004831 (cached) uses Ta0762 as a reagent.
- UniProt Q9HK44 (Swiss-Prot) curates FUNCTION, CATALYTIC ACTIVITY and kinetics from PMID:24914732.

### Findings

- Activity: only Ta0762 of seven candidates acted on mevalonate 3-phosphate
  [PMID:24914732 "Of the seven enzymes tested, only Ta0762 showed activity with mevalonate 3-phosphate"],
  and the product is mevalonate 3,5-bisphosphate by 13C NMR
  [PMID:24914732 "The observed spectrum is consistent with the structure of mevalonate 3,5-bisphosphate."].
- Former annotation wrong: [PMID:24914732 "Ta0762 had been computationally annotated as
  2-phosphoglycerate kinase, though no activity was detected with 2-phosphoglycerate"].
- Pathway position: [PMID:28004831 "with mevalonate 3-phosphate 5-kinase acting between the 3-OH
  phosphorylation of mevalonate and the decarboxylation by MBD"].
- Km could not be measured because the substrate is not commercially available (PMID:24914732).

### Ontology check (2026-11-23)

- Rhea: RHEA:42888, (R)-3-phosphomevalonate + ATP = (R)-3,5-bisphosphomevalonate + ADP + H(+),
  EC 2.7.1.186.
- ExPASy ENZYME: EC 2.7.1.186, mevalonate-3-phosphate 5-kinase.
- GO release 2026-07-26: no rhea2go or ec2go line for RHEA:42888 or EC 2.7.1.186, and OLS finds no
  term (positive controls on existing mevalonate-pathway terms returned hits).
- Requested as `mevalonate-3-phosphate 5-kinase activity` under GO:0016773, with exactMatch mappings to
  RHEA:42888 and EC:2.7.1.186.

### Aside for the Ta0893 review (resolved 2026-11-26)

PMID:24914732 also reports that Ta0893 showed no activity on mevalonate 3,5-bisphosphate, which
PMID:28004831 later overturned with truncated or chaperone-co-expressed protein. The Ta0893 review does
not yet record that superseded negative finding.

Resolved 2026-11-26: the Ta0893 review now records the negative as an OVERTURNED finding on
PMID:24914732, superseded by PMID:28004831.
