# ADIRF (Q15847) — review notes

## Identity, and which name is current

| source | value |
|---|---|
| PAINT worklist `projects/paint/human-no-IBA-simple.csv:5942` | `human,Q15847,ADIRF` |
| HGNC | `HGNC:24043`, approved symbol **ADIRF**, "adipogenesis regulatory factor", 10q23.2, status Approved |
| HGNC `prev_symbol` | `C10orf116` (symbol changed 2013-02-20) |
| HGNC `alias_symbol` | `APM2`, `AFRO` |
| UniProt | `Q15847` / `ADIRF_HUMAN`, `GN Name=ADIRF; Synonyms=AFRO, APM2, C10orf116` |

**ADIRF is current.** All three sources agree. `C10orf116` is the only *previous approved*
symbol; `APM2` and `AFRO` were never approved symbols, only aliases — so the literature's
"APM2" and "C10orf116" papers are about this gene under superseded names, not about
different genes. `Q15847` has no secondary accessions, is Swiss-Prot reviewed, and is
`PE 1: Evidence at protein level`.

**Not the same thing as `ADIRF-AS1`.** A separate gene, an antisense lncRNA at the same
locus, carries most of the recent "ADIRF" hits — 10 of the 37 `ADIRF[tiab]` PubMed records
(e.g. [PMID:36261012](https://pubmed.ncbi.nlm.nih.gov/36261012/) "Circadian lncRNA
ADIRF-AS1 binds PBAF and regulates renal clear cell tumorigenesis"). None of ADIRF's 11
GOA rows cites an ADIRF-AS1 paper, so **the locus/transcript confusion hazard was checked
and is absent from the GO record**. It is recorded here so the boundary is explicit.
One ADIRF-AS1 paper, PMID:35937391, is a **Retracted Publication**; nothing in this review
rests on it.

## Row-count reconciliation, done before reviewing

```
wc -l < ADIRF-goa.tsv                 -> 12  (11 data rows + header)
grep -c '^- term:' ADIRF-ai-review.yaml -> 11
QuickGO geneProductId=UniProtKB:Q15847 -> 11 annotations
```

**11 = 11 = 11.** No stub collapse; every GOA line has its own entry. The single
`GO:0005515` row has one WITH/FROM partner so there was nothing to split.

## The worklist's "no-IBA" name is stale here

ADIRF is on `human-no-IBA-simple.csv` and **carries two IBA rows** (`GO:0005634`
`is_active_in`, `GO:0045600` `involved_in`), both `GO_REF:0000033` from
`PANTHER:PTN008674116`. UniProt's own `DR PAN-GO; Q15847; 2 GO annotations based on
evolutionary models.` line agrees. Do not read the file name as a claim about the gene.

## The decisive fact, and it is in none of the sources the pipeline gives you

**ADIRF is absent from the mouse/rat lineage**, and *every* functional experiment ever
done on it was an ectopic-expression experiment in **mouse 3T3-L1 preadipocytes**.

Measured independently in `ADIRF-bioinformatics/` (NCBI Gene, with positive controls so a
zero cannot be a rejected query):

| query | hits |
|---|---|
| `ADIRF[sym] AND txid10090[Orgn]` (mouse) | **0** |
| `ADIRF[sym] AND txid10116[Orgn]` (rat) | **0** |
| `ADIRF[sym] AND txid337687[Orgn]` (Muroidea) | **0** |
| `ADIPOQ[sym] AND txid10090[Orgn]` — CONTROL | 1 |
| `LEP[sym] AND txid10090[Orgn]` — CONTROL | 1 |
| `ADIPOQ[sym] AND txid337687[Orgn]` — CONTROL | 30 |
| `ADIRF[sym] AND txid55153[Orgn]` (Sciuridae) — negative control for the clade claim | 9 |
| `ADIRF[sym] AND txid7898[Orgn]` (teleosts) | 103 |
| `ADIRF[sym] AND txid8782[Orgn]` (birds) | 104 |

UniProt agrees: 0 mouse and 0 rat entries with gene name ADIRF. The **Sciuridae** count is
the negative control that makes this an argument rather than a coincidence — squirrels and
marmots retain a 76-aa ADIRF, so the loss is localised to Muroidea and is not a rodent-wide
or annotation-wide absence.

The mechanism was published, and it converges on exactly the same clade:

- [PMID:31945134 "Tripartite factors leading to molecular divergence between human and murine
  smooth muscle", "The mouse locus corresponding to human ADIRF harbors a deletion of close
  to 43 kb (Fig 5A). This deletion is predicted to remove the promoter and first exon of
  ADIRF, a sequence that encodes the first 42 amino acids of the 76 amino acid gene
  product."]
- and it places the event in the Muroid ancestor: [PMID:31945134 "deletion of this segment
  (and loss of ADIRF expression) occurred in the evolutionary predecessor to mouse, rat, and
  hamster."]

**Where I disagree with that paper — and the first version of this argument was bad.** It
also states ADIRF "is absent in several other vertebrate species (rat, zebrafish, lamprey)".
I initially declined the zebrafish half on the strength of my NCBI Gene census (103
Actinopterygii hits for `ADIRF[sym]`). **That was the wrong instrument**: a symbol/alias count
is orthology already asserted by an annotation pipeline, not measured — precisely the
name-based inference the rest of this analysis refuses — and the *only* teleost sequence the
family gave me to align, carp `A0A8C1JCC4` (938 aa), lands in the spurious bin at 51/76 and
19.7%. The reviewer caught this and was right.

Settled properly, on sequence (section F of `RESULTS.md`):

| entry | organism / role | length | aligned of 76 | % id | passes |
|---|---|---|---|---|---|
| NP_001373520.1 | *Danio rerio* | 81 | 71 | 38.2 | **yes** |
| XP_085644419.1 | *Trachurus japonicus* | 81 | 71 | 38.2 | **yes** |
| A0A1D5PM71 | *Gallus gallus* — positive control | 76 | 76 | 50.0 | yes (expected) |
| A0A8C1JCC4 | carp, the only teleost UniProt's family offers — negative control | 938 | 51 | 19.7 | no (expected) |

Plus a **composition control**: 1 of 30 composition-matched shuffles of the *Danio* sequence
(identical residue content, order destroyed, deterministic seeds) passes the coverage
criterion, and the shuffles reach only 7.9–27.6% identity against the real 38.2%. So the
criterion is not satisfied by composition alone — the obvious risk for an Ala/Gln-rich 76-aa
protein — though the non-zero shuffle rate is why the identity margin is reported alongside
coverage rather than coverage being treated as sufficient by itself.

**Coverage and identity disagree here, and I report that rather than choosing.** Both fish
proteins clear the coverage criterion comfortably, yet their 38.2% identity sits *below* the
43.4% orthologue floor the birds establish. Coverage is the criterion this analysis committed
to before the fish were examined, and more divergence is expected over a longer branch.

**Why no UniProt query could have answered this.** `IPR034450` has **50 teleost members and
zero ADIRF-sized ones** — the family's entire fish content is oversized spurious matches,
while the real teleost ADIRF proteins live in RefSeq and are absent from the family. So the
signature is simultaneously over-inclusive of unrelated repeat proteins and under-inclusive of
genuine orthologues; the second half is now in the InterPro question too.

**What I still do not claim.** I examined sequence, not synteny. The paper's argument is a
genomic deletion at the syntenic locus, and I have not tested that. So: an ADIRF-like protein
*is* annotated in zebrafish and is inconsistent with a flat absence claim, but the
deletion argument itself is not adjudicated here. Only the mouse/rat/hamster part is relied
on, and that my own measurement independently confirms.

### What this does and does not do to the annotations

It does **not** make `GO:0045600` wrong for human ADIRF — the human protein really did
promote adipogenic differentiation when expressed. It bounds the *interpretation*: the
experiment is gain-of-function in a background with **no endogenous orthologue**, so murine
adipogenesis demonstrably proceeds without any ADIRF. Nothing in the record establishes that
ADIRF is *required* for adipogenesis in a cell that has the gene. That is why the row is
ACCEPTed and the requirement claim is filed as a knowledge gap rather than asserted.

It also explains why the gene is dark: the dominant model organism for adipose biology
cannot be used, and [PMID:31945134 "The chances that ADIRF could result in functional
changes is increased because it appears to encode a protein with no clear paralogs."] — no
paralogue can substitute either. I confirmed the no-paralogue point: the only other human
`PTHR39227` entry, `Q5TBU5`, is an **unreviewed TrEMBL duplicate with the byte-identical
76-aa sequence** (Celera ORF `hCG_1773630`), not a paralogue.

## The GO record says "adipose"; the expression data say "artery"

[PMID:31945134 "The ADIRF gene is relatively highly expressed (over 700 RKMP in tibial
artery in GTEx [Release V6]) and more abundant in arterial than adipose tissue where it was
initially characterized."] HPA independently calls the gene *Tissue enhanced (adipose
tissue, blood vessel)*.

Yet **all 11 GOA rows are adipogenesis or localisation; not one is vascular.** UniProt's
`TISSUE SPECIFICITY` likewise leads with adipose. The gene's name, its InterPro entry name,
its PANTHER family name and its entire GO process record all descend from the tissue in
which it was *first* found, not the tissue in which it is most abundant. Filed as a
curation gap and a UniProt correction request, not as a GO action — there is no functional
vascular experiment to annotate.

Note the same paper supplies a clean antibody control: [PMID:31945134 "Finally, mouse did
not stain for LPHN2/ADGRL2 in lung non-vascular SMC or for ADIRF in any tissue."] The
antibody used was **Sigma HPA026810** — the *same* antibody behind HPA's immunofluorescence
call, hence behind the `GO:0005654` IDA row. An antibody that stains human smooth muscle and
gives no signal in the species that lacks the gene is about as good a specificity control as
a localisation annotation can have. This *strengthens* row 6.

## Evidence-code defect: two of the three IDA rows rest on an over-expression experiment

All three `PMID:23239344` rows are coded **IDA**, and for the two process rows that is
wrong. The abstract states the assay outright:

[PMID:23239344 "Over-expression studies in 3T3-L1 cells indicated that it up-regulates the
levels of CCAAT/enhancer binding protein α (C/EBPα) and PPARγ and promotes adipogenic
differentiation starting from the early stage of adipogenesis."]

GO's `IMP` definition explicitly covers over-expression and ectopic expression of wild-type
genes; `IDA` is for a direct assay of the gene product's own activity or location. So
`GO:0045600` and `GO:0045944` should be **IMP**, not IDA. This is decidable from the
abstract alone and needs no full text (which is not available: `full_text_available: false`).

The localisation row is different and stays IDA legitimately — [PMID:23239344 "Our data
demonstrated that C10orf116 is highly expressed in adipose tissue and is localized primarily
within the nucleus."] is a direct observation, and it is independently corroborated by HPA.

I did **not** downgrade the *terms*. UniProt's curator read the full text and wrote
"stimulates transcription initiation of master adipogenesis factors like PPARG and CEBPA",
so `GO:0045944` is the curator's call on evidence I cannot see; per CLAUDE.md I do not
overrule that from an abstract. What I record is that the abstract measures *levels*, so
whether the effect is exerted at Pol II transcription or downstream is not established by
anything I can read — hence `KEEP_AS_NON_CORE` plus a knowledge gap, not `MODIFY`.

## The InterPro2GO route: correct for this gene, badly over-reaching upstream

`interpro2go` maps `IPR034450` to exactly two terms (fetched from
`ftp.ebi.ac.uk/pub/databases/GO/goa/external2go/interpro2go`):

```
InterPro:IPR034450 Adipogenesis regulatory factor > GO:positive regulation of fat cell differentiation ; GO:0045600
InterPro:IPR034450 Adipogenesis regulatory factor > GO:nucleus ; GO:0005634
```

**For human ADIRF both are circular.** InterPro's own description of `IPR034450` is written
from this gene's human papers (it cites Maeda's submission, Ni *et al.* 2013 = PMID:23239344,
and PMID:23467766), and `IPR034450` has exactly **one** reviewed Swiss-Prot member — human
ADIRF itself. `UniProtKB-SubCell:SL-0191` in row 3's WITH/FROM likewise traces to UniProt's
own `SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:23239344}`. So rows 3 and 4 restate
the IDA rows through a signature built from them. Correct, and worth zero independent
evidence — hence `ACCEPT` with `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT`.

**Upstream the same mapping is badly over-reaching**, measured in `ADIRF-bioinformatics/`
with `withFrom=InterPro:IPR034450`, fully paginated (1512 annotations, `numberOfHits ==
len(results)` asserted):

| | recipients | ADIRF-sized 60–90 aa | >200 aa | 91–200 aa |
|---|---|---|---|---|
| `GO:0045600` positive regulation of fat cell differentiation | **723** | 130 | **504** | 89 |
| `GO:0005634` nucleus | 789 | 131 | 565 | 93 |

**504 of the 723 proteins receiving "positive regulation of fat cell differentiation" are
larger than 200 aa** — they cannot be orthologues of a 76-aa protein. 237 are non-vertebrate
metazoans; 217 are both. Recipients include a 2304-aa *Toxocara canis* protein, a 1578-aa
*Melipona quadrifasciata* protein and nine separate *Mizuhopecten yessoensis* (scallop)
proteins.

### Why: the signature matches composition, not homology

Human ADIRF is 76 aa and its three commonest residues are **43.4%** of the sequence
(A 18.4%, Q 14.5%, K 10.5%). `PTHR39227` has 768 UniProtKB members of which only **123** are
60–90 aa and **556 are >200 aa**, spanning Fungi (39), Bacteria (16), Viridiplantae (15) and
Archaea (1) — for a gene whose real distribution is vertebrates.

Aligning human ADIRF against five genuine orthologues and twelve oversized recipients:

- **every** orthologue aligns over ≥68 of 76 residues (75–76 in fact); **every** oversized
  member over ≤65 (23–65).
- the oversized members are tandem-repeat proteins: self-similarity periods of 11/22/33
  residues at 38–99% periodicity (e.g. *Biomphalaria pfeifferi* repeats `MPNKTSRSEHD`
  ~50 times).

**Coverage is the discriminator, not identity — and this matters.** The two classes do not
overlap on identity either (orthologues 43.4–100%, oversized members 6.6–19.7%, a 23.7-point
separation), but that separation is not the largest feature of the distribution: the largest
gap anywhere in the pooled identity values is 35.5 points, between **50.0% and 85.5%**, which
falls *inside* the genuine orthologues (the bird/mammal split), not between orthologues and
spurious matches. An identity cut placed at the largest observed gap would therefore have
misclassified chicken and pigeon ADIRF. My first version of this check hard-coded a 50% identity floor and it
**wrongly rejected pigeon ADIRF at 43.4%**; the guard fired, which is how I found it. No
identity threshold is used in the committed analysis.

### The taxon constraints are working — which is what makes the finding sharp

`GO:0045600` carries `only_in_taxon NCBITaxon:6072 (Eumetazoa)`; `GO:0005634` carries
`only_in_taxon NCBITaxon:2759 (Eukaryota)`. Both are visibly enforced:

- `GO:0045600` recipients: **0 outside Metazoa** — the 39 fungal, 15 plant and 16 bacterial
  family members receive none of it.
- `GO:0005634` recipients: 0 outside Eukaryota — the bacterial and archaeal members receive
  none of it (fungi and plants do, correctly).

So the 237 invertebrate recipients are **not** a filter failure: they *pass* the constraint.
This is the "a passing taxon constraint ≠ the term applies" case. `GO:0045444`'s definition
is "The process in which a relatively unspecialized cell acquires specialized features of an
adipocyte, an animal connective tissue cell specialized for the synthesis and storage of
fat" — whether an insect fat body cell or a mollusc storage cell satisfies that differentia
is a question for GO, which is how I filed it rather than asserting the answer.

## The PAINT node: 6 of 7 recipients are orthologues, and the 7th is not

`PANTHER:PTN008674116` carries 14 IBA annotations to 7 gene products (both terms to all 7).
The WITH/FROM names one IBD seed, `UniProtKB:Q15847` — the gene under review — so both IBA
rows are **self-referential**, which per campaign convention is valid and records a PAN-GO
curator's core-function judgement rather than a circular transfer.

I expected the recipient set to be homogeneous and **wrote that into the review before
measuring it**. It is false, and the committed guard caught it:

| accession | organism | length | aligned residues of 76 | % id | orthologue? |
|---|---|---|---|---|---|
| G3RMC8 | gorilla | 76 | 76 | 100.0 | yes |
| K7A2I9 | chimpanzee | 76 | 76 | 100.0 | yes |
| Q15847 | human | 76 | 76 | 100.0 | yes |
| A0A287ACN2 | pig | 75 | 75 | 92.0 | yes |
| Q2NKR5 | cow | 76 | 76 | 85.5 | yes |
| A0A8I3RTQ4 | dog | 76 | 73 | 81.6 | yes |
| **A0A5F8H3S4** | **opossum** | **447** | **62** | **15.8** | **no** |

`A0A5F8H3S4` is an Ensembl-derived "Uncharacterized protein" built from a 22-residue tandem
repeat at 85.4% periodicity, whose three commonest residues are 52.1% of the sequence. Its
15.8% identity sits inside the same band as the unambiguously spurious IPR034450 matches
(6.6–19.7%). It nonetheless receives both of human ADIRF's terms, including `is_active_in`
nucleus.

**The root cause is upstream of PAINT, and saying so matters.** *Monodelphis domestica* has
a real, three-exon ADIRF gene — NCBI Gene **100020286** on chromosome 1, with the ADIPOQ
control non-zero for the same taxon — but **UniProt's *Monodelphis* proteome contains no
ADIRF-sized member of the family**, only the repeat protein. So the tree was handed the
wrong sequence for that species and PAINT annotated what it had. PAINT's placement of the
six genuine orthologues is correct, and the campaign's calibration that PAINT models
families well survives this. The two filable items are whether the PANTHER HMM should admit
a 447-aa tandem-repeat protein into a 76-aa subfamily at all, and whether the missing
opossum ADIRF protein should be added to the reference proteome.

## Checks run that came back NEGATIVE — reported so the next reviewer knows

- **Logical-opposite citation cross-product.** `GO:0045599` (negative regulation of fat cell
  differentiation) returns **0** annotations for Q15847. No opposing pair exists, so the
  cross-product check cannot fire. Negative.
- **Reference-projection test.** `PMID:23239344` annotates **1 entity** (Q15847) with 3
  terms, all IDA, all UniProt — a gene-specific paper, not a projection. Negative.
- **Partner-accession resolution.** `UniProtKB:Q14116` is reviewed canonical Swiss-Prot
  **IL18**, 193 aa. No TrEMBL clone, no partial ORFeome construct. Negative.
- **Hub-promiscuity.** IL18 has **15** distinct IntAct partners; ADIRF has **4**. Neither is
  a promiscuous hub, so the promiscuity argument does not apply here. Negative.
- **Topological impossibility.** It does *not* apply: IL18 is a leaderless cytokine whose
  precursor UniProt describes as cytosolic, and ADIRF is nucleoplasmic + cytosolic. Both
  could meet in the cytosol. Negative — I am explicitly *not* using the usual
  secretory-lumen-vs-cytosol objection.
- **Retraction / erratum / corrigendum.** Checked `PublicationType` and
  `CommentsCorrections/RefType` on all ten PMIDs this review relies on: **none** carries a
  retraction, erratum, expression of concern or publisher correction.
- **Fold-to-activity propagation.** *Non-confirmation.* ADIRF has no domain at all — the
  UniProt feature table contains a single `FT CHAIN 1..76` and nothing else — so there is no
  fold from which an activity could have been inferred, and indeed **no MF row exists except
  `GO:0005515`**. The campaign's standard lead has nothing to find here.
- **ARBA rule.** Row 3 is `GO_REF:0000120` but its WITH/FROM names `InterPro:IPR034450` and
  `UniProtKB-SubCell:SL-0191`, **not** an `ARBA…` rule id, so there was no rule to fetch at
  `rest.uniprot.org/arba/`. Negative.

## `NbExp=3` is one screen counted three ways — fourth instance this campaign

`ADIRF-uniprot.txt` line 100 reads
`CC       Q15847; Q14116: IL18; NbExp=3; IntAct=EBI-7162516, EBI-3910835;`.

IntAct returns **one** interaction record for the pair — `EBI-11784632`, `PMID:32296183`,
MI-score 0.56 — logged under **three sub-methods**: `two hybrid array`,
`two hybrid prey pooling approach` and `validated two hybrid`. The source paper says so
itself: [PMID:32296183 "We screened this search space a total of nine times with a panel of
three Y2H assay versions"]. So `NbExp=3` counts assay *versions* of one HuRI screen, not
three experiments. Neither ADIRF nor IL18 is named anywhere in the paper's text; the pair
comes from the supplementary interaction list.

ADIRF's other three IntAct partners (APP amyloid-beta peptide by affinity chromatography,
`PMID:28650319`; RPS6KA6 and GSK3B by two-hybrid, `PMID:21900206`) are **not** in GOA and
have no functional follow-up either. I am not proposing them.

## The extracellular story: three independent routes, none of them in GOA

The two `GO:0070062` HDA rows come from bulk proteomics — `PMID:23533145` annotates **1046**
entities and `PMID:19056867` **1016**, each with the single term `GO:0070062`, all HDA, all
assigned by UniProt. ADIRF is named in neither paper's narrative; both rows come from
supplementary identification lists. The 23533145 authors flag the risk themselves:

[PMID:23533145 "Certainly the presence of high abundant contaminating proteins, in exosome
preparations from cancer-related biofluids such as EPS-urine, must be taken into account and
further verified before generalizing their presence to a clinical association with the
cancerous condition."]

**Unreconciled count.** That paper's text says [PMID:23533145 "in total, close to 900
proteins were identified in the two EPS-urine exosome pools"] while GOA imported 1046
entities from it. I could not resolve the difference: the identifications live in
Supplemental Table 2, which is not in the cached text. Recording it as unresolved rather
than inventing a reconciliation.

**But the extracellular localisation is independently real, and better supported than the
exosome rows themselves.** Three routes, none in GOA and none in the affinage record:

1. **Serum ELISA at µg/mL.** [PMID:33737617 "cut-off value was determined as 18.7 µg/mL,
   with a sensitivity and specificity of 84.0% and 71.7%, respectively"], measured in
   71 + 54 HCC and 14 gastric-cancer patients with
   anti-APM2 ab79579. Note the authors *assume* the route rather than show it:
   [PMID:33737617 "To determine serum APM2 concentration as a potential biomarker of CDDP
   sensitivity, as it is secreted into the blood stream, the APM2 serum level was tested with
   ELISA in 71 HCC patients who were treated with CDDP intra-arterial infusion"] — "as it is
   secreted" is a premise, not a result.
2. **Lipoaspirate fluid, intact protein by top-down MS.** [PMID:26719138 "adipogenesis
   regulatory factor, perilipin-1 fragments, and S100A6, along with their PTMs"].
3. The two exosome proteomes above.

**Why I did not propose `GO:0005576 extracellular region`.** I verified against QuickGO that
`GO:0070062` **is** a descendant of `GO:0005576` (and that `GO:0005576` is *not* a descendant
of `GO:0070062`), so the two existing HDA rows already entail extracellular region. Adding it
would be redundant. Instead the corroboration is used to justify `KEEP_AS_NON_CORE` rather
than `MARK_AS_OVER_ANNOTATED` on the two rows, and the *route* — ADIRF has no signal peptide
and no transmembrane segment, so classical secretion is unavailable — is filed as a knowledge
gap. Related: `GO:0005615 extracellular space` is confirmed obsolete, so it is not an option.

## A real coverage gap: HPA calls two main locations, GOA imported one

HPA's record for ADIRF (`ENSG00000148671`, antibody HPA026810, IF reliability **Supported**)
gives main subcellular locations **Nucleoplasm *and* Cytosol**. GOA's HPA-derived row
(`GO_REF:0000052`) carries only `GO:0005654 nucleoplasm`. `GO:0005829 cytosol` is absent from
ADIRF's entire GOA record — verified against a positive control (GAPDH is also called Cytosol
by HPA and *does* carry `GO:0005829`, resolved through the same mapping), so this is a real
gap in the import and not a broken query or a wrong term id. Proposed as a `NEW` row.

## Why the nuclear localisation is weaker evidence than it looks

At 76 aa / 7855 Da, ADIRF is far below the nuclear-pore passive-diffusion limit, and it has
no annotated NLS. Nuclear *presence* is therefore the default expectation for this protein
and carries little information. The primary paper says "localized primarily within the
nucleus", which implies enrichment rather than mere presence — and enrichment of a freely
diffusible protein requires a retention mechanism, which nobody has identified.

**The argument is symmetric, so it is used on neither row.** Being below the diffusion limit
predicts *both* compartments, so it discounts nuclear and cytosolic localisation equally and
cannot be evidence for either. It therefore appears only in the knowledge gap asking whether
nuclear enrichment is active, and in the question about PAN-GO's `is_active_in` qualifier.
The `GO:0005829` proposal rests on the HPA immunofluorescence call alone, which is sufficient
for it; the nuclear rows rest on their own IDA plus the HPA call with its mouse antibody
control.

## What the affinage record gave, and what it missed

`gates_passed: True`, 2 citations, both real numeric PMIDs (19444912, 23467766), no
`PMID:bio_*` preprint ids. Both check out. But **recall was near zero for annotation
purposes**:

- It returned **none** of the four PMIDs that GOA actually cites, including
  **PMID:23239344** — the paper behind three of the eleven rows and the only functional
  characterisation of the gene in the nucleus.
- It missed **PMID:31945134** (the Muroidea deletion + arterial expression), which is the
  single most consequential fact about this gene, and **PMID:33737617** (serum at µg/mL).
- Its `molecular_activity`, `localization`, `partners` and `complexes` fields are all empty,
  which is *correct* for this gene, but the narrative also asserts "no direct molecular
  activity, binding partner, or structural mechanism for ADIRF has been characterized" while
  a curated IL18 interaction and a nuclear localisation both exist in the record it did not
  read.

Consistent with the campaign's finding that `gates_passed: True` is a floor on precision and
says nothing about recall. Nothing in this review quotes an affinage sentence, and I
re-derived every number in it (there were none to re-derive: it reports no ratios).

## UniProt corrections to request (no GO action available)

The Q15847 entry still carries two keyword-derived GO lines that GOA no longer imports:

```
DR   GO; GO:0030154; P:cell differentiation; IEA:UniProtKB-KW.
DR   GO; GO:0006351; P:DNA-templated transcription; IEA:UniProtKB-KW.
```

Neither is entailed by the gene's actual evidence, and I verified the relations rather than
assuming them (QuickGO ancestors, `relations=is_a,part_of`):

- `GO:0045944` is **not** a descendant of `GO:0006351`. `GO:0006351` is "The synthesis of an
  RNA transcript from a DNA template" — it says ADIRF *performs* transcription, whereas the
  evidence is regulation of it, and GO deliberately keeps `regulates` out of `is_a`.
- `GO:0045600` is **not** a descendant of `GO:0030154` nor of `GO:0045444`.

Confirmed the SPKW route is retired, with a positive control: `GO_REF:0000043` returns **0**
human annotations while `GO_REF:0000044` returns **139,714**, and ADIRF has 0 GOA rows under
either `GO:0006351` or `GO:0030154` (controls: POLR2A has 13 under `GO:0006351`, PPARG has 7
under `GO:0030154`). So there is no GO row to act on and inventing one would be an
over-annotation of the opposite sign. Filed in `suggested_questions` as a UniProt request,
together with the arterial-expression correction and the two missing primary references.

## Verdict summary

| # | term | evidence | reference | action |
|---|---|---|---|---|
| 1 | GO:0005634 nucleus (`is_active_in`) | IBA | GO_REF:0000033 | ACCEPT |
| 2 | GO:0045600 pos. reg. fat cell differentiation | IBA | GO_REF:0000033 | ACCEPT |
| 3 | GO:0005634 nucleus (`located_in`) | IEA | GO_REF:0000120 | ACCEPT (circular/redundant) |
| 4 | GO:0045600 | IEA | GO_REF:0000002 | ACCEPT (circular/redundant) |
| 5 | GO:0005515 protein binding | IPI | PMID:32296183 | MARK_AS_OVER_ANNOTATED |
| 6 | GO:0005654 nucleoplasm | IDA | GO_REF:0000052 | ACCEPT |
| 7 | GO:0070062 extracellular exosome | HDA | PMID:23533145 | KEEP_AS_NON_CORE |
| 8 | GO:0070062 extracellular exosome | HDA | PMID:19056867 | KEEP_AS_NON_CORE |
| 9 | GO:0005634 nucleus | IDA | PMID:23239344 | ACCEPT |
| 10 | GO:0045600 | IDA | PMID:23239344 | ACCEPT (evidence code should be IMP) |
| 11 | GO:0045944 pos. reg. transcription by Pol II | IDA | PMID:23239344 | KEEP_AS_NON_CORE |
| 12 | GO:0005829 cytosol | IDA | GO_REF:0000052 | **NEW** |

Nothing is REMOVEd. Every row's term is either true of the gene or, in the `GO:0005515` case,
a real but uninformative single-screen observation. The defects here are **absence** (no MF,
no vascular annotation, no cytosol row), **redundancy** (two circular IEA rows), one
**evidence-code** error, and one **upstream propagation** problem that does not affect this
gene's own rows.

## Committed tooling

Two scripts live in `ADIRF-bioinformatics/`, both with `--self-test`. They are committed
rather than left in `/tmp` because this file and the PR describe the invariants they enforce,
and a check written in a scratch file gets described as permanent by the same commit that
throws it away.

- **`analyze_adirf.py`** — the five measurements above (Muroidea loss, IPR034450 reach,
  signature promiscuity, HPA-vs-GOA, PANTHER node reach). Writes `results.json` and
  `RESULTS.md`. Every paginated query asserts `numberOfHits == len(results)`; every reported
  zero has a positive control in the same call pattern.
- **`build_review.py`** — generates `ADIRF-ai-review.yaml` from the GOA TSV and audits the
  **emitted** file. `--audit-only` re-runs the audit without regenerating, so the checks can
  be applied to a hand-edited file. The audit covers: duplicate mapping keys (via a strict
  loader — PyYAML drops them on parse, so no checker that walks the parsed tree can see the
  loss), YAML anchors, raw-vs-parsed `reference_id` counts, row count against the TSV,
  duplicate `references[].id`, same-term-same-action, core_functions coverage in **both**
  directions, the standing hedge that no molecular function is asserted, and every `file:`
  quote verbatim against its target.

**`ADIRF-ai-review.yaml` and `RESULTS.md` are both generated.** Edit the builder, not the
output; both were verified byte-identical across two consecutive runs, so a hand-edit would
be silently reverted on the next regeneration.

### Guard defects found by break-testing, not by reading

1. **A hand-assigned threshold.** A 50%-identity floor for "genuine orthologue" wrongly
   rejected pigeon ADIRF at 43.4%. Replaced with a coverage criterion derived from what
   orthology means at this length; identity is now reported descriptively only.
2. **An assertion that could not fail.** I then wrote a "derived cut round-trips the
   classification" check — but the midpoint of `[max(probe), min(control)]` separates those
   two sets by construction. Third round on one predicate, so I **deleted it rather than
   fixing it a third time** and changed the shape instead.
3. **A control that did not control.** The HPA positive control originally hard-coded
   `GO:0005829` separately from `HPA_LOCATION_TO_GO`, so it would have passed even if the
   mapping were wrong — precisely the case where ADIRF reads "missing cytosol" spuriously.
   The control now resolves its term id *through* the mapping the subject uses, which is what
   made the break-test reachable at all.
4. **A check that reported and then crashed.** `section_b` recorded "unexpected term" as a
   problem and then died on `IPR_TERMS[term]`, aborting every later check in the section.
5. **One constant serving two roles.** `HUMAN_ADIRF` was both the query sequence and the
   expected IBD seed, so the break-test for the seed check crashed on the sequence lookup.
   Split into `HUMAN_ADIRF` and `EXPECTED_IBD_SEED`. Note this is the *mirror* of defect 3:
   a control must share the thing it guards, and two distinct roles must not share a constant.
6. **Two fabricated `file:` quotes.** I invented two `RESULTS.md` quotes rather than copying
   them. `checkquotes.py` caught both — but the repo's own reference validator skips `file:`
   quotes entirely, so on CI alone they would have shipped. `build_review.py` now enforces
   this itself, and fails loudly if it checks zero file quotes rather than passing vacuously.
7. **A false claim caught before it shipped.** The homogeneity assertion on the PANTHER node
   was written into the review from expectation, and the guard refused it. That is the whole
   value of computing what you have already concluded by eye.
8. **A hardcoded number beside a measured one.** `analyze_adirf.py` printed the literal
   `"103 Actinopterygii"` inside an f-string while section A measures that count live, so the
   two could drift apart silently — the same defect class as the teleost claim the section
   exists to correct. Now derived from section A's result, with the literal asserted absent
   from the source. Section F consequently depends on section A having run, so it **asserts
   that dependency and refuses to substitute a literal** rather than trusting call order.
9. **A new early return aborted the tests that follow it.** Adding that dependency guard
   silently redirected all three existing section-F break-tests to the dependency message
   instead of their intended targets — they were constructing an empty `Audit`. `_expect_problem`
   now takes a `seed`, and the dependency test is the one case that deliberately does *not*
   seed. Found by the break-tests failing with the *wrong message*, which is exactly why
   asserting the message rather than the failure matters.
10. **A guard whose message could not be delivered.** `write_report` reads every section's
    results key unconditionally, so a section that took its new early return would kill the
    run with a `KeyError` *before* `main()` printed the FAILED INVARIANTS block — the guard
    would fire and the operator would never see why. `main()` now checks section completeness
    first, reports, and declines to regenerate `RESULTS.md` so it cannot silently go stale.
11. **A guard that matched its own vocabulary.** The source scan added to back the claim
    "the literal is asserted absent" stored the forbidden strings as literals, so it found
    itself — the same self-reference trap a retracted-phrase matcher falls into. Restructured
    to match the *shape* (`\d+\s+(?:Actinopterygii|Aves|…)`), and the docstring documenting the
    defect was **reworded rather than exempted**, since an exemption is the bypass anyone
    wanting to reintroduce the literal would use. The break-test fixture synthesises the
    violating string at runtime only (`{103} Actinopterygii` in source has a brace between the
    digits and the clade, so it cannot match while the formatted value does).
12. **A claim about a check that did not exist.** The round-3 commit message said the literal
    was "asserted absent from the source"; the scan lived in a throwaway edit script, not in
    the repository. That is the "a verification you performed is not a verification that
    exists" failure. The scan is now committed next to the thing it guards and runs in both
    modes.
13. **A string-surgery artefact reached the emitted YAML.** Replacing a phrase that spanned
    wrapped string literals in the builder left `"...restating the nuclear rows. It is This row
    rests on..."` in a `review.reason`, and because the YAML is generated it reproduced on every
    run. Nothing in this repo checks emitted prose for well-formedness; the reviewer caught it.
    Fixed at the builder, then verified in the *emitted* file rather than in the source.

### Quote coverage

`checkquotes.py` checked 49 quotes (28 `supported_by` + 21 `findings`) with 0 problems, but
it does **not** walk `provenance`. The 8 `knowledge_gaps[].provenance[]` quotes were verified
separately by hand against the cached sources — 57 quotes in total, all verbatim, none
fabricated. Raw and parsed `reference_id` counts reconcile at 36; no YAML anchors are emitted.
