# GPM3 (YOL056W) — curation notes

*S. cerevisiae* GPM3 / systematic name YOL056W. UniProt Q12326 (PMG3_YEAST). One of three
phosphoglycerate-mutase-family paralogs in budding yeast (GPM1, GPM2, GPM3). This is an
**understudied / dark** gene: it is a sequence homolog of the glycolytic mutase GPM1, but has
no demonstrated mutase activity and no assigned in-vivo role. The primary curation deliverable
is an honest knowledge-gaps statement plus carefully-attributed core-functions/description that
never invents function.

## Provenance rule for these notes

Every substantive claim carries inline `[PMID:xxxx "verbatim quote"]` or a `[file:...]`
provenance pointer. Domain reasoning done inline (see "Domain / pseudoenzyme analysis") is my
own analysis of the UniProt record and a pairwise alignment I ran locally.

## Identity and paralogy (KEEP GPM3 SEPARATE FROM GPM1/GPM2)

- **GPM1 (P00950, PGM1_YEAST)** is the *only functional* phosphoglycerate mutase in yeast — the
  real 2,3-bisphosphoglycerate-dependent (cofactor-dependent, dPGM) glycolytic enzyme. This is
  the enzyme that carries the experimentally established EC 5.4.2.11 activity. **Do not attribute
  GPM1's biochemistry to GPM3.**
- **GPM2 (P37012, PMG2_YEAST)** and **GPM3 (Q12326)** are homologous ORFs detected during the
  genome-sequencing project; both are reported to be non-functional homologs.
- Heinisch et al. 1998 is the definitive characterization of GPM2 + GPM3:
  [PMID:9544241 "Our previous data indicated that GPM1 encodes the only functional phosphoglycerate mutase in yeast. However, in the course of the yeast genome sequencing project, two homologous sequences, designated GPM2 and GPM3, were detected."]

## What is KNOWN about GPM3

1. **It is a phosphoglycerate-mutase-family protein (histidine-phosphatase superfamily, dPGM/BPG-dependent subfamily).**
   - UniProt SIMILARITY: "Belongs to the phosphoglycerate mutase family. BPG-dependent PGAM subfamily."
   - Domain architecture from the UniProt DR block: Pfam PF00300 (His_Phos_1), CDD cd07067
     (HP_PGM_like), Gene3D 3.40.50.1240 (Phosphoglycerate mutase-like), PANTHER PTHR11931,
     PROSITE PS00175 (PG_MUTASE). `[file:yeast/GPM3/GPM3-uniprot.txt]`

2. **The catalytic residues of the dPGM active site are conserved in GPM3.**
   - Heinisch: [PMID:9544241 "Key residues in the deduced amino acid sequence, shown to be involved in catalysis for Gpm1 (i.e. His8, Arg59, His181) are conserved in both enzymes."]
   - My own inline alignment confirms this (see Domain analysis below).

3. **GPM3 has NO detectable phosphoglycerate mutase activity, even when forced to express.**
   - [PMID:9544241 "Higher level expression under the control of the yeast PFK2 promoter partially complemented the gpm1 defects, without restoring detectable enzymatic activity."]
   - Under its own (weak) promoter it does not complement a gpm1 deletion at all:
     [PMID:9544241 "Overexpression of the genes under control of their own promoters in a gpm1 deletion mutant did not complement for any of the phenotypes."]

4. **Deleting GPM3 (alone or with GPM2) has no detectable phenotype.**
   - [PMID:9544241 "Nevertheless, deletion of either GPM2 or GPM3, or the two deletions in concert, did not produce any obvious lesions for growth on a variety of different carbon sources, nor did they change the levels of key intermediary metabolites."]

5. **The protein is expressed (at low abundance) and is cytoplasmic.**
   - Expression: UniProt MISCELLANEOUS "Present with 3730 molecules/cell in log phase SD medium"
     with evidence `ECO:0000269|PubMed:14562106` — i.e. the Ghaemmaghami et al. 2003 global protein
     expression study. `[file:yeast/GPM3/GPM3-uniprot.txt]`
   - Localization: GOA records `located_in cytoplasm` (GO:0005737, HDA) from the Huh et al. 2003
     genome-wide GFP-localization study [PMID:14562095, "Global analysis of protein localization in budding yeast."].
   - PE level 1 (evidence at protein level) in UniProt, consistent with the two proteomic datasets.

6. **Evolutionary origin: gene duplication, probable non-functional homolog.**
   - [PMID:9544241 "We conclude that both genes evolved from duplication events and that they probably constitute non-functional homologues in yeast."]

## What is NOT known about GPM3 (the gap)

- **Whether GPM3 has ANY catalytic activity at all** (mutase or otherwise). The mutase reaction
  was assayed and not detected (Heinisch 1998); no other activity has ever been tested.
