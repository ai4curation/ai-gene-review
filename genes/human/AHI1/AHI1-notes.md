# AHI1 (Jouberin, Q8N157) — curation notes

Human AHI1 review, PAINT + affinage campaign. 37 GOA rows, 37 `existing_annotations`
entries (reconciled below).

## Row-count reconciliation

```
wc -l genes/human/AHI1/AHI1-goa.tsv   -> 38 lines = 1 header + 37 data rows
grep -c '^- term:' AHI1-ai-review.yaml (stub) -> 37
QuickGO geneProductId=UniProtKB:Q8N157         -> numberOfHits 37
```

The `fetch-gene` stub did **not** under-seed this gene: all five `GO:0005515` rows are
present one-per-partner (PMID:18633336/NPHP1, PMID:22623184/DNM2, PMID:23532844/NPHP1,
PMID:23532844/HAP1, PMID:25825872/ADAM12), and the three `GO:0005829` Reactome rows and
the duplicate-term pairs (`GO:0005814` ×2, `GO:0005912` ×2, `GO:0005813` ×2,
`GO:0005929` ×3, `GO:0036038` ×2, `GO:0036064` ×2, `GO:0060271` ×2) all kept their own
entries. Final file has 37 reviewed rows plus NEW proposals appended.

## The headline finding: experimental evidence codes on non-human experiments

The task brief flagged this shape from AHNAK (a `NEW` row carrying `IMP` for a mouse
knockout). On AHI1 it is not in a proposed row — **it is in the shipped GOA**.

### `GO:0060271 cilium assembly`, IMP, PMID:21959375, assigned by UniProt

`publications/PMID_21959375.md` has `full_text_available: true`. Its Methods name every
experimental system, and **none of them is human**:

- zebrafish morpholino knockdown — [PMID:21959375 "Splice (5′-CCACACTCTGAAAGGGAAAAACATT-3′) and translation (5′-GAGTCATTAGCAGCTTTGTTTTTCC-3′) blocking antisense morpholino oligonucleotides (MOs) were designed (Gene Tools, Philomath, Oregon, USA) to target zebrafish ahi1"]
- mouse renal epithelial cells — [PMID:21959375 "Mouse inner medullary collecting duct (IMCD3) cells were cultured in DMEM/Ham’s F12 supplemented with 10% fetal calf serum (Sigma-Aldrich, UK)."]
- siRNA directed at the **mouse** gene — [PMID:21959375 "of each of four siRNA duplexes (OnTargetPlus SMARTpool, Dharmacon) against mouse Ahi1"]
  (the full sentence contains a non-breaking space in "100 pmol", so the quotable
  fragment starts after it)

The internal inconsistency that makes this a curation defect rather than a judgement
call: **the same curator, from the same paper, restricted the other IMP to mouse.**
QuickGO by reference:

```
reference=PMID:21959375  total_annotations=9  distinct entities=4
  GO:0007368  entities=2  {('IMP','ZFIN'): 2}
  GO:0044458  entities=2  {('IMP','ZFIN'): 2}
  GO:0060271  entities=2  {('IMP','UniProt'): 2}   -> Q8K3E5 (mouse) AND Q8N157 (human)
  GO:0005929  entities=2  {('IC','UniProt'): 2}    -> Q8K3E5 AND Q8N157
  GO:0034329  entities=1  {('IMP','UniProt'): 1}   -> Q8K3E5 (mouse) ONLY
```

`GO:0034329 cell junction assembly` — from the E-cadherin result in the *same* IMCD3
experiment — went to mouse Ahi1 alone. `GO:0060271` went to mouse *and* human. Both come
from one siRNA pool against mouse Ahi1.

The **term is right** for human AHI1; it is the evidence code/reference pairing that is
wrong. Independent *human* support exists in a different paper: JBTS patient dermal
fibroblasts, [PMID:23532844 "Fibroblasts from individuals with JBTS showed an ∼50% decrease in primary cilia formation ( p < 0.005; Fig. 1 , A and B )."] with the genotypes given in
Methods. So the row should be ACCEPTed on the term and the defect reported: either
recode to `ISS`/`ISO` with `UniProtKB:Q8K3E5` as the source, or re-reference to
PMID:23532844 where the assay was human.

