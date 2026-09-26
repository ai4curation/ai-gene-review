# AJM1 / C9orf172 (C9J069) — review notes

2026-09-26. PAINT no-IBA backlog. Provider: **affinage refused; falcon used as fallback.**

## affinage's trust gate fired, and it was right

This is the first time in this campaign the affinage symbol-collision gate has **blocked**:

```
⚠️  AJM1: trust gate(s) tripped
    - [BLOCKING] Possible symbol collision: the narrative's opening names a non-human
      context ("c. elegans") despite a human record
❌ refusing to write genes/human/AJM1/AJM1-deep-research-affinage.md
```

I wrote the record to a scratch path with `--out` to inspect it, per the tool's own instructions,
and the gate was correct: **every claim and every PMID in that narrative describes C. elegans
AJM-1** — DLG-1/LET-413 recruitment, the DAC complex, hypodermal lethality, AWC^ON specification.
Nothing about human C9J069. It was not written into the gene folder.

Worth distinguishing this from the ADA case the gate was built for. That is a same-symbol
*different* protein. Here the worm gene is the actual **IBA donor** for this human gene, so the
record is about the phylogenetic source rather than an unrelated protein. Both must be blocked
for the same reason — the file would be ingested as though it described human AJM1 — but the
curatorial reading differs.

**falcon, given the same ambiguous symbol, handled it correctly**, which is a useful contrast:

> [file:genes/human/AJM1/AJM1-deep-research-falcon.md "However, **the literature is limited for this specific human protein**. Most detailed AJM-1 literature concerns the *Caenorhabditis elegans* ortholog."]
> [file:genes/human/AJM1/AJM1-deep-research-falcon.md "Human AJM1 is a poorly characterized, probably non-enzymatic protein whose conserved domains and nematode ortholog suggest a structural or scaffolding role at cell–cell junctions. Direct validation of this role in human cells remains inadequate."]

## The headline: eight rows, one worm protein

Human AJM1 has **zero experimental GO annotations**. Seven of eight rows trace to a single
protein, C. elegans ajm-1 (`UniProtKB:A0A1C3NSL9` / `WB:WBGene00000100`).

The set *looks* diverse — three evidence codes, four GO_REFs — but the three UniProt SubCell IEAs
are second-order. Every SUBCELLULAR LOCATION line in the human entry carries
`ECO:0000250|UniProtKB:A0A1C3NSL9`, so UniProt made an ISS from the worm and the SubCell→GO
mapping re-emitted it as IEA. **Only the InterPro row (IPR038825) is independent of the worm
gene**, and that is family-domain based, not experimental.

A curator scanning the evidence-code column would read this as far better supported than it is.

## The one removal: GO:0005929 cilium

Traced the chain and it bottoms out in nothing:

- human IEA ← UniProt SubCell ← UniProt by-similarity cilium statement ← worm ajm-1
- **worm ajm-1's own `GO:0005929` is itself only IEA** (GO_REF:0000044)

So: inference on inference, no measurement at any step. The worm *does* have one experimentally
grounded ciliary annotation — `GO:0036064` ciliary basal body (IDA) — from the Girdin paper. But
that paper scopes the mechanism explicitly:

> [PMID:27623382 "C. elegans Girdin also regulates localization of the apical junction component AJM-1, suggesting that in nematodes Girdin may position BBs via rootletin- and AJM-1-dependent anchoring to the cytoskeleton and plasma membrane, respectively."]
> [PMID:27623382 "Together, our results describe a conserved role for Girdin in BB positioning and ciliogenesis."]

The conserved claim is about **Girdin**, not AJM-1; the AJM-1 mechanism is "in nematodes". So the
best ciliary evidence in the donor names a *different compartment* and *disclaims transfer*.
REMOVE.

Found by querying the donor's annotations rather than the human gene — worth remembering as a
technique for all-electronic genes.

## An objection I raised and then withdrew

I suspected `GO:0043296 apical junction complex` of a lineage mismatch: the nematode CeAJ is not
built from vertebrate parts, and falcon says so too
[file:genes/human/AJM1/AJM1-deep-research-falcon.md "Mammalian junctional complexes differ from the nematode CeAJ; functional conservation remains untested."].

Checking the **term definition** rather than the label killed the objection. GO:0043296 is
deliberately written to span both: the vertebrate tight junction/zonula adherens/desmosome unit
*and* the invertebrate subapical complex/zonula adherens/septate junction unit. The term is
cross-lineage by design. ACCEPT.

