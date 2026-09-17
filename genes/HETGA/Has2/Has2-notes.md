# Has2 (naked mole rat, *Heterocephalus glaber*) — research notes

UniProt **G5AY81** (HYAS2_HETGA), Swiss-Prot *reviewed*, 552 aa, NCBI taxon 10181.
GOA: 28 rows collapsing to 24 unique (term, evidence, reference) entries. **Every row is
electronic**: ISS (GO_REF:0000024, from human Q92819, mouse P70312, rat O35776) or IEA
(GO_REF:0000044 SubCell, GO_REF:0000118 TreeGrafter, GO_REF:0000120 combined). There are
no experimental GO annotations on this protein.

## 1. What the naked-mole-rat literature establishes about *this* protein

### 1.1 It is a hyaluronan synthase — demonstrated on the NMR protein itself

The single most important fact for this review is that GOA's evidence codes **understate**
what is known. Tian et al. cloned the NMR *HAS2* cDNA and expressed it heterologously:

> [PMID:23783513 "Indeed, when the cDNA for the naked mole-rat HAS2 was overexpressed in human HEK293 cells, they began secreting HMW-HA"]

Methods confirm this is a direct assay of the product of the NMR coding sequence in a
heterologous host:

> [PMID:23783513 "HEK293 cells were transfected with an expression vector containing HAS2 under the CMV promoter and allowed to express HAS2 for 2 days, after which HA secreted into the media was analyzed by pulse-field gel."]

That is **IDA-grade evidence for GO:0050501 hyaluronan synthase activity on G5AY81**, not
an ortholog projection. Independently, loss of function in NMR cells abolishes the product:

> [PMID:23783513 "We then generated H-Ras V12 and SV40 LT expressing naked mole-rat cells, in which HMW-HA was abolished by either integrating shRNA targeting HAS2"]

which is **IMP-grade evidence for GO:0030213 hyaluronan biosynthetic process**. The
functional consequence:

> [PMID:23783513 "This experiment establishes HMW-HA, produced by HAS2, as a key component responsible for the elevated cancer resistance of the naked mole-rat."]

The gain-of-function complement was later done in a whole animal — a transgenic mouse
carrying the NMR gene:

> [PMID:37612507 "nmrHas2 mice showed an increase in hyaluronan levels in several tissues, and a lower incidence of spontaneous and induced cancer, extended lifespan and improved healthspan."]
> [PMID:37612507 "analysis using pulse-field gel electrophoresis showed that hyaluronan extracted from the tissues of nmrHas2 mice was more abundant and had a higher molecular mass in the muscle, heart, kidneys and small intestine"]

So the core MF and BP are supported by NMR-specific gain-of-function (heterologous cells
and transgenic mice) *and* loss-of-function (shRNA in NMR fibroblasts). This is unusually
strong for a species with essentially no experimental GOA coverage.

### 1.2 Sequence: two Asn→Ser substitutions in the catalytic loop

> [PMID:23783513 "Two Asparagines that are 100% conserved among mammals were replaced with Serines in the naked mole-rat HAS2."]
> [PMID:23783513 "The conserved regions carrying Asparagine to Serine substitutions correspond to the cytoplasmic loop containing the enzyme’s active site."]

Comparative work refines this: one of the two is not NMR-private, and the gene is otherwise
strongly constrained across mammals:

> [PMID:25948568 "Comparative screening revealed that one of the two putatively important HAS2 substitutions in the NMR predicted to have a significant effect on hyaluronan synthase function was uniquely shared by all African mole-rats."]
> [PMID:25948568 "we found evidence of strong purifying selection acting on the HAS2 gene across all mammals, and the NMR remains unique in its particular HAS2 sequence"]

The purifying-selection result matters for curation: it is a positive argument that the
conserved, ancestral functions of HAS2 (catalysis, ECM output, the developmental roles) are
**retained** in the NMR, and that the NMR difference is a refinement on top, not a
replacement.

### 1.3 Expression is elevated, and degradation is slow

> [PMID:23783513 "Naked mole-rat skin fibroblasts overexpressed HAS2, the enzyme responsible for the synthesis of HMW-HA in comparison with mouse and human fibroblasts"]
> [PMID:38052795 "NMR and DMR had dramatically higher HAS2 expression."]
> [PMID:37612507 "Has2 mainly produces HMM-HA and shows higher expression in naked mole-rats compared with in mice and humans"]

