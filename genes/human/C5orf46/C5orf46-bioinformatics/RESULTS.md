# C5orf46 (Q6UWT4) — computed evidence for the GO annotation review

Every **number** below is computed by `analyze_c5orf46.py` and mirrored in `results.json`;
the prose around them is written, not generated, so a re-run reproduces `results.json`
byte-for-byte but does not rewrite this file. Re-run with
`uv run --no-project python analyze_c5orf46.py`; the fetched records are cached in `data/`
so the numbers are reproducible without network access. Because quotations from this file
are cited as `supporting_text` in the review, they are deliberately taken from computed
table rows rather than from the surrounding prose — a `file:` quote into a generated
artifact is a two-way dependency, and prose gets reworded. `--self-test`
break-tests every guard and asserts the failure *message*, not merely the failure.

Guard note: the only reported zeros in this document are paired with a non-zero
positive control from the same endpoint in the same call pattern, because a rejected
query and a genuine negative are indistinguishable downstream.

Cache note, so nobody mistakes `data/` for raw responses: the cached records are
**projections**, narrowed at fetch time to the fields this analysis reads. The raw
IntAct responses carry every cross-reference of both partners on every record and came
to **558 MB**, which is not committable; the projection is **0.6 MB** and every number
in this document was verified to reproduce exactly across it. `numberOfHits` and
`totalElements` are preserved, so the anti-truncation assertions still have something to
check. Re-run with `--refresh` to re-fetch.

---

## A. The peptide assayed as "AP-64" is UniProt's annotated mature chain of Q6UWT4

`PMID:33804835` calls its molecule AP-64 and states three properties of it. All three
are reproduced from UniProt's own `CHAIN 24..87` of Q6UWT4:

| property | paper states | computed from UniProt CHAIN 24..87 |
|---|---|---|
| length | 64 residues (the "64" in the name) | **64** |
| molecular weight | `MW = 7.2` | **7.22 kDa** |
| isoelectric point | `PI = 4.54` | **4.54** |
| cysteines | "contains no cysteines" | **0** |

Positive control on the instrument: the same mass routine gives **9693.1 Da** for the
full 87-residue precursor against the **9693** UniProt states in its `SQ` line. Without
this control a wrong mass table could "confirm" the paper; the break-test verifies that
corrupting the table trips the control *and* suppresses the mature-peptide numbers
rather than reporting them anyway.

This matters for one specific reason. A named peptide derived from a larger gene product
is a standing hazard in GO curation — pharmacology performed on a synthetic fragment gets
attributed to the parent gene. Here the assayed molecule is not a fragment: it is exactly
the protein that remains after the annotated 23-residue signal peptide is removed, i.e.
the physiological secreted product. The paper's evidence is therefore evidence about this
gene product.

Composition of the mature chain: 16 acidic residues (D+E) against 10 basic (K+R) and one
histidine — an anionic peptide, unusual among human antimicrobial peptides and the reason
the paper compares it to dermcidin rather than to the defensins or LL-37.

## B. Amphipathicity, and where the hydrophobic maximum actually sits

Kyte–Doolittle, 19-residue window, over the 87-residue precursor:

| window | KD-19 | position | segment |
|---|---|---|---|
| global maximum | **+2.51** | residue 10 | inside the signal peptide (1–23) |
| maximum within the mature chain | **+1.08** | residue 56 | `KFLSLLGTEIIENAVEFIL` |
| global minimum | **−2.90** | residue 33 | the `DDKPDKPDDKPDD` acidic region |

So the mature peptide is amphipathic in the way the paper describes — hydrophilic acidic
N-terminal half, hydrophobic central segment — and, separately, **the single most
hydrophobic window in the full open reading frame is the uncleaved signal peptide.** That
second fact is used in section D and nowhere else. The direction of the comparison is
asserted by a guard; inverting the hydropathy scale trips it.

No secondary-structure or mechanism claim is made here. The paper's α-helix is a PSIPRED
prediction with circular-dichroism support for helical content, which establishes that a
helix exists, not that it forms a pore or spans a membrane.

## C. The 14 `GO:0005515` rows resolve to 13 partners, and the set has one composition

