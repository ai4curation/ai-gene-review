# AEBP2 — review notes

Working journal for the PAINT + affinage review of human **AEBP2** (`UniProtKB:Q6ZN18`,
`HGNC:24051`, 12p12.3). Provenance is recorded inline as `[PMID:x "quote"]`. Everything
numeric here is computed by `AEBP2-bioinformatics/analyze_aebp2.py`; see
`AEBP2-bioinformatics/RESULTS.md` for the tables, which are the claims.

## 0. Identity verified three ways before anything else

| source | says |
|---|---|
| `projects/paint/human-no-IBA-simple.csv:6551` | `human,Q6ZN18,AEBP2` |
| HGNC REST (`/fetch/symbol/AEBP2`) | `HGNC:24051`, status **Approved**, `uniprot_ids: [Q6ZN18]`, no previous symbol |
| UniProt REST | `primaryAccession: Q6ZN18`, `AEBP2_HUMAN`, reviewed (Swiss-Prot), 517 aa |

The UniProt fetch asserts `primaryAccession == Q6ZN18`. A merged accession returns HTTP 200
with a complete reviewed record *for a different protein*, and nothing else in the payload
reveals it, so this assertion is in the committed script and is break-tested against the
known-merged `O15507`.

## 1. Row reconciliation, run before reviewing anything

- GOA TSV: **20** data rows, **20** distinct.
- QuickGO for `UniProtKB:Q6ZN18`: **20** annotations.
- `fetch-gene` stub: **20** `existing_annotations` entries.

All three agree. The stub's known WITH/FROM-blind collapse could not have applied here
because **AEBP2 carries no `GO:0005515 protein binding` row at all** — despite
`DR IntAct; Q6ZN18; 33` and `DR BioGRID; 125736; 49`. The PRC2 interactions that would
normally appear as `GO:0005515 IPI` are instead curated as `GO:0035098 part_of`, which is
better curation, not a gap.

Aspect census: **14 cellular_component, 6 biological_process, 0 molecular_function.**

## 2. The worklist's "no-IBA" name is stale for this gene too

AEBP2 is on `human-no-IBA-simple.csv` and **has two IBA rows**:
`GO:0035098` and `GO:0006357`, both `GO_REF:0000033`, both from
`PANTHER:PTN002323211`. Queried directly, not inferred from the file name. The
EZH2 (`Q15910`) positive control returns 169 annotations from the same endpoint, so a
zero here would have been a real zero.

## 3. The zinc-finger → sequence-specific-DNA-binding lead: NON-CONFIRMED, and quantified

The brief's prediction was that a C2H2 zinc-finger protein annotated by a
transcription-factor pipeline would pick up `GO:0003700`/`GO:0000981`. It did not, and the
denominator is what makes this a finding rather than a shrug.

`GO_REF:0000113` is TFClass-based DbTF curation by NTNU_SB. Fully paginated it covers
**727 human gene products in 1436 annotations**:

- **709 (97.5 %)** receive `GO:0000981` DNA-binding transcription factor activity, RNA
  polymerase II-specific, *plus* `GO:0000785` chromatin;
- **18 (2.5 %)** receive `GO:0000785` **only**. AEBP2 is one of them.

The withheld 18 are a coherent class of chromatin factors whose DNA-binding-like folds
mediate protein contact rather than sequence recognition: **HOPX** (the homeodomain
protein that cannot bind DNA), **ZFPM1/ZFPM2** (FOG1/FOG2 — zinc fingers repurposed as
GATA cofactor surfaces), **NCOA1/2/3** (p160 coactivators), **SMAD6/SMAD7** (inhibitory
SMADs lacking the DNA-binding hairpin), **NR0B1/NR0B2** (DAX-1/SHP, nuclear receptors
without a DBD), plus NFX1, NFXL1, ZC3H6, ZC3H8, TFDP3, DMRTC1, HMBOX1 and AEBP2. The
assertion in the script is on **membership** (`Q6ZN18 ∈ withheld set`), not on the count —
two cancelling errors can keep a count right while corrupting the set.

So the TFClass pipeline made the discrimination correctly and deliberately. Reported as a
non-confirmation; a lead in the brief is a hypothesis, not a quota.

**The reciprocal question is where the real gap is.** AEBP2's DNA binding *has* been
measured, twice, and GO carries none of it:

- `[PMID:10329662 "We have identified a novel transcriptional repressor, AEBP2, that binds to a "]`
  regulatory sequence (AE-1) in the aP2 promoter — mouse;
- `[PMID:19293275 "Subsequent gel shift assays using the sequences obtained from these target loci revealed one potential DNA-binding motif for AEBP2, CTT(N)15-23cagGCC."]`
  — also mouse (mouse GST fusions, mouse brain ChIP).

