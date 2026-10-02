# ARHGEF16 bioinformatics — results

Six rerunnable analyses supporting `genes/human/ARHGEF16/ARHGEF16-ai-review.yaml`.
Each derives the repo root rather than hardcoding a worktree path, and each takes
`--self-test`, which breaks its input or its anchor on purpose and requires every
guard to fire, with negative controls that must stay silent.

```bash
uv run --with requests python gef_term_structure.py                       # -> gef_term_structure.json
uv run --with biopython --with requests python dh_exchange_surface.py     # -> dh_exchange_surface.json
uv run --with biopython --with requests python residue_mapping.py         # -> residue_mapping.json
uv run --with requests python retrieval_and_coverage.py                   # -> retrieval_and_coverage.json
uv run --with requests --with pyyaml python pdz_partner_check.py          # -> pdz_partner_check.json
uv run --with pyyaml python quote_claim_coherence.py                       # -> quote_claim_coherence.json
```

Five of the six query live services (the GO API, OLS4, QuickGO, UniProt, PDBe/SIFTS,
RCSB, PubMed, Reactome), so their JSON outputs are committed as the record of
what those services returned on the run that produced the numbers below.

Self-tests at time of writing: 6/6, 10/10, 6/6, 7/7, 9/9, 11/11. The last two were
mutation-tested by breaking them on purpose and running the suite; see the final
section.

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

---

## 5. `pdz_partner_check.py` — the 42-row retype, checked rather than asserted

The review converts 42 of the 57 `GO:0005515 protein binding` rows to
`GO:0030165 PDZ domain binding`, on the argument that they all report one binding
determinant — ARHGEF16's C-terminal motif — engaging the partner's PDZ domain.
That is a testable proposition about 42 UniProt records, so it is tested. The
script reads the **committed review** rather than a hardcoded list, so it cannot
drift away from the document it defends.

The motif is confirmed first, since the whole argument rests on it: `Q5VV41` is
709 aa, ends `...ETDV`, and UniProt annotates `MOTIF 707-709 "PDZ-binding motif"`
— the motif's last residue is the protein's last residue.

| | rows | accessions | distinct proteins | PDZ domains |
|---|---|---|---|---|
| PDZ side: 42 retyped + 1 GOA already types `GO:0030165` | 43 | 38 | 38 | **147** |
| not on the PDZ side (generic, plus the 7 `GO:0071889` retypes) | 15 | 11 | **10** | **0** |

**Every partner on the PDZ side carries at least one PDZ domain**, from SNTB2 and
MAST2 with one to MPDZ with thirteen and PATJ with ten. And **no partner outside
that set carries one**: HNRNPH1 has three RRMs, LASP1 a LIM and an SH3, BOLL an
RRM and a DAZ, TFG a PB1, MAGED1 a MAGE, ELMO2 an ELMO and a PH, and SFN, YWHAE,
YWHAZ and MAPK1IP1L have no annotated domain at all.

Two corrections a reviewer prompted, both kept visible because each was a way the
table could have misled:

- **Accessions are not proteins.** The eleven outside the PDZ side are **ten**
  distinct proteins: TFG appears twice, as the reviewed `Q92734` and the
  unreviewed `Q05BK6`. The script now reports both counts and names the
  duplicated symbol, so "11 partners" cannot be read as eleven proteins.
- **The panel skipped GOA's own verdict.** The `GO:0030165` row GOA already
  carries — TAX1BP3, from `PMID:21139582` — was in neither bucket, because the
  partition only looked at `GO:0005515` rows. That excluded the single partner the
  ontology has already adjudicated, which is the strongest available positive: if
  the classifier disagreed with GOA there, the classifier would be what is wrong.
  TAX1BP3 is now in the panel, carries one PDZ domain, and the self-test asserts
  its presence so it cannot silently drop out again.

The second direction is the load-bearing one. A lazy "retype everything from the
big PDZ screen" rule would pass the first check and fail the second, and so would
a review that retyped the PDZ partners but overlooked one sitting in a different
reference. The self-test injects a violation into each bucket in turn and requires
the corresponding guard to fire with its own message, then requires the untouched
review to pass silently.

The 42 rows come from three references — `PMID:36115835` (37), `PMID:32203420` (3)
and `PMID:30126976` (2) — and DLG1, SCRIB and SNTB2 each appear in more than one,
which is the point: the set reports one C-terminal determinant measured
repeatedly, not 42 independent findings.

---

## 6. `quote_claim_coherence.py` — does each quote support the claim it sits under?

This one exists because of a defect in this review, found in PR review and not by
any validator in the repository.

Two `GO:0005829 cytosol` rows cite Reactome reactions with different asserted
outputs — `R-HSA-205039` says Rac and Cdc42, `R-HSA-419166` says RhoA/B/C — and
both were generated from a single loop that attached **the same quote**, the RhoA
negative, to both. The RhoA row was right. The Rac/Cdc42 row was arguing about
Rac and Cdc42 while citing evidence about RhoA.

