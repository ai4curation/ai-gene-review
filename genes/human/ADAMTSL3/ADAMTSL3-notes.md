# ADAMTSL3 (P82987, human) — review notes

Working journal for the PAINT + affinage review of human ADAMTSL3 / punctin-2.

## 1. What the protein is

UniProt P82987, `ATL3_HUMAN`, 1691 aa, `PE 1: Evidence at protein level`, HGNC:14633,
chromosome 15q25.2. Cleaved signal peptide (`FT   SIGNAL          1..26`), chain 27–1691,
heavily N-glycosylated (17 annotated `CARBOHYD` sites), secreted into the extracellular
matrix.

Domain content, read off the UniProt feature table rather than the family name: **ten
PROSITE TSP type-1 domains** (SMART counts 12, Pfam `TSP1_ADAMTS` 11 — the counts differ
by method, and the original paper says 13), **three Ig-like C2-type domains** at
896–992 / 1185–1279 / 1296–1378, an ADAMTS-type cysteine-rich region
(`InterPro:IPR045371 ADAMTS_CR_3`, `Pfam:PF19236`), and a C-terminal **PLAC** domain at
1655–1691. Two splice isoforms (P82987-1, P82987-2) differing only in the last 35
residues, which in isoform 2 replaces the PLAC-domain C terminus.

There is **no metalloprotease domain and no disintegrin-like domain**. This is stated
three independent ways:

- UniProt's own `CAUTION` line: `lacks the metalloprotease and disintegrin-like domains which are` typical of that family (`ECO:0000305`);
- the cloning paper [PMID:14667842 "These multi-domain proteins lack both a protease domain and a disintegrin-like domain but are remarkably similar in their domain organization to the ADAMTS proteases, hence the name ADAMTS-like."];
- absence of any M12B/peptidase signature in the InterPro/Pfam/PROSITE match list, which
  contains only TSP1, Ig, `ADAMTS_CR_3` and PLAC.

So the "ADAMTSL proteins lack the catalytic domain" premise **is** true for ADAMTSL3 —
established here from the record, not assumed. The consequence for this review is the
*opposite* of the usual campaign pattern, see §3.

Product size in cells: [PMID:14667842 "Using these and a monoclonal antibody to a C-terminal myc tag, we show that in transfected COS-7 cells, punctin-2 is expressed as a 210-kDa glycoprotein that is located in the extracellular matrix."]

Expression is broad: [PMID:17597111 "ADAMTSL3 is expressed in epithelial cells of the colon, fallopian tube, skin, breast, prostate, epididymis, liver, pancreatic islets and bile ducts, as well as by vascular endothelial cells, smooth muscle cells, fibroblasts, cortical and ganglionic neurons and cardiac myocytes."]

## 2. The GOA record is tiny and lopsided

18 rows in `ADAMTSL3-goa.tsv`:

| n | term | evidence | source |
|---|---|---|---|
| 1 | `GO:0031012` extracellular matrix | IBA | GO_REF:0000033, node `PTN000347317` |
| 1 | `GO:0030198` extracellular matrix organization | IEA | `InterPro:IPR013273` |
| 15 | `GO:0005515` protein binding | IPI | 2 interactome papers, 13 distinct partners |
| 1 | `GO:0071953` elastic fiber | TAS | PMID:23962539 (a review) |

The `fetch-gene` stub collapsed the 15 `GO:0005515` rows into 2, so the review had to be
expanded back to one row per partner (the ACTR5 lesson). Coverage is asserted
programmatically by `ADAMTSL3-bioinformatics/analyze_adamtsl3.py --only coverage`, keyed on
(term, evidence, reference, with/from).

Notable *absence*: there is **no IDA row for extracellular matrix localisation** even
though UniProt records `SUBCELLULAR LOCATION: Secreted, extracellular space, extracellular matrix`
with `ECO:0000269|PubMed:14667842`. The direct experimental localisation exists and has
simply never been transferred to GOA.

## 3. The catalytic-loss question, and where the real defect is

