# ARFGEF1 (BIG1, Q9Y6D6) — review notes

Human `ARFGEF1` encodes BIG1 (brefeldin A-inhibited guanine nucleotide-exchange
protein 1), a 1849-aa peripheral membrane protein of the large, BFA-sensitive
Arf-GEF family. `PE 1: Evidence at protein level`; `3D-structure` keyword; an
OMIM disease (DEDISB, MIM 619964).

## 1. What the protein does

**Catalysis is real, measured, and domain-mapped.** UniProt places a single
`SEC7` domain at residues **709..840** (`ECO:0000255|PROSITE-ProRule:PRU00189`),
and the activity has been measured directly on the human protein:

> "A 39-kDa fragment spanning the Sec7 domain catalyzed loading of guanosine
> 5'-[gamma-thio]triphosphate onto class I ARFs and displayed clear sensitivity
> to BFA."
> [PMID:10393931]

The same paper establishes the drug mechanism that names the family:

> "BFA did not compete with ARF for interaction with p200 but, rather, acted as
> an uncompetitive inhibitor that only targeted the p200-ARF complex with an
> inhibition constant of 7 microM."
> [PMID:10393931]

Substrates are the class I ARFs. UniProt FUNCTION: `Promotes guanine-nucleotide
exchange on ARF1 and ARF3.` The 2008 nucleolar paper restates it:

> "BIG1, a brefeldin A-inhibited guanine nucleotide-exchange protein, activates
> class I ADP-ribosylation factors (ARF1-3) by catalyzing the replacement of
> bound GDP by GTP"
> [PMID:18292223]

This is *not* a name-implied activity of the kind this campaign keeps finding.
The catalytic domain is present, the assay was done on the human protein, and
the drug sensitivity is quantitative.

**BIG1 is explicitly not a GAP.** GOA carries `NOT|enables GO:0005096` by IDA.
The underlying result is that BIG1 *inhibits* another protein's GAP activity:

> "the GAP activity of myosin IXb was significantly inhibited by the addition of
> BIG1 with IC(50) of 0.06 microm"
> [PMID:15644318]

and the mechanism is steric competition:

> "These results suggest that BIG1 and RhoA compete with each other for the
> binding to myosin IXb, thus resulting in the inhibition of the GAP activity by
> BIG1."
> [PMID:15644318]

So the `GO:0034260 negative regulation of GTPase activity` IDA and the
`NOT GO:0005096` are two halves of one coherent result, not a contradiction.

**A GEF-independent structural role at the Golgi.** Depleting BIG1 fragments the
Golgi without blocking cargo export:

> "suppression of BIG1 induces the formation of Golgi mini-stacks still
> polarized and functional in terms of cargo export"
> [PMID:20360857]

> "BIG1 is required to maintain the normal morphology of the Golgi; BIG2 is
> important for endosomal compartment integrity and cannot replace the function
> of BIG1 in Golgi organization."
> [PMID:20360857]

UniProt records the same non-catalytic reading: `Required for the maintenance of
Golgi structure; the function may be independent of its GEF activity.`

**Recruitment.** Arl1 recruits BIG1 to the trans-Golgi through the DCB domain,
with a crystal structure and a mutational map:

> "We find that Arl1 binds to the dimerization and cyclophilin binding (DCB)
> domain in BIG1 and report a crystal structure of human Arl1 bound to this
> domain. Residues in the DCB domain that bind Arl1 are required for BIG1 to
> locate to the Golgi in vivo."
> [PMID:27373159]

Four UniProt `MUTAGEN` entries cite this paper — K105D, Y109K, L156D and Q200E —
all recorded as abolishing the ARL1 interaction, and a second, independent
crystal structure exists [PMID:27436755]. A third paper shows the requirement in
cells [PMID:22291037].

**Oligomerisation.** The same DCB domain drives homodimerisation:

> "Our data demonstrate a strong interaction between DCB domains within GBF1,
> BIG1, and BIG2 to maintain homodimers and an interaction between DCB and HUS
> domains within each homodimer."
> [PMID:17640864]

UniProt SUBUNIT: `Homodimer (PubMed:17640864).`

**Scaffolding, GEF-independently.** BIG1 anchors a myosin phosphatase complex:

> "Reciprocal coimmunoprecipitation of endogenous HeLa cell BIG1 and BIG2 with
> myosin IIA was demonstrably independent of Arf guanine nucleotide-exchange
> factor activity"
> [PMID:23918382]

> "by anchoring or scaffolding the assembly, organization, and efficient
> operation of multimolecular myosin phosphatase complexes that include myosin
> IIA, protein phosphatase 1δ, and myosin phosphatase-targeting subunit 1, BIG1
> and BIG2 serve to integrate diverse biophysical and biochemical events in
> cells."
> [PMID:23918382]

and the related AKAP role is what `GO:0034237 protein kinase A regulatory
subunit binding` records. UniProt hedges it (`Proposed to act as A
kinase-anchoring protein (AKAP)`) but asserts the binding experimentally:
`Interacts with PRKAR1A and PRKAR2A (PubMed:12571360).`

**Regulation.** PKA phosphorylation of Ser-883 reduces GEF activity and is
reversed by PP1γ [PMID:17360629]; the same site plus a `711..715` NLS drives
cAMP-induced nuclear accumulation [PMID:16467138] (UniProt `MUTAGEN 883 S->A:
Abolishes cAMP-induced nuclear localization.`). PDE3A-containing AKAP complexes
keep local cAMP low so the GEF stays active [PMID:19332778].

**Traffic step.** Double knockdown of BIG1 and BIG2 in human cells blocks an
identified retrograde route:

> "knockdown of both BIG2 and BIG1 by RNAi causes mislocalization of a subset of
> proteins associated with the TGN and recycling endosomes and blocks retrograde
> transport of furin from late endosomes to the TGN"
> [PMID:18417613]

