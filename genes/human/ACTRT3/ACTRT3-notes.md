# ACTRT3 (Q9BYD9, ARP-T3 / ARPM1) — review notes

Human actin-related protein T3. 372 aa, Swiss-Prot, `PE 1: Evidence at protein level`,
`Pharos: Tdark`. PANTHER family `PTHR11937` (ACTIN); CDD signature `cd13397
ASKHA_NBD_actin_Arp-T1-3`, i.e. a family-specific signature for the ARP-T1/2/3 clade rather
than a bare actin fold.

## 0. Name check, done first because the aliases cross

`ACTRT3` = `ARPM1` = hArpM1 ("Actin-related protein M1"), and `ACTRT2` = `ARPM2` = hArpM2.
Verified against UniProt: `Q9BYD9 ACTT3_HUMAN ACTRT3 ARPM1` and `Q8TDY3 ACTT2_HUMAN ACTRT2
ARPM2`. The two cDNAs were reported together in one paper, so any ARPM-keyed literature
search returns both genes and the M1/M2 suffixes must be resolved before a claim is
attributed [PMID:11750065 "We identified two cDNAs coding for the novel human actin-related
proteins (Arps) hArpM1 and hArpM2."].

Consequence: PMID:11750065 is **shared literature with the parallel ACTRT2 review**, and its
tissue statement applies to both genes jointly.

## 1. The GOA record: 10 rows, and where each one actually comes from

| # | Term | Ev | Qual | Source |
|---|---|---|---|---|
| 1 | GO:0015629 actin cytoskeleton | IBA | is_active_in | `PANTHER:PTN002631484` + 24 protein tokens |
| 2 | GO:0005200 structural constituent of cytoskeleton | IBA | enables | `PANTHER:PTN000940351` + 10 protein tokens |
| 3 | GO:0005634 nucleus | IEA | located_in | `UniProtKB-SubCell:SL-0191` |
| 4 | GO:0005737 cytoplasm | IEA | located_in | `UniProtKB-SubCell:SL-0086` |
| 5 | GO:0005856 cytoskeleton | IEA | located_in | `UniProtKB-SubCell:SL-0090` |
| 6 | GO:0007010 cytoskeleton organization | IEA | involved_in | inter-ontology from `GO:0005200` |
| 7 | GO:0005515 protein binding | IPI | enables | `UniProtKB:Q9H2J4` (PDCL3), PMID:33961781 |
| 8 | GO:0001673 male germ cell nucleus | IEA | located_in | `UniProtKB:Q8BXF8` (mouse Actrt3) |
| 9 | GO:0033011 perinuclear theca | IEA | located_in | `UniProtKB:Q8BXF8` |
| 10 | GO:0033011 perinuclear theca | ISS | located_in | `UniProtKB:Q8BXF8` |

Rows 3–5 all trace to one UniProt statement, and every clause of it is by similarity with no
source entry named: `file:human/ACTRT3/ACTRT3-uniprot.txt` line 91–92, `CC   -!- SUBCELLULAR
LOCATION: Cytoplasm, cytoskeleton {ECO:0000250}. Cytoplasm`. So they are one inference
re-coded three times, not three lines of support. Same provenance defect ACTL8's review
flagged on its own `GO:0005856` row.

## 2. WITH/FROM resolution (`ACTRT3-bioinformatics/resolve_withfrom.py`, `withfrom.tsv`)

Built from the GOA WITH/FROM field by construction with an assertion on the token count, per
the campaign rule. Row 1 carries **25** tokens (24 protein donors + one PANTHER node) and row 2
carries **11** (10 protein donors + one node); all 24 and all 10 resolved, nothing was left
unresolved and nothing dismissed. (First pass reported 20 of 24 on row 1 because
`xref:wormbase-` does not index WormBase *gene* ids; a free-text fallback was added to the
resolver rather than the four tokens being written off. An `xref:` miss is not an absent
protein.)

- **Row 1, `PTN002631484`.** 23 conventional actins (human ACTB/ACTG1/ACTA1/ACTA2/ACTC1,
  chicken, pig, rat, mouse, *C. elegans* act-2/3/4/5, *Dictyostelium* act1/3/10/22, yeast ACT1,
  *S. pombe* act1, *Candida* ACT1, *Plasmodium* ACT1) **plus `FB:FBgn0011743` = P45891 Arp53D**,
  the divergent *Drosophila* actin that does polymerise. **24/24 carry their own
  experimental (IDA/IMP) annotation for `GO:0015629` or a descendant.** So the "sources only
  carry family-level inference" framing is factually false here, as it usually is for IBA.
  But the donor set is *homogeneous*: every donor is a filament-forming actin. The
  heterogeneity is on the **recipient** side, not the donor side, which is the opposite of
  the AADACL4 situation where a broad term was the correct LCA of disagreeing donors.
- **Row 2, `PTN000940351`.** 10 tokens: conventional actins (ACTB, mouse/rat Actg1, yeast
  ACT1, *Dictyostelium* act1/act10) **plus Arp2 (P61160), Arp3 (P61158), yeast ARP1
  (P38696) and yeast ARP10 (Q04549)**. All 10 carry their own experimental evidence for
  `GO:0005200`. This donor set *is* heterogeneous — three different polymer systems
  (F-actin, the Arp2/3 branch nucleator, the dynactin Arp1 filament) — so `GO:0005200` is a
  defensible LCA **for the node**. Note yeast ARP10 is the Arp11/ACTR10 orthologue, which is
  exactly why the merged ACTR10 review could ACCEPT this same row: ACTR10 has an
  ortholog-strength donor in the set. **ACTRT3 does not — no ARP-T is among the 10 seeds.**
- **Rows 8–10, `UniProtKB:Q8BXF8`.** A genuine 1:1 orthologue, not a paralogue:
  `Q8BXF8 = ACTT3_MOUSE`, gene `Actrt3`, 369 aa, Swiss-Prot, **79.4% globally identical** to
  human ACTRT3 against **47.0%** local identity to β-actin. It carries `GO:0001673` by
  **IDA** (PMID:18692047) and `GO:0033011` by **IDA** (PMID:35793634). Ortholog transfer of
  a directly observed location — the strongest row shape in this record.
- Row 7's partner `Q9H2J4` resolves to `PDCL3_HUMAN`, phosducin-like protein 3 / PhLP2A,
  239 aa, reviewed, canonical length — no TrEMBL/ORFeome substitution.

## 3. Residues, in both directions (`ACTRT3-bioinformatics/analyze_actrt3.py`, `RESULTS.md`)

Contact sets are computed from coordinates, not recalled; the machinery is deliberately
identical to ACTL8's script so the tallies are comparable with that merged review. Contacts
are heavy-atom within 4.0 Å; conservation is read off a global alignment of the structure
chain's own observed sequence, so a residue is never assigned by position number. Tallies are
unchanged under BLOSUM45/-14/-2 as well as BLOSUM62/-11/-1.

Three contact sets, of which the middle one is new to this gene:

| Set | Structure | n contacts | ACTRT3 (id / cons / non-cons / gap) |
|---|---|---|---|
| Nucleotide site | 2BTF chain A, ATP + cation | 19 | **15 / 2 / 2 / 0** |
| Profilin surface | 2BTF chain A vs profilin chain P | 21 | **14 / 2 / 5 / 0** |
| Filament protomer interface | 6DJO, chain C | 38 | **13 / 5 / 19 / 1** |

The profilin surface is included because it is the one interaction ACTRT3 has directed
experimental reason to retain — 2BTF *is* the profilin:β-actin complex, so the same
coordinates that give the nucleotide site give the profilin-binding face.

**Direction 1 — the nucleotide site is essentially intact, so "fold without function" is
refuted for nucleotide binding.** 17 of 19 contacts are chemically compatible. Within the
eight divergent human actin-like/ARP-T proteins, all scored in the same run, ACTRT3 is
**joint best**: ACTRT3 17, ACTRT2 17, ACTRT1 16, ACTL9 15, ACTL7A 14, ACTL8 14, ACTL7B 13,
ACTL10 10. Controls: β-actin 19/19, Arp53D 19/19, Arp1 (ACTR1A) 18/19, Arp11 (ACTR10) 11/19.
The whole P1 phosphate loop is conserved (G13-S14-G15-M16 → G13-S14-G15-M16), K18, the
Mg-coordinating Q137 → Q136, G156/G158, G182, K213/E214, the adenine-contacting G301-G302 and
K336. The two non-conservative losses are D157 → A156 and M305 → S302. This is a measured
confirmation of a 25-year-old claim made from sequence alone [PMID:11750065 "Both of them
show remarkable similarity to conventional actin, and the ATP-binding motif and
nuclear-export signals of actin are highly conserved."].

**Direction 2 — the polymerisation surface is not intact, so a filament claim is not
supported.** 18 of 38 protomer-interface contacts are compatible. Every protein in the panel
that is known to assemble into a two-stranded actin-like filament scores far higher:
ACTA1/ACTC1 38/38, ACTB/ACTG1 38/38, **Arp53D 33/38** (divergent *and* polymerises — the
discriminating positive control), **ACTR1A/ACTR1B 28/38** (the weakest true polymeriser
available, in the dynactin filament). ACTRT3's 18 sits 10 below the weakest polymeriser.

**But this does not earn a REMOVE, and the reason is a caveat I am importing from ACTL8's
own review rather than inventing.** In the same panel, **Arp3 scores 8/38 and Arp2 22/38**,
yet Arp2 and Arp3 form the first protomer pair of a daughter filament at an Arp2/3 branch.
A low score therefore bounds *canonical protomer incorporation into a conventional
two-stranded filament*; it does not show that a protein cannot occupy any position in an
actin-containing structure. ACTRT3 also sits **above** ACTL8's 11/38 — the score that, with
3 additional deletions, earned ACTL8's REMOVE. So the honest verdict on ACTRT3's cytoskeletal
rows is *not supported as a filament constituent*, not *refuted as actin-associated*.

**The clade-level pattern is the interpretable result.** The ARP-T trio retains the
nucleotide core (17/16/17 of 19) while having lost most of the protomer interface (18/21/20
of 38). That is the signature of a monomeric nucleotide-binding actin-fold protein acting as
a scaffold, not of a filament former — which is precisely what the perinuclear-theca
literature describes.

## 4. Headline curation finding: PAINT has already rejected `GO:0005200` at eight sibling nodes

`GO:0005200` is asserted **once** in PTHR11937, at `PTN000940351` (IBD, 2025-08-05, 10 seeds),
and then explicitly **negated (IRD)** at eight descendant nodes. Read straight out of
`interpro/panther/PTHR11937/PTHR11937-paint.tsv`, with the human genes at each node resolved
via QuickGO:

| Node | Date of rejection | Human genes | What that clade actually is |
|---|---|---|---|
| `PTN000233752` | 2025-08-05 | ACTR5 | INO80 chromatin remodeller |
| `PTN000233887` | 2025-08-05 | ACTR6 | SWR1/histone-variant complex |
| `PTN000234048` | 2025-08-05 | ACTR8 | INO80 |
| `PTN001732543` | 2025-08-05 | ACTL6A, ACTL6B | SWI/SNF, NuA4 |
| `PTN008986528` | 2025-08-05 | **ACTL7A, ACTL7B** | testis actin-like; **`GO:0005198` asserted here instead** |
| `PTN000233596` | 2026-04-16 | ACTR2 | Arp2 |
| `PTN000233796` | 2026-04-16 | ACTR3, ACTR3B, ACTR3C | Arp3 |
| `PTN007551901` | 2026-04-16 | ACTR1A, ACTR1B | dynactin Arp1 |

So the term has been withdrawn from **13 human genes across 8 clades**, and the sweep is
ongoing (a second batch landed 2026-04-16). Verified by exact-usage QuickGO query, the human
genes still holding `GO:0005200` itself by IBA from `PTN000940351` are: ACTA1, ACTA2, ACTC1,
ACTG2 (conventional actins, correct), ACTR10 (correct — its own orthologue yeast ARP10 is in
the seed set), and **ACTL9, ACTL10, ACTRT1, ACTRT2, ACTRT3** — the un-adjudicated divergent
five.

The single most useful datum is what PAINT did at `PTN008986528`, the nearest neighbour
clade: it did not merely reject `GO:0005200`, it **substituted the general parent
`GO:0005198 structural molecule activity`** on the same day. That is an in-resource
precedent for exactly the edit this review proposes, and it is why ACTL7A and ACTL7B carry
`GO:0005198` IBA today while ACTRT3 carries `GO:0005200`. Following it also makes this review
*consistent* with the merged ACTL7A and ACTL7B reviews, both of which removed their
`GO:0005200` rows.

Methodological note worth keeping: "`PANTHER:PTN…` is a tree node, not a protein" is true and
invites you to stop looking. The node cannot be resolved to a protein, but it **can** be
looked up in the family's PAINT table, where it may carry an explicit negation of the term
under discussion. (The same lesson is recorded in `ACTL7A-notes.md`.)

**Independent cross-check.** While this review was in progress, two more PTHR11937 genes merged
to `main` — ACTR5 (#2291) and ACTR8 (#2290) — and ACTR8's reviewer read the same cached PAINT
file from the opposite end of the family and reported the identical count: *"PTHR11937 carries 9
GO:0005200 rows in total: 8 IRD negatives at divergent nodes and 1 IBD positive at the actin
node."* Two agents converging on the same nine rows from different starting genes is stronger
evidence than either alone, so this review now cites
`file:interpro/panther/PTHR11937/PTHR11937-paint.tsv` directly rather than only through its own
derived report — the same citation ACTR8 uses.

Incidental, and it resolved itself mid-review: those two merges introduced a **third** duplicate
curie into `cache/go/terms.csv` (`GO:0031011 Ino80 complex`, at lines 3456 and 9070) alongside
the long-standing `GO:0001675` and `GO:0009566`, and one `just validate` run in this worktree
then appended a *further* copy of that same row — identical content, identical timestamp to the
line-9070 row, inserted near EOF with no matching deletion. I restored the file from
`origin/main` and could not reproduce the append in two further runs, so I did not claim a
systematic leak from one unreproduced observation. It was then fixed upstream independently, by
PR #2293 ("the ACTR5/ACTR8 terms.csv collision"), so `main` is back to the two long-standing
duplicates.

The transferable point is procedural. `git diff origin/main -- cache/go/terms.csv` is **not** a
safe pre-commit check while other agents are merging, because `origin/main` moves under it: at
one point that command reported a clean zero-line diff for a working file that differed from my
own `HEAD`, purely because upstream had changed in between. Compare against `HEAD` as well, and
re-fetch immediately before the final check. This branch's committed diff to that file is zero
lines, verified against `HEAD` after a final fast-forward.

### The counter-argument, stated because it is not weak

Read by its definition rather than its label — "The action of a molecule that contributes to
the structural integrity of a cytoskeletal structure" — `GO:0005200` arguably *does* fit
ACTRT3, because GO classifies `GO:0033011 perinuclear theca` under `GO:0005856 cytoskeleton`
(verified: `GO:0033011` ancestors include `GO:0005856` and `GO:0005737` but **not**
`GO:0015629`), and the mouse knockout shows ACTRT3 contributes to PT structure
[PMID:41668650 "We conclude that lack of ACTRT3 affects acrosome biogenesis, PT structure and
actin remodeling."]. I did not take that route, for two reasons. First, it would license the
row on grounds entirely unrelated to the evidence chain the row actually carries, leaving a
reader to conclude that ACTRT3 is a cytoskeletal *filament* constituent by inference from
actin — the reading the interface measurement excludes. Second, ACTL7A is a perinuclear-theca
protein with `GO:0033011` by IDA and its merged review nonetheless **removed** its
`GO:0005200`; accepting the term here on the PT argument would create exactly the kind of
cross-review inconsistency this campaign treats as a defect. The PT route is therefore filed
as a `suggested_questions` item for the whole PT/ARP-T set at once, not acted on unilaterally.

## 5. Second finding: the informative molecular function is missing from the human record

GOA gives ACTRT3 one molecular-function row of experimental grade, and it is bare
`GO:0005515 protein binding` to PDCL3. Meanwhile the interaction the gene is actually known
for is absent.

The mouse orthologue carries `GO:0005515 protein binding` by IPI from PMID:18692047 — four
annotation rows spread over only two entities, i.e. one co-immunoprecipitation logged once by
UniProt and once by IntAct and recorded reciprocally on Actrt3 and Pfn3, not two experiments (see
§14b) — with WITH/FROM `UniProtKB:Q9DAD6`, which resolves to `PROF3_MOUSE`, gene `Pfn3`, 137 aa,
Swiss-Prot — profilin-3 [PMID:18692047 "By co-immunoprecipitation analysis, profilin III was
identified as ArpM1-interacting protein."]. UniProt carries the human side by similarity:
`file:human/ACTRT3/ACTRT3-uniprot.txt` line 88, `CC   -!- SUBUNIT: Interacts with PFN3.
{ECO:0000250}.`

`GO:0005522 profilin binding` exists, is not obsolete, is a molecular-function term, and is
already used with `GO_REF:0000024` ISS for DBN1, EVL and PCLO — so an ISS row for ACTRT3 from
`UniProtKB:Q8BXF8` is ordinary practice, not a novelty. Three independent strands support it:

1. the co-immunoprecipitation itself [PMID:18692047];
2. genetic dependency in the reciprocal knockout [PMID:34869336 "Western blot showed that
   ARPM1 could not be detected in the nuclear fraction of Pfn3-deficient testes and sperm,
   while cytoplasmic ARPM1 protein levels in testes are slightly reduced in Pfn3-deficient
   mice"], which is a stability relationship, not just co-purification; and
3. a directed structural prediction that this review computed *before* looking for
   corroboration: the profilin-binding face of β-actin is retained in ACTRT3 at 16/21
   compatible contacts, against 10/21 for ACTL8 and 8/21 for ACTR10, and 20-21/21 for
   β-actin, Arp53D and Arp1.

So the same measurement that argues *against* the filament rows argues *for* a specific,
informative MF the record is missing. Both directions came out of one structure.

Reciprocal recommendation: the mouse `GO:0005515` rows should themselves be upgraded to
`GO:0005522`, since their WITH/FROM already names a profilin.

## 6. The expression claim: correcting a merged sibling review

ACTL8's merged review states, in three places, that ACTRT3 is "ubiquitously expressed", and
uses it to argue that the divergent-actin clade "is not uniformly testis-restricted". The
statement is a faithful reading of UniProt — `file:human/ACTRT3/ACTRT3-uniprot.txt` line 93,
`CC   -!- TISSUE SPECIFICITY: Ubiquitously expressed.` with `{ECO:0000269|PubMed:11750065}` —
but the underlying observation is narrower than the phrase suggests, and three other sources
in the same UniProt entry disagree with it:

- The cited evidence is a 2001 **mRNA** survey with an explicit abundance caveat
  [PMID:11750065 "Their mRNAs are expressed in all tested human tissues, but in smaller
  amounts than that of actin."].
- The same UniProt entry's own cross-references say testis: `DR   HPA; ENSG00000184378;
  Tissue enriched (testis).` and `DR   Bgee; ENSG00000184378; Bgee`… `Expressed in sperm and
  107 other cell types or tissues.` HPA's API gives one tissue above its specificity
  threshold, testis at 54.1 nTPM.
- At the **protein** level in mouse the orthologue is testis-exclusive [PMID:18692047 "we
  demonstrate here that mouse ArpM1, which closely resembles the conventional actin, is
  expressed exclusively in the testis, particularly in haploid germ cells."].

Reconciliation: broad low-level transcript, strongly testis-enriched, with protein-level
detection confined to male germ cells in the organism where it has been looked for. So
"ubiquitously expressed" is not false about 2001 mRNA data but is misleading as a
characterisation of the gene, and it does not support the inference ACTL8 drew from it. This
is filed as a UniProt correction to report and noted in `suggested_questions`. It does **not**
change any ACTL8 annotation action — the point was made in prose, not used to license a term.

## 7. `GO:0005515` / PDCL3: one experiment, and a mechanism that explains it away

IntAct returns exactly **2** records for Q9BYD9 and they are the **same experiment**: PDCL3
paired with ACTRT3 by `anti tag coip`, MI score 0.5, both from PMID:33961781 (BioPlex 3.0),
one of the two being a **spoke expansion** of a bait-prey pull-down. So UniProt's `NbExp=2`
is one AP-MS experiment counted twice, the ACRV1 pattern.

What makes this more than "unreplicated screen hit" is that the partner explains itself.
PDCL3 / PhLP2A is a CCT/TRiC co-chaperone: UniProt records "Inhibits the folding activity of
the chaperonin-containing T-complex (CCT) which leads to inhibition of cytoskeletal actin
folding (PubMed:17429077)". Actin is an obligate CCT client, so co-purification of an
over-expressed, tagged actin-fold polypeptide with a CCT co-chaperone in HEK293T/HCT116 — cell
types where ACTRT3 protein is not natively present — is the single most expected artefact of
the assay, not a physiological partnership. It is nevertheless mildly informative in the
other direction: it indicates the ACTRT3 polypeptide is recognised as a foldable actin-fold
client.

Contrast with the merged ACTR1B review, which KEEP_AS_NON_CORE'd its row from the *same*
publication: there the partner set was coherent with a known complex (DCTN1–DCTN6, CAPZ,
ACTR10, ACTR1A). Here there is one partner and no complex. Hence
MARK_AS_OVER_ANNOTATED rather than KEEP_AS_NON_CORE — the difference is the partner set, not
the publication.

## 8. A paper affinage missed, found through the orthologue

The mouse `GO:0033011` IDA cites **PMID:35793634**, "The perinuclear theca protein Calicin
helps shape the sperm head and maintain the nuclear structure in mice" — a 2022 Cell Reports
paper titled for **CCIN**, a different gene, and absent from the affinage record entirely.
Its abstract states "We show that Calicin interacts with itself and many other PT
components", and a curator working from its full text made the Actrt3 PT localisation call.
The cached entry is `full_text_available: false` and the abstract does not name Actrt3, so I
cannot quote it for ACTRT3 and do not attempt to; per CLAUDE.md the experimental call stands
and the row is ACCEPTed. Recorded here because it is the campaign's "a paper titled for
another gene can hold your gene's answer" pattern, and because it means the perinuclear-theca
localisation was established in 2022, four years before the dedicated knockout paper.

## 9. Reading the whole paragraph: an F-actin result that cuts the other way

The affinage narrative and the 2026 knockout paper both support an actin-remodelling role
[PMID:41668650 "Expression of Actrt3 caused changes in HEK239T cell shape and F-actin
filament distribution, suggesting a role in cytoskeletal shaping."]. But the one paper with
cached full text contains a section head and a result pointing the other way: in *Pfn3*-null
mice, where ARPM1 is absent from the nuclear fraction, [PMID:34869336 "Interestingly, in the
mid-piece of the sperm flagellum, actin organization seemed not affected."]

These are not strictly contradictory — different compartment (flagellar mid-piece vs sperm
head), different perturbation (indirect ARPM1 depletion vs direct knockout), and ARPM1 is
still detectable in *Pfn3*-null sperm cytoplasm ("a moderate signal of ARPM1 can still be
detected"). But together they mean the actin-remodelling link is not robust enough to license
a specificity upgrade. That is why `GO:0007010` is kept at the general level rather than
refined to `GO:0030036 actin cytoskeleton organization`, which was the route the merged
ACTL7A review took on an identical row shape. Recording the disconfirming result explicitly,
because no mechanical check would have caught its omission.

## 10. Ontology facts verified rather than assumed

All via QuickGO `/ontology/go/terms/<id>/complete` and `/ancestors`:

- `GO:0033011` ancestors include `GO:0005737` and `GO:0005856` but **not** `GO:0005634` or
  `GO:0015629`. So rows 4 and 5 are redundant true ancestors of a row the gene already holds,
  while row 1 is an independent claim.
- `GO:0001673` ancestors include `GO:0005634`. So row 3 is a redundant true ancestor of row 8.
- `GO:0005200`, `GO:0005198`, `GO:0005522`, `GO:0015629`, `GO:0007010`, `GO:0030036`,
  `GO:0001675`, `GO:0007286`, `GO:0033011`, `GO:0001673` are all live, non-obsolete;
  `GO:0001673` carries `secondaryIds: ['GO:0043081']`.
- `GO:0033011`'s own definition contains the caution that "recent studies indicate that the
  bulk of its constituent proteins are not traditional cytoskeletal proteins but rather a
  variety of cytosolic proteins" — relevant background to the `GO:0005200` question above.

## 11. Retraction / validity checks

PubMed publication types checked for every PMID relied on: 11750065, 18692047, 34869336,
35793634, 41668650, 33961781. None is retracted and none carries an erratum; PMID:41668650
was checked by `efetch` (Development 153(3):dev205283, 2026-02-01, `PublicationTypeList` =
Journal Article only, no `CommentsCorrections`) because `esummary` returned no record for it.

The affinage record is marked `correctness: LOW_QUALITY` in the review, on two counts and not
on any incorrect assertion: it presents one study as two dated findings (see below), and it
omits PMID:35793634 entirely — the reference behind the perinuclear-theca IDA on the mouse
orthologue, and therefore behind two of this gene's ten GOA rows. That paper is titled for
CCIN, so a symbol-keyed retrieval would not surface it; the omission was found by asking what
evidence the WITH/FROM donor itself carries, not by reading the provider record.

The affinage record's `gates_passed: True`, but it carries one
`PMID:bio_10.1101_2025.03.27.645694` — a **bioRxiv DOI in a PMID-shaped field**, not a PubMed
record. Comparing its content with PMID:41668650 shows it is the **preprint of the same
study** (same PT localisation, same cap-phase acrosome defect, same GM130/TGN46 result, same
ACTRT1/ACTRT2/ACTL7A/ZPBP co-IPs). So the affinage table's two "independent" 2025 and 2026
findings are one study, and no claim in this review rests on the preprint id.

## 12. Actions taken, and the sibling row each follows

| Row | Action | Precedent followed |
|---|---|---|
| 1 `GO:0015629` IBA | KEEP_AS_NON_CORE | ACTL8's **identical** row (same node, same 25 tokens) |
| 2 `GO:0005200` IBA | MODIFY → `GO:0005198` | PAINT's own edit at `PTN008986528`; ACTL7A/ACTL7B |
| 3 `GO:0005634` IEA | KEEP_AS_NON_CORE | redundant-ancestor pattern (ACTL7A, ACTR1A, ACTR1B) |
| 4 `GO:0005737` IEA | KEEP_AS_NON_CORE | same |
| 5 `GO:0005856` IEA | KEEP_AS_NON_CORE | ACTL7A's "descendant the review keeps" test |
| 6 `GO:0007010` IEA | KEEP_AS_NON_CORE | ACTR10 |
| 7 `GO:0005515` IPI | MARK_AS_OVER_ANNOTATED | ACTL8, ACTR10 (not ACTR1B — see §7) |
| 8 `GO:0001673` IEA | ACCEPT | ACTL7A's ortholog-IDA transfer |
| 9 `GO:0033011` IEA | ACCEPT | ACTL7A |
| 10 `GO:0033011` ISS | ACCEPT | ACTL7A |
| new `GO:0005522` | NEW | §5 |
| new `GO:0001675` | NEW | §13 |

Not one row is REMOVEd. The interface measurement is strong enough to withhold a filament
claim and not strong enough to refute actin association, and that asymmetry is the finding.

## 13. The biological process gap

ACTRT3's only BP row is `GO:0007010 cytoskeleton organization`, inherited from a molecular
function. The knockout phenotype is entirely absent from the record:
[PMID:41668650 "We generated Actrt3-/- male mice and showed that they are subfertile, with
defects of the acrosome first observed during cap phase."] and "Actrt3 deficiency causes
reduced protein levels of the trans-Golgi network markers TGN46 and GOPC and mislocalization
of the cis-Golgi protein GM130."

`GO:0001675 acrosome assembly` is defined as "The formation of the acrosome from the
spermatid Golgi", which matches the phenotype's mechanism as well as its outcome. Added as a
NEW row with ISS from `UniProtKB:Q8BXF8`, since the experiment is in mouse. `GO:0007286
spermatid development` is the correct parent but adds nothing over the specific term and is
not proposed separately.

## 14. Negative results from checks that were run

Recorded so a later reviewer knows they were done rather than skipped.

- **IntAct method audit**: 2 records, 1 experiment, 1 partner, spoke expansion, MI 0.5. No
  orthogonal assay anywhere. (§7)
- **Partner accession audit**: `Q9H2J4` is reviewed, canonical length 239 aa. No TrEMBL or
  ORFeome substitution of the kind found on ACRV1.
- **Donor-precision audit (the ACRV1 "IBA less precise than its donor" check)**: the mouse
  donor holds `GO:0001673` and `GO:0033011`, and the human rows land on **the same two
  terms**, not above them. So **no downward MODIFY is warranted** on rows 8–10.
- **Node-placement audit (the ACTL8 defect)**: ACTRT3 is **not** under either narrow
  β/γ-actin node. Recomputed live: ACTRT3 has 2 IBA rows from `PTN000940351` and
  `PTN002631484`, exactly the median of 2 across the seven other divergent relatives, against
  ACTL8's 11. ACTL8's census is confirmed independently, including the number it assigned
  ACTRT3.
- **Self-referential IBA check**: neither IBA row's WITH/FROM cites ACTRT3 itself, so
  `NO_FAILURE_CORE` does not apply to either.
- **Unresolved WITH/FROM**: none, after the resolver fix described in §2. The four
  `WB:WBGene…` tokens resolve to *C. elegans* act-2, act-3, act-4 and act-5; they are
  conventional actins and do not change the row-1 conclusion.
- **Numeric self-check**: the first draft of these notes said row 1 had 24 tokens / 23 protein
  donors. It has 25 / 24. The discrepancy surfaced only when the generator that builds
  `source_entities` asserted its emitted count against the GOA field, which is the whole reason
  that list is generated rather than typed.

## 14b. Reference scope: ask what a reference covers before treating a row as independent support

`ACTRT3-bioinformatics/reference_scope.py` queries QuickGO **by reference** rather than by gene
for every PMID this review cites. The technique comes from the merged ACTR8 review, where a
reference returning 16 entities × 5 terms exposed a complex-to-subunit projection that a per-gene
view could not see. Results here, and what each one changed:

| PMID | total | complete? | reading |
|---|---|---|---|
| 35793634 | 35 | yes (35 of 35 rows) | 12 PT proteins carry `GO:0033011` IDA; the phenotype row does **not** spread |
| 18692047 | 5 | yes (5 of 5) | one co-IP, logged by two databases **and** reciprocally on both partners |
| 33961781 | 9514 | **no** — 200 rows sampled, 1 unaccounted | 9508 `GO:0005515`; plus a 5-row ComplexPortal projection tail |
| 41668650, 34869336, 11750065 | 0 | — | not curated by GOA at all |

Two of these changed the review.

1. **`GO:0033011` is not a projection, and the discriminator is which row *fails* to spread.**
   PMID:35793634 carries `GO:0033011` by IDA for twelve mouse theca proteins (Actl9, Actrt1,
   Actrt2, Actrt3, Capza3, Capzb, Ccin, Cylc1, Fabp9, Gsto2, H2bl1, Wbp2nl), all `assignedBy:
   UniProt`. A ComplexPortal-style projection would spread the *phenotype* too — and this one does
   not: the paper's only functional row, `GO:0007286` IMP, is confined to **Ccin alone**, the gene
   actually knocked out. So these are twelve per-protein localisation calls from one
   immunolocalisation study. The ACCEPT stands, now on a stated basis rather than an assumed one.
   Side benefit: it places ACTRT1, ACTRT2 and ACTL9 in the theca by IDA *independently* of the 2026
   co-IPs, which is what turns "the ARP-T clade is a theca clade" from an inference from one paper
   into a curated fact — and it strengthens the `suggested_questions` item addressed to that set.
2. **A doubled-count phrasing was mis-statable and has been corrected.** The draft said mouse
   Actrt3 carries protein binding by IPI two separate times from that reference, which reads as two
   experiments. The reference covers only 2 entities in total, so the rows are one
   co-immunoprecipitation logged once by UniProt and once by IntAct, recorded reciprocally on
   Actrt3 and Pfn3 — one experiment recorded four ways. Exactly the ACRV1 `NbExp=3` shape, in my
   own review. The `GO:0005522`
   proposal never depended on a replicate count, so the term survives; the sentence supporting it
   did not.

### The round-2 correction: this checker mixed a total with a 2 per cent sample

The reviewer of the follow-up PR caught the sharper defect, and it is the same class the script
was written to catch. The first version fetched **one `limit=200` page** and reported the
per-term, per-code and per-database breakdowns *from that page*, while taking `total_annotations`
from the API's own hit count. For five of the six references that is harmless, because the page
covers everything. For **PMID:33961781** it is not: 9514 annotations, 200 examined, so every
page-derived field was a 2 per cent sample — and the review then stated two of them as totals.
Both were false:

- *"it is the only term that publication contributes"* — false. `GO:0005515` exact is **9508**,
  not 9514, and the aspect totals are MF 9509 / CC 5 / BP 0.
- *"all assigned by IntAct"* — false. **IntAct 9509 + ComplexPortal 5.**

And the five hidden rows are the interesting part: `GO:0005813 centrosome`, IPI, assigned by
**ComplexPortal**, projected onto the ted-tubulin complex and its four subunits. So the very
reference this review cites to illustrate what is *not* a projection contains a projection tail —
which a 200-row sample of a 9,514-row screen could not show. None of it touches ACTRT3, and no
action changed, but the prose was asserting coverage it did not have.

Every count is now its own **filtered count query** (`limit=1`, read `numberOfHits`); page-derived
fields are renamed `*_seen`; `truncated`, `unaccounted_annotations` and
`term_list_provably_complete` are emitted; and **ComplexPortal is probed unconditionally**, because
a projected tail can sit entirely outside a sample. Three further things came out of doing it
properly:

1. **The verdict function then inverted.** With bare `GO:0005515` excluded from the functional set,
   the newly-visible ComplexPortal rows presented as "multi-entity localisation with no functional
   claim" and were reported as *NOT* a projection — exactly backwards for rows a projecting database
   assigned. Fixed by naming projecting-database rows as such before the heuristic runs at all.
2. **Per-code totals do not partition the total.** QuickGO's `evidenceCode` filter is not
   exact-only: on PMID:35793634 the per-code counts sum to 57 against a total of 35. They are kept
   for orientation and used for no claim.
3. **Completeness is the precondition for the projection test**, and stating it
   makes the two theca ACCEPTs rest on a checkable property rather than on the absence of a
   surprise. PMID:35793634 is complete, 35 of 35, so the twelve-versus-one comparison is sound.

### The round-3 correction: an annotation count is not an entity count

The reviewer then caught a subtler version of the same confusion, one level down, and the file
proved it against itself. `count(reference, goId, goUsage=exact)` returns `numberOfHits` — which
counts **annotation rows** and never collapses per gene product — but the field holding it was
called `true_entities_per_term`. The disproof is in this very audit: PMID:18692047's `GO:0005515`
value read **4** while only **2** entities are involved, Q8BXF8 and Q9DAD6, each logged once by
UniProt and once by IntAct. The double-logging this whole section is about was mislabelled as an
entity count inside the JSON that explains it.

Why the biology survived anyway, and it is worth being explicit that this was luck plus an
asymmetry rather than care:

- **`GO:0007286` = 1 is rigorous either way**, because entities ≤ annotations, so one annotation
  implies exactly one entity. "Confined to Ccin alone" follows regardless of which quantity the
  field held. That is the half of the projection argument that carries the weight.
- **The 12 needed distinct entities**, and it happens to be 12 either way — no theca protein is
  double-logged in that reference. But the audit guard was confirming the sentence against a field
  that could have read 12 while the truth was 11, so the guard was right by luck of the data.

Fixed: the field is now `true_annotations_per_term`; a separate `entities_per_term` is computed
from distinct `geneProductId` values and emitted **only when `rows_complete`**, since
a distinct count taken from a sampled page is a lower bound wearing a total's clothes;
`projection_test_basis` records which of the two the verdict used; and the audit reaches entity
counts through an accessor that raises a named error rather than a bare `KeyError` when the count
is unavailable. `unaccounted_annotations` deliberately stays on the annotation counts — it is
`total - sum(annotations)` and is sound precisely because those are rows.

### The round-4 correction: the gate tested the wrong completeness

One more level down, and the sharpest of the four. `entities_per_term` was gated on
`unaccounted_annotations == 0` — which proves every annotation's **term** was queried. But the
entity counts are computed by collecting distinct `geneProductId` values **from the returned
rows**, so the property they actually need is that every **row** was seen: `not truncated`, which
was already computed two dozen lines earlier and is strictly stronger. The docstring gave the
right reason ("a distinct count taken from a sampled page is a lower bound") while the condition
underneath it enforced something else.

**It missed by one annotation on this very dataset.** PMID:33961781 has 9508 + 5 = 9513 against a
total of 9514, so the single stray row — a `GO:0005515` descendant the sampled page never showed —
is the *only* reason its term list stayed open. Without it, `unaccounted` would have been 0 while
the page still held 200 of 9514 rows, and the block would have emitted
`entities_per_term[GO:0005515] ≈ 119` with `entities_per_term_available: true`,
`projection_test_basis: entities_per_term` and `projection_test_reliable: true`. That is the
round-1 sampling defect returning under a label asserting it had been fixed — and the audit guard,
which inherited the same precondition, would have confirmed it rather than caught it.

Fixed to `rows_complete = not truncated and total > 0`, with `term_list_provably_complete` kept as
a separate, separately-reported property, and `projection_test_reliable` now requiring row
completeness. Both are asserted in the audit so a regression in either is visible.

Same root, smaller: `max_entities_on_a_functional_term` and `max_entities_on_a_location_term` held
**annotation** counts in the fallback branch under names saying "entities" — the round-2 misnomer
surviving in the two fields the rename had not reached (PMID:33961781 read
`max_entities_on_a_location_term: 5`). Renamed to `max_functional_spread` / `max_location_spread`
with a `spread_units` field carrying `entities` or `annotations`, and `verdict()` now prints the
units rather than assuming them.

### The round-5 correction: the same fix, in the output a human reads

The units fix from round 4 reached the JSON and three of `verdict()`'s five branches. Two still
hardcoded the noun: the general fallback said "functional rows on N entities" outright, and the
branch the whole theca argument prints through was units-correct on the localisation count and
hardcoded on the functional one ("confined to N entity"). Both render
`max_functional_spread`/`max_location_spread`, which hold **annotation** counts whenever
`spread_units == "annotations"` — the truncated large-screen case the docstring names as its
motivation. Unreachable with these six references today, and irrelevant that the JSON was right
beside it: `verdict()` is what `main()` prints, and the printed sentence is where a reader forms
the projection judgement.

That is the second time a defect has survived because its branch was unreachable from the cited
data. So the coverage is no longer left to the dataset: `selftest()` runs on every invocation,
before any report is written, driving `verdict()` with synthetic blocks that take the fallback,
localisation and same-count branches on an annotations basis and asserting that **no printed count
carries a unit the block did not declare** — plus the mirror, that an entities basis says entities.
Verified by reintroducing the exact regression: the run aborts in `selftest()` rather than emitting
a report.

Also this round: `audit_claims.py` reaches every JSON field through a `flag()` helper that reports a
renamed or dropped field **by name** instead of raising `KeyError` (verified by renaming
`rows_complete`); the previously unguarded 19-entities figure is now value-checked against
`distinct_entities_seen`; and the review's prose no longer justifies the projection precondition by
naming term-list closure when row completeness is what does the work.

The pattern across all five rounds is one thing, stated five ways at five depths: **a number's
name must match how it was obtained.** Round 1 mixed a total with a sample; round 2 mixed an
annotation count with an entity count; round 3 left two fields the rename missed; round 4 gated a
row-derived count on a term-derived property; round 5 left the hardcoded noun in the two branches
a reader actually sees. Each was invisible to every mechanical check in the repository, and each
was found by someone asking what a specific number was actually counting.

The second, procedural lesson is that **a fix verified only against reachable data is half
verified**. Rounds 3 and 5 were both branches the six cited references never enter; both were
correct in the JSON and wrong in the code path. `selftest()` exists because the reviewer had to
find the same class twice.

Two further guard gaps surfaced from break-testing this round, both of the same family as the
round-2 blindness:

- **The retraction string was too long.** Banning the whole sentence let an emphasised or reworded
  variant walk past — which is exactly how the phrase survived in §5 while §14b declared it
  corrected. The banned string is now just the two words that carry the claim, and `norm()` strips
  markdown emphasis and backticks so `**twice**` and `` `twice` `` cannot bypass it. Both variants
  now fail.
- **A guard that runs after the thing it guards is not a guard.** The availability check for
  `entities_per_term` sat *below* the patterns that indexed into it, so the intended message was
  unreachable behind a `KeyError`. Moved above, and verified by deleting the field.

The general rule, which is the transferable part: **a count taken from a page and a count taken
from `numberOfHits` must never be reported side by side without saying which is which.** The
`*_seen` suffix and the `truncated` flag exist to make that impossible to do by accident again.

The checker itself needed a fix, found by reading its output rather than trusting it: counting
bare `GO:0005515` as a functional claim made *every* interaction paper look like a projection and
mis-flagged PMID:35793634 as "possible projection" until that term was excluded from the
functional set. Same shape as the ACTL8 family survey excluding `GO:0005515` from
"informative MF".

Also checked and negative: **`CommentsCorrections`/`RefType` on all six cited PMIDs is empty** —
no erratum, no Publisher Correction, no retraction. That field is checked directly on each cited
article's own record, because a Publisher Correction is not findable by a publication-type query.

And every cross-gene fact this review leans on was verified against the merged YAML rather than
taken from a summary: ACTL7A `GO:0005198` IBA ACCEPT + `GO:0005200` TAS REMOVE + core MF
`GO:0005198`; ACTL7B the same plus `GO:0015629` TAS REMOVE; ACTR10 `GO:0005200` IBA **ACCEPT**
with core MF `GO:0005200`; ACTL8 `GO:0015629` IBA **KEEP_AS_NON_CORE**; ACTR1B `GO:0005515` from
PMID:33961781 **KEEP_AS_NON_CORE**. All five as relied on.

## 15. The committed lint, and the two real defects it caught

`ACTRT3-bioinformatics/audit_claims.py` checks every load-bearing number in the review and in
these notes against `results.json` and `withfrom.json`. It exists because the campaign's
recurring failure is not a wrong term or a fabricated quote — every mechanical check passes on
those — but a number in prose drifting from the number the analysis computed, or a fix applied
in N places landing in N−1. Run it after any edit: `uv run python audit_claims.py`.

It found two genuine defects, neither of which any existing check would have caught:

1. **The gene count was written as "eleven"; the answer is thirteen.** The prose *enumerated* the genes
   correctly in both batches (ACTR5, ACTR6, ACTR8, ACTL6A, ACTL6B, ACTL7A, ACTL7B, then ACTR2,
   ACTR3, ACTR3B, ACTR3C, ACTR1A, ACTR1B) and then totalled them wrongly, in four places in the
   review and one in these notes. Every constituent string was verbatim and the enumeration was
   right; the error was purely in the join, exactly the ACBD3 shape.
2. **`results.json` was silently mis-ordering the clade rankings.** The ranking was stored as a
   dict sorted by value, and `json.dump(..., sort_keys=True)` re-alphabetised it on the way out,
   so the committed JSON's order was meaningless while `RESULTS.md` — generated in memory before
   the dump — was correct. Found only because the audit reconstructs the RESULTS.md table row
   *from* `results.json` and the reconstruction did not match. Fixed by storing a list of pairs;
   verified by confirming `RESULTS.md` is byte-identical after the fix, i.e. the report was
   always right and only the machine-readable copy was wrong.

**The first version of the lint was blind, and only breaking it revealed that.** It checked that
a phrase such as `"18 of 38"` occurred at least N times. Corrupting one instance did *not* fail
it, because the phrase occurred more than N times elsewhere and the floor was never crossed —
the same shape as a detector and a mutator disagreeing on scope. The rewrite does not count
phrases: it matches a context with the number as a **capture group** and requires *every* match
to equal the computed value, so a changed digit fails wherever it sits. Six deliberate breaks
are now each caught: a corrupted headline tally, a corrupted comparator, a reinstated retracted
phrasing, a gene dropped from the enumeration, a corrupted quoted ranking row, and a changed
identity percentage. One of those (the dropped gene) regressed during the rewrite and was
restored — which is itself the argument for break-testing rather than reading the checker.
