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
NPHP1 or HAP1 — both were additionally examined by gel filtration, which co-migrated each
pair as species whose masses the authors read as a heterotetramer — but it means the count
is not a replication count. (The stoichiometries themselves are the authors' reading of
migration behaviour, not a measured quantity; see the round-2 section below.)

Correction: `NbExp` counts **records**, not methods — which is why NPHP1's 4 does not
equal its 2 methods while HAP1's 3 happens to equal its 3. See the round-1 section below
for the per-record resolution.

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
- **Sibling/paralog review cross-check**: no *paralog* reviews exist (AHI1 has no human
  paralogue), but two *complex-subunit* siblings do — see the next section, which found a
  merged review resolving an identical row the opposite way.

## A merged sibling ACCEPTs the identical row — and is right to

The AADACL2/3/4 lesson says to check how sibling genes resolved the same row, and to flag
a divergence rather than diverge silently. Of the 14 MKS-complex subunits, two have gene
folders in this repo: **CC2D2A** and **TMEM67**. `genes/human/CC2D2A/CC2D2A-ai-review.yaml`
is on `main` and carries the **byte-identical** row —
`GO:1904491 / NAS / PMID:22179047` — with `action: ACCEPT`, where I mark it
over-annotated.

Both are correct, because the surrounding evidence differs, and the numbers say so:

| | annotations for `GO:1904491` | reaches an experimental annotation? |
|---|---|---|
| human **CC2D2A** `Q9P2K1` | **3** — IBA (GO_Central), IEA (Ensembl Compara), NAS (ComplexPortal) | **Yes** — mouse `Cc2d2a` `Q8CFW7` (Swiss-Prot, 1633 aa) holds it by IMP |
| human **AHI1** `Q8N157` | **1** — NAS (ComplexPortal) only | **No** — and mouse `Ahi1` and rat `Ahi1` carry the term at all |

So on CC2D2A the ComplexPortal NAS is redundant with independently supported annotations;
on AHI1 it is the *only* thing asserting the process. The two reviews differ on evidence,
not on method — which is the distinction the AADACL2/3/4 episode showed nobody had drawn.

Corroborating detail from the same reference: of the 4 entities carrying `GO:0035869` by
IDA from PMID:22179047, one is mouse Cc2d2a — and **none is AHI1 in any species**. The
paper's experimental reach simply does not include this gene, for either term.

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
13 are ISS from a single mouse accession and 3 are one Reactome compartment label.

Evidence-code breakdown of the 37 rows, computed rather than eyeballed
(`awk -F'\t' 'NR>1 {print $9}' AHI1-goa.tsv | sort | uniq -c`):
**ISS 13, IPI 6, IDA 6, TAS 3, NAS 3, IEA 2, IBA 2, IMP 1, IC 1 = 37.**

Recorded because the first draft of this review said "14 of 37 GOA rows are ISS" in two
places. The count was never derived — it was estimated while reading — and it was wrong
by one. Counting the column took five seconds. **A number in a review that was not
computed is a latent error**, and the campaign's most heavily confirmed lesson is that a
number which refuses to add up is the actual bug report.

## Review round: the one factual challenge, checked rather than conceded

The PR review approved and raised five non-blocking suggestions. Four were taken as
written. The first was a **factual challenge**, and the campaign rule is to verify a
reviewer's checkable premises before conceding, because a conceded-but-false point
becomes a defect in the review.

The challenge: the `GO:0005515`/NPHP1 row claims UniProt's `NbExp=4` comes from one
publication, but GOA carries **two** NPHP1 IPI rows from two papers (`PMID:18633336` and
`PMID:23532844`) and UniProt cites both — so `NbExp=4` "plausibly spans both".

Re-queried IntAct **per record**, resolving each to its PubMed id rather than to the
internal `EBI-*` experiment id the first pass had printed:

```
NPHP1 (O15259): 4 records
  EBI-9662903  molecular sieving  pubmed=23532844
  EBI-9662916  molecular sieving  pubmed=23532844
  EBI-9662962  anti tag coip      pubmed=23532844
  EBI-9661010  anti tag coip      pubmed=23532844
  distinct PubMed ids: ['23532844']
```

The original claim is **correct**: 4 records, 2 methods, 1 paper. All five partner pairs
resolve the same way — every IntAct record for AHI1 traces to a single publication per
partner.

But the challenge pointed at something real, and the reconciliation is worth recording.
`NbExp` counts **records**, not methods, which is why NPHP1's 4 does not equal its method
count while HAP1's 3 does. And `PMID:18633336`'s NPHP1 evidence is missing from IntAct
because that GOA row is `assignedBy: UniProt` — curated straight from the paper without
being lodged in IntAct — while the other is `assignedBy: IntAct`. So the two GOA rows
**are** independent evidence even though IntAct's count is not, and the apparent
arithmetic problem is an assigner artefact rather than a counting error.