Partner accessions are parsed from the `WITH/FROM` column of `C5orf46-goa.tsv` and asserted
to equal the set QuickGO returns for the same term — on **membership**, not cardinality.
(The break-test includes a length-preserving substitution that a cardinality check cannot
see; it is reported as such, so the membership assertion is demonstrably load-bearing.)

Reviewed status uses `entryType.startswith("UniProtKB reviewed")`. On this gene the naive
`"reviewed" in entryType` test scores **13/13 reviewed** while the anchored test scores
**12/13** — the substring bug is not hypothetical here, it changes the number.

| partner | accession | status | length | TM features | UniProt location | distinct IntAct partners | GOA rows |
|---|---|---|---|---|---|---|---|
| PEX12 | O00623 | Swiss-Prot | 359 | 5 | Peroxisome membrane | 37 | 1 |
| SGTA | O43765 | Swiss-Prot | 313 | 0 | Cytoplasm; Nucleus | 281 | 1 |
| TMBIM6 | P55061 | Swiss-Prot | 237 | 6 | Endoplasmic reticulum membrane | 132 | 2 |
| TBXA2R | Q0VAB0 | **TrEMBL** | 259 | 3 | Cell membrane | 13 | 1 |
| AQP6 | Q13520 | Swiss-Prot | 282 | 6 | Cytoplasmic vesicle membrane | 382 | 1 |
| EBP | Q15125 | Swiss-Prot | 230 | 4 | Cytoplasmic vesicle; ER membrane; Nucleus envelope | 240 | 1 |
| LHFPL5 | Q8TAF8 | Swiss-Prot | 219 | 4 | Cell membrane | 138 | 1 |
| SGTB | Q96EQ0 | Swiss-Prot | 304 | 0 | (none stated) | 202 | 1 |
| RUSF1 | Q96GQ5 | Swiss-Prot | 468 | 1 | Membrane | 199 | 1 |
| TMEM80 | Q96HE8 | Swiss-Prot | 143 | 4 | Cell projection, cilium; Membrane | 66 | 1 |
| MIMS2 | Q96KR6 | Swiss-Prot | 192 | 2 | Mitochondrion inner membrane | 101 | 1 |
| SLC30A2 | Q9BRI3 | Swiss-Prot | 372 | 5 | Cell membrane; secretory-vesicle, endosome, lysosome, mitochondrial-inner and zymogen-granule membranes | 173 | 1 |
| TIMMDC1 | Q9NPL8 | Swiss-Prot | 285 | 4 | Mitochondrion membrane | 185 | 1 |

Two features of this table are the finding:

1. **11 of 13 partners are integral membrane proteins** (≥1 annotated transmembrane
   feature; 44 TM segments across the set).
2. **The two exceptions are SGTA and SGTB**, the two human members of the SGT family of
   TPR co-chaperones (both carry the `Belongs to the SGT family` similarity statement and
   a TPR repeat array; they are 55.6% identical over the shorter sequence).

   **The hydrophobic-client role is curated for SGTA only, and that distinction is kept
   here rather than smoothed over.** UniProt's `FUNCTION` for SGTA reads *"Co-chaperone
   that binds misfolded and hydrophobic patches-containing client proteins in the
   cytosol"* and *"binding more rapidly the transmembrane domain of newly synthesized
   proteins"*. SGTB's entire `FUNCTION` is *"Co-chaperone that binds directly to HSC70 and
   HSP70 and regulates their ATPase activity"* — no hydrophobic-client claim at all. So
   SGTB's presence is *consistent* with the same explanation, by family membership and
   shared architecture, but it is not curated evidence for it.

   **This asymmetry is computed from the cached records, not read off the prose.** Check H
   scans the two entries' `FUNCTION` comments and reports:

   | | `FUNCTION` cues found | `SIMILARITY` | first 90 chars of `FUNCTION` |
   |---|---|---|---|
   | **SGTA** `O43765` | `hydrophobic`, `transmembrane` | Belongs to the SGT family | *"Co-chaperone that binds misfolded and hydrophobic patches-containing client proteins…"* |
   | **SGTB** `Q96EQ0` | **none** | Belongs to the SGT family | *"Co-chaperone that binds directly to HSC70 and HSP70 and regulates their ATPase activity"* |

   Four directions are break-tested: stripping `FUNCTION` from the cache, giving SGTB the
   hydrophobic-client role, taking it away from SGTA, and breaking the family statement. The
   first of those reproduces a defect that actually shipped in this PR — a narrowed cache
   projection had dropped `FUNCTION`, the very field this correction rests on, so the claim was
   right while the evidence for it had left with the projection. **When narrowing a cached
   projection, check that nothing you assert still depends on the fields you dropped.**

