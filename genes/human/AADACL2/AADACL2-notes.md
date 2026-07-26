# AADACL2 (Q6P093) — review notes

Human arylacetamide deacetylase-like 2, HGNC:24427, chromosome 3, 401 aa, `PE 1: Evidence at
protein level`, Pharos `Tdark`. Reviewed 2026-07-25 for the PAINT + affinage campaign.

## What the record contains

Seven GOA rows, **no experimental evidence of any kind**: 2 IBA (PANTHER) and 5 IEA
(InterPro ×2, ARBA ×2, UniProt SubCell ×1). Three rows are activities at three levels of
generality; three are locations, two of which are incompatible readings of the same
N-terminal helix.

| term | evidence | source |
|---|---|---|
| GO:0016787 hydrolase activity | IBA | PANTHER PTN009058710 (+16 protein sources) |
| GO:0016020 membrane (`is_active_in`) | IBA | PANTHER PTN009058713, AADAC, mouse Aadac, mouse Nceh1 |
| GO:0003824 catalytic activity | IEA | ARBA:ARBA00027533 |
| GO:0005576 extracellular region | IEA | UniProtKB-SubCell:SL-0243 |
| GO:0016020 membrane (`located_in`) | IEA | ARBA:ARBA00028763, InterPro:IPR017157 |
| GO:0016787 hydrolase activity | IEA | InterPro:IPR013094 (Alpha/beta hydrolase fold-3) |
| GO:0052689 carboxylic ester hydrolase activity | IEA | InterPro:IPR017157 (Arylacetamide deacetylase) |

## Literature: genuinely absent for function, present for genetics

PubMed returns 6 hits for `AADACL2`; none characterises the protein. The affinage record came
back empty (`n_discoveries: 0`, `citation_count: 0`, `gates_passed: True`), and in this case
the emptiness is corroborated rather than taken on trust — the only literature statement
about AADACL2's function is that there isn't one:

- [PMID:35736449 "The AADAC family comprises five members, including AADAC and four AADAC-like (AADACL1-4) proteins."]
- [PMID:35736449 "all other members of the AADACL protein family, AADACL2, AADACL3, and AADACL4, have so far been only poorly investigated and no functional roles can be concluded"]

The three UniProt `RN` references are all large-scale sequencing (PMID:17974005 German cDNA
consortium, which supplied isoform 2; PMID:16641997 chromosome 3; PMID:15489334 MGC, which
supplied the Ser-186 variant). None assays the protein. Note the campaign rule: `PE 1` means
the protein is *detected*, so the honest statement is that there are no
functional/biochemical data, not that there are no data.

Two genetic associations exist and neither supports a GO annotation:

- Psoriasis exome-indel screen in 32,043 Chinese Han individuals:
  [PMID:31078570 "identified KIAA0319, RELN, NCAPG, ABO, AADACL2, LMAN1, FLG, HERC5, CCDC66, LEKR1, AFF3, ABCG2, ANXA7, SYTL2,GIPR, METTL1, and FYCO1 as unreported genes for psoriasis"]
- SIREN ischemic-stroke GWAS in indigenous Africans:
  [PMID:38317187 "We observed genome-wide significant (P-value < 5.0E-8) SNPs associations near AADACL2 and miRNA (MIR5186) genes in chromosome 3"], with
  [PMID:38317187 "The putative genes near AADACL2, MIR5186, and MIR4458 genes were protective and novel"]

The stroke signal is explicitly *near* the gene, not in it. A skin-expressed gene surfacing
in a psoriasis screen is at least tissue-coherent; a locus association is not a function.

## Family context

