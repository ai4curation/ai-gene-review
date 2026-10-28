# inaZ (P06620, ICEN_PSESY) — review notes

Ice nucleation protein InaZ of *Pseudomonas syringae* pv. *syringae*.
Swiss-Prot reviewed, PE:1, 1200 aa.

## Why this gene is in scope

This review was created as part of grounding CMMMech's microbial
critical-mineral mechanisms to UniProtKB proteins. P06620 appears in
`data/records/anatase.yaml` as the source of the N-terminal outer-membrane
"INP" anchor in an engineered INP–silaffin fusion displayed on *E. coli*
BL21(DE3), used to template a titanium precursor that is afterwards calcined
to anatase. See the CMMMech section at the end for what that record does and
does not establish about InaZ itself.

## What the protein is

- 1200 residues, with a single CHAIN feature and a REGION 176–1151 annotated
  "Octapeptide periodicity"
  [file:PSESY/inaZ/inaZ-uniprot.txt "Octapeptide periodicity"].
- UniProt's DOMAIN note records "Contains 122 imperfect repeats of a consensus
  octapeptide A-G-Y-G-S-T-L-T; further on a 16-residue and a regional
  48-residue periodicity is superimposed"
  [file:PSESY/inaZ/inaZ-uniprot.txt].
- InterPro IPR000258 (Pfam PF00818, PROSITE PS00314, PRINTS PR00327) is a
  **repeat** entry, "Ice nucleation protein, octamer repeat". It describes the
  central repeat array, not the N-terminal membrane anchor. This matters for
  the CMMMech record (below).
- The three-part architecture — N-terminal membrane-binding domain, central
  ice-active repeats, C-terminal domain — is stated directly in the
  Nat Commun study: "It contains an N-terminal tag, the membrane-binding
  N-terminal domain, the ice-active repeat units, and a C-terminal domain of
  unknown function" [PMID:33608518].

## Function: ice nucleation

- UniProt FUNCTION: "Ice nucleation proteins enable bacteria to nucleate
  crystallization in supercooled water" [file:PSESY/inaZ/inaZ-uniprot.txt].
- Direct activity evidence for the *inaZ* product specifically: INP was
  partially purified from the membrane fraction of *E. coli* carrying *inaZ*;
  "The activity of the purified protein was lost after treatment with
  phospholipase C, and its activity was subsequently restored by addition of
  the naturally occurring lipid phosphatidylethanolamine" [PMID:9698431].
  That is a measured activity of the purified protein, and it also shows the
  activity depends on a lipid environment.
- Mechanism: the ice-active repeats fold as a β-helix and order interfacial
  water. "The IR data provides experimental evidence that the central repeat
  region of InaZ has a β-helical fold" and "In this configuration, interaction
  between INPs and water molecules imposes structural ordering on the adjacent
  water network" [PMID:33608518]. The earlier modelling paper reached the same
  general picture: "This model predicts a largely planar extended molecule,
  with one side serving as a template for orienting water into an ice lattice
  and the other side interacting with the membrane" [PMID:8355267].
- Potency: *P. syringae* is the most active natural ice nucleator known;
  "in the presence of the ice-active bacterium Pseudomonas syringae, water
  freezes at temperatures as high as −2 °C" [PMID:33608518].
- The activity is **not** a catalytic turnover in the enzymatic sense: it is a
  templating/ordering surface. GO:0019833 nonetheless uses the word "Catalysis"
  in its definition (see the ontology note below).

## Location: cell outer membrane

The single existing GOA row (GO:0009279, IEA, GO_REF:0000120) is the correct
location and is backed by direct experiment, not only by the InterPro→SubCell
mapping:

- "Nearly all ice nucleation activity was associated with the outer membrane
  because the partitioning of 3-ketodeoxyoctonate (a lipopolysaccharide
  component) and ice nuclei in cell fractions were similar to and opposite
  that of NADH oxidase (a cytoplasmic membrane component)" [PMID:2520825].
- "Nearly all of the iceC gene product, which occurred in low abundance, was
  associated with the outer membrane of both P. syringae and E. coli"
  [PMID:2520825]. UniProt cites this paper as the ECO:0000269 evidence for its
  SUBCELLULAR LOCATION line, i.e. UniProt curators treat *iceC* here as this
  gene product; this review defers to that.
