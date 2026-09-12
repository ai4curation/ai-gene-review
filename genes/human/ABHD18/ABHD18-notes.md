# ABHD18 — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider plus UniProt Q0P651,
the GOA TSV and the primary literature.

## The gap

Two GO annotations, both `mitochondrion`. **No molecular function, no biological process** —
despite UniProt naming the protein *"Cardiolipin-specific deacylase, mitochondrial"* and carrying
a Rhea-referenced `CATALYTIC ACTIVITY` block (`RHEA:32935`).

Two independent 2025 papers characterised the enzyme. Both are now used.

## Two framings of the same enzymology

This is the interesting curation problem, and it only surfaced because a PR reviewer noticed the
affinage record cited a paper I had not adjudicated.

| | PMID:40903572 (*Nature*) | PMID:40378955 (*JBC*) |
|---|---|---|
| Framing | the **missing deacylase** of the remodelling cycle | a **degradative lipase**, homolog of yeast Cld1 |
| ABHD18/TAZ relationship | partners in a hydrolysis–reacylation cycle | *"ABHD18 catalyzes the breakdown of CL, whereas TAZ protects CL from degradation"* |
| Extent of reaction | CL → MLCL | **stepwise**, past MLCL to dilyso-CL |
| Clinical angle | Barth syndrome therapeutic target — ABHD18 loss rescues TAZ-mutant phenotypes | knockdown lowers MLCL in *Taz*-KO myoblasts |

Both describe the same chemistry. `GO:0035965 cardiolipin acyl-chain remodeling` is retained
because both agree ABHD18 supplies the deacylation step of the ABHD18/tafazzin pair — and because
**GO has no cardiolipin catabolic process term**, so the degradative reading cannot currently be
expressed at all. Filed as a `suggested_question`.

My first draft said "removes one acyl chain". PMID:40378955 is explicit that this is wrong:
*"Rather than removing just one fatty acid, we show that ABHD18 deacylates CL further."* Corrected
in the description, `core_functions` and the proposed term.

## Why A2-type, not the generic parent

`RHEA:32935` writes the product as `1'-[1,2-diacyl-sn-glycero-3-phospho],3'-[1-acyl-sn-glycero-3-phospho]-glycerol`.
The chain remaining on the deacylated glycerol is at **sn-1**, so the chain removed was at
**sn-2** — which is A2 regiochemistry. `GO:0004623 A2-type glycerophospholipase activity` is
therefore more precise than `GO:0004620`, and is used.

## The GO gap

GO resolves cardiolipin metabolism at substrate level almost everywhere — synthase
(`GO:0008808`), CMP-forming synthase (`GO:0043337`), phospholipase D (`GO:0035755`),
dehydrogenase (`GO:0160241`) — but has **nothing for deacylation**, even though that step is half
of `GO:0035965`. The gap is historical: the enzyme was unidentified until 2025.

Proposed: *cardiolipin deacylase activity*, defined to cover the stepwise reaction rather than
only the first product.

## Provider note

Affinage's prose added little here — UniProt had already curated the primary paper with a Rhea
cross-reference, and for a gene with one recent, promptly-curated paper the provider is
redundant. But an earlier draft concluded it "added nothing", and **that was wrong**: its
citation list contained PMID:40378955, which I had missed and which materially qualifies the
framing. A concrete case where the provider's value was in its **reference list**, not its
narrative.
