# AFP (human, P02771) — review notes

Working journal for the PAINT + affinage review. Provenance is recorded inline as
`[PMID:xxxxx "verbatim"]`.

## The framing problem: a biomarker is not a function

AFP is one of the most-measured proteins in clinical medicine — second-trimester maternal
serum screening, hepatocellular carcinoma surveillance, germ-cell tumour staging. Almost all
of that literature measures **concentration as a readout**. None of it establishes a molecular
function or a biological process. The review keeps three things apart:

1. **what the protein does** — reversible binding of small hydrophobic and metal ligands, the
   albumin-fold carrier activity;
2. **where/when it is expressed** — yolk sac and fetal liver, re-expressed in HCC and
   AFP-producing gastric cancer. Expression is not function;
3. **what clinicians use it for** — not annotatable at all.

The affinage record is almost entirely category (2) and (3). Of its 17 citations, a large
block (FOXM1, HBP1/HBx, gp96/NR5A2, the −119 HNF1 promoter variant) is about the *transcriptional
regulation of the AFP gene*, which is a function of those regulators, not of AFP.

## Family and PANTHER node — verified, not assumed

- UniProt: `Belongs to the ALB/AFP/VDB family.` (`AFP-uniprot.txt` line 208)
- PANTHER **PTHR11385 "SERUM ALBUMIN-RELATED"**, cached metadata `proteins: 2724`, of which
  the cached `PTHR11385-entries.csv` holds **43 reviewed (Swiss-Prot) members** — i.e. the
  entries file is the Swiss-Prot subset (1.6% of the family), not the family.
- Exactly **four human members**, one per subfamily:
  | gene | acc | PANTHER subfamily |
  |---|---|---|
  | ALB | P02768 | PTHR11385:SF15 ALBUMIN |
  | **AFP** | **P02771** | **PTHR11385:SF7 ALPHA-FETOPROTEIN** |
  | GC | P02774 | PTHR11385:SF11 VITAMIN D-BINDING PROTEIN |
  | AFM | P43652 | PTHR11385:SF14 AFAMIN |

## The ALB check the brief asked for: yes, ALB's accession is in the WITH/FROM

Both IBA rows cite `PANTHER:PTN000147344` with **human serum albumin `UniProtKB:P02768`** among
the seeds. Resolved every token:

| token | identity | status |
|---|---|---|
| UniProtKB:P02768 | ALB, *Homo sapiens*, 609 aa | Swiss-Prot |
| UniProtKB:P02769 | ALB, *Bos taurus*, 607 aa | Swiss-Prot |
| UniProtKB:P08835 | ALB, *Sus scrofa*, 607 aa | Swiss-Prot |
| UniProtKB:P19121 | ALB, *Gallus gallus*, 615 aa | Swiss-Prot |
| UniProtKB:P02774 | GC / vitamin D-binding protein, human, 474 aa | Swiss-Prot |
| UniProtKB:P43652 | AFM / afamin, human, 599 aa | Swiss-Prot |
| RGD:2085 | rat **Alb** (REST API: `"symbol":"Alb"`) | — |
| RGD:2667 | rat **Gc** (REST API: `"symbol":"Gc"`) | — |
| PANTHER:PTN000147344 | internal tree node, not a protein | — |

**Zero AFP-subfamily proteins are seeds on either row.** Not one AFP from any species. So
everything AFP inherits phylogenetically is inherited from albumin, vitamin-D-binding protein
and afamin.

(RGD tokens return HTTP 400 from QuickGO's `geneProductId`; resolved instead through the RGD
REST API for identity and through the rat UniProt accessions P02770/P04276 for evidence.)

## The whole PAINT picture for PTHR11385 is seven IBD assignments

From `interpro/panther/PTHR11385/PTHR11385-paint.tsv`:

| node | term | seeds |
|---|---|---|
| PTN000147344 (family root) | GO:0036094 small molecule binding (F) | 8 |
| PTN000147344 (family root) | GO:0031667 response to nutrient levels (P) | 4 |
| PTN000147369 | GO:0008431 **vitamin E** binding (F) | AFM |
| PTN000147369 | GO:0051180 vitamin transport (P) | AFM |
| PTN002604574 | GO:0005499 **vitamin D** binding (F) | GC + rat Gc |
| PTN002604574 | GO:0042359 vitamin D metabolic process (P) | mouse Gc |
| PTN008319942 | GO:1903981 **enterobactin** binding (F) | human + bovine ALB |