AADAC is the characterised member: a liver/intestine enzyme that hydrolyses both amide bonds
of arylacetamide xenobiotics and ester bonds of diglycerides, and it is
[PMID:35736449 "AADAC is a type II membrane glycoprotein, facing with its active side to the lumen of the endoplasmic reticulum (ER)"].
AADACL1/NCEH1/KIAA1363 is the other characterised member and is likewise membrane-anchored:
[PMID:35736449 "KIAA1363 contains a putative N-terminal transmembrane domain consisting of a 23 amino acid"]-long
hydrophobic stretch. The review also notes
[PMID:35736449 "the conserved structural homologies of the catalytic domain of KIAA1363, as well as AADAC to that of HSL"]
(hormone-sensitive lipase) — the GDXG / HSL-like α/β-hydrolase clan that AADACL2 belongs to
per [file:human/AADACL2/AADACL2-uniprot.txt "Belongs to the 'GDXG' lipolytic enzyme family."].

Expression: HPA reports AADACL2 as skin-restricted (`Tissue enriched (skin)`,
"detected in single", 10.1 nTPM in skin) — the most tissue-restricted member of the family
after AADACL4. AADACL3 is also skin/placenta-expressed, so the paralogous cluster looks like a
skin-associated expansion of the AADAC family.

## Three things worth curating

### 1. The activity is real machinery, not a fold-derived label

The campaign's standing warning is that a domain's *name* becomes an activity in GO. The
mirror-image error is to dismiss such a call without checking the residues. Here the residues
are present:
[file:human/AADACL2/AADACL2-uniprot.txt "FT   ACT_SITE        189"], 341 and 371 (Ser-Asp-His),
an oxyanion-hole motif at
[file:human/AADACL2/AADACL2-uniprot.txt "FT   MOTIF           111..113"], a `GDSSG` nucleophile
elbow at 187-191, a conserved 116-338 disulfide, and a PROSITE `PS01174` GDXG-lipase-serine
match. The reciprocal alignment test in
[file:human/AADACL2/AADACL2-bioinformatics/RESULTS.md "Eight of the fifteen sources with annotated active sites map all three residues onto"]
AADACL2's own annotated triad. Those eight are the seven closest sources plus *M. tuberculosis*
LipN at 26.1% identity, and every source that fails lies at 26.5% identity or below, where the
global alignment loses register in the C-terminal half. They include three independently
characterised *M. tuberculosis* carboxylesterases and the 51.6%-identical human paralog AADAC.

That licenses **GO:0017171 serine hydrolase activity**, whose definition is exactly a serine
nucleophile activated by an acid/base proton relay. GOA currently gives AADACL2 only
`GO:0016787 hydrolase activity` and `GO:0003824 catalytic activity` from the mechanism side,
which is a strictly weaker statement than the protein's own feature table supports.

### 2. The PANTHER node placement is inverted, and it affects three genes

From `RESULTS.md` section 5: `GO:0017171` sits only at the ortholog-specific nodes
`PTN002745055` (AADAC) and `PTN002745068` (NCEH1), so AADACL2/3/4 inherit no mechanism term.
What they *do* inherit at the shared family node `PTN009058713` is `GO:0016020 membrane`.
This is backwards with respect to what transfers safely: the catalytic triad is conserved in
all five human members; the N-terminal anchor is not (12 of the 14 reviewed `IPR017157`
entries carry a `TRANSMEM`, 11 of them an explicit type-II signal anchor, and AADACL2 is the
only one whose equivalent segment is annotated as a cleaved signal peptide instead). Moving `GO:0017171` down to
`PTN009058713` and dropping `GO:0016020` from it would correct AADACL2, AADACL3 and AADACL4
in one edit.

### 3. Where I stopped short: the localisation is genuinely unresolved

My first read was "membrane is a paralog artefact; secreted is right". Measurement did not
support that, and this is recorded here so the reasoning is auditable:

- UniProt's cleavage site (after residue 18) puts **His at -1**, which signal peptidase I
  essentially does not accept (-1 is small/neutral A/S/C/G/T in the great majority of sites).
- The hydrophobic core is *more* hydrophobic than AADAC's experimentally confirmed type-II
  signal anchor (peak KD-19 mean 1.94 vs 1.81), and the two N-termini are homologous over the
  whole segment with the same downstream `TP.PDN.EE.W` motif. Hydropathy cannot tell a
  cleaved signal peptide from a signal anchor here.
