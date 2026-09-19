# ARFGEF3 (BIG3) — computed evidence for the GO review

Two questions, both bearing on GO annotations that human ARFGEF3 currently holds:

1. Is `GO:0005085 guanyl-nucleotide exchange factor activity` (IBA + IEA) supported
   by ARFGEF3's own Sec7 domain, or is it a fold-derived, name-implied catalytic call?
2. What do the WITH/FROM donors of ARFGEF3's two IBA rows actually contribute?

Everything is fetched live from UniProt/QuickGO and aligned with MAFFT. Nothing is
hardcoded. Re-running reproduces the numbers below; `cache/` is disposable.

```
uv run --no-project --with requests --with biopython python resolve_withfrom.py
uv run --no-project --with requests --with biopython python sec7_catalytic_check.py
uv run --no-project --with requests --with biopython python sec7_catalytic_check.py --self-test
```

---

## 1. The Sec7 glutamic finger is absent from ARFGEF3

Sec7-domain ARF-GEFs activate ARF through one invariant glutamate — the "glutamic
finger" — which inserts into the ARF nucleotide pocket and destabilises bound GDP.
Its presence or absence is therefore the residue-level test of whether a Sec7
domain can do the chemistry its name implies.

**Panel construction.** The comparison set is *not* hand-picked: it is the 18
protein donors in the WITH/FROM field of ARFGEF3's own `GO:0005085` IBA row, plus
every reviewed ARFGEF3 orthologue, plus a known-dead comparator (below). 17 of the
18 donors have a UniProt SEC7 domain feature and enter the alignment.

**Column derivation.** The glutamic-finger column is *derived*, not asserted: it is
the alignment column at which the known-active donors are most Glu-conserved. A
hardcoded column would be a latent bug. The derived column is cross-checked against
an independent, alignment-free signal — the `[FY]-x-[LIVM]-P-G-E` Sec7 motif — and
the run aborts if the two disagree on any known-active donor.

**What the motif cross-check does and does not say.** It is *corroborating*, not
required, and the distinction matters when reading `sec7_glutamic_finger.tsv`:
**12 of the 17** active donors match the motif and place its Glu at exactly the
derived column; **5 match no motif at all** (IQSEC2, PSD, Psd3, SYT1, and the
*S. pombe* protein `YDYB_SCHPO`); and **0 disagree**. Those five are divergent Sec7
branches — BRAG/EFA6 in animals, SYT1 and the fission-yeast protein in fungi — that
retain the catalytic glutamate while departing from the FRLPGE consensus around it,
and every one of them still carries E at the derived column. So a `motif_hits: 0`
row is **silent, not contradictory**, and is not counter-evidence to the 17/17
result. The run aborts only on *disagreement*. These counts are emitted under
`motif_crosscheck` in `sec7_glutamic_finger.json` so the point does not rest on
this prose.

### Result

| class | n | residue at the derived column |
|---|---|---|
| known-active donors (own experimental GEF evidence) | 17 | **E in 17/17** |
| known-dead comparator (`ARFGEF1 E793A`) | 1 | A — scored *absent* |
| **human ARFGEF3 (Q5TH69)** | 1 | **N692** |
| mouse Arfgef3 (Q3UGY8) | 1 | **S688** |

Sequence context around the column:

```
ARFGEF1  (human BIG1,  active)   FRLPGEAQKID      E793
ARFGEF2  (human BIG2,  active)   FRLPGEAQKID      E738
CYTH1    (human,       active)   FRLPGEAQKID      E157
SEC7     (S. cerevisiae, active) FRLPGEGQKID      E923
GNOM     (A. thaliana,  active)  FRLPGESQKIQ      E658
--------------------------------------------------------
ARFGEF3  (human BIG3)            LLSLSNVEEVD      N692   <- no motif at all
Arfgef3  (mouse Big3)            LLALSSVEEVD      S688
```

ARFGEF3 matches the Sec7 catalytic motif **zero** times anywhere in its SEC7
domain (583–796). The loss is shared with the mouse orthologue, so it is a
clade-level loss, not a human-specific sequencing or annotation artefact.

