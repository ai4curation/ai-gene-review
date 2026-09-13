# Cgas (naked mole-rat, *Heterocephalus glaber*) — review notes

UniProt **A0AAX6RS70** (TrEMBL, unreviewed), 554 aa, `GN Name=Mb21d1` (the older symbol
for cGAS), RefSeq XP_021099394.1, "Cyclic GMP-AMP synthase isoform X1".

## 1. The annotation set is a single pure phylogenetic propagation

All 13 GOA rows are `IEA` / `GO_REF:0000118` / assigned by `TreeGrafter`, with the same
WITH/FROM: `PANTHER:PTN000069395`. There is not one experimental, ISS, Ensembl-Compara,
ARBA, UniRule or InterPro2GO row. So this review is entirely about whether a PANTHER
ancestral-node assertion transfers to this species.

### Where the node assertions actually sit

`interpro/panther/PTHR10656/PTHR10656-paint.tsv` (family PTHR10656, the family UniProt
assigns this protein to, subfamily PTHR10656:SF35 "CYCLIC GMP-AMP SYNTHASE") contains no
IBD at `PTN000069395` — that is the TreeGrafter graft point for this sequence, not an
assertion node. The IBD assertions carrying exactly this term set are at two nodes:

| node | taxon | GO terms | seeds |
|---|---|---|---|
| `PTN002579681` | `taxon:117571` Euteleostomi | GO:0005634, GO:0005829, GO:0035861, GO:0003682, GO:0003690, GO:0002218, GO:0002230, GO:0006974, GO:0032481, GO:0038001, GO:0071360, GO:2000042 | `MGI:MGI:2442261` (mouse Cgas), `UniProtKB:Q8N884` (human CGAS) |
| `PTN000838114` | `taxon:6072` Eumetazoa | GO:0061501 | 8 seeds spanning fly cGLRs, mouse, human, zebrafish, coral |

That is, the 12 non-catalytic terms come from a Euteleostomi-level node whose experimental
grounding is human CGAS and mouse Cgas; the catalytic term comes from a much deeper
Eumetazoan node. Spot-checking one seed at random confirms the grounding is real and not
itself a propagation: mouse Cgas carries four independent experimental annotations to
GO:0071360 (`IMP` PMID:23258413; `IDA` PMID:24077100, PMID:28214358, PMID:28363908,
QuickGO). **The node placements are sound.** Challenging any of them therefore has to be
an argument about this species, not about donor counts.

## 2. What the naked-mole-rat literature actually establishes

Only four cached publications concern cGAS in this species, and **all four are
abstract-only** (`full_text_available: false`). Two are commentary. So the entire
primary evidence base is one abstract.

### The decisive finding — sign reversal of the HR-repair role

[PMID:41066557 "A cGAS-mediated mechanism in naked mole-rats potentiates DNA repair and delays aging.", "naked mole-rat cyclic guanosine monophosphate-adenosine monophosphate synthase (cGAS) lacks the suppressive function of human or mouse homologs in homologous recombination repair through the alteration of four amino acids during evolution"]

This is a direct, species-specific contradiction of one propagated term,
`GO:2000042 negative regulation of double-strand break repair via homologous recombination`.
The mechanism given is:

[PMID:41066557 "The changes enable cGAS to retain chromatin longer upon DNA damage by weakening TRIM41-mediated ubiquitination and interaction with the segregase P97."]

[PMID:41066557 "Prolonged chromatin binding of cGAS enhanced the interaction between repair factors FANCI and RAD50 to facilitate RAD50 recruitment to damage sites, thereby potentiating homologous recombination repair."]

and the organismal consequence:

[PMID:41066557 "Moreover, the four amino acids mediate the function of cGAS in antagonizing cellular and tissue aging and extending life span."]

The Science commentary agrees on the framing but adds no independent data:
[PMID:41066590 "A DNA repair function in a cytosolic sensor demonstrates a potential role in naked mole-rat longevity."]

PMID:41935903 (Sci Bull) and PMID:41198971 (Nat Aging) are cached with **no abstract body
at all** — title and metadata only. Nothing can be quoted from them, and neither is
primary. They are recorded as `LOW` relevance commentary.

### What the abstracts do NOT say