- Independently: "The ice nucleation protein was totally localized in the
  bacterial envelope" [PMID:9698431].
- Corroborated by the display literature: InaZ is "an outer membrane protein
  found in some Gram-negative bacteria" and displayed fusions are
  protease-accessible from outside [PMID:9624691].

Note on PMID:9624691: its abstract calls Inp "a glycosyl
phosphatidylinositol-anchored outer membrane protein". GPI anchoring is a
eukaryotic pathway; the GPI-like anchor claim for INPs comes from older work
and is not settled. Nothing in this review rests on it, and no anchor-type
annotation is proposed.

A `cell surface` (GO:0009986) or `outer membrane, external side` annotation is
*not* proposed here. The outward orientation is well supported for engineered
INP-anchor fusions in *E. coli* [PMID:9624691], which is a heterologous
construct, and the ice-active face must contact bulk water, which is an
inference rather than a measurement on native InaZ. GO:0009279 is as precise as
the direct evidence for this protein warrants. This is recorded as a suggested
experiment instead.

## Biotechnological context

"Currently, these ice-nucleating (IN) bacteria are being used in snow making
and have potential applications in the production and texturing of frozen
foods, and as a replacement of silver iodide in cloud seeding" [PMID:1760850].
UniProt's BIOTECHNOLOGY line records the Snomax product. The second major
application, and the one CMMMech uses, is as a surface-display anchor: the
N-terminal INP domain carries passenger proteins to the outer surface of
*E. coli* [PMID:9624691].

Neither use is annotatable. Snow-making and surface display are things humans
do with the protein, not processes the gene product participates in in its own
organism, so no GO process term follows from them.

## Ontology notes

- **GO:0019833 ice nucleation activity** exists and is a molecular function,
  child of GO:0050825 ice binding (verified via OLS, 2026-10-28). Its
  definition even names this organism: "This process is commonly found in
  certain bacteria, such as Pseudomonas syringae, and plays roles in
  environmental adaptation and plant pathogenesis."
- A QuickGO query for `goId=GO:0019833` returned `numberOfHits: 0` on
  2026-10-28 — the term currently has **no annotations at all**, in any
  species. The term was reinstated from obsolete (its own definition carries
  the note "Note that this term was reinstated from obsolete"), which explains
  the absence: this is a curation backlog, not a curator convention against
  annotating ice nucleators. It is therefore proposed here as a NEW row rather
  than treated as a deliberate omission.
- Two problems with the GO:0019833 definition are worth raising upstream, and
  are recorded in `suggested_questions`:
  1. It says "Catalysis of the formation of ice crystals". INPs do not
     catalyse in the enzymatic sense; they present an ordered surface that
     templates ice. The term's placement under `ice binding` (and so under
     `small molecule binding`) is consistent with templating, not catalysis,
     so the definition text and the placement disagree.
  2. The teleological clause "to protect the organism from damage by
     intracellular ice formation" fits freeze-tolerant insects and some fungi,
     but for *P. syringae* the literature frames high-temperature nucleation as
     causing frost injury to the plant and releasing nutrients — "they promote
     ice growth at high sub-zero temperatures" to access plant nutrients
     [PMID:33608518], and "A negative aspect of these IN bacteria is frost
     damage to plant surfaces" [PMID:1760850]. A GO definition should not bake
     in one lineage's adaptive story.
- No GO biological process term is proposed. The candidate neighbourhood
  (GO:0050826 response to freezing, GO:0071497 cellular response to freezing)
  is about *responding to* a freezing stimulus; InaZ causes freezing rather
  than responding to it. Pathogenesis/nutrient-release roles are downstream
  ecological consequences, not steps InaZ performs, so they fail the
  participation test in CLAUDE.md.

## PANTHER

The UniProt record carries `PANTHER; PTHR31294:SF8; KERATIN-ASSOCIATED PROTEIN
21-1-RELATED`. A keratin-associated-protein subfamily call for a bacterial ice
nucleation protein is almost certainly an artefact of the low-complexity,
glycine/serine-rich octapeptide repeats rather than homology. No module or
family descriptor in this repository is being created from it, and no PANTHER
id is asserted anywhere in the review, so nothing here depends on it. Flagged
for anyone who later builds a family descriptor for INPs: do not take
PTHR31294:SF8 at face value. This is not recorded as a `source_defect` because
source defects in this repository are for GOA/UniProt/InterPro annotation rows,
and no GO annotation derives from this subfamily assignment.

