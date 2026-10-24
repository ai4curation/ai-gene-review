# AP3S2 (P59780) — bioinformatics support for the annotation review

Three questions came out of the GOA record for human AP-3 complex subunit
sigma-2 (sigma-3B) that can be settled from sequence and database evidence
rather than from assertion. Each script fetches live from the UniProt, GO and
QuickGO REST APIs (responses cached under `cache/`, which is disposable) and
from the committed PANTHER PAINT slice
`interpro/panther/PTHR11753/PTHR11753-paint.tsv`. Nothing below is hardcoded;
delete `cache/` and re-run to regenerate every number.

```
uv run python sigma_dileucine_pocket.py   # -> sigma_dileucine_pocket.tsv
uv run python resolve_withfrom.py         # -> withfrom_resolved.tsv
uv run python arba_funfam_specificity.py  # -> arba_funfam_specificity.tsv
uv run python check_goa_reconciliation.py # GOA tsv <-> review YAML
```

---

## 1. Does sigma-3B retain the dileucine-signal pocket? (`sigma_dileucine_pocket.py`)

**Question.** Acidic dileucine sorting signals `[DE]XXXL[LI]` bind no single AP
subunit; they bind a composite site across the large-subunit/sigma-subunit
interface — gamma1-sigma1 in AP-1, alpha-sigma2 in AP-2, delta-sigma3 in AP-3
(PMID:14691137, PMID:21097499). Mattera et al. (PMID:21097499) located the AP-3
site by substitution: *"the loss of signal binding by the σ2 V88D or L103S
substitutions and the homologous σ1A V88D and I103S and σ3A V94D and L109S
substitutions"*. Every solved AP-3 structure to date is built on **sigma-3A**:
the 2024 cryo-EM core (PMID:39705307) and the 2026 AP3:ARF1 coat
(PMID:42139345), whose methods state the construct as *"AP3S1(1–193) (H.
sapiens)"*. Whether the pocket also exists on sigma-3B is therefore a paralogy
question, and a falsifiable one.

**Method.** Canonical sequences for the four human sigma subunits used in
Mattera's substitution series, plus the mouse Ap3s2 ortholog named as donor by
the human ISS/IEA rows, are fetched live from UniProt. Each anchor residue is
first asserted against its own record, so a UniProt renumbering fails loudly
instead of silently reporting the wrong residue. AP3S2 is then globally aligned
to each comparator (Biopython `PairwiseAligner`, BLOSUM62, gap open −11 /
extend −1) and the AP3S2 position aligned to each anchor is read out.

**Result.**

| comparator | anchor | AP3S2 | verdict | identity to AP3S2 |
|---|---|---|---|---|
| AP3S1 / sigma-3A (Q92572, SV1) | V94 | V94 | RETAINED | 83.9 % |
| AP3S1 / sigma-3A (Q92572, SV1) | L109 | L109 | RETAINED | 83.9 % |
| AP2S1 / sigma-2 (P53680, SV2) | V88 | V94 | RETAINED | 39.4 % |
| AP2S1 / sigma-2 (P53680, SV2) | L103 | L109 | RETAINED | 39.4 % |
| AP1S1 / sigma-1A (P61966, SV1) | V88 | V94 | RETAINED | 37.3 % |
| AP1S1 / sigma-1A (P61966, SV1) | I103 | L109 | SUBSTITUTED | 37.3 % |
| Ap3s2 / sigma-3B (mouse, Q8BSZ2, SV1) | V94 | V94 | RETAINED | 100.0 % |
| Ap3s2 / sigma-3B (mouse, Q8BSZ2, SV1) | L109 | L109 | RETAINED | 100.0 % |

Three things fall out.

- **AP3S2 retains both pocket residues at the same native positions as AP3S1**,
  Val94 and Leu109. The two paralogs differ at 31 of 193 positions overall
  (83.9 % identity), but only 4 of those 31 fall in the 46-residue window
  spanning the two anchors plus 15 residues either side — V113M, N118Y, A121Q
  and M123V, all downstream of Leu109 and none at an anchor. The structural work
  done on sigma-3A therefore transfers to sigma-3B at this site, and no
  loss-of-pocket argument is available against AP3S2.