### What this does and does not license

**Losing the catalytic residue is strong evidence against the activity. Retaining
it would not have been evidence for the activity.** Only the negative direction is
claimed here. A "retained site" result would have been reported as *untested*, not
as confirmation — as it was for ARFGEF3's nucleotide-independent regions, which
this analysis does not probe at all.

### Controls

`--self-test` exits 0 with 0 problems, exercising:

- **leave-one-out over all 17 active donors** — the derived column, and the
  subject's verdict, must survive removal of any single donor, so no one sequence
  is driving the result;
- **positive control** — a verified-active donor must score "Glu present";
- **known-dead control** — that same donor with its glutamic finger mutated to Ala
  must score "Glu absent". A detector that cannot report a negative proves nothing,
  so this control also appears in the *published* table above, not only in the test;
- **no-op guard** — the mutation target is asserted to be `E` *before* it is
  mutated, so a drifted target cannot silently turn the control into a tautology;
- **motif guard** — the subject must not match the Sec7 catalytic motif.

### Reproduction of the published result

Chen *et al.* 2014 (PMID:24997568) reached the same conclusion from a hand-built
alignment of eight Sec7 domains. Reproducing their panel is a **precondition** of
this script: it aborts unless BIG3 scores negative and all seven others score
positive. It does — **7/7 and BIG3 = N**.

**Defect found while reproducing it.** That paper's Methods gives GEP100 as
`Swiss-Prot:Q6ND90`. Q6ND90 is a *Rhodopseudomonas palustris* succinate
dehydrogenase cytochrome b556 subunit (TrEMBL, no Sec7 domain). Human
GEP100/BRAG2/IQSEC1 is **Q6DN90** — two transposed characters. The script records
what each published accession really resolves to and applies the correction
explicitly rather than silently substituting it.

---

## 2. The WITH/FROM donors: the IBA node is sound, the target is the exception

`withfrom_resolved.tsv` resolves all 32 distinct WITH/FROM tokens across the 7 GOA
rows that carry one. Zero unresolved. One (`WB:WBGene00007703`) resolved only by a
free-text fallback, because WormBase *gene* ids are absent from UniProt's
`xref:wormbase` index, which holds *protein* ids — reported rather than hidden.
Four MOD ids map to more than one UniProt entry and are reported as such, since a
`size=1` lookup turns an ambiguity into a confident wrong answer.

**ARFGEF3 itself does not appear in either WITH/FROM list.** There is no
self-referential donor, so no experimental grounding on the target anywhere in
either propagation chain.

### `GO:0005085` (guanyl-nucleotide exchange factor activity), 18 protein donors

| | count |
|---|---|
| donors carrying their own experimental evidence for the term | **18/18** |
| donors carrying their own **IDA** (direct exchange assay) | **15/18** |
| donors carrying InterPro `IPR000904` (Sec7) | 17/18 |

The three donors without IDA are *Drosophila* garz (IGI), *S. pombe* O13690 (IMP),
and *S. cerevisiae* MON2 (IGI/IPI/ISS).

**The node is soundly placed.** "This donor only carries the same family-level
inference" is false here in 18 of 18 cases. The defect is entirely on the target
side: ARFGEF3 is the one member of the set that has lost the catalytic residue.
That is `root_cause: PROPAGATION_BAD` with `failure_mode: PSEUDO_OR_SUBACTIVITY_LOSS`
— **not** `SOURCE_WEAK_OR_INFERRED`, which this analysis directly contradicts.

**A second, reciprocal observation worth reporting to PAINT.** MON2 is the only
donor UniProt annotates with **no SEC7 domain at all**, and it is also one of the
three without an IDA. It is a Sec7-*family* protein in the same structural class as
ARFGEF3 (both carry `IPR015403`, the Mon2/Sec7/BIG1-like HDS domain). So the same
node appears to be donating GEF activity to a second member that may not perform it.

### `GO:0016192` (vesicle-mediated transport), 18 protein donors

