# AAR2 (protein AAR2 homolog, C20orf4) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AAR2-deep-research-affinage.md`) plus UniProt Q9Y312, the GOA TSV and the primary
literature.

## Provider note: the trust gate is a false positive here

The affinage record **tripped its symbol-collision gate** — the narrative opens on yeast, and
the gate flags a non-human token in a human record (the ADA failure mode). Checked, and it is a
false positive of an interesting kind: the narrative correctly covers yeast **Aar2p**, where
the mechanism was worked out structurally, *and* human **AAR2**, which is the genuine ortholog.
UniProt itself annotates the human FUNCTION as `ECO:0000250|UniProtKB:P32357` — by similarity
to the yeast protein — so a yeast-centred narrative is the *right* description of this gene's
literature, not a symbol collision.

Worth recording as a gate-behaviour class for the campaign: **for genes whose mechanism was
established in yeast and transferred to human, the non-human-token gate will fire spuriously.**
The gate is still doing its job (it made me check); it just needs the curator to adjudicate
rather than to discount the record.

## What AAR2 does

AAR2 is a **U5 snRNP assembly factor** and, specifically, a **placeholder/checkpoint** protein.
The mechanism, from yeast structures and now confirmed in human:

- It binds the **RNase H-like (RH) domain of PRPF8**
  [file:human/AAR2/AAR2-uniprot.txt, "SUBUNIT: Interacts with PRPF8 (via RNase H homology domain)"],
  and the human protein was shown to be a genuine ortholog doing the same thing
  [PMID:26527271, "as a true Aar2 orthologue which binds to the RH domain (hsRH) of Prp8 and"].
- It occupies the site the **SNRNP200/Brr2 helicase** must eventually take, and blocks U4/U6
  di-snRNA loading — so it prevents premature spliceosome activation.
- **Species caveat, corrected during review.** I originally stated the displacement model as
  human fact. It is yeast-established: Aar2p and Brr2p are mutually exclusive Prp8 binders and
  Brr2p displaces Aar2p. Human appears to differ —
  [PMID:34131137, "In yeast, Aar2p is exchanged with Brr2p13,14, while in humans AAR2
  co-purifies with all four RHC members12, which indicates that AAR2 stays associated until the
  whole RHC is formed."] and PMID:36322420 reports a structurally distinct human interaction
  with "marked differences" in SEC interaction patterns. So *when* AAR2 leaves is an open
  question in human, now flagged in `suggested_questions`.
- It is a component of the **cytoplasmic precursor U5 snRNP** and is *excluded* from the
  tri-snRNP and the assembled spliceosome.
- The handoff is **phosphoregulated**.

The human-specific result is that AAR2 is more than a placeholder:
[PMID:36322420, "seems to lock PRPF8 RH in a conformation that is only compatible with the first"]
transesterification step, blocking the switch to the step-2 conformation — i.e. a
conformational checkpoint, not just steric occupancy.

## Curation: the NAS annotations understate a structural paper

Three annotations (`GO:0000387`, `GO:0005682`, `GO:0048025`) are `NAS` from PMID:36322420. NAS
is "non-traceable author statement" — but that paper is a **structure-function study of human
AAR2** with a crystal structure, designed interface variants that fail to bind PRPF8, and SEC
interaction mapping. Its own results support these terms directly. All three are `ACCEPT`ed
with the evidence-code gap flagged in `suggested_questions`.

`GO:0048025 negative regulation of mRNA splicing, via spliceosome` deserves a note: it sounds
odd for a splicing assembly factor, but it is right. AAR2's function *is* inhibitory — it
occludes the Brr2 site and blocks di-snRNA loading, holding the particle in an immature state
until the handoff. Negative regulation is the mechanism, not a side effect.

## The `protein binding` set — and here the pattern breaks

Four `GO:0005515` IPIs. Resolving the WITH/FROM accessions:

| Partner | Screens | Assessment |
|---|---|---|
| **EAPP** (Q56P03) | PMID:16189514, 28514442, 33961781 | a **putative U5 chaperone** — plausible, but the pair is uncharacterised |
| **TSSC4** (Q9Y5U2) | PMID:34131137 | **A real, functionally characterised U5 snRNP partner** |

**Correction made during review.** My first draft dismissed EAPP as "a cell-cycle and E2F-pathway
protein with no described connection to splicing or snRNP assembly". That is wrong, and the
refutation was in a paper I had already cited: PMID:34131137 describes *"a putative chaperone
EAPP that has been shown to interact with U5 proteins PRPF8 and EFTUD2"*. EAPP is in the U5
literature. I had judged it on its best-known identity rather than checking it in the context of
this gene's own biology — the same error as pattern-matching the partner set, just applied to a
single accession.

The `MARK_AS_OVER_ANNOTATED` verdict survives but on much narrower grounds: EAPP's U5 role is
explicitly *"putative"*, the AAR2–EAPP pair specifically has never been pursued, and the term is
uninformative regardless. If EAPP's U5 chaperone role is confirmed these rows deserve upgrading,
not discounting.

This is still the first gene in this campaign where a `GO:0005515` annotation points at genuine,
mechanistically pursued biology. PMID:34131137 is not a screen — it is a dedicated study
showing [PMID:34131137, "TSSC4 emerges as a specific chaperone that acts in U5 snRNP de novo"]
biogenesis and recycling, and that
[PMID:34131137, "Specifically, TSSC4 interacts with U5-specific proteins PRPF8, EFTUD2"]
and SNRNP200. AAR2 and TSSC4 are **both U5 snRNP assembly chaperones**, so their interaction is
exactly what the biology predicts.

So the four IPIs split: the three EAPP entries are `MARK_AS_OVER_ANNOTATED`, while the TSSC4
entry is `MODIFY` to `GO:0044877 protein-containing complex binding` — since TSSC4 is bound in
the context of the U5 snRNP particle — with the specific partner named in the summary.

Worth stating plainly because the previous four genes made the opposite case: high-throughput
binding records are *often* disjoint from the characterised biology, but not always, and the
check is to resolve the accessions, not to assume.

## Actions

| Term | Evidence | Action |
|---|---|---|
| `GO:0005682` U5 snRNP | IBA, NAS, ISS | ACCEPT (core) |
| `GO:0045292` mRNA cis splicing, via spliceosome | IBA | ACCEPT |
| `GO:0000387` spliceosomal snRNP assembly | NAS | ACCEPT (core) |
| `GO:0048025` negative regulation of mRNA splicing | NAS | ACCEPT — the inhibition *is* the mechanism |
| `GO:0000244` spliceosomal tri-snRNP complex assembly | ISS | ACCEPT |
| `GO:0005515` protein binding ×3 (EAPP) | IPI | MARK_AS_OVER_ANNOTATED |
| `GO:0005515` protein binding (TSSC4) | IPI | MODIFY → `GO:0044877` |

No `NEW` terms proposed. Unusually for this campaign, the existing record already covers the
biology well; the issues are evidence codes (three NAS that a structural paper could support
much better) rather than missing content.

## Schema note

`GO:0005682 U5 snRNP` belongs in `core_functions.in_complex`, **not** `locations` — the schema
is explicit that complex membership uses `in_complex` (bound to `GOProteinContainingComplexEnum`)
while `locations` is bound to `GOCellularLocationEnum`. Putting it in `locations` fails term
validation with "not in dynamic enum 'GOCellularLocationEnum'", which is the validator working
correctly rather than an ontology-version problem. Worth remembering for any complex-component
gene in this campaign.
