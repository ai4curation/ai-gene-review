# AADACL2: is the esterase call founded, and which of its two localisations is?

Reproduce with `uv run --no-project --with requests --with biopython python audit_aadacl2_record.py`.
Every number below is fetched at run time from the UniProt, InterPro, QuickGO, EBI Proteins
and Human Protein Atlas REST APIs, plus this gene's own `AADACL2-goa.tsv`; if that TSV is
missing the script aborts with the regeneration command rather than dropping a section.
Machine-readable output is in `results.json`. This file is prose written from that file.

Run date: 2026-07-25.

## The record being audited

Seven GOA rows, no experimental evidence of any kind: 2 IBA and 5 IEA. Three rows assert an
activity at three different levels of generality (`GO:0003824 catalytic activity`,
`GO:0016787 hydrolase activity` twice, `GO:0052689 carboxylic ester hydrolase activity`),
and three rows assert a location — two of which cannot both be true (`GO:0016020 membrane`
twice, `GO:0005576 extracellular region`).

## 1. The catalytic machinery is intact, and it is not just the fold

*(script section Q1)*

AADACL2's own UniProt record annotates active sites at **189, 341 and 371**, which are
**Ser, Asp, His** — a serine-hydrolase catalytic triad — plus an oxyanion-hole motif at
**111-113 (HGG)**. A motif scan of the sequence finds one GDXG nucleophile elbow,
**GDSSG at 187-191**, placing Ser189 at the elbow apex, and the record carries the PROSITE
`PS01174` GDXG-lipase serine signature.

Those are UniProt's own assertions, several of them `ECO:0000250` (by similarity), so they
are not independent of the family. The reciprocal test is stronger: align AADACL2 to each
experimentally characterised protein cited in its own GOA `WITH/FROM` column, and ask what
AADACL2 carries at that protein's annotated active-site positions. A hit only counts if the
residue is identical **and** the mapped position is one of AADACL2's own annotated sites —
at 20% identity a global alignment will happily park a source Asp on some unrelated Asp.

| Source (GOA WITH/FROM) | % identity to AADACL2 | triad maps onto S189/D341/H371 |
|---|---|---|
| AADAC, *Homo sapiens* (P22760) | 51.6 | yes |
| Aadac, *Mus musculus* | 51.5 | yes |
| Aadac, *Rattus norvegicus* | 50.0 | yes |
| Nceh1, *Mus musculus* | 38.4 | yes |
| NlhH carboxylesterase, *M. tuberculosis* (P9WK87) | 35.7 | yes |
| LipI esterase, *M. tuberculosis* (P71668) | 32.2 | yes |
| CXE18 carboxylesterase, *A. thaliana* | 28.7 | yes |
| LipN carboxylesterase, *M. tuberculosis* (P95125) | 26.1 | yes |
| CXE12, ICME, Afmid, BNA7, Aes, HIDH | 19.7-26.5 | no |

**Eight of the fifteen sources with annotated active sites map all three residues onto
AADACL2's own annotated triad**, and they are essentially the closest ones: the seven
highest-identity sources all corroborate, and so does LipN at 26.1%. Every source that fails
lies at 26.5% identity or below, which is where this global alignment loses register in the
C-terminal half (for Afmid and Aes the source His has no aligned partner at all). The failures
are therefore alignment artefacts, not evidence of residue loss.

Broken down by position, the aggregate understates the nucleophile badly:

| AADACL2 position | residue | sources aligning here | with the identical residue |
|---|---|---|---|
| 189 | Ser | **15 / 15** | **14 / 15** |
| 341 | Asp | 8 / 15 | 8 / 15 |
| 371 | His | 8 / 15 | 8 / 15 |

**Every one of the fifteen sources places its own catalytic nucleophile on AADACL2 position
189**, and fourteen of them carry a serine there. The single exception is soybean HIDH, whose own
annotated nucleophile is a threonine — and HIDH is the one source in the set whose
physiologically important reaction is a dehydration rather than a hydrolysis, so the
substitution is informative rather than noise. (HIDH is bifunctional, not a pure lyase: it
carries EC 3.1.1.1 alongside EC 4.2.1.105 and a `GO:0106435 carboxylesterase activity` IDA, so
it does not threaten `GO:0016787` — it refutes only the *serine* mechanism term. See
`NODE_PTN009058710.md`, the shared node-level audit for AADACL2, AADACL3 and AADACL4.) The
8/15 triad-complete figure is driven entirely by the acid and the base, which sit in the
C-terminal half where register is lost below 26.5% identity. The nucleophile elbow, the most
conserved element of the fold, never loses register.

