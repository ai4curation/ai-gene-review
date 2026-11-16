# ozpA (GSU2075, UniProt Q74BG6) — Geobacter sulfurreducens PCA

## Starting point

- Q74BG6 is **unreviewed (TrEMBL)**, SubName "Serine protease, subtilase family",
  485 aa. UniProt records **no gene name**, only the ordered locus `GSU2075`; the
  name *ozpA* ("OmcZ protease") was given in the literature (PMID:33837010) and is
  used in the structural work (PMID:36732469), so it is used here and matches the
  folder.
- Features: **signal peptide 1-22**, chain 23-485, a peptidase S8 propeptide/I9
  domain (50-90) and the S8 catalytic domain (124-376), with the subtilisin
  **catalytic triad at 133 (Asp), 169 (His) and 322 (Ser)**. No transmembrane
  segment, no lipid anchor.
- `CC SIMILARITY: Belongs to the peptidase S8 family` — evidence is ARBA plus
  PROSITE-ProRule and RuleBase. The ARBA part is an unvetted prediction and is not
  citable as support, but PROSITE-ProRule and RuleBase are curated UniRule systems
  and are, so the family membership can be cited.
- CDD `cd07477 Peptidases_S8_Subtilisin_subset`; eggNOG COG1404.
- **GOA has 5 rows** (`ozpA-goa.tsv`, 2026-11-15), and none of them is about what
  OzpA is actually known to do.

## Why this gene

OzpA is the last piece of the OmcZ story reviewed in this repository
(`genes/GEOSL/omcZ`). OmcZ is made as a 50 kDa precursor that cannot polymerise;
OzpA cuts it to the 30 kDa filament-forming form. Without that cut there are no
OmcZ nanowires and no high-density current.

## Biology, with provenance

### The one characterised function
- An *ozpA* disruption mutant produces as little current as an *omcZ* mutant, and
  biochemically it accumulates the precursor and makes none of the mature form
  [PMID:33837010 "the ozpA mutant accumulated OmcZL and did not produce OmcZS, which is thought to be a mature form that is essential for the extracellular electron transfer to the electrode"].
- The cleavage is OzpA's own: a lysate from *E. coli* expressing OzpA cuts OmcZL
  [PMID:33837010 "A heterologous expression system cell lysate from an Escherichia coli strain producing OzpA cleaved OmcZL and generated OmcZS as the proteolytic product."],
  and purified OzpA does it to both native and recombinant substrate, after which the
  product self-assembles
  [PMID:36732469 "We found that purified OzpA cleaves both native and recombinant OmcZ50 into OmcZ30 which then self-assembled into nanowires"].
- The authors' own summary of the role
  [PMID:33837010 "These results indicate that OzpA is an essential protease for current production via the maturation of OmcZ"].
- An AlphaFold model of the complex places OzpA's catalytic triad against the loop
  that is cut [PMID:36732469 "Our model of OzpA placed the catalytic triad (His, Asp and Ser) of OzpA near Asn 258"].
  That is a model, not a structure, and is cited as corroboration only.

### Where it acts
- Only the culture supernatant fraction carries OmcZL-cleaving activity
  [PMID:33837010 "only the culture supernatant protein fraction showed OmcZL cleavage activity, indicating that the mature form of OmcZ, OmcZS, can be produced outside the cells"].
- Gu et al. state OzpA "is predicted to localize primarily in the outer-membrane and
  extracellular space" (PMID:36732469) — a prediction, not a measurement.
- **No cellular-component row is proposed.** The signal peptide shows OzpA is
  exported and the supernatant result shows the activity is outside, but neither
  discriminates between free in the extracellular region and attached at the cell
  surface, and `GO:0005576` is explicitly reserved for products *not* attached to the
  surface. Two lines agreeing on "outside" do not pick the term. Recorded as a
  question and an experiment instead.

### Operon context
*omcZ*, *ozpA* and a peptidyl-prolyl cis-trans isomerase (GSU2074) are co-transcribed
(PMID:36732469), and OmcZ-family gene clusters carry a serine peptidase across
bacteria and archaea, including in the ANME nanowire work — so the protease is part
of the conserved maturation module, not a *Geobacter* peculiarity.

