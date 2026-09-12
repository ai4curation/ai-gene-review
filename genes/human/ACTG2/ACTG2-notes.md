# ACTG2 (P63267) — review notes

Smooth muscle gamma-enteric actin. HGNC:145, chromosome 2p13.1, 376 aa, `PE 1: Evidence at
protein level`. Reviewed as part of the PAINT + affinage campaign; a sibling agent reviewed
**ACTA2** (the other smooth muscle actin) in parallel, and the differences between the two are
recorded in a dedicated section below.

## 0. The shape of the problem

ACTG2's GOA record has **27 rows and not one low-throughput experimental annotation**:
3 IBA, 5 IEA, 8 ISS, 3 bulk-proteomics HDA, 8 Reactome TAS. It is the commonest cause of
visceral myopathy and megacystis-microcolon-intestinal hypoperistalsis syndrome (MMIHS5), it
has three deposited cryo-EM structures of its own filament, and GO knows none of it.

Two opposite errors were available and both were avoided deliberately:

- **importing the divergent-actin scepticism.** Twelve actin-family reviews merged before this
  one (ACTL7A/7B/8/10, ACTR1A/1B/5/8/10, ACTRT3, ACTMAP, ACTB) and most of them argue *down*
  family-level actin inferences, because their subjects are 33–50 % identical to beta-actin and
  have never been shown to polymerise. ACTG2 is not in that class: it is 98.7 % identical to
  alpha-skeletal actin and **38/38 identical at the filament protomer interface**
  (`ACTG2-bioinformatics/RESULTS.md` section 2). Family-level actin terms are *true* here.