The campaign hypothesis was that a peptidase-flavoured annotation might have reached
ADAMTSL3 by domain-name propagation. **It has not.** No peptidase, metallopeptidase,
proteolysis or hydrolase term appears anywhere in ADAMTSL3's GOA. That hypothesis is
refuted for this gene.

But resolving *why* it has not turned up a genuine, fixable PAINT defect in the other
direction. From PANTHER's primary files (`IBD.gaf` for node annotations,
`gene_association.paint_uniprot.gaf.gz` for the leaf projections — both parsed by the
analysis script, not read off QuickGO):

- Family `PTHR13723` has exactly **two** PAINT-annotated nodes.
- The root node `PTN000347317` carries four IBD annotations: `GO:0031012` (C),
  `GO:0030198` (P), **`GO:0004222` metalloendopeptidase activity (F)** and **`GO:0006508`
  proteolysis (P)**. The seeds for the two catalytic terms are exclusively genuine ADAMTS
  proteinases (ADAMTS1/2/3/4/5/7/12/13 and orthologues).
- The second node, `PTN002673039`, carries `NOT GO:0004222` (IKR, "inferred from key
  residues") and `NOT GO:0006508` (IRD), scoped to `taxon:117571`.

Streaming the leaf GAF shows `PTN002673039` projects onto exactly **22 leaves, every one of
them an ADAMTSL2 orthologue** (human ADAMTSL2 Q86TH1, mouse Adamtsl2 Q7TSK7, and 20
vertebrate orthologues). So PAINT has *already made the key-residue judgement that the
catalytic domain is lost*, and has attached it to the **ADAMTSL2 orthology group alone**.

The same loss is shared, identically, by ADAMTSL1, ADAMTSL3, ADAMTSL4, ADAMTSL5, PAPLN,
THSD4 and the invertebrate members (madd-4, loh, papilin). None of them carries the
`NOT`. The projection matrix (recomputed by the script) is:

| member | GO:0031012 | GO:0030198 | GO:0004222 | GO:0006508 |
|---|---|---|---|---|
| ADAMTS1 / 9 / 10 / 17 (catalytic control) | ✓ | ✓ | ✓ | ✓ |
| ADAMTSL2 (human + mouse) | ✓ | ✓ | **NOT** | – |
| ADAMTSL4 (human + mouse) | ✓ | ✓ | – | – |
| THSD4 (human + mouse) | ✓ | ✓ | – | – |
| **ADAMTSL3 (human + mouse)** | ✓ | – | – | – |
| ADAMTSL5 (human) | ✓ | – | – | – |
| ADAMTSL1 (human) | – | – | – | – |
| PAPLN (human + mouse) | – | – | – | – |
| madd-4 (worm) | – | – | – | – |

Two things follow, and they are different in kind:

1. **The `NOT GO:0004222` sits at the wrong node** — the ADAMTSL2 orthologue node rather
   than the ancestral node of the non-catalytic ADAMTSL clade. This is the AADACL2/3/4
   "right term, wrong node" pattern, in its *too-deep* form. Moving or duplicating that
   IKR to the clade LCA would state the catalytic loss for six more human genes in one
   edit. This belongs in `suggested_questions` once, naming all affected genes.
2. **`GO:0030198` reaches some non-catalytic members and not others**, on no visible
   biological criterion: ADAMTSL2, ADAMTSL4 and THSD4 receive it, ADAMTSL3 and ADAMTSL5 do
   not. ADAMTSL3 has *more* direct evidence for matrix organisation than several members
   that do receive it (§4, §5). Its `GO:0030198` arrives instead from InterPro. The two
   pipelines happen to agree here; the point is that PAINT's coverage is ragged, not that
   the InterPro term is wrong.

The `NOT GO:0006508` IRD row at `PTN002673039` produces **zero** leaf annotations — even
ADAMTSL2 has no NOT-proteolysis row. Recorded as an observation; there may be an export
rule suppressing a `NOT` where no positive was projected.

Positive control for all of the above: the four catalytic ADAMTS members *do* receive
`GO:0004222`, so absence in the ADAMTSL rows is a property of the projection and not of
the query. The script raises if that control fails.

## 4. Molecular partners that GOA does not have

The most important paper for this gene's molecular function is not in its GOA at all.

[PMID:22242013 "Similar to ADAMTSL-6 [24], ADAMTSL-2, -3, and papilin polypeptides interacted with the N-terminal half of fibrillin-1, while ADAMTSL-1 did not."]
— surface plasmon resonance against recombinant fibrillin-1 polypeptide rF90.

- [PMID:22242013 "Full-length ADAMTSL-2 (320-0 nM) interacts with rF90, as does the C-terminal end of ADAMTSL-3 (80-0 nM)."]
- Specificity control: [PMID:22242013 "ADAMTSL-2, -3, and -6 and papilin polypeptides did not bind to recombinant fibrillin-1 polypeptides with the WMS three-domain deletion (Figure 5a and Table S1)."] — the Weill–Marchesani three-domain deletion abolishes binding, so the interaction maps to a defined region of fibrillin-1.
- [PMID:22242013 "SPR also showed that the C-terminal end of ADAMTS-10 interacted with the C-terminal end of ADAMTSL-3 with high binding affinity (KD = 2 nM) (Figure 5c)."] — and this is selective: [PMID:22242013 "However, neither ADAMTSL-2 nor -1 bound to ADAMTS-10, indicating that ADAMTS enzymes may partner only with specific ADAMTSL proteins."]
- [PMID:22242013 "Binding between ADAMTSL-3 and the C-terminal domains of LTBP-1 was also detected, but neither ADAMTSL-2 nor -3 interacted with LTBP-4."] — again selective.

**Internal contradiction in that paper, which changes the evidence code.** The Results
describe the reagents as `recombinant human ADAMTSL-1, -2, -3, and mouse papilin
polypeptides`, but the Methods say
[PMID:22242013 "Constructs for ADAMTSL3 were made using a clone (RIKEN) and mouse lung cDNA."]
(and, in the same paragraph, that ADAMTSL2 came from a mouse RIKEN clone, contradicting
the same sentence). A RIKEN clone plus mouse lung cDNA is mouse. Only ADAMTSL1 is
explicitly human (`Full-length ADAMTSL1 was obtained from human fibroblast cDNA`). The
conservative reading is that the ADAMTSL-3 polypeptide was **mouse**, so the human
annotation should be `ISS` with the mouse orthologue as supporting entity, not `IPI`. The
discrepancy is recorded rather than resolved — it is a question for the authors.

**Explicit negative in the same paper**, which bounds how far the fibrillin link can be
taken: [PMID:22242013 "Since antibodies specific for ADAMTSL-2 and -3 are not yet available, we were unable to determine whether these proteins also colocalize with fibrillin-1 in skin and whether these are also reduced in WMΔ mutant mice."]
No published work localises ADAMTSL3 protein to a microfibril or an elastic fibre. That
matters for the `GO:0071953` row (§6).

## 5. TGF-β, and the strongest human-cell experiment

[PMID:36539599 "Here we show that the secreted glycoprotein ADAMTSL3 regulates TGFβ in the heart."]

Loss of function (mouse): [PMID:36539599 "We found that Adamtsl3 knock-out mice develop exacerbated cardiac dysfunction and dilatation with increased mortality, and hearts show increased TGFβ activity and CFB activation after pressure overload by aortic banding."]

Gain of function, and this one is **human cells with the human protein**:
[PMID:36539599 "For further mechanistic insights, we overexpressed full-length ADAMTSL3 (L3) and a vehicle control adenovirus (veh) in cultures of human foetal CFBs (hfCFBs) (Fig. S5a), which form an extensive ECM network11."]
with the readout
[PMID:36539599 "Immunoblotting revealed reduced pSMAD (Fig. 4h) and reduced active TGFβ (Fig. 4i), indicating reduced TGFβ signalling."]
and
[PMID:36539599 "Additionally, levels of the LLC, consisting of the latency-associated peptide (LAP), transcribed from the TGFB1 gene, and LTBP1 were reduced in L3 cell and ECM lysates (Fig. 4j-k), indicating reduced TGFβ production."]

Adenoviral overexpression is a perturbation, so this is **IMP**, not IDA. The two halves
agree in sign, which is what makes the negative-regulation call safe:
[PMID:36539599 "Taken together, the loss-of-function and gain-of-function studies suggest ADAMTSL3 as an inhibitor of TGFβ signalling in the heart in vivo and in cardiac fibroblasts in vitro."]

The mechanism is consistent with §4: LTBP-1 and fibrillin-1 are the two proteins that
sequester the large latent TGF-β complex in the matrix, and ADAMTSL3 binds both. The same
paper frames the family this way: [PMID:36539599 "ADAMTSLs are structurally related to the ADAMTS ECM proteases12, but lack a catalytic domain, leaving their biological function largely unknown."]

**Not** annotated: the cardiac phenotypes themselves. Those are mouse, and a
pressure-overload phenotype is a stress response rather than a normal-physiology process
for this protein; the reviewable claim is the TGF-β regulation, which has human-cell
support.

## 6. The elastic-fiber TAS row

`GO:0071953` `located_in`, TAS, from [PMID:23962539] — a review, not primary data, and
`full_text_available: false` in our cache. Its abstract does not name ADAMTSL3.

Reference-scope check (the ACTR8/ACTRT3 discriminator): querying QuickGO by reference
returns **66 annotations over 62 distinct entities**, all TAS, all `GO_Central`, split
`GO:0071953` × 41 entities, `GO:0001527` × 15, `GO:0140149` × 8, `GO:0140144` × 2. So it is
a bulk curation of an elastic-fibre proteome from a specialist review.

But it is **not** an indiscriminate family sweep, and that is the point that decides the
action. The `GO:0071953` set contains ADAMTSL3, ADAMTSL4, ADAMTSL5 and THSD4 (plus mouse
orthologues) and **excludes ADAMTSL1, ADAMTSL2 and PAPLN**. A curator applying the term by
family membership would have taken all seven. The selection therefore reflects the
review's actual content, so this is a real traceable statement rather than a projection
artefact.

Weighed against that: no direct localisation of ADAMTSL3 to an elastic fibre or microfibril
has ever been published (§4, and the antibodies did not exist when the fibrillin work was
done). The honest position is `KEEP_AS_NON_CORE` — retain a specialist curator's traceable
statement, consistent with the fibrillin-1 binding, but do not treat it as an established
location. `REMOVE` would be overruling a curator on an inference I cannot check.

## 7. The 15 `GO:0005515` rows

All 15 IPI rows, over 13 distinct partners, come from **two CCSB systematic yeast
two-hybrid interactome maps**: PMID:25416956 (HI-II-14) and PMID:32296183 (HuRI).

Querying IntAct directly (`findInteractions/P82987`) reproduces the ACRV1 finding exactly:
the detection methods across ADAMTSL3's records are `two hybrid array` ×16,
`two hybrid prey pooling approach` ×16 and `validated two hybrid` ×16 — **three sub-methods
of the same Y2H pipeline**, not three independent assays. So UniProt's `NbExp=3` (and
`NbExp=6` for the two partners found in both screens) counts Y2H variants, not orthogonal
confirmation. MI-scores are 0.56, or 0.72 for the two that appear in both maps.

