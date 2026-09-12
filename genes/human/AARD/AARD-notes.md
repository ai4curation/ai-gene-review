# AARD (alanine- and arginine-rich domain-containing protein, C8orf85) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AARD-deep-research-affinage.md`, gates passed) plus UniProt Q4LEZ3, the GOA TSV and the
primary literature.

## The darkest gene in this campaign so far

AARD's entire GO record is **15 rows, every one of them `GO:0005515 protein binding`, all IPI,
all from a single publication** (PMID:32296183, the HuRI binary interactome). The 15 rows differ
only in their WITH/FROM partner, so the seeder correctly collapses them to one
`existing_annotations` entry with 15 interactors behind it. There is **no molecular function
beyond binding, no cellular component, and no biological process**. UniProt has no FUNCTION
line, no SUBCELLULAR LOCATION, and only two keywords ("Proteomics identification", "Reference
proteome").

Affinage agrees there is nothing to ground: its `mechanism_profile` reports
`molecular_activity: (none)`, `localization: (none)`, `partners: (none)`, and the narrative ends
by saying so explicitly — "no molecular activity, interaction partners, or cellular function for
AARD have been characterized in the available corpus".

So the whole review turns on one question: **should those 15 interactions be believed?**

## Testing the interactions rather than asserting

Rather than dismiss them by the usual argument (single publication, no follow-up), I tested a
specific, falsifiable alternative explanation — **coiled-coil bias**. Sticky or self-activating
preys in yeast two-hybrid are enriched for coiled-coil proteins, which associate promiscuously
through heptad-repeat surfaces. `AARD-bioinformatics/analyze_partners.py` reads the accessions
straight out of `AARD-goa.tsv` and fetches UniProt features at run time.

**Result: 7 of 15 partners (47%) carry a coiled-coil FEATURE.** Against a background of
**2059 / 20431 reviewed human proteins with that feature (10.1%)**, fetched from UniProt for the
purpose, that is a **4.6-fold enrichment**, binomial P(X≥7 | n=15, p=0.101) = **3.3×10⁻⁴**.
Numerator and denominator deliberately use the same criterion: two more partners (KRT24, KRT27)
carry only the *Coiled coil* KEYWORD, which is assigned more liberally than the feature, so
scoring them against a feature-only background would inflate the result. On the consistent
feature-or-keyword pair it is 9/15 against a 10.6% keyword background — **5.6-fold**,
P = 4.8×10⁻⁶ — the same conclusion either way. With n=15 this is a
descriptive statistic rather than a controlled test — the ideal comparison would be against
other single-publication prey sets from the same screen — but the enrichment is now *measured*
rather than asserted.

The partners also span **14 top-level subcellular compartments**:

| Partner | Coiled-coil segments | Where it lives |
|---|---|---|
| GRIPAP1 | 4 | endosome membranes |
| CEP57 | 2 | centrosome |
| STX1A, STX2, STX5 | 1 each | synaptic vesicle / cell membrane / Golgi + ERGIC |
| KIAA0753, CENPQ | 1 each | centriolar satellite / centromere |
| KRT24, KRT27 | keratins | cytoskeleton |
| TFIP11, NTAQ1, LMO4, MAGEB4, VPS37C, TSGA10 | — | nucleus, cytosol, secreted, late endosome |

**Three syntaxins** — STX1A, STX2 and STX5 are SNAREs from three different membranes that share
a coiled-coil SNARE motif. **Two keratins.** Plus centrosomal and centromeric coiled-coil
proteins, a nuclear splicing factor, and a secreted protein. There is no compartment where these
could plausibly meet, and the shared feature across them is architecture, not biology.

That is the artefact signature, and it is a much stronger argument than "no follow-up". Action:
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE` — the physical interactions may well have occurred
in the assay, and I have no positive evidence that any individual pair is false.

**A general trap worth recording.** When a null model is built by querying the same database
that supplies the numerator, the background query must use the **identical predicate**. Here the
numerator counted coiled-coil on feature-OR-keyword while the background query was feature-only
(`ft_coiled:*`) — and since UniProt applies the keyword more liberally than the positional
feature, the mismatch inflated the enrichment (6.0× reported where like-for-like is 4.6×). The
fix is not to pick one criterion but to compute each numerator against its own matching
denominator, which also shows the conclusion is robust to the choice.

## The family route is closed too — but it exists

I originally wrote that AARD has "no recognisable domain beyond the compositional
alanine/arginine-rich description". **That was wrong**, and contradicted by the gene's own
UniProt file, which I had already read:

```
DR   InterPro; IPR051771; FAM167_domain.
DR   PANTHER; PTHR32289:SF2; ALANINE AND ARGININE-RICH DOMAIN-CONTAINING PROTEIN; 1.
DR   PANTHER; PTHR32289; PROTEIN FAM167A; 1.
```

AARD is a **FAM167-family** protein, sharing PANTHER `PTHR32289` with FAM167A and FAM167B. For
a gene this dark, paralogs are the most tractable remaining inference route, so it mattered.

Enumerating the family (now part of the analysis script): **10 reviewed members across 5
species, and not one carries a UniProt FUNCTION statement.**

| Entry | Organism | FUNCTION |
|---|---|---|
| AARD_HUMAN, AARD_MOUSE, AARD_RAT | human/mouse/rat | — |
| F167A_HUMAN, F167A_MOUSE, F167A_BOVIN, F167A_DANRE | 4 species | — |
| F167B_HUMAN, F167B_MOUSE | human/mouse | — |
| CT202_HUMAN | human | — |

So guilt-by-association is unavailable — **not because AARD lacks a family, but because the
entire family is uncharacterised.** That is a far stronger statement than "no family", and it is
independently corroborated by UniProt's own PAN-GO line:
`PAN-GO; Q4LEZ3; 0 GO annotations based on evolutionary models`.

It also raises a better question than any about AARD alone: this is a conserved vertebrate
family, present in fish through mammals, in which *no member* has a described function. Solving
any one of them would likely illuminate the rest, and no member is currently a better starting
point than another.

## What is actually known about AARD

Only expression biology, and only in mouse:

- Expression is **Sertoli-cell specific**, up-regulated during testis differentiation
  [PMID:17486547, "The period of elevated mRNA expression coincides with early
  differentiation of the testis and is limited to Sertoli cells of the developing
  testis cords."]
- It is a **direct androgen receptor target gene**
  [PMID:27959439, "The present study identified Aard as a gene
  that is directly regulated by AR in mouse SCs, which is important in
  spermatogenesis."]

**Neither supports a GO annotation for AARD.** This is precisely the A1BG situation from earlier
in this campaign (PR #2217): being a *transcriptional target of* a pathway is a downstream
relationship, not participation in it. Annotating AARD to androgen-receptor signalling would
repeat exactly the `ROLE_CONFLATION` error I found in the mouse *A1bg* GH annotation. Recorded
in the description and `suggested_questions`; not annotated.

## Outcome

**No `NEW` terms proposed.** AARD stays dark, and that is the correct result. The value added by
this review is:

1. Evidence-based grounds for discounting the only annotations the gene has.
2. An explicit record that the expression/AR biology must not be converted into process terms.
3. Targeted experiments aimed at the actual gap.

| Term | Evidence | Action |
|---|---|---|
| `GO:0005515` protein binding (×15 partners, one publication) | IPI | MARK_AS_OVER_ANNOTATED |

## Note on annotation coverage

The GOA file has 15 rows but `existing_annotations` has one entry. That is not missing coverage:
all 15 rows carry the identical term, qualifier, evidence code and reference, differing only in
WITH/FROM, so they are one annotation supported by 15 interactors. All 15 are named and analysed
in the review summary and in the bioinformatics results.
