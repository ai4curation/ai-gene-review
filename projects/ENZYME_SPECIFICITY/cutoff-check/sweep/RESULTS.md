# Best-family sweep of the cutoff check (2026-11-22)

The [trusted-cutoff check](../RESULTS.md) scores a protein against the NCBIfam families
that carry an annotated activity. A below-cutoff verdict there can mean only "not this
family", because a sister family with no EC number in the NCBIfam release table is never
scored (ptxD's case). The check now also scans each protein against the whole
function-level NCBIfam library, so its closest families are always reported.

This sweep runs that check over every live (not retired) IEA or IBA row in the
P. putida KT2440 (`PSEPK`) and E. coli (`ECOLI`) reviews whose GO term maps to a
complete EC number: 1306 rows on 1043 proteins, NCBIfam release 20.0. The reviewer's
action is read afterwards and is never an input to the verdict. Proposed (`NEW`) rows
are skipped. **No review is changed here.** Two pairs of electronic rows on one term
(pedI, `GO:0004029` and `GO:0004030`) carry different actions; the generated list
reports them for the review's action-consistency check.

- Runner: [`run_sweep.py`](run_sweep.py), about 6 minutes once sequences and the pressed
  library are cached. `--rerender` re-derives the lists from saved scores.
- Raw output: [`sweep_results.yaml`](sweep_results.yaml). Each row records the target
  family it scored best against and up to three closest non-target families, each with
  its NCBIfam metadata (family type, EC numbers, GO terms), score, best-domain score and
  cutoffs.
- Generated lists: [`DISAGREEMENTS.md`](DISAGREEMENTS.md).

## Overall agreement

| reviewer action | rows | passes a target family (ABOVE_TC) | below cutoff or other family only (BTC, SFA) | no family carries the activity (NO_MODEL) |
|---|---|---|---|---|
| kept (ACCEPT, KEEP_AS_NON_CORE) | 1014 | 827 (82%) | 118 | 59 |
| removed (REMOVE, MARK_AS_OVER_ANNOTATED) | 169 | 80 (47%) | 67 | 19 |

Excluding rows where no family carries the activity, the pass rates are 87% (827 of 955)
for kept rows and 53% (80 of 150) for removed rows.

Kept rows also include 10 BETWEEN_NC_TC verdicts and removed rows include 3; the other
123 rows carry another action, such as MODIFY or UNDECIDED. Most kept rows pass a family that carries the
activity. But nearly half of the removed rows pass one too, so passing a family is weak
evidence that a removal was wrong. The reasons are below.

## What the disagreement lists contain

The kept rows that fail their target families but pass another function-level family
are split three ways. The split depends on how each passing family relates to the
protein, which the lists tag:
- `[named]`: the family is named for the protein (its gene symbol, the best target's
  product name, or a protein name on its UniProt record);
- `[record_ec]`: the family carries an EC number the record states;
- `[other]`: neither.

### Kept rows whose protein passes a family for another activity (41)

In these rows, some passing family is `[other]`, or the protein passes its own family
(`[record_ec]`) while its UniProt record does not state the annotated EC. Read case by
case, most rows follow one of three patterns, and none is decided by the scores alone:

- **A partial reaction of a multi-step enzyme.** Glutaminase (`GO:0004359`) on the
  amidotransferases pyrG and carA, and phosphoprotein phosphatase on the bifunctional
  kinase/phosphatase aceK. The passing family is the protein's own amidotransferase or
  bifunctional family.
- **A cofactor or donor variant of the protein's own reaction.** NAD+ versus NADP+ terms
  on sad, gdhA, gpsA and aldB-II; GDP-forming succinate-CoA ligase on sucC, which passes
  the ADP-forming subunit beta families. Also alcohol dehydrogenase (NAD+) on the
  homoserine dehydrogenases thrA and metL, which the thrA review accepts because the
  mapped Rhea reaction is the NAD-linked homoserine reaction. HMM families rarely
  separate cofactors, so these rows are about which term is right, not which family.
- **A complex's activity on one subunit.** NADH dehydrogenase (ubiquinone) on nuoC.

The rest are single cases. Some are a related activity of the protein's own family: alr
is a broad-specificity racemase (EC 5.1.1.10) that passes the alanine racemase families.

### Kept rows where another model of the protein's own family passes (14)

Every passing family is `[named]`: another NCBIfam model of the protein's own family,
which the term is not mapped to. These rows are nuoG, gatA, gatB, paaH, fadB, paaF, puuC,
acs, cheZ, dsbA and appA. They usually show a gap in the release table's EC and GO
mapping, not a doubt about the row. For ECOLI paaH, the target model passes on
whole-sequence score (681.0 / 508.0) but fails on best-domain score (495.3 / 508.0).
HMMER's `--cut_tc` requires both, and the lists show the domain score wherever it is the
one that fails.

### Kept rows whose annotated EC the protein's UniProt record states (18)

Every passing family is `[named]` or `[record_ec]`, and the record also states the
annotated EC. Examples are helicase activity on recB, recG and uvrD, whose families are
named for the exonuclease or the complex, and glutaminase on the amidotransferase hisH.
These are mostly secondary or partial reactions that the family's EC list leaves out.
The record's support for the annotated EC can still be the weak point. In yihU the
4-hydroxybutyrate dehydrogenase EC (1.1.1.61) is on the record with experimental
evidence (PMID:19372223), but the protein's own family is named for its
sulfolactaldehyde reductase activity, and the review keeps the row as non-core.

### Kept rows below cutoff with no competing family (45)

These are the weakest leads. The closest family is usually the expected one, scored just
below its cutoff: sodB 343.9 / 348.0, ppnP 120.6 / 143.0, aruC 340.7 / 372.0, and the
gamma-glutamyl-GABA hydrolases PP_3598, spuA and PP_5298 at 193.0 to 218.5 / 266.0.
That is a divergent family member, not a different function. A few rows carry a more
specific term than the protein's closest family, such as the glutamate-putrescine ligase
term on puuA, puuA-I and puuA-II, whose closest non-target families are glutamine
synthetases.

### Removed rows whose protein passes the family (56)

None of the rows read for this summary looks like a wrong removal. Most fall into four
groups.

- **A subunit model carrying the complex's EC number.** This applies to:
  - DNA polymerase III subunits dnaN, dnaQ, holA, holB, holC and dnaX;
  - RNA polymerase subunits rpoA and rpoZ;
  - NADH dehydrogenase subunits nuoB, nuoI and nuoK;
  - urease subunits ureA and ureB;
  - acetyl-CoA carboxylase subunits accB and accD;
  - phenylacetyl-CoA epoxidase subunits paaC and paaE;
  - K+-transporting ATPase subunits kdpC and kdpF;
  - carbamoyl-phosphate synthase subunits carA and carB.

  The release table gives each subunit model the reaction of the whole complex, so a
  passing score shows membership of the subunit family, not catalysis.
- **Pseudoenzymes and divergent paralogs the reviews identified.** crc (no catalytic
  residues), pyrC' (catalytically inactive), yciO, PP_3394 (lacks the HMG-CoA-lyase
  signature; MvaB is KT2440's lyase), PP_2325, davT and gbd. The family HMM sees the
  fold. The reviews cite residue, paralog or experimental evidence that it cannot see.
  This is the limitation Schnoes et al. describe for superfamily-level transfer.
- **Correct but broader substrate terms**, marked over-annotated: murF and PP_4545.
- **NCBIfam GO metadata naming a sister reaction (rows matched `go_only`).** The family
  became a target only because the release table lists the row's GO term. In six
  models, covering four reactions, that term contradicts the model's own product name or
  EC number. GO definitions were checked in QuickGO:

  | family | product name | GO term in the release table | the term for the named reaction |
  |---|---|---|---|
  | NF006766.0 | formate-dependent phosphoribosylglycinamide formyltransferase (EC 2.1.2.-) | GO:0004644 (10-formyltetrahydrofolate donor) | GO:0043815 phosphoribosylglycinamide formyltransferase 2 activity (ATP + formate) |
  | TIGR01142.1 | phosphoribosylglycinamide formyltransferase 2 | GO:0004644 | GO:0043815 |
  | TIGR02095.1 | glycogen/starch synthase, ADP-glucose type | GO:0004373 (UDP-glucose donor) | GO:0009011 (ADP-glucose donor) |
  | NF001899.0 | glycogen synthase GlgA (EC 2.4.1.21, the ADP-glucose reaction) | GO:0004373 | GO:0009011 |
  | NF006946.0 | CDP-diacylglycerol--serine O-phosphatidyltransferase (EC 2.7.8.8) | GO:0008444 (glycerol-3-phosphate acceptor) | GO:0003882 (L-serine acceptor) |
  | TIGR02491.1 | anaerobic ribonucleoside-triphosphate reductase activating protein | GO:0043365 ([formate-C-acetyltransferase]-activating enzyme) | GO:0043364 glycyl-radical enzyme activating activity, which the sibling model TIGR02826.1 (same product name) carries and E. coli NrdG has by EXP (PMID:9305874) |

  The reviews removed the matching rows on purT, glgA, pssA and nrdG for the same
  reason. Because both PurT models carry the folate-dependent term rather than
  GO:0043815, purT's GO:0043815 row gets `NO_MODEL`. These six models are candidates for
  feedback to NCBI's PGAP curators. They are release-table errors, not defects behind a
  particular GOA row, so they do not fit a review's `source_defects`. They are recorded
  here until a route for NCBIfam feedback exists. The GOA rows on glgA and nrdG came from
  InterPro2GO, which the reviews already flag, so a fix at NCBIfam alone would not reach
  them. A pass comparing each model's EC numbers with the EC cross-references of its GO
  terms over the whole release table would find the rest of this class; this sweep only
  finds models that a swept row lands on. For catB, PP_2528 and pycB, the family's GO
  terms span related reactions its members share, and the reviews judged the protein's
  own specificity. NF011685.0 is named "peptidoglycan glycosyltransferase FtsI", so for
  ftsI it is the review, which treats FtsI as the cross-linking partner of FtsW, that
  disagrees with the family's name.

## What the sweep changes

- Use the library scan when reading a below-cutoff verdict. A protein scoring just under
  its expected family (sodB, ppnP) differs from one that fits another reaction's family.
- Do not read a passing score as support for a removed row without checking the family
  type. Subunit models carry the complex's EC number, and a pseudoenzyme passes its
  active relatives' family.
- Check `go_only` targets against the family's name. The four families above would
  otherwise make the check endorse a wrong activity.

## Limitations

- The library scan uses HMMER's default filters, for speed, while target families are
  scored with filters off. A family the filters drop can be missing from the closest list,
  but the target-family verdicts are unaffected.
- Only function-level families (equivalog, subfamily, exception and their variants, as in
  the check) are reported as competitors. A domain-level model never counts against a row.
- The UniProt-record test reads `EC=` lines from the cached record, so an EC stated only
  in free text is missed.