17/18 carry their own experimental evidence. The donors do **not** agree on a
specific process: between them they hold `GO:0006888`, `GO:0006890`, `GO:0006891`,
`GO:0006892`, `GO:0006893`, `GO:0006887`, `GO:0006895`, `GO:0042147`, `GO:0048193`,
`GO:0048205`, `GO:0016197`, `GO:0043001` and `GO:0032509` — anterograde ER-to-Golgi,
retrograde, intra-Golgi, endosome-to-Golgi and exocytic steps.

`GO:0016192` is therefore the genuine **LCA** of a heterogeneous donor set, not a
curator failing to be specific. `GRANULARITY_MISMATCH` requires the donors to
agree; they do not. No specificity upgrade is warranted on this row.

---

## 3. Two CC rows sit in a disjoint GO branch, because of a SubCell mapping

ARFGEF3's `GO:0030133` and `GO:0030658` rows come from `GO_REF:0000044`, the
UniProtKB-SubCell mapping, via `SL-0244` and `SL-0245`. `subcell_mapping_check.py`
resolves each one and asks how the mapped GO term relates to the term the primary
literature supports — querying QuickGO's `is_a`/`part_of` closure rather than
reading it off the labels, because "secretory vesicle" and "transport vesicle"
sound related and are not.

| SubCell | UniProt's name for it | maps to | literature supports | relation |
|---|---|---|---|---|
| `SL-0086` | Cytoplasm | `GO:0005737` cytoplasm | — | EXACT |
| `SL-0244` | **Secretory vesicle** | `GO:0030133` transport vesicle | `GO:0030141` secretory granule | **DISJOINT** |
| `SL-0245` | **Secretory vesicle membrane** | `GO:0030658` transport vesicle membrane | `GO:0030667` secretory granule membrane | **DISJOINT** |

`GO:0030141` and `GO:0030133` are sibling branches under `GO:0031410 cytoplasmic
vesicle`; neither is an ancestor of the other. So this is not a coarse-but-correct
parent — it is the wrong branch, and the two membrane terms inherit the same split.
GO's definitions make the reason plain: `GO:0030133` is "Any of the vesicles of the
**constitutive** secretory pathway", while insulin and glucagon granules are
**regulated** secretory granules.

**The mismatch starts inside UniProt.** `SL-0244`'s own definition is
regulated-pathway language — a vesicle that "mediates the vesicular transport of
cargo - e.g. hormones or neurotransmitters - from an organelle to specific sites at
the cell membrane, where it docks and fuses to release its content". That is
`GO:0030141`, not `GO:0030133`.

**Scale, stated precisely.** `SL-0244` is carried by **130,685** UniProtKB entries
and `SL-0245` by **90,419** (read from the `x-total-results` header, not from a page
length). That is the number of entries the mapping is *applied to*, and it is **not**
a claim that all of them are mis-annotated: `SL-0244` is a broad term and some
proteins in it may genuinely sit in the constitutive pathway. The claim is that the
mapping is wrong *for this protein*, and that because it is a single vocabulary-level
rule, it would be wrong at that scale wherever the regulated reading applies.

---

## Files

| file | contents |
|---|---|
| `uniprot.py` | cached UniProt/QuickGO REST helpers |
| `resolve_withfrom.py` | WITH/FROM resolution + donor-evidence query |
| `withfrom_resolved.tsv` | one row per distinct WITH/FROM token |
| `donor_evidence.tsv` | each IBA donor's own evidence for the term it donates |
| `supporting_entities.json` | `supporting_entities` lists built *from* the GOA field |
| `sec7_catalytic_check.py` | glutamic-finger analysis, controls and self-test |
| `sec7_glutamic_finger.tsv` | per-sequence scoring table |
| `sec7_glutamic_finger.json` | machine-readable summary |
| `subcell_mapping_check.py` | SubCell→GO branch check for the `GO_REF:0000044` rows |
| `subcell_mapping.tsv` / `.json` | per-SubCell-id resolution and branch relation |
