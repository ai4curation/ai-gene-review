# Family review: PANTHER PTHR48034 (RNA-binding motif / RBM; InterPro IPR050441)

## Why this review exists

During the review of human **CIRBP** (Q14011), two IBA annotations were flagged as
over-annotations:

- `GO:0000398` mRNA splicing, via spliceosome (IBA, GO_REF:0000033)
- `GO:0005681` spliceosomal complex (IBA, GO_REF:0000033)

CIRBP has **no experimental evidence** of a splicing function; its characterized
activities are 3'-UTR binding, mRNA stabilization, and translational control. This
document reviews the PANTHER family CIRBP was placed in, and the model-organism
("mod") genes whose **experimental** annotations were propagated by descent to
produce the incorrect CIRBP splicing IBA.

## The family is functionally heterogeneous

PTHR48034 ("RNA-binding motif", RBM; integrated into InterPro IPR050441) is a large
(15,656 proteins; 26 subfamilies), RRM-containing family that the InterPro/PANTHER
description itself flags as mixing several distinct RNA-metabolism roles
("pre-mRNA splicing, mRNA stabilization, and transcription regulation … proteins that
function in spermatogenesis and sex determination, as well as those that respond to
temperature changes by modulating mRNA stability and translation").

Two functionally divergent groups sit inside the family:

| Group | Representative members | Established core function |
|---|---|---|
| **Transformer-2 / RBMX / SR-like splicing regulators** | TRA2B (P62995), TRA2A (Q13595), RBMX/hnRNP G (P38159), *Drosophila* tra2 (P19018/FBgn0003742), rat Tra2b (P62997), SRSF10 (O75494), RBMY paralogs | Sequence-specific **pre-mRNA (alternative) splicing** regulation; part of spliceosomal/nuclear-speckle machinery |
| **Cold-inducible mRNA-stability / translation proteins** | CIRBP (Q14011; mouse P60824; rat P60825; *Xenopus* cirbp-a O93235), RBM3 (mouse O89086) | RRM + glycine-rich/RGG C-terminus; **3'-UTR binding, mRNA stabilization, translational control**, stress-granule recruitment. **Not** splicing factors |

Both groups share the N-terminal RRM, which is why PANTHER groups them; but the
C-terminal architecture differs (an arginine-serine/RS-type domain in the TRA2/SR
splicing factors vs. a glycine-rich/RGG domain in CIRBP/RBM3), tracking the functional
divergence.

## How the bad IBA was produced (PANTHER PAINT node analysis)

PAINT (PANTHER's phylogenetic annotation, file
`interpro/panther/PTHR48034/PTHR48034-paint.tsv`) assigns IBD (inferred-by-descent)
annotations to internal tree nodes; these descend to leaves as IBA. The relevant nodes:

- **Node PTN000391532** — carries the splicing terms:
  - `GO:0000398` mRNA splicing, via spliceosome — IBD seeds:
    `FB:FBgn0003742` (Dros tra2), `UniProtKB:Q13595` (TRA2A), `UniProtKB:P62995` (TRA2B),
    `RGD:1306751`, `RGD:1565256` (rat Tra2)
  - `GO:0005681` spliceosomal complex — IBD seeds:
    `UniProtKB:P62995` (TRA2B), `UniProtKB:P38159` (RBMX), `RGD:1306751` (rat Tra2)
- **Node PTN008729690** — the CIRBP/RBM3-containing subfamily node — carries **only**:
  - `GO:0003729` mRNA binding — IBD seeds include `UniProtKB:Q14011` (CIRBP itself),
    `O93235` (Xenopus cirbp-a), plus RBMX/TRA2B/RBMY

CIRBP's GOA row for the splicing IBA names the source node explicitly in its WITH/FROM:
`PANTHER:PTN000391532|FB:FBgn0003742|RGD:1306751|RGD:1565256|UniProtKB:P62995|UniProtKB:Q13595`.

**The error:** the splicing IBD annotations are anchored *only* by transformer-2/RBMX
splicing factors at the ancestral node PTN000391532, but were propagated down to the
diverged cold-shock branch (CIRBP/RBM3). The annotation crosses a functional-divergence
boundary: CIRBP's own subfamily node (PTN008729690) is annotated only with the generic,
correct `mRNA binding`. PAINT curators *did* prune annotations in other branches of this
family (e.g. node PTN001924395 carries IRD "NOT" records blocking `GO:0003729`,
`GO:0000381`, `GO:0016607`), so the absence of a pruning/NOT on the CIRBP branch for the
splicing terms is the gap that produced the over-annotation.

## Review of the mod (model-organism) seed genes — all are genuine splicing factors

The propagation source genes are correctly annotated; the problem is the propagation
target, not the seeds. Verified from UniProt and experimental GO evidence:

- **TRA2B / human (P62995, Transformer-2 protein homolog beta).** UniProt FUNCTION:
  "Sequence-specific RNA-binding protein which participates in the control of pre-mRNA
  splicing. Can either activate or suppress exon inclusion. Acts additively with RBMX to
  promote exon 7 inclusion of the survival motor neuron SMN2. Activates the splicing of
  MAPT/Tau exon 10." Falcon deep research (file:human/TRA2B/TRA2B-deep-research-falcon.md)
  likewise places it firmly in splicing — "Belongs to the splicing factor SR family" and a
  regulator of "pre-mRNA splicing, where it interacts with the spliceosome and other
  SR-domain-containing proteins." Has **direct experimental** splicing annotations: `GO:0000398`
  mRNA splicing via spliceosome (IDA, PMID:9546399), `GO:0000381` regulation of
  alternative mRNA splicing (IDA PMID:12165565, PMID:12761049; IMP PMID:25689357),
  `GO:0005681` spliceosomal complex (IMP PMID:25689357), `GO:0048026` positive regulation
  of mRNA splicing (IDA PMID:15009664). Anchor seed for both splicing terms.
- **TRA2A / human (Q13595, Transformer-2 protein homolog alpha).** UniProt FUNCTION:
  "Sequence-specific RNA-binding protein which participates in the control of pre-mRNA
  splicing" (PMID:9546399). Seed for `GO:0000398`.
- **RBMX / human (P38159, hnRNP G).** UniProt FUNCTION: RNA-binding protein involved in
  "regulation of … alternative splicing"; a recognized splicing regulator (acts with
  TRA2B on SMN2 exon 7). Seed for `GO:0005681`. (Note: RBMX also appears as an IntAct
  interactor of CIRBP — a separate, legitimate protein-binding record.)
- **tra2 / *Drosophila melanogaster* (P19018, FBgn0003742).** UniProt FUNCTION:
  "Required for female sex determination in somatic cells and specific splicing and/or
  polyadenylation of doublesex (dsx) pre-mRNA." The classical sex-determination splicing
  regulator. Seed for `GO:0000398`.
- **rat Tra2 (RGD:1306751, RGD:1565256; cf. rat Tra2b P62997).** Rat orthologs of the
  transformer-2 splicing factors; UniProt (P62997, Tra2b/Sfrs10) FUNCTION matches human
  TRA2B (pre-mRNA splicing; SMN2; MAPT/Tau). Seeds for both splicing terms.

## Conclusion and recommendation

- The PTHR48034 splicing IBA on **CIRBP** (and by the same logic on **RBM3** and other
  cold-shock-branch members) is an **over-annotation** caused by IBD propagation of
  transformer-2/RBMX splicing evidence across a functional-divergence boundary. This
  supports the `MARK_AS_OVER_ANNOTATED` action recorded in the CIRBP review for
  `GO:0000398` and `GO:0005681`.
- The seed/mod genes themselves are **correctly** annotated as splicing factors and need
  no change.
- **Upstream fix (PANTHER PAINT):** the cleanest correction is at the tree, not the leaf —
  the CIRBP/RBM3 subfamily branch (node PTN008729690 and its descendants) should carry an
  IRD/NOT (or a more restrictive re-annotation) for the splicing terms `GO:0000398` and
  `GO:0005681`, mirroring how PAINT already pruned other branches of this family. This
  would stop the splicing terms from descending to the cold-inducible mRNA-stability
  members.

## Sources / data files

- `genes/human/CIRBP/CIRBP-goa.tsv` (CIRBP GOA, WITH/FROM source nodes)
- `interpro/panther/PTHR48034/PTHR48034-metadata.yaml` (family description)
- `interpro/panther/PTHR48034/PTHR48034-entries.csv` (reviewed members)
- `interpro/panther/PTHR48034/PTHR48034-paint.tsv` (PAINT node-level IBD/IBA/IRD)
- UniProt: Q14011 (CIRBP), P62995/Q13595 (TRA2B/TRA2A), P38159 (RBMX), P19018 (Dros tra2),
  P62997 (rat Tra2b)
- `genes/human/TRA2B/TRA2B-deep-research-falcon.md` (falcon deep research on the anchor
  seed gene; see TRA2B folder)