(Same lesson as the GO-search note in my memory: read the definition, not the label.)

## core_functions: no molecular_function, deliberately

Populated the process and locations but **asserted no MF**. The worm donor's only MF annotation is
cytoskeletal protein binding with TAS evidence — too weak and too generic to transfer — and
minting a structural-constituent term for a protein with zero human data would be exactly the
over-annotation this project removes. A located, process-level inference with the molecular
activity left open is the honest shape here.

(Contrast AIRIM earlier today, where adding `GO:0005198` *was* right: there the funnel
architecture is structurally resolved.)

## A nuance worth carrying forward

The founding paper places AJM-1 **basal to** the cadherin-catenin complex:

> [PMID:11715019 "We have characterized the novel coiled-coil protein AJM-1, which localizes to an apical junctional domain of Caenorhabditis elegans epithelia basal to the HMR-HMP (cadherin-catenin) complex."]

So `GO:0005912 adherens junction` is a neighbouring-domain description, not a claim that AJM-1 is
a cadherin-complex component. Kept, but flagged in the row.

## Outcome

8 rows: 7 ACCEPT, 1 REMOVE. `just validate human AJM1` → ✓ Valid, no warnings.
11 distinct supporting_text quotes (32 instances) verified, including the 14 `file:` instances CI
does not check.

## Round 2 (review feedback)

All three items were evidence-hygiene failures, and the first two are both instances of the
`file:` blind spot: CI does not substring-check `file:` quotes, so a quote can be attached to the
wrong line and nothing notices.

### 1. The cilium REMOVE cited the wrong UniProt line

I anchored the claim about "UniProt's by-similarity **cilium** statement" to
`SUBCELLULAR LOCATION: Apical cell membrane`. The cilium statement is its own clean substring two
lines down — `Cell projection, cilium` — and it carries the `ECO:0000250` code in the same
snippet. Fixed. The argument was right; the citation was pointing at a different sentence.

### 2. GO:0005912 cited the FUNCTION line to support a *location*

Same shape. Now cites `Cell junction, adherens junction`.

### 3. Six load-bearing donor facts existed only as prose

"Worm `GO:0005929` is itself only IEA" **is** the cilium removal, and nothing in the branch let a
reader re-check it. I had queried QuickGO but committed no evidence.

Added `AJM1-donor-goa-check.json`, following the
`genes/human/SAMD8/SAMD8-reaction-donor-check.json` convention: the full 19-row QuickGO snapshot
for A0A1C3NSL9 with the query URL, retrieval timestamp, a sha256 of the raw response, and an
explicit claims-to-checks mapping so each prose assertion names the row that proves it. Cited
from the six rows that depend on it.

### The judgment call: GO:0005912

The reviewer noticed my row argued *against itself* — it recorded that AJM-1 sits basal to, and
in a domain distinct from, the cadherin-catenin complex, called that "a neighbouring-domain
description" (which is a description of an over-annotation), and then ACCEPTed.

**I withdrew the reasoning rather than the action.** The worm curator who made that IDA read the
full text; I read the abstract. CLAUDE.md is explicit that an abstract is not grounds for
second-guessing an experimental annotation, and I had effectively done so in prose while
formally deferring. The row now cites the donor IDA from the snapshot and defers cleanly.

This is the same internal-inconsistency failure as the ADM5 `summary`/`reason` disagreement
earlier today: the structured field said one thing and the prose said another. Worth watching
for as a class.

### Suggestions taken

- Mouse Ajm1 (A2AJA9), same PTHR21517:SF3 subfamily, is unexamined — added as a question. A
  mammalian ortholog with even one localisation experiment would be far better ground than the
  nematode.
- The "no catalytic domain" claim rests on InterPro/Pfam returning only the three family
  signatures; the cysteine-rich stretch has not been scanned against structural or metal-binding
  motif sets. Added as a question rather than quietly relied on.
- The ~160-word shared preamble repeated in all 8 rows does bury the per-row argument. Left as
  is for now: each row genuinely needs the single-donor context to be readable standalone, and
  the alternative is a cross-reference a curator reading one row would not follow. Flagged rather
  than restructured.

Final: 8 rows, 7 ACCEPT / 1 REMOVE. 20 distinct quotes (39 instances) verified, 21 of them
`file:` instances CI does not check.
