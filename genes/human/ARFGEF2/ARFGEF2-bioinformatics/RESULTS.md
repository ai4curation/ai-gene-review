# ARFGEF2 (BIG2) — provenance audit results

All figures below are produced by `provenance_audit.py` and stored in
`provenance_audit.json`; `audit_claims.py` re-checks every number quoted here
against that file, so a stale claim fails rather than lingering.

The GOA set has **66 rows**: 26 IEA, 12 IDA, 10 IPI, 7 ISS, 4 IBA, 4 IMP, 2 TAS,
1 HDA — i.e. **27 experimental rows**, of which **10 are bare `GO:0005515`
protein binding**. By aspect: 34 cellular_component, 20 molecular_function,
12 biological_process.

## 1. Thirty percent of the GOA set is a double projection of one rat paper

**20 of the 66 rows**, covering **13 distinct GO terms**, carry rat Arfgef2
(`UniProtKB:Q7TSU1`, BIG2_RAT, Swiss-Prot, 1791 aa) in their WITH/FROM column.
Only **three** rat primary references sit behind all 20, and **17 of the 20 rows
rest solely on `PMID:15198677`** (Charych *et al.* 2004, *J Neurochem*).

The same rat annotations arrive twice, by two independent pipelines:

| pipeline | GO_REF | rows |
|---|---|---|
| Ensembl Compara orthology projection | `GO_REF:0000107` | 11 |
| UniProt curator-judged sequence similarity (ISS) | `GO_REF:0000024` | 7 |
| Combined automated annotation | `GO_REF:0000120` | 2 |

The eleven terms that rest **solely** on `PMID:15198677` are
`GO:0005879` axonemal microtubule, `GO:0006887` exocytosis, `GO:0031410`
cytoplasmic vesicle, `GO:0032279` asymmetric synapse, `GO:0032280` symmetric
synapse, `GO:0043197` dendritic spine, `GO:0050811` GABA receptor binding,
`GO:0098793` presynapse, `GO:0098794` postsynapse, `GO:0098978` glutamatergic
synapse and `GO:0098982` GABA-ergic synapse.

**The projection discriminator comes back NEGATIVE here, and that matters.**
`PMID:15198677` annotates only **2 entities** in the whole of GOA — rat Arfgef2
and its partner rat Gabrb3 — so this is genuine per-gene curation, not a
complex-membership projection distributed across subunits. The 23 annotations
are one gene's figures curated at figure granularity (SynGO contributes 12 rows
across four synaptic terms). The defect, such as it is, is **single-source
concentration plus double counting by two pipelines**, not phantom evidence.

## 2. `GO:0017022` myosin binding is a paralog attribution

`PMID:15644318` (Saeki *et al.* 2005) is titled *"**BIG1** is a binding partner
of myosin IXb…"*. Across GOA it annotates **7 entities with 18 annotations**:

- **6 of those annotations are on human ARFGEF1/BIG1** (`Q9Y6D6`) — `GO:0005085`,
  `GO:0005096`, `GO:0005515`, `GO:0017022`, `GO:0034260`.
- **0 are on human ARFGEF2** (`Q9Y6D5`).
- One is on **rat Arfgef2** (`Q7TSU1`): `GO:0017022` myosin binding, IPI with rat
  Myo9b — the only BIG2-family row the paper produced anywhere.

Human ARFGEF2's `GO:0017022` row exists **only** as the Ensembl Compara
projection of that single rat row. Human ARFGEF1 holds the same term directly by
IPI from the same paper.

**The term is nevertheless independently true of BIG2**, from a different paper:
`PMID:23918382` shows reciprocal co-immunoprecipitation of endogenous BIG2 and
non-muscle myosin heavy chain IIA in HeLa cells, and direct binding between
separately *in vitro*-synthesised BIG2 and NMHC IIA. So the finding is a broken
**evidence chain**, not a false term — and the same paper records a genuine
paralog difference: BIG1 binds MYPT1 and PP1cδ directly, BIG2 does not.

