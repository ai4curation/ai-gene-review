# ADAMTSL5 (Q6ZMM2) — review notes

PAINT + affinage campaign. Branch `paint/ADAMTSL5`.

## What the gene is

ADAMTSL5 (ADAMTS-like protein 5; synonym THSD6) is a small secreted, N-glycosylated
extracellular-matrix glycoprotein of the ADAMTS superfamily. At **481 aa** it is the
smallest member of the family by a wide margin (ADAMTSL1 1762, ADAMTSL2 951, ADAMTSL3
1691, ADAMTSL4 1074, THSD4 1018, PAPLN 1278 aa). Domain architecture from the UniProt
feature table: signal peptide 1–42, mature chain 43–481, a single **TSP type-1 domain
(45–97)**, and a C-terminal **NTR module (360–479)**, joined by a proline-rich,
disordered segment (331–361).

## The catalytic question — established, not assumed

The campaign brief flagged "the ADAMTSL proteins lack the catalytic metalloprotease
domain" as a lead to establish. It holds for ADAMTSL5, on three independent lines:

- UniProt CAUTION: [file:human/ADAMTSL5/ADAMTSL5-uniprot.txt "lacks the metalloprotease and disintegrin-like domains which are typical of that family"]
- The gene's own primary paper: [PMID:23010571 "In contrast to ADAMTS proteases, ADAMTSLs lack a catalytic domain and thus have no proteolytic activity."]
- Sequence scan (this review): the zinc-binding signature `HExxHxxGxxHD` is absent, and
  there is **no `HExxH` substring at all** in the 481-residue sequence. Its InterPro
  match set contains no peptidase/reprolysin (M12B) signature.

**But the predicted annotation error did not occur.** ADAMTSL5's GOA contains no
peptidase term of any kind — no `GO:0004222`, no `GO:0008237`, no `GO:0006508`. I
recorded this as a hypothesis that was *not confirmed*, not as a finding. PAINT
actually got this right: the catalytic terms at node `PTN000347317` reached all four
catalytic ADAMTS controls and none of the seven non-catalytic members, and ADAMTSL2
even carries an explicit `NOT|enables GO:0004222` (IKR at `PTN002673039`).

The *shape* of the error does appear one aspect over, in BP — see `GO:0030198` below.

## Annotation-by-annotation reasoning

12 GOA rows. The `fetch-gene` stub seeded only **9** — it collapsed the three
`GO:0005515` partner rows into one and the two `GO:0031012` IDA rows (MGI- and
UniProt-assigned) into one. Restored to 12 so every row gets its own verdict.

### ACCEPT — the experimental core (5 rows, all `PMID:23010571`)

`GO:0008201 heparin binding` IDA, `GO:0050436 microfibril binding` IDA,
`GO:0031012 extracellular matrix` IDA ×2, `GO:0005576 extracellular region` IDA.

Heparin binding is well documented and localised to the NTR module:
[PMID:23010571 "only the C-terminal fragment containing the NTR-module was retained by the heparin matrix"],
with the interaction shown to be ionic
[PMID:23010571 "0.5 and 1M NaCl substantially eluted the bound proteins, indicative of an ionic interaction between ADAMTSL5 and heparin"].

Microfibril binding rests on direct affinity co-isolation with both fibrillins plus
colocalisation:
[PMID:23010571 "Taken together, the findings are consistent with specific binding of ADAMTSL5 to fibrillin-1 and fibrillin-2 and to their macromolecular assemblies, i.e., fibrillin microfibrils."]
`GO:0050436` is_a `GO:0050840 extracellular matrix binding`, and there is **no
"fibrillin binding" term in GO** (OLS returns nothing), so `GO:0050436` is the most
specific molecular function available.

Caveat noted but not acted on: these assays used **recombinant/exogenous** ADAMTSL5
added to fibroblast cultures rather than native protein, which by the campaign's rule
of thumb leans toward IMP. I did not overturn the curators' IDA calls — for a secreted
protein this is standard practice, and the authors ran a non-permeabilised staining
control confirming the signal was extracellular
[PMID:23010571 "suggesting that the stained structures were extracellular and corresponded to fibrillin-1 containing microfibrils in ECM"].

### ACCEPT — `GO:0031012` IBA, and it is unusually well founded

