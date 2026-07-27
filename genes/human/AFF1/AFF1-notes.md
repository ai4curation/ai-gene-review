# AFF1 (P51825) — review notes

## Identity, verified before anything else

- HGNC:7135, approved symbol **AFF1**, approved name **"ALF transcription elongation factor 1"**.
  Previous symbols `PBM1`, `MLLT2`; aliases `AF-4`, `AF4`, `FEL`. The name "AF4/FMR2 family member 1"
  that UniProt still uses as `RecName` is HGNC's older name.
- UniProt **P51825**, `AFF1_HUMAN`, reviewed (Swiss-Prot), 1210 aa. `primaryAccession == P51825`
  asserted on every fetch in the analysis script, and no secondary accessions are recorded, so there
  is no merged-accession hazard on the subject itself.
- Three annotated isoforms (P51825-1/-2/-3); MANE-Select is `ENST00000395146` = isoform 2.

## Row count reconciles — the stub did not collapse anything

```
genes/human/AFF1/AFF1-goa.tsv : 21 lines = 20 data rows, 20 distinct
AFF1-ai-review.yaml stub      : 20 `- term:` entries, in TSV order
```

### Verdict tally

| action | rows |
|---|---|
| `ACCEPT` | 11 |
| `MODIFY` | 7 |
| `KEEP_AS_NON_CORE` | 2 |
| `NEW` | 1 |
| **total entries** | **21** (20 GOA rows + 1 `NEW`) |

Recorded here deliberately. The tally was first written by hand into the PR body and
a commit message as "11 ACCEPT · 6 MODIFY · 2 KEEP_AS_NON_CORE · 1 NEW", which sums
to 20 rather than 21 and undercounts `MODIFY` by one — the third instance in this
review of a count disagreeing with its own enumeration. Stating it in a file the
audit can read makes it checkable: clause 4 of the counted-claims guard computes the
tally from the document and compares it against any tally-shaped string here, so this
table cannot drift from the YAML. The PR body and git commit messages are not
lintable from inside the repository, which is why the numbers there should be copied
from the guard's `COMPUTED_VERDICT_TALLY` output rather than counted by hand.

This gene is a **negative result** for the known `fetch-gene` under-seeding defect
(`GOAValidator.seed_missing_annotations` keys on term+evidence+reference+negated+qualifier and omits
WITH/FROM). AFF1's three `GO:0005515` rows differ in *reference* as well as partner
(`PMID:21729782`/P42568, `PMID:22190034`/P04608, `PMID:23260655`/P42568), so the key separated them
and each partner got its own entry. Checked and reported rather than assumed.

## The worklist name is stale here too

AFF1 sits on `human-no-IBA-simple.csv` and has **five IBA rows** (`GO:0006355`, `GO:0003712`,
`GO:0006354`, `GO:0050877`, `GO:0032783`), all from `PANTHER:PTN000829417`. Confirmed against
QuickGO with a working-endpoint control, not read off the file name.

## What UniProt does and does not say

- There is **no `FUNCTION` comment** in the entry at all. `PE 1: Evidence at protein level` — the
  protein is detected (nine phosphosites and one acetylation site from MS studies) — so the honest
  statement is "no UniProt-curated FUNCTION summary", not "no experimental data".
- `SUBUNIT` names the complex and, importantly, its paralogue slot:
  [file:human/AFF1/AFF1-uniprot.txt "composed of EAF1, EAF2, CDK9, MLLT3/AF9, AFF (AFF1 or AFF4), the P-TEFb"]
  — "AFF1 **or** AFF4", i.e. UniProt models the two paralogues as alternative occupants of one slot.
- `SUBCELLULAR LOCATION` is a curator inference, not an experimental call:
  [file:human/AFF1/AFF1-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000305}."]
  The experimental nuclear evidence arrives only with the 2026 IDA row.
- The reference table records what each cited paper contributed, and two of those `RP` lines carry
  the whole weight of two GOA rows:
  [file:human/AFF1/AFF1-uniprot.txt "RP   IDENTIFICATION IN THE SEC COMPLEX."] for `PMID:22195968`, and
  [file:human/AFF1/AFF1-uniprot.txt "RP   STRUCTURE BY NMR OF 738-779 IN COMPLEX WITH MLLT3."] for `PMID:23260655`.