Deliberately listing this, because it is what constrains the review:

- They do not state whether naked-mole-rat cGAS synthesises 2'3'-cGAMP.
- They do not mention STING, IRF3, type I interferon, antiviral defence, or dsRNA.
- They do not state that naked-mole-rat cGAS localises to sites of double-strand breaks
  (they state chromatin retention on damage, and RAD50 recruitment *to* damage sites).
- They do not name the four amino acids.

Nothing in the other cached naked-mole-rat literature helps. The two NMR genome-maintenance
reviews (PMID:29340215 "Genome Stability Maintenance in Naked Mole-Rat.";
PMID:34199458 "DNA Homeostasis and Senescence: Lessons from the Naked Mole Rat.") and the
two repair-biochemistry papers (PMID:29930219; PMID:31085801) predate the cGAS work and
contain no cGAS or STING content — I grepped all four; the apparent "sting" hits are
substrings of *testing*/*interesting*.

## 3. Own bioinformatics: the catalytic core is intact and the divergence is C-terminal

Because the abstract says nothing about catalysis, I ran a residue-transfer analysis rather
than guess. `Cgas-bioinformatics/align_cgas.py` globally aligns A0AAX6RS70 against human
CGAS (Q8N884) and mouse Cgas (Q8C6L5) and transfers every UniProt `BINDING`/`SITE`/`ACT_SITE`
feature through the alignment. Full write-up in `Cgas-bioinformatics/RESULTS.md`.

Two results matter.

**(a) No pseudoenzyme signature.**
[file:HETGA/Cgas/Cgas-bioinformatics/RESULTS.md "Every catalytically important residue that UniProt annotates on human cGAS is present and identical in the naked mole-rat protein"]
The catalytic Mg(2+) triad transfers as human E225/D227/D319 → **E257/D259/D351**; the
zinc thumb H390/C396/C397/C404 → **H422/C428/C429/C436**; the ATP/GTP/cGAMP contacts and
the nucleosome acidic-patch arginine anchor R255 → **R287** are all conserved. 12 of 15
annotated single-residue human sites are identical, 0 gapped; against mouse, 13 of 14.
The three substitutions are a GTP contact (T211→A243) and two N-terminal DNA-curvature
residues in the poorly conserved disordered arm — none catalytic. Overall identity is
ordinary orthologue-level:
[file:HETGA/Cgas/Cgas-bioinformatics/RESULTS.md "Global identity to human cGAS is 58.2% over aligned columns (55.2% to mouse)"]

The conserved arginine anchor is worth flagging separately: R287 is the residue that docks
cGAS onto the nucleosome acidic patch, so its retention is independently consistent with
the reported chromatin retention.

**(b) The four divergent residues are resolved and are regulatory, not catalytic.**
Secondary coverage of the Science paper names the four substitutions as S463D, E511K,
Y527L, T530K but does not state the numbering frame, and the primary abstract does not
name them at all — so I checked rather than repeated it. Read in **naked-mole-rat**
numbering the wild-type residues are exactly S463, E511, Y527, T530, and the aligned human
residues are exactly D431, K479, L495, K498 (mouse: D416, K464, L480, R483). So the named
series is a *humanising* one, which is self-consistent with the abstract's account of four
amino acids altered during evolution. And:
[file:HETGA/Cgas/Cgas-bioinformatics/RESULTS.md "All four positions fall inside the C-terminal Mab-21-like HhH/H2TH-like domain that UniProt annotates at 437-541 on A0AAX6RS70."]
[file:HETGA/Cgas/Cgas-bioinformatics/RESULTS.md "The divergence that reverses the HR phenotype sits in a C-terminal regulatory surface, not in the active site."]

This is the pivot of the whole review. It separates *what the protein can do* (unchanged)
from *how it is regulated on chromatin* (changed) — which is exactly why a single
propagated term flips sign while the rest of the set survives.

Limits are recorded honestly in RESULTS.md:
[file:HETGA/Cgas/Cgas-bioinformatics/RESULTS.md "it does not demonstrate that the naked mole-rat enzyme actually produces cGAMP, and no naked mole-rat biochemical assay of cGAMP synthesis was found in the cached literature"]

## 4. How each annotation was decided

The principle applied, stated once: **the molecular layer is verified, the immune-output
layer is not, and exactly one term is contradicted.**

- **Contradicted (1).** `GO:2000042` → `REMOVE`, replaced by a `NEW` row for
  `GO:1905168 positive regulation of double-strand break repair via homologous recombination`
  (id checked via QuickGO, not guessed). This is a genuine `REGULATORY_SIGN_INVERSION`
  at the target: the Euteleostomi node encoded "mammalian cGAS suppresses HR" from the two
  species that had been tested, and the naked mole-rat, though squarely inside that clade,
  does the opposite. Note the argument is *target-specific evidence of divergence*, which is
  the legitimate way to challenge a node — not "only two donors".
- **Verified molecular layer (7 `ACCEPT`).** GO:0061501, GO:0003690, GO:0003682, GO:0006974,
  GO:0005634, GO:0035861, GO:0005829. Each is either directly evidenced in the naked
  mole-rat abstract (chromatin binding, DNA damage response, nuclear action on damaged
  chromatin) or underwritten by the residue-conservation result plus an unchallenged node.
- **Untested immune-output layer (4 `UNDECIDED`).** GO:0002218, GO:0002230, GO:0032481,
  GO:0071360. No naked-mole-rat study has tested DNA sensing, STING, interferon, antiviral
  defence or dsRNA response; the abstracts are silent. I am *not* claiming these are wrong —
  the node support is good and the enzyme machinery is intact. But there is also a concrete,
  species-specific reason not to simply wave them through: in human and mouse, chromatin-
  and nucleosome-tethered cGAS is the *inactive* pool (the acidic-patch interaction locks
  cGAS as an inactive monomer), so a variant selected to sit on chromatin *longer* could
  plausibly have a smaller free pool available for cytosolic sensing. That is a hypothesis,
  not a finding, and it belongs in `suggested_experiments`, but it is why `UNDECIDED` rather
  than `ACCEPT` is the honest call for this arm.
- **Peripheral (1 `KEEP_AS_NON_CORE`).** GO:0038001 paracrine signaling — cGAMP transfer to
  neighbouring cells is a real but secondary consequence even in human and mouse, and it
  depends on the same untested cGAMP axis.

Final counts: ACCEPT 7 · UNDECIDED 4 · KEEP_AS_NON_CORE 1 · REMOVE 1 · NEW 1 (14 rows).

### Why no `NEW` annotation for the ageing phenotype

The abstract does support an anti-ageing role
([PMID:41066557 "Moreover, the four amino acids mediate the function of cGAS in antagonizing cellular and tissue aging and extending life span."]),
and terms such as `GO:2000773 negative regulation of cellular senescence` exist. I did not
propose one. Lifespan extension and reduced senescence here are the downstream, indirect
consequence of better HR repair, demonstrated by a gain-of-function substitution series;
the schema is explicit that `NEW` should not be used for indirect or pleiotropic effects.
`GO:1905168` captures the actual mechanism, and the ageing phenotype is recorded in the
description and in `suggested_questions` instead.

## 5. Provider recall: what the two deep-research records contributed, and what they missed

### falcon — thorough on mechanism, and it missed the one paper that matters

A falcon report (`Cgas-deep-research-falcon.md`) landed partway through this review. It is
careful and well disciplined: it verifies gene identity, separates "direct other-mammal"
from "inference" in a per-claim table, and refuses to attribute naked-mole-rat longevity to
this protein without evidence. It contributes one thing nothing else in the folder does —
quantitative grounding for the claim that chromatin-bound cGAS is the *restrained* pool:
[file:HETGA/Cgas/Cgas-deep-research-falcon.md "A 2024 authoritative review reports that nuclear cGAS can constitute approximately **85–95%** of total cGAS in some cell types."]
[file:HETGA/Cgas/Cgas-deep-research-falcon.md "mouse R241E generated about **300-fold** more basal cGAMP than wild type, and human R255E generated over **100-fold** more"]

That second number is directly load-bearing here, because R255 is the arginine anchor I had
already shown to be conserved as **R287** in the naked-mole-rat protein. So the residue that
keeps chromatin-bound cGAS catalytically silent is intact in this species, which turns my
caveat on the interferon arm from a hand-wave into a specific mechanistic worry: the
naked-mole-rat adaptation makes the protein spend *longer* in the restrained state.

**But falcon missed the decisive paper entirely.** It states:
[file:HETGA/Cgas/Cgas-deep-research-falcon.md "the literature search found **no direct biochemical, localization, structural, knockout, or substrate-specificity study of A0AAX6RS70 or XP_021099394.1 itself**"]
[file:HETGA/Cgas/Cgas-deep-research-falcon.md "There is no verified naked-mole-rat kinetic constant, catalytic rate, DNA-length response curve, product measurement, structure, tissue-expression map, or subcellular localization for this accession."]

PMID:41066557 is exactly such a study, is in *Science*, and is **already cached in this
repository**. Falcon's whole section 8 ("Naked-mole-rat-specific interpretation") is built on
the premise that no species-specific functional work exists, and it explicitly advises that
noncanonical nuclear functions "should not yet be incorporated into the core annotation of
A0AAX6RS70" — advice that is precisely backwards for this gene. Following the falcon report
alone would have produced a review with no `REMOVE`, no `NEW`, and an accepted GO:2000042.

This is a clean, quantifiable recall failure on a paper that is neither obscure nor old, and
it is worth logging as such: the report's *precision* is fine (nothing it asserts is wrong
about mammalian cGAS), but its *recall* on the target species was zero, and it converted that
gap into a confident negative claim rather than a hedge. It is marked `LOW_QUALITY` in
`references[].reference_review` for that reason, not for any incorrect mechanism.

### affinage (human ortholog)

`Cgas-deep-research-affinage-human-ortholog.md` is the affinage record for **human CGAS**
(Q8N884) — affinage refuses non-human species — used here only as a conserved-mechanism
baseline. It is a good one: 27 dated, citation-anchored findings, and it independently
supplies the human-side half of the central comparison, including the very paper the
naked-mole-rat work inverts (PMID:30356214, nuclear cGAS suppresses HR via PARP1) and the
nucleosome acidic-patch/arginine-anchor structural work (PMID:32911482, PMID:32913000) that
makes my "chromatin-bound cGAS is the inactive pool" caveat mechanistically concrete rather
than hand-waved.

**What it necessarily missed, being human-only:** everything about this species. It has no
naked-mole-rat content at all — not the sign reversal, not TRIM41, not p97, not the
FANCI–RAD50 step, not the four C-terminal residues. That is not a recall failure on
affinage's part; it is the species restriction doing exactly what the brief warned about.
The practical consequence for provider-recall accounting: **a human-ortholog record cannot
surface the finding that makes this gene interesting, and on its own would have led to
`ACCEPT` on GO:2000042 — the one call that is affirmatively wrong.**

Worth noting the contrast: affinage failed to find the naked-mole-rat paper *by design*
(wrong species), whereas falcon was pointed at the right species and still failed to find it.
Only one of those is a retrieval defect.

Per the brief I did not import its `mechanism_profile` GO ids (they collapse to coarse
parents such as GO:0016740 transferase activity and GO:0003677 DNA binding, both less
informative than what GOA already carries), and no affinage sentence is used as
`supporting_text` anywhere.

## 6. Unresolved

1. **Does naked-mole-rat cGAS make cGAMP?** Machinery intact, activity never assayed in
   this species. The single most valuable missing experiment.
2. **Is the STING/type-I-interferon arm functional in the naked mole-rat?** Entirely
   untested; drives four `UNDECIDED` calls.
3. **`PTN000069395` could not be resolved** to an assertion node — it carries no IBD in the
   local PTHR10656 PAINT slice, consistent with it being the TreeGrafter graft point. The
   assertions it inherits were traced instead to `PTN002579681` and `PTN000838114`.
4. **The four-residue identities rest on a secondary summary for their *functional* claim.**
   I verified the positions, residues and numbering frame from sequence, and the abstract
   independently states that four amino acids changed — but the abstract does not name them,
   so the mapping of "four amino acids" to specifically 463/511/527/530 is corroborated, not
   proven, and is flagged as such in RESULTS.md and in the review.
5. **No full text for any of the four cGAS papers**, so no assay details, cell types or
   residue-level mechanism beyond the abstract were available.