- The alignment **independently reproduces the equivalence Mattera asserted**
  across complexes: sigma-2 V88/L103 and sigma-1A V88/I103 both map onto AP3S2
  V94/L109. The one `SUBSTITUTED` call is Ile→Leu at the second position, which
  is the difference Mattera's own text reports between sigma-1A and the
  sigma-2/sigma-3 pair, not a divergence of AP3S2.
- **Human and mouse AP3S2 are byte-for-byte identical proteins** — both 193 aa,
  100 % identity, no gaps. This is directly relevant to grading the `ISS` rows
  whose donor is `UniProtKB:Q8BSZ2`: the donor is not merely the true ortholog,
  it is the same sequence.

**Limits.** This is a sequence argument about a binding site, not a measurement
of binding. It shows the pocket is present and unchanged; it does not show that
a delta-sigma3B hemicomplex binds a given cargo with the same affinity as
delta-sigma3A. The direct evidence for that is experimental and is discussed in
the notes (PMID:14691137 tested delta-sigma3B explicitly).

---

## 2. Who are the IBA donors and the PAINT seeds? (`resolve_withfrom.py`)

**Question.** The single IBA row (`GO:0016192 vesicle-mediated transport`)
carries eleven gene-product donors plus the ancestral node
`PANTHER:PTN000204281`. Reviewing it means knowing what those donors are, and
which complex each one belongs to.

**Method.** Every token in the GOA `WITH/FROM` column and every seed in the
committed PAINT slice is resolved through the UniProt cross-reference search
(`query=xref:<db>-<id>`, `size=5`, so multi-hits are reported rather than
silently collapsed), preferring the reviewed entry. WormBase gene ids are not in
UniProt's xref index; those fall back to the GO API `bioentity` record and then
to a gene-name lookup, rather than being written off as unresolvable.

**Result.** 30 tokens; all resolved (one via the GO API fallback). The slice
holds two IBD assertions on the same node:

| node | term | aspect | seeds | slice date |
|---|---|---|---|---|
| PTN000204281 | GO:0043231 intracellular membrane-bounded organelle | C | 13 | 20260528 |
| PTN000204281 | GO:0016192 vesicle-mediated transport | P | 10 | 20260828 |

The ten seeds of the `GO:0016192` IBD resolve to:

| seed | protein | complex |
|---|---|---|
| CGD:CAL0000182525 | Q59QC5 APS3_CANAL (*C. albicans* APS3) | **AP-3** |
| SGD:S000003561 | P47064 AP3S_YEAST (*S. cerevisiae* APS3) | **AP-3** |
| SGD:S000004160 | P35181 AP1S1_YEAST (APS1) | AP-1 |
| PomBase:SPAP27G11.06c | Q9P7N2 AP1S1_SCHPO (vas2/aps1) | AP-1 |
| MGI:MGI:1098244 | P61967 AP1S1_MOUSE | AP-1 |
| MGI:MGI:1889383 | Q9DB50 AP1S2_MOUSE | AP-1 |
| FB:FBgn0039132 | *D. melanogaster* AP-1sigma | AP-1 |
| RGD:620188 | P62744 AP2S1_RAT | AP-2 |
| UniProtKB:P53680 | AP2S1_HUMAN | AP-2 |
| WB:WBGene00000157 | Q19123, *C. elegans* aps-2 (F02E8.3) | AP-2 |

The IBA row carries one further donor not in this seed list,
`FB:FBgn0043012` (*D. melanogaster* AP-2sigma, Q9VDC3); that gene *is* a seed of
the same node's `GO:0043231` IBD, whose slice line is three months older. The
discrepancy is a release-timing artefact between the GOA row and the current
PAINT slice, not a donor the tree does not contain.

