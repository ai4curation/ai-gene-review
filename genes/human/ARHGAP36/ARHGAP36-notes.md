# ARHGAP36 (Q6ZRI8) — curation notes

Journal for the PAINT-campaign review of human ARHGAP36. Appended to as work proceeded.

## The shape of the problem

ARHGAP36 has **four** GO annotations and **none of them is experimental**:

| term | aspect | evidence | reference | with/from |
|---|---|---|---|---|
| GO:0005096 GTPase activator activity | F | IBA | GO_REF:0000033 | MGI:MGI:1196332, PANTHER:PTN000973894 |
| GO:0007015 actin filament organization | P | IBA | GO_REF:0000033 | same |
| GO:0015629 actin cytoskeleton | C | IBA | GO_REF:0000033 | same |
| GO:0007165 signal transduction | P | IEA | GO_REF:0000002 | InterPro:IPR000198 |

`MGI:MGI:1196332` resolves to **mouse Arhgap6**, not to anything ARHGAP36-specific
(checked at informatics.jax.org: "Arhgap6 MGI Mouse Gene Detail - MGI:1196332 - Rho GTPase
activating protein 6"). The PAINT record in this repo
(`interpro/panther/PTHR12635/PTHR12635-paint.tsv`) shows all three IBD rows placed on node
`PTN000973894` at `taxon:6072` — **Eumetazoa** — seeded by that one mouse gene.

Subfamily assignment from `interpro/panther/PTHR12635/PTHR12635-entries.csv`:

- ARHGAP36 (Q6ZRI8, human) and Arhgap36 (mouse) → `PTHR12635:SF8` "RHO GTPASE-ACTIVATING PROTEIN 36"
- ARHGAP6 (O43182 human, O54834 mouse) → `PTHR12635:SF6` "RHO GTPASE-ACTIVATING PROTEIN 6"

So the whole molecular-function claim on this gene is one PAINT curator's judgment that
GAP activity was present in the Eumetazoan ancestor of PTHR12635, propagated into a
different subfamily from the one that was assayed.

Meanwhile the literature on this gene is substantial and is about something else entirely.

## The arginine finger

UniProt annotates `FT SITE 258 /note="Arginine finger; crucial for GTP hydrolysis by
stabilizing the transition state" /evidence="ECO:0000255|PROSITE-ProRule:PRU00172"` and
asserts `FUNCTION: GTPase activator for the Rho-type GTPases by converting them to an
inactive GDP-bound state. {ECO:0000250}`.

Position 258 of Q6ZRI8 is a **threonine**. Context 248..268 is `KHGLSAVGIFTLEYSVQRVRQ`.

Verified independently and reproducibly in `ARHGAP36-bioinformatics/` (see `RESULTS.md`):

- Three controls that carry their own annotated arginine finger — ARHGAP1/p50RhoGAP
  (Q07960, R282; resolved in the 1TX4 transition state), mouse Arhgap6 (O54834, R435, the
  PAINT seed itself) and human ARHGAP6 (O43182, R433) — **all three project onto ARHGAP36
  position 258**, agreeing with UniProt's own Site. Each control also recovers every other
  control's annotated finger, so the projection method is not being trusted on faith.
- **Escape test:** the nearest arginine to 258 is at 265, an offset of 7. Not a register
  shift.
- **The mouse ortholog shares the substitution.** Mouse Arhgap36 (B1AUC7, same subfamily
  SF8) carries T at its own annotated Site 246; human 258 and mouse 246 project onto each
  other reciprocally. The arginine was therefore gone before the rodent–primate split —
  far below the Eumetazoan node the IBD sits at.
- Across all 66 reviewed human PROSITE-`PS50238` proteins, 60 hold R at the annotated
  finger and 6 do not; ARHGAP36 is one of the 6, alongside OCRL and ARAP2.

Three published records name this same residue in three different numberings, and all
three fall out of the splice-variant arithmetic:

- UniProt canonical isoform 1: **T258**
- [PMID:33999959 "the site that is structurally equivalent to the arginine finger (Thr227)
  is shown in blue"] → isoform 2 numbering (`VSP_021358`, −31 → 227)
- [PMID:25024229 "The replacement of this structural element with a threonine (T246)"] →
  mouse canonical numbering (B1AUC7, 590 aa)

## What the literature says about GAP activity

Two primary papers from the ARHGAP36 field state it directly, and both are full-text in
the cache:

- [PMID:25024229 Rack et al. 2014 PNAS "Arhgap36-dependent activation of Gli transcription
  factors", "it lacks the “arginine finger” motif that participates in Rho GTPase activity
  ( 25 ). The replacement of this structural element with a threonine (T246) suggests that
  catalytic GAP domain function may not be required for Arhgap36-induced Gli activation."]
- [PMID:33999959 Chen lab 2021 PLoS One, "However, the GAP-like region in ARHGAP36 lacks
  the “arginine finger” motif conserved in catalytically active homologs [7, 24], and
  ARHGAP36 has no effect on the activities of Rac1, Cdc42, and Rho A [25]. In addition,
  ARHGAP36 residues that are structurally equivalent to those previously associated with
  GTP hydrolysis are not required for ARHGAP36-mediated Gli activation [7]."]

Reference `[25]` in that PLoS One sentence resolves (from the journal's own bibliography
at journals.plos.org, DOI 10.1371/journal.pone.0251684) to **Müller et al. 2020 Nat Cell
Biol 22:498–511, PMID:32203420** — a systems-level screen of RhoGEF/RhoGAP regulatory
proteins. That is the primary negative functional result.

### Reading Müller 2020 first-hand, despite the paywall

The article is **not open access** (Europe PMC: no PMC id, `isOpenAccess: N`,
`inEPMC: N`), so the cached record is abstract-only and nothing from it can be used as
`supporting_text`. But the **supplementary workbook is freely downloadable** from
Springer. `ARHGAP36-bioinformatics/scan_muller_supplementary.py` fetches it and reads the
row, so the review's central functional claim is first-hand and re-derivable rather than
a chain of citations.

**Supplementary Table 2**, "RhoGEF/RhoGAP specificities identified in this study and in
the literature", activity-screen columns:

| gene | RhoA | Rac1 | Cdc42 | |
|---|---|---|---|---|
| **ARHGAP36** | **−** | **−** | **−** | query |
| ARHGAP35 | + | + | − | control |
| ARHGAP1 | + | − | + | control |
| ARHGAP17 | − | − | − | control |

**Supplementary Table 1**, the cDNA library: ARHGAP36's entry records
`GEF or GAP (or GAP-like)` = **"GAP-like (arginine finger missing)"** — the authors' own
domain call, an independent expert judgment — and `Comments` = **"human isoform2"**,
517 aa, species Human. That rules out the obvious objection that an inactive splice
variant was screened: isoform 2 is the functionally active one in every Hedgehog assay.

**How much is a negative worth here? Counted, not assumed.** 15 of the 65 scorable GAP
rows are negative for all three GTPases (23%), and **ARHGAP17/RICH1, a characterised
Cdc42 GAP, is one of them** — so the screen has false negatives and a single negative
call is not a refutation on its own. This is stated in the review rather than hidden.

What makes ARHGAP36's negative count is that it agrees with an independent measurement.
Of the six reviewed human PROSITE-`PS50238` proteins whose annotated arginine-finger
position does not hold an arginine (derived in `results.json`, not restated) and that
appear in the screen — ARAP2, ARHGAP36, DEPDC1B, FAM13B, INPP5B, OCRL — **four are
all-negative**: ARHGAP36, DEPDC1B, INPP5B, OCRL. Against a 23% base rate that is a clear
enrichment. Two of the six are *not* all-negative, which is the same decoupling lesson
the ARHGAP11B review drew, and the reason the review does not rest on the residue alone.

Reference `[24]` is Scheffzek/Ahmadian/Wittinghofer 1998 on the arginine-finger mechanism;
`[28]` is **Amin et al. 2016 JBC, PMID:27481945**, a systematic survey of all 66 human
RHOGAP-domain proteins. Its abstract states that of 66 human RHOGAPs "57 have a common
catalytic domain capable of terminating RHO protein signaling". Its body (read at
PMC5034035; the cached record is abstract-only so this is **not** quoted in the review)
carries the section heading "Not all RHOGAP Domain-containing Proteins Are GAPs" and the
sentence: "A first inspection of the sequence alignment of the 66 RHOGAP domains revealed
that ARHGAP36, CNT-D1, DEP1, DEP2, FAM13B, INPP5P, and OCRL1 lack an arginine finger at
the corresponding position (supplemental Fig. S1). These proteins have serine, threonine,
or glutamine instead and thus cannot substitute for the arginine function."

And a third-party restatement, full-text cached:
[PMID:40378841 Kaelin et al. 2025 Curr Biol, "Arhgap36 functioned not as a Rho GTPase
inhibitor but as an inhibitor of PKA signaling by directly binding the catalytic subunit
of PKA (PKAC) and targeting it for lysosomal degradation."]

### MGI has already said the molecular function is unknown

Checked late, and it should have been checked first. Mouse Arhgap36 (MGI:MGI:1922654,
UniProtKB:B1AUC7) has seven GO annotations:

| term | evidence | reference |
|---|---|---|
| GO:0007224 smoothened signaling pathway | IMP (`acts_upstream_of_or_within`) | PMID:31305241 |
| GO:0021525 lateral motor column neuron differentiation | IMP | PMID:31305241 |
| **GO:0003674 molecular_function** | **ND** | **GO_REF:0000015** |
| GO:0005096 GTPase activator activity | IBA | GO_REF:0000033 |
| GO:0007015 actin filament organization | IBA | GO_REF:0000033 |
| GO:0007165 signal transduction | IEA | GO_REF:0000002 |
| GO:0015629 actin cytoskeleton | IBA | GO_REF:0000033 |

GO_REF:0000015 is "Use of the ND evidence code for Gene Ontology (GO) terms": a direct
annotation to a root term with ND records that a curator searched and found no data
supporting anything more specific. So MGI states that Arhgap36's molecular function is
unknown, in the same annotation set where the phylogenetic pipeline states that it is a
GTPase activator. The contradiction this review resolves is already visible in GO's own
data, on the ortholog, and is not a human-specific artefact.

The same table gives the MODIFY its precedent: the ortholog already sits in the
Smoothened branch by IMP, from the same paper this review cites.

Read 2026-09-19 from **two independent services that agree** — QuickGO
(`/QuickGO/services/annotation/search?geneProductId=UniProtKB:B1AUC7`) and
`api.geneontology.org/api/bioentity/gene/MGI:MGI:1922654/function`. An attempt to read
the MGI marker page through WebFetch returned a GO-slim category list rather than the
annotations and was discarded; it is the second time in this session that WebFetch
returned confident, wrong page content (the first was a bibliography for an unrelated
article), so neither reading is relied on anywhere.

### The one thing that points the other way

UniProt records `SUBUNIT: May interact (via the Rho-GAP domain) with the active form of
RAC1. {ECO:0000269|PubMed:35986704}`. The cached PMID:35986704 record is abstract-only and
the abstract does not mention RAC1, so I cannot check what the experiment was. This does
not conflict with loss of catalysis: Amin et al. give OCRL as exactly this case ("OCRL1
has been shown to interact with GTP-bound RAC1 without the stimulation of its
hydrolysis"), and OCRL sits beside ARHGAP36 in the list of arginine-finger-less RHOGAPs.
The bioinformatics run makes the same point quantitatively: 8/25 of the 1TX4 GAP:GTPase
interface positions are identical in ARHGAP36 against 9/25 in mouse Arhgap6, i.e. the
binding surface is about as conserved as the catalysing family member's while the
catalytic residue is not.

**This is why the review distinguishes REMOVE from MARK_AS_OVER_ANNOTATED.** `GO:0005096
GTPase activator activity` is about accelerating hydrolysis, and that is contradicted. A
binding claim is not, and is not being removed — there is no such annotation to remove.

## What ARHGAP36 actually does

The consistent finding across six primary papers is that ARHGAP36 is a **pseudosubstrate
inhibitor of the PKA catalytic subunit**, and that this is how it activates Gli.

- [PMID:27713425 Eccles et al. 2016 Nat Commun "Bimodal antagonism of PKA signalling by
  ARHGAP36", "These experiments demonstrate the direct interaction between ARHGAP36 and
  PKAC, mediated by a pseudosubstrate motif on ARHGAP36."] The inhibition is measured on
  purified components: ["First, we performed an in vitro kinase assay with recombinant
  PKAC. Addition of 36i peptide strongly reduced the fraction of phosphorylated PKA
  substrate (Fig. 3a). A similar extent of kinase inhibition was achieved with equal
  concentrations of PKI (5–24) peptide."] and concluded ["The above experiments
  collectively demonstrate that ARHGAP36 is a pseudosubstrate inhibitor of PKAC with
  potency comparable to PKI."] The motif maps to the N-terminal arginine-rich region
  (R153/R154), **not** to the GAP domain.
- [PMID:25024229] identified Arhgap36 in a genome-scale cDNA screen as a positive
  regulator of the Hh pathway acting Smo-independently, inhibiting Gli repressor formation
  and promoting activation of full-length Gli.
- [PMID:42405753 eLife 2026, "Arhgap36 depletes the levels of PKA and its catalytic
  subunit PKAC, both strongly activating Hh signaling and making signal transduction less
  dependent on regulation via Smoothened."]
- [PMID:30598432 PNAS 2019, "We find that Patched1 interacts with and stabilizes the PKA
  negative regulator ArhGAP36 to the centrosome. Activating the Shh pathway results in the
  removal of ArhGAP36 from the mother centriole and the centrosomal PKA accumulation."]
- [PMID:31305241 eLife 2019] places ARHGAP36 downstream of Shh in lateral motor column
  neuron specification.
- [PMID:40378841] gives the in vivo readout in a non-model organism: melanocyte-specific
  Arhgap36 expression lowers PKAC and shifts cat pigment synthesis to pheomelanin.

### A sign complication worth not papering over

The papers do not all point the same way at the level of individual steps. Rack 2014 and
Eccles 2016 use overexpression and see increased Gli output. PMID:30598432 looks at the
endogenous centrosomal pool and finds that ARHGAP36 sitting at the mother centriole keeps
centrosomal PKAc low, which *prevents* Inversin phosphorylation and *restrains* Smoothened
ciliary translocation — ["we knocked down ArhGAP36 in WT cells and found that ArhGAP36
knockdown significantly increased the protein level of PKAc and pInvs"]. PKA has opposing
roles in the pathway (Gli repressor formation vs Inversin/Smo trafficking), so ARHGAP36
inhibiting PKA is negative on one arm and positive on the other. Every paper measuring
pathway **output** (Gli1 levels, Gli reporters, ventral cell fates) reports an increase.
The review takes the output-level claim and records the step-level complication in the
annotation's reason rather than hiding it.

## A GO expressivity gap

The function that is actually well supported — positive regulation of Gli-dependent
transcription, acting downstream of and largely independent of Smoothened — has no clean
GO term. Checked on **two independent services**:

- OLS4 (via the OLS MCP) and QuickGO's ontology search both return the same set: every
  active GO BP term for this pathway is anchored on Smoothened (`GO:0007224 smoothened
  signaling pathway` — "The series of molecular signals generated as a consequence of
  activation of the transmembrane protein Smoothened" — and its regulation children). GO
  has no non-Smoothened Hedgehog pathway term.
- The two terms that *would* have fitted are obsolete: `GO:0007228` ("obsolete positive
  regulation of hh target transcription factor activity") and `GO:1990787`. Obsolescence
  confirmed on the GO API (definition begins "OBSOLETE.") and on QuickGO (label prefixed
  "obsolete"), and they are absent from OLS4's active index.

So `GO:0045880 positive regulation of smoothened signaling pathway` is the closest
available term. Its 98 human annotations already include downstream/Gli-level regulators
(STK36, CDK1, MAPK1, GAS1, EVC), so using it for a downstream regulator is precedented.

## Proposed molecular function

`GO:0004862 cAMP-dependent protein kinase inhibitor activity` — "Binds to and stops,
prevents or reduces the activity of a cAMP-dependent protein kinase" (verified on the GO
API and OLS4). Comparator check: the term's 54 human annotations are carried by the PKI
pseudosubstrate family (PKIA, PKIB, PKIG), the PKA regulatory subunits (PRKAR1A/1B/2A/2B),
PJA2 and PPP1R1B — i.e. precisely the class of "binds PKAC and blocks its catalytic
activity". Eccles 2016 compared ARHGAP36's 25-aa peptide against PKI(5–24) in the same
assay and got a similar extent of inhibition. This is the informative MF that GOA is
currently missing entirely, and it is the reason `protein binding` would be the wrong way
to record the PKAC interaction.

## Provider gates and what affinage missed

`ARHGAP36-deep-research-affinage.md` was fetched with
`projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ARHGAP36 --accession Q6ZRI8`.
No blocking gate tripped (accession and organism both check out). The soft gate did:
Affinage's own head-to-head self-evaluation scored this record `pairwise = tie`, not
`win`, against the curated UniProt reference. Recorded in the review's `reference_review`.

The record is good on the Hedgehog/PKA biology. Its 7 citations are a subset of the 27
PubMed hits for `ARHGAP36[Title/Abstract]`. The ones it missed that mattered:

- **PMID:27481945** (Amin 2016) and **PMID:32203420** (Müller 2020) — the two papers that
  settle the GAP question. Neither title contains "ARHGAP36"; one is about RHOGAP family
  systematics and the other about RAC1 signalling at integrin adhesions.
- **PMID:35986704** — the *only* functional reference in the UniProt entry, and the source
  of the RAC1 interaction. Its title names a disease.
- The published versions of two records affinage cited only as preprints without PMIDs:
  **PMID:40378841**/**PMID:40378840** (cat coat colour, Curr Biol 2025) and
  **PMID:42405753** (FOXC1, eLife 2026).
- **PMID:37813867**, an Author Correction to PMID:37041138.

The UniProt `RN` list turned out to be the cheapest place to find the first of these: it
has only five references, four of which are large-scale sequencing projects, and the fifth
is PMID:35986704.

## `just validate` is not the only gate: `just validate-families` checks gene residue claims

Learned from a CI failure on PR #3079, and worth recording because the name does not
suggest it. `just validate human ARHGAP36` was green through every round; **`just
validate-families` was not**, and it is what runs
`ai_gene_review.validation.gene_residue_claims` over the gene corpus:

```
[FAIL] TARGET_IDENTITY ARHGAP36 GO:0005096:
       target accession UniProtKB:B1AUC7 is not this gene (Q6ZRI8)
```

The rule is at `src/ai_gene_review/validation/gene_residue_claims.py:148-159`: a
`residue_claim`'s **`target` must be this gene's own protein**. The `anchor` may be any
comparator, but the target may not. That matches `ResiduePosition`'s own wording in the
schema — "the corresponding position in **this gene's** own protein" — which I had read
and still got wrong, because the mouse-ortholog claim was too convenient a place to put a
cross-species measurement.

The second residue claim had anchored on mouse Arhgap6 (O54834 R435) with mouse *Arhgap36*
(B1AUC7 T246) as target, to make the "loss predates the rodent–primate split" argument
machine-checkable. It is now re-pointed to the same anchor with **this gene** as target
(Q6ZRI8 T258), which keeps the PAINT-donor comparison checkable and satisfies the rule.
The dating argument is not expressible as a residue claim at all — it is about a different
protein — so it stays in `review.reason` and in `RESULTS.md` section 4c, where it is
reproducible.

Before/after, both run locally:

```
# committed (broken) version
exit=1  [FAIL] TARGET_IDENTITY ...   6 pass, 1 fail, 0 unresolved
# fixed version
exit=0                                6 pass, 0 fail, 0 unresolved
```

**For the next gene: run `just validate-families` too whenever a review carries
`residue_claims`.** It takes far longer than `just validate` (it walks 244 family reviews
first), but the gene-level residue check can be run alone in seconds:

```
uv run python -m ai_gene_review.validation.gene_residue_claims \
    genes/human/<GENE>/<GENE>-ai-review.yaml
```

## Decisions

| term | action | why |
|---|---|---|
| GO:0005096 GTPase activator activity (IBA) | REMOVE | catalytic arginine lost before the rodent–primate split; no effect on RAC1/CDC42/RHOA in a systematic screen; the one reported Rho-GTPase effect runs the opposite way and is PKA-mediated |
| GO:0007015 actin filament organization (IBA) | MARK_AS_OVER_ANNOTATED | propagated basis (Arhgap6-style GAP-mediated actin remodelling) does not hold, but an actomyosin link exists via PKAc/RhoA (PMID:41644816), so not contradicted |
| GO:0015629 actin cytoskeleton (IBA, is_active_in) | MARK_AS_OVER_ANNOTATED | four papers localise ARHGAP36 to plasma membrane, endo/lysosomal vesicles, mother centriole and cilium; none to the actin cytoskeleton. Unsupported rather than refuted |
| GO:0007165 signal transduction (IEA) | MODIFY → GO:0045880 | true but maximally general, and supplied by the signature of the domain that does not work. The specific process is well evidenced |
| GO:0004862 cAMP-dependent protein kinase inhibitor activity | NEW | in vitro kinase assay on recombinant PKAC + ITC + cellular FRET; the gene otherwise has no correct MF |
| GO:0005886 plasma membrane | NEW | PMID:27713425, human Q6ZRI8-2, IDA; corroborated across isoforms by PMID:33999959 |

**`GO:0005813 centrosome` was considered and dropped.** An earlier draft of this table
listed it as a NEW row on the strength of PMID:30598432 — mother-centriole localisation,
Patched1-dependent, with a knockdown control, which is the best-characterised localisation
this protein has. It was dropped when the cell systems were checked: that work is in mouse
cells (`Ptc1 +/−` and `Ptc1 −/−` lines), so an IDA on the *human* gene would assert a human
experiment that was not performed. `GO:0005886` was proposed instead because PMID:27713425
states in its methods that the construct is human `Q6ZRI8-2`. The centrosome is raised in
`suggested_questions` as a candidate for a separate ortholog-based annotation rather than
asserted here. The row above records the decision actually taken; this paragraph records
the one that was not, so the table is not read as the outcome.


## Full re-review, 2026-09-20/21

All six rows reviewed; four original source assertions and two authored NEW rows preserved. Restore actin organization and actin cytoskeleton from MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE. New accessible primary [PMID:41644816] Fig.8A and supplementary S6-S8 directly establish a contextual actin-associated pool and target-dependent polarized F-actin/pMLC2 distribution. Public primary figures and complete supplementary legends were read; the main text remains embargoed. Loss of catalytic GAP activity does not remove these separate functions or require the same donor mechanism. Details and URLs are in ARHGAP36-primary-evidence.md.

Re-read the existing bioinformatics results and re-executed the primary32203420 workbook parser. Retain catalytic REMOVE based on convergent residue and cellular-screen evidence, while correcting the claim that 15/65 all-negative is a false-negative rate and that an ND root annotation contradicts IBA. Added current sequence versions to the residue claims. Exact target PTN002489201 descends from positive IBD PTN000973894. No wrong-paralog failure is asserted simply from differing subfamilies. Retain the existing signaling refinement and two direct NEW inhibitor/location proposals; no additional NEW rows. Corrected universal isoform-inactivity and no-experiment claims. No focused provider call is needed after the primary supplementary evidence resolves the actin issues; an exact ARHGAP36/Q6ZRI8 global OpenScientist cache search was negative.