## CMMMech record check (`data/records/anatase.yaml`)

CMMMech's `functional_role` for P06620 reads: "Outer-membrane ice nucleation
protein InaZ serving as the N-terminal cell-surface display anchor (INP) in the
engineered INP-silaffin fusion expressed in Escherichia coli
BL21(DE3)/pET28a-INP-silaffin."

Assessment — the claim is accurate and appropriately scoped. It says InaZ
supplies the anchor in an engineered fusion, and does not claim that InaZ
nucleates titanium, mineralizes anything, or acts on a critical mineral. The
record's own evidence block is marked `supports: partial` and explicitly notes
that non-engineered *E. coli* controls were omitted. Two smaller points:

1. **Domain/identifier mismatch.** The protein_example lists
   `InterPro:IPR000258` and `Pfam:PF00818` beside a `functional_role` that is
   about the N-terminal anchor. IPR000258/PF00818 are the *octapeptide repeat*
   signatures of the central ice-active region (InterPro type: Repeat), which
   is precisely the part that INP surface-display constructs normally truncate
   away. The identifiers are correct for the full-length protein and wrong for
   the domain the record is actually describing. The record would be more
   precise if it either dropped the signature ids from that entry or said that
   they match the repeat region rather than the anchor.
2. **Anchor domain boundaries are not given.** The record does not state which
   residues of P06620 constitute the "INP anchor" used in the construct, and
   the Ping et al. supporting information is not reproduced in the record.
   Different INP display systems use INPN, INPNC or other truncations, so
   "N-terminal anchor" alone does not identify the construct.

Neither point is recorded as a `source_defect`: per the project brief, errors
in CMMMech's own fields belong in these notes and the report, not in
`review.source_defects`, which are for GOA/UniProt/InterPro.

## Green & Warren 1985: the founding *inaZ* paper, and why it is not a reference entry

UniProt reference [1] for P06620 is Green R.L., Warren G.J., "Physical and
functional repetition in a bacterial ice nucleation gene", Nature 317:645-648
(1985) [file:PSESY/inaZ/inaZ-uniprot.txt]. It is the source of the cloned
*inaZ* sequence and of the repeat architecture, and so stands behind both the
repeat description in `description` and the heterologous gain of function that
the GO:0019833 row argues from.

It is deliberately **not** added to the review's `references` list. UniProt's
`RN [1]` block carries neither an `RX PubMed=` nor an `RX DOI=` line, and
repeated PubMed E-utilities searches (title phrase; `Nature[jour] AND 1985[pdat]
AND ice nucleation`) return zero hits, so the paper is not in PubMed and cannot
be cached in `publications/`. There is therefore no identifier for it that can
be verified from a repository artifact, and any `supporting_text` quoted from it
would fail the verbatim-substring check. Per the project rule against guessing
identifiers, it is recorded here with its UniProt provenance instead of being
given a fabricated or unverifiable `id`. If a PMID or DOI for it is later
established, it should be fetched and added as a normal reference.

## In-repo anchors for the GO:0019833 claim

- `cache/go/terms.csv` line 4483: `GO:0019833,ice nucleation activity,` with
  fetch timestamp 2026-07-26 — the in-repo record that the id exists and is not
  obsolete. The aspect (molecular function under GO:0050825 ice binding) and the
  definition text quoted in `suggested_questions` rest on the live OLS/QuickGO
  lookups of 2026-10-28 and left no cached artifact; `core_functions.molecular_function`
  is hard-validated against MF branch reachability, so CI is the real check on
  the aspect.
- `projects/TCDB/data/propagation_evidence.tsv` line 195:
  `9.B.133.1.1  GO:0019833  ice nucleation activity  5  1  0  0.0  GAP_CANDIDATE  P06620`
  — an independent in-repo analysis reaching the same conclusion that this is a
  real curation gap for exactly this protein and term.

## Source note on this file

No deep-research provider was available in this environment, so no
`-deep-research-<provider>.md` file was generated. All literature here was
gathered directly (PubMed E-utilities, UniProt flat file, InterPro API, OLS,
QuickGO) and every assertion carries an inline citation.