**Interpretation for the review.** Two of the ten seeds are genuine AP-3 sigma
orthologs, so the node is not an AP-1/AP-2-only inference being stretched to
AP-3. The remaining eight are AP-1 and AP-2 sigma subunits, which act on
different itineraries (TGN/endosome, plasma membrane) from AP-3's
(endosome/lysosome). Donors that disagree in destination are exactly the case in
which the *parent* term is the correct least common ancestor: `GO:0016192
vesicle-mediated transport` is general because the family is, not because the
curator under-called it.

---

## 3. Is the ARBA rule behind the GO:0030123 IEA AP-3-specific? (`arba_funfam_specificity.py`)

**Question.** The `GO:0030123 AP-3 adaptor complex / IEA / GO_REF:0000120` row
cites `ARBA:ARBA00033921|InterPro:IPR027155`. FunFam-based rules are named for
whole families, so a rule of that shape can assign an AP-3-specific complex term
to every sigma subunit in the fold. Whether this one does is empirical.

**Method.** The rule is fetched live from `https://rest.uniprot.org/arba/` and
its condition set printed; the FunFam cross-reference is then read off every
reviewed human AP-complex sigma subunit (the complete set, not a sample).

**Result.** `ARBA00033921` (created 2022-04-29, modified 2025-03-21) fires on
`FunFam id = 3.30.450.60:FF:000001` **and** `taxon = Primates`, and asserts
`GO:0030123`.

| symbol | accession | complex | FunFam | matches rule |
|---|---|---|---|---|
| AP1S1 | P61966 | AP-1 | 3.30.450.60:FF:000005 | no |
| AP1S2 | P56377 | AP-1 | 3.30.450.60:FF:000009 | no |
| AP1S3 | Q96PC3 | AP-1 | 3.30.450.60:FF:000005 | no |
| AP2S1 | P53680 | AP-2 | 3.30.450.60:FF:000004 | no |
| AP3S1 | Q92572 | AP-3 | 3.30.450.60:FF:000001 | **yes** |
| AP3S2 | P59780 | AP-3 | 3.30.450.60:FF:000001 | **yes** |
| AP4S1 | Q9Y587 | AP-4 | 3.30.450.60:FF:000010 | no |
| AP5S1 | Q9NUS5 | AP-5 | (none) | no |

The panel is the complete set of reviewed human AP-complex sigma subunits. The
first seven are also the complete human membership of PANTHER family PTHR11753,
checked against `interpro/panther/PTHR11753/PTHR11753-entries.csv`; AP5S1 is the
one that sits outside the family, and is included so the test is not scoped to
the family the rule is about.

**The suspicion is not borne out.** Within the human sigma panel the FunFam
partitions cleanly by complex, and exactly the two AP-3 sigma subunits match.
Zero non-AP-3 subunits would be called AP-3 by this rule. The IEA row is
therefore well-founded on both halves of its `WITH/FROM`, and no
`PROPAGATION_BAD` call is warranted against it.

**Limits.** The panel is human. UniProt's search index does not expose FunFam as
a queryable cross-reference, so the rule's precision across all primates was not
measured; what is measured is that the discriminating signature exists and
separates AP-3 from AP-1, AP-2 and AP-4 in the species being annotated.

---

## 4. GOA ↔ review reconciliation (`check_goa_reconciliation.py`)

Mechanical check, run before every commit: every row of `AP3S2-goa.tsv` maps to
exactly one `existing_annotations` entry on (GO id, evidence code, reference,
qualifier, normalised `WITH/FROM`); every non-`NEW` entry maps back to a GOA
row; `supporting_entities` is the `|`-split `WITH/FROM` verbatim; and every
`IBA`/`ISS`/`ISO`/`IEA`/`IC` row that carries a `WITH/FROM` carries a
`propagation_review`. 25 GOA rows; 16 of them require a `propagation_review`.
Exit status is non-zero if any check fails.