- HPA's predictor vote does put AADACL2 (and only AADACL2) in the secreted class, but the same
  HPA pipeline **fails to classify AADAC as a membrane protein**, so it cannot be used as
  independent corroboration.
- All four observed peptides lie in the catalytic domain (earliest residue 124). Mass
  spectrometry establishes expression and says nothing about the N-terminal fate.

So both `GO:0005576` and `GO:0016020` are unsupported computational readings of the same
segment, and neither can be accepted or removed on present evidence. Actions: `UNDECIDED` for
all three location rows, with the experiment that would settle it recorded in
`suggested_experiments`. Recording the *contradiction* is the deliverable here; picking a
winner would have been a guess dressed as a finding.

## Isoform note

Isoform 2 (Q6P093-3) replaces residues 47-53 and deletes 54-401, and UniProt flags it as
likely NMD-degraded:
[file:human/AADACL2/AADACL2-uniprot.txt "premature stop codon in the mRNA, leading to nonsense-mediated mRNA"]
decay. It cannot be catalytically active (it stops before Ser189), so no annotation should be
attributed to it. All annotations here concern isoform 1 (Q6P093-1), the MANE-Select product.

## Curiosity, not evidence

The UniProt record carries two DrugBank cross-references, `DB07814 Gibberellic acid` and
`DB07815 Gibberellin A4`. The plant gibberellin receptor GID1 is a derivative of this same
GDXG/HSL-like carboxylesterase clan, so these are almost certainly structure-similarity
mappings rather than any claim about human ligands. Not used for anything in the review.

## Round-1 review follow-ups (PR #2266, approved with five non-blocking suggestions)

All five were taken:

1. The aggregate 8/15 triad figure understated the nucleophile. `results.json` already had the
   per-position data: **all 15 sources align their own catalytic serine onto position 189, and
   14 of 15 carry a Ser there** (the exception is soybean HIDH, whose own nucleophile is Thr —
   and HIDH is the one source that is a dehydratase, not a hydrolase). The 8/15 figure is
   driven entirely by the acid and base drifting out of register below 26.5% identity. Added as
   a table in `RESULTS.md` section 1, computed by the script (`per_target_active_site`), and
   surfaced in the `GO:0017171` MODIFY reason.
2. The `GO:0052689` ACCEPT reason called that term "the best available statement of the core
   function" while `core_functions` uses `GO:0017171`. Reconciled: `GO:0052689` is the most
   informative *activity* statement on the record, but it is inferred from family membership,
   whereas the serine-hydrolase mechanism is evidenced on this protein's own residues and is
   also what survives if AADACL2 prefers amide over ester bonds, as AADAC does.
3. "Mutually exclusive" overstated GO semantics — `GO:0005576` and `GO:0016020` are not
   disjoint (a shed ectodomain can be in both). Narrowed everywhere to what is actually
   claimed: two incompatible readings of one hydrophobic helix, only one of which can describe
   the mature protein.
4. The InterPro2GO `GO:0016787` MODIFY now says where the fix lands — the
   IPR013094→GO:0016787 mapping should *not* change, since a bare alpha/beta-hydrolase-3 match
   warrants nothing more; the correction is a protein-level annotation on AADACL2.
5. Added `PMID:16641997` (chromosome 3 sequencing, UniProt `RN[2]`) to `references:` so the
   "all three UniProt references are large-scale sequencing" claim is self-contained.

> **Items 2 and 4 above are superseded** by the cross-gene adjudication section at the end of
> this file. The reconciliation in item 2 was the wrong way round — `GO:0052689` is now the
> recorded core function — and the "protein-level annotation on AADACL2" framing in item 4
> proposed a term (`GO:0017171`) that one of the row's own donors refutes.

## Actions taken

| term | evidence | action |
|---|---|---|
| GO:0016787 hydrolase activity | IBA | MODIFY → GO:0052689 carboxylic ester hydrolase activity |
| GO:0016020 membrane (`is_active_in`) | IBA | UNDECIDED |
| GO:0003824 catalytic activity | IEA | MODIFY → GO:0052689 carboxylic ester hydrolase activity |
| GO:0005576 extracellular region | IEA | UNDECIDED |
| GO:0016020 membrane (`located_in`) | IEA | UNDECIDED |
| GO:0016787 hydrolase activity | IEA | MODIFY → GO:0052689 carboxylic ester hydrolase activity |
| GO:0052689 carboxylic ester hydrolase activity | IEA | ACCEPT |