## 3. The reference-scope check on the remaining rows

| reference | entities | annotations | on ARFGEF2 | on ARFGEF1 | reading |
|---|---|---|---|---|---|
| `PMID:15198677` | 2 | 23 | 0 | 0 | rat-only, per-gene |
| `PMID:15644318` | 7 | 18 | 0 | 6 | paralog (see §2) |
| `PMID:19946888` | **1142** | 1142 | 1 | 0 | proteome-scale HDA sweep |
| `PMID:12571360` | 2 | 7 | 5 | 2 | targeted, per-gene |
| `PMID:16866877` | 3 | 4 | 1 | 1 | targeted, per-gene |
| `PMID:19332778` | 3 | 6 | 2 | 2 | targeted, per-gene |
| `PMID:22084092` | 4 | 14 | 1 | 7 | BIG1-centred; ARFGEF2 gets one IPI row |
| `PMID:33961781` | n/a | 9514 | 1 | 1 | BioPlex; too large to page |
| `PMID:35271311` | n/a | 2876 | 2 | 2 | OpenCell; too large to page |
| `PMID:40205054` | n/a | 3026 | 1 | 1 | cell maps; too large to page |

`PMID:19946888` (NK-cell membrane proteome) assigns `GO:0016020` membrane to
**1142 distinct entities** — the row is a proteome sweep, not a BIG2 result. The
three "n/a" rows exceed QuickGO's pagination ceiling; their entity counts are
reported as unavailable rather than guessed from a partial page, while their
per-gene counts stay exact because they come from targeted queries.

## 4. The real defect is coverage, not over-annotation

Taking the union of the UniProt entry's own `RX` PubMed list and the affinage
deep-research citation list — a derived set, not a hand-picked one — gives
**43 literature PMIDs**. Of those:

- **26 produce zero GO annotations anywhere in GOA**;
- **33 produce zero annotations on ARFGEF2**.

The 26 silent papers include the gene's founding disease paper
(`PMID:14647276`, *Nat Genet* 2004), the myosin-phosphatase scaffold paper
(`PMID:23918382`, *PNAS* 2013), integrin β1 recycling and cell migration
(`PMID:22908276`, *PNAS* 2012), Filamin A transport (`PMID:16320251`), the
AP-1/GGA dominant-negative papers (`PMID:11777925`, `PMID:12051703`), PP1γ
regulation (`PMID:17360629`), the RIIβ/TNFR1 AKAP paper (`PMID:18625701`),
BIG1/BIG2 redundancy in retrograde transport (`PMID:18417613`), the DCB/HUS
homodimer paper (`PMID:17640864`), β-catenin S675 (`PMID:27162341`) and
dendritic Golgi deployment (`PMID:29455446`).

For a disease gene the campaign's standing expectation is **over-annotation from
the disease phenotype**. ARFGEF2 inverts it: GOA carries **no** cerebral-cortex,
neuron-migration, neural-progenitor or heterotopia term at all, and the
pathology-derived over-annotation simply is not there. The predicted failure
mode was looked for and **not found**; what is there instead is a coverage gap.

## 5. The IBA node is heterogeneous, so the general GEF term is the LCA

`GO:0005085` IBA draws on 19 WITH/FROM tokens — the ancestral node
`PANTHER:PTN008950430` plus 18 proteins spanning the whole Sec7 superfamily:
*Arabidopsis* GNOM, *Drosophila* Sec71 and
garz, mouse Cytohesin-1 and PSD3, yeast GEA1/GEA2/SEC7/MON2/SYT1, *S. pombe*
`SPAC11E3.11c`, and human PSD, CYTH1, CYTH3, CYTH4, IQSEC2, ARFGEF1 — plus
ARFGEF2 itself (`UniProtKB:Q9Y6D5`), which is the expected marker that the target
carries its own experimental grounding for the term, not a circularity.

