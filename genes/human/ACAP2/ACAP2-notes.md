# ACAP2 (Q15057) — review notes

Journal for the PAINT + affinage review of human ACAP2 / centaurin-β2 / CENTB2 / KIAA0041.

## 1. What the protein is

778 aa, five-module architecture, all confirmed in the UniProt feature table
[file:human/ACAP2/ACAP2-uniprot.txt "FT   DOMAIN          399..520"]:

| residues | module | role |
|---|---|---|
| 1–226 | BAR | dimerisation / membrane curvature (inferred from family, not assayed for ACAP2) |
| 266–361 | PH | phosphoinositide sensing (inferred) |
| 399–520 | Arf-GAP | catalysis; C4-type Zn finger 414–437; catalytic Arg442 |
| 640–669, 673–702, 706–735 | ANK 1–3 | RAB35 binding (structurally established, PDB 6IF3) |

`PE 1: Evidence at protein level` — the protein is detected, so nothing here should be
described as "no experimental data"; there is in fact good biochemistry.

## 2. The two established activities

**(a) ARF6-preferring GTPase-activating protein.** The founding paper identified ACAP1 and
ACAP2 as Arf6 GAPs
[PMID:11062263 "Here, we report the identification and characterization of two Arf6 GAPs, ACAP1 and ACAP2."]
with genuine substrate preference
[PMID:11062263 "In vitro, ACAP1 and ACAP2 preferred Arf6 as a substrate, rather than Arf1 and Arf5, more so than did ASAP1."].
Catalysis needs the conserved arginine
[PMID:11062263 "[R448Q]ACAP1 and [R442Q]ACAP2 had no detectable activity using Arf6 as a substrate"]
and the activity is lipid-gated
[PMID:11062263 "ACAP1 and ACAP2 showed similar phospholipid dependencies when Arf6 was used as a substrate."],
which UniProt records as
[file:human/ACAP2/ACAP2-uniprot.txt "CC   -!- ACTIVITY REGULATION: GAP activity stimulated by phosphatidylinositol"].
Specificity is real in the negative direction too: ACAP2 is *not* a GAP for the Rab it binds
[file:human/ACAP2/ACAP2-uniprot.txt "CC       (ARF6). Doesn't show GAP activity for RAB35 (PubMed:30905672)."].
Compartment specificity: the effect is peripheral, not Golgi
[PMID:11062263 "Neither ACAP1, ACAP2, nor ASAP1 (Brown et al. 1998) caused changes in the morphology of the Golgi apparatus"].

**(b) RAB35 effector.** ACAP2 binds GTP-loaded RAB35 through its terminal ankyrin repeat
[PMID:30905672 "In the Rab35/ACAP2 complex structure, Rab35 binds to the terminal ankyrin repeat and a C-terminal extended"],
which UniProt localises to the ANK repeats
[file:human/ACAP2/ACAP2-uniprot.txt "CC   -!- DOMAIN: The ANK domains are required for interaction with RAB35."]
— note UniProt's SUBUNIT line writes "KANK domains", which looks like a typo for ANK; the
DOMAIN line and the crystal structure both say ankyrin repeats. The specificity is extreme
[PMID:25694427 "Centaurin-β2 is the only Rab35-binding protein reported thus far that exclusively recognizes Rab35 and does not recognize any of the other 59 Rabs identified in mammals"].

The two modules compose into one mechanism: RAB35 recruits ACAP2, which then switches ARF6 off
[PMID:24600047 "We show that Rab35 and its effector, ACAP2, a GTPase-activating protein that switches off Arf6 activity, negatively regulate oligodendrocyte morphological differentiation."].

Caution on residue numbering: PMID:25694427 names Asn-610/Asn-691 in the minimal RAB35-binding
site, while PMID:30905672's human mutagenesis is at Asp-721/Arg-727/Met-731/Asp-756. The two
papers are not on the same numbering, so the 610/691 pair must not be quoted as human positions.
The affinage record does exactly that, which is why it was not used as the source for any
residue-level claim here.

## 3. Cellular readouts

- Overexpression suppresses PDGF-induced dorsal ruffles [PMID:11062263 "Overexpression of either ACAP inhibited the formation of PDGF-induced dorsal ruffles"],
  yet the protein still goes to the ruffles that form [PMID:11062263 "The mutant ACAPs, like mutant ASAP1, were efficiently recruited to the actin-rich ruffles"].
