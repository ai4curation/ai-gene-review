# Best-family sweep of the cutoff check (2026-11-22)

The [trusted-cutoff check](../RESULTS.md) scores a protein against the NCBIfam families
that carry an annotated activity. A below-cutoff verdict there can mean only "not this
family", because a sister family with no EC number in the NCBIfam release table is never
scored (ptxD's case). The check now also scans each protein against the whole
function-level NCBIfam library, so its closest families are always reported.

This sweep runs that check over every live (not retired) IEA or IBA row in the
P. putida KT2440 (`PSEPK`) and E. coli (`ECOLI`) reviews whose GO term maps to a
complete EC number: 1308 rows on 1044 proteins, NCBIfam release 20.0. The reviewer's
action is read afterwards and is never an input to the verdict. **No review is changed
here.**

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

Kept rows also include 10 BETWEEN_NC_TC verdicts and removed rows include 3; the other
125 rows carry another action, such as MODIFY or UNDECIDED. Most kept rows pass a family that carries the
activity. But nearly half of the removed rows pass one too, so passing a family is weak
evidence that a removal was wrong. The reasons are below.

## What the disagreement lists contain

### Kept rows that fit another reaction's family (35)

In these rows the protein fails every family carrying the term and passes a function-level
family for a different reaction, and its own UniProt record does not state the annotated
EC. Read case by case, most rows follow one of three patterns, and none is decided by the
scores alone:

- **A partial reaction of a multi-step enzyme.** Glutaminase (`GO:0004359`) on the
  amidotransferase subunits gatA, pyrG and carA, and phosphoprotein phosphatase on the
  bifunctional kinase/phosphatase aceK. The passing family is the protein's own
  amidotransferase or bifunctional family.
- **A cofactor or donor variant of the protein's own reaction.** NAD+ versus NADP+ terms
  on puuC, sad, gdhA, gpsA and aldB-II; GDP-forming succinate-CoA ligase on sucC, which
  passes the ADP-forming subunit beta families. Also alcohol dehydrogenase (NAD+) on the
  homoserine dehydrogenases thrA and metL, which the thrA review accepts because the
  mapped Rhea reaction is the NAD-linked homoserine reaction. HMM families rarely
  separate cofactors, so these rows are about which term is right, not which family.
- **A complex's activity on one subunit.** NADH dehydrogenase (ubiquinone) on nuoC and
  nuoG, which pass their own subunit families.

For ECOLI paaH, the target model passes on whole-sequence score (681.0 / 508.0) but fails
on best-domain score. HMMER's `--cut_tc` requires both, and the table shows the domain
score wherever it is the one that fails. The remaining rows are single cases.

### Kept rows the protein's own record supports (38)

Here the gene's UniProt record does state the annotated EC, and the passing family is
the protein's own family, whose EC list in the NCBIfam release table is narrower than
the protein's activities. Examples are helicase activity on recB, recD, recG and uvrD,
whose families are named for the exonuclease or the complex. These rows are
expected, not conflicts. They are separated out only because the scores cannot tell them
from the list above.

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
  became a target only because the release table lists the row's GO term. In four
  families that term contradicts the family's own product name. GO definitions were
  checked in QuickGO:

  | family | product name | GO term in the release table | the term for the named reaction |
  |---|---|---|---|
  | NF006766.0 | formate-dependent phosphoribosylglycinamide formyltransferase | GO:0004644 (10-formyltetrahydrofolate donor) | GO:0043815 phosphoribosylglycinamide formyltransferase 2 activity (ATP + formate) |
  | TIGR02095.1 | glycogen/starch synthase, ADP-glucose type | GO:0004373 (UDP-glucose donor) | GO:0009011 (ADP-glucose donor) |
  | NF006946.0 | CDP-diacylglycerol--serine O-phosphatidyltransferase | GO:0008444 (glycerol-3-phosphate acceptor) | GO:0003882 (L-serine acceptor) |
  | TIGR02491.1 | anaerobic ribonucleoside-triphosphate reductase activating protein | GO:0043365 ([formate-C-acetyltransferase]-activating enzyme) | the PFL activase term names a different glycyl-radical enzyme |

  The reviews removed the matching rows on purT, glgA, pssA and nrdG for the same
  reason. These four are candidates for feedback to NCBI's PGAP curators. They are
  recorded here and nowhere else yet. For catB, PP_2528 and pycB, the family's GO
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