Nothing here catches that. The reference validator checks a `supporting_text`
against its **source publication** — is this a verbatim substring of PMID X — and
that quote was a perfectly verbatim substring of exactly the right paper. What is
never checked is the quote against the **claim it sits under**. A quote can be
impeccably sourced and still be evidence for a different proposition, and for a
gene whose entire story is which of five GTPases it acts on, that is the whole
review.

The guard collects, per annotation, the GTPases named by the **claim** (from
`RO:0002233 has_input` extensions and the "catalysed output is …" clause of
`reason`) and by the **union of its quotes**, and requires them to intersect.

| term | reference | claim | quotes | overlap |
|---|---|---|---|---|
| `GO:0005085` | PMID:20679435 | RHOG | CDC42, RAC1, RHOA, RHOG | RHOG |
| `GO:0005096` | PMID:21139582 | CDC42 | CDC42, RAC1, RHOG | CDC42 |
| `GO:0005829` | R-HSA-205039 | CDC42, RAC1 | CDC42, RAC1 | CDC42, RAC1 |
| `GO:0005829` | R-HSA-419166 | RHOA, RHOB, RHOC | RHOA | RHOA |
| `GO:0090630` | PMID:20679435 | RHOG | RAC1, RHOG | RHOG |

**Violations: 0.**

The union is deliberate, and it is where a stricter rule would go wrong. The
`GO:0005096` row legitimately pairs the Cdc42 exchange result with the Rac1/RhoG
specificity result, so demanding that *every* quote name the claimed GTPase would
fire on a correct row. Requiring that *some* quote engages the claim is the
strongest rule that does not produce false positives here.

The self-test's central check is a **regression**: it reintroduces the exact
original bug — puts the RhoA quote back under the Rac/Cdc42 row — and requires the
guard to flag it, then restores the correct quote and requires the same row to go
clean. The anchor is asserted to match exactly once, since a zero-match anchor
would "pass" by mutating nothing.

## Mutation testing: what makes these self-tests print FAIL

Self-tests that always pass are worthless, and a check whose construction
guarantees it agrees with its subject is worse than none. Both guards in sections
5 and 6 were therefore mutation-tested by breaking them on purpose and **running**
the suite, not by reasoning about what would happen. Every mutation anchor was
asserted to match exactly once, and every restore was verified by SHA-256 against
the original file.

`pdz_partner_check.py`, baseline **9/9**:

| mutation | result | checks that fired |
|---|---|---|
| classifier keys on the gene name, not the domain list | **5/9** | name-independence; SCRIB; reverse guard; committed review |
| classifier always says yes | **4/9** | name-independence; SCRIB; HNRNPH1; forward guard; committed review |
| drop the reverse guard | 8/9 | PDZ partner outside the retyped set |
| drop the forward guard | 8/9 | non-PDZ partner inside the retyped set |
| revert the partition to skip rows GOA already types `GO:0030165` | 8/9 | TAX1BP3 is inside the panel |

`quote_claim_coherence.py`, baseline **11/11**:

| mutation | result | checks that fired |
|---|---|---|
| never record a violation | 10/11 | the original bug is detected when reintroduced |
| claim extraction returns nothing | **8/11** | extractor finds rows; regression; restored run |
| `RhoG` matched as a substring, so `RhoGEF` counts | 10/11 | substring-lookalike matcher |
| drop `has_input` from the claim side | 10/11 | extractor finds rows |
| `file:` quote verifier stops comparing against the file | 10/11 | a fabricated `file:` quote is rejected |

One of these is the reason the section-5 self-test was rewritten. Its original
name-independence check asserted `has_pdz("Q9H5P4") is True` — and PDZD7 is *named*
for PDZ, so a name-keyed classifier satisfies it too. The check could not fail for
the reason it was named for. Replacing it with three hand-built records — a
protein named PDZD99 whose only domain is an RRM, one with a PDZ domain and an
unrelated name, and one whose PDZ appears under the wrong feature type — is what
makes the first row of the table above report a failure at all.

Two further notes on how these numbers were obtained, since a mutation table is
itself a claim. Each anchor was asserted to match **exactly once** before being
applied — a zero-match anchor "passes" by changing nothing, and a two-match anchor
silently mutates the wrong line. And each restore was verified by **SHA-256**
against the original file rather than by re-reading it, because a verification that
canonicalises whitespace or line endings cannot see the corruption it may have just
caused. Both runs ended with the file byte-identical to its starting state.

### The `file:` quote gap

`quote_claim_coherence.py` also verifies something else CI cannot: that every
`file:` `supporting_text` is a verbatim substring of the artifact it cites.
`conf/reference_validator_config.yaml` lists `file` under `skip_prefixes`, so those
quotes are checked against **nothing** — a quote from a repo artifact can be
paraphrased, stale, or simply invented and every validator in the repository stays
green. This review carries **47** of them, and all 47 verify. The self-test tampers
with one and requires the rejection, with the tamper anchor asserted to match
exactly once.
