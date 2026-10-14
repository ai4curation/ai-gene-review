# Pcbd2 (mouse, Q9CZL5) — curation notes

## Why this review exists

Triggered by **geneontology/go-annotation#6591**, which asks for the molecular
function term on MGI:1919812 (Pcbd2) and MGI:94873 (Pcbd1) to be replaced with
"4-alpha-hydroxytetrahydrobiopterin dehydratase activity", noting that in
PMID:15182178 both enzymes complement *P. aeruginosa* PhhB, a
pterin-4-alpha-carbinolamine dehydratase. The term currently annotated is
`GO:0004505 phenylalanine 4-monooxygenase activity` (IDA); the requested
replacement is `GO:0008124`. Companion review: `genes/mouse/Pcbd1/`, whose notes
set out the term confusion and its origin in full.

No deep-research file: `just deep-research mouse Pcbd2` fails here because no
provider API key is configured. Evidence base is the cached publications, the
UniProt snapshot, the PANTHER PAINT table, and a bioinformatics analysis written
for this review (`Pcbd2-bioinformatics/`).

## The requested fix, and why Pcbd2's case is stronger than Pcbd1's

Same error, same paper, but for Pcbd2 UniProt has recorded the enzymology as
**experimental on this very protein**:

```
DE            EC=4.2.1.96 {ECO:0000269|PubMed:15182178};
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(4aS,6R)-4a-hydroxy-L-erythro-5,6,7,8-tetrahydrobiopterin = ...
CC         Evidence={ECO:0000269|PubMed:15182178};
```

`ECO:0000269` is experimental evidence from the cited publication — i.e. UniProt
read PMID:15182178 and concluded it demonstrates EC 4.2.1.96 for mouse Pcbd2.
(For Pcbd1 the same EC is `ECO:0000250`, by similarity.) So UniProt and the GOA
row disagree outright on the same reference: one says hydro-lyase from this
paper, the other says monooxygenase from this paper. The issue's request resolves
the contradiction in UniProt's favour, and the abstract agrees:

> Like DCoH, DCoH2 forms a tetramer, displays pterin-4alpha-carbinolamine
> dehydratase activity, and binds HNF1alpha in vivo and in vitro.
> [PMID:15182178]

"pterin-4alpha-carbinolamine dehydratase activity" is an exact synonym of
GO:0008124 (OLS-verified). So `MODIFY GO:0004505 → GO:0008124`, keeping IDA and
the reference.

As on Pcbd1, three annotations are collateral:

- `GO:0006571 L-tyrosine biosynthetic process` (IEA, GO_REF:0000108) — WITH field
  is literally `GO:0004505`. Inferred from the wrong MF; **REMOVE**.
- `GO:0004505` (IEA, `ARBA:ARBA00029278`) — a separate ARBA route to the same
  wrong term, so correcting the IDA will not clear it; **REMOVE** and flag the
  rule.
- Note the asymmetry in the GOC inference: Pcbd1's `GO:0006571` row is
  `ECO:0000366` while Pcbd2's is `ECO:0000364`. Both trace to `GO:0004505`.

## An unexploited paper: PMID:24389307

UniProt's `FUNCTION` and `SUBCELLULAR LOCATION` for Pcbd2 both rest on
PMID:24389307 (Kazgan et al., *Gastroenterology* 2014), yet **GOA has no
annotation from it at all**. It is mouse-specific, full text is cached, and it
contains exactly the data GO wants:

- Coactivation, assayed on the mouse protein in a mouse cell line:
  [PMID:24389307 "DCoH2 was distributed in both the nucleus and cytoplasm in this hepatic cell line, with a strong nuclear staining that closely resembled the pattern of SIRT1 (Figure 4D)."]
  and
  [PMID:24389307 "KQ mutant protein displayed a significantly reduced ability to activate a luciferase reporter driven by the mouse FXR promoter in Hepa1-6 cells."]
- Mechanism: [PMID:24389307 "which increases dimerization of HNF-1α"] and
  [PMID:24389307 "SIRT1 was found to deacetylate Dcoh2, promoting its interaction with HNF-1α and inducing DNA binding by HNF-1α."]

