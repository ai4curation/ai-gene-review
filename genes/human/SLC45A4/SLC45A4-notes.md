# SLC45A4 (Q5BKX6) — curation journal

## Scope of the problem

SLC45A4 went from orphan to *twice*-deorphanized within three months of 2025, by two
independent groups that agree on the chemistry (polyamines) but disagree on the
compartment (plasma membrane vs peroxisome membrane). A third 2025 paper independently
nominates plasma-membrane polyamine handling. On top of that sits a legacy family-level
assignment as a sucrose:H+ symporter. This journal records what each line of evidence
actually shows.

## 1. The legacy sucrose annotation — where it really comes from

The brief's working hypothesis was that `GO:0008506` (sucrose:proton symporter activity)
on human SLC45A4 is a plant-derived IBA. **That is only half true, and the half that is
untrue matters.** Tracing the donors:

- IBA `WITH/FROM` for human Q5BKX6 is
  `AGI_LocusCode:AT1G09960|AT1G22710|AT1G71880|AT1G71890|AT2G02860|AT2G14670|AT5G06170|MGI:MGI:1922082|MGI:MGI:2146236|MGI:MGI:2153040|PANTHER:PTN000751434|PomBase:SPAC2F3.08|UniProtKB:Q10R54|UniProtKB:Q69JW3`.
  Q10R54 = rice SUT1, Q69JW3 = rice SUT5 (both plant sucrose transporters) — but the
  three `MGI:` donors are **mouse SLC45 paralogs**, not plants.
- QuickGO for `GO:0008506`, taxon 10090, ECO:0000314 returns exactly three mouse genes —
  `Slc45a2` (P58355), `Slc45a3` (Q8K0H7) and `Slc45a4` (Q0P5V9) — all IDA, all from
  **PMID:25164149**.
- The human **ISS** (`GO_REF:0000024`, ParkinsonsUK-UCL, 2016-03-01) has
  `WITH/FROM = UniProtKB:Q0P5V9`, i.e. it is a direct ortholog transfer from that mouse
  SLC45A4 IDA.

So the PAINT node placement is **not** a plant-to-animal leak: the curator had mammalian
experimental annotations sitting inside the clade. The problem is one node up — the
*source experiment itself*.