Yet **no `GO:0003677` (or descendant) row exists on human AEBP2, mouse Aebp2, or
Drosophila jing** — positive control: human TP53 returns 15 rows from the identical
query pattern. And **`PMID:19293275` has zero annotations anywhere in GOA.** The paper
that defined this protein's DNA-binding motif is entirely absent from the GO record.

I did **not** propose `GO:0003677`. Both measurements are on the mouse protein, and the
human-protein DNA-binding data that exist
`[PMID:41168462 "PRC2–AEBP2S had the highest affinity to DNA and was the only complex for which a complete binding curve could be recorded"]`
are for the **complex**, not for AEBP2 alone. This is filed as a question to GO/PAINT
instead: is the omission deliberate, or a coverage gap?

## 4. The central finding: the dominant human isoform *restrains* PRC2

This is what reframes the whole annotation set, and it is isoform-resolved.

`[PMID:41168462 "In humans, there are three confirmed isoforms, which in this study are referred to as AEBP2L(iso1) (Q6ZN18-1), AEBP2L(iso2) (Q6ZN18-2) and AEBP2S (Q6ZN18-3)"]`
— so the paper maps directly onto UniProt's isoform ids, no inference required.

- `[PMID:41168462 "that AEBP2 enhances PRC2 function, we find that the widely expressed AEBP2L "]`
  isoform inhibits it — the sentence opens "Contrary to prior assumptions" on the preceding
  line of the cached abstract, so the quote is bounded to one physical line;
- `[PMID:41168462 "While core PRC2 alone and PRC2–AEBP2S exhibited comparable HMTase activities, PRC2–AEBP2L was almost completely inactive"]`
- `[PMID:41168462 "In human cells, AEBP2S is expressed mainly in the testis and is otherwise expressed at very low levels"]`

**Re-derive every comparison's two arms, per arm.** The affinage record's framing — "the short
isoform promotes PRC2 activity" — invites the reading that AEBP2S *stimulates* methyltransferase
activity. It does not, and the two isoforms differ per arm rather than uniformly. Against core
PRC2 alone:

| arm | + AEBP2L | + AEBP2S |
|---|---|---|
| HMTase, in vitro | **almost completely inactive** — below baseline | comparable to baseline |
| DNA binding, in vitro probe | Kd > 4000 nM, i.e. **at** baseline | **45.5 nM**, ~90× better |
| SUZ12 on chromatin, in cells | **below** the no-rescue control | above it |

So the only arm where AEBP2L is unambiguously *below* baseline in vitro is the
methyltransferase one — which is exactly the arm `GO:0180000` rests on — while in cells the
chromatin-occupancy reduction is also below control. On the naked-DNA probe AEBP2L merely fails
to confer what AEBP2S confers. Getting this per-arm rather than as one directional word is why
I did **not** propose `GO:0008047 enzyme activator activity` for the short isoform, even though
EED (IBA/IDA/IMP) and SUZ12 (IMP) already hold it; and an earlier draft of this file stated the
"below baseline" claim unqualified, which §15 records.

The direction is independently corroborated in vivo:

- `[PMID:27317809 "targeted mutation of Aebp2 unexpectedly revealed a Trithorax phenotype, normally "]`
  linked to antagonism of Polycomb function, with
  `[PMID:27317809 "Aebp2 mutant embryonic stem cells (ESCs). We further demonstrate that mutant "]`
  showing elevated H3K27 methylation (mouse);
- an independent lab, 11 years earlier, reached the same sign from transcription: the
  somatic/long isoform behaves as an activator and the embryonic/short isoform as a
  repressor of *Snai2* — recorded in PMID:41168462 as
  `[PMID:41168462 "Another report showed that the two main isoforms of AEBP2, the short (AEBP2S) and the long (AEBP2L), bind the promoter of the Snai2 gene in mouse thymus tissue, yet AEBP2S promotes its repression, whereas AEBP2L promotes its transcription (Kim et al, 2015)."]`

Two independent groups converging on the same sign from different assays is much stronger
than either alone.

**Why the field's earlier consensus said the opposite, and it is not a contradiction:**
`[PMID:41168462 "AEBP2S has been shown to enhance PRC2 HMTase activity in vitro"]` and
`[PMID:41168462 "However, no structures of PRC2 containing AEBP2L are currently available, as all previous studies used either AEBP2S or its partial sequence, without its N-terminus"]`.

I checked that claim rather than repeating it, because two verdicts lean on it. Of the
**17 PDB entries** that resolve an AEBP2 chain mapped to Q6ZN18, **15 declare an
N-terminally truncated construct** (UniProt-mapped starts at residues 209, 210, 223, 224,
225, 258, 379, 407). Only two declare 1–517: **8EQV** (released 2024-07-31, primary
citation **PMID:41168462** — the AEBP2L paper's own structure) and **8FYH** (2023,
PMID:37733873). So the census **partially** confirms the paper: the pattern is real and
overwhelming, but "all previous studies" is not exactly right, because 8FYH predates 8EQV
and declares full length. Scope note: these are the *declared UniProt-mapped entity
ranges*, not the resolved residues, so 8FYH may model less than it declares — I did not
test that, and say so rather than resolving it in my own favour.