- **Its in-vivo molecular function or biological role.** Deletion is phenotypically silent under
  the conditions tested; no condition-specific role, partner, or substrate is known.
- **Why the cell retains a third mutase homolog.** GPM3 is expressed as a stable protein
  (~3730 molecules/cell) yet is dispensable and (as far as tested) inactive — the selective
  rationale (if any) for its retention is unknown.
- **Whether the catalytic His residues, though present in sequence, are competent in the folded
  protein.** Heinisch note the residues are conserved yet no activity is recovered even on forced
  expression, so the loss of function is not explained by an obvious active-site lesion.

## Domain / pseudoenzyme analysis (my own inline analysis)

I read `GPM3-uniprot.txt` and ran a local BLOSUM62 global pairwise alignment of GPM3 (Q12326,
303 aa) vs GPM1 (P00950, 247 aa); GPM3 is 42.5% identical to GPM1 over the aligned region. The
three catalytic motifs of the dPGM (cofactor-dependent PGAM; histidine-phosphatase superfamily
clade 1) active site map as follows (GPM3 numbering, motif shown):

| dPGM catalytic element | GPM1 motif | GPM3 motif | GPM3 residue status |
|---|---|---|---|
| N-terminal catalytic His (forms phospho-His intermediate) | `V**RHG**QSEW` (His8) | `L**RHG**QSEL` (His14) | **conserved** (His14; UniProt ACT_SITE 14) |
| Proton donor/acceptor His (RHYG motif) | `NE**RHYG**D` (His88) | `NE**RHYG**A` (His122) | His **conserved** (the D→A after it differs) |
| C-terminal transition-state His (AHGN motif) | `IA**AHGN**S` (His181) | `IV**GHGS**S` (His235) | His **conserved** (UniProt SITE 235); flanking A→G, N→S |

Interpretation: **GPM3 is NOT a classic degenerate pseudoenzyme with an ablated active site.**
The three essential catalytic histidines (equivalent to GPM1 His8/His88/His181, i.e. Heinisch's
His8/Arg59/His181 catalytic set) are all retained in GPM3, matching Heinisch's own statement that
"key residues ... involved in catalysis ... are conserved". This makes GPM3 an unusual case:
catalytic residues present, but no measurable activity. Candidate (untested) explanations
supported by the sequence:

- **A large disordered insertion unique to GPM3.** UniProt annotates a disordered region 168–198
  (`REGION 168..198 /note="Disordered"`, MobiDB-lite) with a basic-and-acidic compositional bias
  (COMPBIAS 177..198). My alignment shows this maps to an ~30-residue insertion that is absent
  from GPM1 (GPM1 has a short `YKYVD` where GPM3 has `NRHLKYGPEEKANERLP...`). Such an insertion in
  the mutase fold could perturb folding, substrate-channel geometry, or the required 2,3-BPG
  cofactor priming.
- **Substitutions in second-shell / substrate-binding positions** (e.g. the RHYG→RHYGA change and
  the AHGN→GHGS change adjacent to the retained catalytic His) could impair substrate binding or
  transition-state stabilization even with the catalytic His intact.

These are hypotheses, not demonstrated mechanisms; the honest position is that the biochemical
reason for GPM3's inactivity is undetermined. I did NOT run structure prediction; this is a
sequence-level analysis of the UniProt record plus a pairwise alignment.

Note on UniProt EC/pathway annotations: the UniProt entry carries `EC=5.4.2.11`,
`PATHWAY: glycolysis`, and a Rhea reaction. These are propagated from the family SIMILARITY
rule (BPG-dependent PGAM subfamily), NOT from measured GPM3 activity — the same entry's FUNCTION
line reads "Could be non-functional." The EC/pathway are therefore family-level inferences, in
tension with the direct experimental finding of no detectable activity.

## Annotation-by-annotation plan (10 GOA annotations)

1. `GO:0004619 phosphoglycerate mutase activity` (IBA, GO_REF:0000033) — MARK_AS_OVER_ANNOTATED /
   over-propagated: phylogenetic (IBA) transfer of the family activity to a paralog that was
   experimentally shown to lack detectable mutase activity (Heinisch 1998). Add propagation_review.
2. `GO:0005829 cytosol` (IBA, GO_REF:0000033) — ACCEPT/KEEP_AS_NON_CORE: consistent with the
   experimental HDA cytoplasm localization; a reasonable location even if the activity is absent.
3. `GO:0061621 canonical glycolysis` (IBA, GO_REF:0000033) — MARK_AS_OVER_ANNOTATED: GPM3 is not
   a functional glycolytic enzyme (no activity; deletion has no metabolite/growth effect).
4. `GO:0003824 catalytic activity` (IEA, GO_REF:0000002, InterPro) — MARK_AS_OVER_ANNOTATED /
   generic root-ish MF; no catalytic activity demonstrated. (Very general; IEA from InterPro.)