- Domain content is `IPR007797` (AF4/FMR2), `IPR043640` (AF4/FMR2 C-terminal homology domain) and
  `IPR043639` (AF4_int); the FT table is otherwise **four `Disordered` regions covering 901 of 1210
  residues (74.5%)** — computed from the feature table by the analysis script, after a first draft
  rounded it to "~1 000", overstating it by ~11% — plus sixteen compositional-bias features. AFF1 is a long intrinsically disordered
  scaffold, and its one solved structure (`2LM0`) is a 42-residue fragment bound to a partner.

## The one direct molecular measurement on human AFF1

`PMID:23260655` is titled for **AF9**, and it contains the only quantitative binding measurement on
AFF1. What was assayed matters: not full-length AFF1 but a 14-residue AFF1 peptide —

[PMID:23260655 "we titrated a peptide derived from the AF9 interaction motif of AF4 (residues 761 to 774) into the AF9 AHD"]

and the affinity is extraordinary:

[PMID:23260655 "The affinity for AF4 is extremely high (KD = 0.17 ± 0.05 nM)"]

with AFF1's residues becoming ordered only on binding:

[PMID:23260655 "1H-15N heteronuclear NOE experiments show that AF4 residues 761-775 are ordered in the complex whereas the remainder is flexible"]

This is a *coupled folding-and-binding* motif, so a 14-mer is the biologically meaningful unit rather
than a truncation artefact — unlike the ADNP-style hazard where a synthetic peptide stands in for a
gene product it cannot represent. AFF1 residues form part of the AF9 hydrophobic core, and the same
paper measures the competing ligands (Dot1L 1.6 nM, BCoR 32 nM, hPC3 > 0.9 µM), so AFF1 is the
tightest of AF9's known partners by an order of magnitude.

The distinct peptide hazard *is* present in this gene's literature, just not in its GOA rows:
`PMID:15269783` characterises **PFWT**, a synthetic peptide modelled on AFF1's AF9-binding domain,
and its cellular effects (apoptosis in t(4;11) cells) are properties of the inhibitor. No GOA row
rests on it, and none should.

## The paralogue-transfer hazard runs in both directions and neither is in GOA

- `PMID:20159561` is titled for **AFF4** and supplies AFF1's `GO:0032783` IDA. The row is sound: the
  basis is a Flag-AFF4 / Flag-ELL1-2-3 purification that recovers endogenous AFF1 —
  [PMID:20159561 "Furthermore, the ELL and AFF4-containing complexes also consist of additional MLL partners, AFF1, ENL, and AF9"]
  — not one of the paper's MLL-AFF1 fusion constructs.
- The same paper is the strongest available **refutation** of a claim the affinage narrative asserts
  for AFF1: [PMID:20159561 "we find that Dot1 is not associated with AFF1, AFF4 or the ELL complexes indicating that ENL is part of at least two distinct complexes"].
  affinage states that AFF1 "recruits the H3K79 methyltransferase DOT1L", citing `PMID:17135274`,
  `PMID:18977325` and `PMID:21030982`. `PMID:17135274` is explicitly mouse —
  [PMID:17135274 "We demonstrate that mouse Af4 functions as a positive regulator of Pol II transcription elongation factor b (P-TEFb) kinase"]
  — its DOT1L half rests on the ENL co-immunoprecipitate that `PMID:20159561` says was
  misinterpreted, and it carries an **unflagged 2023 erratum** (`PMID:37777189`). No DOT1L or
  H3K79-methylation term appears anywhere in AFF1's GOA, so PAINT and UniProt have both been correct
  to withhold one. Nothing in this review asserts it.
- `PMID:20159561` also records a functional asymmetry between the paralogues:
  [PMID:20159561 "We observed that the reduction of the AFF4 homologue AFF1 does not alter ELL1 and P-TEFb stability in these cells"].

## AFF1 vs AFF4: they are not interchangeable, and one paper measures the difference

`PMID:28955517` is indexed as "AFF1 and AFF4 **differentially** regulate the osteogenic
differentiation of human MSCs" — a title the affinage record does not reflect, summarising only the
AFF1/DKK1 half. In human mesenchymal stromal cells:

- loss of AFF1 **increases** osteogenesis
  [PMID:28955517 "siRNA-mediated depletion of AFF1 led to more intense staining of alkaline phosphatase (ALP), an early marker of osteoblastic differentiation"];
- gain of AFF1 **decreases** it
  [PMID:28955517 "We found that overexpression of AFF1 decreased the ALP activity and mineralization of MSCs"];
- AFF1 occupies the DKK1 promoter
  [PMID:28955517 "we performed an anti-AFF1 ChIP assay, which demonstrated that AFF1 bound to the promoter region of DKK1"];
