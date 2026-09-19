# ARHGEF16 bioinformatics — results

Four rerunnable analyses supporting `genes/human/ARHGEF16/ARHGEF16-ai-review.yaml`.
Each derives the repo root rather than hardcoding a worktree path, and each takes
`--self-test`, which breaks its input or its anchor on purpose and requires every
guard to fire, with negative controls that must stay silent.

```bash
uv run --with requests python gef_term_structure.py                       # -> gef_term_structure.json
uv run --with biopython --with requests python dh_exchange_surface.py     # -> dh_exchange_surface.json
uv run --with biopython --with requests python residue_mapping.py         # -> residue_mapping.json
uv run --with requests python retrieval_and_coverage.py                   # -> retrieval_and_coverage.json
```

All four query live services (the GO API, OLS4, QuickGO, UniProt, PDBe/SIFTS,
RCSB, PubMed, Reactome), so their JSON outputs are committed as the record of
what those services returned on the run that produced the numbers below.

Self-tests at time of writing: 6/6, 10/10, 6/6, 7/7.

---

## 1. `gef_term_structure.py` — GO has no term for the substrate, on three services

ARHGEF16 exchanges nucleotide on RhoG and, in cells, on nothing else. That
specificity is the only thing separating it from four ephexin siblings that are
all RhoA GEFs, and the review claims GO cannot express it. The claim is
load-bearing, so it is checked on three independent services.

| specific term | former label | merged into | GO API lists as alt id | OLS4 obsolete | QuickGO returns |
|---|---|---|---|---|---|
| `GO:0005089` | Rho guanyl-nucleotide exchange factor activity | `GO:0005085` | yes | yes | `GO:0005085` |
| `GO:0030676` | Rac guanyl-nucleotide exchange factor activity | `GO:0005085` | yes | yes | `GO:0005085` |
| `GO:0005088` | Ras guanyl-nucleotide exchange factor activity | `GO:0005085` | yes | yes | `GO:0005085` |
| `GO:0017048` | Rho GTPase binding | `GO:0031267` | yes | yes | `GO:0031267` |
| `GO:0032860` | activation of Rho GTPase activity | `GO:0090630` | yes | yes | `GO:0090630` |
| `GO:0032861` | activation of Rac GTPase activity | `GO:0090630` | yes | yes | `GO:0090630` |
| `GO:0005100` | Rho GTPase activator activity | `GO:0005096` | yes | yes | `GO:0005096` |

All four general parents are childless by `is_a`:

| parent | GO API descendants | OLS4 hierarchicalChildren | QuickGO children, any relation | QuickGO `is_a` children |
|---|---|---|---|---|
| `GO:0005085` | 0 | 0 | 2 | **0** |
| `GO:0031267` | 0 | 0 | 0 | 0 |
| `GO:0090630` | 0 | 0 | 0 | 0 |
| `GO:0005096` | 0 | 0 | 1 | **0** |

Two cautions the run reproduces rather than merely repeats:

- **QuickGO silently resolved all seven merges.** Asked for `GO:0017048`, it
  returns `GO:0031267 small GTPase binding` with `isObsolete: false` and a
  different id than the one requested. Read at face value, that says the Rho-
  specific binding term is alive. It is not.
- **QuickGO's non-`is_a` children look like children.** `GO:0005085` has two
  (`negatively_regulates`, `capable_of`) and `GO:0005096` one (`capable_of`);
  none is an `is_a` child, and counting them would falsely suggest the specific
  terms survive somewhere.

The script also pins the two definitions the review turns on, because their names
are one word apart and the GOA record confused them:

- `GO:0005096 GTPase activator activity` — "Binds to and increases the activity
  of a GTPase, an enzyme that catalyzes the **hydrolysis** of GTP." A GAP.
- `GO:0090630 activation of GTPase activity` — "Any process that initiates the
  activity of an inactive GTPase through the **replacement of GDP by GTP**." A
  GEF process, despite the name.

Drift in either definition aborts the run; the self-test confirms that by
breaking the expectation and requiring the abort, then restoring it and requiring
silence.

**Consequence for curation.** No new term is proposed. GO merged these
deliberately, and the correct response is to carry substrate identity in
`core_functions[].substrates` and as `RO:0002233 has_input`, and to record the
limit as an ONTOLOGY knowledge gap.