## Annotation decisions

Existing (5 rows). The GOA set is a pure family-signature stack: everything traces to
the subtilisin S8 domain, nothing to OzpA's own literature.

- `GO:0004252` serine-type endopeptidase activity, IBA → **ACCEPT**. The right MF, and
  now backed by OzpA's own evidence: it makes an internal cut in OmcZ50, which is
  endopeptidase chemistry, and the S8 triad is present.
- `GO:0004252`, IEA → **ACCEPT**, consistent with the IBA row.
- `GO:0008236` serine-type peptidase activity, IEA → **ACCEPT**. Entailed by the above
  but respectably specific on its own — it names the catalytic chemistry — and the
  2026-11-14 maintainer ruling keeps such terms rather than calling them TOO_GENERAL.
  MODIFY is not available either: this row's evidence is IPR000209, a domain shared by
  endo- and exo-peptidases, which cannot reach the deeper term.
- `GO:0008233` peptidase activity, IEA (ARBA) → **TOO_GENERAL**. This one *is*
  imprecise on its own — which peptidase? — and `GO:0004252` is asserted in the same
  review.
- `GO:0006508` proteolysis, IEA → **ACCEPT**. True, and a substantive process claim
  rather than an uninformative one, even though the NEW row below is its descendant.

New (1 row):
- `GO:0016485` protein processing — **IDA**. "Any protein maturation process achieved
  by the cleavage of a peptide bond or bonds within a protein" is exactly the
  OmcZ50 → OmcZ30 cut, shown on purified protein and corroborated by the mutant.

Deliberately **not** added, and this is the interesting part:

- **No extracellular electron transfer or current-production process term.** Deleting
  *ozpA* costs the cell its current, which makes OzpA *necessary* for EET — and
  necessity is not participation. OzpA transfers no electrons; it cuts a peptide bond
  in the protein that does. This is the substrate/participation distinction the
  repository's `NEW` guidance is built around, and OzpA is on the wrong side of it
  for an EET term, however strong the knockout phenotype.
- **No protein polymerization term.** OmcZ polymerises; OzpA removes the domain that
  was blocking it. Licensing a process is not performing it. (`GO:0051258` is on the
  OmcZ and OmcS reviews, where the protein really is the polymer.)
- **No cellular-component row**, for the reason given above.

## Ontology note

Nothing here needs a change to an existing term: `GO:0016485` fits exactly.

The one existing-term problem this family's reviews surfaced is in the ImcH review and
concerns `GO:0008121`'s transporter parents. It was briefly recorded there as two
structured `EDGE_DELETION` requests; those were **withdrawn** after checking the term
itself. `GO:0008121` is cross-referenced to `EC:7.1.1.8` and `RHEA:11484`, and EC class 7
is the translocases, created for vectorial reactions; with a definition that opens
"Enables the transfer of a solute or solutes from one side of a membrane to the other",
the transporter parents are the term's identity rather than an accident inherited from
the cytochrome bc1 archetype. Deleting them would leave the term contradicting its own
definition and both reaction cross-references. The coherent request is the separate
electroneutral term the ImcH review already asks for in `proposed_new_terms`, so that is
now the only live upstream ask, and the parentage is recorded as a question rather than a
change request.

## On the declined cellular-component row

Checked rather than assumed, after the claim was challenged in review: `GO:0005576`
extracellular region does carry the comment "Note that this term is intended to annotate
gene products that are not attached to the cell surface. For gene products at the cell
surface, consider annotating to external side of plasma membrane ; GO:0009897."
(QuickGO, 2026-11-16). So the stated reason for declining the row stands — the term turns
on surface attachment, which the evidence does not resolve.

The review's wording did understate what PMID:33837010 did, though, and is now corrected.
That work compared three fractions, not one, and found OmcZL-cleaving activity in the
supernatant alone, which excludes an intracellular location and a loosely attached
surface one. What remains open is narrower: activity in a fraction is not protein in a
fraction, and a *tightly* attached surface protein would not shear into a loosely bound
fraction either. That is the gap the suggested experiment now addresses by following the
protein rather than the activity, and by adding protease accessibility on intact cells.
