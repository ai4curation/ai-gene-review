# AP4S1 (human, Q9Y587) — review notes

Working notes for the GO annotation review. Inline provenance as
`[PMID:NNNN "verbatim quote"]`. 144 aa, chromosome 14, HGNC:575, PANTHER PTHR11753.

## 0. Identity check

`AP4S1-uniprot.txt` is `ID AP4S1_HUMAN Reviewed; 144 AA.`, `AC Q9Y587;` — the expected
accession, not a merged redirect. RecName `AP-4 complex subunit sigma-1`; alternative
names include `Sigma-4-adaptin`. Family assignment `DR PANTHER; PTHR11753; ADAPTOR
COMPLEXES SMALL SUBUNIT FAMILY`, and `Q9Y587` is present in
`interpro/panther/PTHR11753/PTHR11753-entries.csv` with gene symbol `AP4S1`, so the family
call is not in doubt. InterPro matches, checked live against the InterPro API, are exactly
three: IPR011012 (Longin-like domain superfamily), IPR016635 (Adaptor protein complex,
sigma subunit), IPR022775 (AP complex, mu/sigma subunit). This matters for the two ARBA
rows below.

One nomenclature trap worth stating once: the protein is **sigma-4** (the AP-4 sigma), but
UniProt's recommended name and the GOA `GENE NAME` column both read "AP-4 complex subunit
**sigma-1**". The "-1" is a within-AP-4 subunit index, not a reference to AP-1. Confusing
this with AP1S1 (sigma-1A, P61966) would be easy and wrong; the two proteins are
paralogues in the same PANTHER family with different complexes and different measured
behaviour.

## 1. What AP4S1 is, biologically