PMID:25164149 (Bartölke et al., Biochem J 2014) is a **yeast heterologous expression**
study: [PMID:25164149 "Heterologous expression of the three members SLC45A2, SLC45A3 and
SLC45A4 in Saccharomyces cerevisiae confirmed that they are indeed sucrose transporters."]
with [PMID:25164149 "[(14)C]Sucrose-uptake measurements revealed intermediate transport
affinities with Km values of approximately 5 mM."] A Km of ~5 mM for a disaccharide that
mammals never present to the cytosolic face of any membrane (dietary sucrose is hydrolysed
in the intestinal lumen by sucrase-isomaltase) is a weak basis for a physiological
molecular function.

Two 2025 papers tested sucrose directly and found nothing:

- Purified human protein, nanoDSF: [PMID:40836097 "However, neither GABA nor sucrose
  elicited a change in the thermal stability of purified SLC45A4"] — while polyamines did:
  [PMID:40836097 "Notably, we observed a marked decrease in thermal stability in the
  presence of biogenic amines, with the polyamines Spm and Spd eliciting the largest
  response"].
- Isotope tracing in cells: [PMID:41266324 "Our observations did not support the
  sucrose-transporting activity."] (they are appropriately careful that this does not rule
  out activity in the absence of glucose).

The homology premise is also thinner than the family name suggests:
[PMID:40836097 "On the basis of distant homology to the plant sucrose transporter (SUC) in
Arabidopsis thaliana, SLC45A4 was proposed as a proton-coupled sucrose transporter"] and
[PMID:40836097 "the human SLC45A4 protein shares only about 26% sequence identity with the
A. thaliana SUC1 transporter"]. UniProt has already added a CAUTION to Q5BKX6 on exactly
this point.

**Decision:** REMOVE `GO:0008506` (IBA and ISS) and `GO:0015770` (ISS), with
`propagation_review` root_cause `SOURCE_WEAK_OR_INFERRED` — the failure is not the
phylogenetic placement, it is that the seed IDA is a heterologous, low-affinity,
non-physiological activity that the human protein has since been shown not to exhibit.
This should propagate upstream: the mouse IDAs on Slc45a2/3/4 deserve re-examination too.

## 2. Compartment: plasma membrane vs peroxisome

### Case for plasma membrane (PMID:40836097, Nature 2025; PMID:41075780, Cell Metab 2025)

[PMID:40836097 "Cell-based assays show that SLC45A4 is a selective plasma membrane
polyamine transporter, and the cryo-electron microscopy (cryo-EM) structure reveals a
regulatory domain and basis for polyamine recognition."]
[PMID:40836097 "When electroporated into DRG neurons, eGFP-tagged SLC45A4 is trafficked to
the plasma membrane"]
[PMID:41075780 "Isotope-labeled tracing confirmed these predictions, demonstrating that
SLC45A4 and UNC93A mediate the transport of polyamine and acetylglucosamine species across
the plasma membrane."]

Caveat: both are **overexpression** systems (eGFP fusion electroporated into mouse DRG
neurons; N2a cells; HEK293T KO + cDNA). Overexpression of a multi-pass MFS protein routinely
saturates organellar retention and spills to the surface.

### Case for peroxisome membrane (PMID:41266324, Nat Commun 2025)

[PMID:41266324 "SLC45A4 functions as a putrescine transporter localized to the peroxisome
membrane to facilitate GABA production."]
[PMID:41266324 "SLC45A4 (green signal) is clearly detected around the cell nucleus, without
overlapping actin signal (Fig. 5a, top panel), suggesting organellar localization rather
than plasma membrane localization."]
[PMID:41266324 "This is also confirmed by the absence of co-localization with another plasma
membrane marker, E-cadherin, as shown in Supplementary Fig. 10a."]
[PMID:41266324 "Moreover, SLC45A4 signal strongly co-localized with ABCD3, which is a
peroxisomal transporter of long-chain fatty acids and is frequently used as a peroxisomal
marker"]
[PMID:41266324 "In addition, we observed no overlap between SLC45A4 signals and Golgi
marker, Giantin; endoplasmic reticulum marker, Calnexin or mitochondrial marker,
Mitotracker"]
and biochemically, two independent peroxisome preparations:
[PMID:41266324 "the results showed a strong enrichment of SLC45 A4 protein in the HA-IP
fraction, associated with an enrichment of peroxisome-specific proteins ABCD3 and catalase."]

Strength: this is **endogenous** protein, with an antibody validated against an HA-tagged
construct, in A549/H1299 lung-cancer lines, backed by subcellular fractionation. It is
methodologically the stronger localisation dataset. Weakness: it is one lab, in
transformed epithelial lines, and does not test neurons.

### How I am reading it

These two results are not logically incompatible. The systems differ on essentially every
axis — endogenous cancer-line protein vs overexpressed neuronal protein — and dual
localisation of a polyamine carrier (surface uptake plus peroxisomal delivery to diamine
oxidase) is a coherent cell-biological picture. I therefore keep `GO:0005886` (IDA,
`is_active_in`) rather than displacing it, and add `GO:0005778` (peroxisomal membrane) as a
reviewer-proposed NEW annotation from PMID:41266324 rather than as a replacement. The
`description` states the disagreement as a fact about the biology, and the unresolved
question goes to `suggested_questions`. The cryo-EM structure (which is compartment-agnostic)
constrains the substrate, not the location.

## 3. Substrate: how much of the "spermine/spermidine/putrescine" IDA set is direct?

Worth being precise, because GOA carries four separate MF IDAs from PMID:40836097.

- **Spermidine** is the only directly radiolabelled flux: 14C-SPD uptake time course in N2a
  cells overexpressing human or mouse SLC45A4 vs empty vector.
- **Spermine, putrescine and cadaverine** enter via (i) nanoDSF thermal destabilisation of
  the purified protein and (ii) competition against 14C-SPD uptake:
  [PMID:40836097 "The longest polyamine, Spm, has an half-maximum inhibitory concentration
  (IC50) of 240 µM, followed by Spd (123 µM), with the smaller polyamines Put and cadaverine
  (Cad) having the highest affinity (74 µM and 67 µM, respectively)"].
  Binding + competition is good evidence of recognition; it is one inferential step short of
  demonstrated translocation for each individual amine.
- Selectivity is *for* polyamines but not *among* them:
  [PMID:40836097 "Cell-based radioactive uptake assays further confirmed that SLC45A4
  functions as a non-selective polyamine transporter with an optimum pH of 7.5–8.5"], with no
  inhibition by L-lysine, L-ornithine or L-arginine.

All four MF IDAs are kept (ACCEPT); the nuance is recorded in each `reason`. The substrate
disagreement in the headlines ("polyamine" vs "putrescine") is therefore largely illusory:
putrescine is a polyamine and is the *highest-affinity* ligand in the Nature dataset.

### A direction-of-transport wrinkle

PMID:41075780's cellular readout is not obviously an uptake signature:
[PMID:41075780 "Consistent with the machine learning predictions, acetylspermidine levels
were depleted by nearly 4-fold, while gamma-aminobutyric acid (GABA) accumulated by ~5.5
fold upon SLC45A4 expression"] and [PMID:41075780 "Furthermore, SLC45A4 expression resulted
in elevated levels of [13C4]acetylputrescine in the media"]. Intracellular depletion plus
extracellular accumulation reads as **export** of acetylated polyamines. The authors
themselves flag the evidential ceiling: [PMID:41075780 "However, further structural studies
as well as liposome-based in vitro reconstituted uptake for SLC25A45 and Xenopus larvae
oocytes assays for SLC45A4 and UNC93A should be performed to definitively study the function
of these transporters."] GO MF terms are direction-agnostic, so this does not change any
term choice, but it is a real open question and goes to `suggested_questions`.

Note also that the reference title for PMID:41075780 is about **SLC25A45**, not SLC45A4 —
the citation is nonetheless correct: SLC45A4 is a co-equal subject of that paper
([PMID:41075780 "This approach identifies UNC93A and SLC45A4 as candidate plasma membrane
transporters for acetylglucosamine and polyamines, respectively."]). Flagged in
`reference_review` so a future reader does not mistake it for a transposed PMID.

## 4. Pain

[PMID:40836097 "Mice lacking SLC45A4 show normal mechanosensitivity but reduced sensitivity
to noxious heat- and algogen-induced tonic pain that is associated with reduced excitability
of C-polymodal nociceptors."] plus
[PMID:40836097 "In the mouse nervous system, Slc45a4 expression is enriched in all sensory
neuron subtypes within the dorsal root ganglion, including nociceptors."] and a UKB GWAS
association with chronic pain intensity. `GO:0019233` IMP accepted. The ARBA IEA for the
same term is accepted for consistency (same-term-same-action).

## 5. GO:0005515 protein binding (IPI, PMID:36115835)

Eighteen partners, all PDZ-domain scaffolds (DLG1–4, GRIP1/2, MPDZ, PATJ, PDZK1, MAGI1,
LNX1/2, WHRN, NHERF4, APBA2, IL16, FRMPD2), from a quantitative PDZ-domain holdup assay.
Real, and biologically suggestive of a C-terminal PDZ-binding motif anchoring SLC45A4 at a
membrane — but `protein binding` itself carries no functional information, so
MARK_AS_OVER_ANNOTATED per project guidance. `GO:0030165` (PDZ domain binding) would be the
informative term if a curator wanted to keep it.

## 6. Actions taken

| Term | Evidence | Action |
|---|---|---|
| GO:0008506 sucrose:proton symporter activity | IBA, ISS | REMOVE (+ propagation_review) |
| GO:0015770 sucrose transport | ISS | REMOVE (+ propagation_review) |
| GO:0022857 transmembrane transporter activity | IEA | MODIFY → GO:0015203 |
| GO:0055085 transmembrane transport | IEA | MODIFY → GO:1902047 |
| GO:0005515 protein binding | IPI | MARK_AS_OVER_ANNOTATED |
| GO:0000297 / GO:0015606 / GO:0015489 / GO:0015203 | IDA | ACCEPT |
| GO:0005886 plasma membrane | IDA, IEA | ACCEPT |
| GO:0019233 sensory perception of pain | IMP, IEA | ACCEPT |
| GO:0016020 membrane | IBA | ACCEPT |
| GO:0005778 peroxisomal membrane | — | NEW (proposed, PMID:41266324) |
| GO:0009449 GABA biosynthetic process | — | NEW (proposed, PMID:41266324) |