WITH/FROM has 17 tokens = 16 protein donors + the node `PANTHER:PTN000347317`. This
matches the cached PAINT seed list **exactly** (asserted in code). **All 16 protein
donors carry their own experimental IDA/HDA** for the term or a descendant, so
`SOURCE_WEAK_OR_INFERRED` would be contradicted by my own measurement. One token is
self-referential (`UniProtKB:Q6ZMM2`) — a PAINT curator judging the function core,
which is valid, hence `NO_FAILURE_CORE`.

The donor set spans **four distinct locations** — extracellular matrix (14), basement
membrane (4), interstitial matrix (1), microfibril (1). `GRANULARITY_MISMATCH` requires
donors to agree; they do not, so `GO:0031012` **is** the LCA and refining it would mean
arbitrarily preferring one donor's compartment. ACCEPT with no specificity upgrade.

Also checked and negative (the ACRV1 shape): the IBA does not land *above* its donors —
14 of 16 hold the term itself — so no downward MODIFY is warranted.

### ACCEPT — `GO:0005576` IEA from `UniProtKB-SubCell:SL-0243`

Straightforward: a signal peptide (1–42) plus experimentally demonstrated secretion.
The SubCell→GO mapping is doing exactly what it should.

### MARK_AS_OVER_ANNOTATED — `GO:0030198 extracellular matrix organization` IEA

Two independent legs:

1. **The source signature bundles proteases with non-proteases.**
   `InterPro:IPR013273` is named, literally, "ADAMTS/ADAMTS-like" (26,580 proteins) and
   carries exactly one GO mapping — `GO:0030198`. For the catalytic ADAMTS members, ECM
   organization follows from ECM proteolysis. ADAMTSL5 has no such activity. This is the
   familiar "a domain's name is not an activity" failure moved one aspect over: **a
   family signature too broad to carry a process**.
2. **The only direct test of it was negative.**
   [PMID:23010571 "However, comparison of microfibril density in fBNL cell cultures grown in the presence of ADAMTSL5 or vector conditioned medium, did not identify a consistent difference (data not shown)."]
   The abstract puts it as colocalisation "but without discernible effect on microfibril
   assembly". Direct binding to fibronectin was also not supported.

**Why not REMOVE.** The negative is a *"data not shown"* result from a single
exogenous-protein assay. It shows no role has been **demonstrated**; it does not refute
one. UniProt itself hedges — "May play a role in modulation of fibrillin microfibrils".
`MARK_AS_OVER_ANNOTATED` is the honest ceiling.

**A third leg I deliberately did NOT use.** ADAMTSL5 has no `GO:0030198` **IBA**, while
ADAMTSL2/ADAMTSL4/THSD4 got one from the same node. That looks like PAINT declining to
propagate the process to ADAMTSL5 — but the propagation is incoherent family-wide (see
below), and ADAMTSL1 and PAPLN received *nothing at all*. So the absence is more likely
a propagation gap than a judgement, and leaning on it would be rationalising a number I
could not explain.

### MARK_AS_OVER_ANNOTATED — the three `GO:0005515` rows

All three from `PMID:32296183` (HuRI). IntAct shows each logged under **three
sub-methods of one experiment** — `two hybrid array` + `two hybrid prey pooling
approach` + `validated two hybrid`, MI-score 0.56. UniProt's `NbExp=3` is therefore
**one screen counted three ways** — the ACRV1 finding, replicated here on a second gene.

Distinct partner counts (derived as entity sets; IntAct *records* are not partners):

| protein | records | distinct partners | localisation |
|---|---|---|---|
| CYSRT1 | 1670 | **517** | cornified envelope |
| KRTAP5-9 | 842 | **213** | intracellular hair-keratin matrix |
| FHL5 | 316 | **108** | nucleus |
| ADAMTSL5 | 22 | **12** | secreted / ECM |

Every partner is topologically incompatible with a signal-peptide secreted ECM protein.
Decided **per partner** as the brief requires; all three independently come out the
same. All three resolve to reviewed canonical Swiss-Prot entries at canonical lengths —
no ORFeome/TrEMBL substitution of the ACRV1 kind (negative result, recorded).

I differ here from the merged **ADAMTSL4** review, which used `REMOVE` on four
comparable Y2H `GO:0005515` rows. Per this campaign's convention an unreplicated screen
hit is `MARK_AS_OVER_ANNOTATED`, and `REMOVE` is reserved for demonstrably wrong
inferences. Flagged as a cross-family inconsistency rather than silently diverging.

