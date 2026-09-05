# Cd44 (Heterocephalus glaber, A0AAX6R0R7) — review notes

Reviewer journal for the GO annotation review. Every assertion below carries provenance.
UniProt entry: `A0AAX6R0R7_HETGA`, 701 aa, TrEMBL, `PE 4: Predicted`, derived from RefSeq
model `XP_012930388.1`. 38 GOA rows, all IEA; **zero experimental annotations**, in line
with the species-wide picture.

---

## 1. What the naked-mole-rat literature actually establishes about this protein

### 1.1 CD44 is a functional hyaluronan receptor in naked mole-rat cells — established

This is the one place where NMR-specific, on-the-protein evidence exists, and it is good.

Tian et al. 2013 blocked CD44 on intact NMR cells with an antibody and got a
proliferation phenotype:

> [PMID:23783513 "To confirm that HA signaling triggers ECI via the CD44 receptor we
> cultured naked mole-rat cells in the presence of a CD44-blocking antibody. Naked
> mole-rat cells grown with CD44 antibodies reached a higher cell density (Figure 3b)
> indicating that the ECI signal from HMW-HA is in part transmitted via the CD44
> receptor."]

The same blockade removes the transformation barrier:

> [PMID:23783513 "Similarly, naked mole rat cells cultured in the presence of CD44
> blocking antibody formed colonies in soft agar (Supplementary Figure 6)."]

and the authors place CD44 in a defined axis:

> [PMID:23783513 "Collectively these results establish that ECI is controlled by the
> HA/CD44/NF2 pathway."]

with the cytoplasmic partner named explicitly:

> [PMID:23783513 "On the cytoplasmic face, the CD44 receptor interacts with NF2 (merlin),
> which mediates contact inhibition17."]

The HA-affinity FACS assay is a **whole-cell** measurement, not a CD44-specific one, and
I have been careful not to over-read it:

> [PMID:23783513 "Naked mole-rat cells displayed a two-fold higher affinity to HA than
> mouse or human cells (Figure 3d), which can contribute to higher sensitivity of naked
> mole rat cells to HA signaling."]

The methods make the assay design explicit — fluorescein-labelled bovine HA on whole
cells read by FACS — so the two-fold difference is attributable to the cell surface as a
whole (CD44 plus RHAMM, LYVE1, layilin and HA synthase-tethered pericellular coat), not
to CD44 alone. It is supporting context for a CD44 hyaluronan-binding annotation, not a
direct measurement of it.

Independent restatement in a 2023 comparative-genomics paper:

> [PMID:38052795 "NMR HMM-HA triggers a signaling cascade through the membrane receptor
> CD44 and induces a p16-dependent early contact inhibition1."]

and in the "myths" review, which is careful to note the pathway is **not** classical
cell-contact-dependent inhibition:

> [PMID:34476892 "naked mole‐rat fibroblasts secrete abundant hyaluronan into the culture
> medium which increases its viscosity and arrests cell proliferation before cells reach
> confluence via cluster of differentiation 44 (CD44) receptor signalling"]

> [PMID:34476892 "Frequent medium changes remove this hyaluronan and result in confluent
> cell culture with naked mole‐rat cells attaining higher densities than observed for
> mouse cells, suggesting that contact inhibition is not a cell autonomous process"]

**Curation consequence.** The proliferation phenotype is real and CD44-dependent, but the
mechanism is a *soluble/pericellular* hyaluronan signal read at the cell surface, not
information transmitted "by direct cell-cell contact" as GO:0060242 `contact inhibition`
requires. I therefore proposed `GO:0008285 negative regulation of cell population
proliferation` as the NEW annotation rather than a contact-inhibition term. This is a
small but real ontology-fit issue and I recorded it as a suggested question.

### 1.2 The proteostasis arm: CD44 acts in the ER and raises basal ATF6 output

Takasugi et al. 2023 is the most important paper for this review and proposes a CD44
function that is nowhere in the projected GOA set. Crucially, part of the work is done
**in naked mole-rat cells with naked mole-rat CD44**, so it is not merely a cross-species
inference:

> [PMID:37708026 "Indeed, NMR OPCs showed higher resistance against an ER stress inducer,
> tunicamycin, compared with mouse OPCs in a manner dependent on CD44."]

> [PMID:37708026 "In addition, overexpression of mouse or NMR CD44 enhanced tunicamycin
> resistance in mouse OPCs (Figures 3J and 3K)."]

> [PMID:37708026 "In the genes that were downregulated by CD44 knockdown, most of the
> overrepresented terms were associated with the ER, unfolded protein response (UPR)/ER
> stress, and the UPR regulator ATF6 (Figure 3E)."]

> [PMID:37708026 "NMR OPCs and U2OS cells also exhibited ER localization of CD44 (Figures
> S6D and S6E)."]

> [PMID:37708026 "High expression of CD44 was confirmed at protein levels in expanded and
> freshly isolated NMR OPCs (Figures 3A and S2D)."]

The overall claim, and its explicit hyaluronan-independence:

> [PMID:37708026 "CD44 modifies proteome and membrane properties of the ER and enhances ER
> stress resistance in a manner dependent on unfolded protein response regulators without
> the requirement of HA."]

> [PMID:37708026 "We found that CD44 localizes to the endoplasmic reticulum (ER) and
> enhances basal ATF6 activity."]

The sufficiency experiment is done in human CD44-KO cells but is mechanistically
decisive: an ER-retained CD44 ectodomain reproduces the effect, so the function is
exerted from inside the ER rather than from the plasma membrane.

> [PMID:37708026 "CD44-ectodomain-KDEL enhanced the expressions of HSP90B1 and HSPA5 and
> cellular resistance to tunicamycin in CD44 KO U2OS cells (Figures 7F and 7G)"]

**How much of this is NMR-specific?** Honest answer: the *mechanism* is presented as
general mammalian biology (IMR90 human fibroblasts, U2OS, mouse OPCs), and the
NMR-specific claim is one of **expression level**, not of a different protein activity —
CD44 is unusually highly expressed in NMR OPCs and CD44 expression correlates with maximum
lifespan across mammals:

> [PMID:37708026 "expression levels of CD44, an ECM-binding protein that has been suggested
> to contribute to NMR longevity by mediating the effect of hyaluronan (HA), are not only
> high in OPCs of long-lived species but also positively correlate with longevity in
> multiple cell types/tissues."]

So the correct framing for the review is: this is a **conserved CD44 function that the
naked mole rat uses more of**, not a naked-mole-rat-specific invention. That is enough to
justify NEW annotations on the NMR protein, because the loss-of-function experiment was
done on NMR CD44 in NMR cells.

**Ontology fit is imperfect.** The paper is explicit that the effect is on *basal* ATF6
tone, not on the stress-induced UPR:

> [PMID:37708026 "Taken together, CD44 promotes basal ATF6 activity but does not affect UPR
> gene expressions once exposed to strong ER stress."]

`GO:1903893 positive regulation of ATF6-mediated unfolded protein response` is the closest
existing term and I used it, but it does not distinguish setting the basal tone of a
sensor from amplifying its stress response. Recorded as a proposed new term and as a
knowledge gap.

### 1.3 What naked-mole-rat hyaluronan does *to* CD44 — and why it matters for GOA

The 2020 cytoprotection paper establishes that CD44 is the receptor through which NMR
very-high-molecular-mass HA acts:

> [PMID:32398747 "Knockdown of RHAMM did not block the cytoprotective effect of NSF-HA,
> whereas CD44 siRNA as well as a CD44 neutralizing antibody abrogated its effect"]

**Important caveat I kept in front of me throughout:** these experiments put *NMR
hyaluronan* onto *human IMR90 cells*, so the receptor tested is human CD44. The paper is
evidence about the ligand's species-specific properties, not about the NMR receptor
protein. The key mechanistic result is a **negative** one for several projected
annotations:

> [PMID:32398747 "These results show that CD44 protein-protein interactions are promoted
> by HMM-HA but are suppressed by vHMM-HA."]

i.e. the very-high-mass hyaluronan that NMR tissue is full of *suppresses* CD44
clustering and CD44 protein-protein interactions rather than driving them. A review of
NMR hyaluronan restates this:

> [PMID:33846452 "very-HMW HA molecules (> 6 MDa) bind CD44 and thus reduce the binding of
> CD44 with other proteins, leading to a partial attenuation of p53 and its target genes"]

This bears directly on the receptor-clustering-dependent outputs projected from human —
ERK activation, migration, endocytic uptake — and is the main reason several of those are
marked non-core rather than accepted.

### 1.4 CD44 ectodomain shedding is absent in NMR fibroblasts

> [PMID:36790936 "we observed an absence of ADAM10 mediated CD44 cleavage, as well as
> shedding of exogenous and overexpressed betacellulin in NPSF, whereas in mouse primary
> skin fibroblasts ionomycin induced ADAM10-dependent cleavage of both CD44 and
> betacellulin."]

This is **abstract-only** (`full_text_available: false`), so I have not quoted any method
detail beyond what the abstract states. Two things it does establish and one it does not:

- It establishes that stimulated ADAM10-dependent CD44 cleavage does not occur in NMR
  primary skin fibroblasts, while it does in mouse.
- It establishes the cause is **upstream of CD44** — a cell-level phosphatidylserine
  externalisation deficit, not a change in CD44 itself:
  > [PMID:36790936 "increased phosphatidylserine (PS) externalization, which rescued the
  > ADAM10 sheddase activity and promoted cell migration in NPSF in an ADAM10-dependent
  > manner."]
- It does **not** establish that NMR CD44 is never shed: one cell type, one stimulus
  (ionomycin), one sheddase; MT1-MMP and other proteases also shed CD44 in other systems.

**Curation consequence.** This is a positive, NMR-specific argument for downgrading
`GO:0005576 extracellular region` (which for a type-I membrane protein means the shed
soluble ectodomain) and for treating the migration/lamellipodium cluster as non-core. It
is not enough for `REMOVE`, because the defect is demonstrably in the cell, not in the
protein, and is rescuable.

A separate, independent line of speculation points the same way — that the material
properties of NMR hyaluronan may themselves protect the receptor from cleavage:

> [PMID:31036852 "The main HA receptor is CD44, a cell surface adhesion receptor that binds
> a range of ligands and is itself associated with metastasis12."]

(that paper's cleavage discussion is explicitly speculative and I did not use it as
evidence).

### 1.5 Hyaluronan catabolism in the naked mole rat runs backwards from the human case

Two independent NMR results:

> [PMID:23783513 "HAase activity of the naked mole-rat cells was much lower than that of
> human, mouse or guinea pig cells (Figure 2c)."]

> [PMID:39009271 "Naked mole-rats (NMRs) accumulate abundant high-molecular weight
> hyaluronan (HA) in their tissues, suggesting decreased HA degradation."]

(the TMEM2 paper is abstract-only; it reports that NMR TMEM2 carries Asn247/Val302 in
place of the catalytic His/Ala and is inactive.)

**Curation consequence.** `GO:0030214 hyaluronan catabolic process` was projected from
human, where CD44 is the *receptor* that routes HA to HYAL1/HYAL2 (PMID:17170110), not an
enzyme. In the naked mole rat, the defining tissue phenotype is hyaluronan **accumulation**
through reduced degradation. Projecting a catabolic-process role onto NMR CD44 is exactly
the kind of transfer this species falsifies. Marked over-annotated (not removed — nobody
has tested whether NMR CD44 internalises HA).

### 1.6 The naked mole rat lacks NK cells

> [PMID:34476892 "These findings are further supported by studies that their immune cell
> populations lack natural killer cells, the cells responsible for immune surveillance and
> eradication of virally infected cells (Hilton et al., 2019)."]

Note the term actually projected is `GO:0051132 NK T cell activation`, which by definition
concerns natural killer **T** cells, a distinct αβ-TCR lineage. I did not conflate the two:
the cached literature says NMRs lack NK cells and says nothing about their NKT compartment.
What tips this row to over-annotated is the combination of (a) no NMR evidence, (b) an
atypical NMR NK/lymphoid compartment, and (c) a term-scoping question at the *source*
(below).

---

## 2. Sequence analysis performed for this review

Written up in [`Cd44-bioinformatics/RESULTS.md`](Cd44-bioinformatics/RESULTS.md), script
`cd44_isoform_architecture.py`. Two questions the UniProt record could not answer.

**(a) Is the 701-aa entry a particular isoform?** The TrEMBL record carries no
`ALTERNATIVE PRODUCTS` and no `VAR_SEQ`, so no isoform identity can be read off it — and I
have not asserted one. What the alignment to human P16070-1 does show is architectural:
86.3% (270/313) of the human alternatively spliced insert (residues 223–535, the segment
missing from the short human isoform 11/CD44R2) has an aligned counterpart in the NMR
protein, and the NMR ectodomain is 588 residues versus 629 for the full-length human
canonical form. So the **RefSeq gene model chosen as the reference protein encodes a long,
variant-exon-containing (CD44v-like) form**, not the short standard CD44s. That is a
statement about the gene model, not about what NMR tissues express — no cached study
reports NMR CD44 splice usage, and this remains a genuine gap.

Does it matter for annotation? Only marginally, and I said so rather than inventing a
consequence:
- The Link/hyaluronan-binding module sits in the invariant N-terminal region present in
  every isoform, so `GO:0005540` is unaffected by splice form.
- Variant exons are where isoform-specific co-receptor functions live in human CD44
  (heparan-sulfate-bearing v3 presenting growth factors; v6 in MET signalling), so a
  variant-containing model is at least architecturally compatible with
  `GO:0044344 cellular response to fibroblast growth factor stimulus`. That is an argument
  about capability, not evidence, and I did not use it to accept the annotation.
- The variant stem is the least conserved region (74.1% identity vs 92.1% for the Link
  domain and 97.2% for the cytoplasmic tail), which is what one expects for a mucin-like
  O-glycosylated spacer.

**(b) Does the UniProt `CAUTION` undermine hyaluronan binding?** The entry says
[file:HETGA/Cd44/Cd44-uniprot.txt "Lacks conserved residue(s) required for the propagation
of"] feature annotation, cited to PROSITE-ProRule PRU00323. PRU00323 is the Link-domain
rule (trigger PS50963 `LINK_2`), and its only feature output is two `DISULFID` bonds
gated on a `C-x*-C` condition — so the flag concerns automatic **feature propagation**,
not function. Mapping the human landmarks through the alignment shows the residues that
matter are all present:

| Human | NMR | role (UniProt P16070 feature table) |
|---|---|---|
| R41 | R43 | hyaluronan binding |
| R78 | R80 | hyaluronan binding |
| Y79 | Y81 | hyaluronan binding |
| Y105 | Y107 | hyaluronan binding |
| C28/C129, C53/C118, C77/C97 | C30/C132, C55/C120, C79/C99 | three Link-region disulfides |

Link domain identity to human is 92.1%. So the `CAUTION` is not evidence against
`GO:0005540`, and I recorded that explicitly so a later reader does not mistake it for one.

---

## 3. What the affinage human-ortholog record contributed, and what it missed

`Cd44-deep-research-affinage-human-ortholog.md` is an Affinage record for **human CD44
(P16070)**, fetched deliberately as a conserved-mechanism baseline; its frontmatter and
heading both say `human`. I used it only for mechanism, never as evidence about the naked
mole rat, and I did not import its `mechanism_profile` GO ids.

**What it gave me.** A clean mechanistic spine for the conserved protein: HA endocytosis
to lysosomes with no intrinsic catalytic activity (PMID:1370836); glycosylation-gated,
avidity-based HA recognition (PMID:8601595, PMID:10871609); ADAM10 shedding followed by
γ-secretase release of CD44-ICD (PMID:14623895, PMID:15596040); IQGAP1/RhoA/Syk coupling
via the cytoplasmic tail. The ADAM10 entry in particular is what let me read
PMID:36790936 correctly — knowing that ADAM10-dependent shedding is a canonical,
ligation-and-Rac1-augmented CD44 step made the NMR "absence of shedding" result
interpretable rather than isolated.

**What it missed — and this is the substantive recall finding.** The affinage record does
**not** contain the ER/ATF6/proteostasis function at all. PMID:37708026 is absent from its
20 citations, and its `localization` profile lists plasma membrane, nucleus and lysosome —
no ER. That is the single most consequential recent finding about CD44, it is a 2023 *Cell
Reports* paper with the gene name in the title, and it is the only line of work in which
naked-mole-rat CD44 itself was knocked down and overexpressed. Everything in §1.2, and all
three NEW annotations I proposed, come from outside the provider record.

It also misses, unsurprisingly given its human scope, the entire naked-mole-rat literature:
the CD44-blocking-antibody experiments (PMID:23783513), the vHMM-HA/CD44 interactome
inversion (PMID:32398747), and the absence of ADAM10-mediated CD44 shedding in NMR
fibroblasts (PMID:36790936).

A smaller point of tension worth recording: the affinage entry for PMID:7545465 states
that CD44 engagement inhibits anti-CD3- and dexamethasone-induced apoptosis in T cells
"but not UV-induced (p53-dependent) apoptosis". Two of the Ensembl-projected rows here
(`GO:0043518`, `GO:1902166`) assert negative regulation of p53-mediated DNA-damage
signalling. Those come from a different paper and a different cell system, but the
juxtaposition is a reason not to treat the p53 rows as core.

---

## 4. How I treated the annotation set

All 38 rows are electronic. There is no curator who read a full text on this protein, so
"do not overrule the curator" is not the binding constraint — but `REMOVE` still needs a
positive biological argument, and I did not reach that bar for any row. Nothing was
removed.

Provenance of the projections matters for calibration, so I traced the human source
annotations behind the `GO_REF:0000107` rows via QuickGO. They are all grounded in human
experimental annotations, and several rows share a source:

| Human source | Evidence | Rows projected to NMR |
|---|---|---|
| PMID:17045821 (MIF–CD74–CD44) | IDA | GO:0004896, GO:0035692, GO:0043518, GO:1902166, GO:0070374 |
| PMID:20962267 (podoplanin) | IDA/IMP | GO:0016324, GO:0031258, GO:0044319, GO:2000392 |
| PMID:16945930 (acylation/rafts) | IDA/IMP | GO:0038024, GO:0045121 |
| PMID:17170110 (HYAL1/2 catabolism) | IDA | GO:0030214, GO:0005540 |
| PMID:15100360 (BMP-7, renal) | IMP | GO:0034116, GO:0070487 |
| PMID:11944887 (chondrogenesis) | **IEP** | GO:0051216 |
| PMID:19577615 (bFGF, fibrosarcoma) | IDA | GO:0044344 |
| PMID:37006235 (galectin-9, NK cells) | IDA | GO:0038023, GO:0051132 |
| PMID:20522558 (cytokines, endothelium) | IMP | GO:1900625 |

Two observations fell out of that table:

1. **Five rows are one paper.** The p53 rows, the MIF receptor complex, cytokine receptor
   activity and the ERK row are not five independent lines of evidence; they are one human
   IDA study of the MIF–CD74–CD44 complex. Counting them as five is how a projected set
   manufactures apparent depth.
2. **`GO:0051216 cartilage development` rests on an IEP** — an expression-pattern
   correlation during chondrogenesis, the weakest experimental code — projected across
   species. NMR cartilage is genuinely interesting (very-high-mass HA, stiffer, strongly
   OA-resistant, PMID:33112509) but that paper attributes the protection to HA polymer
   size and tissue mechanics, not to CD44, so there is no NMR rescue for this row.

A term-scoping issue at the source, flagged rather than resolved: PMID:37006235 is titled
for **natural killer cells** but grounds `GO:0051132 NK T cell activation`, which is
defined for natural killer **T** cells. I have not read that paper's full text and do not
assert the curator erred; I record it as an unresolved concern that adds to the case for
treating the row as an over-annotation in this species.

### Renal/immune organ-physiology transfers

`GO:0034116`, `GO:0070487` and `GO:1900625` all descend from monocyte-adhesion assays in
renal-tubular or endothelial disease models. These are the classic weak transfers the
naked mole rat is most likely to break, and there is no NMR evidence for any of them.

### The two `GO_REF:0000108` logical inferences

These are GO-to-GO inferences with no organism evidence at all, and I treated them
differently from each other:

- `GO:0016192 vesicle-mediated transport` ← `GO:0038024 cargo receptor activity`. The
  inference is mechanically valid but lands at the top of the transport hierarchy, and it
  chains off a cargo-receptor row that the NMR hyaluronan-turnover picture already argues
  against. Over-annotated.
- `GO:0019221 cytokine-mediated signaling pathway` ← `GO:0004896 cytokine receptor
  activity`. Worth noting that the source MF row carries `contributes_to` — CD44 does not
  bind MIF, CD74 does — while the inferred BP row carries `involved_in`, so the inference
  silently upgrades a contributory role into a participatory one. The underlying biology
  (CD44 as the signal-transducing component) is real in human, so this is non-core rather
  than over-annotated.

---

## 5. What I could not resolve

- **Splice repertoire in NMR tissue.** The reference protein is a variant-exon-containing
  model, but no cached study reports which CD44 isoforms naked mole rats express, in which
  tissues, or whether NMR CD44 carries the heparan-sulfate substitution that in human v3
  supports growth-factor presentation. This is why `GO:0044344` is marked over-annotated
  rather than accepted or removed.
- **Whether NMR CD44 internalises hyaluronan at all.** The species phenotype (low
  hyaluronidase activity, catalytically dead TMEM2, HA accumulation) argues the flux is
  low, but no one has run a CD44-dependent HA-uptake assay in NMR cells. `GO:0030214` and
  `GO:0038024` are marked over-annotated on that reasoning; a direct assay could flip
  either to accepted or to removed.
- **Whether the ER/ATF6 function requires anything NMR-specific.** The mechanism as
  published is general mammalian biology used more heavily by a long-lived species. Whether
  NMR CD44 has any sequence feature that makes it a better ER modulator than mouse CD44 is
  untested — the paper's own overexpression comparison put mouse and NMR CD44 side by side
  in mouse OPCs and reported both as effective.
- **The whole immune arm.** `GO:0006954`, `GO:0042110`, `GO:2000106` and the NK row rest
  entirely on conserved-family biology. NMR immunology is atypical enough (no NK cells;
  not disease-resistant in the way folklore claims) that none of these can be confirmed or
  refuted from what is cached. They are kept non-core or marked over-annotated on the
  strength of the projection, not on NMR data.
