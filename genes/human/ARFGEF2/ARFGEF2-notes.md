# ARFGEF2 (BIG2) — review notes

Human `ARFGEF2` / `Q9Y6D5` / BIG2_HUMAN, 1785 aa, `PE 1: Evidence at protein level`.
Sec7 domain 654–785; DCB region 2–224; HUS region 508–528
(`file:human/ARFGEF2/ARFGEF2-uniprot.txt`). Two PDB entries, `3L8N` and `3SWV`,
both covering only 635–836 — i.e. the Sec7 catalytic module; nothing structural
outside it.

## What the protein does

BIG2 is one of the three human brefeldin A-sensitive large ArfGEFs (GBF1, BIG1,
BIG2). It was cloned alongside BIG1 from human brain and shown biochemically to
be a GEF: *"BIG2, synthesized as a His6 fusion protein in Sf9 cells, accelerated
guanosine 5'-3-O-(thio)triphosphate binding by recombinant ARF1, ARF5, and ARF6.
It activated native ARF (mixture of ARF1 and ARF3) more effectively than it did
any of the nonmyristoylated recombinant ARFs. BIG2 activity was inhibited by BFA
in a concentration-dependent manner but not by B17, a structural analog without
effects on Golgi function."* [PMID:10212200]. The *in vivo* substrate preference
is class I ARFs: *"We also have shown that BIG2 has an exchange activity toward
class I ARFs (ARF1 and ARF3) in vivo and inactivation of either ARF exaggerates
the BIG2(E738K)-induced tubulation of endosomal membranes."* [PMID:15385626].

`E738K` is the catalytically dead Sec7 mutant used throughout this literature;
UniProt records its phenotype as *"E->K: Disturbs membrane organization at the
TGN, impairs association of the AP-1 complex and GGA1 with the TGN membranes."*
(`file:human/ARFGEF2/ARFGEF2-uniprot.txt`).

Two localisations, two jobs:

- **trans-Golgi network** — recruits AP-1 and GGA clathrin adaptors via ARF
  activation.
- **recycling endosome** — *"we have revealed that another population of BIG2 is
  associated with the recycling endosome and found that expression of a
  catalytically inactive BIG2 mutant, E738K, selectively induces membrane tubules
  from this compartment"* [PMID:15385626]; and the transferrin-receptor result,
  *"Tfn release appeared unaffected by BIG1 siRNA but was significantly slowed
  from cells treated with BIG2 siRNA alone or plus BIG1 siRNA"* [PMID:16477018].

The BIG1/BIG2 division of labour is explicit and experimentally direct:
*"BIG1 is required to maintain the normal morphology of the Golgi; BIG2 is
important for endosomal compartment integrity and cannot replace the function of
BIG1 in Golgi organization."* [PMID:20360857].

Non-catalytic side: BIG2 is an A-kinase anchoring protein with three R-subunit
binding regions — *"Residues 27-48 (domain A) interacted with RI alpha and RI
beta, 284-301 (domain B) interacted with RII alpha and RII beta, and 517-538
(domain C) interacted with RI alpha, RII alpha, and RII beta."* [PMID:12571360].
Note that domains A/B/C sit in the DCB/HUS half of the protein, well N-terminal
of the Sec7 domain (654–785) — the AKAP function is *not* a property of the
catalytic module.

## The single biggest structural fact about this GOA set

**20 of the 66 GOA rows (13 distinct GO terms) are projections from rat Arfgef2
`Q7TSU1`, and 17 of them rest solely on one paper, `PMID:15198677`** — arriving
twice, once as UniProt ISS (`GO_REF:0000024`) and once as Ensembl Compara IEA
(`GO_REF:0000107`). See `file:human/ARFGEF2/ARFGEF2-bioinformatics/RESULTS.md` §1.

`Q7TSU1` is the genuine rat ortholog (BIG2_RAT, Swiss-Prot, 1791 aa vs the human
1785 aa), so the *form* of the transfer is legitimate; what is worth recording is
that a third of the human annotation set has a single point of failure, and that
two pipelines double-count it.

