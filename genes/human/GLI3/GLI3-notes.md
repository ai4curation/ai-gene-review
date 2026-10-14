# GLI3 — curation notes

Research journal for the GLI3 GO annotation review. Appended to as work proceeds.

## 1. What the gene is

Human GLI3 (UniProtKB:P10071, HGNC:4319, 1580 aa in the current entry; originally reported
as 1596 aa / ~190 kDa) is a Krüppel-type C2H2 zinc-finger transcription factor of the
Ci/GLI family. The founding characterisation established both the size and the DNA-binding
activity: *"Sequence analysis of these clones and identification of the GLI3 protein by using
polyclonal antisera demonstrated that GLI3 encodes a protein of 1,596 amino acids and an
apparent molecular mass of 190 kilodaltons"* and *"Furthermore, when produced in vitro, the
GLI3 protein bound specifically to genomic DNA fragments containing GLI-binding sites"*
[PMID:2118997].

UniProt records five C2H2 zinc fingers spanning residues 480-632, a repressor domain at
1-397 and an activator domain at 827-1132, plus two chains: `PRO_0000047202` (Transcription
activator GLI3, 1-1580) and `PRO_0000406137` (Transcription repressor GLI3R, 1-?)
[file:human/GLI3/GLI3-uniprot.txt].

## 2. The two forms — the central fact about this gene

GLI3 is the one GLI paralog specialised for repression. Dai et al. drew the contrast with
GLI1 explicitly: *"GLI3 containing both repression and activation domains acts both as an
activator and a repressor, as does Ci, whereas GLI1 contains only the activation domain"*
[PMID:10075717].

Wang, Fallon & Beachy established the processing mechanism in vertebrates and, importantly,
the quantitative asymmetry: *"We demonstrate that PKA-dependent processing of vertebrate
Gli3 in developing limb similarly generates a potent repressor in a manner antagonized by
apparent long-range signaling from posteriorly localized Sonic hedgehog protein"* and *"The
high relative abundance and potency of Gli3 repressor suggest specialization of Gli3 and its
products for negative Hedgehog pathway regulation"* [PMID:10693759].

Shin et al. showed the two forms behave like Ci155 and Ci75 respectively, including in their
subcellular distribution: *"Here we show that full-length GLI3 localizes to the cytoplasm and
activates PTCH1 expression, which is similar to full-length Ci155"* and *"PHS mutant protein
(GLI3-PHS) localizes to the nucleus and represses GLI3-activated PTCH1 expression, which is
similar to Ci75"* [PMID:10077605].

**Curation consequence.** The gene-level GOA record carries only the undirected parents
GO:0003700 and GO:0000981. The curated human Hedgehog GO-CAMs are much sharper, and they
split by proteolytic product:

- `UniProtKB:P10071-PRO_0000406137` (GLI3R) → GO:0001227 / GO:0045879 / nucleus
  (`gomodel:693b3c0900000157/693b3c0900000307`)
- `UniProtKB:P10071-PRO_0000047202` (activator) → GO:0001228 / GO:0007224 / nucleus
  (`gomodel:693b3c0900001501/693b3c0900001567`)

I therefore used MODIFY on the four GO:0003700 rows to propose GO:0001228 (activation
assays) or both directional terms (the orthology row), rather than adding anything with
`action: NEW`. This keeps the proposal anchored to rows that already exist and matches the
module, which names GO:0001227 as the function of its `ci_gli_repressor` annoton and GLI3 as
the exemplar (`modules/hedgehog_signaling.yaml`).

## 3. Processing mechanism

PKA priming → CK1/GSK3 → SCF(beta-TrCP) → limited proteolysis. Wang & Li demonstrated the
adaptor step directly: *"Our gain- and loss-of-function analyses in cultured cells further
reveal that betaTrCP, the vertebrate homolog of Slimb, is required for Gli3 processing, and
we demonstrate that betaTrCP can bind phosphorylated Gli3 both in vitro and in vivo"*
[PMID:16371461]. Wen et al. confirmed this for the endogenous protein and added the
Hedgehog-dependence: *"We also confirmed that phosphorylation and betaTrCP/Cul1 are required
for endogenous Gli3 processing and that this is inhibited by Hh"* [PMID:20154143].

A second, distinct ubiquitin route destroys rather than processes: SPOP/CUL3 reads Ser/Thr-rich
degrons — *"We find that similar S/T-rich motifs are present in Gli proteins as well as in
numerous HIB-interacting proteins and mediate Gli degradation by SPOP"* [PMID:19955409].

Reactome models the whole cassette at the ciliary base (R-HSA-5610720, -5610722, -5610732,
-5610746, -5610754), which is where the six ciliary-base TAS rows come from. GO-CAM
`693b3c0900000157` models the same steps with PKA, GSK3B, BTRC and RBX1.

## 4. Repression mechanisms — two of them