`GO:0005929 cilium` IC PMID:21959375 (with-from `GO:0060271`) inherits the same problem
by construction — an IC is only as species-correct as the annotation it is inferred from.

### `PMID:18633336` — five human IDA rows, mouse and canine cells

`full_text_available: false`, so this rests on what the abstract states **explicitly**
(the exception CLAUDE.md names). The abstract assigns a cell system to each localisation:

- [PMID:18633336 "Jouberin is expressed at cell-cell junctions, primary cilia and basal"] /
  [PMID:18633336 "body of mIMCD3 cells while a Jouberin-GFP construct localized to centrosomes in"] —
  mIMCD3 is **mouse**. Supplies `GO:0005911`, `GO:0005912`, `GO:0005929`, `GO:0036064`.
- [PMID:18633336 "subconfluent and dividing MDCK cells. Our results suggest that Jouberin is a"] —
  MDCK is **canine**, and the protein is an overexpressed GFP fusion. Supplies `GO:0005813`.
- [PMID:18633336 "was confirmed by exogenous and endogenous co-immunoprecipitation in HEK293"] —
  HEK293 is **human**, and the co-IP was *endogenous*. This one row is strong human evidence.

I did **not** REMOVE any of these. Four of the five localisations have independent
human-cell support (below), and for the GFP/MDCK centrosome row the abstract does not
say whether the construct was human or canine AHI1 — unresolvable without the full text,
so the caveat is recorded rather than acted on.

Independent human support for the same locations:
- `GO:0005813 centrosome` — HPA immunofluorescence (`GO_REF:0000052`), done in human cell
  lines. The HPA API returns `Subcellular main location: ['Centrosome']`,
  `Subcellular additional location: ['Primary cilium']`. This, not the MDCK experiment,
  is the human evidence for centrosome.
- `GO:0036064 ciliary basal body` — human AHI1 constructs (V443D and R351L are human
  numbering) localise to the basal body in [PMID:23532844 "These results showed that ∼80% of the cells expressing the wild type AHI1 (AHI1-WT) protein had AHI1 at the basal body of the primary cilium"].
- `GO:0005911`/`GO:0005912` junctions — same paper, human constructs:
  [PMID:23532844 "whereas more than 60% of the cells expressing AHI1-WT had AHI1 localized to the cell junctions of IMCD3 cells"].

## Complex-to-subunit projection: PMID:22179047 / ComplexPortal

The brief's ACTR8 check, run by reference rather than by gene, and it separates cleanly
into a sound half and a projected half:

```
reference=PMID:22179047  total_annotations=211 (fully paginated)  distinct entities=36
  GO:0036038 MKS complex                     entities=24  IDA:18 (UniProt 8 + MGI 10), NAS:14, TAS:1
  GO:0035869 ciliary transition zone          entities=19  NAS:15, IDA:5
  GO:1904491 protein localization to ciliary TZ  entities=15  NAS:15 — ZERO experimental
```

`GO:1904491` is a **biological process** term held by 15 entities, every one of them NAS
from ComplexPortal, and the 15 are exactly `ComplexPortal:CPX-2531` plus its 14 subunits
(confirmed against the ComplexPortal record: CPX-2531 "MKS transition zone complex",
systematic name `AHI1:B9D1:B9D2:CC2D2A MKS1:TCTN1:TCTN2:TCTN3:TMEM17:TMEM67:TMEM107:TMEM216:TMEM231:TMEM237`).
That is the complex's property distributed to every member, which is ComplexPortal's
documented convention — not 15 independent findings.

The discriminator the brief asks for (does the *phenotype* spread, or stay on the
perturbed gene?) answers cleanly here: the **membership** term `GO:0036038` carries 18
IDA annotations including mouse Ahi1's own (`Q8K3E5`, `GO:0036038` IDA PMID:22179047,
assigned by both UniProt and MGI), so complex membership was measured. The **process**
term `GO:1904491` carries none anywhere. Chih et al.'s own knockouts were of *B9d1* and
*Tmem231*, not *Ahi1* — [PMID:22179047 "Mouse knockouts of B9D1"] …
[PMID:22179047 "and TMEM231 have identical defects in Sonic hedgehog (Shh) signalling and"]