## 5. `GO:0031507 heterochromatin formation` is a complex-level projection

Both rows are `NAS` from ComplexPortal, on `PMID:33514705` and `PMID:29348366`. The
reference-projection test (fully paginated) says these are projections, not observations:

| reference | annotations | entities | of which ComplexPortal complexes | dominant signature |
|---|---|---|---|---|
| `PMID:33514705` | 38 | 9 | 2 (CPX-2212, CPX-2330) | identical 4-term set on 5 entities |
| `PMID:29348366` | 35 | 9 | 2 (CPX-2209, CPX-2213) | identical 4-term set on 6 entities |

In both, the same NAS triple (`GO:0000122` + `GO:0031507` + `GO:0005634`) lands on the
complexes **and** every subunit — EED, RBBP4, SUZ12, RBBP7, EZH1/EZH2, JARID2 and AEBP2.

The brief's second question is the discriminating one: **does the functional term spread,
or stay on the entity that was perturbed?** On `PMID:33514705` it stays put — `GO:0031491`
nucleosome binding, `GO:0046976` H3K27 methyltransferase activity and `GO:0140693`
condensate scaffold activity are all `IMP` on **EZH1 alone**, the catalytic subunit. So
ComplexPortal was careful with the catalytic MF and projected the BP/CC.

The census across the complex confirms the shape rather than assuming it: `GO:0031507`
is held by **NAS alone** on AEBP2, JARID2, MTF2, PALI1, PHF19, RBBP4, RBBP7 and SUZ12, and
with other evidence (IDA/ISS/IBA) only on **EED, EZH1, EZH2**. The term tracks complex
membership, not per-subunit evidence.