- and DKK1 is the operative intermediate
  [PMID:28955517 "Depletion of DKK1 significantly abolished the inhibition of ALP activity triggered by AFF1 overexpression"];
- while AFF4 does the **opposite**
  [PMID:28955517 "depletion of AFF4 significantly reduced the alkaline phosphatase (ALP) activity and extracellular matrix mineralization, indicating that it had an opposite effect on osteogenic differentiation compared with AFF1"].

Both directions were tested, so this is requirement *and* sufficiency, plus an in-vivo ectopic
bone-formation arm. This is the best-characterised gene-specific human function AFF1 has, and GOA
carries **no osteogenesis annotation for it at all** — hence one `NEW` row proposing
`GO:0045668 negative regulation of osteoblast differentiation`.

Two caveats recorded rather than smoothed over:
1. The paper carries a **2020 Correction** (`PMID:32257529`) whose content is not stated anywhere
   retrievable — its abstract is only "[This corrects the article DOI: 10.1038/boneres.2017.44.]",
   and the PMC record adds nothing. Neither affinage nor GOA flags it.
2. One sentence in the overexpression section reads "the expression of osteogenic-related genes …
   was significantly repressed in AFF1-**depleted** cells" where the surrounding figure and the rest
   of the section describe AFF1-overexpressing cells. The claims above deliberately rest only on the
   unambiguous sentences.

The paper's discussion also states the mutual-exclusivity model:
[PMID:28955517 "Although AFF1 and AFF4 are components of SECs, they may be independently localized and are not found together in a single SEC."]
That is **contested by measurement**: IntAct records an AFF1–AFF4 physical association across 8
records and 2 distinct PMIDs (`20153263`, `21729782`) at MI 0.6, and `PMID:20159561`'s AFF4
purification recovers AFF1. Filed as a knowledge gap, not resolved.

## The DNA-damage block: one recent paper, seven rows, and it is not a projection

`PMID:41062835` (Nat Chem Biol 2026) supplies 7 of the 20 GOA rows. The cache is
`full_text_available: false`, so nothing here characterises its figures. The abstract supports:

[PMID:41062835 "Upon DNA damage, PARP1 binds to and PARylates AFF1 in a region targeted by the E3 ligase Siah1, preventing AFF1 ubiquitination and promoting its stability. This stabilization supports efficient transcriptional recovery after DNA damage."]

and

[PMID:41062835 "AFF1 depletion impairs DNA repair and survival"].

The **reference-projection test** on this PMID (fully paginated, entities as a distinct id set)
returns **8 annotations over 2 entities**: six terms on AFF1 alone, and `GO:0090734 site of DNA
damage` shared with PARP1 (`P09874`). The phenotype terms do not spread. This is the benign shape,
not the ACTR8-style complex-projection defect — and the check was run precisely because AFF1 *is* a
complex subunit. The two IMP rows and one shared location row are attributed to the gene whose
depletion was performed.

The same PARP1/Siah1 axis is corroborated independently and from the opposite direction by
`PMID:31611376`, which has full text:

[PMID:31611376 "we show that site-specific acetylation of super elongation complex (SEC) subunit AFF1 by p300 reduces its interaction with other SEC components and impairs P-TEFb-mediated C-terminal domain phosphorylation of RNA polymerase II both in vitro and in vivo"]

[PMID:31611376 "Reexpression of wild-type AFF1, but not an acetylation mimic mutant, restores SEC component recruitment and target gene expression in AFF1 knockdown cells."]

That last experiment is the cleanest demonstration that the *bridging* is AFF1's own activity: a
point change in AFF1 alone dissolves SEC and costs Pol II CTD phosphorylation. It is why this review
places `GO:0030674 protein-macromolecule adaptor activity` in `molecular_function` and the
elongation-factor and coregulator terms in `contributes_to_molecular_function`. The same paper states
the paralogue slot the same way UniProt does:
[PMID:31611376 "Human SEC was described as a megadalton complex containing elongation factors P-TEFb (a heterodimer of CyclinT1 and CDK9) and ELL in association with AFF1 or AFF4, AF9 or ENL, and EAF1/2"].

Together the two papers describe one process — transcription shutdown then restart around DNA damage
— that GO cannot name; see the ontology gap below.

## AFF1 is a constitutive P-TEFb partner

[PMID:24367103 "we show that the AF4/FMR2 family member 1 (AFF1) is bound to CDK9-CycT and is present in all major P-TEFb complexes and that the tripartite CDK9-CycT-AFF1 complex is transferred as a single unit within the P-TEFb network"]