So: `GO:0036038` and `GO:0035869` kept; `GO:1904491` marked over-annotated with a
`propagation_review`.

## Reactome `cytosol` ×3 is a compartment label on a basal-body complex

Three separate `GO:0005829 cytosol` TAS rows, from R-HSA-5617816, R-HSA-5626681 and
R-HSA-5638009. Querying the Reactome ContentService participants endpoint for Q8N157:

```
R-HSA-5617816: AHI1 sits inside participant "basal body:transition zone proteins:RAB3IP:RAB11A:GTP:Golgi-derived vesicle [cytosol]"
R-HSA-5626681: AHI1 sits inside "Tectonic-like complex [cytosol]" and "basal body:transition zone proteins [cytosol]"
R-HSA-5638009: AHI1 sits inside "basal body:transition zone proteins [cytosol]" and the same larger assembly
```

In every case AHI1 is a *member of a basal-body/transition-zone complex entity*, and
`[cytosol]` is the compartment Reactome assigns to that whole entity — Reactome's model
has no ciliary-transition-zone compartment, so the basal body itself is labelled
`[cytosol]`. The annotation therefore records Reactome's compartment shorthand, not an
observation that AHI1 is in the soluble cytosol.

Scale of the projection, QuickGO by reference:

```
reference=Reactome:R-HSA-5626681  total_annotations=91  distinct entities=91
  GO:0005829  entities=87  {('TAS','Reactome'): 87}
```

87 entities receive `cytosol` from this single reaction. All three rows → non-core, with
the mechanism stated once.

A cytoplasmic pool of AHI1 does exist independently (UniProt: `Cytoplasm, cytoskeleton,
cilium basal body`; the Jouberin–β-catenin shuttling work below requires a
non-ciliary pool), so the term is not false — it is uninformative and triply redundant.

## `GO:0044458 motile cilium assembly` IBA — one zebrafish morphant

WITH/FROM: `PANTHER:PTN002893387|ZFIN:ZDB-GENE-060803-1`. Resolving both:

- `ZFIN:ZDB-GENE-060803-1` → zebrafish `ahi1`. UniProt `xref:zfin-ZDB-GENE-060803-1`
  returns **two TrEMBL hits and no Swiss-Prot entry**: `F1QX08` "Jouberin" and
  `A0AC58HN91` "Jouberin isoform X1" (both unreviewed — reported, per the rule that an
  unreviewed source is weaker support and hiding it is silent degradation).
- Its own evidence for the term (QuickGO on `UniProtKB:F1QX08`):
  `GO:0044458 IMP PMID:21959375 (ZFIN)` — a single annotation, from the morpholino work,
  where the cilia lost were **Kupffer's vesicle** cilia, which are motile.
- `PANTHER:PTN002893387` is a tree node, not a protein.

So the sole non-self donor is a morphant phenotype in a transient embryonic motile-cilium
organ. Human AHI1's entire experimental record is the **primary, non-motile** cilium, and
UniProt says so: [file:human/AHI1/AHI1-uniprot.txt "ciliogenesis, formation of primary non-motile cilium, and recruitment"].
Human AHI1 already carries `GO:0060271 cilium assembly`, the parent that covers both, and
separately carries `GO:0097730 non-motile cilium`. `GO:0044458` is a specificity claim in
the wrong direction → MARK_AS_OVER_ANNOTATED.

Note this is *not* a paralog problem — see the family check below.

## `GO:0036064 ciliary basal body` IBA is self-referential and sound

WITH/FROM: `MGI:MGI:87971|PANTHER:PTN002893387|UniProtKB:Q8N157`.

- `MGI:87971` resolves via `xref:mgi-87971` (bare number; the inner colon in the GOA token
  `MGI:MGI:87971` returns HTTP 400) to **`Q8K3E5` AHI1_MOUSE, Swiss-Prot, 1047 aa** — the
  true 1:1 orthologue, plus four unreviewed hits for the same gene.