(The three MODIFY rows originally proposed `GO:0017171 serine hydrolase activity`; see the
cross-gene adjudication below for why they now all collapse onto `GO:0052689` instead.)

## Cross-gene adjudication of the PTN009058710 `GO:0016787` row (AADACL2 / AADACL3 / AADACL4)

**The defect.** AADACL2, AADACL3 and AADACL4 each carry one `GO:0016787 hydrolase activity`
IBA row from `GO_REF:0000033`, transferred from PANTHER node `PTN009058710`, and the
`WITH/FROM` fields are **byte-identical** across the three records — the same 17 tokens. Three
separate reviews nevertheless reached three different verdicts on that one row:

| gene | PR | verdict as merged |
|---|---|---|
| AADACL2 | #2266 | `MODIFY` → `GO:0017171`, `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH` |
| AADACL4 | #2263 | `MODIFY` → `GO:0052689`, `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH` |
| AADACL3 | #2264 (open) | keep `GO:0016787` as the genuine LCA; replace only as redundant, `EVIDENCE_CIRCULAR_OR_REDUNDANT` |

**How it was settled.** By measurement, not by preference. The shared node audit
`AADACL2-bioinformatics/audit_node_PTN009058710.py` resolves all 17 tokens (16 proteins plus
the tree node itself) and reads each donor's chemistry off its own EC numbers *and* its own
curated GO annotations classified by fetched ontology ancestry, and its nucleophile off its own
`ACT_SITE` features. Results in `NODE_PTN009058710.md`:

```
GO:0016787 hydrolase activity:                  TRUE 16, FALSE 0, UNDETERMINED 0
GO:0052689 carboxylic ester hydrolase activity: TRUE 14, FALSE 2, UNDETERMINED 0
GO:0017171 serine hydrolase activity:           TRUE 15, FALSE 1, UNDETERMINED 0
```

Neither refinement is true of the whole node, and the two refutations lie on **different
axes**, so neither can be rescued by choosing the other:

- the bond-type axis is blocked by the two kynurenine formamidases, mouse Afmid (`Q8K4H1`,
  `GO:0004061` by IMP) and yeast BNA7 (`Q04066`, `GO:0004061` by IDA), both EC 3.5.1.9. Their
  term sits under `GO:0016810` (C–N bonds), a *sibling* of the ester branch.
- the mechanism axis is blocked by soybean HIDH (`Q5NUF3`), whose nucleophile-elbow residue is
  **Thr164**, against `GO:0017171`'s definition demanding "a catalytic triad consisting of a
  serine nucleophile".

Because `GO:0016788` and `GO:0016810` are siblings whose only common ancestor below
`GO:0003824` is `GO:0016787`, the term PAINT chose is the **exact LCA** of its donor set.
So **AADACL3's reading was the correct one**, and all three genes are now harmonised to it:
`MODIFY` → `GO:0052689` on redundancy grounds only, `root_cause:
EVIDENCE_CIRCULAR_OR_REDUNDANT`, and **no** `failure_modes`. `GRANULARITY_MISMATCH` is dropped
because it presupposes donors that agree with a term still sitting above them; here the donors
disagree and the parent is their LCA, so there is no granularity defect at all.

**Two premises that were wrong and mattered.**

1. Both merged reviews leaned on soybean HIDH being "not a hydrolase at all but a dehydratase",
   which would have threatened even `GO:0016787`. It is bifunctional: `GO:0033987` dehydratase
   by IDA **and** `GO:0106435 carboxylesterase activity` by IDA, EC 4.2.1.105 **and** EC
   3.1.1.1. So it refutes the *serine* term only, and the ester term is blocked by the two
   formamidases instead. This sentence in `RESULTS.md` was corrected.
