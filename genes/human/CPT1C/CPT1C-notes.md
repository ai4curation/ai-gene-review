# CPT1C Review Notes

## 2026-02-05: Initial Review

### Context
CPT1C was identified during analysis of human Recon3D metabolic model as having an EC number discrepancy (CLASS_CHANGE type). This prompted a full GO annotation review.

### Recon3D Model Error

**Finding**: CPT1C (gene ID 126129) is annotated in Recon3D with carnitine O-palmitoyltransferase activity (EC 2.3.1.21), but experimental evidence demonstrates it actually functions as a palmitoyl thioesterase (EC 3.1.2.22).

| Source | EC Number | Enzyme Class | Function |
|--------|-----------|--------------|----------|
| Recon3D | 2.3.1.21 | Transferase | Carnitine O-palmitoyltransferase |
| UniProt (correct) | 3.1.2.22 | Hydrolase | Palmitoyl thioesterase |

**Impact**: This is a CLASS_CHANGE error - the enzyme class is completely different:
- Recon3D assumes CPT1C transfers acyl groups to carnitine for mitochondrial fatty acid import
- CPT1C actually hydrolyzes thioester bonds to depalmitoylate proteins in the ER

This would affect:
1. Any metabolic model simulations involving fatty acid beta-oxidation
2. Predictions for CPT1C knockout phenotypes (would incorrectly predict fatty acid metabolism defects)
3. Drug target modeling (thioesterase vs transferase active sites are structurally different)

**Root cause**: CPT1C was named based on sequence homology to CPT1A and CPT1B, which are bona fide carnitine palmitoyltransferases. However, CPT1C has evolved a distinct function and is now classified as a pseudoenzyme with respect to the canonical CPT1 activity.

### GO Annotation Errors Found

Four IEA/IBA annotations incorrectly attribute ancestral CPT1 functions to CPT1C:

| GO Term | Annotation | Problem |
|---------|------------|---------|
| GO:0016740 | transferase activity | WRONG - CPT1C is a hydrolase |
| GO:0016746 | acyltransferase activity | WRONG - CPT1C lacks this activity |
| GO:0006631 | fatty acid metabolic process (IBA) | WRONG - CPT1C not involved |
| GO:0009437 | carnitine metabolic process (IBA) | WRONG - CPT1C not involved |

**Notably**, the correct NOT annotations already exist:
- NOT GO:0004095 (carnitine O-palmitoyltransferase activity)
- NOT GO:0005739 (mitochondrion)
- NOT GO:0006631 (fatty acid metabolic process)
- NOT GO:0009437 (carnitine metabolic process)

The conflict between positive IBA/IEA and negative ISS annotations reflects the tension between sequence-based inference and experimental evidence.

### Key Literature

1. **PMID:12376098** (Price 2002) - Original cloning, noted low/absent CPT1 activity
2. **PMID:16651524** (Wolfgang 2006) - Energy homeostasis role, malonyl-CoA binding
3. **PMID:25751282** (Rinaldi 2015) - SPG73 disease association, ER localization, ATL1 interaction
4. **PMID:30135643** (Gratacós-Batlle 2018) - KEY: Demonstrated palmitoyl thioesterase activity with catalytic triad Ser-252/His-470/Asp-474

### Disease Association

Mutations in CPT1C cause **Spastic Paraplegia 73 (SPG73)** [MIM:616282]:
- Autosomal dominant
- Pure spastic paraplegia phenotype
- R37C mutation affects N-terminal regulatory domain
- Mechanism involves altered lipid droplet formation and ATL1 interaction

### Alzheimer's Disease Relevance

CPT1C is relevant to AD through:
1. **AMPAR regulation** - CPT1C controls AMPAR trafficking; glutamatergic dysfunction is a feature of AD
2. **Brain-specific expression** - Only CPT1 isoform expressed predominantly in neurons
3. **Energy sensing** - Malonyl-CoA binding couples nutrient status to synaptic function
4. **Lipid metabolism** - Though not classical fatty acid metabolism, CPT1C affects lipid handling

The Recon3D error would incorrectly model CPT1C in fatty acid oxidation pathways rather than its actual role in synaptic receptor regulation.

### Summary of Functional Neofunctionalization

CPT1C represents a striking example of enzyme neofunctionalization:

```
                     CPT1A/CPT1B (mitochondrial)
                     - Carnitine O-palmitoyltransferase (EC 2.3.1.21)
                     - Fatty acid import into mitochondria
Ancestral CPT1 ----{
                     CPT1C (ER)
                     - Palmitoyl thioesterase (EC 3.1.2.22)
                     - Protein depalmitoylation for AMPAR trafficking
```

Despite retaining the carnitine palmitoyltransferase family fold and name, CPT1C has evolved:
- Different cellular localization (ER vs mitochondria)
- Different enzymatic mechanism (hydrolysis vs transfer)
- Different substrate (palmitoylated proteins vs acyl-CoA + carnitine)
- Different biological role (synaptic regulation vs energy metabolism)

---