- In human HeLa cells [PMID:11062263 "we used HeLa cells to test for an effect of the ACAPs on Arf6 function in vivo"]
  ACAP2 blocks ARF6-driven protrusions [PMID:11062263 "Coexpression of Arf6 with either ACAP inhibited the formation of protrusions in response to AlF4 treatment"]
  by half [PMID:11062263 "ACAP2 reduced the number of cells generating protrusions by 50%."], GAP-dependently
  [PMID:11062263 "The effects of ACAP1 and ACAP2 were dependent on GAP activity."].
  These are overexpression/point-mutant experiments, i.e. IMP-grade, not IDA-grade, evidence for the process.
- Steady state it is largely soluble but visits ARF6 tubules
  [PMID:11062263 "In untreated cells, although ACAP1 and ACAP2 were primarily cytosolic, they could be observed on tubular portions of the Arf6 endosomal compartment"],
  and those tubules are the recycling route
  [PMID:11062263 "In addition, ACAP1 and ACAP2 were recruited to peripheral, tubular membranes, where activation of Arf6 occurs to allow membrane recycling back to the plasma membrane."].
- Non-human deployments of the same axis: NGF-triggered neurite outgrowth in rat PC12
  [PMID:22344257 "We found that Rab35 accumulates at Arf6-positive endosomes in response to nerve growth factor (NGF) stimulation and that centaurin-β2 is recruited to the same compartment in a Rab35-dependent manner."],
  FcγR phagocytosis in macrophages [PMID:22045739 "Furthermore, GTP-Rab35-dependent recruitment of ACAP2, an ARF6 GTPase-activating protein, was shown in the phagocytic cup formation."],
  and oligodendrocyte differentiation [PMID:24600047 "We show that Rab35 and its effector, ACAP2, a GTPase-activating protein that switches off Arf6 activity, negatively regulate oligodendrocyte morphological differentiation."].
- One human loss-of-function phenotype outside membrane traffic
  [PMID:25853217 "We show that knockdown of ACAP2 blocks apoptosis in cancer cells in response to the chemotherapeutic antimetabolite 5-fluorouracil"],
  in a paper that also reports direct lipid binding
  [PMID:25853217 "We report here that ACAP2, a homolog of C. elegans CNT-1, has a pro-apoptotic function and an identical phosphoinositide-binding pattern to that of tCNT-1, despite not being an apparent target of caspase cleavage."].
  Abstract-only in the cache, so the lipid species and the assay cannot be read off; unreplicated.

## 4. WITH/FROM resolution (the highest-yield step)

Every accession in column 11 of `ACAP2-goa.tsv`, resolved:

| id | identity | verdict |
|---|---|---|
| UniProtKB:Q5FVC7 | **Acap2**, *Rattus norvegicus* | true ortholog — ISS transfers legitimate |
| UniProtKB:Q6ZQK5 | **Acap2**, *Mus musculus* | true ortholog — Compara projection legitimate |
| UniProtKB:Q15286 | **RAB35**, human | real, direct, crystallised partner |
| UniProtKB:Q96P50 | **ACAP3**, human | **paralog** — but this is an IPI physical interaction, not a transfer |
| RGD:1562939 | rat Acap2 (= Q5FVC7) | ortholog |
| WB:WBGene00000565 | *C. elegans* **cnt-1** | ortholog-grade family member |
| MGI:MGI:2153589 | mouse **Acap3** | **paralog**, not the mouse Acap2 ortholog |
| SGD:S000002932 | *S. cerevisiae* **AGE1** (ArfGAP effector protein 1) | distant ArfGAP |
| PomBase:SPBC17G9.08c | *S. pombe* **csx2** | distant |
| AGI_LocusCode:AT5G13300 | *Arabidopsis* **AGD3/VAN3/SFC** ArfGAP | distant |
| AGI_LocusCode:AT5G61980 | *Arabidopsis* **AGD1** ArfGAP | distant |
| dictyBase:DDB_G0279649 | Q54WI0, BAR+PH+Arf-GAP+ANK, PTHR23180:SF160 | genuine ACAP-like |
| dictyBase:DDB_G0276395 | Q551Q8, PH+Arf-GAP, PTHR23180:SF414 | genuine ACAP-like |
| FB:FBgn0004133 | *Drosophila* **blow** (blown fuse) | **PH domain only — no BAR, no Arf-GAP, no ANK** |
| InterPro:IPR001164 / IPR045258 | ArfGAP domain / ACAP1-2-3-like | correct signatures |
| UniProtKB:Q15057 | ACAP2 itself | self-reference: PAN-GO curator marking the function core |

All of this is now reproducible: `ACAP2-bioinformatics/resolve_withfrom.py` regenerates the
table from primary APIs and writes `RESULTS.md`. It was added in response to PR review,
which correctly pointed out that the `blow` and `MGI:MGI:2153589` claims were load-bearing
but had nothing behind them in-repo.