AP4S1 is the single small (sigma) subunit of adaptor protein complex 4, an obligate
heterotetramer of two large adaptins (epsilon/AP4E1 and beta4/AP4B1), one medium adaptin
(mu4/AP4M1) and sigma4 [`file:human/AP4S1/AP4S1-uniprot.txt` "SUBUNIT: Adaptor protein
complex 4 (AP-4) is a heterotetramer composed of two large adaptins (epsilon-type subunit
AP4E1 and beta-type subunit AP4B1), a medium adaptin (mu-type subunit AP4M1) and a small
adaptin (sigma-type AP4S1)."]. AP-4 was described twice independently in 1999, by
co-immunoprecipitation and yeast two-hybrid [PMID:10436028] and by gel filtration,
sedimentation velocity and immunoprecipitation [PMID:10066790]; sigma4 is a component in
both.

AP-4 assembles a **non-clathrin** coat on vesicles budding from the trans-Golgi network.
Immunogold EM put it on non-clathrin-coated vesicles at the TGN [PMID:10436028 "Immunogold
electron microscopy indicates that AP-4 is associated with nonclathrin-coated vesicles in
the region of the trans-Golgi network."], and immunofluorescence put it at the TGN or an
adjacent structure in a brefeldin-A-sensitive manner, i.e. ARF-dependent [PMID:10066790
"Immunofluorescence analyses showed that AP-4 is associated with the trans-Golgi network
or an adjacent structure and that this association is sensitive to the drug brefeldin A."].
The ARF dependence is now structural: cryo-EM of the AP-4 core and of the AP-4/ARF1 complex
shows two ARF1 sites, on epsilon and on mu4-CTD, and that efficient membrane recruitment
needs ARF1 and cargo together [PMID:41565640].

The best-established cargo is ATG9A, whose export from the TGN to peripheral and axonal
compartments fails when AP-4 is lost; APP is the other well-characterised cargo, and its
missorting is what Reactome models. SERINC1/3, AGTRAP, sortilin, AMPA and delta-2
glutamate receptors have also been reported as AP-4-dependent.

## 2. Disease: SPG52 / AP-4 deficiency syndrome

Bi-allelic loss-of-function variants in AP4S1 cause spastic paraplegia 52
(MIM:614067), one of the four genetic forms of an otherwise indistinguishable
"AP-4 deficiency syndrome" [PMID:32979048 "Exploring genotype-phenotype correlations, we
found that disease severity and major phenotypes were equally distributed among the four
subtypes, establishing that SPG47, SPG50, SPG51 and SPG52 share a common phenotype, an
'AP-4 deficiency syndrome'."]. The founding report identified a nonsense variant
p.Arg42* [PMID:21620353].

Two negatives that matter for how strongly anything here should be stated:

- Heterozygous carriers are **unaffected**. A 2024 report proposed a dominant AP4S1
  phenotype; a 2025 study of 28 carriers of the same p.Arg97Ter allele rejected it
  [PMID:39865903 "Alternative causes should be considered when evaluating patients with
  heterozygous AP4S1 variants and neurological symptoms, as misattribution of
  pathogenicity can impact clinical care and genetic counseling."]. SPG52 is strictly
  recessive; there is no AP4S1 haploinsufficiency phenotype to annotate.
- Bulk autophagic flux is **not** disrupted in patient fibroblasts despite ATG9A
  mislocalisation [PMID:31915823 "we found that fibroblast lines derived from AP-4-HSP
  patients showed intact autophagic flux despite the changes in ATG9A distribution."].
  This is the reason I do not propose an autophagy BP term for AP4S1 — see §7.

## 3. The one genuinely AP4S1-specific molecular function: holding the core together

This is the substantive finding of the review, and it is absent from GOA.

Sigma4 is not inert filler. The yeast three-hybrid result is direct and specific: the two
large adaptins of AP-4 cannot associate without it [PMID:11409905 "two large subunits of
the AP-4 complex, epsilon-adaptin and beta4-adaptin, are found to interact with each other
only in the presence of the small subunit, sigma4"]. The same paper shows the identical
dependence for AP-1 (gamma + beta1 need sigma1) and for the COPI F subcomplex
(gamma-COP + beta-COP need zeta-COP), so this is the conserved architectural role of the
small subunit across the whole superfamily.

Human genetics and biochemistry give the same answer by loss of function. In fibroblasts
from a patient with compound-heterozygous AP4S1 nonsense/frameshift variants, sigma4 is
undetectable and every other AP-4 subunit falls [PMID:25552650 "In the AP4S1* cell line
appeared completely absent, and there was a substantial reduction of all other AP-4
subunits, implying that the loss of σ4 leads to the destabilization of the entire AP-4
complex."], the hemicomplexes and the whole tetramer fail to assemble
[PMID:25552650 "We show that the premature stop mutations in AP4S1 result in a reduction
of all AP-4 subunits and loss of AP-4 complex assembly."], and the only known AP-4
accessory protein loses its membrane recruitment [PMID:25552650 "Recruitment of the AP-4
accessory protein tepsin, to the membrane was also abolished."]. AP-1 assembly in the same
cells is normal, so this is not a general secretory collapse.

The structure makes the geometry explicit: sigma4 is the subunit that the epsilon trunk
wraps around to build the central core [PMID:41565640 "The N-terminal halves of ε and β4
capture σ4 and the N-terminal domain of μ4 (μ4-NTD), respectively, and wrap around them to
form the central structural core of AP-4"], and the construct used is unambiguously this
protein [PMID:41565640 "σ4 (UniProt ID: Q9Y587)"]. Finally, assembly is chaperoned, and
sigma4 is one of the two subunits the chaperone holds [PMID:35976721 "binds to and
stabilizes the AP-4 ε and σ4 subunits, thus promoting complex assembly"].

**Annotation consequence:** `GO:0005198 structural molecule activity` — "The action of a
molecule that contributes to the structural integrity of a complex" (definition checked on
QuickGO) — is a real, subunit-attributable molecular function for AP4S1 and is proposed as
a NEW row. It is not "protein binding": the claim is not that sigma4 touches epsilon, it is
that epsilon and beta4 cannot associate in its absence.

## 4. Does sigma4 contribute to cargo-signal binding? No — and I take a position on the AP1S1 analysis

The prompt asked me to read `genes/human/AP1S1/AP1S1-bioinformatics/RESULTS.md` (on
`origin/main`) and take a position on its treatment of AP4S1 as a "verified non-binder"
negative control that nevertheless retains 4/5 of the sigma-side dileucine pocket
residues.

**My position: the analysis is right, its design is the right design, and its use of
sigma4 is well-grounded — with one citation-weighting correction and one extension.**

*Where the negative actually comes from.* The AP1S1 notes cite the sigma4 non-binding to
`[PMID:14691137, PMID:21097499]` jointly. Those two citations are not of equal weight, and
the difference is instructive:

- PMID:14691137 (Janvier 2003) tested two signals (HIV-1 Nef ENTSLL, LIMP-II ERAPLI) by
  yeast three-hybrid and scored **both** alphaC-sigma2 and epsilon-sigma4 negative. Its
  companion GST pull-down is weaker still for AP-4, because the input preparation
  "contained large quantities of AP-1 and AP-2, moderate quantities of AP-3, and traces of
  AP-4" — an AP-4 negative from a prep containing traces of AP-4 is close to uninformative.
  The paper says so itself in the discussion [PMID:14691137 "In particular, it will be of
  interest to determine whether other"... signals "are recognized by α–σ2 or ɛ–σ4, which
  tested negative in our assays despite having structures similar to γ1–σ1 and δ–σ3."].
  On this paper alone, sigma4 would be an *untested-beyond-two-signals* non-binder, not a
  verified one.
- PMID:21097499 (Mattera 2011) is the load-bearing citation. It tested three signals
  (Nef ENTSLL, mouse tyrosinase ERQPLL, human LIMP-II ERAPLI) and reported
  [PMID:21097499 "we found that all of these signals interact with the AP-1 γ1-σ1A, AP-2
  αC-σ2, and AP-3 δ-σ3A hemicomplexes but not with the homologous AP-4 ϵ-σ4 hemicomplex"].
  Crucially **alphaC-sigma2 scored positive here**, i.e. the other half of the 2003
  negative did not survive, while the epsilon-sigma4 negative did — in the same assay, run
  by the same laboratory, with the positive controls working. That is what converts sigma4
  from "untested" to a genuine measured negative, and it is a stronger position than the
  AP1S1 write-up claims for it.

So the correction is only about which citation carries the weight. I did **not** edit the
AP1S1 review: AP1S1 is not a donor for any AP4S1 row, and the campaign brief confines
cross-gene edits to donor-side defects. Flagged in the return report instead.

*The extension.* The AP1S1 analysis closed one door and explicitly left the next question
open: the specificity difference "must lie elsewhere — in the partner large subunit, in
the surrounding surface, or in conformational accessibility of the pocket". I tested the
first of those three, because the site is not a sigma-only site. PMID:21097499 describes it
as "hydrophobic pockets on σ2 that fit the Leu and (L/I) residues, and a basic patch
straddling the boundary of α and σ2" — so the acidic `(D/E)` position of the signal is read
by a **two-part** basic patch, one arginine on the sigma and one on the large subunit
(gamma1 R15, alphaC R21, delta R26), and the large-subunit one is the dominant contributor
in AP-1 [PMID:21097499 "mutation of γ1 R15E caused a much greater reduction in binding to
the (D/E) XXX L(L/I) signals than mutation of σ1A Arg 15"].

Result, in `file:human/AP4S1/AP4S1-bioinformatics/RESULTS.md`: with a 6/6 method control
(the three verified anchors map onto one another exactly), all three anchors map to the
**same** epsilon residue, position 44, and it is threonine. Epsilon and delta share an
identical `LVRGI` immediately upstream, so the register is visible without trusting the
aligner. Sigma4 does retain the sigma-side Arg15. The basic patch is therefore
**half-complete in AP-4**: present on sigma4, absent on epsilon. Every complex that binds
`(D/E)XXXL(L/I)` has both halves; the complex that does not is the one missing the
large-subunit half.

That is a hypothesis consistent with the measured negative, not a test of it — the test
would be an epsilon T44R substitution — and the write-up says so. It does not change any
annotation on AP4S1. What it does is close the loop: sigma4's intact pocket is not evidence
of binding, because the half of the site it cannot supply on its own is the half AP-4 has
lost. **No cargo-signal-binding MF is proposed for AP4S1.**

*Where AP-4's cargo signals really are read.* On mu4, in every case, and never on sigma4:
the original tyrosine-signal result [PMID:10436028 "The mu4 subunit of the complex
specifically interacts with a tyrosine-based sorting signal"]; the APP YKFFE signal, bound
at a site on mu4 that is distinct from the canonical one [PMID:20230749, PMID:24498434];
and the ATG9A peptide, bound by mu4-CTD with a measured affinity [PMID:41565640 "The
binding affinity between the ATG9A peptide and μ4-CTD was measured by the isothermal
titration calorimetry (ITC) assay with the Kd of 1.1 ± 0.1 μM"]. Reactome says the same
thing in its own reaction summary [`file:reactome/R-HSA-5229132.md` "The medium (mu)
adaptins of all AP complexes can recognise and interact with tyrosine-based (YXXphi)
sorting signals found within the cytoplasmic tails of integral membrane proteins"].

## 5. ATG9A: the readout, and what it licenses for AP4S1 specifically

ATG9A mislocalisation is the functional assay for AP-4 deficiency, and — importantly for
this review — it has been measured **on AP4S1 patient cells**, not only on AP4B1/AP4E1
cells. PMID:31915823 included four AP4S1 fibroblast lines among fifteen
[PMID:31915823 "we generated fibroblast lines from 15 well-characterized patients carrying
homozygous or compound-heterozygous variants in AP4B1 (7 lines), AP4M1 (3 lines), AP4E1 (1
line) and AP4S1 (4 lines)"] and concluded across all of them [PMID:31915823 "We conclude
that bi-allelic loss-of-function variants in any of the AP-4 subunit genes lead to loss of
AP-4 function and subsequently to accumulation of ATG9A in the TGN area and depletion from
peripheral compartments."]. The effect is AP-4-dependent rather than incidental
[PMID:31915823 "ATG9A was redistributed upon re-expression of AP4B1 arguing that
mistrafficking of ATG9A is AP-4-dependent."]. PMID:34729478 turned the same readout into a
quantitative diagnostic assay and applied it to AP4S1 probands.

So there is human, AP4S1-specific, loss-of-function evidence that this gene product is
required for export of a transmembrane cargo out of the TGN. The correct GO term for that
is `GO:0006892 post-Golgi vesicle-mediated transport` — "The directed movement of
substances from the Golgi to other parts of the cell, including organelles and the plasma
membrane, mediated by small transport vesicles" (definition checked on QuickGO). Confirmed
by QuickGO's ancestor closure to be a descendant of GO:0016192 and **not** of GO:0015031,
so it sharpens the IBA rather than duplicating the InterPro protein-transport row. Proposed
as a NEW row with IMP.

I deliberately did **not** choose `GO:0006895 Golgi to endosome transport`: its definition
names early sorting endosomes as the destination and clathrin vesicles as the vehicle, and
AP-4's ATG9A route is non-clathrin and terminates in peripheral/pre-autophagosomal
compartments rather than early endosomes. Modern work is explicit that
[PMID:41032520 "AP-4-mediated TGN export operates independently of clathrin"].

Animal models agree but are not annotatable on the human gene as IMP: zebrafish morpholino
knockdown [PMID:32216065] and a CRISPR truncation allele [PMID:37767851 "The ap4s1
truncation led to motor impairment, delayed neurodevelopment, and distal axonal
degeneration."] both give neurodevelopmental and axonal phenotypes.

## 6. The IBA — one row, a pan-AP-sigma node, and the right LCA term

The single IBA row is `GO:0016192 vesicle-mediated transport`, `GO_REF:0000033`, with
`PANTHER:PTN000204281` plus eleven gene donors in WITH/FROM.

*The node.* `just fetch-panther-paint PTHR11753` returns exactly one annotated PAINT node
for the whole family — PTN000204281 — carrying two IBD rows, `GO:0043231` (C) and
`GO:0016192` (P). There is **no IRD and no IKR anywhere in the family**, so no curator has
asserted loss or divergence at any descendant node. Re-running the fetch produced no diff,
so the committed slice is current. Yes, this is the same node the AP1S*/AP2S1 genes inherit
from — it is the only one there is, and AP4S1 is in the family's `entries.csv`, so AP4S1
inherits from the same node, as GO_Central's own WITH/FROM asserts.

*The seeds, resolved.* The GO:0016192 IBD seed list in the PAINT slice has ten entries; the
IBA row on AP4S1 carries eleven gene donors plus the node. The extra one in the IBA row,
`FB:FBgn0043012`, is a seed of the *other* IBD row at the same node (GO:0043231), so the
node's evidence base is the same set of proteins; I note the discrepancy rather than
reading anything into it (the IBD rows carry different dates, 20260828 vs 20260528, and the
IBA row is dated 20250902). Resolved via UniProt xref search (size 5, multi-hits reported):

| WITH/FROM | resolves to | protein |
|---|---|---|
| CGD:CAL0000182525 | Q59QC5 | *C. albicans* APS3, AP-3 sigma |
| FB:FBgn0039132 | Q9VCF4 (+3 TrEMBL) | *D. melanogaster* AP-1sigma (CG5864) |
| FB:FBgn0043012 | Q9VDC3 (+1 TrEMBL) | *D. melanogaster* AP-2sigma (CG6056) |
| MGI:MGI:1098244 | P61967 (+3 TrEMBL) | mouse Ap1s1, sigma-1A |
| MGI:MGI:1889383 | Q9DB50 (+4 TrEMBL) | mouse Ap1s2, sigma-1B |
| PomBase:SPAP27G11.06c | Q9P7N2 | *S. pombe* vas2, AP-1 sigma-1 |
| RGD:620188 | P62744 (+4 TrEMBL) | rat Ap2s1, AP-2 sigma |
| SGD:S000003561 | P47064 | *S. cerevisiae* APS3, AP-3 sigma |
| SGD:S000004160 | P35181 | *S. cerevisiae* APS1, AP-1 sigma-1 |
| UniProtKB:P53680 | P53680 | human AP2S1, AP-2 sigma |
| WB:WBGene00000157 | Q19123 | *C. elegans* aps-2, AP-2 sigma (F02E8.3) |

`WB:WBGene00000157` is not a UniProt xref key; it was resolved through the GO API bioentity
endpoint to `F02E8.3` and thence to Q19123.

The one ungrounded donor, re-checked directly: FB:FBgn0039132 (fly AP-1sigma, queried
through Q9VCF4) carries GO:0016192 only by IEA from InterPro2GO (IPR000804, IPR044733) and
by ISS from SGD:S000004160 — which is itself another donor in this same WITH/FROM, so that
strand contributes nothing independent. Its `source_status` is therefore
`SOURCE_WEAK_OR_INFERRED`: the record is neither missing nor untraceable, it simply never
carries the term experimentally.

*Donor GO records, counted not asserted* (`.scratch/iba_donor_table.py`, QuickGO with
`goUsage=descendants`): **10 of the 11 donors** carry at least one direct experimental
annotation to GO:0016192 or to a term GO's `is_a/part_of/occurs_in` closure places beneath
it — spanning synaptic vesicle endocytosis (P53680 IDA/IMP; P62744 EXP/IDA/IMP),
retrograde endosome-to-Golgi transport (P61967 IMP; Q9P7N2 IDA), synaptic vesicle budding
from endosome (Q9DB50 IDA/IMP), Golgi-to-vacuole transport (P35181, P47064, Q59QC5, all
IMP) and clathrin-dependent endocytosis (Q19123 IMP). The one without is FB:FBgn0039132,
queried through Q9VCF4, which shows only IEA/ISS there; FlyBase's native record may carry
more than QuickGO exposes under that accession. (The FB:FBgn0043012 experimental row is
`GO:0035615` clathrin-cargo adaptor activity IMP, a molecular function that GO's closure
places under GO:0016192 via a part_of link — worth naming rather than burying.)

*Is AP4S1 inside the clade that inherited it?* Yes, and there is nothing to argue with. The
node's seeds are AP-1, AP-2 and AP-3 sigmas from fungi, nematode, insect, rodent and human
— it sits at or near the eukaryotic root of the family, before the AP-1/2/3/4 sigma
duplications. Sigma4 is a bona fide member of that family by HMM, by fold (Longin-like) and
by function: AP-4 makes coated vesicles at the TGN. There is no lineage, compartment or
activity mismatch to raise.

*Is the term too general?* No, and this is the case where it is important not to reach for
`GRANULARITY_MISMATCH`. The donors do **not** agree on a specific sub-process: they split
across endocytosis (AP-2 sigmas), Golgi-to-vacuole transport (AP-3 sigmas) and
retrograde/endosomal transport (AP-1 sigmas). GO:0016192 is the correct least common
ancestor of a genuinely heterogeneous donor set, not a lazy parent. The AP4S1-specific
refinement belongs in a separate NEW row grounded in AP4S1's own patient-cell data (§5),
which is exactly what I have done. `NO_FAILURE_CORE`.

*No self-reference here.* Q9Y587 does not appear in its own WITH/FROM (checked by script),
and its own GO record carries GO:0016192 only by IBA and NAS — there is no experimental BP
annotation on AP4S1 for the PAINT curator to have used. This is the normal case, not a
defect.

## 7. Row-by-row calls that need justifying

**`GO:0031904 endosome lumen`, TAS, Reactome:R-HSA-5229111 — REMOVE.** This is a
compartment-inheritance artefact, and the Reactome API shows exactly how it arises:
R-HSA-5229111 is a `BlackBoxEvent` whose **output entity is the complex `AP4:APP` placed in
compartment "endosome lumen"**, so every member of that complex — all four AP-4 subunits —
inherits "endosome lumen" in the Reactome-to-GO CC mapping. AP-4 is a cytosolic peripheral
membrane coat [`file:human/AP4S1/AP4S1-uniprot.txt` "SUBCELLULAR LOCATION: Golgi apparatus,
trans-Golgi network membrane {ECO:0000305|PubMed:10436028}; Peripheral membrane protein"],
it engages ARF1 and the *cytosolic* tails of cargo [PMID:41565640], the paper that
established AP-4 as an ARF1 effector says so in its own first sentence [PMID:11707398 "This
complex consists of four subunits (epsilon, beta4, mu4 and sigma4) and localizes to the
cytoplasmic face of the trans-Golgi network (TGN)."], and GO:0031904 is "The volume
enclosed by the membrane of an endosome" (QuickGO). A cytosolic coat adaptor cannot
be in the endosome lumen; the topology is impossible, not merely unsupported. Reactome's
own summary describes APP being delivered to endosomes, not AP-4 entering their lumen.
This is a positive biological argument, which is what REMOVE requires. (Note: the AP4B1
review in this repo marked the same row KEEP_AS_NON_CORE; I think that is too generous and
say so here rather than editing that gene.)

The reference-projection test makes the scale of the artefact exact: QuickGO by
`reference=Reactome:R-HSA-5229111` returns 11 annotations over 5 entities — the four AP-4
subunits plus APP — with GO:0031904 on five of them and GO:0032588 on five of them. One
compartment assignment, five proteins. The companion reaction R-HSA-5229132 places its
inputs and output at the TGN membrane and projects 5 annotations over the same 5 entities,
all GO:0032588, and is fine.

**`GO:0012505 endomembrane system`, IEA, ARBA:ARBA00028953 — MODIFY to GO:0032588.** True
but the least informative form of a fact the gene already carries precisely (TGN and TGN
membrane rows). Too general is exactly the MODIFY case.

**`GO:0005737 cytoplasm`, IEA, ARBA:ARBA00026971 — ACCEPT.** Broad, but correct and
load-bearing: it is the same topological fact that makes the endosome-lumen row wrong. Also
already entailed — QuickGO's closure puts GO:0005737 among the ancestors of GO:0030124, so
the IDA complex row implies it.

**Both ARBA rows carry a reproducibility defect worth recording.** Fetching
`https://rest.uniprot.org/arba/ARBA00026971` and `.../ARBA00028953` and intersecting every
condition set against AP4S1's three real InterPro matches: ARBA00026971 has 2388 condition
sets, of which one (#289) names an AP4S1 signature but requires IPR016635 **and** IPR022775
**and IPR027156**, which AP4S1 does not match; ARBA00028953 has 533 condition sets, of
which one (#74) requires IPR010908, IPR011012, IPR044565 and Eukaryota, and AP4S1 matches
only IPR011012. **Neither annotation can be reproduced from its own rule's published
condition sets.** The GO terms are nonetheless biologically right, so this is a curation
provenance problem, not a biology problem — recorded as a CURATION knowledge gap rather
than used as grounds for REMOVE. (Same pattern as the ARBA00027853 review already merged in
this repo.)

**The two IC rows** (`GO:0006605 protein targeting`, `GO:0008104 intracellular protein
localization`, both `supporting_entities: GO:0030124`) are curator inferences from complex
membership, and complex membership is established by IDA on this protein. Both terms fit
what AP-4 does. ACCEPT both; the propagation source is a GO term rather than a gene
product, which is what an IC is, and I record it as such rather than omitting the block.

**The three ComplexPortal NAS rows** (TGN, vesicle-mediated transport, AP-4 adaptor
complex, all `PMID:10436028`) are author-statement annotations whose source paper is the
primary characterisation of the complex. All three are supported by that paper's own
abstract. ACCEPT.

**`GO:0030124 AP-4 adaptor complex` IDA (`PMID:10066790`)** is the anchor annotation of the
whole record and is correct. The GO definition names the subunit exactly — "consists of
beta4, epsilon, mu4 and sigma4 subunits" (QuickGO) — so the term and the protein are
matched by construction. ACCEPT, core.

**Why no `GO:0030117 membrane coat` NEW row:** QuickGO's ancestor closure already places
GO:0030117 above GO:0030124, so it would be redundant with the IDA row.

**Why no autophagy BP:** ATG9A is the cargo, and its missorting is robust, but bulk
autophagic flux is intact in AP-4-deficient patient fibroblasts (§2). The autophagy
phenotype is spatial and axonal, demonstrated in mouse and neuronal models rather than on
human AP4S1 loss-of-function directly. Annotating AP4S1 to `GO:0000045 autophagosome
assembly` would assert more than the human evidence carries. Recorded as a knowledge gap.

**Why no cargo-binding MF:** §4.

## 8. Isoform note

UniProt's canonical is Q9Y587-1 (144 aa), and MANE-Select is NM_001128126.3 / NP_001121598.1
= Q9Y587-1. The clinical literature, however, standardises on **NM_007077** — Q9Y587-2 — for
variant nomenclature: PMID:21620353 reports `NM_007077.3: c.124C>T, p.Arg42*`, PMID:39865903
uses `NM_007077.3: c.289C>T, p.Arg97Ter`, and PMID:34729478 draws its AP4S1 domain figure
"based on UniProt Q9Y587-2". Isoforms 2, 3 and 4 all replace the C-terminal ~42-46 residues.
The four AP4S1 fibroblast lines and the residue numbering in the disease literature are
therefore on a different isoform frame from UniProt's canonical. No GOA row on this gene
carries an `isoform` qualifier, and none of the annotations reviewed here is
isoform-specific, so nothing changes in the review — but it is a real trap for anyone
mapping a published p.Arg97Ter onto the canonical sequence, and it is recorded as a
knowledge gap. (PMID:34729478 additionally writes "For AP4S1, alignment was transferred from
isoform 1 and isoform 2 of Q9Y6B7" — Q9Y6B7 is AP4B1, not AP4S1; an evident slip in that
paper's methods, noted so no downstream claim rests on it.)

## 9. What the deep-research report gave me, and what it missed

`AP4S1-deep-research-affinage.md` describes the right protein (`uniprot_accession:
Q9Y587`, and the narrative is about the AP-4 sigma subunit, not a symbol collision), the
trust gates are clear (`.affinage.log`: "AP4S1: trust gates clear"), `self_evaluation_pairwise:
win`, `faith_pct: 100.0`, and all eight citations are numeric PMIDs (no bioRxiv). Its eight
findings all check out against the papers. It is a good record.

Its recall is another matter, exactly as the campaign brief predicts. **It missed every
paper that establishes AP4S1's molecular function**, because they are titled for the
complex, the partner or the family rather than for this gene:

- PMID:11409905 — the yeast three-hybrid showing epsilon and beta4 need sigma4 to
  associate. This is the single most AP4S1-specific mechanistic result in the literature
  and it is the basis of the NEW GO:0005198 row. Title names "clathrin adaptor complexes
  and COPI complex".
- PMID:41565640 (2026) — the cryo-EM structure of AP-4 and AP-4/ARF1. Cross-referenced from
  the UniProt record itself as EMD-63965/63966/63968/63969, which is how I found it.
- PMID:21097499 and PMID:14691137 — the dileucine hemicomplex assays, i.e. the measured
  negative for sigma4.
- PMID:35976721 — AAGAB stabilises epsilon and sigma4 specifically.
- PMID:11707398 — AP-4 as an ARF1 effector, and the sentence that settles the topology
  question behind the endosome-lumen removal. Title names ARFs.
- PMID:10066790, PMID:10436028 — the two 1999 papers that are the `original_reference_id`
  of five of the fourteen GOA rows. (These were already in the GOA-seeded reference list,
  so the review had them; affinage did not.)
- PMID:39865903 — the measured negative on heterozygous carriers.
- PMID:20230749, PMID:24498434 — the mu4 cargo-site work, which is what settles that
  cargo binding is not sigma4's job.
- PMID:32979048, PMID:41032520, PMID:30262884, PMID:11802162, PMID:31142229.

One paper affinage *did* return turned out to matter for a reason affinage did not state:
PMID:31660686 calls NM_001128126.3 "the canonical isoform 2", which is the MANE Select
transcript that UniProt calls isoform **1**. That is a third naming frame for the same
gene, and it is why the isoform mismatch is recorded as a knowledge gap rather than left
as a footnote.

Affinage's `mechanism_profile` proposed GO:0060090 and GO:0005198 for the molecular
activity. I did not import those ids; I re-grounded both from the primary literature, and
they land in different slots than a naive import would have put them (GO:0005198 as the
subunit-level MF, GO:0060090 as `contributes_to_molecular_function` at complex level).

## 10. Tooling notes

- **Europe PMC was down for the whole session.** `https://www.ebi.ac.uk/europepmc/webservices/rest/search`
  returned HTTP 503 on every attempt across several hours, and `www.europepmc.org` returned
  530, while `rest.uniprot.org`, QuickGO and `eutils.ncbi.nlm.nih.gov` were all fine. The
  brief's Europe PMC searches were therefore run against NCBI eutils instead
  (`.scratch/pubmed.py`), covering the symbol, `sigma4 adaptin`, `SPG52`, `AP-4 sigma`,
  `AP-4 deficiency`, the partners (tepsin, ATG9A, ARF1, AAGAB), the family and the
  paralogues. Coverage looks complete for this gene — it surfaced the 2026 structure paper
  and the 2025 negative, neither of which was in the affinage record.
- `interpro/panther/PTHR11753/` was already present and current; `just fetch-panther-paint
  PTHR11753` produced no diff, so nothing new to commit there.
