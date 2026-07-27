# ADCK2 (Q7Z695) — review notes

Human ADCK2, 626 aa, chromosome 7, HGNC:19039. PAINT + affinage campaign.

## 0. GOA / stub reconciliation (done first, per procedure)

```
ADCK2-goa.tsv rows (minus header):            8
distinct rows (minus header):                 8
'- term:' entries in the seeded review YAML:  8
```

Perfect reconciliation — no collapsed rows to restore. QuickGO independently returns
`numberOfHits = 8` for `geneProductId=UniProtKB:Q7Z695` with `len(results) = 8` (not a
paginated page total), so the local TSV is the complete annotation set.

## 1. What ADCK2 is annotated with, and what it conspicuously is not

The eight GOA rows are six `GO:0005739 mitochondrion` / `GO:0016020 membrane` location
rows, one `GO:0005515 protein binding` IPI, and one `GO:0010795 regulation of ubiquinone
biosynthetic process` IDA. **There is no protein-kinase annotation of any kind** — no
`GO:0004672`, no `GO:0004674`, no `GO:0006468`, not even `GO:0005524 ATP binding`.

That matters because UniProt's own entry is loud about kinase activity:

- `DE   RecName: Full=Uncharacterized aarF domain-containing protein kinase 2;`
- `DE            EC=2.7.11.-;` (EC 2.7.11.- is *protein-serine/threonine kinase*)
- `KW   Serine/threonine-protein kinase; Transferase; Transmembrane;`
- `DR   GO; GO:0004674; F:protein serine/threonine kinase activity; IEA:UniProtKB-KW.`
- `DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.`

and simultaneously disclaims it in prose:

- `CC   -!- FUNCTION: The function of this protein is not yet clear. It is not`
  (continues: "known if it has protein kinase activity and what type of substrate it
  would phosphorylate (Ser, Thr or Tyr) (Probable)")

So the entry asserts *serine/threonine* specificity in three machine-readable fields
while its curated prose says the substrate class is unknown. Those two `DR GO` lines are
the keyword-derived annotations; they are **absent from current GOA**, which is why the
review has no kinase row to act on. The defect sits one layer upstream of GOA, in the
EC number and the keyword set. It goes in `suggested_questions` as a UniProt correction
to report, not in an annotation verdict.

## 2. What COQ8A/COQ8B were actually shown to do (primary sources, not family prose)

The brief's lead was that the characterised members turned out not to be canonical
protein kinases. Checked against the primary papers, that is right, with one important
2024 complication.

Stefely 2015, crystal structure of ADCK3/COQ8A
[PMID:25498144 "we show that UbiB proteins adopt an atypical PKL fold with multiple
UbiB-specific features positioned to inhibit protein kinase activity"]. The suppressor
is chemical as well as steric: [PMID:25498144 "Collectively, these results demonstrate
that ADCK3 A339 inhibits protein kinase activity in vitro."], where A339 is an alanine of
the UbiB "A-rich loop" that replaces the canonical Gly-rich loop —
[PMID:25498144 "The A339G and A337G,A339G double mutations both enabled
autophosphorylation"].

Stefely 2016 made the negative explicit and extended it to yeast
[PMID:27499294 "Collectively, these results demonstrate that the enzymatic activities of
mammalian COQ8A and yeast Coq8p are highly similar, and that neither catalyzes canonical
protein kinase activity."], with the steric mechanism
[PMID:27499294 "Even with a nucleotide bound, the KxGQ motif is positioned to occlude the
typical peptide substrate binding site and preclude in trans protein phosphorylation."].
Crucially for ADCK2, the same paper generalises the prediction to the whole family
[PMID:27499294 "we predict uPKL functionality to be conserved throughout this ancient
protein family"].

Two guards against over-reading that negative:

1. The autophosphorylation that the A-rich loop suppresses is a *cis* activity and is not
   the gene's function anyway [PMID:27499294 "showing that the autophosphorylation
   observed in vitro is dispensable for function in vivo"].
2. **The negative has since been partly contested.** A 2024 in vitro reconstitution of the
   COQ metabolon reports [PMID:38425362 "COQ3, but not COQ6, is phosphorylated by COQ8B at
   multiple sites"], and GOA now carries `GO:0004672 enables` IDA on COQ8B from that
   paper. So COQ8B holds **both** a `NOT|enables` (PMID:27499294) and an `enables`
   (PMID:38425362) for `GO:0004672`, and COQ8A holds a `NOT|enables` IDA
   (PMID:27499294) alongside an `enables` ISS propagated from COQ8B (GO_REF:0000024).
   Both contradictions are in the live QuickGO record. This is a real curation problem in
   the family, worth flagging, and it is a reason to be careful rather than sweeping about
   "the family is not a protein kinase".

## 3. Does ADCK2 keep the residues? (own analysis — `ADCK2-bioinformatics/`)

`ubib_motif_analysis.py` builds a Clustal Omega MSA of ADCK2, COQ8A, COQ8B, Cqd1/YPL109C,
Cqd2/YLR253W, ADCK1, ADCK5, *E. coli* UbiB and PKA (P17612, negative control), then projects
COQ8A's own UniProt-annotated motif and ligand positions through the alignment. Residue
identity and "lands on a site the target itself annotates" are kept as separate conditions,
per the campaign rule that identity alone manufactures matches at low identity.

Register is judged by the negative control: 6 of 9 columns place PKA inside one of PKA's
own annotated sites, and PKA reproduces **4/4** canonical catalytic residues and **0/2** KxGQ
positions, so the KxGQ columns are UbiB-diagnostic and not an artefact of aligning any
kinase. The one column the strict test cannot confirm is `DFG_D` — but the two conditions
come apart there for an uninteresting reason: PKA lands on **D185**, its own DFG aspartate,
identical to COQ8A's D507, and P17612 simply carries no feature annotation at that position.
Absence of an annotation in the control is not evidence the column is out of register.
ADCK2's reading there (D493) is separately corroborated by local context — COQ8A `all[D]FG`
versus ADCK2 `vll[D]AG` — and by a motif scan of the raw sequence.

Worth recording as a methodological point: **adding Cqd2 to the alignment improved the
register**, moving PKA's DFG column from a spurious Ser to its true D185 and taking the
control from 3/4 to 4/4. A sparse alignment was mis-seating one column, and the fix came
from more taxa rather than from more parameters.

Results:

| feature | COQ8A | ADCK2 | reading |
|---|---|---|---|
| KxGQ motif | K276…Q279 | **K147…Q150** (`KLGQ`) | retained |
| A-rich loop | `AAAS` 337–340 | **`GSGC` 207–210** | *not* Ala-rich |
| beta3 Lys | K358 | K311 | retained |
| catalytic Asp | D488 | D445 | retained |
| catalytic-loop Asn | N493 | N450 | retained |
| DFG-equivalent Asp | D507 | D493 (`DAG`) | retained |

Two conclusions, pulling in opposite directions, and both must be stated:

- **ADCK2 is a UbiB uPKL, not a conventional kinase in disguise.** It keeps the KxGQ motif,
  the exact feature Stefely showed occludes the peptide groove and on which the family-wide
  uPKL prediction rests. It also keeps the TM-helix → KxGQ → kinase-domain arrangement of
  COQ8A (ADCK2 TM 103–123 / KxGQ 147; COQ8A TM 214–230 / KxGQ 276).
- **ADCK2 is not a pseudokinase either.** All four canonical catalytic positions are intact,
  and all three A-rich-loop positions fall inside ADCK2's *own* annotated ATP-binding site.
  So the "fold retained, catalytic residues lost" argument that would justify REMOVE on a
  catalytic term is **not available here**. Had a `GO:0004672` row existed, the honest
  verdict would have been MARK_AS_OVER_ANNOTATED on the KxGQ/occlusion argument, not REMOVE.

The A-rich loop is the interesting divergence: ADCK2 (and Cqd1) carry Gly where COQ8A
carries the suppressor Ala. Since A339G is precisely the COQ8A mutation that de-represses
autophosphorylation, the naive reading is "ADCK2 is the branch that kept phosphotransfer".
I am not making that claim: the de-repressed activity is *cis* autophosphorylation, shown
dispensable in vivo, and the KxGQ occlusion is untouched. Recorded as a hypothesis for
`suggested_experiments`, not a finding.

**The A339-equivalent column turns out to be branch-diagnostic**, which is a stronger result
than the divergence alone. Across the 8 UbiB proteins in the alignment, Gly appears in
exactly **2** — ADCK2 and Cqd1 — while all six others, *including Cqd2 and ADCK1*, carry the
suppressor Ala. So a single residue reproduces the Cqd1↔ADCK2 / Cqd2↔ADCK1 pairing.

Two scope limits, both of which I initially got wrong and a reviewer caught:

1. This is **independent of the genetics in PMID:34362905 but not of PANTHER**, whose
   subfamily assignment is itself sequence-derived. It is a second sequence-based line
   agreeing with the genetics, *not* a third independent line.
2. **Only `Arich_A3` is branch-diagnostic.** At the adjacent `Arich_A1` position Gly is
   carried by four proteins — ADCK2, Cqd1, **Cqd2 and ADCK1** — so that column cuts across
   the pairing rather than along it. The claim is about the A339-equivalent position
   specifically, not about the A-rich loop as a whole.

It corroborates the orthology; it does not on its own show the two branches differ
functionally, and it is not used to assert anything about ADCK2's activity.

**Identity figures in the report are MSA-derived and not portable.** Adding Cqd2 shifted every
one of them (the negative control moved 17.1% → 11.9%), because Clustal Omega's gap placement
depends on the whole input set. Never compare an identity number from this report against one
computed from a different membership — recompute.

## 4. Orthology, and why the ADCK genes must not be pooled

The three human sub-branches sit in **three different PANTHER families** —
ADCK2 `PTHR45890`, ADCK1 `PTHR43173`, COQ8A/COQ8B `PTHR43851` — and their yeast
counterparts line up exactly with the published assignment:

| human | PANTHER family | IBA node | yeast counterpart |
|---|---|---|---|
| ADCK2 | PTHR45890 | PTN000059786 | YPL109C = **Cqd1** (Q02981, `PTHR45890:SF1`) |
| ADCK1 | PTHR43173 | PTN005148758 | YLR253W = **Cqd2** / Mcp2 (Q06567) |
| COQ8A/COQ8B | PTHR43851 | PTN000059692 | Coq8 |

Kemmerer 2021 makes the same pairing from the biology
[PMID:34362905 "it will be important to determine if functional conservation exists between
Cqd1 and Cqd2 and their putative human orthologs, ADCK2 and ADCK1/5, respectively"], and it
was already implicit in ADCK2's own primary paper, which used YPL109C as the complementation
host. So **ADCK2's yeast orthologue is Cqd1, and ADCK1's is Cqd2 — two proteins with
reciprocal effects on CoQ distribution** [PMID:34362905 "we identify two highly conserved
but poorly characterized mitochondrial proteins, Ypl109c (Cqd1) and Ylr253w (Cqd2), that
reciprocally affect this process"], [PMID:34362905 "Loss of Cqd1 skews cellular CoQ
distribution away from mitochondria"]. Anything asserted about ADCK1 does not transfer to
ADCK2, and vice versa; the branches are, if anything, antagonistic.

Cqd1's own activity is inferred, not measured
[PMID:34362905 "Unlike COQ8, Cqd1 is recalcitrant to recombinant protein purification"],
but the inference is genetic and specific: rescue [PMID:34362905 "depended on core protein
kinase-like (PKL) family residues"]. Cqd1 has since been localised to the inner membrane at
a contact site [PMID:37073556 "we identified a novel mitochondrial contact site in
Saccharomyces cerevisiae that is formed by the inner membrane protein Cqd1 and the outer
membrane proteins Por1 and Om14"], with the authors expecting conservation
[PMID:37073556 "Cqd1 is highly conserved, suggesting that this complex is conserved in form
and function from yeast to human"] and a second lipid role
[PMID:37073556 "Our data suggest that Cqd1 is additionally involved in phospholipid
homeostasis."].

## 5. The human ADCK2 evidence (PMID:31480808), read for what it discriminates

Before this paper the record was empty [PMID:31480808 "no information is available about
the role of ADCK2 in CoQ biosynthesis"].

*Localisation.* [PMID:31480808 "Immunoblotting in various subcellular fractions of HEK293
cells showed a distribution of ADCK2 similar to the mitochondrial TOM20 and Mfn2"] and
[PMID:31480808 "The presence of ADCK2 was not detected in the endoplasmic reticulum and
cytosolic fraction."]. Protease protection places it inside:
[PMID:31480808 "consistent with its presence in the mitochondrial matrix or bound to the
inner mitochondrial membrane"]. Note this is endogenous protein, and it explicitly declines
to discriminate matrix from IMM — so it supports `GO:0005739` and is compatible with
`GO:0016020`, but does **not** license `GO:0005743`.

*CoQ.* Patient (R333*, matching UniProt `VARIANT 333..626 Missing`) fibroblasts
[PMID:31480808 "The mutation produced a termination codon that led to a significant decrease
in ADCK2 mRNA and protein levels in dermal fibroblasts"] with reduced CoQ10 rescued by WT
allele; mouse [PMID:31480808 "Collectively, these results supported the role of
ADCK2-encoded protein in the biosynthesis of mitochondrial CoQ in"] both species; and — the
decisive cross-species control — heterologous complementation
[PMID:31480808 "The deletion of YPL109c, the S. cerevisiae homolog of human ADCK2, caused a
40% decrease in the production of CoQ6"],
[PMID:31480808 "Transformation of the ΔYPL109c yeast strain with wild type YPL109c or human
ADCK2 construct rescued CoQ6 biosynthesis"].

*The experiment that fixes the GO term.* 3H-mevalonate labelling found total cellular CoQ
and cholesterol synthesis **unchanged**, with only the mitochondrial fraction depleted
[PMID:31480808 "which indicated a defect in intracellular trafficking of isoprenoid and
cholesterol from the cytoplasm"]. So ADCK2 is *not* a step in the biosynthetic pathway; it
governs how much precursor reaches the organelle. This is exactly why
`GO:0010795 regulation of ubiquinone biosynthetic process` is the right term and
`GO:0006744 ubiquinone biosynthetic process` (which COQ8A/COQ8B correctly hold) would be
wrong for ADCK2. The curator's choice is confirmed, not upgraded.

*Fatty acids.* [PMID:31480808 "palmitate-dependent OCR decreased in permeabilized MEFs
lacking Adck2 compared to WT cells"], with lipid-storage myopathy and hepatic steatosis in
patient and mouse. The paper and the later mouse work
[PMID:35936917], [PMID:39354863] treat the beta-oxidation defect as downstream of the CoQ
deficit — CoQ10 supplementation partially rescues. **Function versus phenotype:** a
beta-oxidation phenotype in a haploinsufficient mouse does not establish a molecular
function, and I have not proposed a fatty-acid GO term on the strength of it. The brief's
framing that ADCK2 is linked "to fatty-acid metabolism rather than to coenzyme Q" does not
survive the paper: the CoQ deficit is upstream and is the rescuable node.

## 6. The `GO:0005515` row, checked the ACRV1/ADAMTSL5 way

Partner is `UniProtKB:P05141` = SLC25A5 / ANT2, ADP/ATP translocase 2. UniProt records
`CC       Q7Z695; P05141: SLC25A5; NbExp=4; IntAct=EBI-21505425, EBI-355133;`.

Expanding the IntAct records rather than trusting `NbExp` (third instance of this pattern in
the campaign, after ACRV1 and ADAMTSL5):

- All **4** evidences are from **one publication**, PMID:27499296 (Floyd 2016), by **one**
  method (`anti tag coip`), ADCK2 bait / SLC25A5 prey, MI-score **0.35**, and **3 of the 4
  are spoke-expanded** — i.e. inferred from a co-complex pulldown, not demonstrated binary.
  `NbExp=4` is one AP-MS experiment counted four times.
- Partner promiscuity: SLC25A5 carries **385** IntAct interaction evidences; ADCK2 has 83
  distinct partners over 7 publications. ANT2 is among the most abundant IMM proteins and a
  routine AP-MS background for any mitochondrial bait.
- Topology check comes back **negative** (i.e. no objection): unlike ACRV1's cytosol-facing
  partners for a secretory-lumen protein, ANT2 and ADCK2 are both IMM/matrix-facing, so the
  interaction is at least physically possible. Recording the null so the next reviewer knows
  it was run.
- The cached full text of PMID:27499296 does not mention ADCK2 at all — the interaction lives
  in the supplementary AP-MS dataset, so the paper's own narrative offers no interpretation.

Verdict: `MARK_AS_OVER_ANNOTATED`, not REMOVE. The pulldown happened; `protein binding` is
simply uninformative (CLAUDE.md) and rests on one unreplicated, spoke-expanded, low-score
run against a hub protein. There is no informative MF to MODIFY it to.

## 7. Checks run that came back NEGATIVE (recorded so they are not re-run blind)

- **PAINT node defect: not found.** `PTN000059786` propagates **49 annotations over 49
  distinct gene products** (annotation count and entity count verified equal, and the result
  is unpaginated) to exactly **one** term, `GO:0005739`. 17 of the 49 carry a symbol matching
  `/adck2/i`; the rest are systematic ORF identifiers in fungi, protists and nematodes, and
  one is literally named `cqd1`. Yeast YPL109C/Cqd1 **is** under the node and yeast
  Mcp2/Cqd2 — the ADCK1 donor — **is not**, so the node's reach is the ADCK2/Cqd1 orthologue
  group and nothing else. No kinase term, no CoQ term, no over-reach. The reciprocal question
  ("which node's reach is exactly my gene set, and what did it give them?") returns the same
  node and the same single, true term. Both halves clean.
- **Fold-name-propagated-into-activity in GOA: hypothesis NOT confirmed.** No `GO:0004672`,
  `GO:0004674`, `GO:0006468` or `GO:0005524` row exists on ADCK2. Like ADAMTSL5, the
  predicted error simply is not in the annotation set. It is present in UniProt's EC/keyword
  layer, which is a different artefact with a different owner.
- **IBA-less-precise-than-donor (ACRV1 pattern): not warranted.** Donors resolve to mouse
  Adck2 Q6NSR3 (Swiss-Prot; own HDA PMID:18614015 + IDA PMID:31480808 for `GO:0005739`) and
  yeast Q02981/Cqd1 (Swiss-Prot; 3x HDA for `GO:0005739`, plus IDA for `GO:0005743`
  *mitochondrial inner membrane* and `GO:0044289` from PMID:37073556). The donor set is
  **heterogeneous in specificity** — one at mitochondrion, one at inner membrane — so
  `GO:0005739` is the correct LCA and a downward MODIFY would mean arbitrarily preferring the
  yeast donor. Per the AADACL4 rule, `GRANULARITY_MISMATCH` needs the donors to agree; they
  do not.
- **Retraction / erratum / expression-of-concern scan: all clear.** 16 PMIDs checked via
  `CommentsCorrections/RefType` on each cited record plus publication types: 31480808,
  33988507, 34800366, 27499296, 25498144, 27499294, 34362905, 37073556, 35936917, 39354863,
  35205819, 36439873, 22355351, 38425362, 36302899, 18614015. None flagged.
- **Complex-projection test (ACTR8 pattern): negative.** `PMID:31480808` annotates only **2**
  entities (human ADCK2 and mouse Adck2), 2 terms each — a genuinely gene-specific paper, not
  a projection. `PMID:33988507` annotates 4 entities. `PMID:34800366` (1235 annotations) and
  `PMID:27499296` (117) are paginated, so entity counts there are unavailable and the test is
  unreliable for them; both are coded HTP/IPI, which is the appropriate code for a survey.
- **Self-referential IBA.** `UniProtKB:Q7Z695` appears in its own WITH/FROM. Per the campaign
  brief this is valid and records a PAINT curator judging the term core — `NO_FAILURE_CORE`,
  never `CIRCULAR_PROPAGATION`.

## 8. Provider record (affinage)

`gates_passed: True`, faith 100%, 5 numeric PMIDs, no `PMID:bio_*` preprint ids. Its narrative
is broadly right but conflates two things this review keeps apart: it calls CoQ biosynthesis
"the core function from which the metabolic and developmental phenotypes derive", where the
labelling experiment shows the defect is in precursor *delivery*, not synthesis. Its cancer
findings (PMID:35205819 melanoma/MYL6, PMID:36439873 NSCLC, PMID:22355351 HIF-1alpha screen)
are all knockdown/overexpression phenotypes in transformed lines with no molecular mechanism
tying them to ADCK2's biochemistry; none supports a GO term and none is used here beyond
context. No affinage sentence is quoted as evidence anywhere in the review.

## 9. Ontology gap found

GO has **no term for coenzyme Q transport or distribution**. Yet the characterised activity of
ADCK2's own yeast orthologue is control of *cellular CoQ distribution*, and the human evidence
points at precursor trafficking. The nearest available parents are
`GO:0032365 intracellular lipid transport` and `GO:0120009 intermembrane lipid transfer`.
Filed as `proposed_new_terms`, explicitly scoped so that ADCK2 is a candidate rather than an
asserted holder — the direct holders today would be yeast Cqd1/Cqd2.

**My first attempt to establish this absence was invalid, and a reviewer caught it.** I had
enumerated the descendants of `GO:0006743 ubiquinone metabolic process` (9 terms: biosynthesis,
catabolism, seven enzyme activities) and concluded no transport term exists. But a transport
term would *never* be classified under a metabolic process, so that query could not have found
one had it existed — it was guaranteed to return nothing. An absence is only evidence when the
query could have returned a hit.

Redone in `ADCK2-bioinformatics/coq_transport_term_check.py` with two complementary sweeps that
each could have:

- **Label sweep:** all **102** GO terms whose label mentions ubiquinone / coenzyme Q /
  quinone / **quinol**. Every transport-flavoured term among them is set aside on one of
  **two** grounds, not one. Most are *electron transport* terms, where the electron is the
  cargo and the quinone merely the acceptor. One — `GO:1903222 quinolinic acid transmembrane
  transport` — is a genuine BP transport process and is excluded on entirely different
  grounds: it matched only through a substring accident (see trap 3 below).
- **Branch sweep:** the **2584 distinct** descendants of `GO:0006869`, `GO:0010876`,
  `GO:0032365`, `GO:0120009` and `GO:0006810`. Zero ubiquinone-specific children.

Each candidate is printed with the reason it was excluded, so the filtering is auditable rather
than buried in the verdict. Sweep 1 would catch a term classified in the wrong branch; sweep 2
a term whose label avoids the word. The absence is evidence only to the extent those two
together are exhaustive, and the script says so.

**Three substring traps in one small script**, all the same error wearing different clothes:

1. `"transport" in name` matched **"electron transport"**, giving 8 spurious hits on the first
   run. Ubiquinone there is the electron *acceptor*, not the cargo.
2. **`"quinone"` does not match `"ubiquinol"`.** The reviewer caught this: my original keyword
   set left *both* sweeps blind to any term named after the reduced form — the exact shared
   blind spot the two-sweep design exists to rule out — and ubiquinol-named GO terms do exist
   (6 in this repo's own cache). Adding `quinol` pulled in four real terms that had been
   invisible (`GO:0006122`, `GO:0008121`, `GO:0009486`, `GO:0009496`), all correctly
   adjudicated out.
3. Adding `quinol` then produced the mirror error: **`"quinol"` *is* a substring of
   `"quinolinic"`**, so `GO:1903222 quinolinic acid transmembrane transport` passed every
   other filter as a genuine BP transport term. Quinolinic acid is a tryptophan-pathway NAD
   precursor unrelated to CoQ. Excluded by deleting the `quinolin` substring and re-testing
   the keywords: whatever still matches did not come from the false friend. The first
   version of that rule instead asked "contains `quinolin` and names no real CoQ species",
   which is *not* equivalent — `pyrroloquinoline quinone biosynthetic process` contains
   `quinolin` and also matches on its own `quinone`, so the weaker rule would have excluded
   it while reporting the wrong reason. Delete-and-retest keeps it.

The brief's rule — *any substring test on a controlled vocabulary needs an anchor* — cost
three rounds here, in both directions: too-loose matching invented hits, too-narrow matching
hid a whole chemical species.

## 10. Cross-gene note for the concurrent ADCK1 review

Derived here independently; relay as a claim, not a fact. ADCK1 and ADCK2 are in different
PANTHER families with different IBA nodes and different yeast donors (Cqd2/Mcp2 vs Cqd1),
and Kemmerer 2021 pairs them with proteins of *reciprocal* effect on CoQ distribution. ADCK1
also carries no MF annotation in GOA — so if the ADCK1 review reports a kinase-activity
propagation defect, that would be a disagreement worth resolving, because QuickGO returns
only four BP rows for Q86TW2 (`GO:0007005` IBA, `GO:0055088` IBA, `GO:0010637` IMP,
`GO:1903852` IMP) and no MF rows at all.

**Compared against PR #2310 after the fact.** The two reviews were derived independently and
agree on every cross-cutting point: the fold-propagation hypothesis is not confirmed in GOA
but is present in UniProt's EC/keyword layer; `GO_REF:0000043` keyword annotations have been
withdrawn; the catalytic residues are intact in both genes so neither is a pseudokinase; the
Cqd1↔ADCK2 / Cqd2↔ADCK1 pairing holds; and `just validate` silently collapses main's two
pre-existing duplicate curies in `cache/go/terms.csv` on every run.

The one substantive difference is a genuine biological one, not a disagreement: at the
A339-equivalent column, **ADCK1 carries A164 and ADCK2 carries G209** — both reviews report
their own gene's residue correctly, and my alignment (which includes both proteins plus both
yeast orthologues) shows the split is exactly ADCK2+Cqd1 versus everyone else. PR #2310 uses
ADCK1's retained alanine to question ProRule's ATP-ligand assignment, on the grounds that
COQ8A with Ala is ADP-selective. The reciprocal prediction for ADCK2 — Gly, hence plausibly
more ATP-selective — follows from the same logic but is untested, so no nucleotide term is
proposed here either. Both reviews withhold a nucleotide-binding term for the same reason:
the site is untested, not refuted.

Two claims in #2310 that I could not check from my own data and am deliberately not relaying
as fact: that mouse ADCK1 was localised to the inner membrane in primary brain endothelial
cells (PMID:40884816), and that the Yoon kinase-independence result is a gain-of-function
readout. Both are ADCK1-specific and neither bears on ADCK2.