### Does each source hold its own evidence for what it donates?

An IBA/ISS WITH/FROM list is supposed to name experimentally annotated family members, so it
is worth asking rather than assuming. Querying QuickGO for each source's own annotations to
the donated term (descendants included):

| source | donated term | source's own evidence |
|---|---|---|
| rat Acap2 Q5FVC7 | GO:0010008 / GO:0032456 / GO:1990090 | IDA / IMP / IDA |
| mouse Acap2 Q6ZQK5 | GO:0031267 | IPI |
| mouse Acap3 Q6NXL5 | GO:0005096 | IMP |
| worm cnt-1 Q9XXH8 | GO:0005886 / GO:0010008 | IDA x3 + EXP x2 / IDA x2 |
| yeast AGE1 Q04412 | GO:0005096 | IDA |
| Arabidopsis AGD3 Q5W7F2 | GO:0005096 | IDA |
| Arabidopsis AGD1 Q9FIT8 | GO:0005886 | IDA |
| pombe csx2 Q9UUE2 | GO:0005886 | IDA |
| Dicty Q54WI0 | GO:0005096 / GO:0005886 / GO:0030036 | IDA / IDA / IMP + IGI |
| Dicty Q551Q8 | GO:0030036 | IGI |
| fly blow A1Z714 | GO:0030036 | IMP |

Every single source carries wet-lab evidence for the term it donates. So none of these
transfers is an inference recycling another inference, and no verdict here should say
otherwise. That sharpens the `blow` objection rather than softening it: blow's actin
annotation is a real experimental result, and the problem is purely that a protein with no
ArfGAP domain cannot be producing that phenotype the way ACAP2 would. It also softens the
mouse-Acap3 note — the paralog is a competent donor for GAP activity (its own IMP), so the
only observation is that the ortholog is absent from that support set.

Two things fall out of this table.

**(i) `blow` is a family-boundary artifact.** PANTHER places blow in PTHR23180 (CENTAURIN/ARF)
as subfamily SF399, and blow carries experimental `GO:0030036 actin cytoskeleton organization`
from myoblast fusion. But A1Z714/P91678 has *one* annotated domain, a PH domain at 204–307 —
no BAR, no ArfGAP catalytic domain, no ankyrin repeats, and UniProt records no PANTHER
cross-reference for it at all. Whatever blow does to actin during myoblast fusion, it cannot be
doing it as an ARF GAP. Its inclusion among the four supporting entities of ACAP2's
`GO:0030036` IBA is therefore not real support.

**(ii) PTN001142372 is pan-eukaryotic.** All four IBA rows come from this single node. Querying
QuickGO for annotations carrying `PANTHER:PTN001142372` returns the identical four-term set
(GO:0005096, GO:0005886, GO:0010008, GO:0030036) on *Brassica napus*, *Cucumis sativus*,
*Medicago truncatula*, *Theobroma cacao*, *Zostera marina* and *Mimulus guttatus* genes, on
yeast AGE1, and on *Xenopus* acap2.L. So the node ancestral to these annotations predates the
plant/fungal/animal split; it is not the ACAP1/2/3 node. GAP activity survives that depth
(everything under it except blow has an ArfGAP domain). A specific process term does not.

## 5. The ontology problem

The best-characterised fact about ACAP2 — that it is an **ARF6**-preferring GAP — cannot be
expressed in current GO. `GO:0008060 ARF GTPase activator activity` has been merged into
`GO:0005096 GTPase activator activity`, together with GO:0005097 (Rab GAP), GO:0005098 (Ran
GAP), GO:0005099 (Ras GAP), GO:0005100 (Rho GAP), GO:0005101, GO:0017123, GO:0030675 and
GO:0046582 — all nine appear as `secondaryIds` of GO:0005096, which now has no substrate-specific
children (its only child is GO:1902773 GTPase activator complex).

The same has happened on the binding side: `GO:0017137 Rab GTPase binding` is now a secondary id
of `GO:0031267 small GTPase binding`, which has no children at all.

So GOA's `GO:0005096` and `GO:0031267` rows for ACAP2 are already maximally specific. The
ARF6-versus-ARF1/ARF5 preference, and the exclusive recognition of RAB35 among 60 mammalian
Rabs, are recoverable only through `has_input` annotation extensions or a GO-CAM — not through
term choice. This is a deliberate GO design decision, so the right recommendation is extensions,
not resurrecting the obsoleted terms.

By contrast the **process** side has a real, unused, non-obsolete term:
`GO:0032013 negative regulation of ARF protein signal transduction`. GOA gives ACAP2 four BP
annotations (actin cytoskeleton organization IBA, actin filament-based process IDA, endocytic
recycling ISS, cellular response to NGF ISS) and none of them says that ACAP2 turns ARF6 off,
which is the whole of its characterised biology. That is the main gap this review closes.