Add to that: both references are **structure papers**, and neither assays heterochromatin
nucleation, spreading or boundary formation, which `GO:0031507`'s definition explicitly
requires ("This process starts with heterochromatin nucleation, its spreading, and ends
with heterochromatin boundary formation"). And AEBP2's own functional data run the other
way for the broadly expressed isoform (§4).

→ **`MARK_AS_OVER_ANNOTATED`**, not `REMOVE`. Unmeasured for AEBP2 earns
over-annotation; measured-and-absent would earn removal, and PRC2 as a whole does
establish facultative heterochromatin, so nothing here is refuted.

## 6. The two IBA rows are both well founded, for different reasons

**`GO:0035098` IBA** — WITH/FROM `MGI:MGI:1338038 | PANTHER:PTN002323211 | UniProtKB:Q6ZN18`.
The `UniProtKB:Q6ZN18` token is **self-referential**, which is valid: it records a PAINT
curator judging the function core (`NO_FAILURE_CORE`, never `CIRCULAR`). `MGI:MGI:1338038`
resolves — via the *bare* number, since an inner colon returns HTTP 400 — to mouse Aebp2
`Q9Z248` (reviewed, 504 aa), among 4 candidates of which 1 is Swiss-Prot; the 3 TrEMBL
candidates are reported, not hidden. That donor carries **three independent IDA rows** for
`GO:0035098` (`PMID:20064375`, `PMID:20064376`, `PMID:31451685`). Nothing here is
circular or family-level.

**`GO:0006357` IBA** — WITH/FROM `FB:FBgn0086655 | MGI:MGI:1338038 | PANTHER:PTN002323211`.
`FB:FBgn0086655` resolves to Drosophila **jing** `Q7KHG2` (reviewed, 1486 aa), the fly
member of the same family (UniProt: "Belongs to the AEBP2/jing C2H2-type zinc-finger
family").

Asking *which term* each donor holds, not merely whether it holds one, produced the best
argument in the review: mouse Aebp2 carries `GO:0000122` **IMP**, and jing carries
`GO:0000122` **IMP** *and* `GO:0045944` **IMP** — i.e. the donors are **split on the sign
of the regulation**. `GO:0006357` is exactly their lowest common ancestor. PAINT climbed to
the direction-neutral parent instead of picking a direction, which is the ontology and the
pipeline both working correctly. `GRANULARITY_MISMATCH` is inapplicable: it requires the
donors to agree.

The script asserts this rather than asserting it in prose: if the donor directions ever
stop disagreeing, the check fails and tells you the LCA argument must be re-derived.

**Node reach, and the reciprocal question.** `PTN002323211` reaches **117 recipients** in
196 annotations. All 117 get `GO:0006357`; only **79** also get `GO:0035098`, so **38**
receive the transcription term without the animal PRC2 complex term. PAINT is therefore
withholding the complex term from a subset rather than blanket-propagating it — again the
pipeline behaving well. Reported as a negative for the over-propagation hypothesis.

## 7. `GO_REF:0000120` is only as independent as its tokens — and here it is one witness

WITH/FROM: `ARBA:ARBA00089504 | UniProtKB:Q9Z248 | ensembl:ENSMUSP00000084896`. Resolving
**all** tokens shows `ensembl:ENSMUSP00000084896` **is** `Q9Z248` (mouse Aebp2). So a
combinatorial reference asserting agreement between independent methods here records
**one protein twice** plus one rule.

That rule is worth reading. `rest.uniprot.org/arba/ARBA00089504` asserts exactly one thing
— `GO:0035098` — from **8 alternative condition sets, each a FunFam-id + taxon conjunction
containing no residue, interaction or assay term at all**. The set that fires on AEBP2 is

```
FunFam 3.30.160.60:FF:000323  AND  FunFam 3.30.160.60:FF:000471  AND  Eukaryota  AND NOT Ascomycota
```

and AEBP2's own cross-references are exactly `3.30.160.60:FF:000323` and
`3.30.160.60:FF:000471`. The other seven sets cover other PRC2 subunits' structural
families (`2.170.270.10` SET domain → EZH1/EZH2; `2.130.10.10` WD40 → EED/RBBP4/RBBP7),
each with its own taxon clause. So **membership of a named multiprotein complex is granted
on structural-family membership plus taxon**, and the requirement for *two* co-occurring
AEBP2-specific FunFams is what keeps it from over-reaching.

The conclusion is nonetheless **true** for AEBP2, and four other rows (one IBA, two IPI,
one IDA) establish it experimentally, so this is an ACCEPT with the route documented — not
a defect. I have not filed it as an ARBA complaint; it is a note on how the row was made.

## 8. Molecular function: AEBP2 is the only PRC2 subunit with none

| subunit | total GOA rows | MF rows |
|---|---|---|
| EZH2 | 169 | 94 |
| RBBP4 | 196 | 63 |
| EED | 91 | 47 |
| EZH1 | 72 | 43 |
| SUZ12 | 87 | 39 |
| PHF19 | 55 | 36 |
| RBBP7 | 135 | 31 |
| PALI1 (LCOR) | 45 | 25 |
| EPOP | 17 | 9 |
| JARID2 | 35 | 7 |
| MTF2 | 28 | 5 |
| **AEBP2** | **20** | **0** |

Asserted on membership: the set of PRC2 subunits with zero MF rows must be exactly
`['AEBP2']`, and there is a tripwire on the aspect census so that if a molecular_function
row ever appears in GOA the script says the claim in this file is stale.

Meanwhile mouse Aebp2 holds `GO:0003712 transcription coregulator activity` by **IDA and
IMP** (MGI, `PMID:10329662`) — the only MF annotation anywhere in the ortholog set — and
UniProt's own `DR GO` block lists three MF terms for human AEBP2 that GOA does not carry:

| UniProt `DR GO` row | in GOA? | route |
|---|---|---|
| `GO:0003677 DNA binding; IEA:UniProtKB-KW` | no | Swiss-Prot keyword — GOA stopped importing these (~Apr 2026) |
| `GO:0008270 zinc ion binding; IEA:UniProtKB-KW` | no | same |
| `GO:0006351 DNA-templated transcription; IEA:UniProtKB-KW` | no | same |
| `GO:0003712 transcription coregulator activity; IEA:Ensembl` | **no** | a live Ensembl route GOA does not reflect |

The three keyword rows are the retired SPKW route and there is no GO row to act on, so per
the ADCK5 pattern they are filed as a UniProt observation, not a GO action. The
`GO:0003712` divergence is different — that route is live — and is filed as a question.

I did **not** propose `GO:0003712` for human AEBP2, for a reason worth recording: **no
human PRC2 subunit carries it** (checked across all 12 in the table above), and the term's
definition requires modulating transcription "via binding to a DNA-binding transcription
factor", which is not how PRC2 is recruited. Adding it to AEBP2 alone would make the gene
inconsistent with the complex it belongs to.

## 9. What I did propose, and why each is scoped the way it is

**`contributes_to GO:0031491 nucleosome binding`** — `contributes_to`, not `enables`,
because the activity is the assembled module's. UniProt records
`REGION 495..517 /note="Important for nucleosome binding activity of the PRC2 complex"`,
and the underlying measurements are isoform-resolved:
`[PMID:29499137 "It binds to the C2 domain of Suz12 and relocates the latter to a unique position in S12R4J2A2 to promote nucleosome binding"]`
and, for the C-terminus,
`[PMID:29499137 "while S12R4J2A2d lost binding to mononucleosomes, S12R4J2A2a exhibited a 2-fold enhancement of nucleosome binding compared to the wild-type counterpart"]`
where the constructs are defined as
`[PMID:29499137 "We disturbed the H3K4D by either deleting the last 5 residues to mimic Aebp2 from some lower eukaryotes (A2d) or adding the 14 residues found in isoforms 1 and 3 (A2a)"]`.

**A trap I nearly walked into.** `PMID:29348366` reports that AEBP2 "interacts with the
RBAP48 subunit, mimicking an unmodified H3" tail, and `PMID:29499137` shows
`[PMID:29499137 "The C-terminus of human Aebp2 isoform 2 thus appears to displace H3K4 from Rbbp4 through direct competition."]`
That is AEBP2 **being mimicked as** a histone, not AEBP2 **binding** a histone — its own
C-terminal K502/R503 occupy the RBBP4 pocket that H3K4/R2 would use. So `GO:0042393
histone binding` is **not** supported by these papers, and I did not propose it, even
though the affinage record lists it in its own grounding.

**`GO:0180000 histone methyltransferase inhibitor activity`**, scoped to `Q6ZN18-1` — the
definition is "Binds to and stops, prevents or reduces the activity of a histone
methyltransferase", which is what was measured (§4). The in-pathway precedent was measured,
not assumed: the term has **15 annotations in GOA, all EZHIP orthologs**, with a single
experimental anchor, human **EZHIP `Q86X51` IDA `PMID:30923826`**. AEBP2 would be the
second protein in GO to hold it, and EZHIP is the canonical PRC2 inhibitor, so the
proposal sits inside an existing curation pattern rather than inventing one.

**Sufficiency vs requirement, stated because GO's codes do not distinguish them.** The
`GO:0180000` proposal rests on a **requirement**-type result in cells (loss of AEBP2L
raises PRC2 occupancy and H3K27me3) *and* a direct in vitro measurement on recombinant
human proteins. By contrast the `GO:0000122` evidence is **sufficiency**-type: the 1999
data are co-transfection over-expression and a Gal4-tethering experiment
(`[PMID:10329662 "Moreover, a chimeric construct encoding a fusion AEBP2 protein with the Gal4 "]`
DNA-binding domain repressed a heterologous promoter), which shows AEBP2 *can* repress when
delivered to a promoter, not that the gene is required for repression anywhere.

## 10. Checks that came back negative — recorded because a null is a finding

- **Logical-opposite citation cross-product**: intersecting the reference sets of
  `GO:0000122`/`GO:0045944`, `GO:0045892`/`GO:0045893` and `GO:0031507`/`GO:0031508` finds
  **nothing**; no logically opposed pair is co-annotated on this gene. The detector is
  demonstrated to see a synthetic cross-product, so the negative is not the silence of a
  broken comparison.
- **Paralog-transfer / wrong-donor check**: both IBA donors are genuine family members
  (mouse ortholog; the fly member of the AEBP2/jing family). No paralog substitution.
- **PANTHER node over-reach**: the node withholds `GO:0035098` from 38 of its 117
  recipients. No blanket propagation.
- **Fold-to-activity (`domain name became an activity`)**: absent from GOA. There is no MF
  row at all, so there was nothing to remove. Non-confirmation, and consistent with the
  brief's running scoreboard.
- **Retraction / erratum scan**: the PMIDs this review relies on
  (10329662, 15225548, 19293275, 27317809, 29348366, 29499137, 29681498, 33479123,
  33514705, 20075857, 41168462) carry no retraction, erratum or expression-of-concern
  notice in their cached records.

## 11. Provider handling

`gates_passed: True`, `faith_pct: 100.0`, 24 citations. Two are **bioRxiv DOIs in a
PMID-shaped field** (`PMID:bio_10.1101_2025.11.09.687442`,
`PMID:bio_10.1101_2025.10.14.682307`); both concern the isoform story, and **no claim in
this review rests on either** — the peer-reviewed `PMID:41168462` carries it instead.

Recall was, unusually, good on this gene: the affinage record surfaced `PMID:41168462`,
which is the paper that reframes the annotation set. Its **framings** still needed
re-derivation (§4): "the short isoform promotes PRC2 activity" collapses a DNA-binding
result and an HMTase result whose baselines differ. A provider's arithmetic and
comparisons reach you by reading, not by quoting.

Its GO grounding block lists `GO:0042393 histone binding`, which §9 shows the cited
structural papers do not support, and `GO:0003677 DNA binding`, which GOA deliberately
does not carry — so the caveat printed in the record about that block being coarse is
accurate and worth obeying.

## 12. Verdict summary

| term | rows | evidence | action |
|---|---|---|---|
| `GO:0035098` ESC/E(Z) complex | 5 | IBA, IEA(`GO_REF:0000120`), IPI ×2, IDA | ACCEPT |
| `GO:0006357` reg. of transcription by RNA Pol II | 1 | IBA | ACCEPT |
| `GO:0000785` chromatin | 1 | ISA (TFClass) | ACCEPT |
| `GO:0005654` nucleoplasm | 4 | IDA (HPA), TAS ×3 (Reactome) | ACCEPT |
| `GO:0005634` nucleus | 4 | IEA, NAS ×2, EXP | ACCEPT |
| `GO:0000122` neg. reg. of transcription by RNA Pol II | 3 | IEA (Compara), NAS ×2 | KEEP_AS_NON_CORE |
| `GO:0031507` heterochromatin formation | 2 | NAS ×2 | MARK_AS_OVER_ANNOTATED |
| `GO:0031491` nucleosome binding (`contributes_to`) | — | proposed, IDA | NEW |
| `GO:0180000` histone MTase inhibitor activity (`Q6ZN18-1`) | — | proposed, IDA | NEW |

20 existing rows + 2 NEW = 22 `existing_annotations` entries. The extra two are my own
proposals and are marked `NEW`.

`GO:0000122` is `KEEP_AS_NON_CORE` rather than `ACCEPT` because it is true of one isoform
and one direction: it is supported for AEBP2S and in the PRC2.2 context, and contradicted
for the broadly expressed AEBP2L. The gene's core biological process is better carried by
the direction-neutral parent `GO:0006357`, which is why that one is ACCEPT and in
`core_functions`. The same-term-same-action rule forces all three `GO:0000122` rows to
share the verdict, which is correct here since they all trace to the same repression model.

## 13. Isoform bookkeeping

| isoform | UniProt id | paper's name | span | note |
|---|---|---|---|---|
| 1 | `Q6ZN18-1` | AEBP2L(iso1) | 1–517 (displayed) | inhibits PRC2 |
| 2 | `Q6ZN18-2` | AEBP2L(iso2) | Δ504–517 (**MANE-Select**, `ENST00000266508`) | inhibits PRC2; also deletes 14 of the 23 residues of the `495..517` nucleosome-binding region |
| 3 | `Q6ZN18-3` | AEBP2S | Δ1–216 + 217–223 substituted → 301 aa | promotes PRC2 DNA binding; human expression essentially testis-only |

The isoform-2 overlap is computed, not eyeballed: the deletion `[504, 517]` against the
region `[495, 517]` is **14 of 23 residues**, and the script fails if that overlap ever
goes to zero. It matters because `PMID:29499137` measured that adding those 14 residues
back doubles nucleosome binding — so the *reference transcript's* protein is the weaker
binder. **The difference is quantitative, not qualitative**: isoform 2 supports the activity,
roughly twofold less well. An earlier draft of this review turned that preference into an
exclusion; see §15.

Also worth recording: `PMID:29499137`'s crystal used
`[PMID:29499137 "The Aebp2 fragment used in the crystal structure of S12R4J2A2 contains the last 97 residues of human Aebp2 isoform 2, including the C2B and H3K4D domains (Fig. 1A)."]`
— consistent with the computed PDB range for 5WAI (407–503).

All seven `CC INTERACTION` partners in UniProt (HMBOX1, KRTAP10-8, LDOC1, MDFI, PICK1,
TSPYL2, ZNF408) are logged against isoform `Q6ZN18-2` with `NbExp` 3–6. None of them is a
PRC2 component and none appears in GOA, so no annotation rests on them; I did not analyse
them further beyond noting that `NbExp` has three known wrong meanings in this campaign
(sub-methods of one screen, screen replicates, domains of one partner) and cannot be read
as an evidence-strength proxy.

## 14. Process and the committed guards

Worked in an isolated worktree (`/private/tmp/AEBP2-wt`, branch `paint/AEBP2`). Three
committed scripts, each with `--self-test`:

| script | what it enforces |
|---|---|
| `analyze_aebp2.py` | every number in this file and in the review YAML; 12 checks, all with positive controls |
| `check_review_quotes.py` | every `supporting_text` verbatim, including the `file:` quotes CI skips entirely and the `provenance` blocks `checkquotes.py` does not walk; strict duplicate-key loader; anchor refusal; raw-vs-parsed reconciliation |
| `audit_review_consistency.py` | summary opener vs action, same-term-same-action, the hedge sweep, complex-not-in-locations, description hygiene, isoform scoping on `NEW` rows, the notes verdict table in **both** directions, and 13 prose numbers tied to `results.json` |

**A number that refused to add up, caught in self-review.** Two surfaces said the PRC2
molecular-function census covered "eleven" proteins. It covers **twelve** — the table has
twelve rows, and `EPOP` is the twelfth, absent from the `GO:0031507` tally only because it
carries that term by no evidence at all. The adjacent claim, "eight of eleven hold
`GO:0031507` by NAS alone", was *correct* for a different denominator (11 of the 12 carry
the term), which is exactly why the wrong one read as consistent. Fixed to name the
denominator explicitly in both places.

The structural fix, not just the text fix: `audit_review_consistency.py` check H now reads
each such number out of `results.json` and requires the prose to contain the measured
value, so a changed query breaks the check instead of quietly falsifying the sentence.
Adding it immediately caught a second instance of the same class — the ARBA condition-set
count was **spelled out as a word**, and a number written as a word is invisible to any
check that greps for the digit. Both directions are break-tested: a drifted digit fires,
and so does a digit respelled as a word.

Two real defects in my own code were found only by writing the break-tests, never by
reading:

- the QuickGO paginator turned the service's undocumented page cap into an opaque
  HTTP 400 instead of a loud truncation report. A rejected query and a genuine
  end-of-results are indistinguishable downstream, so it now raises with `truncated` in
  the message and names the retrieved-vs-total counts;
- the UniProt feature dispatch keyed on the **flat-file** name `VAR_SEQ` where the JSON
  says `Alternative sequence`, which silently emptied the isoform list. Caught only
  because a presence guard on `VSP_034359` existed; an overlap calculation alone would
  have happily reported nothing and the isoform section of this file would have been
  quietly wrong.

Each self-test was itself proven able to fail. Reverting `is_reviewed` to the substring
form `"reviewed" in entryType` — which also matches *un*reviewed — makes `analyze_aebp2.py
--self-test` exit 1 with `is_reviewed: promoted a TrEMBL entry to reviewed`. The other two
harnesses assert the failure *message* on every direction, not merely that something
failed, and each mutation is asserted present before it is applied so a drifted anchor
cannot make a break-test a silent no-op.

**A hook error I did not obey.** The repo's pre-write hook resolves `file:` paths against
`$CLAUDE_PROJECT_DIR`, so from a sibling worktree it reported 24 non-existent-file errors
and a batch of "text part not found" errors for quotes that are all present. Verified
before acting rather than complying: the three target files exist, `just validate human
AEBP2` inside the worktree returns `✓ Valid`, and `check_review_quotes.py` matches all 53
quotes exactly. Complying would have meant deleting correct evidence.

## 15. Round 2: the isoform scope was an exclusion where the data show a preference

The reviewer's blocking point was correct, and verifying it against the cached full text is
what settled it rather than deferring:

- the wild-type reconstituted module in `PMID:29499137` is
  `[PMID:29499137 "The Aebp2 fragment used in the crystal structure of S12R4J2A2 contains the last 97 residues of human Aebp2 isoform 2, including the C2B and H3K4D domains (Fig. 1A)."]`
  — i.e. **isoform 2's** C-terminus;
- and it worked:
  `[PMID:29499137 "We found that S12R4 exhibited poor nucleosome binding by itself"]`
  against
  `[PMID:29499137 "In stark contrast, S12R4J2A2 displayed robust binding towards mononucleosomes, with a low micromolar binding affinity"]`.

So the 14 extra residues of isoforms 1 and 3 give a **twofold enhancement** over an already
robust baseline, and only the engineered five-residue deletion — not any natural isoform —
abolishes binding. My `core_functions[0]` had converted that preference into an **exclusion**,
writing the MANE-Select form out of the gene's only proposed `contributes_to` molecular
function. The annotation row's own reason had it right ("expected to be weaker for
`Q6ZN18-2`"), so the file contradicted itself with the correct reading in the row.

Two consequences beyond the wording:

- **The `isoform:` field on that row now reads `Q6ZN18-2`, not `Q6ZN18-1`.** Per CLAUDE.md the
  field records *what was tested*, and what was tested was isoform 2's C-terminus. The activity
  is not isoform-restricted at all — all three isoforms retain residues 407–503 — so recording
  the tested form is both literally correct and less misleading than naming the strongest one.
- **The scope is now single-sourced.** Two surfaces could express it, so correcting one left the
  other; `audit_review_consistency.py` check I requires one canonical clause verbatim on both
  surfaces and fires if either diverges. Its retracted-phrase list scans the review YAML only,
  and deliberately not this notes file, because a notes file has to be able to *narrate* a
  retraction — that limitation is stated rather than papered over.

### The correction propagated to a surface nobody had flagged

Adding check I's retracted-phrase list caught a **third** instance of a related imprecision:
"suppresses PRC2 DNA binding and methyltransferase activity" appeared in the `GO:0000122` row's
reason and in a `suggested_question` addressed to UniProt curators. Re-deriving the arms shows
why it was wrong:

| arm | core PRC2 alone | + AEBP2L | + AEBP2S |
|---|---|---|---|
| DNA binding, in vitro probe | Kd > 4000 nM | Kd > 4000 nM (**at baseline**) | **45.5 nM** |
| HMTase, in vitro | baseline | **almost completely inactive** | comparable to baseline |
| SUZ12 on chromatin, in cells | no-rescue control | **below the control** | above |

`[PMID:41168462 "Conversely, core PRC2 alone, PRC2–AEBP2L(iso1) and PRC2–AEBP2L(iso2) complexes did not substantially bind the DNA probe, which indicates a much lower affinity"]`
and
`[PMID:41168462 "However, ectopically expressed AEBP2L reduced the amount of SUZ12 on chromatin compared to AEBP2S and even compared to the no-rescue control cells"]`.

So "AEBP2L inhibits PRC2 DNA binding" — the paper's own abstract wording — is **true of chromatin
occupancy in cells and not of the naked-DNA probe in vitro**, where AEBP2L merely fails to confer
what AEBP2S confers. The below-baseline claim that `GO:0180000` rests on is the **methyltransferase**
arm, which is untouched and is if anything cleaner for having been separated out. Same shape as
the provider-arithmetic lesson: a directional word is meaningless until you know which two arms
the comparison has.

### Refuting the reviewer's BP-term suggestion, with evidence

The review was asked why no biological-process term is proposed in the
regulation-of-H3-K27-methylation branch for the headline finding. **Because GO has dismantled
that branch.** Fetched from QuickGO:

| term | status |
|---|---|
| `GO:0016571` histone methylation | **obsolete** |
| `GO:0031056` regulation of histone modification | **obsolete** |
| `GO:0031060` / `GO:0031061` / `GO:0031062` regulation of histone methylation | **obsolete** |
| `GO:0061085` / `GO:0061086` / `GO:0061087` regulation of histone H3-K27 methylation | **obsolete** |

None carries a `term_replaced_by`. A search of live `biological_process` terms returns **no**
non-obsolete regulation-of-histone-methylation term, controlled against a search for
"heterochromatin formation" that *does* return live terms — so the zero is a real zero and not a
failed query. A process term cannot be requested in a branch GO deliberately removed, and the
molecular-function regulator route is what GO now provides, which is exactly where this review
puts the claim (`GO:0180000`, plus the proposed activator sibling). Recorded in the second
`proposed_new_terms` justification.

### Round 3: the literal pin missed a fifth variant, so the guard changed shape

The reviewer's non-blocking follow-up found `core_functions[1]` still saying "suppresses the
complex's DNA binding" without naming the arm — **a fifth variant of the same sentence, which
the retracted-phrase pin did not match.** That is the documented limitation of a literal pin
arriving in practice, so the response was to change the guard's shape rather than add a fifth
literal.

`audit_review_consistency.py` **check J** now anchors on the claim's *structure*: any sentence
that pairs a suppression verb with a DNA-binding marker and a long-isoform subject must also
carry an arm qualifier. It runs over the **parsed document's prose fields**, not the raw file —
the first version sentence-split the whole YAML and fired on a run-together of a
`supporting_text` quote and a term label, because the detector and the artifact disagreed on
what a sentence is.

Its vacuity guard also had to be rewritten. The first version required at least one *qualified*
suppression claim, which a correctly-written file need not contain at all — it failed on perfect
agreement, the classic guard-defeat mode. The precondition a correct file can satisfy is that
the matcher reaches DNA-binding prose at all; 22 sentences do.

**Coverage demonstrated against the defects that actually shipped**, not against an invented
mutation. `--history` runs check J over every version this branch pushed:

| version | check J flags |
|---|---|
| `a50319089` (first push) | **4** |
| `c58380583` | **4** |
| `80c1459c9` (the version the reviewer flagged) | **1** — exactly the variant the literal pin missed |
| current | **0** |

`--history` asserts that the sequence decreases monotonically, that the current count is zero,
that the first version flags at least two (or the check is not demonstrating coverage of a
class), and that the reviewer-flagged version flags exactly one. It refuses to report a zero
from a git extract shorter than 500 lines, because a silent zero from a failed extract is
indistinguishable from a clean result — which happened once while developing it.

The other follow-up: the `GO:0180000` row justified its `isoform:` field from the DNA-binding
arm when the term is about methyltransferase activity. Corrected, and the limitation stated
rather than glossed: the HMTase result is reported for "PRC2-AEBP2L" without separating the two
long isoforms, so `Q6ZN18-2`'s methyltransferase behaviour is **inferred, not measured** — the
two were separately measured only in the DNA-binding arm.

### Five references added

`PMID:20064375`, `PMID:20064376`, `PMID:31451685` (the three behind mouse Aebp2's `GO:0035098`
IDA rows, which is what makes that IBA well-founded), `PMID:21949878` (the neural-crest sentence
in the description) and `PMID:31959557` (cited by UniProt's FUNCTION line and by the isoform
question). All five were cited in prose while absent from `references:` — a gap the reviewer
found and that no gate checks.