**Corrected after review — the aggregate does not answer the question.** The first version
of this analysis counted detection methods across ADAMTSL3's *whole* IntAct record and then
asserted that no orthogonal assay existed for these pairs. That was a non sequitur, and the
committed `results.json` refuted it at the aggregate level: the same counter records
`anti tag coip` ×15 and one BioID. Disaggregating **per pair** is what settles it, and it
does so in favour of the claim: **0 of the 13 GOA partners carries any non-Y2H detection
method**, while the `anti tag coip` and BioID methods belong entirely to the **17** IntAct
partners that are *not* in GOA (from PMID:40205054 and PMID:39232006, separate publications
that are not the source of any row reviewed here).

Writing that per-pair check exposed a second, quieter defect. IntAct returns partner
identifiers with a database suffix — `A8MQ03 (uniprotkb)`, not `A8MQ03` — so a lookup keyed
on the bare accession matches **nothing**, and "no non-Y2H method recorded" would have been
indistinguishable from "partner not found". The script now strips the suffix and raises if
any GOA partner is absent from the IntAct record, because a silent zero is exactly what this
check exists to rule out. Normalising the identifiers also merged a few duplicate labels, so
the degree numbers moved by one apiece: ADAMTSL3's own degree is **30** (was 31) and the
partner median is **188** (was 189). Small, but they were wrong, and the numbers quoted in
the review are the corrected ones.