## 5b. A curation asymmetry with ACAP1

PMID:11062263 characterised ACAP1 and ACAP2 together, in the same figures, and ACAP1 was the
more potent of the two in the protrusion assay
[PMID:11062263 "As shown in Fig. 9, ACAP1 was most effective at inhibiting protrusions."].
Yet QuickGO returns three annotations from that reference for ACAP2 (GO:0005096, GO:0030029,
GO:0001726, all IDA) and **zero** for ACAP1 (UniProtKB:Q15027) — verified directly:

```
.../annotation/search?geneProductId=UniProtKB:Q15027&reference=PMID:11062263  -> numberOfHits 0
.../annotation/search?geneProductId=UniProtKB:Q15057&reference=PMID:11062263  -> numberOfHits 3
```

So the asymmetry is a curation artifact, not biology. Two consequences for this review: ACAP2's
IDAs from this paper are not over-calls (they are the recorded half of a symmetric experiment),
and ACAP1 is under-annotated from the same source. Cross-checked against the parallel ACAP1
review (PR #2251), which reached the same conclusion independently.

## 6. Interactome triage

IntAct has 33 records for Q15057. Almost all are single-shot high-throughput: a PI(3)P affinity
proteomics screen that pulled 681 proteins [PMID:23416715], socioaffinity inferences, and
one-off tag co-IPs (MAPT, DOK2, ELK4, RASA1, RAB5A, RAB8A, CAPZB, MED4, Tgs1, Naa10, PDK3,
HSPB1). Two entries are worth separating out:

- **ACAP3 (Q96P50)** is recovered by two orthogonal proteome-scale datasets — BioPlex 3.0
  [PMID:33961781] and OpenCell [PMID:35271311] — and UniProt promotes it to an INTERACTION line
  with NbExp=4. The pair is probably real, and hetero-oligomerisation through the shared
  N-terminal BAR domain would be the obvious mechanism, but nothing has been tested; AP-MS
  cannot license a dimerisation MF. Both GOA rows stay as uninformative `protein binding`.
- **Vaccinia K1L** binds ACAP2 [PMID:16806385], but the paper's point is that the host-range
  function of K1L is *separable* from ACAP2 binding, so it says nothing about ACAP2's own function.

Not in GOA and not used: RNF126-driven degradation of ACAP2 in ovarian cancer [PMID:40251363] —
a single 2026 paper, ACAP2 as substrate rather than agent.

## 7. Decisions taken

- `GO:0005096` (IBA, IEA, IDA) — ACCEPT ×3. Maximally specific term available; substrate
  specificity noted for extension/GO-CAM capture.
- `GO:0031267` (IEA from mouse ortholog) — ACCEPT. `GO:0005515` with RAB35 — MODIFY to
  GO:0031267 + GO:0030742 (GTP-dependent protein binding), since ACAP2 recognises only the
  GTP form.
- `GO:0005515` with ACAP3 ×2 — MARK_AS_OVER_ANNOTATED. Real but functionally silent.
- `GO:0030029` (IDA) and `GO:0030036` (IBA) — MODIFY both to `GO:0032956 regulation of actin
  cytoskeleton organization`. ACAP2 is upstream signalling, not cytoskeletal machinery; and the
  IBA's supporting set is the pan-eukaryotic node plus blow.
- `GO:0016020` (HDA) — MARK_AS_OVER_ANNOTATED. Bulk NK-cell membrane fraction; the study's own
  method removed peripheral membrane proteins and it concedes ~40% plausible membrane proteins,
  while ACAP2 is peripheral. Subsumed by the specific membrane terms anyway.
- `GO:0005737` (IEA from the BAR signature) — KEEP_AS_NON_CORE. True (largely cytosolic at
  steady state) but uninformative, and BAR→cytoplasm is a poor inference for a curvature-binding
  module.
- NEW: `GO:0032013` (IMP, PMID:11062263) and `GO:0035091 phosphatidylinositol binding`
  (IDA, PMID:25853217).
- Not proposed: `GO:0043065 positive regulation of apoptotic process`. Only PMID:25853217
  supports it, abstract-only, unreplicated, and the paper itself notes ACAP2 is not caspase-cleaved
  so the CNT-1 mechanism does not transfer. Filed as a knowledge gap and an experiment instead.
- Not proposed: phagocytosis. PMID:22045739 says only "in macrophages" and the cache is
  abstract-only, so the species is not stated and an ISS cannot be justified from it.