- Mouse Ahi1's own evidence for the term: `GO:0036064` IDA from PMID:19625297 (×2,
  UniProt + MGI), PMID:19718039 (×2) and PMID:20081859 — **five IDA annotations across
  three independent papers**.
- `UniProtKB:Q8N157` is the target itself: a self-referential IBA recording a PAINT
  curator's judgement that the function is core → `root_cause: NO_FAILURE_CORE`, never
  CIRCULAR.

## PANTHER family: strictly 1:1 orthologues, so no paralog hazard

`PTHR44499` "Primary Cilium-Associated Jouberin", single subfamily `PTHR44499:SF1`.
`interpro/panther/PTHR44499/PTHR44499-entries.csv` has **3 rows** — human `Q8N157`,
mouse `Q8K3E5`, rat `Q6DTM3` — all three named Jouberin/Ahi1.

Scope caveat (the ACTA1 lesson): that CSV is built from InterPro's **reviewed-only**
protein endpoint, so 3 is the Swiss-Prot subset, not the family. The cached metadata
gives the family total as `proteins: 1838` across `taxa: 3670`; 3/1838 = 0.16%.

What survives the caveat: AHI1 has **no human paralogue** — there is no second human gene
in PTHR44499 — so none of this campaign's paralog-transfer failure modes
(`WRONG_ORTHOLOG_OR_PARALOG`, the ACTL8 mis-placed-member defect, the ACAP2 `blow` case)
can apply to any AHI1 row. Every donor resolved here is an orthologue. **Negative result,
recorded because it was checked.**

Also noted, not used: the InterPro family description carries `is_llm: true`,
`is_reviewed_llm: false`. It is not cited as evidence anywhere in this review.

## `NbExp` counts sub-methods, not experiments — third instance in this campaign

UniProt's INTERACTION block lists `NPHP1; NbExp=4` and `HAP1; NbExp=3`. Expanding the
IntAct records for Q8N157 (`/intact/ws/interaction/findInteractions/Q8N157`, 68 records,
fully paginated):

| partner | records | detection methods | distinct publications |
|---|---|---|---|
| O15259 NPHP1 | 4 | anti tag coip, molecular sieving | 1 (EBI-9660942) |
| P54257 HAP1 | 3 | 2 hybrid, anti tag coip, molecular sieving | 1 (EBI-9660942) |
| Q8N157 AHI1 (self) | 2 | anti tag coip, molecular sieving | 1 (EBI-9660942) |
| P50570 DNM2 | 2 | anti bait coip, anti tag coip | 1 (EBI-6248843) |
| O43184 ADAM12 | 2 | peptide array, phage display | 1 (EBI-21225559) |

`NbExp=3` for HAP1 is **one study logged under three method terms**. This does not weaken
NPHP1 or HAP1 — both were additionally measured by gel filtration with defined
stoichiometry — but it means the count is not a replication count.

The same query also shows a BioID dataset (EBI-11176939) placing AHI1 in proximity to
OFD1, PCM1, IQCB1, SSX2IP, ECD and others — a coherent centriolar-satellite/basal-body
neighbourhood, consistent with the localisation rows. Those are `proximity` records
(miscore 0.27) and are not in GOA; I did not import them.

## Partner accessions all resolve to reviewed canonical entries

The ACRV1 check (a named partner is not a verified partner), run and negative:

| accession | entry | reviewed | length |
|---|---|---|---|
| O15259 | NPHP1_HUMAN | reviewed | 732 |
| P54257 | HAP1_HUMAN | reviewed | 671 |
| P50570 | DYN2_HUMAN | reviewed | 870 |
| O43184 | ADA12_HUMAN | reviewed | 909 |
| Q8K3E5 | AHI1_MOUSE | reviewed | 1047 |

No TrEMBL substitutions, no partial ORFeome clones, no length mismatches against the
canonical entries. **Negative result, recorded.**

## Retraction / erratum sweep: clean