Two consequences for this review:

1. The direct nucleus and cytoplasm observations are better evidence than the
   SubCell-keyword IEAs currently carrying those terms. Recorded in the reasons
   via `additional_reference_ids` so a curator can upgrade the evidence codes.
2. `GO:0003713 transcription coactivator activity` is proposed as **NEW**. See
   the comparator check below, because this one needed it.

## Comparator check on the proposed NEW GO:0003713

Project rules say not to add what curators deliberately declined to add, so I ran
the check before proposing. QuickGO for `GO:0003713` over the PCD family returns:

| Gene | Species | Evidence | Reference |
|---|---|---|---|
| PCBD1 | human (P61457) | TAS | PMID:1763325 |
| Pcbd1 | mouse (P61458) | ISO | PMID:1763325 |
| Pcbd1 | rat (P61459) | IDA | PMID:1763325 |
| **PCBD2** | **any species** | **absent** | — |

So GO:0003713 is on PCBD1 in three species and on PCBD2 in none. That pattern is
exactly the shape that usually means "the term does not mean what you think" —
but here the alternative explanation is visible and better supported: human
PCBD2 carries `involved_in GO:0045893` with **IDA** from PMID:11980910, whose
abstract states

> DCoH stabilizes HNF1alpha as a dimer and enhances its transcriptional activity
> on the beta-fibrinogen promoter reporter, and DCoHm had similar activity.
> [PMID:11980910]

(DCoHm is PCBD2.) Curators therefore did not decline the function — they recorded
the **process** for PCBD2 and both the process and the molecular function for
PCBD1. The absence is a missing MF row, not a judgment that PCBD2 is not a
coactivator.

Applying the participation test: the entity doing the work is Pcbd2 itself. It
binds Hnf1a, increases Hnf1a dimerization, and a point-mutant that mimics
constitutive acetylation loses reporter activation — so it is a component of the
activating complex, not merely upstream of or required for transcription.
`GO:0003713` is the term for that — its definition is "A transcription
coregulator activity that activates or increases the transcription of specific
gene sets via binding to a DNA-binding transcription factor at a specific genomic
locus, either on its own or as part of a complex", which is DCoH2 on Hnf1a
exactly. It is neither an ancestor nor a descendant of the `GO:0045893` the gene
already has (one is MF, the other BP). The four coactivator mechanisms the
definition goes on to list are introduced as examples, so dimer stabilisation not
being among them is not an exclusion.

## Mitochondrion: the interesting annotation

`GO:0005739 mitochondrion` HDA from PMID:18614015 (MitoCarta) is the one row that
does not fit the characterised biology — the dehydratase substrate is made by
cytosolic hydroxylases and the coactivator partner is nuclear — and MitoCarta's
own paper concedes MS-based inventories carry "up to 41% false positive rates".
UniProt has not adopted it: `SUBCELLULAR LOCATION` lists only Cytoplasm and
Nucleus.

It would be easy to call this a contaminant. I wrote
`Pcbd2-bioinformatics/nterm_mts_analysis.py` to test the mechanistic
prerequisite instead, because Pcbd2 has something Pcbd1 does not: ~33 extra
N-terminal residues (136 aa vs 104 aa). Scored against 259 reviewed mouse
proteins with annotated mitochondrial transit peptides and 300 reviewed mouse
cytosolic proteins:

- mouse Pcbd2 residues 1–32: net charge **+4** (presequence median +4), **4 Arg**
  (median 4), **0 acidic** (median 0), max ⟨µH⟩ **0.423** (median 0.416).
- mouse Pcbd1 residues 1–32, as internal control: net charge **−1** (0.2nd
  percentile of presequences), **6 acidic** (99.8th percentile). Opposite case.
- Confounder, stated honestly: the extension is **40.6% Ala**, above both
  reference distributions, so the zero acidic count is partly low-complexity bias
  rather than selection. What survives is the positive charge and amphipathicity.