The first pass had printed `publicationIdentifiers[0]`, which is an `EBI-*` token that
says nothing about how many papers are involved — the `size=1` trap in another guise: a
lookup that answers confidently about the wrong thing.

The other four suggestions were adopted: the `GO:0090263` proposal now spells out the
**two-step** implementation (mouse IMP first, human ISS second — a curator cannot make an
ISS whose `WITH` target lacks the term); `core_functions` entry 1 now says explicitly
that its adaptor MF is **inferred by transfer** from a mouse macrophage assay rather than
demonstrated at the transition zone; `GO:0097730` was added to that entry's locations and
self-association was given its **own** `core_functions` entry, since V443D separates it
from NPHP1 tetramer formation and it is one of only two molecular activities measured on
the human protein in human cells; and the `GO:0007169` row now states the line it sits
on — whether the annotated process is one the protein's *measured activity acts on* —
which keeps it while `GO:0045944` and `GO:0050795` fall the other way.

## Review round 2: four over-claims, all in a block I had just added

Round 2 approved and raised four non-blocking items, **all inside the `GO:0042802`
`core_functions` entry written in response to round 1** — i.e. the newest prose was the
weakest. All four were verified against the paper and all four were real. They share one
shape: **I reported the authors' interpretation as their result.**

**The oligomeric state is hedged, and I had asserted it.** I wrote that gel filtration
"resolves AHI1 dimers and tetramers as discrete species". What PMID:23532844 says is:

[PMID:23532844 "which could correspond to an AHI1 homodimer. However, the molecular weight of the peak is smaller than the expected weight of the dimer"]

— a hedge *followed by an argument against itself*. And the "tetramers and dimers of
AHI1" phrase I had leaned on occurs in the **V443D mutant** lane, not the wild-type one.
This is the ACBD3 rule exactly: **quote to the end of the interpreting clause.** Truncating
before "However…" converts a hedged non-result into a finding. The entry now separates the
*activity* (established: co-IP of two differently tagged copies in human cells) from the
*stoichiometry* (not established).

**A quote that supported the neighbouring claim, not the one it was attached to.** The
entry's second `supporting_text` was the AHI1–NPHP1 co-migration sentence — which
evidences the heterocomplex, not self-association. Verbatim, correctly attributed, and
attached to the wrong claim; no quote checker can see this, because every mechanical check
validates a quote against its *source* and none validates it against the *claim*. Replaced
with the sentence that actually carries the point, which also carries the separability
argument:

[PMID:23532844 "These results demonstrate that AHI1 is capable of self-association; however, the V443D mutation in AHI1 did not disrupt the self-association of AHI1"]

**"Retained" asserted a mechanism the data does not distinguish.** I had written that AHI1
is required for RAB8A "to be retained" at the basal body. PMID:19625297 reports that
Rab8a levels *fall* and it *cannot be detected* there — which does not separate failed
recruitment from failed retention, and the total-level drop means part of the effect may
be stability rather than localisation at all. Now stated as "accumulate", with the
ambiguity named.

**UniProt's own hedge dropped in transit.** UniProt writes "probably as heterodimers
and/or AHI1(2):NPHP1(2) heterotetramers" and "probably as AHI1(2):HAP1(2)
heterotetramers"; my `description` had "assemble into a defined heterotetramer and
heterodimer". Corrected in all four places where a stoichiometry appears, applied with a
script that asserts each anchor is present before replacing and absent afterwards, so a
missed site is an error rather than a silent no-op.

**The generalisable lesson:** the review's oldest, most-checked prose was fine, and every
defect this round was in text added one round earlier and gated only by "is the quote
verbatim?". A new block written to satisfy a reviewer deserves the same scepticism as the
original draft, not less.

## Review round 3: the guard was fine, the site list was not

Round 3 requested changes on one IMPORTANT item, and it is the sharpest process finding
of this review.

Round 2's fix was applied with a script that **asserted each anchor was present before
replacing and absent afterwards** — the "fixed in N places, landed in N−1" guard, working
exactly as designed. It reported four edits applied. And yet the retracted phrase
*"resolve AHI1 dimers and tetramers as discrete species"* was still in the file, in the
`GO:0042802` `existing_annotations` row, saying the opposite of what `core_functions` now
said.