---

## 2. `dh_exchange_surface.py` — the DH surface is intact, and tells you nothing about the substrate

A DH domain has no catalytic residue in the chemical sense; it catalyses exchange
by distorting switch I and switch II. "The catalytic residue" is therefore
replaced by the **exchange surface**: DH residues within 4.0 Å of the GTPase in a
solved complex. Six complexes are used, spanning three substrates, with
chain-to-UniProt correspondence read from SIFTS rather than assumed.

| PDB | GEF | substrate | contacts inside DH | outside |
|---|---|---|---|---|
| 1KZ7 | Dbs/MCF2L (mouse) | Cdc42 | 23 | 6 |
| 1LB1 | Dbs/MCF2L (mouse) | RhoA | 22 | 10 |
| 1FOE | Tiam1 (mouse) | Rac1 | 26 | 5 |
| 1KI1 | ITSN1 | Cdc42 | 22 | 3 |
| 1X86 | LARG/ARHGEF12 | RhoA | 24 | 7 |
| 2NZ8 | Trio | Rac1 | 25 | 3 |

Fraction of contact positions retained (identical or BLOSUM62-positive):

| protein | DH? | 1KZ7 | 1LB1 | 1FOE | 1KI1 | 1X86 | 2NZ8 |
|---|---|---|---|---|---|---|---|
| **ARHGEF16/Ephexin-4** | yes | **0.70** | **0.64** | **0.50** | **0.68** | **0.54** | **0.52** |
| ARHGEF16 isoform 2 | yes | 0.70 | 0.64 | 0.46 | 0.64 | 0.50 | 0.48 |
| NGEF/Ephexin-1 | yes | 0.74 | 0.73 | 0.42 | 0.68 | 0.50 | 0.48 |
| ARHGEF19/Ephexin-2 | yes | 0.65 | 0.59 | 0.50 | 0.64 | 0.67 | 0.48 |
| ARHGEF5/Ephexin-3 | yes | 0.56 | 0.50 | 0.46 | 0.68 | 0.67 | 0.48 |
| ARHGEF15/Ephexin-5 | yes | 0.65 | 0.68 | 0.42 | 0.68 | 0.54 | 0.52 |
| ARHGEF26/SGEF | yes | 0.65 | 0.59 | 0.46 | 0.73 | 0.62 | 0.56 |
| TIAM1 | yes | 0.56 | 0.59 | **1.00** | 0.68 | 0.42 | 0.52 |
| ITSN1 | yes | 0.70 | 0.64 | 0.58 | **1.00** | 0.58 | 0.64 |
| LARG/ARHGEF12 | yes | 0.65 | 0.64 | 0.50 | 0.73 | **1.00** | 0.56 |
| MCF2L/DBS (human) | yes | **1.00** | **1.00** | 0.61 | 0.64 | 0.62 | 0.80 |
| DOCK4 (out-group) | **no** | 0.13 | 0.14 | 0.35 | 0.00 | 0.04 | 0.00 |

Each anchor's own GEF scores 1.00, which is the internal check that the SIFTS
offsets and the projection are right.

**Q1 — is the surface retained?** Yes. ARHGEF16 sits inside the range of bona
fide Dbl-family GEFs at every anchor, with no gap at any contact position that
distinguishes it from its siblings.

**Q2 — does the surface identify the substrate?** No, and this is the result
that matters. Read naively, the table names Cdc42: ARHGEF16 scores highest
against the two Cdc42-bound anchors (0.70, 0.68) and lowest against the
Rac1-bound ones (0.50, 0.52). The measured substrate is RhoG, which appears in
none of the six structures. The clean internal control says why the ranking is
uninformative: **1KZ7 and 1LB1 are the same GEF (Dbs) bound to two different
GTPases**, and their contact sets share a Jaccard of **0.731**, moving ARHGEF16's
score by only **0.06**. Holding the GEF constant and changing the GTPase barely
changes the surface, so the ranking tracks GEF-to-GEF sequence similarity, not
specificity. The sequence cannot supply what GO's merged terms also cannot
express.

**Q3 — reported in both directions, as the brief requires.**