So this is not a case of a family name propagating onto a fold-only relic: the nucleophile,
the acid, the base and the oxyanion loop are all present and all in register with three
independently characterised bacterial carboxylesterases and with the 51.6%-identical human
paralog AADAC. `GO:0017171 serine hydrolase activity` — whose definition requires exactly a
serine nucleophile activated by an acid/base proton relay — is the term this evidence
licenses **for AADACL2 itself**. Nothing here identifies a substrate, and nothing here licenses
the term on the `PTN009058710` IBA row: that row's donors include a threonine-nucleophile
member, so the term has to be reached from the family node instead (section 5, and
`NODE_PTN009058710.md`).

## 2. `GO:0016020 membrane` is a family-majority feature that AADACL2 alone lacks

*(script section Q2, with the WITH/FROM resolution from Q3)*

`GO:0016020` is asserted twice: once by PANTHER (IBA, `PTN009058713`) and once by
InterPro/ARBA (IEA, `IPR017157` = *Arylacetamide deacetylase*, plus `ARBA00028763`).
Tabulating every **reviewed** UniProtKB entry carrying `IPR017157`:

| N-terminal feature | count |
|---|---|
| `TRANSMEM` | 12 |
| cleaved `SIGNAL` and no `TRANSMEM` | **1 — AADACL2 (human)** |
| neither | 1 — AADACL3 (human) |

Eleven of the twelve transmembrane segments are annotated explicitly as
"Helical; Signal-anchor for type II membrane protein"; the exception is mouse Aadacl3, which
carries three plain helices. Of the 14 reviewed members, AADACL2 is the only one whose
N-terminal hydrophobic segment UniProt calls a cleaved signal peptide. Its three `WITH/FROM` protein sources for the
membrane IBA are all type-II signal-anchored: human AADAC (`TRANSMEM 6-23`), mouse Aadac
(`6-26`) and mouse Nceh1 (`5-25`). So the membrane claim is a transfer of a feature that
AADACL2's own record says it does not have.

## 3. But the sequence does not actually settle it, and this is the interesting part

*(script sections Q5 and Q4)*

The tempting conclusion — "membrane is a paralog artefact, secreted is right" — does not
survive measurement. UniProt puts the cleavage site after residue 18, giving
**(-3,-1) = V-S-H**: histidine at -1, which is not a residue signal peptidase I accepts
(the -1 position is small and neutral, A/S/C/G/T, in the overwhelming majority of sites).
And the hydrophobic core itself is indistinguishable from the validated anchors. Peak mean
Kyte-Doolittle hydropathy over a 19-residue window in the N-terminal 45 residues, measured
identically for all five human family members:

| protein | UniProt N-terminal call | peak KD-19 window | peak mean KD |
|---|---|---|---|
| AADAC | `TRANSMEM 6-23`, type II signal anchor (experimentally validated) | 5-23 | 1.81 |
| **AADACL2** | **`SIGNAL 1-18`, cleaved** | **1-19** | **1.94** |
| NCEH1 | `TRANSMEM 5-25`, type II signal anchor | 5-23 | 2.08 |
| AADACL3 | none | 6-24 | 2.50 |
| AADACL4 | `TRANSMEM 5-25`, type II signal anchor | 6-24 | 2.80 |

AADACL2's segment (1.94) is **more** hydrophobic than AADAC's experimentally confirmed
signal anchor (1.81). Hydropathy cannot distinguish them, and the N-termini are homologous
across the whole segment (`MGLKALCLGLLCVLFVSHFYTPMPDNIEESWKIM` in AADACL2 against
`MGRKSLYLLIVGILIAYYIYTPLPDNVEEPWRMM` in AADAC, same position, same downstream
`TP.PDN.EE.W` motif). This is the classic signal-peptide / type-II-signal-anchor ambiguity,
and UniProt has resolved it one way for AADACL2 and the other way for its four paralogs.

The Human Protein Atlas, whose protein-class assignment is a majority vote over several
secretome and membrane predictors, does place AADACL2 — and only AADACL2 — in the secreted
class:

| protein | HPA protein class | RNA tissue distribution |
|---|---|---|
| AADAC | Enzymes; Metabolic; **Predicted intracellular** | detected in many (liver 884 nTPM) |
| NCEH1 | Enzymes; Predicted intracellular; **Predicted membrane** | detected in all |
| **AADACL2** | **Predicted secreted** | **detected in single (skin, 10.1 nTPM)** |
| AADACL3 | **Predicted membrane** | detected in some (skin 3.0, placenta 1.5) |
| AADACL4 | **Predicted membrane** | detected in single (choroid plexus 1.7) |

That discrimination is suggestive but it is not independent corroboration, for two reasons:
these predictors are SignalP-family tools of the same kind that produced UniProt's call, and
HPA's membrane classifier **fails to recognise AADAC**, an experimentally validated
single-pass type-II ER membrane protein, as a membrane protein at all. A classifier that
misses one of the family's two experimentally validated membrane proteins cannot be used to
argue that AADACL2 is a negative.

## 4. Mass spectrometry does not adjudicate it either

*(script section Q7)*

AADACL2 is `PE 1: Evidence at protein level`, so it is worth asking what the peptides
covered. Four observed peptides are recorded (PeptideAtlas, ProteomicsDB):

| residues | peptide | source |
|---|---|---|
| 124-130 | AFDFLNR | ProteomicsDB |
| 214-233 | MQVLLYPGLQITDSYLPSHR | PeptideAtlas |
| 294-316 | DYVYTEPILGGLSYSLPGLTDSR | PeptideAtlas |
| 345-353 | DDGLMYVTR | PeptideAtlas, ProteomicsDB |

The earliest observed residue is **124**. No peptide spans the annotated cleavage site and
none starts at the putative mature N-terminus (residue 19). Detection establishes that the
protein is made; it says nothing about whether the N-terminal helix is removed. The
localisation question is genuinely open, not merely under-curated.

## 5. The PANTHER node placement is inverted

*(script section Q6)*

Comparing the IBA annotations of all five human family members and the node each was
transferred from:

| term | AADAC | NCEH1 | AADACL2 | AADACL3 | AADACL4 |
|---|---|---|---|---|---|
| `GO:0017171` serine hydrolase activity | `PTN002745055` | `PTN002745068` | — | — | — |
| `GO:0005789` endoplasmic reticulum membrane | `PTN002745055` | — | — | — | — |
| `GO:0016787` hydrolase activity | — | — | `PTN009058710` | `PTN009058710` | `PTN009058710` |
| `GO:0016020` membrane | — | `PTN009058713` | `PTN009058713` | `PTN009058713` | `PTN009058713` |

The mechanistic molecular function sits only at the two **ortholog-specific** nodes
(`PTN002745055` for AADAC, `PTN002745068` for NCEH1), so AADACL2/3/4 inherit nothing from
it. What they do inherit at the shared family node `PTN009058713` is `GO:0016020 membrane`.
Meanwhile their only molecular function comes from the much deeper node `PTN009058710`,
whose 16 protein sources span three Arabidopsis CXE carboxylesterases and the Arabidopsis
isoprenylcysteine methylesterase ICME, mouse Afmid, yeast BNA7, *E. coli* Aes, three
*M. tuberculosis* esterases and soybean HIDH — a node so broad that bare `hydrolase
activity` is all it can safely carry (only 5 of those 16 sources have any transmembrane
segment, which is why the membrane call could not have come from here).

The placement is the wrong way round with respect to what actually transfers. The catalytic
triad is demonstrably conserved across the whole family including AADACL2 (Q1), so
`GO:0017171` is safe at `PTN009058713`; the type-II signal anchor is not conserved in
AADACL2, so `GO:0016020` is not. Moving the activity down to the family node and dropping
the localisation from it would fix three human genes at once.

Both halves of that claim were then tested donor by donor in `NODE_PTN009058710.md`, the
shared node-level audit for AADACL2, AADACL3 and AADACL4. It confirms that `GO:0017171` is
true of every donor PAINT cites at `PTN009058713` and IDA-supported by all three of them,
and that at
`PTN009058710` no candidate term below `GO:0016787` survives every donor — so the deep-node
row cannot be upgraded, only recognised as redundant with the `IPR017157`-derived
`GO:0052689` that all three genes already carry.