So every partner in the set is either a hydrophobic-helix-bearing membrane protein or an
SGT-family TPR co-chaperone, and the family's curated member binds exposed transmembrane
helices. The set has a single shared property, and it is hydrophobicity rather than a
pathway, a compartment or a complex.

**One partner is not the canonical protein.** `Q0VAB0` is an unreviewed 259-residue TrEMBL
entry for TBXA2R; canonical TBXA2R is `P21731`, reviewed, **343** residues. The annotation's
partner is an 84-residue-truncated clone, so even taken at face value the row does not
record an interaction with the thromboxane A2 receptor as curated.

**Compartment accessibility, stated with its limits.** Three partners sit in compartments a
signal-peptide-directed secretory protein never enters — PEX12 (peroxisome membrane, which
imports from the cytosol), MIMS2 and TIMMDC1 (mitochondrial inner/inner-membrane) — and two
more (SGTA, SGTB) are cytosolic. The ER-membrane partners TMBIM6 and EBP are at least on the
protein's own biosynthetic route, so this argument covers 5 of 13 rather than all of them,
and it is corroboration rather than the main point. What applies to all 13 is that every
interaction was scored in the *Saccharomyces cerevisiae* nucleus or in a HEK293T lysate, so
no partner was tested in its native topology at all.

## D. Interaction provenance: two pipelines, and `NbExp` counts sub-methods

IntAct holds **41** interaction records for Q6UWT4, fully paginated, from exactly **3**
publications:

| publication | detection method | records |
|---|---|---|
| PMID:32296183 (HuRI) | `two hybrid array` | 13 |
| PMID:32296183 (HuRI) | `two hybrid prey pooling approach` | 13 |
| PMID:32296183 (HuRI) | `validated two hybrid` | 12 |
| PMID:28514442 (BioPlex 2.0) | `anti tag coip` | 2 |
| PMID:33961781 (BioPlex 3.0) | `anti tag coip` | 1 |

Twelve of the thirteen partners come from **one** publication and carry **3 records each**
under three names of the same yeast two-hybrid screen. This is why UniProt's entry reads
`NbExp=3` for twelve partners: the number counts sub-methods, not experiments. SLC30A2
reads `NbExp=5` for the same reason — five records, still one publication, still the same
three methods, with two of them logged twice. Every HuRI record shares one MI-score, 0.56.
C5orf46 is the **bait** in **26 of the 38** HuRI records - the remaining twelve are the same
interactions re-logged under `validated two hybrid` with both partners as `neutral component`,
so 26/38 rather than 29/41 is the scoped number, the other three bait records being BioPlex.
The construct expressed in the yeast nucleus is therefore the full open reading frame,
including the hydrophobic signal peptide characterised in section B.

The only partner with more than one publication is **TMBIM6**, and both are `anti tag coip`
from the same affinity-proteomics programme (BioPlex 2.0 and its 3.0 expansion), so it is
one method in two releases rather than two independent assays. No orthogonal method — no
co-immunoprecipitation of endogenous protein, no biophysical binding measurement, no
reciprocal pull-down — supports any partner.

IntAct carries **14** distinct partners against GOA's 13: `Q9HAB8` (PPCS,
phosphopantothenate–cysteine ligase, 25 distinct IntAct partners) appears in BioPlex 2.0 at
MI-score **0.35** and has no GOA row. Recorded for completeness — the count difference is a
GOA/IntAct threshold difference, not a missing review row, and PPCS is noted here so a future
reviewer does not read the 13-vs-14 gap as an omission.

**Promiscuity, reported with its exceptions.** Distinct IntAct partners, fully paginated:

| protein | distinct partners |
|---|---|
| **C5orf46 (subject)** | **14** |
| AQP6 | 382 |
| SGTA | 281 |
| EBP | 240 |
| SGTB | 202 |
| RUSF1 | 199 |
| TIMMDC1 | 185 |
| SLC30A2 | 173 |
| LHFPL5 | 138 |
| TMBIM6 | 132 |
| MIMS2 | 101 |
| TMEM80 | 66 |
| PEX12 | 37 |
| TBXA2R (Q0VAB0) | 13 |

Twelve of thirteen partners exceed the subject's 14, most by an order of magnitude. The
claim is *not* that all thirteen are hubs: PEX12 at 37 is only 2.6× the subject, and the
truncated TBXA2R clone at 13 is **below** it. Those two are recorded as exceptions rather
than smoothed away.

## E. The annotation coverage gap, quantified

Evidence-code census for Q6UWT4 across all 16 GOA annotations: **IPI 14, IEA 1, HDA 1**.
Three distinct terms: `GO:0005515`, `GO:0005576`, `GO:0070062`. There is no molecular
function beyond `protein binding` and no biological process at all.

**IBA count: 0.** Positive controls in the same call pattern: ADGRA2 **6** IBA rows, ACTB
**11**. So the zero is a real absence, not a rejected query — consistent with UniProt's
own `PAN-GO; Q6UWT4; 0 GO annotations based on evolutionary models`. There is no PAINT
propagation on this gene to adjudicate.

**Annotations in all of GOA citing `PMID:33804835`, the sole functional characterisation of
this gene: 0.** Positive control from the same endpoint: `PMID:19199708` returns **396**.
The paper that purified the peptide, measured its bactericidal activity with a dose
response and an MIC, imaged the killed bacteria, and protected mice with it has never been
curated into GO for any organism.

**The family is uncurated too.** PANTHER `PTHR37864` contains **153 proteins across 426
taxa**, of which only **3** are reviewed Swiss-Prot entries — human C5orf46 (87 aa), mouse
Gm94 `Q3V2D2` (93 aa) and bovine `Q3T146` (88 aa). Their GO records:

| member | annotations |
|---|---|
| bovine Q3T146 | 1: `GO:0005576` IEA (GO_REF:0000044) |
| mouse Gm94 Q3V2D2 | 4: `GO:0005576` IEA, plus **`GO:0003674`, `GO:0008150` and `GO:0005575` by ND** (GO_REF:0000015) |

The mouse orthologue carries MGI's *"no biological data available"* root-term annotation in
all three aspects — while the same paper that characterised the human peptide reports that
Gm94, the mouse gene product, is itself bactericidal against Gram-negative bacteria and
protects mice in vivo. That is the coverage gap stated as sharply as it can be: the
ontology's explicit "nothing is known" placeholder sits on a gene with a published
purified-protein activity.

**The class IS curatable, and has been curated — for the sibling molecule.** The same
laboratory previously characterised C10orf99 as a human antimicrobial peptide under the same
naming convention, AP-57, and the AP-64 paper cites that work as its own predecessor. That
gene *was* curated: `Q6UWK7` (GPR15LG) carries **four IDA rows from `PMID:25585381`**, among
them `GO:0050830` defense response to Gram-positive bacterium and `GO:0050832` defense
response to fungus, all assigned by UniProt — which also took *"Antimicrobial peptide with 57
amino acid residues"* into the entry as an alternative name.

The two peptides are near-mirror images, which is what makes the comparison sharp rather than
loose:

| | AP-57 / C10orf99 (`Q6UWK7`) | AP-64 / C5orf46 (`Q6UWT4`) |
|---|---|---|
| charge | basic, net +14, pI 11.28 | **anionic**, pI 4.54 |
| cysteines | 4 | **0** |
| kills | Gram-positive bacteria, a fungus | **Gram-negative bacteria** |
| does not kill | (not the reported focus) | Gram-positives, yeast |
| GO term from its paper | **`GO:0050830`, curated** | `GO:0050829`, **absent** |

So `GO:0050829` proposed here is the exact counterpart of a term the sibling already holds,
from an equivalent experiment in an equivalent paper by the same group. The gap is a
consistency defect, not a request for a novel kind of annotation.

