# NDUFV1 curation notes

## 2026-09-04 — PAINT no-IBA project finishing pass (AI-assisted)

Reviewed every entry in `NDUFV1-ai-review.yaml`, checked the top-level `description` and
`core_functions`, and wrote the accompanying family review at
`interpro/panther/PTHR11780/PTHR11780-review.yaml`. The file validated clean on arrival
and still does. Status moved `IN_PROGRESS` → `COMPLETE`.

### Changes made

1. **Factual error in `core_functions.description`: "covalently bound FMN" → non-covalently
   bound.** Complex I's FMN is a dissociable cofactor, not covalently attached — this is
   the basis of the standard FMN-release assays and of the flavin-site ROS chemistry.
   UniProt records it as a `COFACTOR` with the note "Binds 1 FMN" and
   `ECO:0000269|PubMed:28844695`, with no covalent-attachment feature. Corrected, and the
   fact that both cofactors are resolved in the human cryo-EM structure added.

2. **Two `GO:0005515` IPI lines promoted `KEEP_AS_NON_CORE` → `MARK_AS_OVER_ANNOTATED`.**
   The draft demoted all seven protein-binding lines uniformly, but they are not of equal
   standing. The NDUFV3 lines (PMID:24344204, PMID:30021884, PMID:33961781) and the
   RAB5IF line (PMID:31536960) reflect genuine FP-subcomplex neighbourhood and respirasome
   assembly biology, so non-core is right for them. The other two are not:
   - **PMID:32296183 (HuRI, NDUFV1–CYSRT1).** A yeast two-hybrid binary screen; CYSRT1 is
     a keratinocyte-associated cytoplasmic protein with no mitochondrial role, and the
     assay places both partners outside their native compartments. The paper itself notes
     "the majority of PPIs in HuRI were found in only one screen".
   - **PMID:32814053 (Haenig et al.).** ~25 unrelated partners for NDUFV1 from a single
     systematic Y2H screen designed around protein aggregation in neurodegeneration, with
     no orthogonal validation. These lines over-state what is known about NDUFV1 binding
     rather than adding non-core biology.

3. **Second `core_functions` entry added for `GO:0009055` (electron transfer activity).**
   The draft asserted electron transfer activity in the prose of the first entry's
   description but left it out of the structured `molecular_function` slot, so the claim
   was unindexed. Added as its own entry, matching the `NEW` annotation already proposed
   in `existing_annotations`.

4. **Empty `findings: []` filled for 13 references** — five `GO_REF` entries, seven
   Reactome reactions, and PMID:32296183 — each stating what that source actually
   contributes to this gene and, where a cached publication exists, with a verbatim
   quote. This also records why several of them are weak (inter-ontology inference
   yielding a membrane-arm process term; LONP1 reactions supporting only localization).

### Bioinformatics done for this pass (reproducible)

Global BLOSUM62 alignment (BioPython `PairwiseAligner`, gap open −11 / extend −1) of
P49821 against P25708 (bovine), P31979 (*E. coli* NuoF), Q9FNN5 (*Arabidopsis*), O94500
(*S. pombe*) and Q54I90 (*Dictyostelium*), all fetched from the UniProt REST API; every
mapped position re-confirmed by direct indexing.

**The four N3 cysteine ligands are invariant across the family:**

| protein | N3 ligands |
|---|---|
| P49821 human NDUFV1 | C379, C382, C385, C425 |
| P25708 bovine NDUFV1 | C379, C382, C385, C425 |
| P31979 *E. coli* NuoF | C351, C354, C357, C398 |
| Q9FNN5 *A. thaliana* | C402, C405, C408, C448 |
| O94500 *S. pombe* | C377, C380, C383, C424 |
| Q54I90 *D. discoideum* | C396, C399, C402, C442 |

Unlike the by-similarity cysteines on the partner 49 kDa subunit family (see
`genes/human/NDUFS2/NDUFS2-notes.md`), all four of these are structurally observed —
UniProt cites PubMed:28844695 plus PDB 5XTB/5XTD/5XTH/5XTI for each. Recorded as the
`fe4s_n3_ligands` site in the family review. Left at `strength: CONTRIBUTES` rather than
`REQUIRED` despite the mechanism warranting `REQUIRED`, because no family member has been
found that lost a ligand and the residue validator rightly refuses a `REQUIRED` claim with
no negative control.

**The NADH-binding glycine loop (UniProt `BINDING 87..96`) is `GRGGAGFPTG`** in human,
bovine, *Arabidopsis* and *Dictyostelium*, but `GRGRYG` at 80–85 in *S. pombe* O94500.
Deliberately **not** declared as a family motif site for that reason — a `G.GG.G` pattern
would over-claim. Described in prose in the family review instead.

### On the "no IBA" premise — this gene gives the sharp answer

NDUFV1 does receive IBAs, but only two, and both are non-molecular-function:
`GO:0045271` and `GO:0006120`, matching the two IBD rows at the eukaryotic node
`PTN000207233`. **It receives no molecular-function IBA of any kind**, because that node
carries no F-aspect IBD. The family's only F-aspect IBD — `GO:0003954`, NADH dehydrogenase
activity, dated 20260528 — sits on the *bacterial* node `PTN000207323`, seeded by *E. coli*
NuoF (P31979), and human NDUFV1 is not a descendant of it.

The consequence is that the defining functions of the 51 kDa flavoprotein — NADH
dehydrogenase activity, FMN binding, NAD binding, electron transfer activity — reach the
human protein only as InterPro2GO and keyword-derived IEAs, with no phylogenetic
assertion behind any of them, even though they are conserved from *E. coli* to human and
are what the family is named for [PMID:8288251, "plays an important role in the formation
of the NADH-binding site and is believed to be the principal site of entry for electrons
donated by NADH into the respiratory chain"].

Recommendation recorded in the family review: raising `GO:0003954` (and, on the strength
of the invariant sites, `GO:0010181`, `GO:0051287` and `GO:0009055`) to a node above the
bacteria/eukaryote split would be sound. **Raising `GO:0008137` would not** — the
actinobacterial members of the same single subfamily (*M. tuberculosis* P9WIV6/P9WIV7,
*M. bovis* P65568, *S. coelicolor* Q9XAQ9) come from organisms whose respiratory chain
uses menaquinone, not ubiquinone. The current PAINT curation already avoids that trap by
choosing the acceptor-neutral `GO:0003954`; that choice should be preserved.

### Why this family is coherent and its Q-module partner is not

PTHR11780 has no plastid branch: the chloroplast NDH complex has **no counterpart of this
subunit at all**, which is exactly why it is reduced by ferredoxin rather than by NADH.
The fetched entries slice bears this out — 0 chloroplastic members in PTHR11780 against
134 of 638 in PTHR11993, all of the latter binned into the same subfamily as human NDUFS2.
The two family reviews were written as a pair for this reason.