Partner identity, all resolved to reviewed Swiss-Prot entries at canonical length (no
TrEMBL/ORFeome substitutions — the ACRV1 `Q86WV8` trap checked and negative):

- **9 keratin / keratin-associated proteins**: KRT40, KRTAP1-1, KRTAP2-3, KRTAP2-4,
  KRTAP3-2, KRTAP5-7, KRTAP10-6, KRTAP10-8, KRTAP12-3
- **CYSRT1**, a cornified-envelope protein that is itself a KRTAP-network hub
- **GLRX3** (cytosol), **MDFI** (nucleus/cytoplasm), **NOTCH2NLA**

Quantitatively: the median number of distinct IntAct partners across the 13 is **188**,
against **30** for ADAMTSL3 itself; six of them (CYSRT1 516, MDFI 483, KRT40 448,
KRTAP10-8 415, NOTCH2NLA 276, GLRX3 190) are extreme interactome hubs. Only KRTAP2-3 (10)
is not.

Compartment argument: ADAMTSL3 has a cleaved signal peptide and is a secreted matrix
protein. Hair-keratin-associated proteins are intracellular intermediate-filament matrix
proteins of the hair cortex; GLRX3 is cytosolic; MDFI is nuclear/cytoplasmic. In a Y2H
assay both partners are forced into the yeast nucleus, where the signal peptide is inert,
so the compartment mismatch is not tested by the assay that produced these rows. Nothing
in the ADAMTSL3 literature follows any of them up.

