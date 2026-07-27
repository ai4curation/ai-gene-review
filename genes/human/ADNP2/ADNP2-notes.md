# ADNP2 (Q6IQ32) — review notes

Working journal for the PAINT + affinage review. The reproducible measurements live in
`ADNP2-bioinformatics/` (`analyze_adnp2_propagation.py` → `results.json` + `RESULTS.md`); this file
records reasoning, negative results, and process facts that do not belong in the review YAML.

## Accession, verified rather than inherited

The worklist row is `human,Q6IQ32,ADNP2`. UniProt confirms `Q6IQ32` = `ADNP2_HUMAN`, Swiss-Prot
reviewed, 1131 aa, *Homo sapiens*, `PE 1: Evidence at protein level`, gene `ADNP2` with synonyms
`KIAA0863`, `ZNF508`.

**The worklist's "no-IBA" name is wrong for this gene.** ADNP2 carries **two** IBA rows
(`GO:0005634`, `GO:0010468`), both from PANTHER node `PTN000405125`, and UniProt's `DR PAN-GO` line
says so explicitly: *"PAN-GO; Q6IQ32; 2 GO annotations based on evolutionary models."* Consistent with
the brief's standing warning; queried GOA rather than trusting the list name.

## Row-count reconciliation, done before reviewing

```
GOA TSV rows                18   (18 distinct — no byte-identical duplicates)
fetch-gene stub entries     15
```

The three missing entries are the known `seed_missing_annotations` collapse: the seeder keys on
(GO id, evidence, reference, negated, qualifier) and omits WITH/FROM, so the three PMIDs that report
*both* CBX1 and CBX3 (`21888893`, `27705803`, `33961781`) each collapsed 2 → 1. Restored, so every
partner has its own verdict. Final review has 19 entries = 18 GOA rows + 1 `NEW` proposal, asserted
programmatically against the TSV on (term, evidence, reference, WITH/FROM).

---

## The campaign question: did the ADNP NAP-peptide defect reach ADNP2?

**Answer: no, with one qualification, and the qualification is the interesting part.**

### 1. ADNP2 does not contain the peptide — established from sequence, with a positive control

| accession | entry | length | NAPVSIPQ | any `NAP` tripeptide |
|---|---|---|---|---|
| Q6IQ32 | ADNP2_HUMAN | 1131 | none | **none** |
| Q8CHC8 | ADNP2_MOUSE | 1165 | none | **none** |
| Q9H2P0 | ADNP_HUMAN | 1102 | 354 | 354, 701 |
| Q9JKL8 | ADNP_RAT | 1103 | 354 | 354, 586, 701 |
| Q9Z103 | ADNP_MOUSE | 1108 | 354 | 354, 585, 700 |

The three ADNP orthologues are asserted as positive controls in the script — a scan that cannot find
`NAPVSIPQ` in ADNP raises rather than reporting a clean negative for ADNP2. Human and mouse ADNP2 do
not merely lack the octapeptide; they contain **no `NAP` tripeptide at all** in >1100 residues. So no
experiment performed with NAP can be an experiment on ADNP2 under any reading.

### 2. None of ADNP's 19 rat-Compara terms reached ADNP2 — and the reason is structural

ADNP's 53 GOA rows cover 33 terms; ADNP2's 18 rows cover 8. Seven terms are shared, all generic
(`GO:0000785`, `GO:0000981`, `GO:0003677`, `GO:0005515`, `GO:0005634`, `GO:0006357`, `GO:0010468`).
**The 19 terms in ADNP's rat Ensembl-Compara block — the block the merged ADNP review classified
`SOURCE_BAD` + `ROLE_CONFLATION` — intersect ADNP2's term set in exactly zero terms.**

The mechanism is worth stating because it predicts where this defect class *can* and *cannot* travel:

- `GO_REF:0000107` (Ensembl Compara) and `GO_REF:0000024` (UniProt ISS) project along **orthologues**.
  ADNP's donors are `UniProtKB:Q9JKL8` (rat Adnp) and `UniProtKB:Q9Z103` (mouse Adnp). ADNP2's single
  sequence-similarity donor is `UniProtKB:Q8CHC8` — **mouse Adnp2, its own one-to-one orthologue**.
  Compara never crosses the ADNP/ADNP2 paralogy boundary, so the NAP block had no route.
- The one route that *does* span both clades is the IBA at node `PTN000405125`, whose reach is 44 gene
  products covering ADNP and ADNP2 orthologues together. **PAINT gave that node exactly two terms**,
  `GO:0005634 nucleus` and `GO:0010468 regulation of gene expression` — both LCA-appropriate, neither
  NAP-derived. That is PAINT behaving correctly, and it is why the containment held.

Reported as a **non-confirmation** of the predicted defect, per the brief. It is worth as much as a
finding: it locates the NAP problem as an *ortholog-projection* defect rather than a family-wide one,
which means the fix retracts cleanly on the ADNP side without touching ADNP2.

### 3. The qualification: one NAP paper *is* inside an ADNP2 donor set