1. **SKI-bridged deacetylase recruitment.** *"Here we report that the Ski corepressor binds
   to Gli3 and recruits the histone deacetylase complex"*, with direct co-IP: *"Gli3 Rep was
   efficiently coprecipitated with HDAC1, indicating that HDAC1 and GLI3 Rep associate with
   one another"*, and a functional requirement: *"The Gli3-mediated repression was impaired
   by anti-Ski antibody and in Ski-deficient fibroblasts"* [PMID:12435627]. This is also the
   grounding for the transcription-repressor-complex (GO:0017053) row, whose mouse source is
   an IDA from this same paper.

2. **An HDAC-independent repressor domain.** *"Overexpression studies confirm that the
   N-terminal parts harbor gene repression activity and we mapped the minimal repressor to
   residues 106 till 236 in Gli3"* [PMID:19084012]. The paper explicitly separates this from
   the HDAC route.

## 5. Activation mechanism

CBP: *"Transcriptional co-activator CBP binds to GLI3, but not to GLI1"*, and the functional
read-out *"GLI3 directly binds to the Gli1 promoter and induces Gli1 transcription in
response to Shh"* [PMID:10075717].

Mediator: *"We show that Gli3 binds to MED12 and intact Mediator both in vitro and in vivo
through a Gli3 transactivation domain (MBD; MED12/Mediator-binding domain)..."* and
*"Disruption of the Gli3-MED12 interaction through dominant-negative interference inhibited,
while RNA interference-mediated MED12 depletion enhanced, both MBD transactivation function
and Gli3 target gene induction in response to Shh signaling"* [PMID:17000779].

Both partners bind the C-terminal region, i.e. the part lost on processing — which is exactly
why GLI3R cannot activate.

## 6. Localisation

- **Ciliary tip, full-length form.** *"Most importantly, the data indicate that all three
  full-length Gli proteins along with Sufu colocalize to the distal tips of cilia in primary
  limb bud cells"*, and the antibody-orientation control *"Since the Gli3 antiserum recognizes
  the N-terminus of Gli3, and GFP is fused to the C-terminus in Gli3::GFP virus, the data
  suggest that it is the full-length form of Gli3 that localizes to the cilium tip"*
  [PMID:16254602]. Wen et al.: *"We show that the species of Gli3 that accumulates at cilium
  tips is full-length and likely not protein kinase A phosphorylated"* [PMID:20154143].
- **Requires KIF7.** *"We also demonstrate a requirement for Kif7 in the efficient
  localization of Gli3 to cilia in response to Hh and for the processing of Gli3 to its
  repressor form"* [PMID:19592253].
- **Nucleus / cytoplasm, form-resolved.** *"FL-Gli3 was localized to dot-like structures in
  both cytoplasm and nucleus, whereas Gli3ΔC staining only displayed a punctate pattern in
  the nucleus"* [PMID:12435627]. The punctate nuclear pattern is consistent with the
  nuclear-speck row (mouse IDA source), which I accepted on that basis.
- **Cytoplasmic retention.** SUFU (*"SUFU is an essential intracellular negative regulator of
  mammalian Hedgehog signalling and acts by binding and modulating the activity of GLI
  transcription factors"* [PMID:24311597]) and DZIP1 (*"First, DZIP1 interacts with GLI3, a
  transcriptional regulator for Hedgehog signaling, and prevents GLI3 from entering the
  nucleus"* [PMID:23955340]). PP2A/mTORC1 also shift the balance: *"An increase in PP2A
  activity or treatment with rapamycin leads to cytosolic retention of GLI3 and,
  consequently, reduced transcription of the GLI3 target gene and cell cycle regulator,
  cyclin D1"* [PMID:18559511].

### Note on the axoneme and ciliary-base rows

Haycraft et al. reported that *"The GFP signals failed to colocalize with γ-tubulin (basal
body marker), indicating that the Gli::GFP proteins do not localize to the basal body at the
base of the cilia"* [PMID:16254602]. That sits awkwardly with GO:0097546 (ciliary base, one
ARBA row and six Reactome TAS rows) and GO:0005930 (axoneme).

I did **not** modify either. For the axoneme row the human annotation is an orthology transfer
of a *mouse IDA* (PMID:21209331) whose full text I cannot read; per the project rule I do not
second-guess an experimental annotation on the strength of a different paper's steady-state
imaging. For the ciliary-base rows, Reactome's own text acknowledges the pool is small —
*"Although GLI and SUFU proteins are not concentrated in the cilium in the absence of Hh
signaling, processing and/or degradation of the transcription factors requires transit
through the cilium and basal levels of these proteins can be detected there"*
[Reactome:R-HSA-5610766] — which is a transient-intermediate claim rather than a
steady-state one. I accepted them and flagged the tension in the reasons and in
`suggested_questions`.

## 7. Protein-binding rows (GO:0005515) — how they were handled

Sixteen bare `protein binding` rows. Project policy: MODIFY when the cited paper supports a
more informative MF, otherwise REMOVE; never ACCEPT or MARK_AS_OVER_ANNOTATED.

