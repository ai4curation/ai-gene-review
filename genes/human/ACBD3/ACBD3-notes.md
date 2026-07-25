# ACBD3 (GCP60, PAP7) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(gates passed, `pairwise: win`) plus UniProt Q9H3P7, the GOA TSV and the primary literature.

## Headline: the gene is named for a domain whose activity it may not have

`GO:0000062 fatty-acyl-CoA binding` (IEA, InterPro) comes from the **ACB domain at residues
83–174**. It is a domain-implies-function inference, and the case against it is unusually clean:

- ACBD3's characterised activity lives in a **different domain** — the GOLD domain recruits
  PI4KB and binds PKA regulatory subunits, and a short MWT motif binds giantin and golgin-45.
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
| **PI4KB** (Q9UBF8) | 4 | core — GOLD-domain recruitment, NMR-defined |
| Picornaviral 3A (Aichi O91464, polio P03300, …) | 2 | the same adaptor activity, hijacked |
| **PRKAR1A** (P10644) | 1 | already informatively annotated |
| TBC1D22A/B | 3 | real but functionally uncharacterised → over-annotated |
| PPM1L | 1 | topically coherent, no follow-up → over-annotated |

## Core/non-core consistency

`GO:0005739 mitochondrion` is kept **non-core** (UniProt's steroidogenesis statement is
`ECO:0000250` by similarity), so it is deliberately *not* listed in `core_functions.locations`
either — the validator flags that mismatch, and it is the same inconsistency a reviewer caught on
AAMDC (PR #2221). Stated explicitly in the `core_functions` description rather than left implicit.