21 PMIDs checked against `CommentsCorrections/RefType` on each cited article's own PubMed
record (the only way a Publisher Correction is discoverable) plus PublicationType:
22179047, 18633336, 21959375, 22623184, 23532844, 25825872, 21623382, 21602792, 19718039,
20956301, 18936234, 35821088, 19625297, 20592197, 20081859, 31391239, 25103236, 28442542,
25616960, 18636121, 33741721. **All clean** — no retraction, erratum, expression of
concern, or corrected-and-republished link on any of them.

## The affinage record: precision gate passed, and it missed the Wnt axis entirely

`AHI1-deep-research-affinage.md` frontmatter has **no `gates_passed` field**; it reports
`faith_pct: 83.33`, `self_evaluation_pairwise: win`, 31 citations. Treated accordingly:
nothing mechanistic was taken from it without an independent source.

Two provider traps present:

1. The last citation is `PMID:bio_10.1101_2025.01.20.633784` — a **bioRxiv DOI in a
   PMID-shaped field**, not a PubMed record. The CEP290/AHI1 distribution claim resting on
   it is excluded from this review.
2. **Recall failure on the single most-cited functional story about this gene.** The
   report's 31 findings never mention Wnt, β-catenin, or CTNNB1 — yet UniProt's own
   FUNCTION block ends with
   [file:human/AHI1/AHI1-uniprot.txt "in neuronal differentiation. As a positive modulator of classical Wnt"]
   citing PubMed:21623382 at `ECO:0000269`, and the SUBUNIT block lists
   [file:human/AHI1/AHI1-uniprot.txt "Interacts with CTNNB1/beta-catenin (PubMed:21623382)."]
   Three papers carry it (PMID:19718039, PMID:21602792, PMID:21623382) and none is in the
   affinage citation list. Consistent with the campaign's measured finding that the
   decisive paper is usually titled for something else: two of the three are titled for
   *cystic kidney disease* and *the primary cilium*, not for AHI1.

## The Wnt/β-catenin axis is a GO coverage gap in all three annotated species

```
QuickGO geneProductId=UniProtKB:Q8N157 -> 37 annotations, ZERO in {GO:0016055, GO:0060070,
                                          GO:0090263, GO:0008013, GO:0030177, GO:0198738}
QuickGO Q8K3E5 (mouse) goId=GO:0016055,GO:0008013 goUsage=descendants -> 0 hits
QuickGO Q6DTM3 (rat)   63 annotations, none Wnt/β-catenin
```

So three Nature-family papers over three years produced **no GO annotation in any
species**. That is a coverage defect, not an over-annotation defect, and the review says so.

Species discipline on what can be proposed (the AHNAK lesson — an experimental code
asserts the experiment was done *in the annotated organism*):

- PMID:21623382's *in vivo* work is entirely mouse (Ahi1−/−; BATgal reporter; lithium
  rescue). The human material is fetal MRI — imaging, not molecular.
- Its **molecular** experiments used human AHI1 constructs carrying human JBTS mutations
  in human numbering (V443D, R723Q, H896R against a 1196-aa protein; mouse Ahi1 is 1047
  aa), expressed in 293T: [PMID:21623382 "These disease mutations each exhibited comparable protein expression levels to wild-type Jbn in 293T cells"].
- The β-catenin co-IP and the TOPFlash assay are overexpression experiments, and the
  reporter effect is modest: [PMID:21623382 "Overexpression of wild-type Jbn in these cells resulted in a 1.6-fold increase in reporter activity over vector control"].

## Molecular function: what has actually been measured

AHI1 is a 1196-aa multi-domain protein — coiled coil 13–45, seven WD repeats 607–926,
SH3 domain 1051–1111 (UniProt FT table), no catalytic domain, no EC number, no
nucleotide- or metal-binding site, `PE 1: Evidence at protein level`. The brief's
"a domain's NAME is not an activity" rule applies to both modules: WD40 and SH3 are
interaction modules, and neither implies a catalytic activity to withhold.

Measured molecular properties, all in human cells with human protein:

- **Self-association.** [PMID:23532844 "These results demonstrate that AHI1 is capable of self-association; however, the V443D mutation in AHI1 did not disrupt the self-association of AHI1 ( Fig. 14 )."]
  Already annotated as `GO:0042802`.
- **Defined-stoichiometry heterocomplexes with two different partners through two
  different regions.** NPHP1 through the WD40 repeats:
  [PMID:23532844 "AHI1-WT and NPHP1 co-migrated in two different size complexes, corresponding to molecular masses of 430 and 210 kDa, which possibly represent a heterotetramer (AHI1 2 -NPHP1 2 ) and a heterodimer (AHI1-NPHP1) ( Fig. 3 B )."]
  HAP1 through a region *between* the coiled coil and the WD40 repeats:
  [PMID:23532844 "We determined that a smaller region of AHI1-F2, denoted as AHI1-F3 (141–434 aa), is still able to bind HAP1 ( Fig. 7 , A and G )."]

This is the architecture of a scaffold, and `protein binding` says none of it. Whether it
licenses `GO:0060090 molecular adaptor activity` / `GO:0030674 protein-macromolecule
adaptor activity` turns on whether anything has shown AHI1 *bridging* two partners that
do not otherwise associate — see the decision recorded in the review YAML.

## Checks run that came back negative (recorded so the next reviewer knows)

- **Paralog transfer**: impossible here; PTHR44499 contains one human gene.
- **Retraction/erratum**: 21/21 clean.
- **Partner identity**: 5/5 reviewed canonical Swiss-Prot entries, lengths matching.
- **Stub under-seeding**: none; 37 = 37 = 37.
- **`GO:0042802` downward MODIFY** (the ACRV1 "IBA above its donor" check): not warranted
  — the row is a human IPI at the correct term, not a propagation.
- **Sibling/paralog review cross-check**: not applicable, no paralog reviews exist.

## The adaptor claim: one real test, and two that were checked and rejected

"AHI1 is a scaffolding protein" is asserted throughout the literature from its domain
content alone. In PMID:19625297 it is an Introduction sentence citing somebody else's
review — [PMID:19625297 "Given these domains, it is presumed that AHI1 acts as a scaffolding protein ( 31 )."]
— not a result. A domain's name is not an activity, and the same applies to a domain's
reputation.

The distinguishing test for adaptor activity is a **dependency with a reciprocal
control**: partner A and partner B associate only when the adaptor is present, and
losing B does not abolish A's binding to the adaptor. Exactly one study does this:

- [PMID:35821088 "but affected the interaction between OTUD1 and Tyk2, as shown by the abolishment of the OTUD1-Tyk2 interaction upon AHI1 knockout in primary macrophages"]
- [PMID:35821088 "However, OTUD1 deficiency did not strongly affect the AHI1-Tyk2 interaction"]

The assay is in **mouse** peritoneal macrophages —
[PMID:35821088 "g Immunoprecipitation analysis of the interaction between endogenous OTUD1 and Tyk2 in Ahi1+/+ and Ahi1"]
— and the paper's human material (A549, patient PBMCs) supports only the binary
interactions. Hence `GO:0030674` is proposed as **ISS**, not IDA.

Two candidates were checked and rejected:

1. **AHI-1/BCR-ABL/JAK2.** The interaction is genuinely human and endogenous —
   [PMID:18936234 "We demonstrated a direct interaction between AHI-1 and BCR-ABL at endogenous levels by detection of BCR-ABL in human CML cells (K562) after IP with a human AHI-1 antibody"]
   and [PMID:18936234 "We determined that JAK2 was associated with this protein interaction complex, as AHI-1 could be detected by an anti"]
   — but nothing tests whether BCR-ABL and JAK2 need AHI-1 to associate. A ternary
   complex is not an adaptor demonstration.
2. **AHI1–RAB8A.** Stabilisation and localisation, not bridging, and measured with mouse
   Ahi1 (below).

## The reagent-species trap, in the authors' own words