**The guard verified the four sites it was handed. The four sites had been enumerated
from memory rather than from a search.** So the failure mode the guard exists to prevent
simply moved one level up, into the input. A guard over a hand-supplied site list inherits
the incompleteness of that list, in the same way the ACTA1 guard inherited the scope of
the claim it was checking.

Worse, the surviving text was load-bearing, not cosmetic: the rejection of a MODIFY to
`GO:0042803 protein homodimerization activity` rested **entirely** on the retracted claim
("the paper resolves tetramers as well as dimers"). The conclusion survives and is in fact
stronger — an unresolved copy number is a reason not to narrow to a dimer-specific term —
but a curator reading that row alone would have got the disavowed argument.

**The fix is structural, not another careful pass.** `audit_ahi1_claims.py` now carries:

- **check 7** — a scan for every retracted phrasing across *both* the review YAML and the
  notes, which takes **no site list as input** and therefore cannot be defeated by an
  incomplete one. The notes are scanned with double-quoted spans stripped, so this
  write-up can quote the retracted phrases while documenting them.
- **check 8** — the *replacement* claims must be present. A retraction with nothing in its
  place is a deletion, and check 7 alone would pass on it silently.

Check 8's first version was itself defective and the self-test caught it: it took an
**OR-list of alternatives**, so deleting one site still passed because a sibling phrase
elsewhere satisfied the list — the "guard defeatable by deleting the thing it guards"
failure, reproduced verbatim. Rewritten as one required string per site with its own
minimum count. **Two of the seven guards in this file were found broken by trying to break
them, and neither by reading them.**

Two non-blocking items from the same round, both verified before acting:

- **My RAB8A caveat over-corrected.** I had written that the total-level drop means "some
  of the effect may be stability rather than localisation at all". The paper controls for
  exactly that — overexpressed HA-Rab8a restores abundance and *still* never reaches the
  basal body in Ahi1-knockdown cells, so localisation fails independently of abundance.
  The recruitment-versus-retention ambiguity is real and kept; the stability alternative
  is excluded and has been removed. A hedge can be wrong in the cautious direction, and
  that is still wrong.
- **The HAP1 stoichiometry was hedged harder than NPHP1's** although both rest on the same
  kind of evidence and the same degree of authorial hedging. Levelled.

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

## 2026-09-27 substantive re-review (Codex)

This entry supersedes the interpretation and action recommendations in the earlier review rounds above. Historical notes are retained as provenance, not as current conclusions. All 37 imported annotations and all three pre-existing NEW proposals retain their source objects, qualifiers and supporting entities. Original reference identifiers/titles and alternative-product records are preserved. The biological review now separates the ciliary, Wnt and immune-adaptor contexts, and the document is DRAFT pending normal recovery of one newly required publication cache.

### Identity, baseline and source access

AHI1 is the HGNC-approved symbol (HGNC:21575), UniProt Q8N157. The HGNC-supplied NCBI record independently confirms aliases AHI-1, JBTS3, ORF1 and dJ71N10.1; FLJ20069 and Jouberin also occur in the existing source record. Identity source: <https://www.ncbi.nlm.nih.gov/gene/54806>. The parent verified current-main author blobs and searched open PRs for canonical/historical names before authoring; no overlap was found. The immutable UniProt, GOA, existing genuine affinage report and old bioinformatics script are unchanged.

The required genuine Falcon attempt with configured perplexity-lite fallback used writable temporary UV directories. Both attempts stopped before provider execution because `uvx deep-research-client` could not resolve PyPI. Wrapper exit was 1; no new provider report was created. The existing affinage report remains genuine but is a lead, not primary evidence. Concurrent normal publication retrieval found all 18 originally cited PMIDs cached. A standard PAINT fetch for PTHR44499 also failed to resolve data.pantherdb.org; no source files were manufactured. The detailed current ancestral node/MSA remains uninspected.