The HA phenotype is a two-sided balance — synthesis up, catabolism down. The catabolic side
is not Has2's doing:

> [PMID:39009271 "Thus, unlike mTMEM2, nmrTMEM2 is not a physiological hyaluronidase."]
> [PMID:38158036 "This phenomenon in NMRs is attributed to a higher processing and production capacity by some of their hyaluronan synthases, along with lower degradation by certain hyaluronidases."]

### 1.4 Polymer length — the property that matters, and the one that is disputed

HAS isoenzymes differ systematically in the length of the polymer they extrude, and HAS2 is
the long-polymer synthase. This is generic mammalian biology, not an NMR peculiarity:

> [PMID:38052795 "HAS1 and HAS3 synthesize polymers of relatively smaller size, while HAS2 synthesizes the longer polymers"]
> [PMID:33846452 "the medium of mouse Has1 and Has3 transfectants contains HA with broad MW ranging from 0.2 to 2.0 MDa, while Has2 transfectants secrete very large HA with average MW > 2 MDa, possibly around 4 MDa"]

The original NMR claim:

> [PMID:23783513 "the HA secreted by naked mole-rat cells has a molecular weight of 6–12 MDa, while mouse and guinea pig HA ranges from 0.5–3 MDa"]

**This magnitude is genuinely contested.** Del Marmol et al. re-measured by size-exclusion
chromatography *and* gel electrophoresis and could not reproduce it:

> [PMID:33846452 "We could not find ultra-high molecular weight HA (≥ 4 MDa) in NMR samples, in contrast to previous descriptions."]
> [PMID:33846452 "NMR had larger amounts and higher molecular weight (maximum, around 2.5 MDa) of HA in serum and almost all tissues tested"]

The consensus "myths" review adjudicates in favour of the *qualitative* claim while
rejecting the *quantitative* one:

> [PMID:34476892 "Naked mole‐rat hyaluronan is larger than hyaluronan from several other mammals examined and has unusual material properties."]
> [PMID:34476892 "A recent analysis has demonstrated that naked mole‐rat hyaluronan has a high average molecular weight, but not greater than 2.5 MDa, whether from tissue or cell supernatant"]
> [PMID:34476892 "Results may differ among research groups due to hyaluronan molecular weight being affected by the isolation procedure."]

It also flags that the mechanistic link from the two substitutions to processivity is not
established:

> [PMID:34476892 "it is unclear how the two mutations in the conserved catalytic core of the naked mole‐rat hyaluronan synthase 2 (HAS2) enzymes could lead to higher molecular weight, as a variety of sizes was produced when naked mole‐rat HAS2 was expressed in cancer cells."]

Direct evidence that HAS2 *sequence* (not just expression level) sets polymer length does
exist in a sister subterranean species:

> [PMID:38052795 "Strikingly, even when equal amount of mouse and BMR HAS2 were transfected, the size of HA secreted by BMR HAS2-expressing cells was still larger than that secreted by mouse HAS2-expressing cells"]
> [PMID:38052795 "These results suggest that the sequence changes and differential expression levels of HAS2 contribute to accumulation of HMM-HA in subterranean species."]

Why length matters biologically (and therefore why it deserves an ontology term):

> [PMID:32398747 "vHMM-HA (>6.1 MDa) has superior cytoprotective properties compared to the shorter HMM-HA."]
> [PMID:32398747 "It protects not only NMR cells, but also mouse and human cells from stress-induced cell-cycle arrest and cell death in a polymer length-dependent manner."]

**Curation stance taken:** I describe the NMR product as *unusually long / very-high-molecular-
mass* and cite both the 6–12 MDa and the ≤2.5 MDa measurements, rather than asserting either
number as settled. The GO annotations at stake (GO:0050501, GO:0030213) do not depend on the
magnitude, only on the qualitative fact that HAS2 makes HA, which is not in dispute.

### 1.5 Downstream material and tissue consequences

> [PMID:31036852 "In common with mouse HA, NMR HA forms a range of assemblies corresponding to a wide distribution of molecular weights."]
> [PMID:31036852 "Unlike HA that is commercially available, NMR HA readily forms robust gels without the need for chemical cross-linking."]
> [PMID:33112509 "Our study shows that NMRs are remarkably resistant to OA, and this resistance is likely conferred by high molecular weight HA."]