`GO:0010468 IBA` names three WITH/FROM tokens: `MGI:MGI:1338758`, `PANTHER:PTN000405125`, `RGD:71030`.
Resolving the two gene tokens and then asking **what molecule each seed's own experimental evidence
assayed** (the brief's recipe, applied one level below the usual donor check):

| seed | own experimental evidence in the `GO:0010468` subtree | reference title | molecule |
|---|---|---|---|
| mouse Adnp (Q9Z103) | `GO:0000981` IDA, `GO:0006357` IDA | *Activity-dependent neuroprotective protein (ADNP) differentially interacts with chromatin…* | gene product |
| mouse Adnp (Q9Z103) | `GO:0010468` IMP | *ADNP promotes neural differentiation by modulating Wnt/β-catenin signaling.* | gene product |
| rat Adnp (Q9JKL8) | `GO:0010629` IDA | ***NAP mechanisms of neuroprotection.*** | **synthetic NAPVSIPQ** |

So rat Adnp's *only* experimental annotation anywhere in that subtree is peptide-derived. Following
the brief's insistence on separating **provenance** from **circularity**: the provenance is tainted,
and on its own supports no verdict; the substantive question is whether the chain is empty of
gene-product evidence, and it is not — the co-seed carries an IMP and two IDAs on the protein itself.
Verdict therefore `ACCEPT` with `root_cause: NO_FAILURE_CORE` at the row level and
`source_status: SOURCE_BAD` on the rat entity alone. That combination is deliberate; the row is sound
and one of its donors is not.

Filed as a `suggested_question` to PAINT: should a seed annotation derived from a synthetic peptide
fragment count toward an IBD at all?

---

## Checks run, including the ones that came back negative

- **Logical-opposite citation cross-product** (ADIPOQ's test): **negative**. ADNP2 carries no
  positive/negative regulation pair, so the defect cannot occur. Automated in the script so the null is
  recorded rather than assumed.
- **Reference-projection test** on the two classification-style references. `GO_REF:0000113` (TFClass)
  carries 1436 annotations across GOA — a bulk classification import, as expected, and treated as such.
  For the interaction references, entity counts were derivable for the three small ones (`PMID:21888893`
  → **9** entities; `PMID:27705803` → 135; `PMID:24981860` → 314) and **not** for HuRI (85343
  annotations) or BioPlex (9514), where the honest statement is that the test is uninformative by
  construction rather than a number read off one page.
- **Retraction / erratum sweep** over all 15 PMIDs touched (esummary `pubtype`): none flagged. Note this
  catches retraction and erratum publication types but, per the brief, not a Publisher Correction
  reachable only through `CommentsCorrections`, nor a corrigendum with a null PubMed id.
- **Partner-accession resolution**: `P83916` = CBX1_HUMAN, 185 aa, reviewed; `Q13185` = CBX3_HUMAN,
  183 aa, reviewed. Both canonical, neither a truncated ORFeome clone (the ACRV1 failure mode).
  **Negative for that defect.**
- **Sibling-review consistency**: ADNP's merged review resolves its HP1 `GO:0005515` rows to
  `GO:0070087 chromo shadow domain binding`. Same term used here, so the paralogues agree rather than
  diverging silently. Where the two reviews *do* differ is deliberate and evidence-driven: ADNP's core
  set includes `GO:0000977` sequence-specific DNA binding and `GO:0140463` chromatin-protein adaptor
  activity; neither is claimed for ADNP2, because ADNP2's targeting runs through HP1β and its
  chromatin localisation is conferred *on* it rather than *by* it.
- **PxVxL motif count with its null**: reproduced the merged ADNP review's published figures as a
  precondition (1 hit `PGVLL`@820-824, expected 0.758 under the protein's own composition, regex
  `P.V.[LMIV]`) before reporting ADNP2's. ADNP2 has **2** candidates against an expectation of **2.705**
  — so the count is, if anything, *below* chance and carries no information. The discriminating test is
  projective: a global BLOSUM62 alignment (27.1% identity) maps ADNP's motif start onto ADNP2 position
  **1107**, which is exactly where ADNP2's `PSVLL` sits. The motifs are positionally homologous. The
  second candidate (`PPVLV`@662) has no ADNP counterpart and no experimental support — turned into a
  suggested experiment rather than a claim.

## Where I disagree with, or extend, the merged ADNP review

Nothing in it is contradicted. Two extensions:

1. The ADNP review notes that *"What has NOT been done is a point mutation of ADNP's PxVxL showing loss
   of HP1 binding, so the chromo-shadow-domain mechanism is inferred."* **For ADNP2 that experiment
   exists**: `PMID:38960717` reports PxVxL point mutants that fail to bind HP1β and lose chromatin
   occupancy. So the mechanism the ADNP review had to infer is directly demonstrated on the paralogue,
   and given the motif's positional homology this retrospectively strengthens ADNP's inference too.
2. The ADNP review's PxVxL null of 0.758 uses the degenerate `P.V.[LMIV]` consensus. My first pass used
   strict `P.V.L` and got 0.31 for ADNP and a single ADNP2 hit — a **different number from a different
   consensus, not a disagreement**. Adopted the sibling's regex so the two columns are comparable, which
   is also what turned up ADNP2's second candidate.

## Reading the definitions rather than the labels

Three calls in this review turn on a definition, and all three would have gone the other way from the
label alone:

- **`GO:0000981`** — its parent `GO:0003700` requires binding *"a specific double-stranded genomic DNA
  sequence (sometimes referred to as a motif) within a cis-regulatory region."* ADNP2's authors could
  not define a motif, its peaks avoid TSSs, and mutating the HP1-docking motif abolishes chromatin
  binding. `MODIFY` → `GO:0140110`, verified via QuickGO to be a genuine ancestor (so a generalisation,
  not the sideways move that caught ADIPOQ with `GO:0048018`).
- **`GO:0003677`** — asserts only "interacts selectively and non-covalently with DNA", **no specificity
  clause**. The homeodomain and nine zinc fingers are intact and detected by four independent
  signatures. So the same evidence that kills the specific term leaves the generic one standing:
  `KEEP_AS_NON_CORE`, untested rather than refuted. This is the ADGB globin lesson — one gene, two
  DNA-related terms, opposite verdicts, because the definitions differ.
- **`GO:0141005`** — the reflexive choice for ChAHP2, and **wrong**: it requires the mechanism to
  *involve heterochromatin assembly*, and *"H3K9me3 levels at ADNP and ADNP2 peaks were not reduced by
  either individual or combined removal of these factors."* ChAHP2 reads the mark, it does not deposit
  it. Proposed the bare parent `GO:0010526` and filed the missing "reader-mediated, assembly-independent
  silencing" term as an ontology gap.

## affinage

`gates_passed: True`, 6 citations, all six genuinely about ADNP2 or the ADNP2 orthologues — no
citation resolving to a different protein, and the complex was stated **correctly** as ADNP-CHD4-HP1
(the coordinator warned it had been mis-stated as ADNP-CHD4-BRG1 on ADNP; that error did not recur
here). Recall was also good on this gene, unusually: it returned `PMID:38960717`, the paper this whole
review rests on, and `PMID:18179478`, the paper behind both `GO:0007399` rows. Worth recording as a
counter-example to the campaign's accumulating recall complaints.

One trap it did lay: **`PMID:39251453` is a NAP/davunetide pharmacology paper** — its own title says so
— whose only ADNP2 content is a transient mRNA change after cocaine injection. Using it would have
imported exactly the peptide-pharmacology confusion this review exists to test for, into a gene that
does not contain the peptide. Excluded deliberately, and recorded as `relevance: NONE` so the exclusion
is visible rather than silent.

Affinage's own GO grounding lists `partners: CHD4, CBX1, BRG1, ADNP`. `ADNP` is wrong — the primary
paper states *"no ADNP was copurified with ADNP2 and vice versa"* — which is another instance of the
rule that the provider's structured grounding is a lead, never evidence.

## Process notes

- **The pre-write hook blocked on 12 valid full-text quotes.** It resolves paths against
  `$CLAUDE_PROJECT_DIR`, which for an agent in a sibling worktree is the *other* checkout — where
  `publications/PMID_38960717.md` was a stale 3 KB abstract-only copy, against my worktree's 149 KB
  full text. `origin/main` carries the full-text version and my worktree matches it byte-for-byte, so
  the hook was wrong and obeying it would have deleted the evidence four verdicts rest on. Staged under
  a non-matching filename and validated inside the worktree instead, exactly as the brief prescribes.
- **A merged UniProt accession is not the quiet zero it is usually described as.** Writing the
  inactive-accession guard, I found that `O15507` — the brief's own example — does **not** 404 and does
  **not** report `entryType: Inactive` when `fields=` is supplied. UniProt answers HTTP 303 to its
  successor, urllib follows it, and you receive a complete `UniProtKB reviewed (Swiss-Prot)` record for
  **P56159 GFRA1_HUMAN, 465 aa**. Neither the status code, nor `entryType`, nor the presence of
  `uniProtkbId` distinguishes it; the only field that does is `primaryAccession`. My first two guard
  attempts both passed against it. The guard now compares the returned accession to the requested one
  and is break-tested in both directions.
- **Quote coverage reconciles exactly**: 56 `supporting_text` values in the file; `checkquotes.py`
  covers 49; the 7 it skips are all `knowledge_gaps[].provenance[]`, hand-verified by literal substring
  match. 49 + 7 = 56, so nothing is covered by neither. Raw-vs-parsed counts agree for both
  `supporting_text` (56/56) and `reference_id` (46/46) under a strict duplicate-key-rejecting loader,
  and the file contains no YAML anchors or aliases.
- The `file:` quotes into `ADNP2-bioinformatics/RESULTS.md` are not checked by any repo gate, so all
  three were verified by literal substring match **and** by requiring each to sit on a single physical
  line.
- The remaining validation warning ("No annotations reference available deep research files") is left
  standing. The review cites the PMIDs affinage surfaced, not affinage's prose, which is what the
  brief's hard rule requires.
