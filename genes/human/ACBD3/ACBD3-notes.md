# ACBD3 (GCP60, PAP7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(gates passed, `pairwise: win`) plus UniProt Q9H3P7, the GOA TSV and the primary literature.

## Headline: the gene is named for a domain whose activity it may not have

`GO:0000062 fatty-acyl-CoA binding` (IEA, InterPro) comes from the **ACB domain at residues
83–174**. It is a domain-implies-function inference, and the case against it is unusually clean:

- ACBD3's characterised activity lives in **different domains** — the **Q domain (241–308)**
  recruits PI4KB; the **unique region (UR)** immediately upstream of the GOLD domain carries the
  **MWT374-376 motif** that giantin and golgin-45 bind redundantly [PMID:38134218 "We therefore
  concluded that the second mechanism for Golgi recruitment of ACBD3 is between the MWT374-376
  residues of ACBD3 and two golgins: golgin-45 and giantin."]; and that UR together with the
  **GOLD domain (384–526)** binds the SEC22B longin domain, PKA RIIα and picornaviral 3A
  proteins. None of them is the ACB domain.
- **No acyl-CoA ligand, affinity or acyl-CoA-dependent activity has ever been reported.**
- The affinage record for this gene synthesises **30+ primary papers** across Golgi structure,
  PI4KB recruitment, steroidogenesis, sphingolipid transport, STING trafficking and picornavirus
  biology — and **never mentions acyl-CoA once**.

That last point is the strongest evidence available, and it is *negative* evidence from a source
that is otherwise dense and specific. Marked `MARK_AS_OVER_ANNOTATED` rather than removed: the
domain is genuinely present and PROSITE-recognised, ACBD-family members vary in whether the
domain retains binding, and a ligand may yet be found. But it should not read as characterised.

This is the same failure mode as ABHD8 (PR #2230), where α/β-hydrolase-*fold* IBAs assigned
lipase activity to a protein whose only characterised function is adaptor-like. **Fold and
domain names propagate into GO as activities.**

## The informative/uninformative inversion

Worth naming because it inverts the usual pattern in this campaign:

| Term | Source | Informative? |
|---|---|---|
| `GO:0043495` protein-membrane adaptor activity | **IBA** | ✅ exactly right |
| `GO:0034237` PKA regulatory subunit binding | IPI | ✅ specific partner |
| `GO:0005515` protein binding ×6 | **IPI, from the focused mechanistic papers** | ❌ says nothing |

The bare rows are the ones from the papers that *did the work* — PI4KB structural NMR, the
picornavirus 3A studies. The phylogenetic inference is more informative than six experimental
annotations. Three PI4KB rows are `MODIFY`ed to `GO:0043495`.

## Partners, resolved

| Partner | Papers | Verdict |
|---|---|---|
| **PI4KB** (Q9UBF8) | 4 | core — **Q-domain** recruitment, NMR of residues 241–308 |
| Picornaviral 3A (Aichi O91464, polio P03300, …) | 2 | the same adaptor activity, hijacked |
| **PRKAR1A** (P10644) | 1 | already informatively annotated |
| TBC1D22A/B | 3 | bind the **same Q domain**, mutually exclusively with PI4KB → MODIFY |
| PPM1L | 1 | topically coherent, no follow-up → over-annotated |

## Core/non-core consistency

`GO:0005739 mitochondrion` is kept **non-core** (UniProt's steroidogenesis statement is
`ECO:0000250` by similarity), so it is deliberately *not* listed in `core_functions.locations`
either — the validator flags that mismatch, and it is the same inconsistency a reviewer caught on
AAMDC (PR #2221). Stated explicitly in the `core_functions` description rather than left implicit.


## Correction: PI4KB binds the Q domain, not GOLD

An earlier draft of this review stated seven times that PI4KB is recruited through the GOLD
domain. **That is wrong**, and UniProt says so explicitly:

```
Interacts (via Q domain) with PI4KB (via N-terminus)
Interacts (via Q domain) with TBC1D22A and TBC1D22B;
  interactions with PI4KB and with TBC1D22A and TBC1D22B are mutually exclusive
-!- SUBUNIT: (Microbial infection) Interacts (via GOLD domain) with 3A proteins
```

`FT DOMAIN 384..526 GOLD`; the NMR structure of the PI4KB complex is of residues **241–308**,
which is the Q domain.

**How the error got in:** the affinage narrative says PI4KB is recruited *"through its GOLD
domain"*, and I used that sentence as `supporting_text` without checking it against UniProt —
on rows that listed the UniProt file in the same `supported_by` block. The campaign's own rule
is that a provider sentence is a lead, not evidence; I did not apply it. The quote is removed
everywhere and the affinage `reference_review` is marked `MISCITED` for that claim.

**Two things the correction bought:**

1. **The Q domain is a switch.** PI4KB and TBC1D22A/B compete for the same surface. So the
   TBC1D22 rows are not "uncharacterised screen hits" as I first called them — they engage the
   very surface that defines the protein's molecular function, and the competition is
   presumably how the Golgi arbitrates between PI4P synthesis and Rab-directed traffic. Those
   rows are now `MODIFY` rather than `MARK_AS_OVER_ANNOTATED`.
2. **Viral 3A uses a different surface from the host kinase** — GOLD, not Q. That explains how
   picornaviral 3A can clamp ACBD3 onto replication organelles *without* displacing PI4KB, which
   is the whole point of the hijack.

## The PKA regulatory subunit: compartment-specific, not contested

An earlier version of these notes and of the review called this "genuinely contested" and said
"the two sources disagree". That was over-dramatised, and a reviewer was right to push back: the
2023 paper reconciles the split itself. The only claim that survives as a genuine problem is a
negative one, and it belongs to UniProt.

| Source | Evidence | Claim |
|---|---|---|
| GOA `GO:0034237` IPI, WITH/FROM `UniProtKB:P10644` | IPI | binds PRKAR1A, i.e. **RIα** |
| UniProt SUBUNIT line | **(By similarity)**, ECO:0000250 | binds RI-alpha; does **not** bind RI-beta or **RII-alpha** |
| PMID:37044218 (2023, human) | experimental | GOLD domain binds **RIIα**; RIα not detected in the same pull-down, but explicitly *not* excluded |

The 2023 pull-down detects RIIα and not RIα [PMID:37044218 "His-RIIα, but not His-RIα, was
readily detected in the pulldown fraction"], but the authors do **not** read that as excluding RI.
Two sentences in the same paragraph do the reconciling for us:

- [PMID:37044218 "it is possible that ACBD3 binds RIα in such low affinity that this binding is
  below the detection limit in our assay."] — a dual-specific AKAP binds RI 10–100 fold more
  weakly than RII, so a negative pull-down is not a negative interaction.
- [PMID:37044218 "The discrepancy between ACBD3’s preference for the R subunit at different
  organelles may be explained by the fact that RI and RII are highly enriched at the mitochondria
  and the Golgi apparatus, respectively"] — i.e. one protein, two compartments, two subunits.

So "which subunit" is not a live dispute: the Golgi pool is RII-anchored, the mitochondrial pool
RI-anchored, and both records can be right. Per the project rule about not overruling curators, the
curated RIα IPI stands — I have not read PMID:17911601's full text, which is abstract-only in the
cache and whose title is about ezrin.

**What does survive.** UniProt's `(By similarity)` statement that ACBD3 does *not* interact with
RII-alpha is contradicted head-on by a human pull-down that does detect RIIα. A by-similarity
negative standing against a human experimental positive is the weakest configuration in the
record, and that specific point remains a UniProt correction to report.

`GO:0034237` is unaffected either way: the term is agnostic about which R subunit binds.

**Why this matters beyond the isoform.** The 2023 paper places the RII interaction in the **GOLD
domain** [PMID:37044218 "the GOLD domain of ACBD3 directly interacts with the regulatory subunit II
(RII) of PKA and effectively recruits PKA holoenzyme to the Golgi"]. Combined with the Q-domain
correction above, the map collapses to **two** interaction surfaces, not three:

- **Q domain (241–308)** — PI4KB *or* TBC1D22A/B, mutually exclusively
- **UR + GOLD (≈368–526)** — one shared surface. `MWT374-376` binds giantin *or* golgin-45
  (redundantly); `I380/K381` are the picornaviral 3A contact residues; `K381` is required for
  PKA RIIα docking; and the UR-plus-GOLD fragment (328–528) binds the SEC22B longin domain.

An earlier version of these notes called this map "clean and non-overlapping" and set UR
(golgins) against GOLD (3A, PKA, SEC22B). **That was wrong**, and a reviewer caught it using the
very paper I had just cited: PMID:38134218 places 3A recruitment at *"the UR of the GOLD
domain"* [PMID:38134218 "Picornavirus 3A peptide recruits ACBD3 to viral replication sites
through a protein–protein interaction via the UR of the GOLD domain of ACBD3"], its Figure 1D
puts I380/K381 four residues downstream of T376 [PMID:38134218 "MWT (M374/W375/T376) residues
highlighted in blue and protein 3A targeted residues"], and the study's premise is competition
[PMID:38134218 "We reasoned that the 3A peptide must outcompete the endogenous Golgi-localized
ACBD3 recruitment factor."]. Having adopted the convention that "the UR of the GOLD domain" is
one locus, I could not then use UR and GOLD as *contrasting* labels.

Cross-referencing the two papers makes it sharper still: PMID:37044218 maps RIIα docking to
**K381** [PMID:37044218 "K381P mutation greatly reduced the interaction between RIIα and the
GOLD domain, while Q379P and I380P had almost no effect"] — one of the two residues the 2024
paper names as the 3A contact site. So residues **374–381 are a shared hub** for the golgins,
PKA RII and viral 3A.

What survives unchanged is the Q-domain conclusion: 3A does not displace PI4KB, because neither
the UR nor GOLD is the Q domain. What changes is the mechanism of the hijack — it is most
likely **displacement of ACBD3's own anchors**, giantin/golgin-45 and PKA, rather than occupancy
of a spare site. That is now the leading `suggested_experiment`, with 3A-vs-golgin competition
foregrounded over 3A-vs-PKA because the paper states the golgin premise itself.

## A gap the GOA record has, found by reading the paper the record cites

ACBD3 has **no retrograde-transport annotation at all**. The `GO:0006888` IMP cites
PMID:37044218, but that paper's subject is Golgi-to-ER retrograde recycling: anterograde cargo
arrival is the *trigger*, and what ACBD3 controls is whether retrograde transport runs
constitutively [PMID:37044218 "depletion of ACBD3 reduces the Golgi fraction of RII, resulting in
moderate, but constitutive activation of PKA and KDELR retrograde transport, independent of cargo
influx from the ER"].

So the record captured the trigger and missed the regulated process. `GO:2000156` *regulation of
retrograde vesicle-mediated transport, Golgi to ER* is proposed as a `NEW` IMP — it has no
children, so it is the most specific term available, and the regulation parent is right because
ACBD3 is not transport machinery: it sets whether the pathway is cargo-gated. The existing
`GO:0006888` IMP is left `ACCEPT`, since the addition is additive rather than a correction to a
curator's experimental call.

## The MWT/giantin claim: checked against the primary paper, and it holds

The first three versions of this review stated the Golgi-targeting mechanism as "an MWT motif that
binds the golgins giantin and golgin-45" in the top-level `description` and in seven row summaries,
sourced only to `ACBD3-deep-research-affinage.md:68`. A reviewer flagged that as the same failure
mode as the GOLD/PI4KB error above: a provider domain-assignment sentence outrunning the UniProt
file cited beside it, since `ACBD3-uniprot.txt:366-368` says "The C-terminal GOLD domain is
essential for giantin binding".

That objection was procedurally right and substantively wrong, which is the interesting part.
`PMID:38134218` (Stalder et al. 2024, *Mol Biol Cell*) is now fetched and cached with full text,
and it supports the claim:

- The motif is **MWT374-376**, in the **unique region (UR) immediately upstream of the GOLD
  domain**. The paper's own section heading is "ACBD3 is recruited to the Golgi apparatus via a
  protein–protein interaction within a UR of the GOLD domain", and it repeatedly calls the locus
  "the UR of the GOLD domain" [PMID:38134218 "We thus demonstrated that the residues MWT374-376 in
  the UR of the GOLD domain of ACBD3 participate in a protein–protein interaction that recruits
  ACBD3 to the Golgi apparatus."]. So **"MWT motif" and "GOLD domain region" are two resolutions of
  one site**, not rival claims. The isolated GOLD domain without the UR is cytosolic; 328-528 and
  368-528 are Golgi-localised.
- Alanine scanning of the 21-residue UR relocalises only one mutant, MWT374-376>AAA, to the
  cytosol - and that mutant co-immunoprecipitates **neither** golgin [PMID:38134218 "the
  MWT374-376>AAA mutation that prevents the localization of ACBD3 to the Golgi apparatus does not
  interact with either of the golgins."].
- **Giantin and golgin-45 are redundant.** Single giantin knockout does not displace ACBD3
  [PMID:38134218 "the loss of giantin did not affect the recruitment of ACBD3 to the Golgi"]; only
  the double knockout does [PMID:38134218 "KO of both golgin-45 and giantin drastically affects the
  localization of endogenous ACBD3 at the Golgi apparatus"]. That redundancy is precisely why the
  older single-golgin model looked wrong.
- UniProt's giantin attribution traces to **Sohda 2001 (PMID:11590181), a yeast two-hybrid**
  result, and the 2024 paper says so while noting the knockdown result that unsettled it
  [PMID:38134218 "Initially, based on a yeast two-hybrid interaction, the golgin giantin was
  proposed to recruit ACBD3"]. The paper's own introduction also states the combined form -
  [PMID:38134218 "the GOLD domain and its extended UR interact with multiple different golgins
  including giantin, golgin-45, and golgin-160"] - which is UniProt's DOMAIN line and the MWT claim
  in one sentence.

**So the two sources are reconciled, not in conflict**, and the review now says so with the primary
paper cited on every row that makes the claim. The real defect was citing a provider narrative for a
mechanistic claim instead of the primary paper it named - the campaign rule, again, and this time
the rule caught a claim that happened to be true. Worth recording: "the provider said it" is not
evidence *even when the provider is right*, because you cannot tell which case you are in without
fetching the paper.

## What else the 2024 paper brought

Reading it added three things beyond the fix:

1. **SCFD1 (SLY1) is an essential upstream recruitment factor.** Its CRISPR knockout strips ACBD3
   from the Golgi [PMID:38134218 "Loss of SCFD1, however, resulted in the almost complete loss of
   ACBD3 from the Golgi apparatus"], and takes PI4KIIIβ with it. **SEC22B is a different case**:
   ACBD3 binds it, but its knockout [PMID:38134218 "Loss of TMED10 and SEC22B caused a drastic
   loss of Golgi organization resulting in Golgi fragmentation."] wrecks the Golgi generally, so a
   specific requirement for ACBD3 recruitment cannot be read off it. The review therefore
   attributes the upstream *requirement* to SCFD1 alone and annotates SEC22B only as a binding
   partner.
2. **The GOLD domain binds the longin domain of SEC22B** [PMID:38134218 "We thus conclude that the
   UR and GOLD domain of ACBD3 interacts with the longin domain of SEC22B"], with the SNARE and
   transmembrane domains excluded by truncation. Annotated as a `NEW` `GO:0000149 SNARE binding`
   IPI. Deliberately *not* annotated as complex membership, which the paper does claim: the assays
   are binary co-IPs from overexpressing cells, and the cytosolic MWT374-376>AAA mutant binds
   SEC22B *more* strongly than wild type, so binding and Golgi residence are separable. Nor is it
   listed in `core_functions`: SEC22B binding serves ACBD3's own delivery to the cis-Golgi,
   upstream of what ACBD3 does for the cell, and `core_functions` records the two outputs (PI4KB
   recruitment, PKA anchoring). An informative MF term need not be a core function.
3. **ACBD3 is required for PI4KB to reach the Golgi, one-way.** ACBD3 knockout loses Golgi
   PI4KIIIβ; PI4KIIIβ knockout leaves ACBD3 in place. The gene had no protein-localisation
   process term at all, so `GO:0034067 protein localization to Golgi apparatus` is proposed as a
   `NEW` IMP - the process counterpart of the `GO:0043495` adaptor MF it already carries.

Together these mean the **UR/GOLD surface is not viral-only**: it has two host partners
(SEC22B longin domain, PKA RIIα) as well as picornaviral 3A — and, per the correction above,
they are not on private sub-sites but share residues 374–381 with the golgin motif.

## Recruitment, as it now stands

```
SCFD1 (SM protein); ACBD3 binds SEC22B       <- step 1, UR+GOLD binds SEC22B longin domain
        |                                       SCFD1 KO -> ACBD3 cytosolic
        v
giantin  OR  golgin-45   (redundant)         <- step 2, both bind MWT374-376 in the UR
        |                                       double KO -> ACBD3 off the Golgi
        v
ACBD3 on cis/trans-Golgi membranes
        |
        v
PI4KB (via Q domain) / PKA RII (via UR+GOLD, K381) / FAPP2 / PPM1L / STING
```

Sequential, not parallel: ACBD3-giantin binding drops in SCFD1-KO cells, while ACBD3-SCFD1 binding
is unchanged in the golgin double KO [PMID:38134218 "This suggests that the recruitment of ACBD3 via
SCFD1 is upstream of the interaction with the golgins, and ACBD3 is recruited to the Golgi in a
two-step process."].