Partner accessions resolved against UniProt (not guessed):

| Partner | Accession | Action | Replacement |
|---|---|---|---|
| SUFU (×4: PMID:10564661, 24311597, 28965847, 35140242) | Q9UMX1 | REMOVE | — (GO:1990788 already records the complex) |
| Zic1 / Zic2 (mouse) | P46684 / Q62520 | MODIFY | GO:0008134 transcription factor binding |
| ZIC3 | O60481 | MODIFY | GO:0008134 |
| EMX1 (+WDR11 on same row) | Q04741 (+Q9BZH6) | MODIFY | GO:0008134 |
| TRPS1 | Q9UHF7 | MODIFY | GO:0008134 |
| SKI | P12755 | MODIFY | GO:0001222 transcription corepressor binding |
| BTRC / mouse Btrc | Q9Y297 / Q3ULA2 | MODIFY | GO:0031625 ubiquitin protein ligase binding |
| mouse Spop | Q6ZWS8 | MODIFY | GO:0031625 |
| MED12 | Q93074 | MODIFY | GO:0036033 mediator complex binding |
| KIF7 | Q2M1P5 | MODIFY | GO:0019894 kinesin binding |
| DZIP1 | Q86YF9 | REMOVE | — (no partner-class term; the retention activity is DZIP1's) |

The four SUFU rows are removed rather than modified precisely because the informative
statement already exists as GO:1990788 (GLI-SUFU complex, IPI, PMID:24311597), and because
the activity inside that complex — protein sequestering — belongs to SUFU, not GLI3. The
GO-CAM agrees: SUFU carries GO:0140311 in `gomodel:693b3c0900001501/693b3c0900001527`.

## 8. Non-core developmental and immunological rows

Limb/digit/nose/gut morphogenesis and limb development: kept as `KEEP_AS_NON_CORE`. These are
organ-level outcomes downstream of GLI3-dependent transcription, not activities GLI3
performs. Human genetic grounding is solid — Pallister-Hall with *"a GLI3 mutation (Q717X)"*
[PMID:18478223] and [PMID:9354785] for postaxial polydactyly type A (cached entry is
title-only).

Thymic rows (GO:0033077, GO:0045060, GO:0046638, GO:0046639, GO:0070242, each as an IEA/ISS
pair): traced to mouse Gli3 IMPs, PMID:15855276 and PMID:19667090 (verified via QuickGO
against UniProtKB:Q61602). Real experimental evidence, but tissue-restricted and with no
human corroboration → non-core. Note that GO:0046638 and GO:0046639 are formally opposite;
both are retained because Gli3 acts at different thymocyte transitions with opposite sign.

## 9. Wnt crosstalk

*"Assays in embryos and cell lines indicate that repressor forms of the Hh-regulated
transcription factor, Gli3 (Gli3R), which are generated in the absence of Hh signaling,
inhibit canonical Wnt signaling"* and *"Consistent with this, Gli3R appears to physically
interact with the carboxy-terminal domain of beta-catenin, a region that includes the
transactivation domain"* [PMID:17331723]. Here GLI3R genuinely does the work (it is the
protein that binds beta-catenin), so the beta-catenin-binding MF row is ACCEPTed; the process
row GO:0090090 is KEEP_AS_NON_CORE as a crosstalk activity rather than the gene's core job.

## 10. Consistency with the module and family reviews

Nothing found that contradicts `modules/hedgehog_signaling.yaml`. The module's
`ci_gli_repressor` annoton (GO:0001227, GO:0045879, nucleus, exemplar GLI3/P10071, family
PANTHER:PTHR45718, ancestral node PANTHER:PTN001836086) matches what this review concludes
and what GO-CAM `693b3c0900000157` models. The GOA IBA for GO:0007224 cites
PANTHER:PTN001836086, the same node the module records — consistent.

One gap worth noting rather than a contradiction: the module describes the repressor form
only, and the GOA record has no gene-level GO:0001227 or GO:0001228 at all. That asymmetry is
what the MODIFY proposals on the GO:0003700 rows address. PTHR45718 has no family review yet.

## 11. Actions used

ACCEPT 78 · MODIFY 23 · KEEP_AS_NON_CORE 18 · REMOVE 5 · UNDECIDED 0 · NEW 0.

No `NEW` terms were proposed. Everything GLI3 demonstrably does is already represented by an
existing row, or is reachable by MODIFY from one; adding a term would not have passed the
participation/comparator bar for anything I considered.

Three annotations relied on a curator's reading of full text not in the cache
(PMID:31279575 smoothened signaling, PMID:28473536 SELEX DNA binding, PMID:9354785 limb
morphogenesis). None was left UNDECIDED: in each case the asserted function is independently
established for GLI3 elsewhere in the same record, so the standing rule is to ACCEPT (or, for
the developmental outcome, KEEP_AS_NON_CORE) and defer, not to second-guess.