The donor paper is a real BIG2 study: *"BIG2 is present in both inhibitory
GABAergic synapses that contain GABA(A)Rs and in asymmetric excitatory
synapses."* and *"BIG2 is also present in vesicle-like structures in the
dendritic cytoplasm, sometimes colocalizing with GABA(A)Rs."* [PMID:15198677].
It also carries the GABA(A)R β-subunit interaction and the ER-exit result:
*"In transfected human embryonic kidney cell line 293 cells, BIG2 promotes the
exit of GABA(A)Rs from endoplasmic reticulum."* [PMID:15198677] — note that the
ER-exit experiment was done in **human HEK293 cells**, while the synaptic
localisation is rat brain EM.

**The projection discriminator came back negative**, and that is a finding worth
stating: `PMID:15198677` annotates only **2 entities** in all of GOA (rat Arfgef2
and rat Gabrb3), so this is per-gene curation at figure granularity, not a
complex-membership phenotype distributed across subunits. The synapse rows are
therefore kept, as non-core.

### The one row inside that block I cannot reconcile

`GO:0005879 axonemal microtubule`. Three observations, none individually
decisive:

1. `PMID:15198677`'s abstract describes hippocampal neurons, the TGN, dendritic
   vesicle-like structures and synapses. There is no ciliary or flagellar
   content in it at all. The full text is subscription-only (Europe PMC reports
   `isOpenAccess: N`, `inEPMC: N`, no PMC id), so I could not read the figure
   the annotation rests on.
2. The **rat UniProt entry's own `SUBCELLULAR LOCATION` section, curated from the
   same paper**, records the generic *"Cytoplasm, cytoskeleton"* and lists no
   cilium, axoneme or flagellum anywhere.
3. A measured census (RESULTS.md §6) over 13 accessions — the four human large
   ArfGEFs, with accessions **derived by gene-name lookup** rather than written
   by hand, plus the nine proteins resolvable from this gene's WITH/FROM column
   — finds exactly **one** cilium-compartment holder among the large ArfGEFs,
   and it is ARFGEF2 itself by this very projection. (The first pass of that
   script hardcoded `Q9Y678` as GBF1; it is **COPG1**. The conclusion survived,
   the cohort did not, which is why the accessions are now derived and the
   resolved gene symbol is asserted against the one sought.)

The related, non-ciliary observation that *does* exist for human BIG2 is
cytoplasmic-microtubule and centrosome association: *"endogenous BIG2 and Exo70
in HepG2 cells were visualized at Golgi membranes and apparently at the
microtubule-organizing center (MTOC). Both were identified in purified
centrosomes."* [PMID:15705715].

**And the census returned one result that cuts against my own argument, which is
reported rather than suppressed: EXOC7/Exo70 — the exocyst subunit BIG2 binds and
co-localises with at the MTOC — itself carries `GO:0036064` ciliary basal body.**
BIG2 therefore has a documented partner at the ciliary base, even though BIG2 has
never been looked for there. That does not rescue *axonemal microtubule*, which is
a different compartment from the basal body, but it is exactly why the right
action is to flag and measure rather than to delete, and it is the motivation for
the first suggested experiment.

I have **not** asserted the rat IDA is wrong — I cannot see what the curator saw.
The two human rows are ISS and Compara IEA, so I marked those as over-annotated
and filed the rat row for re-examination as a suggested question.

## `GO:0017022 myosin binding` — right term, wrong evidence chain

`PMID:15644318` is titled *"BIG1 is a binding partner of myosin IXb and regulates
its Rho-GTPase activating protein activity"*, and its abstract is BIG1
throughout: *"Through the yeast two-hybrid screening using the tail domain of
myosin IXb as bait we found BIG1, a guanine nucleotide exchange factor for
ADP-ribosylation factor (Arf1), as a potential binding partner for myosin IXb."*
and *"The interaction between myosin IXb and BIG1 was demonstrated by
co-immunoprecipitation of endogenous myosin IXb and BIG1 with anti-BIG1
antibodies in normal rat kidney cells."* [PMID:15644318].

Querying GOA by that reference (RESULTS.md §2) shows it annotates 7 entities with
18 annotations: **6 on human ARFGEF1**, **0 on human ARFGEF2**, and exactly one
BIG2-family row anywhere — `GO:0017022` on **rat** Arfgef2. Human ARFGEF2's
myosin-binding row is the Compara projection of that single rat row.