(abstract only; nothing below is asserted about its figures). IntAct agrees and quantifies it: CDK9
(`P50750`) is AFF1's best-supported partner anywhere — **16 records over 7 distinct PMIDs and 5
distinct detection methods, MI 0.9** — with cyclin T1 (`O60563`) at 8 records across six different
cell lines from one publication.

## WITH/FROM resolution, and the donor evidence question asked properly

All five IBA rows come from `PANTHER:PTN000829417`. The protein donors resolve as:

| token | resolves to | relationship to AFF1 |
|---|---|---|
| `FB:FBgn0041111` | `Q9VQI9` lilli, *D. melanogaster*, Swiss-Prot | the single fly family member; co-orthologue of all four vertebrate AFFs |
| `MGI:MGI:1100819` | `O88573` Aff1, mouse, Swiss-Prot | the **1:1 ortholog** |
| `MGI:MGI:106927` | `P51827` Aff3, mouse, Swiss-Prot | **paralog** |
| `MGI:MGI:1202294` | `O55112` Aff2, mouse, Swiss-Prot | **paralog** |
| `UniProtKB:P51825` | AFF1 itself | **self-reference** (rows for `GO:0006355` and `GO:0006354`) |

MGI tokens arrive as `MGI:MGI:1100819` and UniProt's `xref:mgi-` index needs the bare number; a query
containing the inner colon returns HTTP 400. Every lookup returned multiple candidates (3–10) and the
script reports all of them rather than taking the first, then requires exactly one Swiss-Prot entry.

**Every one of the nine (donor, term) pairs holds its own experimental evidence in that term's
subtree.** So `SOURCE_WEAK_OR_INFERRED` would be contradicted by the measurement; the correct
root cause on every accepted IBA row here is `NO_FAILURE_CORE` (or `NO_FAILURE_NON_CORE`), and the
self-referential rows record a PAINT curator judging the function core rather than a circularity.

Two findings that only appear when you ask **which** term the donor holds:

1. **`GO:0050877 nervous system process` lands two levels above its donors' evidence.** Both
   experimental donors — fly lilli (`PMID:18310460`) and mouse Aff2 (`PMID:11923441`) — carry
   `GO:0007611 learning or memory` **IMP**, a descendant. Propagating `GO:0007611` itself to human
   AFF1 would be unsupported, so the generalisation is deliberate and conservative: good PAINT
   practice, the mirror image of the ACRV1 defect where a propagation landed above a donor that
   *did* hold the specific term.
2. **The ortholog is absent from four of the five donor sets.** Mouse Aff1 is cited only for
   `GO:0006355`. For `GO:0050877` in particular it contributes nothing — and yet the AFF1-specific
   nervous-system literature is a mouse phenotype: the *robotic* mutant stabilises Af4 and causes
   Purkinje-cell loss and ataxia (`PMID:12629167`), with Af4 directly regulating *Igf-1* in Purkinje
   cells (`PMID:20007461`). MGI has annotated **no** nervous-system term to Aff1. So the nervous
   system claim reaches human AFF1 through its paralogues while the ortholog's own relevant
   phenotype is uncaptured — a curation gap worth reporting upstream, and the reason this row is
   `KEEP_AS_NON_CORE` rather than core.

## Node reach, both halves of the question

`PTN000829417` carries **395 IBA annotations over 79 recipient gene products** — five terms × 79, so
the block is applied uniformly. Its human reach is exactly **AFF1, AFF2, AFF3, AFF4**, and all four
receive the identical five terms. Verified against QuickGO per paralogue.

The reciprocal question — which node's reach is exactly my gene set, and what did it give them —
comes back clean here. There is no node whose human reach is a proper subset of the AFF family doing
something odd to it: `GO:0032783` reaches AFF2 twice (also via `PTN002575678`), which is redundant
rather than wrong. And the family-level assignment is *well founded* on its face: `GO:0032783`'s own
definition names the family —

> "At minimum, the complex contains a transcription factor of the ELL family, an EAF protein, and an
> AFF family protein or distant relative"

— and `PMID:22547686` reports that AFF2 and AFF3 occupy the SEC-L2 and SEC-L3 variants, so all four
paralogues genuinely belong to SEC-family complexes. This is the inverse of the ACTL8/`GO:0035267`
case: reading the term definition here *supports* the propagation.