Cell line confirmed from the PMC full text ("HeLa cells were cultured in minimal
essential medium…", Materials and Methods), so an IMP on the human gene is
species-correct.

## 2. Findings that changed the review

### 2.1 `GO:0005086 ARF guanyl-nucleotide exchange factor activity` no longer exists

This gene's single most characteristic fact — that it is an **ARF**-specific GEF
— cannot be stated in GO's molecular-function branch any more.

QuickGO `/ontology/go/terms/GO:0005086/complete` resolves to
**`GO:0005085 guanyl-nucleotide exchange factor activity`**, and `GO:0005085`
lists as `secondaryIds`:

```
GO:0005086 GO:0005087 GO:0005088 GO:0005089 GO:0005090 GO:0008321 GO:0008433
GO:0016219 GO:0016220 GO:0017034 GO:0017112 GO:0017132 GO:0019839 GO:0030676
```

i.e. the ARF, Rho, Ras, Ran, Rab and Rac substrate-specific GEF terms were all
merged into the generic parent. `GO:0005085` now has **no substrate-specific
`is_a` children at all** — its only children are `GO:1905098` (a regulation
term, `negatively_regulates`) and `GO:0032045` (`capable_of`). An OLS search for
"ARF guanyl-nucleotide exchange factor activity" returns only `GO:0005085`.

This is the same merge the campaign already documented on the GAP side
(`GO:0008060 ARF GTPase activator activity` → `GO:0005096`). So `GO:0005085` is
**already maximal**: ACCEPT it, do not propose a child, and record the substrate
machine-readably instead (`extensions` `RO:0002233` has_input, and
`core_functions[].substrates`). Reproduced by
`ARFGEF1-bioinformatics/check_terms.py` → `term_status.json`.

Corroborating observation: across the 18 protein donors of ARFGEF1's
`GO:0005085` IBA — yeast Sec7/Gea1/Gea2/Syt1/Mon2, *Arabidopsis* GNOM,
*Drosophila* Sec71/garz, human/mouse cytohesins, PSD, PSD3, IQSEC2, ARFGEF2 —
**every single one holds `GO:0005085` and not one holds any descendant**
(`donor_evidence.tsv`). That is what a fully merged branch looks like from the
annotation side.

### 2.2 `GO:0030532 small nuclear ribonucleoprotein complex` is the wrong RNA class

`GO:0030532` is annotated `part_of` by IDA from [PMID:18292223]. That paper is
about **U3 small nucleolar RNA**, not a small nuclear RNA:

> "(32)P labeling of RNAs immunoprecipitated with BIG1 or nucleolin from nuclei
> revealed bands of approximately 210 bases that also hybridized with U3 small
> nucleolar (sno)RNA-specific oligonucleotides."
> [PMID:18292223]

The term definitions settle it. `GO:0030532` requires "at least one RNA of the
small nuclear RNA (snRNA) class"; `GO:0005732 sno(s)RNA-containing
ribonucleoprotein complex` is "A ribonucleoprotein complex that contains an RNA
molecule of the snoRNA family and associated proteins." They are sibling
`is_a` children of `GO:0030529 ribonucleoprotein complex`, so this is not a
granularity question — it is the wrong sibling. Almost certainly a
`sno` → `sn` transcription slip. **MODIFY → `GO:0005732`.**

I did not go further to `GO:0031428 box C/D methylation guide snoRNP complex`.
U3 is a box C/D snoRNA, but it guides pre-rRNA **cleavage**, not 2'-O-methylation,
and `GO:0031428`'s definition requires the complex be "capable of
ribose-2'-O-methylation of target RNAs". `GO:0005732` is the honest level.

The paper is also careful, and the review should be too: the co-IP was abolished
by RNase A or DNase, so the association is nucleic-acid-dependent, and the
authors write only that the components "may exist together in nuclear
complexes". `part_of` is retained because that is the curator's call and the
term is being corrected, not the claim.

### 2.3 A paralog shadow set on MYO9A from PMID:15644318

`GO:0017022 myosin binding` appears twice on ARFGEF1 from [PMID:15644318], once
with `UniProtKB:Q13459` (MYO9B) and once with `UniProtKB:B2RTY4` (**MYO9A**).
The paper's title, abstract and every described experiment concern **myosin
IXb**; myosin IXa is never mentioned in the abstract.

Querying GOA *by reference* rather than by gene shows the shape of the problem
(`reference_annotations.tsv`, 18 rows for this PMID):

| gene product | term | qualifier | ev | with/from |
|---|---|---|---|---|
| MYO9B `Q13459` | GO:0005096 | enables | IDA | — |
| MYO9B `Q13459` | GO:0032011 | **NOT**\|involved_in | IDA | — |
| MYO9B `Q13459` | GO:0005515 | enables | IPI | RHOA `P61586` |
| MYO9B `Q13459` | GO:0005515 | enables | IPI | ARFGEF1 `Q9Y6D6` |
| **MYO9A `B2RTY4`** | GO:0005515 | enables | IPI | RHOA `P61586` |
| **MYO9A `B2RTY4`** | GO:0005515 | enables | IPI | ARFGEF1 `Q9Y6D6` |
| RHOA `P61586` | GO:0017022 | enables | IPI | MYO9B `Q13459` |
| RHOA `P61586` | GO:0005515 | enables | IPI | **MYO9A `B2RTY4`** |
| ARFGEF1 `Q9Y6D6` | GO:0017022 | enables | IPI | MYO9B `Q13459` |
| ARFGEF1 `Q9Y6D6` | GO:0017022 | enables | IPI | **MYO9A `B2RTY4`** |

MYO9A has acquired an exact copy of MYO9B's *partner* set (RHOA and ARFGEF1) but
none of MYO9B's *functional* rows (`GO:0005096`, the `NOT GO:0032011`) — the
signature of an accession slip rather than a second protein having been assayed.

**I did not act on this as a removal.** The cached record is abstract-only
(`full_text_available: false`) and the JBC full text returns HTTP 403, so I
cannot see what the curator saw; the campaign rule is explicit that an
experimental annotation is not overruled from an abstract. Checked and excluded
alternatives: `B2RTY4`'s twelve secondary accessions do **not** include `Q13459`
or any of its secondaries, so this is not an accession-identity migration. The
row's *term* is in any case correct for BIG1 — `GO:0017022` is independently
established by the MYO9B row and by the myosin IIA co-IP in [PMID:23918382]. So
the MYO9A row is **UNDECIDED**, and the observation is filed as a question for
the assigning curator, naming all four affected annotations across three genes.

### 2.4 The GOA record is a coverage problem, not an over-annotation problem

`literature_coverage.py` takes the union of the affinage citation block and
every `RX PubMed=` line in the UniProt entry (48 PMIDs) and asks QuickGO how
many GO annotations each reference supports anywhere. Restricted to the 26
functional papers affinage returned:

| bucket | n | PMIDs |
|---|---|---|
| annotate ARFGEF1 | 6 | 14973189, 15644318, 17227842, 18292223, 19332778, 20360857 |
| annotate only other genes | 3 | 22291037, 23386609, 24090963 |
| no GO annotation anywhere | **17** | 10393931, 12606707, 16467138, 17360629, 17640864, 18417613, 23220274, 23918382, 24198228, 27162341, 27834853, 28414797, 29740613, 31678406, 32415087, 35090882, 36562883 |

The most striking single entry is **PMID:10393931**, the paper that measured the
Sec7 fragment loading GTPγS onto class I ARFs and determined the BFA inhibition
constant. It is the best molecular-function experiment ever done on the human
protein and it has produced **zero** GO annotations. The `GO:0005085` IDA on
ARFGEF1 instead cites [PMID:15644318], a myosin IXb paper.

Also absent from GO: the entire PKA/PP1γ regulatory switch (16467138, 17360629),
the homodimer (17640864), both Arl1 crystal structures (27373159, 27436755), the
retrograde-transport step (18417613) and the myosin-phosphatase scaffold
(23918382). Four of these are the basis of this review's `NEW` rows.

### 2.5 `GO:0006887 exocytosis` is not supported for BIG1

Two rows: a `TAS` from [PMID:10212200] (assigned by ProtInc in 2003) and an
`ARBA` IEA. PMID:10212200 is the BIG1/BIG2 cloning paper; its only relevant
statements are background about the family — "ARFs ... play an important role in
intracellular vesicular trafficking" and BFA "blocks protein secretion" — and
its one biochemical assay is on **BIG2**, not BIG1:

> "BIG2, synthesized as a His6 fusion protein in Sf9 cells, accelerated guanosine
> 5'-3-O-(thio)triphosphate binding by recombinant ARF1, ARF5, and ARF6."
> [PMID:10212200]

`GO:0006887`'s definition ends "and ends when molecules are secreted from the
cell". No experiment on human BIG1 has measured the plasma-membrane fusion step.
Where BIG1 has been implicated in surface delivery it is of *integral membrane*
cargo — ABCA1 [PMID:23220274], GABA-A receptors [PMID:24198228] — which is
`GO:0006893 Golgi to plasma membrane transport`, a sibling that "precedes
exocytosis" by its own definition. Both rows → `MARK_AS_OVER_ANNOTATED`;
`GO:0016192` (already annotated, IBA) is the supported level.

### 2.6 `GO:0090303 positive regulation of wound healing` overshoots the assay

`GO:0090303` is defined at tissue level: "the series of events that restore
integrity to a damaged tissue, following an injury." What [PMID:22084092]
measured is a scratch assay on a cell monolayer:

> "Treatment of cells with BIG1- or KANK1-specific siRNA interfered significantly
> with directed cell migration and initial orientation of Golgi/MTOC toward the
> leading edge, which was not mimicked by KIF21A depletion."
> [PMID:22084092]

MODIFY → `GO:0030335 positive regulation of cell migration`. The companion row
from the same paper, `GO:2000114 regulation of establishment of cell polarity`,
is accepted unchanged — Golgi/MTOC reorientation is exactly what that term
covers, and it is the half of the phenotype that *was* measured directly.

## 3. Checks that came back negative — recorded so they are not re-run

* **Partner identity.** All 12 `GO:0005515` IPI partner accessions resolve to
  **reviewed (Swiss-Prot) canonical entries** with lengths matching the
  canonical protein; no TrEMBL fragments, no partial ORFeome clones
  (`partner_checks.tsv`). Two tokens are isoform-suffixed (`Q13459-2`,
  `Q7Z4S6-2`) and both resolve to the right gene.
* **`NbExp` inflation.** Expanding the IntAct records and counting distinct
  (publication, detection-method) pairs rather than `NbExp` did **not** collapse
  any partner to a single screen logged several ways. ARFGEF2 6 experiments /
  4 publications (MI 0.84), MYCBP 6/4 (0.79), KIF21A 6/2 (0.71). The thin ones
  are NCL (1 experiment) and TBC1D22B (1 record, spoke-expanded, MI 0.35);
  NCKAP1L, TBC1D22A and rat Dpy30 have no IntAct record at all.
* **Projection from a complex.** No reference in ARFGEF1's GOA shows the
  ACTR8-style signature. Every functional reference annotates 1–4 entities
  (`reference_scope.tsv`). The three large references (BioPlex 9514
  annotations, OpenCell 2876, multimodal cell maps 3026) are paginated, so entity
  counts are reported as unavailable rather than derived from one page; all three
  contribute only `GO:0005515`.
* **Donor evidence for propagated rows.** 43 of 44 (donor, term) pairs carry the
  donor's **own** experimental evidence for the propagated term
  (`donor_evidence.tsv`). The one exception is *Dictyostelium* `Q86KG9`, which
  holds `GO:0016192` by IBA only. No propagated row could be argued down on
  "the source only carries the same family-level inference".
* **Self-referential IBA.** `GO:0007030` IBA lists `UniProtKB:Q9Y6D6` in its own
  WITH/FROM. That is a PAINT curator judging the function core using ARFGEF1's
  own IMPs, not circularity. `root_cause: NO_FAILURE_CORE`.
* **IBA node heterogeneity.** `PTHR` node `PTN008950430` carries both
  `GO:0016192` and `GO:0005085` and spans the whole Sec7 superfamily — large
  BFA-sensitive GEFs, cytohesins, EFA6/PSD, BRAG/IQSEC, and yeast Mon2. At that
  depth `GO:0016192 vesicle-mediated transport` is the genuine LCA (the donors'
  own terms are spread over `GO:0006888`, `GO:0006890`, `GO:0006891`,
  `GO:0006893`, `GO:0006895`, `GO:0042147`, `GO:0016197`, `GO:0048193`), so
  "too general" would be the wrong criticism. ACCEPT.
* **A lipid-affinity screen hit deliberately not imported.** IntAct records
  ARFGEF1 against PI(3)P (`CHEBI:17283`, pull down, [PMID:23416715]). That study
  reports "the identification of 681 proteins/protein complexes which interact
  with PI(3)P", ARFGEF1 has no FYVE, PX or PH domain in its InterPro content, and
  there is no GOA row. No `GO:0032266` proposed.
* **Retractions / errata.** None of the PMIDs relied on here carries a
  retraction, erratum or expression-of-concern note in its cached record.
* **Paralog cross-check.** `ARFGEF2` is not yet reviewed in this repository, so
  no sibling review exists to reconcile against. GBF1 carries `GO:0042147` by
  IMP, which is the comparator that licenses the same term on ARFGEF1.

## 4. Things a curator should look at

* The `GO:0005085` IDA on ARFGEF1 cites [PMID:15644318]; [PMID:10393931] is the
  paper that actually measured the exchange reaction and the BFA inhibition
  constant on the human protein, and it carries no GO annotation at all.
* The MYO9A rows from [PMID:15644318] (§2.3).
* `interpro2go` maps `IPR000904` (Sec7 domain) to `GO:0032012 regulation of ARF
  protein signal transduction`. Every characterised Sec7-domain protein is an
  *activator*, and `GO:0032014 positive regulation of ARF protein signal
  transduction` exists. Whether the mapping can be sharpened family-wide is a
  question for InterPro, not something to assert from one gene — but the
  per-gene MODIFY is warranted here because the direction is measured
  [PMID:10393931].
* `UniProtKB:Q8K3E7` (rat Dpy30, 99 aa) is the named partner of an `IPI` on the
  **human** gene from [PMID:19651892]. The row is being removed as uninformative
  anyway, but the species mismatch is worth a curator's eye.
* ARFGEF1 haploinsufficiency causes DEDISB (MIM 619964) with seizures in about
  half of affected individuals [PMID:34113008]; the mouse model attributes the
  lowered seizure threshold to reduced surface GABA-A receptors [PMID:31678406].
  The human-cell counterpart of that trafficking defect has not been shown, and
  [PMID:24198228] does not state the species of the neurons used — which is why
  no GABA-A trafficking row was added here.

## 5. Provenance for the analyses

All scripts are committed under `ARFGEF1-bioinformatics/` and run from the repo
root with `uv run python`. See that folder's `README.md` for what each produces
and `RESULTS.md` for the numbers quoted above.