Consistent with cleavage, the two Pcbd2 crystal structures (1RU0, 4WIL) cover
33/34–136 — Rose et al. assayed the protein *without* the extension — and
UniProt flags both source mRNAs `Erroneous initiation` because they began at the
internal Met34.

And the organellar evidence is thicker than one HDA row:

- Human PCBD2 is in **MitoCoP**: QuickGO has `Q9H0N5 located_in GO:0005739` with
  **HTP** from PMID:34800366, a study built to exclude contaminants
  [PMID:34800366 "We classified >8,000 proteins in mitochondrial preparations of human cells and defined a mitochondrial high-confidence proteome of >1,100 proteins (MitoCoP)."]
- Mouse Pcbd2's K120/K124/K131 acetylation comes from PMID:23576753, a SIRT3
  study of the **liver mitochondrial** acetylome (`ECO:0007744` on the UniProt
  MOD_RES lines), with succinylation at the same lysines from PMID:23806337
  (SIRT5). Both sirtuins are mitochondrial.
- The family has a genuine mitochondrial member elsewhere: PANTHER's PAINT table
  for PTHR12599 has a `GO:0005739` IBD at PTN000972177 (Embryophyta), seeded by
  `AGI_LocusCode:AT1G29810` = Q6QJ72, "Pterin-4-alpha-carbinolamine dehydratase 2,
  **mitochondrial**".

All of that is the same class of evidence (detection in organellar preparations),
so none of it substitutes for imaging or fractionation. But four preparations
across two species, one explicitly contaminant-filtered, plus a presequence-like
extension, is not the profile of a single artefact. **Action: KEEP_AS_NON_CORE** —
retain, do not treat as a site of either characterised function, and see
`RESULTS.md` for the experiments that would settle it.

## PANTHER note

Pcbd2 is in PTHR12599 subfamily **SF15** ("PTERIN-4-ALPHA-CARBINOLAMINE
DEHYDRATASE 2"). It does **not** receive the IBAs that Pcbd1 gets from
PTN002650414, even though that node is placed at taxon:117571 (Euteleostomi) and
both paralogs descend from the vertebrate ancestor. The node therefore appears to
sit below the Pcbd1/Pcbd2 duplication. Since GO:0008124 is experimentally
supported for Pcbd2 itself (UniProt `ECO:0000269|PubMed:15182178`), this looks
like a case where the dehydratase IBD could be asserted deeper. Raised as a
question for PAINT curators, not actioned.

## Summary of actions

| Term | Evidence | Action |
|---|---|---|
| GO:0004505 phenylalanine 4-monooxygenase activity | IDA PMID:15182178 | **MODIFY → GO:0008124** (the issue's ask) |
| GO:0004505 | IEA ARBA:ARBA00029278 | **REMOVE** (independent ARBA fix needed) |
| GO:0006571 L-tyrosine biosynthetic process | IEA GO_REF:0000108 | **REMOVE** (inferred from the wrong MF) |
| GO:0005515 protein binding (w/ Hnf1a) | IPI PMID:15182178 | **MODIFY → GO:0140297** |
| GO:0005515 protein binding (w/ Pcbd1) | IPI PMID:15182178 | **UNDECIDED** (paralog hetero-oligomer; as on Pcbd1) |
| GO:0042802 identical protein binding (w/ self) | IPI PMID:15182178 | KEEP_AS_NON_CORE |
| GO:0005634 nucleus ×2, GO:0005737 cytoplasm | IEA / IPI | ACCEPT (direct mouse evidence available to upgrade) |
| GO:0005739 mitochondrion | HDA PMID:18614015 | **KEEP_AS_NON_CORE** |
| GO:0006729 tetrahydrobiopterin biosynthetic process | IEA InterPro | ACCEPT (regeneration, not de novo) |
| GO:0008124 | IEA GO_REF:0000120 | ACCEPT (core) |
| GO:0045893 positive regulation of DNA-templated transcription | ISO GO_REF:0000119 | ACCEPT (core) |
| GO:0003713 transcription coactivator activity | — | **NEW** from PMID:24389307 |