The sharpest single sentence found in this review, and the reason UniProt's `RAB8A
(By similarity)` coding is right:

[PMID:19625297 "Since our mouse Ahi1 antibody cannot recognize human AHI1 in HEK293 cells, we used this cell line for testing whether Ahi1 and Rab8a form a complex."]

HEK293 is a human line, so the interaction *looks* human at a glance — but the human
protein was deliberately invisible, and what was assayed was transfected **mouse** Ahi1
against transfected Rab8a. Anyone citing PMID:19625297 as human AHI1 interaction evidence
is wrong, and UniProt is not: its SUBUNIT block marks RAB8A and CEND1
`ECO:0000250|UniProtKB:Q8K3E5` while marking CTNNB1 `ECO:0000269|PubMed:21623382`. That
within-block discrimination is what the `GO:0008013` proposal defers to.

## Bounding the Wnt claim with the neighbouring sentence

Two sentences adjacent to the quotes that support `GO:0090263` qualify it, and both are
carried into the review rather than dropped:

- [PMID:19718039 "HEK293T cells transfected with this construct and Jbn alone did not show activation of the Wnt pathway, indicating that Jbn is not an activator of the pathway"]
- the effect size is modest — [PMID:21623382 "Overexpression of wild-type Jbn in these cells resulted in a 1.6-fold increase in reporter activity over vector control"]

So jouberin is an **amplifier of an already-initiated response**, not an initiator.
`GO:0090263`'s definition ("increases the rate, frequency, or extent") accommodates that;
a term implying initiation would not.

## A genuine disagreement in the field, not a curation error

Two independently derived Ahi1-null mouse lines contradict each other on ciliogenesis,
in the same cell type, in the same year:

- [PMID:19625297 "However, there was a significant reduction in ciliated MEFs cultured from Ahi1"] (10% vs 57%)
- [PMID:19718039 "We therefore concluded that Jbn is not necessary for proper ciliogenesis, suggesting alternative mechanisms for the defects in these mice."]
- and the same group again in cerebellar granule neurons —
  [PMID:21623382 "CGNs isolated from Ahi1 null and control littermates exhibited indistinguishable number of cilia and morphology"]

The human patient-fibroblast result falls on the "required" side
([PMID:23532844 "Fibroblasts from individuals with JBTS showed an"] ~50% decrease), and
PMID:23532844 itself notes the discrepancy —
[PMID:23532844 "Our data from JBTS patient cells and Ahi1 knock-out mice showing impairments in primary cilia formation"]
— attributing it to strain background. Recorded as a `knowledge_gap` on the GO:0060271
row rather than resolved, and it is a further argument for anchoring the human annotation
to human cells.

## Human interaction data GOA has never taken up

Separate from the Wnt gap, two endogenous human interactions have no GO annotation:
AHI-1 with BCR-ABL and JAK2 in K562 cells (PMID:18936234), and AHI1 with OTUD1 and TYK2
in A549 cells and patient PBMCs (PMID:35821088). Both are filed in `suggested_questions`.
Consistent with the campaign's finding that for a well-studied gene the defect is as
likely to be **absent curation** as over-annotation: this gene has 37 GOA rows, of which
14 are ISS from a single mouse accession and 3 are one Reactome compartment label.

## Committed check

`AHI1-bioinformatics/audit_ahi1_claims.py` (with `--self-test`) enforces the invariants
above: strict duplicate-key loading, GOA-row-to-review bijection keyed on
(term, evidence, reference, WITH/FROM), `source_entities` derived from the WITH/FROM
field rather than by hand, no `PENDING` left, every cited reference declared, and
raw-vs-parsed `reference_id` arithmetic.

Writing it exposed a defect in itself: check 3 indexed the WITH/FROM map with `[]`, so a
row that failed check 2 raised a `KeyError` that aborted the whole run *before any
problem was printed* — the harness would have reported nothing while looking like it had
run. Found by the self-test, not by reading. The fix appends a problem and continues,
per the rule that a check must never raise from inside the collector.

Paths resolve relative to the script. A scratch copy of a similar checker in the shared
session directory carried an absolute path into a **different agent's worktree**, which
made every full-text quote resolve against a cache holding only abstracts and produced 56
false failures. That is the same shape as the `size=1` trap: a lookup that silently
answers about the wrong thing.