Because that clade mixes BIG-type, GBF-type, cytohesin-type and MON2-type GEFs
acting on different ARF/ARF-like substrates, `guanyl-nucleotide exchange factor
activity` **is** the least common ancestor of the donor set, not a curator
failing to be specific.

Independently: **`GO:0005086` ARF guanyl-nucleotide exchange factor activity no
longer exists as a distinct term.** QuickGO's `complete` record for `GO:0005085`
lists `GO:0005086`-`GO:0005090`, `GO:0008321`, `GO:0008433`, `GO:0016219`,
`GO:0016220`, `GO:0017034`, `GO:0017112`, `GO:0017132`, `GO:0019839` and
`GO:0030676` among its `secondaryIds` — every substrate-specific GEF term was
merged into it. So `GO:0005085` is already **maximal** for this protein and there
is no child to propose; the ARF1/ARF3 substrate preference has to be recorded
machine-readably (`core_functions[].substrates`, and a `has_input` extension on
the annotation) rather than as a more specific term.

## 6. Cilium census: is a ciliary term plausible anywhere near this protein?

The two `GO:0005879 axonemal microtubule` rows claim a cilium. Rather than assert
"no other ArfGEF has one", the claim was measured. The cohort is the four human
large ArfGEFs — **accessions derived by gene-name lookup, not written by hand**,
after a first pass hardcoded `Q9Y678` as GBF1 when it is in fact **COPG1** — plus
the nine proteins resolvable from this gene's own WITH/FROM column. Thirteen
accessions; each was queried for `GO:0005879` and the cilium/axoneme compartment
terms an ArfGEF would plausibly receive if it were ciliary.

| accession | gene | cilium terms held | note |
|---|---|---|---|
| `Q9Y6D6` | ARFGEF1 | — | large ArfGEF |
| `Q9Y6D5` | ARFGEF2 | `GO:0005879` | this projection only |
| `Q5TH69` | ARFGEF3 | — | large ArfGEF |
| `Q92538` | GBF1 | — | large ArfGEF |
| `Q7TSU1` | Arfgef2 (rat) | `GO:0005879` | the donor of the human rows |
| `Q9UPT5` | EXOC7 | `GO:0036064` | **ciliary basal body** |
| `A5PKW4` `O43739` `Q14432` `Q15438` `Q5JU85` `Q99417` `Q9UIA0` | PSD, CYTH3, PDE3A, CYTH1, IQSEC2, MYCBP, CYTH4 | — | |

Two results, and the second is the one that complicates the story:

1. Of the four human large ArfGEFs, **only ARFGEF2 holds a cilium-compartment
   term, and only by the projection under review**. The family gives no
   independent support to a ciliary localisation.
2. **EXOC7/Exo70 — the exocyst subunit BIG2 binds and co-localises with at the
   MTOC — carries `GO:0036064` ciliary basal body.** So a ciliary context near
   BIG2 is not absurd, and the honest verdict is "flag and measure", not "delete".

## 7. WITH/FROM resolution

All **45 distinct WITH/FROM tokens** across the 47 rows that carry one resolved;
**0 unresolved**. Five MOD ids returned more than one UniProt hit
(`RGD:1560793`, `RGD:631430`, `FB:FBgn0264560`, `MGI:MGI:1334257`,
`MGI:MGI:1918215`) — in every case all hits are the **same gene** (the Swiss-Prot
canonical entry plus TrEMBL isoform records), so identity is unambiguous; the
multiplicity is reported rather than collapsed. Two tokens resolve only to
**unreviewed (TrEMBL)** entries: `FB:FBgn0028538` (*Drosophila* Sec71) and
`FB:FBgn0264560` (*Drosophila* garz). Their *annotations* may still be
experimental, but their *protein names* are automatic, so neither name is used
here as evidence of what the family does.
