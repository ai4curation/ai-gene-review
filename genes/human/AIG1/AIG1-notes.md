# AIG1 (Q9NVV5) — review notes

Human AIG1, 238 aa, chromosome 6. HGNC:21607. PANTHER `PTHR10989:SF11`,
InterPro `IPR006838` (ADTRP/AIG1), Pfam `PF04750` (Far-17a_AIG1).
TCDB `9.B.203.1.1` "the aig1 lipid hydrolase (aig1) family".

## Bottom line

AIG1 is a polytopic membrane **threonine hydrolase** that cleaves the ester bond of
fatty acid esters of hydroxy fatty acids (FAHFAs). Catalysis depends on Thr43
(nucleophile) and His134 (general base); both residues are present in the UniProt
feature table with `ECO:0000269|PubMed:27018888` and both were mutated to Ala with
loss of activity [PMID:27018888 "The FAHFA hydrolase activities of AIG1 and ADTRP were
abolished by mutating their putative catalytic nucleophilic residues Thr-43 and Thr-47,
respectively"; "Mutation of His134 to Ala in AIG1 (H134A) eliminated FP-labeling"].

The gene's *name* is an expression observation — it was cloned as a
dihydrotestosterone-inducible transcript from dermal papilla cells
[PMID:11266118 "We isolated a novel cDNA clone, designated as AIG1
(Androgen-inducible Gene 1), whose expression was found to be inducible by androgen."],
and that paper closes "Further study will be needed to understand the functions of AIG1
in the androgen-regulated hair cycle."

## Hypotheses from the task brief, and what the data said

Three of the four predicted defect classes did **not** confirm. Recording the nulls.

| brief hypothesis | outcome |
|---|---|
| "the measured hydrolase activity may not have reached GO" | **NOT CONFIRMED.** `GO:0120573 FAHFA hydrolase activity` exists (created 2026-03-14) and AIG1 holds it twice — IMP from PMID:27018888 and IEA from 12 RHEA reactions. No MF coverage gap. |
| "the residual GO record is just the expression observation" | **NOT CONFIRMED.** GOA carries no androgen-response, hair-follicle, HCC-biomarker or NFAT term. PMID:11266118 and PMID:21622095 (the biomarker paper) produced no GO annotation at all. |
| "a domain-derived catalytic MF with no measurement" (the AGFG1 pseudoenzyme shape) | **NOT CONFIRMED.** The activity was measured directly on the human protein, in human cells, and both catalytic residues are present as annotated `SITE` features. This is the opposite of a fold-derived activity. |
| "check the paralogue: a term whose only support is the sibling" | **PARTLY CONFIRMED, but it inverts.** The IBA WITH/FROM is `PANTHER:PTN001659973 | UniProtKB:Q96IZ2 (ADTRP) | UniProtKB:Q9NVV5 (self)`. ADTRP is a genuine paralogue co-seed, and it carries its **own IMP** to both propagated terms from the same paper. So the IBA is not a family-level guess. What *is* wrong with it is different — see below. |

## The headline finding: the `GO:0016787` IBA is a stale projection

GOA ships `GO:0016787 hydrolase activity` on AIG1 by IBA (`GO_REF:0000033`, WITH/FROM
`PANTHER:PTN001659973|UniProtKB:Q96IZ2|UniProtKB:Q9NVV5`, date 2026-05-28).

PANTHER's own current data say otherwise. Checked against the live authoritative files,
not against GOA's WITH/FROM column:

- `https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf` — node `PTN001659973`
  carries exactly two annotations, and `GO:0016787` is not one of them:

  ```
  PTN001659973    GO:0120573  IBD  UniProtKB:Q9NVV5|UniProtKB:Q96IZ2  F  20260603
  PTN001659973    GO:0042758  IBD  UniProtKB:Q96IZ2|UniProtKB:Q9NVV5  P  20251127
  ```

- `gene_association.paint_uniprot.gaf.gz` (PANTHER's leaf projection) already projects
  the specific term onto both genes:

  ```
  Q9NVV5  AIG1   GO:0120573  IBA  PANTHER:PTN001659973|UniProtKB:Q9NVV5|UniProtKB:Q96IZ2  F  20260603
  Q96IZ2  ADTRP  GO:0120573  IBA  PANTHER:PTN001659973|UniProtKB:Q9NVV5|UniProtKB:Q96IZ2  F  20260603
  ```

- QuickGO returns **zero** IBA annotations to `GO:0120573` anywhere in GOA
  (`goId=GO:0120573&evidenceCode=ECO:0000318&evidenceCodeUsage=descendants` → 0 hits).

So PAINT placed the general term on 2026-05-28 and **replaced it with the specific term
six days later, on 2026-06-03**. GOA has not ingested that release. The `GO:0016787` row
is a snapshot of a node state that no longer exists — `SOURCE_STALE_OR_MISSING`, not a
curator judgement. Action: MODIFY → `GO:0120573`.

The repo's own cached slice records the transition, which is how it was noticed:

```
$ git show 5d1348b100^:interpro/panther/PTHR10989/PTHR10989-paint.tsv
PTHR10989  PTN001659973  GO:0016787  F  IBD  false  ...  20260528
$ git show 5d1348b100:interpro/panther/PTHR10989/PTHR10989-paint.tsv
PTHR10989  PTN001659973  GO:0120573  F  IBD  false  ...  20260603
```

`5d1348b100` = "Refresh and harden PAINT family slices (#2745)", 2026-08-29.

### This supersedes a conclusion in the merged ADTRP review

`genes/human/ADTRP/ADTRP-ai-review.yaml` (merged 2026-07-27, PR #2338) resolves the
byte-identical row as `KEEP_AS_NON_CORE` and argues:

> "PAINT placed this term on 2026-05-28, ten weeks after GO:0120573 was created
> (2026-03-14), so the general term is a deliberate judgement and not a stale-term
> artefact."

That was correct **on the data available on 2026-07-27** — the cached PAINT slice then
still carried `GO:0016787` at the node — but it is no longer correct. Two lessons:

1. The date in the GOA row is the *projection* date, not evidence about what the node
   currently holds. The node record has to be read from `IBD.gaf`.
2. ADTRP's analysis derived the node→term map from GOA's WITH/FROM field
   (`analyze_adtrp_propagation.py` queries QuickGO with `withFrom=PANTHER:<node>`), so it
   could only ever recover the terms GOA had already projected. It cross-checked against
   the cached slice, which at the time agreed. Both sources were downstream of the same
   stale release.

ADTRP's identical row should be revisited. Flagged in `suggested_questions` with both
genes named once, rather than repeated per gene.

## The paralogue divergence that is real: plasma membrane

AIG1 and ADTRP both carry `GO:0005886 plasma membrane` EXP from PMID:27018888, and both
carry the SL-0039 IEA derived from UniProt's `SUBCELLULAR LOCATION: Cell membrane` line.
The merged ADTRP review already established that **PMID:27018888 contains no localisation
experiment**, and I re-ran that scan independently on the cached full text
(`full_text_available: true`) before relying on it. Case-insensitive counts:

| absent phrase | count | present phrase (control) | count |
|---|---|---|---|
| `plasma membrane` | **0** | `membrane fraction` | 3 |
| `cell surface` | **0** | `membrane lysates` | 9 |
| `immunofluoresc` | **0** | `transmembrane` | 29 |
| `confocal` | **0** | `HEK293T` | 36 |
| `subcellular` | **0** | `FAHFA` | 67 |
| `localization` / `localisation` | **0** | | |

The right-hand column is the positive control: the scan finds what is there, so the zeros
are real absences and not a broken grep. These figures reproduce the merged ADTRP review's
numbers exactly, which is the precondition for using them. (They are inflated relative to
the printed paper because the cached file repeats each section, but they are comparable
within the file.) Supplementary figures are not cached, so the scan is scoped to the
cached full text.

What the paper actually shows is recovery of activity in a 100,000 g membrane pellet
[PMID:27018888 "Both KC01 and JJH260, but not THL or ABC34 also inhibited the FAHFA
hydrolase activity of LNCaP cell lysates, which was mostly found in the membrane
fraction"] plus six *topology predictors* placing the catalytic residues in TM helices.
Its only statement resembling a compartment call is explicitly speculative
["...indicates these enzymes could have evolved to perform hydrolytic chemistry within
the cell membrane environment"].

**ADTRP and AIG1 diverge here, and it is the divergence that matters.** ADTRP's
plasma-membrane call stands independently on PMID:21868574 (imaging + Triton X-114
partitioning with TFPI and caveolin-1 in endothelial lipid rafts), which is why the ADTRP
review could ACCEPT the term with only an attribution caveat. **AIG1 has no such paper.**
Its UniProt `SUBCELLULAR LOCATION` line cites PubMed:27018888 and nothing else, so the
whole plasma-membrane claim on this gene rests on a reference that does not make it.

And the one study that did examine AIG1's localisation places it somewhere else:
[PMID:27040980 "Analyzing the topology of AIG1 in the ER membrane using a
protease-protection assay suggested that AIG has five transmembrane domains with a
luminal N- and cytosolic C-terminus"], with the functional readout also ER-based
["AIG1 over-expression slightly increased susceptibility to oxidative stress, which
correlated with an increased ER Ca(2+) concentration in two different cell lines."].

I did **not** convert that into an ER annotation. `full_text_available: false` for that
paper, the abstract does not state the species of the topology construct or the identity
of the "two different cell lines", and it is a single study. Both `GO:0005886` rows go to
`MARK_AS_OVER_ANNOTATED` (the protein is genuinely a membrane protein, so the term is not
*wrong*, merely unsupported on this gene), `GO:0016020 membrane` is accepted as the
compartment the evidence actually supports, and the PM-vs-ER conflict is recorded as a
`knowledge_gaps` entry and a suggested experiment.

Note the topology disagreement is independent of the compartment disagreement: UniProt's
FT table gives **six** TM helices with a **cytoplasmic** N-terminus, all
`ECO:0000255`/`ECO:0000305|PubMed:27018888` (i.e. prediction, since PMID:27018888 ran no
topology experiment), whereas PMID:27040980 measured **five** TMs with a **luminal**
N-terminus by protease protection. The two agree only on the cytosolic C-terminus.

## The RCHY1/Pirh2 interaction

GOA's single `GO:0005515` row is `IPI` with `UniProtKB:Q96PM5` from PMID:21988832 (the
human liver protein interaction network). Resolving the partner: Q96PM5 is reviewed
Swiss-Prot `ZN363_HUMAN`, 261 aa, "RING finger and CHY zinc finger domain-containing
protein 1", **EC 2.3.2.27** — a RING-type E3 ubiquitin transferase. Canonical length, no
ORFeome-fragment substitution.

Expanding IntAct rather than trusting `NbExp=4` (the ACRV1 lesson — a single screen can be
logged as several sub-methods). For this pair the count survives expansion: the four
records from PMID:21988832 are **four genuinely different assay types**, not sub-methods
of one Y2H:

```
2 hybrid | pull down | anti tag coip | confocal microscopy      (all EBI-3895963, PMID:21988832)
```

Contrast the rest of AIG1's IntAct record, which is the pattern the brief warns about:
141 of 161 interactions come from one publication (PMID:32296183) logged as
`two hybrid array` 47 + `two hybrid prey pooling approach` 47 + `validated two hybrid` 47.
None of those reached GOA as `GO:0005515` rows, so GOA is already being selective here.

Independent corroboration, 14 years later and in a different laboratory:
[PMID:40303337 "Co-IP results similarly indicated that endogenous AIG1 strongly interacted
with Pirh2 in cardiomyocytes under steady-state conditions"], plus proximity ligation and
truncation mapping. Caveat on institutional independence, stated rather than glossed: the
Y2H papers (PMID:21988832, PMID:21622095) share an author (Huo K) and both are Fudan
University work, so they are **not** two independent screens; PMID:40303337 is a different
Fudan department (Zhongshan Hospital cardiology) 14 years later with different authors and
different methods.

So the partner is real, and the row is upgraded from bare `protein binding` to
`GO:0031625 ubiquitin protein ligase binding` (def: "Binding to a ubiquitin protein ligase
enzyme, any of the E3 proteins"), which the partner's own EC number licenses directly.

**What I declined to take from PMID:40303337.** It maps the interaction to AIG1 residues
35–93 by deletion. That span crosses `TOPO_DOM 31..44` (extracellular), `TRANSMEM 45..67`
and `TOPO_DOM 68..87` (cytoplasmic), i.e. it removes an entire TM helix. A deletion that
large cannot distinguish "this is the contact surface" from "the protein no longer folds
or inserts correctly" — the ACBD3 lesson in deletion form — so no binding-site claim is
made, only that the interaction occurs.

**Ambiguity worth flagging rather than resolving.** PMID:21622095's abstract reads
"we identified a novel Pirh2-interacting protein, AIG1, by yeast two-hybrid screening and
confirmed its interaction with **p53** both in vitro and in vivo." Read literally, the
in vitro/in vivo confirmation is of an AIG1–p53 interaction, not AIG1–Pirh2. The affinage
record paraphrases it as confirmation of the Pirh2 interaction. The abstract is
self-inconsistent and the full text is not cached; nothing in this review rests on that
sentence.

## `GO:0042758` — the direction trap that wasn't

Initial worry: AIG1 *releases* free long-chain fatty acids rather than degrading one, so
"long-chain fatty acid catabolic process" might be inverted (the `GO:2000738` shape).

Checked instead of assumed. ChEBI classifies the substrate `CHEBI:83670` 9-PAHSA(1-) as a
**long-chain fatty acid anion** (OLS4 hierarchical ancestors: `fatty acid anion`,
`long-chain fatty acid anion`, `lipid`). The FAHFA *is* a long-chain fatty acid, so
hydrolysing it is literally its breakdown, and every UniProt catalytic-activity line gives
`PhysiologicalDirection=left-to-right`. The term is correct. ACCEPT, matching the merged
ADTRP verdict on the byte-identical row.

## Ontology state: GO models FAHFA metabolism only half-way

`GO:0120573 FAHFA hydrolase activity` was created **2026-03-14** and is the only FAHFA term
in GO — a QuickGO text search for `FAHFA` returns it and nothing else. Walking the ontology
rather than only searching it (the AHSP rule): `GO:1901569 fatty acid derivative catabolic
process` has five children — fatty acid primary amide, ketone body, icosanoid,
fatty-acyl-CoA and fatty alcohol catabolic processes — and none of them covers FAHFAs. GO
already models the closest analogue, the *thio*ester case, as
`GO:0036115 fatty-acyl-CoA catabolic process`.

The merged ADTRP review already files the matching `proposed_new_terms` entry ("fatty acid
ester of hydroxy fatty acid catabolic process", parent `GO:0042758`). I concur and do
**not** duplicate the proposal; it is recorded here as an `ONTOLOGY` knowledge gap so the
AIG1 review is self-contained without filing the same request twice.

## Counting and provenance checks

- **GOA rows vs review entries.** `AIG1-goa.tsv` has 11 lines = 10 annotations + header.
  The `fetch-gene` stub seeded exactly 10 `- term:` entries. **10 = 10, no collapse** —
  the ADAMTSL5/ACTR5 under-seeding defect is absent here. The final review has 12 entries:
  the 10 GOA rows plus 2 `NEW` proposals, stated in the PR body.
- **Retraction / erratum / expression-of-concern.** All eight cited PMIDs were checked via
  `CommentsCorrections/RefType` on each article's own PubMed record (the pubtype query does
  not see Publisher Corrections). One hit: **PMID:21988832 has `ErratumIn: PMID:29254952`**.
  Read it — it is an author-name correction only ["the authors have noticed that the author
  name Juncheng Wei was published incorrectly"], with no data change. The interaction row
  is unaffected. Seven others clean.
- **Reference projection test.** QuickGO by reference: PMID:27018888 annotates
  **8 annotations over exactly 2 entities** (Q9NVV5, Q96IZ2) × 4 terms. That is
  per-protein curation of the two proteins the paper characterises, not a
  ComplexPortal-style distribution — the ACTR8 projection signature is **absent**.
  PMID:21988832 has 756 annotations and is paginated, so its entity count is
  **unavailable**; not substituted with a page total.
- **Who else holds `GO:0120573`.** 495 annotations across GOA, of which exactly **two are
  experimental** — human AIG1 and human ADTRP, both IMP from PMID:27018888, both
  `assignedBy: FlyBase`. Everything else is IEA from RHEA (`GO_REF:0000116`) or Ensembl
  Compara (`GO_REF:0000107`). The FlyBase attribution on two human annotations is unusual
  but not a defect: GO permits any group to annotate any species, and FlyBase curates the
  Drosophila family member. Noted, not actioned.
- **RHEA WITH/FROM arithmetic.** `GO:0120573` carries 12 RHEA cross-references
  (52048/52052/52056/52060/52064/52068/52072/52076/52080/52084/52092/52096) and AIG1's IEA
  row lists all **12**. UniProt curates 12 CATALYTIC ACTIVITY lines for AIG1, each
  `ECO:0000269|PubMed:27018888`. 12 = 12 = 12. (ADTRP's equivalent row lists 11: it lacks
  RHEA:52092, the 5-(9Z-hexadecenoyloxy)-octadecanoate reaction. Recorded as an observed
  difference between the two records, not interpreted.)
- **Node reach reproduced before being cited.** The suggested_question about `GO:0042758`
  sitting at a pan-eukaryotic node relies on numbers first published in the merged ADTRP
  review, so they were re-derived rather than relayed. QuickGO
  (`withFrom=PANTHER:PTN001659973&goId=GO:0016787&evidenceCode=ECO:0000318`) returns
  `numberOfHits` 86 with 86 results collected — complete, not truncated — and 86 distinct
  gene products, identical for `GO:0042758`. Resolving all 86 accessions against UniProt
  (0 unresolved) gives **65 Metazoa, 14 Fungi, 5 Viridiplantae, 2 Amoebozoa**, and
  **7 Swiss-Prot reviewed / 79 TrEMBL** — `entryType` compared with an exact-string match,
  not a `"reviewed" in …` substring test, and 7 + 79 = 86 with both counts differing from
  the total. The seven reviewed members are ADTRP (human, mouse, rat), AIG1 (human,
  mouse), and two uncharacterised fungal proteins, **P38842 `UPF0641 membrane protein
  YHR140W`** and **Q96WV4 `UPF0641 membrane protein PJ4664.05`**. So the claim that the
  node's only reviewed non-animal representatives are curated as uncharacterised is
  verified, and the 5 plant members have no reviewed representative at all. Every figure
  matches the ADTRP review exactly.
- **The ADTRP caveolae claim was checked too**, since the whole plasma-membrane divergence
  turns on it: `publications/PMID_21868574.md` contains "We confirm ADTRP expression and
  colocalization with TFPI and caveolin-1 in ECs", plus one occurrence each of
  `lipid raft`, `triton` and `x-114`. ADTRP's independent surface evidence is real, so the
  divergence from this gene is genuine rather than an artefact of my reading.
- **interpro2go for IPR006838**, verified independently rather than inherited from the
  ADTRP review. `https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006838/` returns
  `type: family`, `name: ADTRP/AIG1`, member databases `{pfam: PF04750, panther:
  PTHR10989}`, `proteins: 5902`, and `go_terms: [GO:0016020 membrane (cellular_component)]`
  — exactly one term, no molecular function. So the family-signature-implies-catalysis
  error is genuinely absent, and the entry's restraint is a measured fact rather than a
  relayed claim.
- **Expression profile is NOT settled, and the review says so.** PMID:27018888's discussion
  cites biogps for AIG1 being broadest in brain and macrophages with ADTRP restricted to
  metabolic organs. That conflicts with the gene's own primary expression paper
  [PMID:11266118 "AIG1 mRNA was expressed at a relatively high level in the heart, ovary,
  testis, liver, and kidney."] and with UniProt's HPA cross-reference ("Tissue enhanced
  (liver)"). A first draft of this review used the biogps figures as settled fact in a
  knowledge-gap boundary and to *choose the tissues for a proposed experiment* — corrected
  before review to state the disagreement and to make measuring the AIG1:ADTRP activity
  ratio by competitive ABPP the first step of that experiment rather than an assumption
  inside it.
- **affinage record.** `gates_passed: True`, 7 citations, all numeric PMIDs, none a
  `PMID:bio_*` preprint id, and all seven resolve to papers genuinely about AIG1. Its
  recall was good here — it surfaced four papers absent from GOA (PMID:27040980,
  PMID:32152231, PMID:38816388, PMID:40303337), two of which changed the review. Its own
  GO grounding block is **wrong** and was not imported: it lists
  `GO:0140098 catalytic activity, acting on RNA` for a lipid hydrolase, and asserts
  `GO:0005783 endoplasmic reticulum` as the localisation without flagging that this
  contradicts UniProt. No affinage sentence is used as `supporting_text`.

## Species discipline on the NEW rows

Every AIG1-specific functional experiment in PMID:38816388 is in **mouse** — FI3KO/FI3OE
mouse adipocytes, mouse brain and kidney membrane proteomes for ABPP, HFD mice. The paper's
human SGBS adipocyte work is about IRF3, not AIG1; the only `hAIG1` strings in the full
text are inside `shAIG1`. PMID:40303337 is C57BL/6 mice, global and AAV9 cardiac-specific,
with HL-1 (mouse) cardiomyocytes; the HEK293T truncation Co-IPs do not state the species of
the constructs. Both NEW rows therefore take **ISS**, not IMP/IPI/IDA.

By contrast every experiment behind the existing `GO:0120573` and `GO:0042758` IMP rows is
human — HEK293T transfection and mutagenesis, shRNA knockdown in LNCaP, and primary human
T-cells — so IMP is the correct code there.

## In vivo caveat worth keeping

PMID:32152231 is the in vivo test, and it is careful about which genotype did what:
"Tissues from mice lacking ADTRP (Adtrp-KO), **or both AIG1 and ADTRP (DKO)** had higher
concentrations of FAHFAs". The single *Aig1*-KO is not reported as elevating tissue FAHFAs.
So AIG1's individual contribution to whole-tissue FAHFA tone in vivo is not established by
that paper, even though its contribution in human cells is (≈70% of PAHSA hydrolysis lost
on shRNA knockdown in LNCaP). Recorded as a knowledge gap rather than smoothed over.

## Sibling-check results, including the nulls

Run because ACRV1/ACRBP established them; reported whether or not they fired.

| check | result |
|---|---|
| WITH/FROM resolution | 3 tokens, 3 resolved. `Q96IZ2` = human ADTRP (reviewed, paralogue co-seed, carries its own IMP to both terms); `Q9NVV5` = self (valid, not circular); `PTN001659973` = a tree node, not a protein. Zero unresolved. |
| IntAct `NbExp` expansion | **Fired in the benign direction.** 4 records = 4 distinct methods for RCHY1, so the count is real. The 141-record HuRI block is the noisy pattern but never reached GOA. |
| partner accession sanity (TrEMBL / length) | **Negative.** Q96PM5 is reviewed Swiss-Prot at canonical length. |
| IBA less precise than its donor (ACRV1 shape) | **Fired.** The donors hold `GO:0120573` by IMP while GOA's IBA landed on `GO:0016787`, three levels up — but the cause is a stale GOA ingest, not PAINT's term choice, since PANTHER already projects the specific term. |
| complex-projection by reference (ACTR8 shape) | **Negative.** PMID:27018888 = 2 entities, per-protein curation. |
| retraction / erratum | **One erratum, immaterial** (author name). |
| LCA / heterogeneous-donor caveat | **Does not apply.** Two donors, both characterised in the same paper, both holding the same specific term. No heterogeneous clade is forcing a broad term. |
| catalytic residues present in the FT table | **Present.** `SITE 43` and `SITE 134`, both `ECO:0000269|PubMed:27018888`, both with `MUTAGEN` entries showing loss of activity. The pseudoenzyme defect is absent. |

## Review round 2 — what the reviewer changed, and the one I was about to get wrong

The PR approved with no blocking items and six suggestions. Four were acted on, two
declined with reasons. The instructive one is #3.

**#3, conceded, and it reversed my draft position.** The reviewer asked whether
`GO:1901800 positive regulation of proteasomal protein catabolic process` belongs
alongside `GO:0031398`. I had drafted a decline on the grounds that the paper's
proteasome statement is hedged — *"likely regulated through a ubiquitin-proteasome
mechanism"* — before reading the experiments that sentence summarises. They are properly
controlled:

- a **cycloheximide chase** measuring turnover rate, not steady-state level
  [PMID:40303337 "In fact, a cycloheximide (CHX) chase assay conducted in HL-1
  cardiomyocytes revealed that AIG1 silencing significantly decelerated p53 protein
  degradation"]; and
- a **three-inhibitor discrimination** with a negative arm [PMID:40303337 "Our results
  showed that protein level of p53 was reduced in response to AIG1 overexpression, an
  effect reversed by MG132 treatment but unaffected by 3-MA or Baf A1 under DOX stress"].

MG132 reverses, 3-MA and bafilomycin A1 do not. That is a route assignment, not an
inference from the ubiquitination result, so the term is not redundant with `GO:0031398`:
one covers the modification step, the other the catabolic outcome, and each was measured
separately. Added as a third `NEW` row.

The lesson is the campaign's own and I repeated it: **the hedge in an author's summary
sentence is not a measure of the evidence underneath it.** I had read this paper
thoroughly for the Pirh2 interaction and skimmed the degradation arm, which is exactly the
ACRBP failure ("cited a paper four times without reading past the abstract") in a milder
form. Declining on a quoted hedge would have looked well-sourced and been wrong.

**#2, acted on.** Both `NEW` rows lacked `supporting_entities`. GO requires a With/From on
a similarity code. Added `UniProtKB:Q9D8B1` (AIG1_MOUSE, reviewed) to all three, and
upgraded `ISS` to **`ISO`**: the transfer is from the 1:1 orthologue, not from generic
similarity — Q9D8B1 and Q9NVV5 sit in the same PANTHER subfamily and carry the same
reviewed protein name. Also recorded the reviewer's point that on GO's conventions the
primary annotation belongs on *mouse* Aig1 with IMP, with the human row as its orthology
projection; neither exists in GOA, so the mouse row is the one a curator should make first.

**#4 and #5, acted on together.** `core_functions[1]` gave the Pirh2 arm co-equal billing
with the hydrolase activity on one murine paper plus a Y2H this review itself marks
`UNVERIFIED`, while the review's own knowledge gap concedes the two functions may not be
separable. The reviewer was right that this argues for secondary placement rather than for
a split. Removed; the claim still lives in three `NEW` annotation rows with full evidence,
and the knowledge gap now states explicitly *why* `core_functions` carries only the
hydrolase. That also dissolves #5 (curation commentary in the description), which existed
only inside the removed entry.

**#6, acted on.** `PMID:21868574` carried the whole AIG1-versus-ADTRP divergence argument
in two `reason` blocks and a `suggested_question` without appearing in `references`, so no
reader could check it. Added with a finding and a `reference_review`, title copied from the
cached frontmatter rather than written from memory.

**#1, declined here and escalated.** The merged ADTRP review now asserts, on a
byte-identical row, a verdict this PR disproves — and its `supported_by` quotes a
node-to-term line that is stale against the repo's own PAINT slice. The reviewer agrees the
scope boundary is debatable. It is a different gene, needing its own history record and its
own validation run, so it belongs in a follow-up PR rather than being smuggled into this
one. Already disclosed in `suggested_questions`; reported to the campaign coordinator.

**Reviewer's own caveat, checked.** It could not run `just validate` (no `just`/`uv` in its
sandbox) and relied on this PR's reported result. That result was re-derived after every
edit in this round: `✓ Valid` with the one deliberately-unsatisfied warning, `checkquotes`
57/57 with zero `file:` quotes, `cache_lint` exit 0, and `terms.csv` untouched.

## Isoform note, not actioned

Isoforms 5 and 6 truncate at residue 134–138 (`VSP_060691` H134→L plus `VSP_060692`
135–238 missing; `VSP_060693/4` similarly), i.e. they **destroy or delete the catalytic
His134** and are predicted to be catalytically dead. Isoform 3 (`VSP_060690`) deletes
48–99. No annotation in GOA carries an `isoform` qualifier and no experiment has tested
isoform-specific activity, so nothing is asserted; raised as a suggested experiment
instead.