New primary [PMID:28118669, The Ciliopathy Gene ahi1 Is Required for Zebrafish Cone Photoreceptor Outer Segment Morphogenesis and Survival](https://pubmed.ncbi.nlm.nih.gov/28118669/) was verified from the primary PubMed abstract. Normal `fetch-pmid 28118669` failed DNS and cached 0/1; no file was produced. This is the sole additional notes-inclusive publication gate. Its full paper was not recovered. It reports cell-specific outcomes: cone outer segments and distal pronephric cilia are affected while the photoreceptor connecting cilium and Cc2d2a/Cep290 localization are retained. These results qualify universal claims without excluding a function in other tissues.

`full_text_unavailable` is based on local cache metadata/content, not on an external page or a peer's full-text access. The locally abstract-only records remain marked unavailable even where additional primary text was read externally. No cached source was hand-edited.

### Ancestral inference and donor provenance

The two IBA rows inherit from PTN002893387. Their propagation assessments now represent that ancestor, rather than substituting a list of modern proteins. Human AHI1 appearing among experimental descendants is expected PAINT behavior, not circularity. A single zebrafish descendant or a TrEMBL identifier is not weaker experimental evidence merely because of the count or entry status. Non-motile-cilium localization does not demonstrate loss of motile-cilium assembly function in humans.

The full cached [PMID:21959375](https://pubmed.ncbi.nlm.nih.gov/21959375/) directly reports Kupffer's-vesicle cilia loss after zebrafish ahi1 knockdown: “cilia were absent from KV in 23 out of 25”. Mouse Ahi1 mRNA rescues gross morphant phenotypes; that rescue is not recast as a separate quantified rescue of every ciliary endpoint. The same paper studies mouse IMCD3 knockdown and evolutionary occurrence in ciliated eukaryotes. Retain the motile-cilium IBA in the absence of evidence for human lineage-specific loss, while clearly distinguishing inheritance from a direct human motile-cilium assay. The current PAINT slice was unavailable, so its internal placement is UNRESOLVED rather than falsely claimed as independently reconstructed.

The indexed historical MGI comparative graph, <https://www.informatics.jax.org/homology/GOGraph/Ahi1>, independently resolves the mouse Q8K3E5 links: receptor internalization, receptor-tyrosine-kinase signaling, positive Pol II transcription and behavior all trace to [PMID:20956301](https://pubmed.ncbi.nlm.nih.gov/20956301/); photoreceptor/opsin localization and apoptosis to [PMID:20081859](https://pubmed.ncbi.nlm.nih.gov/20081859/); vesicular trafficking/centriole localization to [PMID:19625297](https://pubmed.ncbi.nlm.nih.gov/19625297/); outer-segment organization also to [PMID:20592197](https://pubmed.ncbi.nlm.nih.gov/20592197/). This is provenance from an indexed snapshot, not a claim that a current complete GOA export was obtained.

The original source-code mismatch question for the human IMP from PMID:21959375 is retained, but the paper is no longer called an incorrect citation merely because its experiments use model systems. The biological cilium-assembly assertion has independent direct human fibroblast support in [PMID:23532844](https://pubmed.ncbi.nlm.nih.gov/23532844/).

### Positive evidence and context corrections

The primary full Results of [PMID:20956301 / PMC2973903](https://pmc.ncbi.nlm.nih.gov/articles/PMC2973903/) were externally recovered through the indexed primary page. They include surface-crosslinking/internalization experiments, reduced intracellular BDNF after Ahi1 depletion, TrkB degradation time courses and Hrs–TrkB association. The earlier abstract-based suggestion that no internalization assay existed is superseded. Receptor degradation and internalization remain distinct readouts. Mouse behavioral rescue and signaling phenotypes justify a contextual process annotation without implying that human psychiatric disease was experimentally modeled.

Positive regulation of transcription does not require AHI1 itself to bind DNA. The exact transcription readout underlying the PMID:20956301 donor annotation remains unresolved, but independent cached full [PMID:19718039](https://pubmed.ncbi.nlm.nih.gov/19718039/) measures stimulated Wnt reporter and endogenous cyclin D1 output with beta-catenin nuclear accumulation. These establish a plausible signaling-mediated positive-regulation role. The source distinction is explicit in the annotation and reference review.

Opsin-dose rescue of photoreceptor death in PMID:20081859 places apoptosis downstream of cargo handling. It does not logically disprove negative regulation of apoptosis; that broad process can include an indirect protective mechanism. The annotation is retained as a retinal non-core consequence rather than interpreted as direct caspase inhibition.

Broad centrosome, centriole, cilium and cytosol locations are retained where the source supports them. A precise basal-body or transition-zone record does not invalidate a broader observed compartment. Conversely, junctional localization remains a contextual epithelial pool. PMID:18633336 names mouse mIMCD3 and canine MDCK hosts, but an expression host does not determine construct species; the accessible abstract alone does not justify declaring all human annotations wrong. Later PMID:23532844 explicitly uses human AHI1 constructs and independently corroborates basal-body and junctional localization.

The three Reactome events were checked against cached summaries and live reaction pages: [R-HSA-5617816](https://reactome.org/content/detail/R-HSA-5617816), [R-HSA-5626681](https://reactome.org/content/detail/R-HSA-5626681), and [R-HSA-5638009](https://reactome.org/content/detail/R-HSA-5638009). Their cytosol assertions concern participant assemblies. They do not make AHI1 the exchange factor or the catalytic actor of the named event.

### Interaction specificity and core synthesis

The four generic protein-binding rows for NPHP1, HAP1 and DNM2 are removed as uninformative functional summaries, without denying their interaction evidence. The NPHP1 domain-mapping lead is acknowledged but a new assay-specific domain claim is not manufactured from the full-length co-immunoprecipitation alone. By contrast, the full [PMID:25825872](https://pubmed.ncbi.nlm.nih.gov/25825872/) peptide-array and phage-display experiments directly establish recognition of proline-rich ADAM12 motifs by the isolated AHI1 SH3 domain. That row is refined to GO:0070064, proline-rich region binding. A shared motif preference does not invalidate an assay; lack of full-length cellular validation limits physiological interpretation, not the observed domain activity. Live definitions: <https://amigo.geneontology.org/amigo/term/GO:0070064> and <https://amigo.geneontology.org/amigo/term/GO:0017124>.

Self-association from human tagged-protein co-immunoprecipitation in PMID:23532844 is retained and integrated with ciliary organization. The source's larger complex sizes are migration-based, tentative stoichiometries; neither a particular tetramer nor a universally obligatory oligomer is asserted.

A read-only annotation-reviewer consultation independently inspected [PMID:22179047](https://pubmed.ncbi.nlm.nih.gov/22179047/) through the author-uploaded primary article (<https://www.researchgate.net/publication/51897621_A_ciliopathy_complex_at_the_transition_zone_protects_the_cilia_as_a_privileged_membrane_domain>). Affinity recovery with two baits and co-fractionation support Ahi1 complex membership. Perturbations of other subunits do not invalidate structural participation, but they also do not identify an AHI1-specific molecular bridge. The exact protein-localization-to-transition-zone process is left UNDECIDED, distinguished from better-resolved delivery into cilia. GO:1904491 includes maintenance at the zone, not only physical transport: <https://amigo.geneontology.org/amigo/term/GO:1904491>.

Full cached [PMID:25103236](https://pubmed.ncbi.nlm.nih.gov/25103236/) places Ahi1 downstream of Cby1 recruitment and shows Ahi1-depletion effects on ciliary ARL13B rescued with human AHI1. [PMID:31391239](https://pubmed.ncbi.nlm.nih.gov/31391239/) is abstract-only locally but corroborates ARL13B recruitment/stability. Full [PMID:33741721](https://pubmed.ncbi.nlm.nih.gov/33741721/) distinguishes lost ciliary MCHR1 from preserved total and plasma-membrane receptor in mouse neurons. Together with human fibroblast data, these justify the existing refinement from broad intracellular protein localization to protein localization to cilium.

The Wnt core retains the actual positive interaction, nuclear localization and stimulated-response evidence from PMID:19718039 and [PMID:21623382](https://pubmed.ncbi.nlm.nih.gov/21623382/). [PMID:21602792](https://pubmed.ncbi.nlm.nih.gov/21602792/) supports ciliary sequestration at abstract scope. The description no longer claims purified direct binding, universal tissue effects, universal absence of annotations, or an inferred reason that a pipeline missed a paper. Original construct provenance remains a specific uncertainty. The prior NEW Wnt proposal is retained on mechanistic participation, not on absence alone; it is not a substrate-necessity inference. GO:0090263 has positive-regulation-of-signaling parents, and none of the other retained NEW proposals is its ancestor/descendant. The cached GO-CAM index has no Q8N157/Q8K3E5/AHI1 match. Comparative primary-database searches of BCL9/PYGO proteins show canonical Wnt/Pol II process annotations, with varied granularity, rather than a universal prohibition on annotating intracellular beta-catenin cofactors. They do not establish an exact GO:0090263 gap by themselves.

The third core is now the separately supported immune adaptor mechanism. Full cached [PMID:35821088](https://pubmed.ncbi.nlm.nih.gov/35821088/) and independent peer consultation support Ahi1-dependent OTUD1–Tyk2 association in mouse primary macrophages, with reciprocal controls and human A549 corroboration. Figure 4C uses RAW264.7 cells; Figure 4G is the primary-macrophage dependency experiment. OTUD1 performs deubiquitination; AHI1 recruits it. This is not presented as the molecular activity measured at the ciliary transition zone. The human CML complex in [PMID:18936234](https://pubmed.ncbi.nlm.nih.gov/18936234/) supports association/signaling but does not establish the same particular dependency. The earlier claim that exactly one study in all literature has tested bridging is replaced by the bounded account of the source actually read.

All reference-review findings were reconciled with these decisions. Exact original reference titles remain unchanged. No new provider output, machine cache or source assertion was invented.

### Final evidence-excerpt and citation-census check

The coordinator independently read all 40 decisions, three cores and 27 reference assessments and accepted the biological scope. Before publication, 34 incomplete inherited supporting excerpts were replaced with substantive verbatim passages from their actual caches, including beta-catenin co-recovery, human fibroblast ciliation, HAP1 binding, ciliary/junctional localization and the OTUD1–TYK2 dependency. All 73 cached annotation/core/finding excerpts were checked against the source text. Actions and all original source objects remain unchanged. The transcription caveat for PMID:20956301 now explicitly covers the externally recovered Results inspected, rather than implying only the abstract was considered.

The earlier prefix-only citation census missed three identifiers in the historical comma-separated retraction-sweep list: PMID:28442542, PMID:25616960 and PMID:18636121. These are retained historical citations, not newly verified primary support for the current judgments; the inherited claim of a clean corrections sweep is not independently reasserted. Normal fetches for all three failed DNS and cached 0/1 each. The complete notes-inclusive census is therefore **22 PMIDs, 18 cached, four missing**: PMID:18636121, PMID:25616960, PMID:28118669 and PMID:28442542. This supersedes the earlier single-source cache-gate statement. No cache bytes or provider output were fabricated, and the review remains DRAFT.


## 2026-09-27: PR #3215 evidence-code and core follow-up

Read the complete current-head review at <https://github.com/ai4curation/ai-gene-review/pull/3215#issuecomment-5852254267> against head `515f45bac7a82f32942208d20dedaeec74e0072b`. The three gene artifact blobs matched the published tree before edits. All 37 machine-seeded annotation objects retain their original term, evidence, reference, qualifier, supporting entities and isoform fields; their actions are unchanged.

The three prior authored NEW proposals are withdrawn, superseding the earlier retention notes above. For GO:0090263, the full cached [PMID:19718039](https://pubmed.ncbi.nlm.nih.gov/19718039/) shows stimulated reporters and endogenous cyclin D1 in human host cells, plus mouse loss-of-function and beta-catenin nuclear-localization measurements. [PMID:21623382](https://pubmed.ncbi.nlm.nih.gov/21623382/) uses disease-variant constructs linked back to the former study. Neither accessible Methods section resolves the original Jouberin construct species. Further attempts to read the PMC/Nature supplement did not recover it. A human host cell is not sufficient to code an assay as direct evidence for a human transgene. The same limitation applies to the prior GO:0008013 IPI proposal: the human UniProt record has an experimental CTNNB1 interaction citation, but that curated trace alone does not resolve the source detail needed to manufacture a NEW annotation. This does not deny beta-catenin association or the positive Wnt findings.

For the prior GO:0030674 ISS proposal, full cached [PMID:35821088](https://pubmed.ncbi.nlm.nih.gov/35821088/) Figure 4g directly measures loss of OTUD1–Tyk2 association in Ahi1-null mouse peritoneal macrophages; Figure 5c tests ubiquitination dependency in RAW264.7 cells. Human A549 Supplementary Figure S5a shows association and S4g measures TYK2 stability. Those human assays corroborate the pathway but do not establish the same bridging dependency. An independent annotation-reviewer consultation confirmed this boundary. An exact implementable mouse donor GO assertion remains unverified. Consequently, no direct-human IDA/IMP recoding is made merely to satisfy the review. The measured mammalian biology remains in the synthesis and questions, with the original species limits, while the corresponding formal core MF/BP assignments are omitted pending provenance resolution.

The ciliary core also omits its optional GO:0042802 MF because self-association does not identify the specific AHI1 activity that organizes the transition zone. The existing self-association annotation remains ACCEPT. The core's explicit knowledge gap carries this distinction; no hypothetical complex activity or contributes_to qualifier is invented.

Retain GO:0016192 vesicle-mediated transport as ACCEPT: the mouse primary study [PMID:19625297](https://pubmed.ncbi.nlm.nih.gov/19625297/) directly distinguishes defective Golgi-directed transport and transferrin recycling from preserved vesicle formation/internalization. These are central cargo-organization functions, now included in the ciliary/trafficking core. Refining a different opsin-localization source to its measured ciliary destination does not force all trafficking to that destination. Likewise, retain the GO:0044458 IBA: cilium assembly is already represented by the broader core process, and annotation core status does not require literal duplication of every child term in the core table.

Fresh primary verification of [PMID:28118669](https://pubmed.ncbi.nlm.nih.gov/28118669/) on 2026-09-27 recovered the PubMed abstract and figure captions, with DOI 10.1167/iovs.16-20326 and PMCID PMC5270624. Figure 9 shows preserved photoreceptor connecting-cilium markers; Figure 10 explicitly describes human AHI1 RNA rescue of mutant zebrafish distal pronephric cilia. This strengthens the conserved cilium-assembly interpretation without asserting a native human motile-cell assay. The PMC full-text route returned a browser challenge. VERIFIED continues to mean that the identifier and cited primary result were checked; it does not mean a local cache exists. No cached quote or findings entry has been manufactured from the web passage.

The cilium IC annotation no longer uses a culture-medium sentence as localization support; the existing human-construct basal-body result provides the relevant evidence. GO:1904491 remains UNDECIDED because the full original NAS evidence and the AHI1-specific transition-zone recruitment dependency are incompletely resolved. Preservation of two markers in one retinal model does not disprove structural participation for every substrate or tissue.

The four existing notes-inclusive cache gates remain: PMID:18636121, PMID:25616960, PMID:28118669 and PMID:28442542. They are assigned to the normal batch recovery workflow; this follow-up does not duplicate that active fetch, fabricate records or downgrade previously verified external identity merely because the cache is missing. Status remains DRAFT. Validation, rendering, new history and the final publication manifest are recorded separately for the coordinator.

## 2026-09-27 verified source2 cache recovery

This entry supersedes the preceding missing-cache statements without rewriting
that historical access record. Four genuine, normally generated publication
records are now cached: PMID:28118669 and PMID:28442542 contain extracted full
text; PMID:18636121 and PMID:25616960 remain abstract-only. Each byte count and
SHA-256 digest matches `tmp/verified-reference-records2/local-import-receipt.json`.
The source artifact is 10923045788 from run 36289953066, source head
`fecff1befb769b1753300fa1bc2e3442813e9dd2`, ZIP SHA-256
`0876942c72b2e537e858e8af7cd3c79d34b97c2169490e3d883c6f00884e2965`.
No source bytes were edited or reconstructed.

The recovered Methods/Results and Figures 9–10 of PMID:28118669 confirm the
previous external source reading. Human wild-type AHI1 RNA rescues pronephric
cilia and cone outer-segment phenotypes in mutant zebrafish; the R589X construct
does not. This remains human-construct rescue in a zebrafish host, not an assay
of native human motile cells. A verbatim cached result is now attached to the
retained IBA judgment. Connecting-cilium localization of Cc2d2a and Cep290 is
preserved in the retinal model, although Cc2d2a fluorescence intensity is reduced.
This distinction is now explicit in the transition-zone process rationale;
it does not resolve all possible AHI1-dependent substrates or tissue contexts.

PMID:28442542 Methods and Results test full-length human AHI1 isoform 1 and
WD40-domain variants expressed as mRFP fusions in hTERT-RPE1 cells. Wild-type
protein is enriched at the ciliary base, and tested RP/JBTS variants show reduced
enrichment. Patient-fibroblast ciliation, cilium length and IFT marker patterns
show no significant differences in the reported comparisons. This corroborates
compartment and allele-specific context without establishing a new exact
transition-zone recruiting mechanism. PMID:18636121's recovered abstract
explicitly describes the mouse Ahi1–Hap1 complex and developmental/trafficking
phenotypes. PMID:25616960's abstract distinguishes tolerated C-terminal human
truncations from disease-associated upstream effects, with zebrafish experiments;
it does not establish that every truncating AHI1 allele is functionally equivalent.
The earlier historical claim of a clean retraction sweep is not reasserted merely
because citation records are now available.

All 37 seeded source objects and actions, core functions and the three withdrawn
prior NEW proposals remain as in the reviewed follow-up. The prior unpublished
feedback history is preserved byte-for-byte; a separate cache-recovery history
records this session. All four notes-inclusive publication cache gates are now
closed. Status remains DRAFT while the unused-provider validation advisory
persists; cache availability is not confused with universal full-paper access
or verification of every donor assertion.

## 2026-09-27 human-construct evidence follow-up to PR #3215

The exact starting head was `6b887c162d6740158c36c518fb65324ed4230db4`.
A fresh GitHub API read confirmed that open head, and all three local author
files matched its immutable Git blobs before editing. This entry addresses
[the current review](https://github.com/ai4curation/ai-gene-review/pull/3215#issuecomment-5853340565).
All 37 seeded source objects and all 37 actions remain unchanged. No withdrawn
NEW proposal is reinstated, and no machine-fetched source or prior history is edited.

The recovered primary [PMID:28442542](https://pubmed.ncbi.nlm.nih.gov/28442542/)
([PMC5574394](https://pmc.ncbi.nlm.nih.gov/articles/PMC5574394/),
DOI 10.1136/jmedgenet-2016-104200) is now an explicit YAML reference. I read its
cached cDNA-construct and immunocytochemistry Methods, Results Figures 4–5 and
Discussion. The synthetic full-length human isoform 1 construct AM393493 was
adapted to reference NM001134831.1; wild-type and variant sequences were
Sanger-validated. The human hTERT-RPE1 experiment used N-terminal mRFP fusions;
full-length expression was checked separately in HEK293T. Thus construct species
and cellular host are both established rather than inferred from the cell line.

The exact result, “Wild-type mRFP-AHI1 showed a diffused cytoplasmic localisation
and a strong enrichment at the ciliary base of ciliated hTERT-RPE1 cells”, now
supports the basal-body IDA judgment, the broader cilium IC judgment, the three
Reactome cytosol judgments and the integrated ciliary core. The two original
experimental references retain their own mouse/construct-access limits; the
human study is independent corroboration, not a rewritten original assay.
The new study does not establish AHI1 throughout the axoneme or distinguish
cytosol from every cytoplasmic subcompartment by fractionation.

Tested RP and Joubert WD40 variants both reduce basal-body enrichment; their
similar localization phenotype does not explain the distinct clinical groups.
“Neither ciliary frequency nor cilium length varied significantly” applies to
the RPE1 overexpression comparisons. Patient A-II:1 fibroblasts separately
retain approximately 90% ciliation, cilium length and the reported IFT-marker
distribution. These measured limits now support the core's model/allele context.
The paper's residual-function and tissue-specific mechanistic explanations are
hypotheses, not new mechanistic annotations.

The three nonblocking suggestions were assessed as follows:

- The Wnt and OTUD1–TYK2 core descriptions retain explicit biological synthesis
  and knowledge gaps without adding optional GO terms. A core slot is not an
  evidence-coded annotation, but it is still a human molecular/process assertion.
  Preserving the direct-human construct and endogenous bridging boundaries is a
  deliberate conservative representation; the positive mouse mechanism remains
  fully described. This choice does not imply that an implementable donor
  annotation is a schema prerequisite for every core function.
- The three cytosol assertions remain ACCEPT at their curated Reactome
  participant resolution. A specialized adherens-junction pool being non-core
  does not make the broader compartment non-core. The human cytoplasmic imaging
  is attached as corroboration, and cytosol is now included among core locations.
- The transition-zone NAS row gains the exact cached PMID:25103236 statement,
  “We show that Cby1, Ofd1, and Ahi1 localize as tightly apposed rings at a similar
  position along the long axis of the centriole.” The suggested AHI1-specific
  quotation is not present in the local PMID:22179047 record: that cache is
  abstract-only and does not name Ahi1. Its MKS-complex rows therefore retain the
  previously documented author-full-text affinity/co-fractionation evidence and
  original source coding, without attaching a generic nine-protein or another
  subunit's knockout quote as if it directly identified Ahi1. The full author
  route remains recorded above; no source text is fabricated.

No additional publication or Reactome cache is required by this follow-up.
The existing genuine provider report remains preserved and is not treated as
primary evidence merely to suppress its unused-provider advisory. Targeted
validation, rendering, exact-quote/source-preservation checks and a newly
scaffolded session record are recorded in the accompanying frozen manifest.

### Recursive preserved-report cache census

The current YAML and authored biological notes have no missing source cache.
A separate recursive check of the immutable genuine affinage report found 14
older provider-only PMID citations with no cache: PMID:12186888, PMID:15322546,
PMID:15467982, PMID:18785627, PMID:19211505, PMID:22123816, PMID:23658157,
PMID:29449373, PMID:30949029, PMID:31062249, PMID:33782379, PMID:34218273,
PMID:35643536 and PMID:36691038. Its five uncached pathway identifiers are
Reactome:R-HSA-1266738, Reactome:R-HSA-162582, Reactome:R-HSA-168256,
Reactome:R-HSA-392499 and Reactome:R-HSA-9609507. These are now explicit
artifact-source gates; no new biological conclusion was copied from that report.
The earlier cache-closure entry covered the then-audited YAML/notes citations
and did not establish this broader preserved-report census.

Ordinary retrieval attempts were initiated on 2026-09-27; their exact outcomes
are recorded separately in `/tmp/AHI1-provider-citation-fetch.log` and
`/tmp/AHI1-provider-reactome-fetch.log`. Recovery design source8 is authorized
to include the finite unresolved set after those attempts finish. The synthetic
PMID:11111111 in the old bioinformatics script is an invalid-reference test
fixture, not a citation, and is excluded. No provider file, fixture or cache
has been rewritten. DRAFT status therefore reflects both the unused-provider
advisory and these explicitly separated source gates.
