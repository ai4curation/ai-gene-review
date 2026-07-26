# ACBD3 (GCP60, PAP7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(gates passed, `pairwise: win`) plus UniProt Q9H3P7, the GOA TSV and the primary literature.

## Headline: the gene is named for a domain whose activity it may not have

`GO:0000062 fatty-acyl-CoA binding` (IEA, InterPro) comes from the **ACB domain at residues
83–174**. It is a domain-implies-function inference, and the case against it is unusually clean:

- ACBD3's characterised activity lives in **different domains** — the **Q domain (241–308)**
  recruits PI4KB, the **GOLD domain (384–526)** binds picornaviral 3A proteins, and a short MWT
  motif binds giantin and golgin-45. None of them is the ACB domain.
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

## The PKA regulatory subunit: UniProt and the primary literature disagree

This is unresolved in the sources, not just in this review, and it is worth stating plainly
because the disagreement is about a negative claim.

| Source | Evidence | Claim |
|---|---|---|
| GOA `GO:0034237` IPI, WITH/FROM `UniProtKB:P10644` | IPI | binds PRKAR1A, i.e. **RIα** |
| UniProt SUBUNIT line | **(By similarity)**, ECO:0000250 | binds RI-alpha; does **not** bind RI-beta or **RII-alpha** |
| PMID:37044218 (2023, human) | experimental | GOLD domain binds **RII**; ACBD3 binds RII but **not RI** |

[PMID:37044218 "Our results indicate that ACBD3 interacts specifically with the RII, but not RI subunit."]
directly contradicts UniProt's by-similarity negation of RII-alpha. Per the project rule about
not overruling curators, the curated RIα IPI stands — I have not read PMID:17911601's full text,
which is abstract-only in the cache and whose title is about ezrin. But a by-similarity negative
is the weakest kind of statement to leave standing against a 2023 human experimental positive,
so this is recorded as a UniProt discrepancy to report rather than resolved in either direction.

`GO:0034237` is unaffected either way: the term is agnostic about which R subunit binds.

**Why this matters beyond the isoform.** The 2023 paper places the RII interaction in the **GOLD
domain** [PMID:37044218 "the GOLD domain of ACBD3 directly interacts with the regulatory subunit II
(RII) of PKA and effectively recruits PKA holoenzyme to the Golgi"]. Combined with the Q-domain
correction above, the domain map becomes clean and non-overlapping:

- **Q domain (241–308)** — PI4KB *or* TBC1D22A/B, mutually exclusively
- **GOLD domain (384–526)** — PKA RII, and picornaviral 3A proteins

So GOLD is not a viral-only surface, as the previous version of these notes implied. It has a
host partner, and the same reasoning that made 3A-vs-PI4KB non-competitive predicts that a virus
clamping GOLD would displace PKA — a testable consequence, added to `suggested_experiments`.

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