**Correction (2026-11-23, issue #6783)**

The review carried a `NEW` biological-process row on **GO:0002084 "protein
depalmitoylation"** (IDA, PMID:30135643), and listed the same id under
`core_functions[].directly_involved_in`. That term is **obsolete** in the current
ontology (verified against QuickGO, GO release 2026-11-21, where it resolves as
"obsolete protein depalmitoylation"). GO's obsoletion comment: *"The reason for
obsoletion is that this term represents a molecular function, not a biological
process. Consider instead annotating to the molecular function
'palmitoyl-(protein) hydrolase activity' (GO:0008474)."* There is no `replaced_by`.

Three things were checked before deciding:

1. **The `consider` target is already annotated.** GO:0008474
   palmitoyl-(protein) hydrolase activity is live, and CPT1C already carries it
   twice in GOA — by **IDA from the very same PMID:30135643** (ECO:0000314) and by
   IEA (GO_REF:0000120). Both rows are `ACCEPT` in this review, and GO:0008474 is
   already the review's `core_functions[].molecular_function`. A `NEW` row is by
   definition "a proposed annotation, not one that exists in the existing GO
   annotations", so re-proposing GO:0008474 is not available: it would be a
   duplicate, and CLAUDE.md's `NEW` bar explicitly rejects a term "the gene already
   carries".
2. **The suggested BP fallback is also obsolete.** GO:0098734 "macromolecule
   depalmitoylation", which the old `reason` cited as the broader IEA row that
   GO:0002084 would refine, has *also* been obsoleted in the current release, for
   the same stated reason (*"this term represents a molecular function, not a
   biological process. Consider instead ... 'palmitoyl hydrolase activity'
   (GO:0098599), or, for protein substrates, 'palmitoyl-(protein) hydrolase
   activity' (GO:0008474)"*). Note that this is recent: the 2026-07-26 go-basic
   release still has both terms live (GO:0002084 flagged
   `subset: gocheck_obsoletion_candidate`), and OLS and api.geneontology.org were
   both still serving them as non-obsolete when checked on 2026-11-23. QuickGO,
   on the 2026-11-21 release, is the current source. So "fall back to GO:0098734"
   is not an option either.
3. **No other live BP term states the claim.** The surviving ancestors
   (GO:0035601 protein deacylation, GO:0098732 macromolecule deacylation) are live,
   but asserting one would reintroduce exactly the aspect error GO obsoleted the
   branch to remove — the chemistry CPT1C performs is a molecular function, and the
   biological process it serves is already asserted on this gene as GO:0099072
   regulation of postsynaptic membrane neurotransmitter receptor levels and as the
   `NEW` row GO:1904719 positive regulation of AMPA glutamate receptor clustering
   (both verified live).

**Decision: the `NEW` GO:0002084 row was dropped**, and GO:0002084 was removed
from `core_functions[].directly_involved_in` (leaving GO:0099072 there). Nothing
is lost: the depalmitoylation chemistry is carried by the existing GO:0008474 IDA
row from the same paper, and the biological consequence by GO:0099072 /
GO:1904719. No replacement BP term was invented, and no `proposed_new_terms` entry
was added, because GO's obsoletion was a deliberate decision that this chemistry
belongs in the molecular-function aspect, not an accidental gap.

**Left alone, deliberately:** the *existing* GOA row on GO:0098734 (IEA,
GO_REF:0000108) is still present in `GENE-goa.tsv` and is still `ACCEPT` here.
Per CLAUDE.md, `existing_annotations[].term.id` comes from GOA and is not
rewritten by this review; the obsoletion is upstream GOA's to propagate. Its
`reason` prose ("correctly captures the core molecular function of CPT1C") does
read oddly for a BP-aspect row, and is arguably the same aspect confusion GO
obsoleted the term for — worth revisiting in a review of that row, which is out of
scope for this correction.

## Review follow-up (2026-11-23, PR #6790 round 2)

Reviewer suggestion 7: two rows whose `reason` argued against their own action. Only the
action and reason are the review's own; neither GOA-sourced term id was touched.

- `GO:0003824 catalytic activity` (IEA, GO_REF:0000117) was `ACCEPT` with a reason reading
  "this is a root-level term that provides minimal information". CLAUDE.md forbids
  accepting a term while arguing that it is too general. The action is now `TOO_GENERAL`,
  which is exactly the case the enum describes: the term is true of the gene but
  uninformative because a more specific term asserted elsewhere in this review already
  entails it — `GO:0008474 palmitoyl-(protein) hydrolase activity`, which CPT1C carries by
  IDA from PMID:30135643 (`CPT1C-goa.tsv`, ECO:0000314). `MODIFY` is not used: this row's
  own evidence is an ARBA electronic call that reaches only the root of the
  molecular-function branch, and CLAUDE.md requires a MODIFY to rest on this row's own
  evidence for the deeper term. The action judges the term, not the evidence; the claim is
  not called false.
- `GO:0098734 macromolecule depalmitoylation` (IEA, GO_REF:0000108) is a biological-process
  row whose reason called it "the core molecular function of CPT1C". It stays `ACCEPT` —
  the claim and the aspect are right — and the reason now calls it the core biological
  process, points at `GO:0008474` for the molecular function, and records the earlier
  mislabelling.