The design is coherent and, for the MF branch, correct: the **LCA goes at the root, the
specific ligand goes at the subfamily node**. Afamin's node gets vitamin E, GC's node gets
vitamin D, albumin's node gets enterobactin.

**The reciprocal half of the check (the brief's "which node's reach is exactly my gene set?"):
PTHR11385:SF7, the alpha-fetoprotein subfamily, carries nothing at all.** AFP is the one human
member of this family with no subfamily-level PAINT assignment, so it inherits the general
parent and no ligand term — while its three paralogs each got theirs. And `GO:0005504 fatty
acid binding` — the one ligand demonstrated for ALB (2 IDAs), for human AFP (below) and for
mouse Afp — sits at **no node at all**.

This is the AADACL2/3/4 "right term, wrong node" shape in a new guise: not a misplaced term,
but a **missing** one at a node that exists.

## What has actually been measured on human AFP (as opposed to inherited from ALB)

This is the question the brief asked, and the answer is: more than GOA records.

**Copper.** `[PMID:80265 "Alpha-fetoprotein bound 1 mol of copper(II) ion per mol of protein
above pH 6.0"]`, by equilibrium dialysis and gel filtration on AFP purified **from human
umbilical cord serum and from hepatoma ascites** — not recombinant, not a family inference.
The site was mapped by chemistry: `[PMID:80265 "Photooxidation of alpha-fetoprotein in the
presence of methylene blue resulted in the loss of the copper(II)-binding ability of the
protein in parallel with the destruction of the histidyl residues."]` and reconstituted:
`[PMID:80265 "A synthetic amino-terminal undecapeptide of alpha-fetoprotein also bound
copper(II) ion."]` UniProt encodes exactly this as `FT BINDING 22 /ligand="Cu(2+)"
/evidence="ECO:0000269|PubMed:80265"`. **GOA has no copper term.**

**Bilirubin.** `[PMID:89900 "1 mol of each alpha-fetoprotein bound 1 mol of bilirubin at pH
8.3"]` with Kd 2.6–7.4 × 10⁻⁷ M by two independent methods (difference spectrum and the
Jacobsen peroxidase assay), again on cord-serum and hepatoma-ascites AFP. **GO has no
`bilirubin binding` MF term at all** — see the proposed term below.

**Fatty acids and zinc — the paper nobody cited.** `PMID:38678117` (*Commun Biol* 2024, PDB
**8X1N**) is the first structure of human AFP and it is the single most function-relevant paper
on this gene. `[PMID:38678117 "We observed and identified certain structural features of AFP,
including N-glycosylation at Asn251, four natural fatty acids bound to distinct domains, and
the coordination of metal ions by residues His22, His264, His268, and Asp280."]` The fatty
acids were identified chemically, not modelled from shape: `[PMID:38678117 "According the
results of GC-MS, it was identified that palmitic acid (C16:0) was the most abundant FA bound
to AFP"]` — 57.42% of total FA, with stearate the other major peak — at four sites,
`[PMID:38678117 "These FA binding sites are located in AFP substructures IIA, IIA/IIB, IIIA,
and IIIB, respectively"]`. The metal was not supplied by the experimenters:
`[PMID:38678117 "the presence of metal ions was not intentionally introduced during the protein
extraction process"]`, and His22 is the same residue UniProt already annotates as the Cu(2+)
ligand from the 1978 paper. Caveat recorded honestly in the review: the authors note
`[PMID:38678117 "This could be due to the presence of multiple metal ions at this binding site,
and the metal ion density being obtained through an averaging algorithm"]`.

**This paper is absent from GOA and absent from the affinage report.** It is the campaign's
recall lesson exactly: `gates_passed: True` certifies precision, never recall.

Measured rather than asserted (computed in `AFP-bioinformatics/audit_afp_claims.py`'s sibling
step and recorded in `references[].reference_review`): affinage returned **17** citations, of
which **0** appear in AFP's GOA record and **1** (`PMID:33009373`) is cited in this review. It
missed `PMID:38678117` and both 1970s ligand papers. Its gates passed and all 17 ids are numeric
PubMed identifiers with no bioRxiv DOIs in PMID-shaped fields, so its *precision* is fine — the
failure is entirely one of recall and of framing. A large part of its narrative is the
transcriptional regulation of the *AFP gene* by FOXM1, HBP1/HBx, gp96/NR5A2 and the −119 HNF1
promoter variant, which are functions of those regulators and not of alpha-fetoprotein, and the
remainder is HCC cell biology in which AFP concentration is the readout. **Ligand binding — what
the protein actually does — is absent from the record entirely.**

## `GO:0031667 response to nutrient levels` — the row that does not survive reading its sources

The productive technique from the brief ("go one level deeper than the donor") pays off here.
The IBA reaches AFP from four non-node donors (human/rat/chicken ALB, rat Gc). Querying each
donor's *own* evidence under the term:

- **human ALB P02768**: its `GO:0031667` is itself the same IBA. Its only experimental rows in
  the branch are `GO:0009267` IDA `PMID:16245148` and `GO:0072732` IDA `PMID:16153637`.
- **rat Alb P02770**: `GO:0007584` **IEP** `PMID:20227002`; everything else ISS/ISO **from human
  ALB**.
- **chicken ALB P19121**: `GO:0009267` and `GO:0072732` both **ISS from human ALB**; its one
  IDA in the branch is `GO:0033189` response to vitamin A.

So the apparent breadth is one experiment re-counted. Reading the three primary papers:

1. `PMID:16245148` — *Production of human serum albumin by sugar starvation induced promoter and
   rice cell culture.* `["Mature form of HSA was expressed under the control of the sucrose
   starvation-inducible rice alpha Amy3 promoter"]`. **The starvation response belongs to the
   rice αAmy3 promoter; albumin is the recombinant cargo protein.** A biotechnology yield paper
   has become a `cellular response to starvation` IDA on the cargo.
2. `PMID:16153637` — `["In serum-free medium, albumin (29 or 49 mg/ml) fully prevented the
   apoptotic effects of dotarizine, flunarizine and cyclopiazonic acid."]` Exogenous albumin at
   29–49 mg/ml as a culture-medium supplement, against **drug-induced ER Ca²⁺ release**. That is
   not a nutrient level.
3. `PMID:20227002` — `["there was a restoration of serum glucose, total protein, and albumin
   concentrations, which were reduced by fetal malnutrition"]`. Albumin **concentration as a
   nutritional-status readout**. This is the biomarker fallacy in the donor set itself.

Add AFP's own biology: two independent human families carry null *AFP* alleles and
`[PMID:15280901 "The affected individuals were asymptomatic and presented normal development."]`,
`[PMID:18854864 "Despite this, fetal development and birth were normal."]`

Verdict: **REMOVE**, with a PAINT recommendation stated once at the node level — the term reaches
every member of PTHR11385 from PTN000147344, so the fix belongs upstream, not on AFP alone.

## `GO:0036094 small molecule binding` — general because the node is heterogeneous, i.e. correct

The AADACL4 corrective applies. Before calling a broad term "too general", check whether the
donors agree. They do not: ALB holds `GO:0005504` fatty acid (IDA ×2), `GO:0030170` pyridoxal
phosphate (IDA), `GO:0019825` oxygen (IDA), `GO:1903981` enterobactin (IDA), `GO:0005507`
copper (NAS); GC holds vitamin D; AFM holds vitamin E. The LCA of {fatty acid, pyridoxal
phosphate, oxygen, enterobactin, copper, vitamin D, vitamin E} **is** `GO:0036094`. Verified via
QuickGO ancestry that both `GO:0005504` and `GO:0005507` are descendants of `GO:0036094`
(ion binding sits under small molecule binding in current GO — I had this wrong from memory and
checked it).

So `GO:0036094` is the ontology and PAINT working correctly. **ACCEPT**, and make the review
additive rather than corrective: supply AFP's own measured ligands as `NEW`.

## The rodent function that must NOT be transferred — and the check that came back negative

Mouse *Afp* is the textbook case of an AFP function, and it is **estrogen-driven**:
`[PMID:12297623 "Whereas mutant homozygous adult males are viable and fertile, AFP null females
are infertile."]`, `[PMID:12297623 "It is most likely that AFP acts by virtue of its capacity to
bind estrogen, because the infertility phenotype of the Afp knockout mice resembles that of
female animals exposed perinatally to estrogens"]`; extended by `PMID:16388309` to protection of
the developing female brain from masculinization. Mouse UniProt P02772 FUNCTION is literally
`Binds estrogens, fatty acids and metals`.

Human AFP does not have this property — UniProt states that only a small percentage (less than
2%) of human AFP shows estrogen-binding properties — and human AFP nulls are asymptomatic.

**Predicted defect: the rodent reproductive phenotype leaking into human AFP by ISO/IBA.
Checked: it has not happened.** Mouse Afp carries five IMP BP rows (`GO:0001542` ovulation from
ovarian follicle, `GO:0006915`, `GO:0006955`, `GO:0042448` progesterone metabolic process,
`GO:0048872`) and **none of them appears on human AFP**. Mouse Afp also carries no estrogen-binding
MF, so there is nothing to transfer. Reporting this as a non-confirmation per the ADAMTSL5
precedent — the check was run and is negative, which is a real distinction between the two species'
records.

## Per-partner judgement on the three `GO:0005515` rows

Queried IntAct directly (21 interaction records, 12 distinct partners) rather than trusting
`NbExp`.

**GPC3 (P51654), `PMID:39822733` — real, and the ACRV1 "one screen counted three ways" check is
negative.** The three IntAct records are *not* sub-methods of one experiment: `anti bait coip`
in HepG2 cells, plus `pull down` **typed `direct interaction`, host `In vitro`**, plus an in
vitro `anti bait coip`. MI-score **0.59**, the highest of any AFP interaction. The cached file
said `full_text_available: false`; **the flag was stale** — PMC11737099 has the full text, and
re-fetching with `--force` got it. The full text settles the term choice:
`[PMID:39822733 "The results show that AFP pulls down GPC3, but not MUC16, a control protein"]`
(purified Fc-tagged AFP against GPC3-His, with a negative control), and crucially
`[PMID:39822733 "The results show that the GPC3-ΔHS also precipitates AFP, suggesting that the
GPC3 core protein might bind AFP"]`. **Binding is to the core protein, not the heparan sulfate
chains — so `GO:0043394 proteoglycan binding` would misdescribe it.** No functional consequence
was measured. Bare `GO:0005515` is, unusually, the correct ceiling here; recorded as a per-partner
justification rather than a shrug.

**HCV E2, `PMID:26808496` (two rows, IntAct + AgBase).** `UniProtKB:Q99IB8-PRO_0000045596`
resolves to **Envelope glycoprotein E2, residues 384–750** of the HCV genotype 2a JFH-1
polyprotein — i.e. a *different species'* protein. `[PMID:26808496 "85 cellular proteins and
three viral proteins were successfully identified in three independent trials, among which
alphafetoprotein (AFP), UDP-glucose: glycoprotein glucosyltransferase 1 (UGT1) and HCV NS4B were
further validated as novel E2 binding partners."]` Validation was co-IP of over-expressed
Flag-AFP with E2 in 293T `[PMID:26808496 "To this end, we subcloned AFP, UDP-glucose:glycoprotein
glucosyltransferase 1 (UGT1), and Cdc2 in a Flag-tagged expression plasmid and co-transfected
with a HCV E2 expression plasmid into 293T cells."]` — weaker than the GPC3 purified-protein
pull-down, and the paper's functional follow-up was on UGT1, not AFP.

`GO:0140272 exogenous protein binding` ("Binding to a protein or protein complex from a different
species") is the exact term, and the paralog **ALB already carries it by IDA** — so this is a
precedented, informative replacement for bare `protein binding`. **MODIFY both rows.**

**The other nine IntAct partners are not in GOA, and should not be.** A single `two hybrid array`
screen (`PMID:21988832`) contributes seven of them — AP4S1, PIDD1, MED27, EHD4, PHB2, PSMB7,
GNB1 — every one cytosolic/nuclear/proteasomal, i.e. topologically inaccessible to a
signal-peptide protein that is constitutively secreted, and all in a *S. cerevisiae* host that
forces both partners into the yeast nucleus. GOA imported only the two partners their own papers
validated. **That is good curation and worth saying so.**

## `GO:0005737 cytoplasm` — right term, wrong provenance

The recorded route is Ensembl Compara (`GO_REF:0000107`) from mouse Afp `P02772`, whose whole
basis is a **single** MGI IDA, `PMID:8607965`. That paper's own abstract reports the opposite of
what the annotation needs: `[PMID:8607965 "antibodies to SA gave a positive reaction in embryos
of 7 days, while AFP was not detected during this period"]` and, in the teratocarcinomas,
`[PMID:8607965 "Only SA protein was detectable by immunostaining."]` — AFP was detected only as
mRNA. The "intracellular presence of AFP" in that abstract is a **background citation to earlier
work**, not this paper's result. (Abstract only; I have not read the full text, so this is stated
as "cannot be verified from the available record", not as a curator error.)

The term nevertheless survives on **independent human evidence**: `[PMID:33009373 "Moreover,
partial colocalization of AFP and HuR was observed in the cytoplasm of HuH7 and HepG2 cells"]`.
So: `KEEP_AS_NON_CORE`, kept for a reason GOA does not record, with the weak provenance flagged —
and with the context caveat that the cytoplasmic pool is described in AFP-producing hepatoma
lines, not in the fetal plasma protein.

## Retraction / erratum / expression-of-concern sweep

All **29** candidate PMIDs checked against PubMed, reading **both** `PublicationTypeList` and
`CommentsCorrections/RefType` (the ACTR8 lesson: a Publisher Correction is invisible to a
pubtype query). **All clean** — no retraction, no erratum, no expression of concern. Recorded as
a negative result so the next reviewer knows it was run.

## Row-count reconciliation (the ADAMTSL5 check)

`AFP-goa.tsv` has **8** data rows; the `fetch-gene` stub seeded **7**. The stub collapsed the two
`GO:0005515` / `PMID:26808496` / `Q99IB8-PRO_0000045596` rows that differ only by assigner
(**IntAct** and **AgBase**). Restored to 8 so each assigner gets its own verdict; they resolve the
same way, but the redundancy is now visible rather than hidden. Plus **3** `NEW` proposals =
**11** `existing_annotations` entries.

Enforced mechanically by `genes/human/AFP/AFP-bioinformatics/audit_afp_claims.py`, which rebuilds
`supporting_entities` straight from the GOA WITH/FROM column, asserts row-for-row coverage,
verifies all **63** `supporting_text` quotes (including the **5** `file:` quotes that CI does not
check), requires UniProt quotes to sit inside one physical line, and rejects duplicate YAML keys.
Its four guards were each verified by breaking the document on purpose (`--self-test`), and
`RESULTS.md` is regenerated by the script so a hand-edit to it cannot survive.

Its first run failed with a `FileNotFoundError` on a mis-resolved repo root — recorded here
because that is the behaviour wanted: a missing input is a loud error naming the path, not a
silently skipped section.

## Diagnosis: this is an under-annotation gene, with one over-annotation

Following AFF4's framing. Human AFP's entire GO record is **8 annotations / 6 distinct terms**,
with **zero experimental molecular-function evidence beyond three `protein binding` IPI rows** and
**zero experimental biological-process rows**. Meanwhile there are two 1970s ligand-binding papers
on protein purified from human tissue, a 2024 cryo-EM structure with four fatty acids and a metal
ion resolved, six FAM20C phosphosites, and two human null-allele reports — none of which produced
a GO annotation. That is a **coverage** defect. The single over-annotation is `GO:0031667`.

## What I deliberately did not propose

A transport **BP** (`GO:0015908`, `GO:0006869`) or `GO:0140104 molecular carrier activity`. The
*binding* is measured; the **delivery step is not**. `GO:0140104`'s definition requires
"delivering it either to an acceptor molecule or to a specific location", and the placental
DHA-transfer claim in `PMID:38678117`'s discussion is a citation to other work, not a measurement
in that paper. ALB holds `GO:0140104` by EXP; AFP has no equivalent experiment. Raised as a
suggested experiment instead. Noting this explicitly because the temptation to round "binds
fatty acids and circulates in fetal plasma" up to "transports fatty acids to the fetus" is exactly
the kind of join the campaign keeps getting caught by.