**But the term is independently true of BIG2**, from a different paper:
*"Reciprocal coimmunoprecipitation of endogenous HeLa cell BIG1 and BIG2 with
myosin IIA was demonstrably independent of Arf guanine nucleotide-exchange factor
activity"* and, for direct binding, *"After incubation of in vitro-synthesized
BIG2 and NMHC IIA, BIG2 IP collected approximately 1% of added NMHC IIA"*
[PMID:23918382]. So the row is kept (non-core) and the recommendation is to
**re-reference it to `PMID:23918382` with human evidence** rather than delete it.

The same paper draws a clean paralog line that should not be blurred: *"Despite
>70% sequence identity of the two C fragments, no interaction of BIG2-C with
MYPT1 or PP1cδ was detected"* [PMID:23918382]. BIG1 binds the phosphatase
directly; BIG2 binds BIG1 and myosin IIA.

*(Cross-gene note, offered as a claim and not a fact: human ARFGEF1 carries
`GO:0005096 GTPase activator activity` IDA from `PMID:15644318`, whose result is
that BIG1 **inhibits** myosin IXb's GAP activity — *"the GAP activity of myosin
IXb was significantly inhibited by the addition of BIG1 with IC(50) of 0.06
microm"*. ARFGEF1's separate `GO:0034260 negative regulation of GTPase activity`
IDA from the same paper reads the direction the other way. That is ARFGEF1's row,
not this gene's, and the ARFGEF1 review was still an unmodified stub when this
was written, so it is raised as a question rather than acted on.)*

## `GO:0032760` — a receptor/ligand conflation

`PMID:17276987` is about **TNFR1**, the *receptor*: *"We conclude that the
association between BIG2 and TNFR1 selectively regulates the extracellular
release of TNFR1 exosome-like vesicles from human vascular endothelial cells via
an ARF1- and ARF3-dependent mechanism."* [PMID:17276987]. Nothing in it measures
production of the TNF cytokine, and the mechanism it does report is explicitly
*not* proteolysis: *"neither BIG2 nor BIG1 was required for the IL-1beta-induced
proteolytic cleavage of TNFR1 ectodomains"* [PMID:17276987].

`GO:0032760` is *positive regulation of tumor necrosis factor production*, whose
parent `GO:0032680` is about the appearance of TNF itself. The paper's own framing
is that released TNFR1 *"can bind and modulate TNF bioactivity"* — a soluble
decoy receptor, if anything an antagonist. Querying GOA by this reference returns
exactly 2 annotations on 1 entity, both on ARFGEF2, so this is one curator's term
choice and not a propagated error.

Replacement proposed: `GO:1903553 positive regulation of extracellular exosome
assembly`, which is what the constitutive-release result measures.

## Coverage, not over-annotation — the disease-gene trap inverted

The union of the UniProt `RX` list and the affinage citation list is 43
literature PMIDs. **26 produce zero GO annotations anywhere in GOA; 33 produce
zero on ARFGEF2** (RESULTS.md §4). The silent set includes the founding disease
paper [PMID:14647276], the myosin-phosphatase scaffold paper [PMID:23918382],
integrin β1 recycling and migration [PMID:22908276], Filamin A transport
[PMID:16320251], the AP-1/GGA dominant-negative papers, PP1γ regulation, the
RIIβ/TNFR1 AKAP paper, the DCB/HUS homodimer paper, β-catenin S675, and dendritic
Golgi deployment.

Meanwhile GOA carries **no** cerebral-cortex, neuron-migration, neural-progenitor
or heterotopia term for ARFGEF2 at all. The over-annotation-from-pathology
failure mode was specifically looked for and **is not present**. This is the
"uncharacterised rather than over-annotated" diagnosis.

**I deliberately did not propose a neurodevelopmental BP term.** The cell-biology
in [PMID:14647276] rests on brefeldin A (which inhibits GBF1 and BIG1 as well as
BIG2) and on a dominant-negative construct (BIG1 and BIG2 are in the same
macromolecular complex, [PMID:10716990]), so neither isolates BIG2, and the
human genetics establishes a *disease*, not a molecular process. The PVNH2
material belongs in the gene description as disease context and in
`suggested_questions`, not in `existing_annotations`.

The two NEW rows I did propose both come from **human** siRNA experiments in
HeLa cells with reversal controls, so the evidence code is IMP and the species is
right:

- `GO:0051497 negative regulation of stress fiber assembly` — *"Stress fibers
  were significantly more prominent after BIG1 or BIG2 depletion than in control
  cells"* [PMID:23918382].