5. `GO:0004619 phosphoglycerate mutase activity` (IEA, GO_REF:0000120, EC/Rhea) — same as #1,
   over-annotation from EC mapping; MARK_AS_OVER_ANNOTATED.
6. `GO:0006096 glycolytic process` (IEA, GO_REF:0000120) — MARK_AS_OVER_ANNOTATED, as #3.
7. `GO:0016868 intramolecular phosphotransferase activity` (IEA, GO_REF:0000002, InterPro) —
   MARK_AS_OVER_ANNOTATED; the specific catalytic activity is not demonstrated. (Note: this term
   may be obsoleted/merged in current GO; do not rewrite the GOA id.)
8. `GO:0005737 cytoplasm` (HDA, PMID:14562095) — ACCEPT: direct experimental localization.
9. `GO:0003674 molecular_function` (ND, GO_REF:0000015) — ACCEPT as the honest MF root (SGD's own
   "no data" call reflects the true state: no positively demonstrated activity).
10. `GO:0008150 biological_process` (ND, GO_REF:0000015) — ACCEPT as honest BP root.

Rationale for using MARK_AS_OVER_ANNOTATED (not REMOVE) on the mutase/glycolysis IBA/IEA rows:
these are electronic/phylogenetic inferences (not experimental annotations), and per the GO
guidelines over-propagated IEA/IBA are legitimately down-graded on biological grounds. There is
direct experimental evidence (Heinisch 1998) that the transferred activity is absent, which is
exactly the situation MARK_AS_OVER_ANNOTATED / propagation_review is for. I am NOT removing any
experimental annotation.

## Update after falcon deep research (2026-07-05)

The falcon (Edison) deep-research report landed late (`GPM3-deep-research-falcon.md`, 21
citations, genuine). It is consistent with the Heinisch primary data and adds useful context
(citations are by citekey/DOI, not PMID, so I have NOT used them as `supported_by` quotes):

- **Family layout confirmed:** three paralogs GPM1 (YKL152C, the major functional enzyme),
  GPM2 (YDL021W), GPM3 (YOL056W). GPM1 is a homotetramer (~28 kDa subunits); deletion of GPM1
  blocks growth on glucose.
- **Interpretive nuance / tension worth flagging:** the falcon report (leaning on Papini et al.
  2010, *Biotechnol J* 5:1016-1027, doi:10.1002/biot.201000199, and Costenoble et al. 2011 SRM
  proteomics) argues GPM3's physiological insignificance is "primarily due to insufficient
  endogenous expression rather than complete loss of catalytic competence," inferring "residual
  catalytic capacity" from the *partial complementation* of gpm1Δ when GPM3 is overexpressed
  from the PFK2 promoter. This is an INFERENCE. It stands in tension with the Heinisch (1998)
  primary result that the same PFK2-driven overexpression complemented "without restoring
  detectable enzymatic activity." I therefore keep the honest position: GPM3 has NO directly
  measured mutase activity (Heinisch), while partial complementation on non-fermentable carbon
  after prolonged incubation leaves open the possibility of weak/residual activity that was below
  the assay's detection limit. My review states both facts and does not over-claim activity.
- **Costenoble et al. 2011** (targeted SRM proteomics) reportedly detected Gpm3 protein across
  metabolic states — consistent with the UniProt ~3730 molecules/cell figure; corroborates that
  GPM3 is a genuinely expressed protein.
- **Localization:** falcon agrees GPM3 is cytoplasmic (Huh et al. 2003) with no evidence for the
  cell-wall/moonlighting localization documented for GPM1 (and for *C. albicans* Gpm1
  plasminogen/complement binding). GPM3-specific moonlighting: none known.
- **Evolution:** GPM2/GPM3 arose by duplication; notably Conant & Wolfe (2007) *excluded* the
  GPM2/GPM3 pair from their set of WGD-retained, dosage-amplified glycolytic duplicates —
  consistent with GPM3 being a divergent, near-non-functional paralog rather than a
  flux-boosting duplicate.

Net effect on the review: no change to actions. The over-annotation calls on the mutase/glycolysis
terms remain correct (GPM3 is not a physiologically functional mutase and its deletion is silent),
and the honest knowledge gap (whether it retains ANY residual activity, and why the third homolog
is kept) is if anything reinforced by the expression-vs-activity tension between Heinisch and the
Papini-based interpretation.

## References to cite

- PMID:9544241 — Heinisch et al. 1998, characterization of GPM2/GPM3 (HIGH relevance; the key paper). Abstract-only in cache but the abstract itself contains all the load-bearing findings.
- PMID:14562095 — Huh et al. 2003, global localization (supports cytoplasm; MEDIUM).
- PMID:14562106 — Ghaemmaghami et al. 2003, global expression (supports the ~3730 molecules/cell abundance; MEDIUM).
- file:yeast/GPM3/GPM3-uniprot.txt — domain/active-site features and expression/localization summary.