2. Yeast BNA7 does resolve — `xref:sgd-S000002836` → `Q04066`, `ACT_SITE 110` labelled
   "Nucleophile" by UniProt and reading as Ser. The AADACL3 audit reached it through an
   Alliance record and reported the nucleophile unresolved, undercounting the serine tally;
   with BNA7 in, it is 15 of 16 serine, one threonine.

**Where the mechanism term does belong.** `GO:0017171` is not wrong about this family, it is
attached to the wrong node. At the *family* node `PTN009058713` — whose `WITH/FROM` names only
human AADAC, mouse Aadac and mouse Nceh1 — the term is true of every donor PAINT cites there
and held by **IDA** in all three of them, and all three are `IPR017157` members. All three blockers at the deep
node lie *outside* `IPR017157`. So the PAINT recommendation is a **node move**
(`PTN002745055`/`PTN002745068` → `PTN009058713`), not a term change on the row, and it is now
stated that way in `knowledge_gaps` and `suggested_questions` in AADACL2 and in
`suggested_questions` in AADACL4.

**Knock-on change to `core_functions`.** AADACL2's core molecular function moves from
`GO:0017171` to `GO:0052689`, matching AADACL4 and AADACL3, which have identical catalytic
registers and the same subfamily signature. `GO:0017171` remains true of AADACL2 on its own
residues and is stated as such in the `core_functions` description, but no existing row carries
it and it is pursued as the node move above rather than asserted as a second activity. The
`GO:0003824` ARBA row's replacement was moved to `GO:0052689` for the same reason: all three
general molecular-function rows on this record now collapse onto the one specific term the
record actually has.

### Round-2 corrections to the adjudication (PR #2286 review)

Five factual/rhetorical items, all conceded after checking:

1. **The three-gene equality was asserted but only measured for two.** `genes/human/AADACL3/` is
   not in the tree while #2264 is open, so the first version of the audit recorded
   `genes_sharing_the_row: ["AADACL2","AADACL4"]` while the prose claimed all three. Fixed by
   *measuring* rather than softening: the audit now fetches the audited row's `WITH/FROM` set per
   accession from QuickGO for **Q6P093, Q5VUY0 and Q5VUY2**, cross-checks it against the committed
   TSVs wherever both exist, and treats a gene covered by neither source as a hard error. AADACL3's
   set comes back as the **same 17 tokens**, so the claim now rests on measurement for all three.
   The script's missing-TSV path also prints the absence and its reason instead of returning a
   silent `{"present": False}`, which is what its own docstring had promised.
2. **The family node is IDA-supported by all three donors, not two.** Human AADAC (`IBA,IDA,IEA`),
   mouse Aadac (`IBA,IDA,IEA,ISO`) and mouse Nceh1 (`IBA,IDA`) all hold `GO:0017171`
   experimentally. The audit now records this per member (`family_node.mechanism_term_support`), so
   the node-move recommendation is stronger than first stated.
3. **The Thr164 call is a fold-position inference and the whole verdict turns on it.** UniProt
   describes HIDH's `ACT_SITE 164` as **"Proton acceptor"** (`ECO:0000305`), not as a nucleophile —
   unlike Afmid and BNA7, where the nucleophile *is* labelled. Two things now carry the call
   instead of the label: the **elbow pentapeptide**, added to the audit for every donor, shows 15 of
   16 reading G-x-S-x-G (`GDSAG` ×12, `GQSAG`, `GHSAG`, `GHSVG`) while HIDH alone reads **`GETSG`**;
   and a **sensitivity analysis** shows the verdict is robust — downgrading HIDH to undetermined
   still leaves `GO:0017171` untrue of every donor, and downgrading *every* positionally-inferred
   nucleophile leaves it supportable for only the 2 donors UniProt labels explicitly.
4. **"All fifteen donors place their catalytic serine on position 189" contradicted the threonine
   donor.** It is the catalytic *nucleophile* that aligns on 189 in 15 of 15, with a serine there in
   14 of 15. Corrected in the row summary and in `core_functions`.
