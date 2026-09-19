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
proteins. That is the primary negative functional result. Its cached record is
abstract-only, so the claim is anchored on the PLoS One sentence above rather than quoted
from it.

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

## Decisions

| term | action | why |
|---|---|---|
| GO:0005096 GTPase activator activity (IBA) | REMOVE | catalytic arginine lost before the rodent–primate split; no effect on RAC1/CDC42/RHOA in a systematic screen; the one reported Rho-GTPase effect runs the opposite way and is PKA-mediated |
| GO:0007015 actin filament organization (IBA) | MARK_AS_OVER_ANNOTATED | propagated basis (Arhgap6-style GAP-mediated actin remodelling) does not hold, but an actomyosin link exists via PKAc/RhoA (PMID:41644816), so not contradicted |
| GO:0015629 actin cytoskeleton (IBA, is_active_in) | MARK_AS_OVER_ANNOTATED | four papers localise ARHGAP36 to plasma membrane, endo/lysosomal vesicles, mother centriole and cilium; none to the actin cytoskeleton. Unsupported rather than refuted |
| GO:0007165 signal transduction (IEA) | MODIFY → GO:0045880 | true but maximally general, and supplied by the signature of the domain that does not work. The specific process is well evidenced |
| GO:0004862 cAMP-dependent protein kinase inhibitor activity | NEW | in vitro kinase assay on recombinant PKAC + ITC + cellular FRET; the gene otherwise has no correct MF |
| GO:0005813 centrosome | NEW | PMID:30598432, mother-centriole localisation, Ptc1-dependent, with knockdown control |
