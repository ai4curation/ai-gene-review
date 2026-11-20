---
title: "GO annotation guidelines (de novo)"
maturity: SCOPING
tags: [PIPELINE]
autolink_gene_symbols: false
---

# GO annotation guidelines (de novo)

**Bottom line:** this project writes a new, detailed set of Gene Ontology (GO)
annotation guidelines. The sources are the GO Consortium's own documentation and
the rules this repository has worked out in review. The existing GO guidance is
spread over about 22,000 wiki pages, Drive documents, GitHub issues and papers,
and much of it is unclear, contradictory or out of date. We first inventoried all
of it ([sources](GO_GUIDELINES/sources/SOURCES.md)), then wrote 16 topic
guidelines with 274 numbered rules. Each document cites the original sources
where possible. It states plainly where we depart from them: 218 rows of
"differences from prior guidance", and 112 open questions for the GOC to decide.

Status: **draft v0.1 (2026-11-15)**. The documents were drafted by AI from the
inventoried sources and repository rules, with every GO id and label checked
against the ontology. No GOC curator has reviewed them yet. Read them as a
proposal.

## The guidelines

Every rule has a stable id (for example [MF-5](GO_GUIDELINES/guidelines/molecular-function.md#mf-5)),
a one-line normative statement, a rationale, worked examples with verified GO
ids, sources, and a provenance tag:

- **[GOC]** restates current, documented GO Consortium guidance.
- **[GOC+]** clarifies, sharpens or extends it.
- **[NEW]** is our own synthesis, absent from GOC guidance or departing from it.

| Document | Rules | Differences | Open questions | Scope |
|---|---|---|---|---|
| [Evidence codes](GO_GUIDELINES/guidelines/evidence-codes.md) | EV-1–16 | 13 | 6 | choosing codes and ECO classes; IPI, IGI, IEP, HTP, IC, TAS, ND |
| [From paper to annotation](GO_GUIDELINES/guidelines/from-paper-to-annotation.md) | LIT-1–14 | 13 | 5 | assay → aspect and depth; overexpression; negative results; what not to annotate |
| [Molecular function](GO_GUIDELINES/guidelines/molecular-function.md) | MF-1–18 | 15 | 7 | activity vs binding; protein binding; enzymes and promiscuity; pseudoenzymes; transporters; regulators |
| [Transcription regulation](GO_GUIDELINES/guidelines/transcription-regulation.md) | TR-1–16 | 14 | 8 | dbTF vs coTF vs GTF; DNA-binding evidence; chromatin proteins; bacterial and plant regulators |
| [Biological process](GO_GUIDELINES/guidelines/biological-process.md) | BP-1–15 | 14 | 6 | participation vs necessity; acts upstream of; phenotypes; development; precomposed terms |
| [Regulation and signaling](GO_GUIDELINES/guidelines/regulation-and-signaling.md) | RS-1–14 | 13 | 7 | part of vs regulation of; sign; pathway boundaries; ligands and receptors; response to |
| [Cellular component](GO_GUIDELINES/guidelines/cellular-component.md) | CC-1–19 | 15 | 8 | CC relations; organelles and sub-compartments; transit; topology; HTP localization; condensates |
| [Protein complexes](GO_GUIDELINES/guidelines/protein-complexes.md) | PC-1–16 | 14 | 8 | complex membership; enables vs contributes_to; assembly factors; oligomerization |
| [Qualifiers and negation](GO_GUIDELINES/guidelines/qualifiers-and-negation.md) | QN-1–16 | 12 | 8 | the gp2term relations; NOT annotations and conflicts |
| [Annotation extensions](GO_GUIDELINES/guidelines/annotation-extensions.md) | AE-1–14 | 12 | 7 | has_input, occurs_in, part_of, happens_during; extension vs new term |
| [Phylogenetic propagation](GO_GUIDELINES/guidelines/phylogenetic-propagation.md) | PH-1–20 | 14 | 6 | PAINT IBD/IBA/IKR/IRD; ISO/ISS; when propagation must stop |
| [Electronic annotation](GO_GUIDELINES/guidelines/electronic-annotation.md) | IEA-1–16 | 11 | 6 | InterPro2GO, keywords, UniRule/ARBA, EC/Rhea mappings; fixing a mapping |
| [GO-CAM modeling](GO_GUIDELINES/guidelines/gocam-modeling.md) | CAM-1–19 | 17 | 7 | activity units; causal relations; complexes; compartments; evidence per edge |
| [Multi-organism and ncRNA](GO_GUIDELINES/guidelines/multi-organism-and-ncrna.md) | MO-1–21 | 16 | 8 | host/symbiont terms; effectors; immunity; miRNA, lncRNA and guide RNAs |
| [Reviewing annotations](GO_GUIDELINES/guidelines/reviewing-annotations.md) | REV-1–20 | 12 | 7 | judging claims; review actions; deferring to curators; retractions; source defects |
| [Ontology change and taxa](GO_GUIDELINES/guidelines/ontology-change-and-taxa.md) | ONT-1–20 | 13 | 8 | obsoletion and replaced_by; term requests; taxon constraints |

## Principles that run through all of them

The documents were written separately, but the same few ideas recur. They are
the core of what we think GO best practice is.

1. **An annotation is a claim about what the gene product does.** Judge it as a
   claim, not by its evidence code. Rows that share a term reinforce one another
   and get consistent actions ([REV-1](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-1),
   [EV-16](GO_GUIDELINES/guidelines/evidence-codes.md#ev-16)).
2. **Participation, not necessity.** `involved_in` needs a step the product
   performs. A knockout phenotype shows necessity and supports, at most, `acts
   upstream of or within` the most proximal process
   ([BP-1](GO_GUIDELINES/guidelines/biological-process.md#bp-1),
   [BP-4](GO_GUIDELINES/guidelines/biological-process.md#bp-4),
   [LIT-8](GO_GUIDELINES/guidelines/from-paper-to-annotation.md#lit-8),
   [QN-3](GO_GUIDELINES/guidelines/qualifiers-and-negation.md#qn-3)).
3. **Activities, not bindings.** Bare protein binding is uninformative. A binding
   term is a fallback for when the activity the binding serves is unknown
   ([MF-3](GO_GUIDELINES/guidelines/molecular-function.md#mf-3),
   [MF-5](GO_GUIDELINES/guidelines/molecular-function.md#mf-5),
   [CAM-4](GO_GUIDELINES/guidelines/gocam-modeling.md#cam-4)).
4. **Depth follows this row's own evidence.** Annotate the deepest term the
   evidence reaches and no deeper. A correct but general term is refined only on
   evidence that reaches the specific term
   ([MF-2](GO_GUIDELINES/guidelines/molecular-function.md#mf-2),
   [BP-13](GO_GUIDELINES/guidelines/biological-process.md#bp-13),
   [REV-3](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-3)).
5. **Attribute the activity to the entity that performs it.** This applies to the
   subunit vs the complex, the enzyme vs its substrate, the regulator vs the
   regulated, and the symbiont vs the host
   ([PC-5](GO_GUIDELINES/guidelines/protein-complexes.md#pc-5),
   [BP-2](GO_GUIDELINES/guidelines/biological-process.md#bp-2),
   [MO-3](GO_GUIDELINES/guidelines/multi-organism-and-ncrna.md#mo-3)).
6. **Inferred annotations are arguments, and you argue with their premise.**
   - An IBA is challenged at its PAINT node, not by its donor count.
   - An IEA is challenged at its mapping.
   - A fix goes to the source in a form the source can use.

   See [PH-1](GO_GUIDELINES/guidelines/phylogenetic-propagation.md#ph-1),
   [IEA-11](GO_GUIDELINES/guidelines/electronic-annotation.md#iea-11) and
   [REV-17](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-17).
7. **Correct, don't delete.**
   - A true claim with the wrong relation, an over-general term or a stale
     obsolete id is corrected as structured data.
   - `REMOVE` is for claims that are contradicted, or demonstrably wrong.

   See [QN-7](GO_GUIDELINES/guidelines/qualifiers-and-negation.md#qn-7),
   [BP-14](GO_GUIDELINES/guidelines/biological-process.md#bp-14) and
   [ONT-7](GO_GUIDELINES/guidelines/ontology-change-and-taxa.md#ont-7).
8. **Defer to what you have not seen; never manufacture what you cannot support.**
   - A reviewer without the full text does not overrule an experimental curator.
   - `NEW` is held to a higher bar than any other action.

   See [REV-8](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-8),
   [LIT-13](GO_GUIDELINES/guidelines/from-paper-to-annotation.md#lit-13) and
   [REV-11](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-11).

## Headline departures from prior guidance

A selection. Each document's "Differences from prior guidance" table has the full
list with sources.

| Rule | Prior guidance | What we recommend |
|---|---|---|
| [EV-3](GO_GUIDELINES/guidelines/evidence-codes.md#ev-3) | wiki: IPI may support processes "by association" | IPI supports binding and complex terms. It supports a regulator MF only with a measured effect on the partner, and a BP only alongside evidence of the product's own activity |
| [QN-3](GO_GUIDELINES/guidelines/qualifiers-and-negation.md#qn-3) | defaults differ: wiki `acts_upstream_of_or_within`, GOA/Protein2GO `involved_in`, GAF 2.2 left it open | read an unqualified BP as `acts_upstream_of_or_within`; assert `involved_in` only when the MF can be named |
| [BP-4](GO_GUIDELINES/guidelines/biological-process.md#bp-4) / [QN-7](GO_GUIDELINES/guidelines/qualifiers-and-negation.md#qn-7) | wiki: phenotype-based annotations "should be reviewed and removed" | correct the relation as structured data and keep the true claim |
| [RS-8](GO_GUIDELINES/guidelines/regulation-and-signaling.md#rs-8) | wiki: ligand availability counts as regulation of the pathway | ligands are part of the pathway they start; biogenesis and secretion get their own terms (follows FlyBase practice) |
| [RS-10](GO_GUIDELINES/guidelines/regulation-and-signaling.md#rs-10) | FlyBase-only convention | regulation does not cross transcription, for all groups |
| [PH-11](GO_GUIDELINES/guidelines/phylogenetic-propagation.md#ph-11) | go-annotation#2042: no IBA should list its own target in WITH/FROM | self-reference is expected and is not circular |
| [IEA-2](GO_GUIDELINES/guidelines/electronic-annotation.md#iea-2) | InterPro (2007, go-annotation#385): keep enzyme mappings on families with a few inactive members | a signature mapping must hold for every member; use a conditional rule when only a condition separates right from wrong members |
| [PC-7](GO_GUIDELINES/guidelines/protein-complexes.md#pc-7) | wiki: all ATP synthase components `contributes_to` the activity | only subunits whose part is in the mechanism; accessory and structural subunits get their own MF or none |
| [CC-3](GO_GUIDELINES/guidelines/cellular-component.md#cc-3) | PAINT emits `is_active_in` by default | a pipeline-default `is_active_in` counts as no stronger than `located_in` |
| [CAM-8](GO_GUIDELINES/guidelines/gocam-modeling.md#cam-8) | 2023 relations page allows direct edges for small-molecule effects | "directly" only between activities of different gene products; small-molecule effects go through a ChEBI node |
| [MO-3](GO_GUIDELINES/guidelines/multi-organism-and-ncrna.md#mo-3) | go-annotation#1367 allowed viral-process terms on co-opted host factors; later issues did not | co-opted host proteins never get viral or symbiont process terms |
| [REV-15](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-15) | planned GORULE:0000022 blanket filter on retracted papers | flag the citation, then act on each evidence line separately |
| [ONT-3](GO_GUIDELINES/guidelines/ontology-change-and-taxa.md#ont-3) / [ONT-5](GO_GUIDELINES/guidelines/ontology-change-and-taxa.md#ont-5) | `replaced_by` treated as safe to apply mechanically | check each annotation; a cross-aspect replacement is always a `consider` |
| [ONT-17](GO_GUIDELINES/guidelines/ontology-change-and-taxa.md#ont-17) | taxon-constraint violations are filtered | decide which is wrong, the annotation or the constraint; the RAR re-examination found about a quarter of the constraints it tested too narrow |

## Defects found in this repository along the way

Writing the guidelines surfaced several places where the repository contradicts
its own rules or GOC guidance. Each is filed as an issue; none is fixed in this PR.

- **Qualifier descriptions** ([#6440](https://github.com/ai4curation/ai-gene-review/issues/6440)).
  `AnnotationQualifierEnum` in `src/ai_gene_review/schema/gene_review.yaml`
  describes `acts_upstream_of` as "acts upstream of or within", which conflates
  two RO relations, and describes `colocalizes_with` only as weaker than `located_in`.
- **`contributes_to` for non-catalytic subunits** ([#6441](https://github.com/ai4curation/ai-gene-review/issues/6441)).
  The schema example and #4237 give accessory subunits `contributes_to` the
  complex activity; [PC-7](GO_GUIDELINES/guidelines/protein-complexes.md#pc-7),
  following the GOC Complex Working Group, does not. This needs a maintainer
  decision. NDUFS4 (core `GO:0008137` on a supernumerary subunit) and UQCRC1
  (core `GO:0008121` on a subunit its own text calls structural) are wrong under
  either reading. COX4I1 accepts a TAS `enables GO:0004129` row while its reason
  argues for `contributes_to`. PSMA1's core `contributes_to` endopeptidase turns
  on the decision.
- **Missing doc** ([#6442](https://github.com/ai4curation/ai-gene-review/issues/6442)).
  `CLAUDE.md` links `docs/isoform_tracking.md`, which does not exist.
- **Protein-binding policy** ([#6443](https://github.com/ai4curation/ai-gene-review/issues/6443)).
  `MOLECULAR_ADAPTOR_ACTIVITY` says the policy prefers MODIFY; the policy
  docstring makes REMOVE the default. [MF-5](GO_GUIDELINES/guidelines/molecular-function.md#mf-5)
  and [REV-13](GO_GUIDELINES/guidelines/reviewing-annotations.md#rev-13) follow
  the docstring: MODIFY when the row's own paper supports an informative MF,
  otherwise REMOVE.
- **Obsolete scaffold term** ([#6444](https://github.com/ai4curation/ai-gene-review/issues/6444)).
  `MOLECULAR_ADAPTOR_ACTIVITY` uses `GO:0032947` as the out-of-branch scaffold
  exclusion; it is obsolete in the 2026-11-03 build, and `GO:0140378` protein
  complex scaffold activity is the live term.

## Open questions for the GOC

Each document ends with its own open questions, 112 in all. The themes that
recur across documents:

1. **Default BP relation.** What a BP annotation with no stated relation means,
   and whether GO should export `acts_upstream_of_or_within` as the default. See
   QN, BP and RS.
2. **The 2026 obsoletions.** Whether the announced protein-binding and
   oligomerization obsoletions go ahead: `GO:0042803` and `GO:0051259` are still
   live in the release used here. See MF and PC.
3. **Scoped negation and the `contributes_to` export.** How to express a negation
   with limited scope, as for COQ8B. Whether `contributes_to` should be exported
   from emergent complex activities in GO-CAM. See QN and CAM.
4. **A qualifier for "response to".** A way to separate "acts in the response"
   from "is induced during it". See EV, RS and BP.
5. **Fixing pipelines.** What replaces SubCell2GO, EC2GO and KW2GO coverage for
   unreviewed entries, and whether interpro2go should support conditions. See IEA.
6. **Taxon constraints for viruses.** The 2015 and 2017 sources conflict. Also
   how to record the interacting taxon in mixed host-symbiont models. See ONT,
   MO and CAM.

## Sources and how this was made

- **Inventory.** [sources/SOURCES.md](GO_GUIDELINES/sources/SOURCES.md) describes
  the exhaustive, receipted inventory of the GO Drive, GO wiki, papers and books,
  and the `geneontology/go-annotation` repository.
  - Every item has a relevance score (1-5) and a rationale.
  - [top-sources.md](GO_GUIDELINES/sources/top-sources.md) lists tallies and every
    item scored 5.
  - [key-sources.yaml](GO_GUIDELINES/sources/key-sources.yaml) has every item
    scored 4 or 5 (1,550 items).
  - The full per-item receipts (about 22,000 items, 11 MB) are kept out of git,
    in `GO_GUIDELINES/sources/receipts/`. The scripts that built them are in
    `GO_GUIDELINES/sources/scripts/`.
- **Drafting.** The full text of every item scored 3-5 was assembled into a
  corpus. Each topic document was drafted from that corpus, from the repository's
  own policy pages and from `CLAUDE.md`.
  - Every GO, ECO, RO and CL id was checked with OAK against the local GO build
    (2026-11-03).
  - PMIDs come only from the corpus or repository pages.
- **Citation links.** Drive links are internal to the GO Consortium. Wiki links
  point to wiki.geneontology.org.
- **Ontology state.** A few statements about term status (for example, that
  `GO:0005615` extracellular space is obsolete) reflect that build. QuickGO may be
  ahead of it.

## Next steps

1. Curator review of each document, starting with the [NEW] rules and the
   Differences tables. Record sign-offs under `manual_reviews` in this page's
   frontmatter.
2. Resolve the cross-document overlaps: the CC/QN rules on `colocalizes_with` and
   `is_active_in`, and the PC/QN/MF rules on `contributes_to`. They agree at
   present, but each topic currently restates them.
3. Feed settled rules back into `CLAUDE.md` and the validators, and fix the
   repository defects listed above.
4. Take the open questions to the GO annotation call.
