# ACBD3 (GCP60, PAP7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(gates passed, `pairwise: win`) plus UniProt Q9H3P7, the GOA TSV and the primary literature.

## Headline, corrected: the ACB domain does bind acyl-CoA

*(Rounds 1–8 of this review said otherwise. This section is the retraction.)*

`GO:0000062 fatty-acyl-CoA binding` (IEA, InterPro) comes from the **ACB domain at residues
83–174**. Rounds 1–8 of this review called it an over-annotation and asserted that **no acyl-CoA
ligand had ever been reported for ACBD3**. **That was false**, and the correction is now
`KEEP_AS_NON_CORE`.

**The source that refutes it was already cited here, in a sentence I quoted the second half of.**
PMID:38134218's introduction reads:

[PMID:38134218 "The ACBD domain oligomerizes upon binding to C18:1-CoA or C16:0-CoA"]

I quoted the *tail* of that same sentence — "the GOLD domain and its extended UR interact with
multiple different golgins…" — for the domain map, and never read the head of it, which names the
ligands. Rule 1 (*quote to the end of the interpreting clause*) has a mirror image: **read the
start of the sentence too.** The primary source it points to is Soupene and Kuypers 2015
(PMID:26290611), whose abstract makes the ACBD3 claim by contrast:

[PMID:26290611 "In contrast to ACBD1 and ACBD3, ligand binding did not result in the dimerization
of ACBD6."]

That paper is *titled* for ACBD6, which is why it never surfaced in any ACBD3-keyed search — and
why the campaign rule about not treating a silent record as evidence of absence exists.

**And the ACB domain has a gene-specific function too.** PMID:23166793: ACBD3 binds SREBP1 directly
and blocks its maturation [PMID:23166793 "ACBD3 blocked intracellular maturation of SREBP1 probably
through directly binding with the lipid regulator rather than disrupted SREBP1-SCAP-Insig1
interaction"]. The ACB-containing N-terminus plays an important part in that effect — but only a
part, since deleting it attenuates FASN-promoter suppression from 76% to 40% rather than abolishing
it, and the co-IP itself used full-length ACBD3 [PMID:23166793 "Taken together, these results
suggest that ACB domain-containing N-terminal sequence of ACBD3 plays an important role in its
regulatory effects on SREBP1."]. The lipogenic readout is real but weaker than the
abstract implies — unchanged at 48 h, reduced only at 72 h [PMID:23166793 "if allowing
overexpressed ACBD3 to be present in the cells for longer time (72 hours), we could see the
reduction of palmitate synthesis"].

**Why non-core rather than accepted as core.** The binding is demonstrated, so the InterPro
inference is corroborated. But no acyl-CoA-*dependent* step in ACBD3's Golgi activity is
known. This is a statement about the **ligand**, not the domain — the ACB domain has its own
functions (SREBP1 restraint, and the FAPP2 attribution; see the domain map). What is absent is
any demonstrated consequence of acyl-CoA binding. Deleting the ACBD domain does not prevent Golgi
localisation [PMID:38134218 "Our data suggest that the binding of ACBD3 to C18:1-CoA, C16:0-CoA or
related fatty acyl chains and the subsequent oligomerization does not affect its recruitment to the
Golgi as deletion of the ACBD domain does not prevent Golgi localization."], and the domain is
dispensable for **3A-mediated** PI4KB recruitment — the enteroviral assay, not host recruitment on
its own
[PMID:30755512 "we show that acyl-coenzyme A
binding (ACB) and charged-amino-acid region (CAR) domains are dispensable for 3A-mediated PI4KB
recruitment and efficient enterovirus replication"], with Q+GOLD sufficient [PMID:30755512 "we
dissected the different domains of ACBD3 and uncovered that the glutamine-rich region (Q) and Golgi
dynamics domain (GOLD) together suffice to support enterovirus replication"]. A real molecular
function; not the core one.

### How the error survived eight rounds

Three separate guards failed, and all three failed the same way — by treating an *absence* as a
finding:

1. **The affinage record's silence was used as evidence.** "Synthesises 30+ primary papers and
   never mentions acyl-CoA once" was quoted as *support* for the over-annotation call, in four
   places. It is a coverage gap in one provider's summary, nothing more. The campaign brief says
   this in as many words — *an empty or silent affinage record is NOT evidence that literature is
   absent* — and I applied that rule to other genes' records while breaking it here.
2. **A domain-name-is-not-an-activity heuristic was applied without checking the converse.** The
   ABHD8 analogy (fold name propagating into GO as activity) was apt in form and wrong in fact:
   here the domain name *is* backed by biochemistry. Pattern-matching to a known failure mode is
   not evidence either.
3. **The papers that had the answer were read only in the parts that concerned other claims.**
   PMID:38134218 was read for the golgins; PMID:30755512 was read from its abstract, whose ACB
   sentence is the *dispensability* result — while the results paragraph that names the two ACB
   functions, with citations, sits at line 164. The reviewer found it by reading the paragraph.

The generalisable rule, added below: **a negative claim about the literature needs a positive
search, not a silent source.** Before writing "no X has been reported", search for X by name — and
search under the paralog names too, since the paper that had this answer is titled for ACBD6.

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

Two annotations are kept **non-core**, and in both cases the term is right while the evidence is
not core-strength:

- `GO:0005739 mitochondrion` — UniProt's steroidogenesis statement is `ECO:0000250` by similarity,
  so it is deliberately *not* listed in `core_functions.locations` either. The validator flags that
  mismatch, and it is the same inconsistency a reviewer caught on AAMDC (PR #2221). Stated
  explicitly in the `core_functions` description rather than left implicit.
- `GO:0000062 fatty-acyl-CoA binding` — the binding is *demonstrated* (see the corrected headline),
  so it is not an over-annotation; but no acyl-CoA-dependent step in ACBD3's Golgi activity is
  known, and the ACB domain is dispensable for 3A-mediated PI4KB recruitment (the enteroviral
  assay). Real molecular function, not the core one, and so not promoted into `core_functions`.


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
correction above, the UR/GOLD split collapses — leaving **three** functional regions, not four:

- **ACB domain** — boundaries are source-dependent (UniProt `83–174`; PMID:23166793 writes
  "ACB domain (80–171)" and deletes `1–171`), which is rule 3's own case; nothing here turns on it.
  Binds C18:1-CoA / C16:0-CoA and oligomerises on ligand. Contributes to SREBP1 restraint, but only
  in part: ΔN weakens the effect without abolishing it, and the SREBP1 co-IP used full-length ACBD3,
  so the interaction is not domain-mapped. Credited by PMID:38134218 with recruiting FAPP2, citing
  PMID:29750412 — though that paper's abstract maps nothing to the ACB domain and models FAPP2
  dispersal as a *consequence* of Golgi fragmentation, so treat the FAPP2 domain assignment as
  PMID:38134218's rather than established.
- **Q domain (241–308)** — PI4KB *or* TBC1D22A/B, mutually exclusively
- **UR + GOLD** — one shared surface. UniProt places GOLD at **384–526**; the paper's
  Golgi-competent, SEC22B-binding fragment is **328–528**; and the 21-residue
  alanine-scanned UR lies immediately upstream of 384, i.e. inside that fragment. No
  source gives "UR + GOLD" a lower bound, so quote residues, not a range. Within it:
  - `MWT374-376` — giantin *or* golgin-45, redundantly
  - `I380/K381` — the picornaviral 3A contact residues
  - the **single α helix, ≈379–383** — the PKA RIIα-binding *interface* (K381P breaks the
    helix and abolishes binding; Q379P and I380P do not). No contact *residue* is mapped;
    Ile380 is proposed from the apo structure and is untested.
  - `328–528` — the SEC22B longin domain

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

Cross-referencing the two papers makes it sharper still — but the residue has to be read off the
right experiment. An earlier version of this section said PMID:37044218 "maps RIIα docking to
**K381**", citing [PMID:37044218 "K381P mutation greatly reduced the interaction between
RIIα and the GOLD domain, while Q379P and I380P had almost no effect"]. **That over-reads a
proline scan.** The mutants are prolines chosen as helix breakers [PMID:37044218 "we generated
GST-tagged GOLD mutants (Q379P, I380P, or K381P) for pulldown assays since proline is known to be
a potent helix breaker"], and the authors read the result structurally, not as a contact
[PMID:37044218 "suggesting that K381P disrupts the helical structure and the RIIα-binding
interface"]. Two sentences later they nominate a contact from the crystal structure:
[PMID:37044218 "the side chain of Ile380 is mostly available for protein interactions, likely
involved in binding the shallow hydrophobic groove on RII surface"], with Phe383 buried.

**Second correction, same sentence, opposite direction.** A later version of this paragraph
then asserted that the RIIα contact residue *is* **I380**. That over-reads too, and the
reviewer caught it in the half of the sentence I had again cut away: **`I380P` had almost no
effect.** Quoting the sentence whole, as the rule below demands:

[PMID:37044218 "K381P mutation greatly reduced the interaction between RIIα and the GOLD
domain, while Q379P and I380P had almost no effect, suggesting that K381P disrupts the
helical structure and the RIIα-binding interface."]

And the Ile380 nomination is not a measurement. It comes from inspecting the **apo** GOLD
structure — PDB 5LZ1, ACBD3 alone, no R subunit [PMID:37044218 "Structural illustration is
generated by PyMOL using the crystal structure file 5LZ1."] — it is hedged ("*likely*
involved in binding"), and it is offered to explain why the buried Phe383 does not make
ACBD3 RI-selective. Its only direct test in that paper is the null I380P.

**What the two papers jointly support is the helix, not a residue.** The GOLD domain has one
α helix [PMID:37044218 "The crystal structure of the GOLD domain consists of one α helix and
11 β strands"], K381P breaks it and abolishes RIIα binding, and both 3A contact residues
[PMID:38134218 "in red (I380/K381; AlphaFold2)"] lie inside it. So residues **374–381 remain
a shared hub** for the golgins, PKA RII and viral 3A — as *overlapping surfaces*, which is a
weaker and correct claim. Whether PKA and 3A share a contact residue is exactly what
`suggested_experiments[3]` is designed to test, so it must not be written as settled.

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
2. **The UR plus GOLD domain binds the longin domain of SEC22B** [PMID:38134218 "We thus conclude
   that the UR and GOLD domain of ACBD3 interacts with the longin domain of SEC22B"] — the mapped
   fragment is 328–528, so GOLD alone is not the right attribution. With the SNARE and
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
PI4KB (via Q domain) / PKA RII (via the UR+GOLD α helix, ~379-383) / FAPP2 / PPM1L / STING
```

Sequential, not parallel: ACBD3-giantin binding drops in SCFD1-KO cells, while ACBD3-SCFD1 binding
is unchanged in the golgin double KO [PMID:38134218 "This suggests that the recruitment of ACBD3 via
SCFD1 is upstream of the interaction with the golgins, and ACBD3 is recruited to the Golgi in a
two-step process."].

## Three rules, two of them learned on one sentence

The same sentence of PMID:37044218 produced two opposite errors in consecutive rounds, which is
where rules 1 and 2 come from —
first reading the loss-of-binding proline mutant `K381P` as a contact residue, then reading
`I380` as the contact although the same sentence reports `I380P` as having almost no effect.
Both halves were verbatim; both readings were wrong.

1. **Quote to the end of the interpreting clause.** If the sentence continues with
   *suggesting*, *while*, *although*, *whereas* or a comparison, the continuation is part of
   the result. Cutting at a comma inverts meaning as often as it shortens it.
2. **A mutant's phenotype names an element, not a residue, unless the substitution is
   conservative and the structure is holo.** Two corollaries, one for each error:
   - a **proline** substitution that abolishes binding implicates the *secondary structure*, not
     the side chain;
   - a substitution with **no effect** does not nominate its residue as a contact either — it is
     evidence against, or at best uninformative.
   Apo structures propose contacts; they do not map them.
3. **When two sources draw different boundaries for one region, resolve to residue numbers**
   and treat the domain names as commentary. (Rounds 3–5 were all boundary-label
   collisions; see the UR/GOLD correction above.)

**One caveat on my own numbers.** The `≈379–383` span I use for the helix is an *inference*,
flagged here under rule 3 because it is the same class of thing rule 3 warns about. Neither paper
gives the helix endpoints. What is sourced is: the GOLD domain has *one* α helix; Q379, I380 and
K381 were the residues substituted as helix-breakers; and Phe383 is buried. `379–383` is bracketed
from those facts, which is why it is written as "roughly" everywhere it appears.

4. **A negative claim about the literature needs a positive search, not a silent source.**
   "No X has been reported" is a claim about all of PubMed, and no summary, however dense,
   can support it. Search for X by name — and under the **paralog** names, since the paper
   carrying this gene's acyl-CoA data is titled for ACBD6 and never surfaced in an
   ACBD3-keyed search.

## One sentence, three errors

`publications/PMID_38134218.md:72` has produced a distinct error in each of rounds 4, 9 and 10:

```
The ACBD domain oligomerizes upon binding to C18:1-CoA or C16:0-CoA (Soupene and
Kuypers, 2015)  and recruits the membrane-shaping protein FAPP2 (Liao et al., 2019),
  ^-- round 9 missed this head       ^-- round 10 missed this middle
the CAR-Q domain recruits PI4KIIIβ (Klima et al., 2016), and the GOLD domain and its
extended UR interact with multiple different golgins ...
                                  ^-- round 4 quoted only this tail
```

Round 4 quoted the tail for the domain map. Round 9 read the head and inverted the acyl-CoA
call. Round 10 read the clause between them and found the ACB domain has a protein client.
Each time the fix was correct and each time I stopped at the clause I needed.

**Rule 1 restated, generally:** *quote the whole sentence, then decide what to use.* Not "to
the end of the interpreting clause" — to **both** ends. A sentence that enumerates domains is
a table in prose; reading one row of a table is not reading the table.

It is also worth naming why this sentence in particular: it is a **secondary** sentence, an
introduction compressing four primary papers into four clauses. High information density,
each clause a lead worth a fetch, and no redundancy to catch a partial read. Reviews should
treat an introduction's domain enumeration as a work list, not as a citation.

### Round 11: the same shape one level further in — a figure legend for a paragraph

Round 10 annotated `GO:2000639` and said the cached text carried *no quotable loss-of-function
result*, so the call rested on overexpression alone. **It does carry one**, three occurrences of it:

[PMID:23166793 "More strikingly, after knocking down endogenous ACBD3, nuclear SREBP1 expression was
enhanced in both HEK293T and Hep G2 cells"] — with the authors' conclusion
[PMID:23166793 "All these results strongly suggest that ACBD3 intrinsically plays a negative role in
SREBP1 protein maturation."] and a specificity control
[PMID:23166793 "knockdown of endogenous ACBD3 had no effect on the expression of these two
SREBP-binding proteins, either (Figure S2)"].

What I read was the **Figure 3 legend**, which describes the experiment and not its outcome. The
result is the paragraph immediately above it. So the progression across rounds is:

| Round | What stood in for the evidence |
|---|---|
| 8 | the **abstract** stood in for the results paragraph |
| 10 | one **clause** stood in for the sentence |
| 11 | the **figure legend** stood in for the paragraph |

Each is a shorter, tidier text that sits next to the real one and reads as if it were complete.
**Rule 5: a caption is not a result.** Figure legends, abstracts and introductions are all
*summaries*; when a claim turns on what an experiment showed, the sentence that reports the outcome
is in the body text, and it is the only one that counts. Corollary: this cut against my own
annotation — the correction *strengthened* `GO:2000639` from one-directional to bidirectional — so
the habit is not conservative, it is just wrong in whichever direction the summary happens to lean.