5. **The `core_functions` rationale leaned on cross-gene consistency.** It now leads with the
   evidence that actually carries `GO:0052689` — `IPR017157` is a family-specific signature over
   almost the whole chain, and every biochemically characterised family member is a carboxylic ester
   hydrolase — with the paralog consistency noted afterwards rather than doing the work.

**One item held, with the reasoning recorded.** The reviewer notes that dropping
`GRANULARITY_MISMATCH` goes beyond the enum's literal definition ("parent term is true but
uninformative"), which would fit this row. Held, because `failure_modes` is documented as the
*biological shape of a propagation issue* and this propagation has none: the parent is
uninformative because the donors are heterogeneous, not because the transfer could have been more
specific. That is the rule this campaign already adopted ("ask whether the term is the LCA of its
donors; `GRANULARITY_MISMATCH` is only apt when the donors agree and the term still sits above
them"). The reasoning is now stated inline in both hydrolase rows rather than left implicit, and
the schema's enum description is flagged as worth clarifying so the two readings stop being
interchangeable.

### Round-3 tidy-up (the five optional items from the #2286 review)

All five taken; none changed a conclusion.

1. The `GRANULARITY_MISMATCH` argument was stated twice in the same `reason` field — the round-1
   sentence survived alongside the fuller round-2 paragraph. Round-1 sentence dropped, and the
   `IPR013094` IEA row now cross-references the argument on the IBA row instead of repeating the
   whole paragraph verbatim.
2. `RESULTS.md` still carried the self-contradicting sentence the YAML had already fixed ("places
   its own catalytic **serine** on position 189, and fourteen of them carry a serine there").
   Corrected at source to "catalytic **nucleophile**", and the `supporting_text` that quotes it
   moved with it — the fix had to be made in both places or the quote would have gone stale.
3. "True of every donor **at** the family node" was an inference stated as a measurement: the
   family donor set is the `WITH/FROM` of the `GO:0016020` row, and `PTN009058713`'s membership is
   never enumerated because the PANTHER tree is not fetched. Reworded throughout to "every donor
   PAINT **cites** at that node", with `membership_enumerated: false` recorded in the audit JSON.
   The independently measured half of the argument is the `IPR017157` split, which is per donor.
4. Two script infelicities: the `uncovered` guard could not fire (`from_quickgo` is built from
   `PARALOG_ACCESSIONS`, which covers all three genes), so it is now an assertion documenting the
   invariant — it fires if a gene is ever added to `GENES` without an accession; and
   `family_mechanism` silently skipped an unresolvable family-row token, which now dies, matching
   what `query_for` already refuses to do.
5. Two `supporting_text` entries quoted the same file with one a strict prefix of the other, the
   longer starting mid-bold. Reduced to the single clean quote.

### Round-4: the same staleness, in the file that flagged it

The reviewer found that `AADACL2-bioinformatics/RESULTS.md` still carried "true of every donor at
`PTN009058713` and IDA-supported by **two** of them" — a sentence this PR itself added, left
un-updated when round 2 changed "two" to "three" in six other places and round 3 changed "every
donor **at**" to "every donor PAINT **cites** at". So both conceded items were unapplied in one
sentence, in the very file whose stale-quote problem was item 9. Patching named line numbers is
what let it survive twice.

Fixed by **sweeping instead of patching**: a single script now greps all seven changed files for
every `IDA … two of them` variant and every unqualified `every donor at the family node`, applies
the corrections idempotently, and then **re-greps and hard-fails** if any occurrence survives.
That found four more instances beyond the one reported — the round-1 sentence in *both* notes
files, the "Not two of three: every donor at the family node" line in `NODE_PTN009058710.md`, and
two places in the AADACL4 review that round 3's line-targeted edit had missed. Lesson for the
campaign log: when a phrase is corrected, grep the whole changed file set for the phrase, not for
the line.

Also from the same review: the `uncovered` guard is now an explicit `if … die()` rather than an
`assert`, since `python -O` strips assertions and the guard is the mechanism by which the
"no gene drops out of the equality test" promise is kept.