- *Retention does not imply activity.* The counter-example is this protein.
  Full-length Ephexin4 is autoinhibited by two independent modes and is quiet
  until relieved by Elmo1 or a PDZ protein ([PMID:33597305], [PMID:28667327],
  [PMID:30445756]). A fully intact exchange surface is compatible with no
  measurable activity.
- *Absence would not imply inactivity.* The out-group DOCK4 catalyses exchange on
  Rac with no DH domain at all. A low score here means "not a Dbl-family GEF", not
  "not a GEF".
- *This analysis is confirmatory only.* ARHGEF16's exchange activity was measured
  directly on purified DH-PH protein ([PMID:20679435]); the sequence never had to
  carry the argument. The residue analysis would not have settled it either way.

**Controls, and one honest failure.** The negative control is each protein
against **its own composition-matched shuffle** (5 seeded replicates), not an
absolute cut-off — an absolute threshold would have to be tuned until the run
passed. Every positive beats its own shuffle by +0.26 to +0.48. The out-group is
controlled on **DH presence** (UniProt gives DOCK4 no DH domain), deliberately
not on its score, because at one of the six anchors (1FOE) DOCK4's local
alignment scored 0.35, +0.22 above its own shuffle — a chance match of a
1966-residue protein against a 195-residue domain. That is exactly why the
presence test exists, and it is reported rather than hidden.

**Isoform 2** (`Q5VV41-2`, lacking 1–288) scores 0.46–0.70, within 0.04 of the
canonical at every anchor: the `VSP_018149` deletion removes the N-terminal
regulatory region and only the first five residues of the DH domain, leaving the
exchange surface essentially complete. Whether that makes isoform 2
constitutively de-repressed is a hypothesis this analysis raises and does not
test; it is recorded as a suggested experiment, not as a finding.

---

## 3. `residue_mapping.py` — the published mutant is murine, and 295 is a serine in human

PMID:30445756 defines the autoinhibition interface with `Ephexin4E295A`, and its
methods state the construct: "All Ephexin4 mutants were generated by a polymerase
chain reaction (PCR)-based strategy from the murine Ephexin4 cDNA (NM_001112744)"
— mouse `Q3U5C8`, 713 aa. Human `Q5VV41` is 709 aa and **position 295 is a
serine**. Quoting "E295" into a human review would assert a residue the human
protein does not have.

| source | mouse | human | offset | conserved |
|---|---|---|---|---|
| E295A, autoinhibition interface | `Q3U5C8` E295 `EERKRQEAIF[E]ILTSEFSYLH` | `Q5VV41` **E291** `EERKRQEAMF[E]ILTSEFSYQH` | 4 | yes |
| P271A, companion mutant | `Q3U5C8` P271 `RPAQLTWSQL[P]EVLESGVLDT` | `Q5VV41` **P267** `RPAQVTWSQL[P]EVVELGILDQ` | 4 | yes |

Both mappings round-trip. The self-test asserts the *naive* reading fails —
human 295 is not a glutamate — so the script's conclusion is not vacuous. The
review's `residue_claim` is anchored on human `Q5VV41` E291 with the murine
construct position recorded as the comparator, never on an alignment column.

Human E291 lies 8 residues inside the UniProt DH domain (284–468) and inside the
region UniProt marks "Required for RHOG activation and mediates interaction with
EPHA2" (275–481).

---

## 4. `retrieval_and_coverage.py` — a clean gate, a 77%-miss, and an error in 81 taxa

### Retrieval

The deep-research provider reported `trust gates clear`,
`self_evaluation_pairwise: win`, `faith_pct: 100.0`. Every one of its six
citations is genuinely about this protein — the gate is doing its job, and its
job is precision.

PubMed, queried for the union of the protein's names
(`Ephexin4[Title/Abstract] OR ARHGEF16[Title/Abstract] OR "Ephexin-4"[Title/Abstract]`),
returns **26** records. affinage returned **6**, missing **20** — including
`PMID:20679435`, the one paper GOA leans on hardest, which alone accounts for 8
of the gene's 12 experimental GO rows.

Every mechanistic paper it missed has **Ephexin** in the title, not ARHGEF16:

| PMID | year | journal | title |
|---|---|---|---|
| 20679435 | 2010 | J Cell Biol | Ephexin4 and EphA2 mediate cell migration through a RhoG-dependent mechanism |
| 21621533 | 2011 | Exp Cell Res | Ephexin4 and EphA2 mediate resistance to anoikis through RhoG and phosphatidylinositol 3-kinase |
| 23772378 | 2013 | FEBS Open Bio | Ephexin4-mediated promotion of cell migration and anoikis resistance is regulated by serine 897 phosphorylation of EphA2 |
| 28667327 | 2017 | Sci Rep | Intermolecular steric inhibition of Ephexin4 is relieved by Elmo1 |
| 30445756 | 2018 | Cells | The Intermolecular Interaction of Ephexin4 Leads to Autoinhibition by Impeding Binding of RhoG |
| 30682817 | 2019 | Cells | Emerging Roles of Ephexins in Physiology and Disease |
| 33597305 | 2021 | PNAS | Double inhibition and activation mechanisms of Ephexin family RhoGEFs |
| 39675713 | 2025 | J Biol Chem | Phosphorylation of Ephexin4 at Ser-41 contributes to chromosome alignment via RhoG activation in cell division |

The gate certified that the six returned were real. It said nothing about the
twenty that were not, and a name-keyed retriever loses a protein whose literature
name and database symbol differ.

### GO coverage

QuickGO queried **by reference**, species-blind across `Q5VV41` and `Q3U5C8`: of
the 26 papers, exactly **two** produced any GO annotation.

| PMID | rows | terms |
|---|---|---|
| 20679435 | 8 | `GO:0005085/IDA`, `GO:0005515/IPI`, `GO:0030971/IPI`, `GO:0031267/IPI`, `GO:0060326/IMP`, `GO:0090630/IMP`, `GO:1903078/IMP` |
| 21139582 | 4 | `GO:0005096/IDA`, `GO:0030165/IPI`, `GO:0031267/IPI`, `GO:0032489/IDA` |
| the other 24 | 0 | — |

No result set was truncated, so these are zeros and not page artefacts; the
script reports a truncated page as *unknown* rather than as zero, and the
self-test exercises that branch. The 24 include incidental hits (a sheep-genome
survey, a melanoma toxicogenomics paper) alongside every one of the mechanistic
papers in the table above. The whole experimental GO record of this gene rests on
**two** papers, one of which the provider did not retrieve.

### Propagation

`GO:0005096 GTPase activator activity` is a GAP molecular function annotated by
IDA to a GEF, from a paper that measured nucleotide exchange. QuickGO, asked
which annotations carry `UniProtKB:Q5VV41` in `WITH/FROM`:

| term | rows | taxa | evidence |
|---|---|---|---|
| `GO:0005096` | **83** | **81** | IEA (`GO_REF:0000107`, Ensembl Compara), ISO (`GO_REF:0000119`) |
| `GO:0005085` | 221 | 100 | IBA, IEA, ISO, ISS |

The single human row has been projected to 83 orthologs in 81 species. Mouse
`Q3U5C8` carries it twice, by IEA and ISO, and has **no experimental GO
annotation of its own** — its entire record is a projection from human. The
`GO:0005085` figure is the healthy comparator: the same machinery, carrying the
correct term, reaches 221 rows across 100 taxa.

### Reactome

The two `GO:0005829 cytosol` TAS rows trace to reactions whose catalyst is a
`DefinedSet` of Dbl-family GEFs:

| reaction | asserts | protein participants | contains ARHGEF16 |
|---|---|---|---|
| `R-HSA-419166` GEFs activate RhoA,B,C | RhoA/B/C | 54 | yes |
| `R-HSA-205039` p75NTR indirectly activates RAC and Cdc42 via a GEF | Rac, Cdc42 | 52 | yes |

Membership is by DH domain, not by measured specificity — the same set contains
TIAM1/TIAM2 (Rac-only), FGD1–FGD4 and ITSN1 (Cdc42-only) and SOS1/SOS2/RASGRF2
(Ras). The outputs are the three GTPases `PMID:20679435` explicitly failed to
detect for this protein. Only the uncontroversial `cytosol` term reaches GOA, so
this is recorded as **provenance on the TAS rows**, not as a GO error; but it is
the same shape as the ARHGAP11B case, and a reader of the Reactome page is told
ARHGEF16 activates RhoA.