`GO:0006355` staying at the unsigned parent is likewise correct rather than lazy. The node's members
are heterogeneous in **direction**: AFF1 activates DKK1 (`PMID:28955517`) while mouse Aff2 carries
`GO:0010629 negative regulation of gene expression` by IMP. When donors disagree on sign, the unsigned
parent is the LCA and there is no granularity defect to fix.

## The finding: one reference, one clade got the specific term, the other did not

`PMID:22195968` annotates both `GO:0008023 transcription elongation factor complex` and its child
`GO:0032783 super elongation complex`. Resolving every recipient's organism:

- `GO:0032783` → **10 recipients, all *Drosophila melanogaster*** (lilli, Cdk9, CycT, Eaf, Ice1,
  Ice2, ear ×2, Uspl1l, CG8229);
- `GO:0008023` only → **12 recipients**: the **11 human** ones (AFF1, AFF4, CDK9, ELL, ELL2, ELL3,
  EAF1, EAF2, MLLT1, MLLT3, ICE2) plus **Drosophila Ell**.

Twenty-two gene products receive one of the two terms, 11 human and 11 *Drosophila*. **Not one of the
11 human recipients got the specific term, and 10 of the 11 fly ones did.** Stated precisely because
the exception matters: the split is not purely clade-based — *Drosophila* Ell is the twelfth
parent-only recipient — so this is a per-annotation gap rather than a rule about clades. (An earlier
draft of this section said "12 human", counting Ell among them; the enumerated list has 11 names and
that mismatch is what surfaced the error. A count disagreeing with its own enumeration is the bug
report, not a rounding detail.)

And the consequence for AFF1 is a three-step detour: fly lilli's `GO:0032783` **IPI from this very paper** is the donor of human AFF1's
`GO:0032783` **IBA**, while AFF1's own direct annotation from the same paper sits one level up. The
specific term reached the gene by phylogenetic inference from a fly protein annotated in the same
experiment that annotated the human protein.

UniProt's own reference table for that paper reads
[file:human/AFF1/AFF1-uniprot.txt "RP   IDENTIFICATION IN THE SEC COMPLEX."], i.e. the curator's
reading was SEC-specific. Hence `MODIFY GO:0008023 → GO:0032783`, and a `suggested_question` naming
**all eleven affected human gene products once** rather than repeating it per gene.

## The other granularity call: polymerase specificity

The node asserts, of the same 79 gene products, both `GO:0032783` — a term whose definition is
explicitly *"increases the overall rate of RNA polymerase II transcription elongation"* — and
`GO:0006354 DNA-templated transcription elongation`, which is polymerase-agnostic. Those two cannot
both be maximally precise. Every characterised SEC substrate is Pol II:
[PMID:22547686 "The SEC family members demonstrate high levels of polymerase II (Pol II) C-terminal domain kinase activity"],
and the p300 paper measures CTD phosphorylation of Pol II specifically. AFF1 already holds the
Pol II-specific regulatory term `GO:0032968` by IMP. `GO:0006368 transcription elongation by RNA
polymerase II` was verified to be an `is_a`/`part_of` descendant of `GO:0006354` before proposing it,
so both `GO:0006354` rows are `MODIFY → GO:0006368`.

Deliberately **not** claimed: that `GO:0032968` is under `GO:0006368`. It is not — GO links them by
`positively_regulates` and keeps regulation out of the `is_a` hierarchy. Both closures were fetched.

## Redundancy the ontology can see

Fetched, not inferred (all seven relation claims are asserted in `results.json`):

| relation | verified | consequence for this gene |
|---|---|---|
| `GO:0032968` ⊂ `GO:0032786` | yes | the two IMP rows from `PMID:41062835` are a parent/child pair from one reference; the parent is redundant → `MODIFY → GO:0032968` |
| `GO:0032783` ⊂ `GO:0008023` | yes | the two complex IDAs differ only in precision |
| `GO:0006355` ⊂ `GO:0010468` | yes | the InterPro2GO row is the least specific regulation row on the gene |
| `GO:0006368` ⊂ `GO:0006354` | yes | licenses the polymerase-specificity refinement |
| `GO:0003711` ⊄ `GO:0003712` | correct | the two MF rows are **different claims**, not a general/specific pair, so both stand |
| `GO:0000785` ⊄ `GO:0005634` | correct | chromatin and nucleus are independent location claims |
| `GO:0090734` ⊄ `GO:0000785` | correct | the two damage-associated locations are not a pair |

`GO:0003711` has **no children**, so it is already maximal; there is no Pol II-specific
elongation-factor-activity term to refine to, and ACCEPT is the only available action.