- **reading the disease as the function.** ACTG2's literature is overwhelmingly about what
  happens when it is mutated. Kept separate throughout: the protein's function is to be the
  thin-filament actin of visceral smooth muscle; the diseases are the consequence of losing it.
  Note the mechanism is explicitly **dominant-negative, not loss of function**
  [PMID:38820162 "These mutations are thought to cause disease through dominant-negative rather
  than loss-of-function mechanisms since heterozygous ACTG2 truncations and frameshifts have
  been documented in healthy individuals"], which is itself a reason not to convert disease
  phenotypes into gene-level process annotations wholesale.

## 1. The headline finding: `GO:0005884 actin filament` never reaches the smooth muscle actins

Measured, not asserted. Inside PANTHER family PTHR11937, `GO:0005884 actin filament` is
asserted at exactly **three** nodes, all on the same day, 2019-03-01
(`interpro/panther/PTHR11937/PTHR11937-paint.tsv`):

| node | IBD seed(s) | taxon | human genes reached |
|---|---|---|---|
| `PTN000233075` | `UniProtKB:P68133` (ACTA1) | 32523 Tetrapoda | ACTA1 only |
| `PTN000748220` | `UniProtKB:P68032` (ACTC1) | 32523 Tetrapoda | ACTC1 only |
| `PTN002631586` | `MGI:MGI:87906`, `UniProtKB:P63261` | 117571 Euteleostomi | ACTB, ACTBL2, ACTG1, ACTL8, POTEE/F/I/J/KP |

Two singleton nodes plus one cytoplasmic-clade node. **No node covers the smooth muscle
actins**, so QuickGO returns **zero** annotations to `GO:0005884` or any descendant for either
`P63267` (ACTG2) or `P62736` (ACTA2), while every other conventional human actin has it. The
same node `PTN000748220` also carries `GO:0017022 myosin binding`, `GO:0033275 actin-myosin
filament sliding` and `GO:0007015 actin filament organization`, and each of those reaches
ACTC1 alone.

The irony is exact and is the reason this is a *node-placement* finding rather than a missing
row: the **only** PAINT node in PTHR11937 that specifically covers the smooth muscle actin pair
is `PTN004322804`, and what it gives them is `GO:0005576 extracellular region`. Checked against
all 1420 human `GO:0005576` IBA annotations: the node reaches exactly **ACTA2 and ACTG2** and
nothing else.

So PAINT has a node for the smooth muscle actins and used it to place them outside the cell,
while the term that is unambiguously true of them sits on two single-gene nodes. Same shape as
the AADACL2/3/4 finding ("right term, wrong node"), and fixable in one edit for two genes.

## 2. The evidence that ACTG2 *is* a filament actin — from ACTG2, not from the family

`PMID:38820162` (Ceron et al., Sci Adv 2024) is the paper GO has not seen. QuickGO returns
**zero annotations** for this reference. It provides, on recombinant human ACTG2 expressed in
human cells:

- purified WT ACTG2 polymerises in a pyrene-actin assay, with a measured rate and critical
  concentration [PMID:38820162 "WT ACTG2 exhibited slower polymerization compared to"];
- three cryo-EM helical reconstructions of ACTG2 filaments at 2.45–2.72 Å [PMID:38820162
  "structures of WT ACTG2, R40C, and R257C filaments using helical reconstruction"] —
  PDB 8V2O (WT), 8V2Z (R257C), 8V30 (R40C);
- every protomer of every structure carries **Mg-ADP**, and the paper states the hydrolysis
  happened in the tube [PMID:38820162 "release occurred during sample preparation, before
  vitrification, resulting in all three structures containing Mg"];
- ACTG2 filaments are propelled by smooth muscle myosin in a gliding assay, at a velocity
  indistinguishable from alpha-actin [PMID:38820162 "The filament gliding velocity was similar
  for"];
- the structures also resolve `HIC` (4-methyl-histidine) in every protomer, independently
  corroborating UniProt's experimentally-evidenced His-74 SETD3 methylation
  [file:human/ACTG2/ACTG2-uniprot.txt "CC   -!- PTM: Methylated at His-74 by SETD3."].

Computed independently in `ACTG2-bioinformatics/`: the 38 protomer-interface positions of
F-actin (PDB 6DJO chain C, 4.0 Å) are **38/38 identical** in ACTG2 and in ACTA2, tying ACTA1 and
ACTC1 at the top of a 16-protein panel whose bottom is ACTL10 at 5/38. The script refuses to
report that number unless it first reproduces all 14 columns published in the merged ACTL8
review, which it does exactly.

## 3. The AgBase ISS block: one 1999 chick paper on the *other* smooth muscle actin

Six of ACTG2's 27 rows (`GO:0005737`, `GO:0010628`, `GO:0030027`, `GO:0030175`, `GO:0044297`,
`GO:0090131`) are ISS from `UniProtKB:P08023`. Resolved: that is **chicken ACTA2**, "Actin,
aortic smooth muscle". Every one of its six source annotations comes from a single reference,
`PMID:10633868`, which is titled and framed for alpha-smooth-muscle actin
[PMID:10633868 "alpha-Smooth-muscle actin (SMA) is the major isoform of adult vascular tissues."]
and studies chick atrioventricular endocardial cushion endothelial-to-mesenchymal
transformation [PMID:10633868 "distributed in a punctate manner in the lamellipodia/filopodia of
invading mesenchymal cells"].

Three things make this a paralog transfer rather than an ortholog one:

1. **Chicken has its own ACTG2.** `P63270` (ACTH_CHICK, 376 aa) is the reviewed one-to-one
   orthologue and was not used.
2. **The same block is already on human ACTA2**, which is the correct target: `P62736` carries
   `GO:0010628`, `GO:0030027`, `GO:0030175`, `GO:0044297` and `GO:0090131` ISS from the very same
   `UniProtKB:P08023`.
3. **The cell type is wrong for ACTG2.** ACTG2 is enteric
   [file:human/ACTG2/ACTG2-uniprot.txt "CC   -!- TISSUE SPECIFICITY: In the intestine, abundantly expressed in smooth"],
   not cardiac-cushion mesenchyme.

`GO:0010628 positive regulation of gene expression` deserves a separate note: the paper's SMA is
the *target* of TGF-beta-dependent induction and of antisense knockdown
[PMID:10633868 "Antisense oligodeoxynucleotide (ODNs) specific for SMA reduced both SMA
expression and mesenchymal formation in AV endothelial cells cultured with myocardium on a
collagen gel lattice."]; nothing in the abstract has SMA regulating any other gene's expression.
I have only the abstract, so the AgBase IDA on chicken ACTA2 is flagged as a question for AgBase
rather than declared wrong; the human ISS row is removed on the paralog/cell-type grounds above,
which do not depend on it.

## 4. `GO:0032982 myosin filament` — right biology, impossible compartment

Row 10 is ISS from `UniProtKB:F1P476`, an **unreviewed TrEMBL** chicken ACTA2 entry (a second
copy of the same paralog), whose IDA comes from `PMID:8006065`, "Actin isoform compartments in
chicken gizzard smooth muscle cells". The sentence behind it says
[PMID:8006065 "Using an antibody specific only for muscle actin, labelling was found generally
around the myosin filaments of the contractile apparatus, but was absent from the core of the
dense bodies that contained beta-actin."].

*Around* the myosin filaments, not in them. `GO:0032982` is defined as "A supramolecular fiber
containing myosin heavy chains, plus associated light chains and other proteins, in which the
myosin heavy chains are arranged into a filament" — an actin cannot be located in it. The
correct compartment for the observation is `GO:0030485 smooth muscle contractile fiber`.

Unusually for this row's donor, the underlying biology is *better* founded for ACTG2 than for
ACTA2: chicken gizzard is enteric smooth muscle, the antibody was pan-muscle-actin rather than
alpha-specific, and the paper says both muscle actins are present
[PMID:8006065 "Differentiated smooth muscle cells typically contain a mixture of muscle (alpha
and gamma) and cytoplasmic (beta and gamma) actin isoforms."]. So this row is repaired
(MODIFY to `GO:0030485`) rather than removed.

## 5. The rat Ensembl-Compara rows are alpha-SMA liver-fibrosis marker measurements

Rows 6–8 (`GO:0045471` response to ethanol, `GO:0071354` cellular response to interleukin-6,
`GO:1905641` cellular response to acetaldehyde) are IEA/GO_REF:0000107 from rat `Actg2`
(`P63269`), whose own evidence is **IEP** — expression pattern — from two liver studies:

- `PMID:21294755`, "Leptin and acetaldehyde synergistically promotes **alphaSMA** expression in
  hepatic stellate cells by an interleukin 6-dependent mechanism"
  [PMID:21294755 "an activation marker of HSCs"]. Reference-projection check: 8 annotations over
  **6 entities** (Col1a1, Tgfb1, Il6, Timp1, Actg2, Mapk14), with `GO:1905641` on **6 of 6** —
  a marker panel measured in one experiment, with the term spreading across the whole set.
- `PMID:28320086`, ethanol liver fibrosis in rats
  [PMID:28320086 "as denoted by reducing a-smooth muscle actin (a-SMA) expression in the liver"].
  3 annotations over 3 entities (Tgfb1, Il6, Actg2), all IEP.

Both papers measure **alpha-SMA**, the canonical activated-hepatic-stellate-cell marker, i.e. the
ACTA2 gene product; neither mentions enteric gamma-actin, and rat `Acta2` (`P62738`) received no
annotation from either paper. That looks like an alpha-SMA/ACTG2 symbol conflation at the rat
end, but I have not read either full text, so it is recorded as a question for RGD rather than
asserted. The action taken is on the **human IEA rows**, which is a propagation judgement and
does not overrule any curator: an mRNA/protein-level change in a marker panel does not make a
structural actin "involved in" a chemical response, and ACTG2 is not expressed in hepatic
stellate cells.

## 6. `GO:0005576 extracellular region` IBA — the full chain

`PTN004322804` has a **single** IBD seed, `RGD:621676` = rat `Acta2`. The chain has to be stated
carefully, because the first version of these notes ran two independent routes together and a
cross-check against the parallel ACTA2 review caught it.

- **The seed gene is also a recipient.** Rat Acta2's own `GO:0005576` annotation is
  `GO:0005576 IBA GO_REF:0000033` with `PANTHER:PTN004322804` and `RGD:621676` — the identical
  row human ACTG2 carries, citing this node and rat Acta2's own identifier. A self-referential
  IBA is a normal PAINT construct, not by itself a defect, but it means the seed's exact-term
  annotation is the node's own output and is not independent support.
- **No non-IBA evidence for the exact term exists in the chain.** Rat Acta2's only non-IBA
  annotation anywhere under `GO:0005576` is `GO:0005604 basement membrane` IDA from
  `PMID:30476341`, a fetal-rat-testis retinoic-acid/phthalate toxicology study
  [PMID:30476341 "Humans are universally exposed to low levels of phthalate esters (phthalates),
  which are used to plasticize polyvinyl chloride."]. The PAINT table records which *gene* seeded
  an IBD, not which of its annotations justified it, so identifying that IDA as the underlying
  basis is an inference — the only candidate, but an inference.
- **That IDA reaches human by a different route, and not to ACTG2.** Human ACTA2 carries
  `GO:0005604` IEA from `GO_REF:0000107` with `UniProtKB:P62738` — Ensembl Compara, a different
  term, evidence code and reference from the IBA. Human ACTG2 carries **no** `GO:0005604` row at
  all. The two chains are independent and must not be merged.

The reference-projection check on `PMID:30476341` comes back **negative** for projection — 13
annotations over 7 entities, and only Acta2 got the localisation IDA while the other six got
retinoic-acid-response IEP terms — so this is genuine per-protein curation, not a
complex-to-subunit spread. That negative is worth recording: the problem is not that the source
is fabricated, it is that

1. the source is the **paralog** (Acta2), in **rat**, in **fetal testis**;
2. the only experimental anchor sits three levels below the term the node asserts, so the node
   asserts something no experiment in the chain measured — the inverse of the ACRV1 case, where
   a propagation landed above its donor; and
3. the qualifier is `is_active_in`, which asserts that ACTG2 performs its molecular function in
   the extracellular region.

Combined with the three bulk-proteomics HDA rows (`GO:0070062` 1046 entities, `GO:0072562` 141,
`GO:0005576` 95 — all one term per reference across every entity), ACTG2's entire extracellular
record is proteomic carry-over plus one paralogous immunostain.

## 7. `GO:0005200` is correctly retained here — verified, not assumed

The brief warned that `GO:0005200` is IRD-negated at eight descendant nodes and that "the four
conventional actins" retaining it might not include ACTG2. Checked from primary PAINT data plus
QuickGO: the term is asserted at `PTN000940351` (IBD, 10 seeds) and negated (IRD) at exactly
eight nodes — `PTN000233596`, `PTN000233752`, `PTN000233796`, `PTN000233887`, `PTN000234048`,
`PTN001732543`, `PTN007551901`, `PTN008986528`. `PTN000940351` reaches **10 human genes: ACTA1,
ACTA2, ACTC1, ACTG2, ACTL9, ACTL10, ACTR10, ACTRT1, ACTRT2, ACTRT3.** So the "four conventional
actins" in that tally are ACTA1/ACTA2/ACTC1/**ACTG2** — ACTB and ACTG1 get the term from
`PTN002631586` instead — and ACTG2 *is* in the retained set.

The donor set at that node is deliberately heterogeneous: conventional actins (yeast ACT1,
ACTB, mouse/rat Actg1, two *Dictyostelium* actins) **plus Arp2 and Arp3** (branched-filament
nucleators) **plus yeast ARP1 and ARP10** (dynactin's mini-filament). At that depth
"structural constituent of cytoskeleton" is the genuine LCA of the donors, so
`GRANULARITY_MISMATCH` does not apply and no specificity upgrade is warranted at the node. All
10 protein donors resolve and all 10 carry their own experimental-code evidence for the term.

### Why the sibling reviews are consistent rather than contradictory

Three merged reviews resolved the *same* `GO:0005200`/`PTN000940351` row three ways:
ACTR10 ACCEPT, ACTL10 MARK_AS_OVER_ANNOTATED, ACTRT3 MODIFY to `GO:0005198`. This looks like
the AADACL2/3/4 inconsistency but is not the same situation: those three genes have identical
donor sets *and* comparable evidence, whereas here the recipients differ in exactly the property
the term asserts. On the 38-position filament interface panel, ACTR10 scores 20+8, ACTRT1 13+8,
ACTL10 3+2, and ACTG2 38+0. A term about contributing to the structural integrity of a
cytoskeletal structure is a measurement-backed ACCEPT at 38/38 and a genuine question at 5/38.
ACTG2 therefore ACCEPTs it without disturbing the divergent-gene calls, and the ACCEPT is
grounded in ACTG2's own structures rather than in the node.

## 8. Where ACTG2 and ACTA2 differ (reviewed in parallel)

Identical in GOA: both carry `GO:0005200` IBA from `PTN000940351`, `GO:0015629` IBA from
`PTN002631484`, `GO:0016887` ISS from pig ACTA1 `P68137`, `GO:0005856` IEA from SubCell SL-0090,
`GO:0005576` IBA from `PTN004322804`, and the same Reactome cytosol export. Both lack
`GO:0005884`. Both score 38/38 at the filament interface.

Differences that matter:

- **ACTA2 is the correct ISS target of the chick alpha-SMA block; ACTG2 is not.** ACTA2 holds
  five of those rows legitimately (chicken ACTA2 is its orthologue); ACTG2 holds six of them as
  paralog transfers. This is the single largest difference in their records and it accounts for
  six of the removals here.
- **ACTA2 has its own experimental annotations, ACTG2 has none.** ACTA2 carries three `GO:0005737`
  IDAs, two IEP rows, a `GO:0032991` IDA and ten `GO:0005515` IPI rows; ACTG2 has no IDA, IMP,
  IPI, IGI or IEP row at all.
- **Only ACTG2 has a solved filament.** PDB 8V2O/8V2Z/8V30 are ACTG2; there is no equivalent
  ACTA2 filament reconstruction in its UniProt cross-references.
- **Only ACTG2 carries the rat Ensembl-Compara response-to-chemical rows** — which is itself
  evidence for the conflation in section 5, since alpha-SMA is what those papers measured and
  ACTA2 is the gene that should have received them if anything.
- **Tissue.** ACTA2 is vascular/aortic; ACTG2 is enteric and bladder, "tissue enhanced
  (intestine, seminal vesicle, smooth muscle)" in HPA.

## 9. Provider record (affinage) assessment

`gates_passed: True`, 13 citations, all numeric PMIDs, no `PMID:bio_*` preprint identifiers.
The narrative is accurate on the disease genetics and the polymerisation defect and was useful
as a lead list. Two limitations, both recorded because they mattered:

- **It misses `PMID:38820162` entirely** — the only paper that measures purified human ACTG2 and
  solves its filament, and the source of every experimental annotation proposed here. The
  provider's most recent structural claim is a 2025 mouse knock-in paper. So the highest-value
  reference for this gene was found from the UniProt PDB cross-references, not from the record.
- Its bottom third is cancer-cell over/under-expression and miRNA-sponge work
  (`PMID:28385530`, `PMID:35652208`, `PMID:37213144`, `PMID:27107594`, `PMID:33910387`) which
  reports ACTG2 as a *regulated transcript* in cell lines. None of it supports a gene-level GO
  function and none of it is used.

**Retraction / erratum check (negative, reported because it was run):** all 20 load-bearing
PMIDs were checked by reading `PublicationTypeList` **and** `CommentsCorrections/RefType` on each
cited article's own PubMed record — the only way to see a Publisher Correction, which a
publication-type query cannot find. None of `38820162, 26647307, 24337657, 24676022, 30626964,
31993215, 8006065, 10633868, 21294755, 28320086, 30476341, 36264152, 40617346, 31769566,
23533145, 22516433, 23580065, 24743229, 22960657, 25998219` carries a retraction, erratum,
expression of concern, or correction.

## 10. Checks run whose result was negative or null

- **Reference-projection check** on all ten literature references (section 6 of RESULTS.md).
  Negative for complex-to-subunit projection everywhere; the three HDA references are bulk
  proteomics (one term, 1046/141/95 entities) and `PMID:21294755` is a six-gene marker panel, but
  none is a ComplexPortal-style phenotype spread of the ACTR8 kind. `PMID:38820162` returns **0**
  annotations, which is the gap rather than a projection.
- **Entity counts are distinct gene-product counts, fully paginated.** The script fetches every
  page and reports "unavailable" rather than substituting an annotation total or a page total.
  All ten enumerations completed within the page budget.
- **Dead-accession guard.** Every UniProt lookup asserts `primaryAccession == requested`, so a
  deleted entry cannot masquerade as a subunit carrying no annotations (the ACTR10/`O15507`
  trap). No dead accessions were found among the 31 distinct source proteins.
- **Unresolved WITH/FROM tokens: none.** All 54 tokens across 16 rows resolve; the four
  `WB:WBGene…` tokens needed a free-text fallback because WormBase *gene* identifiers are absent
  from UniProt's `xref:wormbase` index, and the strategy that answered is recorded per token.
- **Swiss-Prot vs TrEMBL counted separately from evidence:** 31 distinct source proteins, 31 with
  their own experimental evidence for the term they donated, **28** reviewed. The three
  unreviewed ones are *Candida* ACT1, *C. elegans* act-5 and chicken `F1P476` — the same two
  TrEMBL entries the ACTL10 review reported for `PTN002631484`, verified here independently.
- **Truncation audit.** The panel is length-audited before any conservation number is computed,
  and the audit is required to flag ACTL10 (245 aa against a conventional-actin modal 377) before
  it may clear ACTG2. ACTG2 is 376 aa and matches its rat, mouse and chicken orthologues exactly,
  so nothing here is a truncation artefact.

## 11. Two numbers that refused to add up, and what they were

- The interface panel initially failed its own reproduction assertion on 4 of 14 published
  columns (ACTL9 5/22 published vs 11/20 recomputed, etc.) while the six conventional actins
  matched. The cause was not the alignment: the ACTL8 script classifies substitutions with
  **hand-defined conservative groups**, and I had used BLOSUM62 > 0. Adopting the committed
  groups reproduces all 14 columns exactly. Had I not asserted reproduction, I would have
  published a panel that silently disagreed with the merged sibling review on the divergent
  genes while agreeing on the conventional ones — the hardest kind of divergence to notice.
- The donor audit reported "20/24 resolved" and, separately, every TrEMBL donor as Swiss-Prot.
  Both were bugs in my own resolver, not facts: UniProt's `entryType` strings are
  `UniProtKB reviewed (Swiss-Prot)` and `UniProtKB unreviewed (TrEMBL)`, so a substring test for
  `"reviewed"` matches **both** and promotes every unreviewed entry; and WormBase gene ids are
  not in the `xref:wormbase` index. Fixed, with the reviewed/unreviewed test now keyed on the
  parenthesised database name and the lookup strategy recorded per token.

## 12. Ontology gap noted

GO models the smooth-muscle contractile apparatus at fibre level (`GO:0030485 smooth muscle
contractile fiber`) and at anchor level (`GO:0030486 smooth muscle dense body`) but **not at
filament level**, while the striated counterpart exists (`GO:0005865 striated muscle thin
filament`). The filament is exactly the level at which ACTG2, ACTA2 and the smooth-muscle
tropomyosins act, and the smooth-muscle thin filament is structurally distinct — no troponin, no
Z-disc, anchored at dense bodies rather than sarcomere ends.

Placement checked rather than guessed: `GO:0036379 myofilament` is **not** available as a parent,
because its definition restricts it to "the smallest contractile units of a myofibril (striated
muscle fiber)". `GO:0005865` itself is not a descendant of `GO:0005884 actin filament` in the
current ontology, so a smooth-muscle sibling should probably be placed `part_of GO:0030485` by
analogy with `GO:0030486`, and the exact axiomatisation is left to GO editors.

## 13. Actions

| rows | action | count |
|---|---|---|
| 2, 3, 4, 9 | ACCEPT | 4 |
| 5, 11, 20–27 | KEEP_AS_NON_CORE | 10 |
| 10 | MODIFY (to `GO:0030485`) | 1 |
| 6, 7, 8, 17, 18, 19 | MARK_AS_OVER_ANNOTATED | 6 |
| 1, 12, 13, 14, 15, 16 | REMOVE | 6 |
| — | NEW | 5 |

27 existing rows = 27 GOA lines (`wc -l` on the TSV is 28 including the header), plus 5 rows
authored here with `action: NEW`, giving 32 entries in `existing_annotations`.

The five NEW rows are `GO:0005884` actin filament (IDA), `GO:0043531` ADP binding (IDA),
`GO:0005524` ATP binding (ISS), `GO:0017022` myosin binding (IDA) and `GO:0006939` smooth
muscle contraction (IMP). Four of the five come from `PMID:38820162`; `GO:0006939` rests on the
human genetic series plus the two knock-in mouse lines.

`core_functions` carries three entries — `GO:0005200` (structural constituent of cytoskeleton),
`GO:0016887` (ATP hydrolysis) and `GO:0017022` (myosin binding) — each with
`directly_involved_in: GO:0006939`, so the machine-readable block states the gene's defining
process and not only its structural role.

## 14. Round-2 corrections (PR review)

Four things changed after review, three of them because a number disagreed with another number.

1. **Six residue counts in `source_label` strings were wrong** — Candida ACT1, *C. elegans*
   act-5 and all four *Dictyostelium* actins. The script asserts that WITH/FROM *tokens* cannot
   drift from GOA; it said nothing about the prose labels wrapped round them, which were typed.
   Fixed programmatically from `results.json`, and closed permanently with
   `ACTG2-bioinformatics/check_source_labels.py`, which checks every `(accession, N aa)` and
   `(accession, Swiss-Prot|TrEMBL)` pair anywhere in the review against the computed record,
   rejects invented `source_id`s, and asserts **presence** so it cannot be defeated by deleting
   the thing it guards. Four self-tests.
   - Writing that guard immediately exposed a bug in the guard: its first regex excluded `)`
     from the window between accession and residue count, so labels of the form
     `A0A1D8PFR4, TrEMBL (unreviewed), 376 aa` were invisible and **two of the six drifted
     lengths went unreported**. That is the same detector-versus-mutator scope mismatch the
     guard exists to catch, found by running it rather than by reading it.
   - The first self-test also asserted the wrong expectation: relabelling one `source_id` does
     not exercise the presence check, because the accession survives elsewhere in the row's
     prose. The guard was behaving correctly and the test was wrong. Split into two mutations.
2. **"human ACTA2 already carries five of the same rows" was the one load-bearing number not
   re-derivable from the committed artefacts.** Now computed in `RESULTS.md` §6a and cited on
   all six affected rows: ACTG2 has 6 ISS rows from `P08023`, human ACTA2 has 5 from the same
   donor, all 5 shared, `GO:0005737` on ACTG2 only. The unused chicken orthologue `P63270` is
   resolved in the same section.
3. **`core_functions` omitted the review's own headline biology.** `GO:0006939` and
   `GO:0017022` were proposed as NEW but appeared nowhere in the structured block, so a
   consumer reading only `core_functions` would have learned that ACTG2 is a structural
   cytoskeletal ATPase and not that it is the thin filament of visceral smooth muscle
   contraction. Added `directly_involved_in` to all three core functions and a third core
   function for the myosin track.
4. **`GO:0005524` ATP binding added as a fifth NEW row.** The record asserted ATP *hydrolysis*
   with no ATP *binding*, which cannot be right. Entered as ISS rather than IDA, one code
   weaker than the ADP row, because no structure resolves ATP-bound ACTG2 — the distinction
   between the observed and the inferred ligand is kept visible.

**One reviewer suggestion was checked and declined.** The suggestion was IPI rather than IDA for
`GO:0017022`, "given the named SMM-S1/MYL6 partner". The paper does not name the partner. Its
methods say the construct came from a baculovirus "provided by L. Sweeney", coexpressed in Sf9
cells with the essential light chain MYL6; no heavy-chain gene or species is given, and MYH11
occurs in the paper exactly twice, both in the introduction, as a visceral-myopathy disease gene
rather than as the identity of this construct. MYL6 is named but is a light chain, not the
actin-binding moiety, so citing it as the interactor would misdescribe the assay. IDA is kept,
with the reasoning written into the row and a note that a curator who can establish the heavy
chain from the cited methods reference should convert it to IPI.