These support GO:0085029 extracellular matrix assembly as a real, direct downstream process
for HAS2 output, but they are properties of the *polymer*, not of the *enzyme*, so they
inform the BP annotation rather than adding new MF claims.

## 2. The decisive finding: the renal annotations do not survive contact with NMR data

`GO:0035810 positive regulation of urine volume` and `GO:0070295 renal water absorption` are
ISS transfers from **rat** Has2 (UniProtKB:O35776). Both are organ-level renal-physiology
terms. The rat basis is medullary interstitial HA:

> [PMID:33846452 "HA content in the mouse and rat renal medulla is known to be much higher than in the cortex and to increase during water loading"]
> [PMID:33846452 "The role of this interstitial HA is likely to reduce water reabsorption and allow the excretion of diluted urine"]

Del Marmol et al. quantified HA in NMR kidney cortex and medulla separately, and the renal
medulla is the **single tissue where the NMR runs against the species trend**:

> [PMID:33846452 "The only exception is the renal medulla, in which HA content appeared lower in NMR than the other species."]
> [PMID:33846452 "The renal medulla average HA content we found in the NMR (150 µg/g dry weight) is closer to that of desert gerbils"]
> [PMID:33846452 "In the kidney, our results show a very similar HA localization between NMR, GP, and mice tissues"]
> [PMID:33846452 "The NMR has no access to free water but shows only a moderate, not very high, kidney concentrating ability"]

and, importantly, the authors say the actual physiological test has never been done in NMR:

> [PMID:33846452 "we do not know how the NMR renal medullary HA content would respond to water loading"]

There is a countervailing observation from the original paper, based on whole-kidney alcian
blue rather than quantitative cortex/medulla assay:

> [PMID:23783513 "Naked mole-rat skin, heart, brain and kidney were highly enriched for HA"]

and the transgenic mouse does raise kidney HA when the NMR gene is expressed
[PMID:37612507 "...more abundant and had a higher molecular mass in the muscle, heart, kidneys and small intestine"], but that is a mouse kidney driven by a CAG promoter, not NMR renal
physiology.

**Conclusion:** the rat organ-physiology terms are transferred on sequence similarity alone,
into a species whose renal medullary HA is the one measurement that does *not* follow the NMR
pattern and whose urine-concentrating physiology is explicitly described as unremarkable. This
is not enough to call the function contradicted — HA is present in the NMR medulla around the
vasa recta [PMID:33846452 "In the kidney medulla, HA is found mainly around the vasa recta"] —
but it is enough to call the transfer an over-annotation. Both get
`MARK_AS_OVER_ANNOTATED`, not `REMOVE`, with the resolving experiment named (a water-loading
protocol with medullary HA quantification and urine osmolality).

## 3. Cardiac / vascular development terms (mouse-derived)

`GO:0001570 vasculogenesis`, `GO:0036302 atrioventricular canal development`, and
`GO:0090500 endocardial cushion to mesenchymal transition` come by ISS from mouse Has2
(UniProtKB:P70312), grounded in mouse *Has2* knockouts. There is no NMR-specific evidence
for or against them. Two things argue for retaining rather than deleting:

1. Strong purifying selection on HAS2 across mammals [PMID:25948568 "we found evidence of
   strong purifying selection acting on the HAS2 gene across all mammals, and the NMR remains
   unique in its particular HAS2 sequence"] — the ancestral developmental role is very
   unlikely to have been lost.
2. The NMR's HA phenotype is explicitly **postnatal**, i.e. the embryonic behaviour of the
   enzyme is not the divergent part: [PMID:37612507 "In the naked mole-rat, HMM-HA begins to
   accumulate postnatally"].

But they are developmental processes of a pleiotropic ECM enzyme, not what HAS2 is *for* in
the NMR, so they are `KEEP_AS_NON_CORE`.

## 4. Localizations

HAS enzymes are polytopic plasma-membrane proteins that polymerise HA on the cytoplasmic face
and extrude it directly outward:

> [PMID:33846452 "Three HA synthase isoforms (HAS1, HAS2, and HAS3), present in all mammals, synthesize HA at different rates, directly from the inner aspect of the plasma membrane into the extracellular matrix, and with different average sizes."]

So `GO:0005886 plasma membrane` is the functional site (ACCEPT, core). The remaining CC terms
(`GO:0005789` ER membrane, `GO:0000139` Golgi membrane, `GO:0005794` Golgi apparatus,
`GO:0005764` lysosome, `GO:0031982` vesicle, `GO:1903561` extracellular vesicle) are all
trafficking-itinerary compartments taken from the human SubCell record; UniProt itself
describes them as a route ("Travels from endoplasmic reticulum (ER), Golgi to plasma membrane
and either back to endosomes and lysosomes, or out into extracellular vesicles"). None has
NMR-specific support. They are kept as non-core, with two term-level fixes:

- `GO:0005794 Golgi apparatus` → MODIFY to `GO:0000139 Golgi membrane`: HAS2 is a seven-pass
  membrane protein (UniProt FT TRANSMEM ×7), so the membrane term is the informative one, and
  it is already annotated from the same donor.
- `GO:0000271 polysaccharide biosynthetic process` → MODIFY to `GO:0030213 hyaluronan
  biosynthetic process`. Verified against QuickGO: GO:0000271 sits under
  GO:0016051 carbohydrate biosynthetic process / GO:0005976 polysaccharide metabolic process,
  whereas GO:0030213 sits under GO:0006024 glycosaminoglycan biosynthetic process /
  GO:1901137 carbohydrate derivative biosynthetic process. GO:0000271 is **not** an ancestor
  of GO:0030213 — it is a parallel, less-informative branch, and the specific term is already
  annotated from the same donor set.

## 5. GO term gap: no term for high-molecular-mass hyaluronan biosynthesis

Re-verified independently (QuickGO `/ontology/go/terms/<id>/complete` plus a text search of
the whole ontology). GO contains exactly **eight** hyaluronan terms:

| GO id | name |
|---|---|
| GO:0030212 | hyaluronan metabolic process |
| GO:0030213 | hyaluronan biosynthetic process |
| GO:0030214 | hyaluronan catabolic process |
| GO:0050501 | hyaluronan synthase activity |
| GO:0005540 | hyaluronic acid binding |
| GO:1900125 | regulation of hyaluronan biosynthetic process |
| GO:1900126 | negative regulation of hyaluronan biosynthetic process |
| GO:1900127 | positive regulation of hyaluronan biosynthetic process |

`GO:0030213` has **no `is_a` children at all** (only the three `regulates` children above),
and none of the eight carries a `secondaryIds` entry, so no HMM-HA term has been merged away
either. The absence is real.

Since the biologically decisive variable is polymer length — HAS1/HAS3 short vs HAS2 long as
a general mammalian rule, and length-dependent cytoprotection as a measured effect — a child
of GO:0030213 is proposed. Note this is *not* an NMR-specific request: it would apply to
mammalian HAS2 generally, with the NMR simply being the extreme case.

I considered proposing the distinction at MF level instead (a "high-molecular-mass hyaluronan
synthase activity" child of GO:0050501), since processivity is an intrinsic enzyme property.
I did not, because GO MF terms for glycosyltransferases are defined by the reaction and the
reaction is identical regardless of product length; and because the NMR phenotype demonstrably
depends on the synthesis/degradation *balance*, which is a process-level property. This is
flagged as an open question for the ontology editors rather than settled here.

## 6. What the affinage human-ortholog record missed

`Has2-deep-research-affinage-human-ortholog.md` is the Affinage record for **human HAS2
(Q92819)**, used here only as a conserved-mechanism baseline. It is good on human mechanism
(AMPK Thr-110 phosphorylation, K190 ubiquitination, Ser-221 O-GlcNAc, HAS1/HAS3 heteromers,
ATG9A-dependent autophagic turnover, the transcriptional inputs), and its 32 citations are
plausible. But measured against what this review actually needed:

- **It contains exactly one naked-mole-rat citation**, PMID:37612507 (the transgenic mouse),
  and even that is framed as a human-HAS2 finding. It does **not** cite PMID:23783513, the
  paper that cloned the NMR gene and did the heterologous-expression experiment — i.e. it
  misses the single piece of evidence that turns this gene's core MF from an ortholog
  projection into a species-specific direct assay. That is the decisive omission.
- It misses the entire size controversy (PMID:33846452, PMID:34476892) and therefore would
  have led to over-claiming 6–12 MDa as settled fact.
- It misses PMID:25948568 (purifying selection + the substitution being shared across African
  mole-rats), which is what licenses keeping the mouse developmental terms.
- It says nothing about renal HA physiology, so it gives no purchase at all on the two rat-
  derived annotations that are the hardest calls in this review.
- Its `mechanism_profile` grounds the MF at `GO:0016740 transferase activity` — three levels
  above the correct `GO:0050501`. As instructed, none of its GO ids were imported.

This is the expected failure mode for a human-only provider on a species-divergence question:
correct conserved mechanism, zero coverage of what makes the ortholog interesting.

## 7. Unresolved

- Whether the two Asn→Ser substitutions are *causally* responsible for longer polymer, as
  opposed to expression level plus low hyaluronidase activity. PMID:34476892 says explicitly
  this is unclear; the closest positive evidence is from blind mole-rat HAS2, not NMR
  [PMID:38052795 "Strikingly, even when equal amount of mouse and BMR HAS2 were transfected,
  the size of HA secreted by BMR HAS2-expressing cells was still larger than that secreted by
  mouse HAS2-expressing cells"].
- The actual maximum molecular mass of NMR HA (6–12 MDa vs ≤2.5 MDa). Two labs, two methods,
  no reconciliation; the myths review attributes the discrepancy to isolation procedure.
- Whether NMR renal medullary HA responds to water loading as in rat — the experiment that
  would decide GO:0035810 / GO:0070295.
- Whether the developmental phenotypes of mouse *Has2* knockouts have any NMR counterpart. No
  NMR embryology on this gene exists; the terms are retained as non-core on conservation
  grounds, not on evidence.

## 8. Curation outcome and one deliberately-left warning

Action counts across the 24 unique GOA entries (28 GOA rows; the seeding key omits WITH/FROM,
so the three GO:0050501 ISS rows, the two GO:0030213 ISS rows and the two GO:0005886 ISS rows
each collapse into one entry — no distinct GO term is lost):

| action | n | terms |
|---|---|---|
| ACCEPT | 8 | GO:0050501 ×2, GO:0030213 ×2, GO:0085029 ×2, GO:0005886 ×2 |
| KEEP_AS_NON_CORE | 12 | GO:0000139 ×2, GO:0005764 ×2, GO:0005789 ×2, GO:0031982 ×2, GO:1903561, GO:0001570, GO:0036302, GO:0090500 |
| MODIFY | 2 | GO:0005794 → GO:0000139; GO:0000271 → GO:0030213 |
| MARK_AS_OVER_ANNOTATED | 2 | GO:0035810, GO:0070295 |
| REMOVE / UNDECIDED | 0 | — |

### The evidence-code recommendation that could not be encoded

I initially added two `action: NEW` entries recording that this protein qualifies for
experimental annotations — `GO:0050501` **IDA** and `GO:0030213` **IMP**, both against
PMID:23783513 — because GOA currently holds *no* PMID-backed annotation on G5AY81 at all,
despite the heterologous-expression and shRNA-knockdown experiments. The best-practices
validator rejects `NEW` for any term already present in GOA regardless of evidence code
("Annotation with action=NEW exists in GOA: GO:0030213"), so both were removed and the
recommendation now lives in the `review.reason` of the corresponding ACCEPT rows.

This is a genuine expressivity gap in the review format, worth flagging: there is currently no
way to say "this term is correctly annotated but the evidence code understates the evidence
available for *this species*." For a species like the naked mole rat, where the entire GOA is
electronic, that is exactly the recommendation a curator most wants to make.

### Warning left in place

`just validate HETGA Has2` reports **✓ Valid (with 1 warnings)**; term validation and reference
validation both pass cleanly (all 47 `supporting_text` quotes verified as verbatim substrings
before writing, and reference titles copied verbatim from the cache).

The remaining warning is `no_deep_research_results`: "No annotations reference available deep
research files". Satisfying it requires a `supported_by` entry whose `reference_id` is the
`file:` deep-research path — i.e. quoting an Affinage sentence as `supporting_text`. The brief
forbids that ("never quote an affinage sentence as supporting_text for a mechanistic claim — a
provider sentence is a lead, not evidence"), and the Affinage record here is about the *human*
ortholog, so any such quote would also be evidence about the wrong species. The record's
provenance is instead recorded properly via `additional_reference_ids` on the two annotations
whose reasons draw on it (GO:0005789, GO:0005764) and on GO:0050501, plus a full
`reference_review`. The warning is left standing deliberately.