### MODIFY — `GO:0071953 elastic fiber` TAS → `GO:0001527 microfibril`

The TAS source `PMID:23962539` is a **review** (`full_text_available: false`) used as
the reference for **62 distinct entities**, assigning `GO:0071953` to **41** of them.
Its abstract never mentions ADAMTSL5. The same curation from the same review assigned
the *more specific* `GO:0001527 microfibril` to 15 other proteins including
THSD4/ADAMTSL6 — so the specific term was available and simply not chosen here.

Meanwhile the gene's own primary data supports microfibril association specifically,
and **UniProt already records `GO:0001527; C:microfibril; IDA:UniProtKB`** — a term
**GOA does not carry** (verified: QuickGO returns exactly 12 annotations for Q6ZMM2 and
`GO:0001527` is not among them). `GO:0001527` is current and is a `part_of` child of
`GO:0071953`, so the replacement retains the parent by closure while gaining precision.
The merged ADAMTSL4 review independently proposed `GO:0001527` as a NEW term, which is
useful convergent support.

## The main PAINT finding: one node, incoherent propagation

All eight human ADAMTSL/papilin proteins sit in **PTHR13723**. Node `PTN000347317`
carries four IBD terms. Who received them:

| gene | subfam | GO:0031012 | GO:0030198 | GO:0004222 | GO:0006508 |
|---|---|---|---|---|---|
| ADAMTSL1 | SF157 | – | – | – | – |
| ADAMTSL2 | SF147 | IBA | IBA | **NOT-IBA** | – |
| ADAMTSL3 | SF169 | IBA | – | – | – |
| ADAMTSL4 | SF144 | IBA | IBA | – | – |
| **ADAMTSL5** | SF173 | **IBA** | – | – | – |
| THSD4 | SF16 | IBA | IBA | – | – |
| PAPLN | SF281 | – | – | – | – |
| ADAMTS1/9/10/17 | *catalytic* | IBA | IBA | IBA | IBA |

From a single node, `GO:0031012` reached 5 of 7 and `GO:0030198` reached 3 of 7, in no
biologically coherent pattern. The sharpest case is **PAPLN**, which received nothing
although **three of its own orthologs are seeds** for `GO:0031012` at that very node —
fly `Ppn` (`FB:FBgn0003137`), mouse `Papln` (`MGI:MGI:2386139`) and worm `mig-6/ppn-1`
(`WB:WBGene00003242`). Human PAPLN and human ADAMTSL1 both have **no IBA at all**.

This is not the "right term, wrong node" defect (AADACL) nor the "mis-placed member"
defect (ACTL8). It is a **propagation-coverage** defect: the node and its term
assignments look correct, and the term simply failed to reach some descendants.

Reported once in `suggested_questions`, naming all affected genes, rather than repeated
per gene.

## Cross-check with the sibling agents (ADAMTSL1, ADAMTSL3)

Derived independently from QuickGO rather than read off their branches:

- **ADAMTSL3** carries an `GO:0031012` IBA **identical to mine** — same node
  `PTN000347317`, same 17 WITH/FROM tokens. Our two derivations should agree; if that
  review reaches a different verdict on the same row, the disagreement is the finding.
  ADAMTSL3 also shares the `GO:0071953` TAS from `PMID:23962539` and the InterPro
  `GO:0030198` IEA — so all three of my non-ACCEPT verdicts have a direct counterpart
  there.
- **ADAMTSL1** has only **4 annotations** and **no IBA at all** despite being in
  PTHR13723 (SF157). Its only BP row is the same InterPro `GO:0030198` IEA. If that
  review reports ADAMTSL1 as having IBA support, that is a discrepancy worth resolving.

## An ontology issue this surfaced

`GO:0001527 microfibril` is `part_of` `GO:0071953 elastic fiber`, which asserts every
microfibril is part of an elastic fiber. That contradicts `GO:0001527`'s **own
definition** — "Extracellular matrix components occurring independently **or** along
with elastin" — and contradicts the ciliary zonule, a fibrillin-microfibril structure
essentially devoid of elastin (the reason FBN1 mutations cause ectopia lentis).
ADAMTSL5's own expression pattern is a further mismatch: cartilage and bone are not
elastic-fibre tissues
[PMID:23010571 "Immunostaining during mouse organogenesis identified ADAMTSL5 in musculoskeletal tissues such as skeletal muscle, cartilage and bone, as well as in many epithelia."]