### The two curatorial precedents, queried rather than asserted

A PR review pointed out that these two claims sat in the review prose without a committed
query behind them, unlike every other quantitative claim here. They are now check **G** in
`analyze_c5orf46.py`, with both directions break-tested (an empty result is reported, and a
precedent the source does not actually hold is reported as false). Querying them changed one
of the two:

| precedent | what the query returns | strength |
|---|---|---|
| **C10orf99 / GPR15LG `Q6UWK7`**, 81 aa, reviewed | `GO:0050830` **IDA** and `GO:0050832` **IDA**, both from `PMID:25585381`, both assigned by UniProt | strong — a curator assigned these from the AP-57 experiments |
| **DCD dermcidin `P81605`**, 110 aa, reviewed | `GO:0031640` by **IEA, `GO_REF:0000002` (InterPro2GO)**; its *experimental* defence rows are `GO:0042742` IDA and `GO:0140367` IDA | **weaker than first stated** — precedent that the term is *used* for this class, not that it was assigned from an experiment |

So the dermcidin precedent is corroboration at reduced strength, and the non-redundancy of
`GO:0031640` against `GO:0050829` rests on the verified closure fetch (`GO:0031640` under
`GO:0001906`, not under `GO:0042742`) rather than on it. The C10orf99 precedent is unaffected
and remains the load-bearing comparison.

The same check also asserts the **subject holds none** of `GO:0031640`, `GO:0042742`,
`GO:0050829`, `GO:0050830`, `GO:0019731` or `GO:0061844` — because if it did, the two `NEW`
proposals would not be new. It holds none.

*Accession caution, recorded because it nearly propagated:* C10orf99 is **`Q6UWK7`**. An
earlier pass in this analysis looked it up as `Q6UWT2`, which is **adropin (ENHO)** — a
different protein whose record would have supported the opposite conclusion, that the class is
uncurated. The right accession was confirmed by `primaryAccession` and by the entry's gene
synonyms including `C10orf99`.

**Cross-review consistency of the protein-binding verdicts.** Across the 1,769 merged human
reviews on `main`, excluding this one, there are **803** `GO:0005515` rows whose reference is
HuRI (`PMID:32296183`). They are resolved as: `MARK_AS_OVER_ANNOTATED` **554 (69%)** over 465
genes, `KEEP_AS_NON_CORE` 142, `REMOVE` 87, `MODIFY` 12, `ACCEPT` 6, one `UNDECIDED`, one
`PENDING`. The 14 `MARK_AS_OVER_ANNOTATED` verdicts here therefore follow the corpus's
dominant convention rather than diverging from it — checked deliberately, because independently
reviewed genes giving one identical row three different answers is a known campaign defect.

Two hypotheses from the campaign brief were tested here and **did not confirm**, which is
worth recording so the next reviewer knows the checks were run:

- **Fold-name-becomes-an-activity.** `IPR027950` (DUF4576, Pfam PF15144) is the gene's only
  InterPro signature, and it has **no entry in interpro2go** — verified against all
  **30,122** `InterPro:` mapping lines in the current `external2go/interpro2go`, with `IPR001879`
  as a positive control showing the lookup works.
  No molecular function reaches this gene from a domain name, because no mapping exists.
- **Model organism lacks the orthologue.** It does not. Mouse Gm94 is a genuine 93-residue
  orthologue in the same PANTHER subfamily, and the AP-64 paper assayed it directly. The
  ADIRF-style "every experiment is ectopic expression in a lineage without the gene" caveat
  does not apply to this gene.

## What this does and does not support

Supported: the assayed molecule is this gene's mature secreted product; the peptide is
anionic, cysteine-free and amphipathic; the `GO:0005515` set is one two-hybrid screen plus
one affinity-proteomics pipeline, sharing hydrophobicity as its only common property, with
one partner not even the canonical protein; and the gene's functional literature is entirely
absent from GO in every organism.

Not supported, and deliberately not claimed: any mechanism for the killing (the paper itself
offers membrane damage and an intracellular target as alternatives and settles neither); any
molecular function term; and any inference that the interaction rows are false rather than
unsupported. The tables above are the claim; the sentences around them are not.
