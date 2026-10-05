# NDUFS2 curation notes

## 2026-09-04 — PAINT no-IBA project finishing pass (AI-assisted)

Reviewed every entry in `NDUFS2-ai-review.yaml`, checked the top-level `description`
and `core_functions`, cleared all validation warnings, and wrote the accompanying
family review at `interpro/panther/PTHR11993/PTHR11993-review.yaml`. Status moved
`IN_PROGRESS` → `COMPLETE`.

### Changes made

1. **`GO:0016651` (oxidoreductase activity, acting on NAD(P)H), IEA — `MODIFY` → `ACCEPT`.**
   The draft proposed replacing it with `GO:0048038` (quinone binding). That is not a
   refinement but a substitution of a different molecular function, which is not what
   `MODIFY` means. `GO:0016651` is a direct parent of `GO:0008137`, which this review
   accepts on four independent evidence lines, so rejecting the parent while accepting
   the child was also internally inconsistent — and the equally broad `GO:0016491` was
   already being accepted. Kept as a redundant parent, with the real caveat recorded in
   the summary: NDUFS2 does not itself contact NAD(P)H. The quinone-site function is
   captured directly by the `GO:0048039` `NEW` annotation instead.

2. **`GO:0051287` (NAD binding), IEA — `REMOVE` retained, and now supported at family
   level.** The InterPro signature set on NDUFS2 (IPR001135, IPR014029, IPR022885,
   IPR029014) is *identical* to that of poplar plastid ndhH (A4GYX2), which receives
   the same `GO:0051287` InterPro2GO annotation — on a protein whose complex has no
   N-module and cannot oxidise NADH at all. This is a family-wide mapping error, not a
   per-gene one, and it is now recorded as `scope: NOT_APPLICABLE` in the PTHR11993
   family review.

3. **`description` — removed database commentary.** "UniProt annotates one [4Fe-4S]
   cluster … by similarity" is curation commentary, not biology. Rewritten as a
   biological statement: the cluster assignment follows from the NiFe-hydrogenase
   large-subunit fold NDUFS2 retains, no structure of mammalian complex I places a
   cluster on this subunit, and the terminal N2 cluster is ligated by NDUFS7.

4. **`core_functions.locations` — added `GO:0005743`** alongside `GO:0005759`. NDUFS2 is
   a peripheral inner-membrane protein on the matrix side; both terms are already in
   `existing_annotations` with experimental support.

5. **Two `references[].findings` supporting_text quotes fixed** (PMID:30922174). The
   quotes contained UniProt-style bracketed expansions such as
   `[nicotinamide adenine dinucleotide]`, which the reference validator strips as
   citation markers before matching, so the residual string was not a substring of the
   cached abstract. Replaced with verbatim fragments. File now validates with zero
   warnings.

### Bioinformatics done for this pass (reproducible)

Global BLOSUM62 alignment (BioPython `PairwiseAligner`, gap open −11 / extend −1) of
O75306 against P17694 (bovine NDUFS2), P33599 (*E. coli* NuoCD), P93306 (*Arabidopsis*
NAD7) and A4GYX2 (poplar plastid ndhH), each fetched from the UniProt REST API. Every
mapped position was re-confirmed by direct indexing of the fetched sequence.

**The UniProt [4Fe-4S] cysteine triad does not survive conservation analysis.** UniProt
lists Cys326/Cys332/Cys347 as ligands on `ECO:0000255` (by-similarity) evidence. Three
ligands is one short of what a [4Fe-4S] cluster requires, and the middle position is not
a cysteine outside the animal orthologues:

| protein | ↔ C326 | ↔ C332 | ↔ C347 |
|---|---|---|---|
| O75306 human NDUFS2 | C326 | C332 | C347 |
| P17694 bovine NDUFS2 | C326 | C332 | C347 |
| P93306 *A. thaliana* NAD7 | C257 | **I263** (a Cys sits one position earlier, C262) | C278 |
| P33599 *E. coli* NuoCD | C459 | **L465** | C480 |
| A4GYX2 poplar ndhH | **S257** | **V263** | **A278** |

Since *E. coli* NuoD and *Arabidopsis* NAD7 are bona fide respiratory 49 kDa subunits,
the loss is not a plastid peculiarity. Together with the absence of any cluster on this
subunit in the structural record, this supports reading the site as the vestigial
[NiFe] hydrogenase metal centre. Recorded as the `vestigial_hydrogenase_cys` residue
site in the family review at `strength: ASSOCIATED`, with P33599 (L465) and A4GYX2
(V263) as negative controls, deliberately as a brake on future propagation. The
`GO:0051536` / `GO:0051539` annotations were nonetheless left as `ACCEPT`, deferring to
the UniProt cofactor annotation that generates them, with the caveat stated in each
`reason`.

**The quinone-site His/Tyr pair is invariant and quinone-generic.** The "His59/Tyr108"
of the complex I literature is mature-chain numbering; the precursor equivalents are
His92/Tyr141 (O75306 carries a 33-residue transit peptide). Both are conserved in
bovine NDUFS2 (H92/Y141), *E. coli* NuoCD (H224/Y273), *Arabidopsis* NAD7 (H23/Y72) and
poplar plastid ndhH (H23/Y72). Because the pair is present in the plastoquinone-reducing
plastid member, it supports acceptor-neutral `GO:0048038` rather than `GO:0048039`
[file:human/NDUFS2/NDUFS2-deep-research-falcon.md, "NDUFS2 lines the amphipathic
Q-channel and contributes the conserved His/Tyr ligand pair (His59, Tyr108) that
interacts with the quinone headgroup and small-molecule Q-site ligands"].

**Arg118 (mature Arg-85) is conserved far beyond the enzyme that modifies it** — present
in bovine (R118), NAD7 (R49), ndhH (R49) and *E. coli* NuoCD (R250) — so conservation of
this arginine is not evidence that a member is methylated. NDUFAF7 orthologues are
eukaryotic [PMID:24089531, "it is a protein methylase that symmetrically dimethylates
the ω-N(G),N(G') atoms of residue Arg-85 in the NDUFS2 subunit of complex I"; "This
methylation step occurs early in the assembly of complex I and probably stabilizes a
400-kDa subcomplex that forms the initial nucleus of the peripheral arm and its juncture
with the membrane arm"].

### On the "no IBA" premise

NDUFS2 is **not** an IBA-free gene. Its GOA record carries four `ECO:0000318` rows
(`GO:0005743`, `GO:0045271`, `GO:0008137`, `GO:0006120`), matching exactly the four IBD
assertions at PAINT node `PTN000241916`, and O75306 is itself a seed on all four — which
is the expected pattern when a gene has its own experimental annotations for the term,
not circularity. The genuine gap in this family is different and narrower: **no PAINT
node in PTHR11993 asserts any quinone-binding term**, although the quinone chamber is
the one contribution every member of the family makes and the His/Tyr pair that lines it
is invariant from *E. coli* to chloroplasts. `GO:0048038` at the family root is the
missing IBD.

### Open questions carried forward

The `suggested_questions` block already covers the rat-versus-human scope of the
oxygen-sensing work, the mechanism of Arg-85 dimethylation, the catalytic-versus-assembly
mutation split, and the complex III destabilisation reported in NDUFS2 patients. Nothing
added this pass.