The `GO:0010468` row comes from InterPro2GO via `IPR007797`, the AF4/FMR2 family signature. PAINT
gives the same family `GO:0006355` — one level more specific — so **two automatic pipelines assign
different granularities to the same family from the same evidence base**, and the coarser one is
strictly redundant on this gene. `MODIFY → GO:0006355`.

## Interaction rows, decided per partner

IntAct expansion (all 104 records accounted for; the run fails if any is unassigned):

| partner | records | distinct PMIDs | distinct methods | max MI |
|---|---|---|---|---|
| CDK9 `P50750` | 16 | **7** | 5 | 0.90 |
| MLLT1/ENL `Q03111` | 9 | 2 | 3 | 0.60 |
| **AFF4** `Q9UHB7` | 8 | 2 | 3 | 0.60 |
| CCNT1 `O60563` | 8 | 1 (six cell lines) | 3 | 0.53 |
| **MLLT3/AF9** `P42568` | 7 | 2 | **5** | 0.73 |
| EAF1 `Q96JC9` | 5 | 3 | 1 | 0.64 |
| ELL3 `Q9HB65` | 4 | 3 | 1 | 0.64 |
| **HIV-1 Tat** `P04608` | 3 | **1** | 2 | 0.56 |

- **AF9** (`GO:0005515` rows 8 and 10) is a real partner by any standard: five orthogonal methods
  including NMR, CD and gel filtration, a deposited structure, and a sub-nanomolar dissociation
  constant. `protein binding` is uninformative for it, so both rows `MODIFY → GO:0030674
  protein-macromolecule adaptor activity`, which is what the AF9 contact and the SEC-assembly
  requirement jointly establish. Noted for the record: the same paper's curator assigned
  `GO:0060090 molecular adaptor activity` to **AF9** (`P42568`). That is not double counting — AF9
  is the hub for chromatin-side ligands (Dot1L, BCoR, hPC3 compete for the same surface) while AFF1
  is the hub bridging P-TEFb to the ELL/EAF module — but the symmetry is worth a curator's eye.
- **Tat** (row 9) is one publication: 3 records, 2 sub-methods, HEK293T and Jurkat, MI 0.56. `NbExp=3`
  in UniProt is that one study, consistent with the campaign's repeated finding that `NbExp` counts
  sub-methods. Functionally corroborated at abstract level by `PMID:24367103`, but that paper's
  stated mechanism is that AFF1 raises **Tat's affinity for CycT1** — which does not establish a
  direct AFF1–Tat contact, and AFF1 has no Tat co-structure (its only PDB entry is `2LM0`). So:
  `KEEP_AS_NON_CORE`, real but non-core, and the molecular detail left open.
- **Negative results worth recording.** (i) `P53367 ARFIP1` appears only against isoform P51825-3,
  from a single HuRI screen logged as three sub-methods (`two hybrid array` + `two hybrid prey
  pooling approach` + `validated two hybrid`), both partners over-expressed in yeast. GOA did **not**
  import it, which is the right call and matches this repo's convention (554/803 merged HuRI
  `GO:0005515` rows are marked over-annotated). Nothing to act on. (ii) Two records pair AFF1's own
  Ensembl **transcripts** with RNAcentral miRNAs by CLASH (`PMID:23622248`) — RNA–RNA records, not
  protein interactions, and correctly absent from GOA. (iii) Four partner entities are not proteins
  at all: two MLL-AFF4 fusion constructs, one ENL construct, and `ENSG00000136997` — the *MYC gene*,
  from a ChIP record. None reached GOA.
- **The fusion hazard did not materialise in GOA.** MLL-AFF1 is a chimeric oncoprotein and most of
  this gene's fame rests on it; IntAct does carry fusion-construct records. But no GOA row for AFF1
  rests on the fusion. Hypothesis tested, not confirmed — reported as such.

## Ontology gap

There is **no GO term for transcriptional restart / recovery of RNA synthesis after DNA damage.**
Confirmed on a working endpoint (control: a search for "super elongation complex" returns
`GO:0032783` first) across five phrasings, and by enumerating all **96** `is_a`/`part_of` descendants
of `GO:0006974` — none has "recover", "restart" or "resum" in its name. Consequently the one process
that `PMID:41062835` and `PMID:31611376` jointly describe has to be expressed as an unrelated pair,
`GO:0006974` + `GO:0032968`, which loses the fact that AFF1 is the *switch* for both the shutdown and
the restart. Filed under `proposed_new_terms`.

