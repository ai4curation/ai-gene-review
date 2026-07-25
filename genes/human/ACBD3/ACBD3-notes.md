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