## Non-GO biology (informs `description`, not annotations)

- **Psoriasis autoantigen.** ADAMTSL5 is an HLA-C\*06:02-presented melanocyte
  autoantigen [PMID:26621454 "we identified ADAMTS-like protein 5 (ADAMTSL5) as an HLA-C*06:02-presented melanocytic autoantigen of the Vα3S1/Vβ13S1 TCR"].
  The recognised peptide `VRSRRCLRL` maps to **residues 67–75**, inside the TSP type-1
  domain (verified against the UniProt sequence). This is a property of the peptide in
  an MHC groove, not a molecular function of the secreted protein, so it generates no
  GO annotation.
- **Hepatocellular carcinoma.** [PMID:33197513 "ADAMTSL5 targeting interfered with tumorigenic properties of HCC cells in vitro and in vivo, whereas ADAMTSL5 overexpression conferred tumorigenicity to pre-tumoural hepatocytes sensitized to transformation by a modest level of MET receptor expression."]
  Knockdown/overexpression in a cancer context; I did not propose a signalling GO term
  from it, since the RTK effects are downstream and the mechanism connecting a secreted
  ECM protein to receptor levels is not established.

## Provider record (affinage)

`gates_passed: False`. The tripped gate is specifically the **self-evaluation pairwise
tie** (`self_evaluation_pairwise: tie`), not a faithfulness failure — `faith_pct` is
100.0. All 7 citations are numeric PMIDs; **no `PMID:bio_*` bioRxiv ids**. I verified
every claim I used against the cited PMID directly and quoted the PMIDs, never the
provider's prose. The narrative is broadly accurate on this gene; its GO grounding
however proposes `GO:0008289 lipid binding` and `GO:0098772 molecular function
regulator activity`, **neither of which has any support** — the ligand demonstrated is
heparin, a glycosaminoglycan (`GO:0008201`), not a lipid. Not imported.

## Checks run, including the ones that came back negative

- **Retraction / erratum / expression of concern** on all 9 PMIDs relied on, via PubMed
  publication types **and** each record's own `CommentsCorrections` (a Publisher
  Correction is invisible to a pubtype query): **none flagged**. `PMID:26621454` has two
  `Comment in` entries — commentaries, not corrections.
- **Reference projection test**: `PMID:23010571` annotates only **2** entities
  (ADAMTSL5 + mouse ortholog) — gene-specific curation, not a projection. Negative.
- **Partner accession integrity**: all three IPI partners reviewed, canonical, correct
  length. Negative.
- **IBA-above-donor precision defect**: absent. Negative.
- **Dead-accession check**: every WITH/FROM UniProt lookup returns a named entry; the
  resolver raises rather than reporting a silent zero.

## Process notes worth carrying to the next gene

- **QuickGO's `geneProductId` rejects MOD ids** (`MGI:`, `FB:`, `WB:`, `RGD:`) with
  HTTP 400 in every form. Donor evidence can only be queried through the resolved
  UniProt accession. My first script printed "NONE" for all 13 MOD tokens — a silent
  degradation reading as a null result, which would have inverted the conclusion from
  "16/16 donors have their own experimental evidence" to "almost none do".
- **UniProt does not index WBGene ids** (`xref:wormbase-WBGene00003242` → `[]`); it keys
  WormBase xrefs on the CDS name. Resolve WBGene → symbol via the WormBase REST first.
- **That symbol search must use `gene_exact:`.** Fuzzy `gene:mig-6` also returns
  mig-10/mig-5/mig-14/mig-18 and puts the **wrong** entry first. The 16/16 count would
  otherwise have been right for the wrong reason.
- **QuickGO strips the DB prefix from WITH/FROM tokens.** `withFrom[].connectedXrefs[]`
  returns `{"db": "FB", "id": "FBgn0003137"}` as *two fields*, so the `id` alone is
  `FBgn0003137`, not `FB:FBgn0003137`. Comparing that set naively against a GOA TSV
  WITH/FROM string reports **17 vs 17 tokens that are "not identical"** for data that is
  in fact the same — the token must be reassembled as `db + ":" + id` first. I hit this
  while verifying the ADAMTSL3 cross-check; the sibling comparison itself was sound
  (both sides came from QuickGO, so both were in the stripped serialisation), but the
  same-size-yet-different result is exactly the kind of discrepancy that must be
  investigated rather than waved through.