Considered and **not** filed: child terms for AFF1-SEC versus AFF4-SEC. `GO:0032783` has no children
and ComplexPortal's seven AFF1-containing entries all list AFF1 *and* AFF4 together, so no external
resource models the distinction either — but the underlying biology is contested (mutual exclusivity
per `PMID:28955517`'s discussion versus a measured AFF1–AFF4 association in IntAct). Proposing terms
for a distinction the evidence does not settle would be an over-annotation of the opposite sign; it is
a knowledge gap instead.

## affinage assessment

`gates_passed: True`, `faith_pct: 100.0`, 23 citations, all well-formed numeric PMIDs, no
`PMID:bio_*` preprint ids. Precision looks fine. **Recall on the reference set that actually decides
this gene's annotations was 0 of 7** — affinage returned none of `PMID:41062835`, `20159561`,
`22195968`, `22547686`, `21729782`, `22190034`, `23260655`, including the 2026 paper behind 7 of the
20 rows. Computed, not estimated, in `RESULTS.md` §G. This matches the ADIPOQ characterisation: on a
well-studied gene the provider returns the textbook history rather than the annotation-relevant
literature.

Four provider defects beyond recall:

1. **Two cited papers carry unflagged corrections.** `PMID:28955517` → Correction `PMID:32257529`
   (2020); `PMID:17135274` → Erratum `PMID:37777189` (2023). Both found by reading
   `CommentsCorrections/RefType` on each cited article's own record. Crossref was also checked for
   null-PMID corrections on all seven GOA references: **none** (`update-to` and `updated-by` empty
   throughout; two carry only a `has-review` relation).
2. **A mechanistic claim contradicted by a cached paper**: the DOT1L-recruitment sentence, above.
3. **A hypothesis reported as a demonstration.** affinage's row for `PMID:12629167` reads "A missense
   mutation in the highly conserved region of mouse Af4 **causes** autosomal dominant cerebellar
   ataxia". The paper is titled "A mutation in Af4 is **predicted** to cause cerebellar ataxia and
   cataracts in the robotic mouse" and says
   [PMID:12629167 "We demonstrate that Af4 is specifically expressed in Purkinje cells, and we hypothesize that the expression of mutant Af4 leads to neurodegeneration."].
   The provider's sentence upgraded a stated hypothesis into a causal claim. Caught because the
   builder verifies every quote before writing and refused the paraphrase — which is the whole point
   of making the check a precondition rather than a review step.
4. **A complex-level result attributed to the single gene.** affinage's row for `PMID:20007461` reads
   "Af4 directly regulates transcription of the Igf-1 gene". The paper attributes it one level up:
   [PMID:20007461 "Chromatin immunoprecipitation confirmed that Igf-1 is a direct and the first validated target of the AF4 transcriptional regulatory complex"].
   Same class of error as the one this gene is most exposed to, arriving from the provider rather
   than from GOA.

The last two together are why the reason field for `GO:0050877` states the mouse evidence at exactly
the strength the papers state it. Note that neither error would have been caught by quote hygiene
alone had I paraphrased: the ADPRS lesson is that a provider's framing contaminates even when none of
its text is quoted, and here two of its framings were wrong in the same direction — overstating
strength and overstating attribution to the single gene.

No affinage sentence is used as `supporting_text` anywhere in this review, and no number is taken
from it — the ADPRS lesson is that a provider's *arithmetic* contaminates even when none of its text
is quoted, so every figure here is re-derived from the primary source or computed by the script.

## Disagreement with the concurrent AFF4 review — MEASURED, not predicted

`paint/AFF4` (PR #2349) opened while this review was in its sixth round, so the comparison the
brief asks for could be run rather than left conditional. Ten rows are byte-identical between the
two genes (same term, evidence code, reference and WITH/FROM). **Seven agree; three diverge.**

| shared row | AFF1 | AFF4 |
|---|---|---|
| `GO:0008023` IDA `PMID:22195968` | **MODIFY → `GO:0032783`** | ACCEPT |
| `GO:0006354` IBA `GO_REF:0000033` | **MODIFY → `GO:0006368`** | ACCEPT + separate `NEW` `GO:0006368` |
| `GO:0010468` IEA `GO_REF:0000002` | **MODIFY → `GO:0006355`** | ACCEPT |
| `GO:0003712`, `GO:0005634`, `GO:0006355`, `GO:0032783`, `GO:0050877`, and both shared `GO:0005515` rows | — | agree |

Read carefully, only the first is a substantive disagreement; the other two are the *same
assessment implemented differently*, which is still an inconsistency worth resolving because the
two reviews recommend different things for identical rows.

**`GO:0006354`** — we agree on the biology. AFF4's review independently reaches `GO:0006368` as
the right term on its own human evidence, and verified the same ancestor closure. It implements
that as a `NEW` row while keeping the IBA at `ACCEPT`; this review implements it as a `MODIFY` of
the IBA. Convergent conclusion, divergent action. Since the WITH/FROM is byte-identical
(`PANTHER:PTN000829417` + `UniProtKB:P51825`), one node-level recommendation should cover both.

**`GO:0010468`** — both reviews call the term correct-but-uninformative and both note it is a
verified ancestor of terms the gene already holds. AFF4 accepts on that basis; this review
MODIFYs on the upstream argument that `IPR007797` supports the more precise term for every
protein it matches. Again a mechanism difference on a shared assessment.

**`GO:0008023` — the real divergence, and I think both checks are right about different
questions.** AFF4's review ran the *projection* test (does the phenotype spread across the
subunits?) and reports a clean negative, which this review's own data confirms: the paper's
functional term `GO:0042795` sits on 7 entities and reaches neither AFF4 nor AFF1. That is
sound. But it is not the question this review asked. The *granularity* question — which
recipients of this reference got the child term `GO:0032783` — has a different answer: **10 of
the 11 Drosophila recipients did, and none of the 11 human ones.** The two tests are orthogonal,
and a negative on projection does not bear on granularity.

One checkable correction for that review: it states this term reaches **16** entities and
enumerates 16. The fully-paginated count is **17** — the enumeration omits **human ICE2
(`Q659A1`)**, which is in the recipient set. Its other two figures for this reference (61
annotations, 26 entities) match this review's computation exactly, so the discrepancy is confined
to that one list, and it does not affect its "no bystander in the list" conclusion, since ICE2 is
a genuine elongation-complex subunit. The likely cause is a mental filter to SEC members: ICE2 is
a *little* elongation complex subunit.

**Two further asymmetries where the reviews agree and should:** AFF4 carries `GO:0034976 response
to ER stress` and nucleoplasm/nuclear-body localisations that AFF1 does not, and AFF1 carries the
entire seven-row DNA-damage block from `PMID:41062835` that AFF4 does not. Those are real
gene-level differences, not propagation defects.

**And the sign trap this family sets, restated because it is the one that would do real damage:**
AFF1 and AFF4 have **opposite** effects on osteogenesis (`PMID:28955517`), so any term moved
between them in either direction inverts the biology. Neither review does this.

## Where the risk actually sat, across six review rounds

Worth recording for whoever reviews AFF2, AFF3 or AFF4 next. **Not one reviewer finding was
about the curation.** No term, action, evidence code, qualifier, quote or reported biological
number was ever challenged. All eleven findings were about claims made *about the checks*:

| class | instances |
|---|---|
| a count disagreeing with its own enumeration | 3 (the human recipient set; the `MODIFY` row count; the stated total) |
| a number estimated where a derivable one existed | 1 (disorder coverage: 901, not "~1000") |
| a guard scoped to the failure already known | 2 (check G's first two clauses; the tally clause) |
| a check matching only its own exemption, i.e. vacuous | 2 (clause 4's prose regex; the total sub-clause) |
| a report string asserting what it never read | 1 (the `in_complex`/`locations` live instance) |
| a silent-nothing lookup where siblings raise | 1 |
| prose duplicated or narrating process in a biology field | 1 |

Two further defects were found by the guards' own break-tests failing, not by reading the code —
a case-sensitive number match and an enumeration regex that required the *correct* list, so
substituting a symbol made the check go silent. The generalisable lesson is the campaign's own:
a passing self-test proves the guards you thought of fire, and the coverage question stays a
reading question. The cheapest detector by far was **deriving an expected number independently
and comparing** — it found four of the eleven.

## Process

Every claim about provenance in the review YAML is computed by
`AFF1-bioinformatics/analyze_aff1_annotations.py` (nine analyses, guards break-tested with
`--self-test`). Two real defects were found by numbers that refused to add up while writing it:
`publicationIdentifiers` produced "1 record, 5 publications" because its entries are
`"32296183 (pubmed)"` strings mixed with DOI/IMEx ids; and an equality test against the bare
accession silently discarded 5 of 104 IntAct records because the subject also appears as isoform
`P51825-3` and as its own Ensembl transcripts. Both are now assertions rather than comments.