Verdict: `MARK_AS_OVER_ANNOTATED` on all 15, not `REMOVE`. These are real observations
recorded correctly by IntAct curators; what they do not license is a functional claim, and
bare `protein binding` conveys none anyway. Decided per partner (the brief's rule), and the
two that appear in *both* screens are not rescued by it: HI-II-14 and HuRI share the CCSB
ORFeome and search space, and both replicating partners (KRTAP10-8, MDFI) are among the
highest-degree hubs in the set.

Two newer screens are in IntAct but **not** in GOA and so are out of scope here: a
15-partner `anti tag coip` spoke-expanded set (PMID:40205054) and one BioID hit with CDH5
(PMID:39232006).

## 8. Neural biology — real, but mouse

Two strong mouse papers, both from the Tyagarajan group:

- [PMID:37572323 "Here, we identify that the secreted protein Adamtsl3 functions as critical hippocampal synapse organizer acting through the transmembrane receptor DCC (deleted in colorectal cancer)."] and [PMID:37572323 "We demonstrate that early post-natal deletion of Adamtsl3 in neurons impairs DCC protein expression, causing reduced density of both glutamatergic and GABAergic synapses."]
- [PMID:42277231 "Here, we identify the schizophrenia-associated glycoprotein Adamtsl3 as a PV+ cell-autonomous regulator of PNN integrity."] and [PMID:42277231 "Mechanistically, Adamtsl3 modulates matrix metalloprotease-9 (MMP9) activity, and Adamtsl3 deletion results in elevated MMP9 levels, PNN reduction, decreased Otx2 uptake, and heightened oxidative stress in PV+ cells."]

The perineuronal net is a specialised extracellular matrix, so the second paper is
independent corroboration that ADAMTSL3 is involved in extracellular matrix organisation —
cited in the `GO:0030198` row for that reason rather than as a new term.

Synapse organisation is proposed as a `NEW` row with **ISS**, not IMP: the conditional
knockouts are mouse. The orthology is well founded — the *C. elegans* orthologue is a
synaptic organiser too ([PMID:24896188] "C. elegans Punctin specifies cholinergic versus
GABAergic identity of postsynaptic domains") and MADD-4 signals through the DCC orthologue
UNC-40 ([PMID:22014523 "MADD-4's activity is dependent on UNC-40/DCC, a netrin receptor, which functions cell-autonomously to direct membrane extension."]), which is the same
receptor as in the mouse hippocampus. Human relevance is supported by ADAMTSL3 protein
being present in human cortical and ganglionic neurons (§1, PMID:17597111).

One caution worth writing down: MADD-4/Ce-Punctin is the orthologue of **both** ADAMTSL1
and ADAMTSL3 — [PMID:22014523 "The biological role of MADD-4 orthologs, including ADAMTSL1 and 3 in mammals, is unknown."] — so worm synaptic phenotypes cannot be assigned to
ADAMTSL3 alone. The mouse conditional knockouts can.

## 9. Human genetics — real signal, but not GO-annotatable

- Height: `ADAMTSL3` is one of the 20 loci in [PMID:18391952 "The genes implicate a number of biological pathways and processes in the normal determination of human height, including Hedgehog signaling (IHH, HHIP, PTCH1), basic cell cycle regulation (CDK6, one of the cyclin-dependent kinases implicated in cell cycle progression13), extracellular matrix (ADAMTSL3 and EFEMP1) and chromatin rearrangement and polycomb proteins (HMGA2 and SCMH1)."], and the locus recurs across lean-mass and body-composition GWAS.
- Schizophrenia: [PMID:21239144] — an imputation/resequencing follow-up that refines but
  does not resolve the association; its own conclusion is that ADAMTSL3 remains "a
  candidate for further investigation".
- Diabetes: [PMID:29162515] proposes A137T as a candidate susceptibility variant in one
  Japanese family.

A GWAS association is a statement about a locus, not about a gene product's activity, and
none of these identifies a molecular mechanism. None is used to support a GO term. They are
recorded because they are the reason this gene is studied and because they motivate the
suggested experiments.

## 10. Cancer and glaucoma claims — weaker than they read

- [PMID:32266537] is a **genome-wide CRISPR screen** in one HCC line; the ADAMTSL3 result is
  "sgRNAs targeting the ADAMTSL3 and PTEN genes appeared twice on the list", followed by
  [PMID:32266537 "Moreover, knocking out either the ADAMTSL3 or PTEN genes promoted either the proliferation or metastasis of HCC cells, respectively."]. Single line, single screen,
  no mechanism. Not annotated.
- [PMID:18474779] is cited by the affinage record as showing "an antiangiogenic role for
  ADAMTSL-3". It does not. The paper compares POAG with normal optic-nerve-head astrocytes
  and finds ADAMTSL-3 among the transcripts raised in POAG astrocytes
  ([PMID:18474779 "The ONH astrocytes from donors with POAG decreased expression of proangiogenic factors (vascular endothelial growth factor C and platelet-derived growth factor A) and increased expression of antiangiogenic factors (collagen XVIII and ADAMTSL-3) when compared with normal ONH astrocytes."]); the tube-formation assay compares
  whole astrocyte populations, with no ADAMTSL3 perturbation. Correlation, not function.
  Marked `MISCITED` in `reference_review`.

## 11. Provenance and quality of the affinage record

`gates_passed: False`. The tripped gate is a suspected symbol collision flagged because the
narrative opens on *C. elegans*. On inspection that gate is a **false positive**: the
narrative correctly identifies human ADAMTSL3/punctin-2 and is discussing the worm
orthologue Ce-Punctin/madd-4, which is a legitimate part of this gene's story. Every claim
used from the record was nonetheless re-verified against the cited PMIDs, per the rule.

Defects found in the record itself:

1. **Mis-joined citation.** It attributes "functions as a synaptic organizer specifying
   postsynaptic neurotransmitter receptor domain identity" to `[PMID:14667842, PMID:24896188]`.
   PMID:14667842 is the 2003 ECM cloning paper and contains no synaptic content whatever;
   PMID:24896188 is about the *worm* protein. The claim about the human protein is assembled
   across two sources neither of which makes it. Every constituent statement is individually
   defensible; the error is in the join.
2. **A `—` in the PMID column.** The 2025 CAR-T/TGF-β finding is sourced to bioRxiv with no
   PubMed id. It has since been published as PMID:42497245 (*Sci Immunol* 2026), but the
   claim is a germline variant-burden association in a trial cohort and supports no GO term.
3. **Over-reading of PMID:18474779** (§10).
4. **Misses the two most informative papers for this gene**: PMID:22242013 (the fibrillin-1 /
   ADAMTS-10 / LTBP-1 binding, §4) and PMID:36539599 (the TGF-β knockout and human-cell
   rescue, §5). Its "the biochemical mechanism ... has not been characterized in the
   available corpus" is a statement about *its* corpus, not about the literature.

Retraction / erratum check: all 16 PMIDs relied on were fetched from PubMed and inspected
for `RetractionIn`, `ErratumIn`, `ExpressionOfConcernIn` and `CorrectedandRepublishedIn` in
their own `CommentsCorrections` records. **All clean.** Recording the negative so the next
reviewer knows the check was run.

## 12. Checks run, including the ones that came back negative

| check | result |
|---|---|
| WITH/FROM resolution on the IBA row | 17 tokens; 16 protein donors + 1 PANTHER node; **all 16 resolved** |
| Donors' own experimental evidence for `GO:0031012` | **16/16** carry their own IDA/HDA to the term or a descendant — so "these sources only carry the same family-level inference" is false here |
| Self-referential WITH/FROM tokens | **0** |
| Donor heterogeneity | donors hold `GO:0001527` microfibril, `GO:0005604` basement membrane, `GO:0005614` interstitial matrix and `GO:0031012` — the general term is the genuine LCA, so no specificity upgrade is warranted (AADACL4 rule) |
| IBA less precise than its donors? (ACRV1 pattern) | **No.** The donors disagree about the specific compartment, so the parent is correct; no downward MODIFY |
| Partner accessions vs canonical entries | **13/13 reviewed Swiss-Prot at canonical length**; no ORFeome/TrEMBL substitution |
| IntAct method audit | one Y2H pipeline logged as three sub-methods, as on ACRV1 |
| Reference-scope / projection test on the TAS row | 62 entities, but selective within the family — **not** a blanket projection |
| Retraction and erratum scan | 16/16 clean |
| Paralog agreement | ADAMTSL4's merged review (`genes/human/ADAMTSL4`) reached `GO:0050840 extracellular matrix binding` as a `NEW` term for the same fibrillin-binding biology; this review uses the same term, so the two are consistent |

A third check, run because the campaign brief insists on it, caught something nothing else
would have. Reconciling the **raw** count of `reference_id:` occurrences in the review YAML
against the **parsed** count gave 32 versus 60. The tempting reading — "the 15 identical
two-hybrid rows must be collapsing somehow" — would have been a rationalisation. The real
cause: the fifteen `GO:0005515` rows shared one Python list object, so PyYAML emitted it
once as `supported_by: &id001` followed by fourteen `*id001` aliases. Valid YAML, parses
identically, and invisible to `checkquotes.py` and to the repo validator, both of which walk
the parsed document. It is the mirror image of the duplicate-key trap found on ACTMAP:
there, parsing *destroys* data the raw text contains; here, parsing *creates* data the raw
text does not show. Fixed by deep-copying per row and by dumping through a
`SafeDumper` subclass whose `ignore_aliases` returns `True`, with an assertion that no
`&id`/`*id` survives into the file. Final reconciliation is 60 = 60, with a strict
duplicate-key loader passing as well.

Two identifier traps hit and fixed while doing this, both of the "silent wrong answer"
kind:

- I first assumed mouse Adamtsl3 was `Q8BLD4`. **`Q8BLD4` is Tardbp.** The mouse orthologue
  is `G3UXC7`, and it is TrEMBL — there is no reviewed Swiss-Prot mouse Adamtsl3 entry.
- `WB:WBGene00003242` does not resolve through UniProt's `xref:wormbase-` index, which is
  keyed on transcript ids. Resolved through the GO consortium `wb.gaf` to **`mig-6`,
  papilin** (`O76840`, Swiss-Prot, GO:0005604 basement membrane IDA). It is **not** madd-4,
  which is `WBGene00009958` — an easy and tempting mis-identification on this gene, since
  madd-4 *is* the functional orthologue discussed in the neural literature. Then
  `gene:mig-6` in UniProt fuzzy-matched **mig-10**, so the script now asserts the returned
  entry carries the exact symbol.

## 12a. Three decisions taken under review, recorded so they are not re-litigated

1. **`GO:0002020 protease binding` added.** The 2 nM SPR interaction with ADAMTS-10 was
   described in the review but carried no term of its own. It does now, as `ISS` with the
   same reagent-species caveat as `GO:0050840`. Deliberately *not* an inhibitor term: the
   contact is with ADAMTS-10's non-catalytic Tsp1 region
   ([PMID:22242013 "The C-terminal recombinant ADAMTS-10 polypeptide used in the SPR studies represents the noncatalytic region of ADAMTS-10, a region composed primarily of Tsp1 repeats (Figure S3)."]),
   so nothing has been shown about its activity. The merged ADAMTSL4 review also carries
   `GO:0002020`, so the paralogues stay consistent.

2. **`P35555` removed from the `GO:0050840` WITH/FROM.** For `ISS` the field takes the
   sequence-similar entity — mouse `G3UXC7` — and the binding partner belongs there only on
   an `IPI` upgrade. Worth flagging as a general trap: `supporting_entities` is an
   unconstrained string list in the schema, so validation passes either way and this can
   only be caught by reading.

3. **The neuronal role is non-core, and the document now says so once.** An earlier draft
   listed it in `core_functions` while the annotation row called it non-core — and the
   `core_functions` entry justified its inclusion with *the same premise* ("the evidence is
   entirely non-human") that the row used to exclude it. The `core_functions` entry has been
   removed and the annotation row is the single statement of the position: the direct
   evidence is entirely mouse and worm, and the molecular activity behind the DCC effect is
   unknown and recorded as an `MF_DARK` gap. The biology is still fully present in the gene
   description, in the annotation row, and in §8 above; its matrix component is carried by
   `GO:0030198` in core function 1. Note the deletion alone would not have been enough — the
   contradiction lived in two passages, and both were touched.

## 13. For whoever reviews ADAMTSL1

Derived independently here, offered as claims to check rather than facts to inherit:

- Human **ADAMTSL1 (Q8N6G6) receives no PAINT annotation at all** — zero rows in the leaf
  PAINT GAF — although mouse Adamtsl1 (Q8BLI0) receives `GO:0031012`. Its only GO annotation
  is the same InterPro `GO:0030198` IEA. Worth confirming from the primary GAF rather than
  from this note.
- ADAMTSL1 and ADAMTSL3 are **co-orthologues of the same worm gene** madd-4/Ce-Punctin
  (PMID:22014523), so worm synaptic data are shared between them and cannot be assigned to
  either alone.
- In the fibrillin-1 SPR panel, **ADAMTSL-1 was the negative**: [PMID:22242013 "Similar to ADAMTSL-6 [24], ADAMTSL-2, -3, and papilin polypeptides interacted with the N-terminal half of fibrillin-1, while ADAMTSL-1 did not."] and it also failed to bind ADAMTS-10. So
  the microfibril-adaptor story that carries ADAMTSL3 should *not* be transferred to
  ADAMTSL1 — the same experiment tested it and it was negative. That negative is the single
  most useful thing in this note for that review.
- The `NOT GO:0004222` node recommendation in §3 covers ADAMTSL1 too; it should be stated
  once, for the whole clade, not repeated per gene.