- `GO:0030335 positive regulation of cell migration` — *"Motility of HeLa cells
  transfected with BIG1 or BIG2 siRNA was significantly impaired relative to that
  of cells transfected with NT siRNA, and overexpression of BIG1 or BIG2,
  full-length or C fragment, but not N or S fragments, reversed those effects"*
  [PMID:23918382], corroborated independently by *"Treatment of HeLa cells with
  BIG2 siRNA resulted in perinuclear accumulation of integrin β1 and its delayed
  return to the cell surface. Motility of BIG2-depleted cells was simultaneously
  decreased"* [PMID:22908276].
- `GO:0034067 protein localization to Golgi apparatus` — *"we have demonstrated
  that AMY-1 is associated with the TGN through interacting with BIG2 but not
  with BIG1 using an RNA interference approach"* [PMID:16866877].

## `GO:0005085` is already maximal

`GO:0005086` *ARF guanyl-nucleotide exchange factor activity* **no longer exists
as a distinct term**: QuickGO's `complete` record for `GO:0005085` lists
`GO:0005086`–`GO:0005090`, `GO:0008321`, `GO:0008433`, `GO:0016219`, `GO:0016220`,
`GO:0017034`, `GO:0017112`, `GO:0017132`, `GO:0019839` and `GO:0030676` among its
`secondaryIds` — every substrate-specific GEF term was merged in. So there is no
child to propose, and proposing one would recreate what GO deliberately merged.
The ARF1/ARF3 preference is recorded machine-readably instead, via
`core_functions[].substrates` and a `has_input` (`RO:0002233`) extension.

The `GO:0005085` IBA node is also genuinely heterogeneous — GNOM, Sec71, garz,
cytohesins, PSD/PSD3, IQSEC2, yeast GEA1/GEA2/SEC7/MON2/SYT1 — so the general
term is the LCA of the donor set, not lazy curation. `GRANULARITY_MISMATCH` does
not apply.

## Per-partner disposition of the 10 `GO:0005515` rows

Decided per partner, not per gene (all partner accessions resolved to reviewed
canonical entries of the expected length — no TrEMBL or ORFeome substitutions):

| partner | rows | disposition |
|---|---|---|
| `Q9Y6D6` ARFGEF1 | 4 (`PMID:10716990`, `19332778`, `22084092`, `35271311`) | real and heavily replicated (UniProt `NbExp=14`); still uninformative as `protein binding` → REMOVE the generic rows, keep the fact in `core_functions.in_complex` |
| `Q99417` MYCBP | 4 (`PMID:16866877`, `33961781`, `35271311`, `40205054`) | one targeted study plus three orthogonal proteome-scale screens; MODIFY to the functional consequence (`GO:0034067`) rather than keep `protein binding` |
| `Q9UPT5-1` EXOC7 | 1 (`PMID:15705715`) | real (Y2H + co-IP of *in vitro*-translated fragments), but no informative MF term exists for exocyst binding → REMOVE as uninformative |
| `Q14432` PDE3A | 1 (`PMID:19332778`) | real, part of the AKAP/cAMP module → REMOVE as uninformative, function captured by `GO:0034237` |

`GO:0005515` removal here means "the generic term carries no functional
information", not "the interaction is false" — each interaction is stated in the
`reason` and, where it supports one, in a replacement term.

## Things I checked that came back negative

- **Retraction / erratum check.** None of the PMIDs relied on here carries a
  retraction, erratum or expression-of-concern notice in its cached PubMed
  record.
- **Non-numeric PMID tokens in the affinage record.** None; all 24 citations are
  numeric PubMed ids.
- **affinage recall.** The record is good on this gene (24 citations, all real),
  but it did **not** surface `PMID:15198677` — the rat paper behind 17 of the 66
  GOA rows — nor `PMID:15644318`, the BIG1/myosin-IXb paper behind the myosin
  row. Both were found only by resolving WITH/FROM and querying QuickGO by
  reference. Its `## Citations` list has no `gates_passed` key at all; the
  frontmatter reports `faith_pct: 100.0` and `self_evaluation_pairwise: win`,
  which are precision signals and say nothing about recall.
- **Complex-projection check** on the synapse block: negative (2 entities).
- **Partner-accession check**: negative (no TrEMBL/partial-clone substitutions).
- **Dead-accession check**: negative (all 45 WITH/FROM tokens resolved, 0 dead).
