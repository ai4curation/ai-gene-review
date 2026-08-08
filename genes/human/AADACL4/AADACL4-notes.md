# AADACL4 (Q5VUY2) — review notes

Human arylacetamide deacetylase-like 4, HGNC:32038, chromosome 1p36.21, 407 aa.
Reviewed for the PAINT + affinage campaign.

Paralog map (verified against NCBI Gene and UniProt, since it matters for how the IBA
donors are read): AADAC (3q25.1), AADACL2 (3q25.1) and NCEH1/AADACL1 (3q26.31) are on
chromosome 3; AADACL3 and AADACL4 are adjacent at 1p36.21. AADACL3 is the closest paralog -
both 407 residues, same active-site positions 193/347/377, 55% identity, all three figures
recorded in `AADACL4-bioinformatics/results.json` from live UniProt data - and is being
reviewed separately.

## Bottom line

AADACL4 is a genuinely dark gene: no publication has assayed it, and UniProt classifies
it `PE   3: Inferred from homology;` — there is not even a protein-level detection to
build on, let alone a biochemical activity. Its entire GO record (5 rows, all IBA/IEA) is
homology-derived. The single question that decides whether that record is defensible is
whether the GDXG catalytic machinery is intact, and it is: Ser193–Asp347–His377 plus an
HGG oxyanion hole. So the correct outcome is neither "accept the esterase because the
domain is called an esterase domain" nor "fold without function" — it is: keep the
specific ester-hydrolase term, retire the redundant general `hydrolase activity` rows,
and leave the location at the general `membrane` level because the evidence genuinely
does not resolve further.

## What is actually known

### Nothing functional has been published

The only review that discusses AADACL4 at all places it explicitly among the
uncharacterised half of the mammalian metabolic serine hydrolases, in a section headed
"Representative examples of poorly characterized hydrolases"
[PMID:21696217 "AADAC is highly homologous to several related lipases, AADACL1, 2, and 4,
the latter two of which remain completely unannotated."] and
[PMID:21696217 "Candidate endogenous substrates, selective inhibitors, or knockout mice
have not, to our knowledge, been described for AADAC or the related enzymes AADACL2 and
AADACL4."]. The `AADACL1` in that sentence is NCEH1/KIAA1363, so the review is naming the
AADAC/NCEH1 clade AADACL4 belongs to.

The affinage deep-research record is empty (`n_discoveries: 0`, `citation_count: 0`, and no
`self_evaluation_pairwise` score — the trust gates were clear only for want of anything to gate). Following the campaign rule that an empty affinage record is
not evidence that literature is absent, I checked independently:

- UniProt cites exactly one reference for this entry, the chromosome 1 sequencing paper
  [PMID:16710414], i.e. the entry rests on genome annotation alone.
- Europe PMC has 53 records mentioning "AADACL4"; a title/abstract-restricted search
  returns 2, both livestock/tumour GWAS or signature papers where the gene is one locus
  among many. Full-text mentions in the four papers I pulled are: the Chem Rev review
  above; a serine-hydrolase inhibitor screen where the gene appears only in supplementary
  tables [PMID:21084632]; a meibomian-gland transcriptome where the mention is likewise in
  a supplementary table (the cached full text has no "AADACL4" hit); and one avian study,
  discussed below.

So the "no primary literature" conclusion here is a conclusion I checked, not one I
inherited from a silent provider record.

### The catalytic machinery is complete

UniProt annotates `ACT_SITE 193/347/377` (ECO:0000250 from mouse Nceh1 Q8BLF1) and a
`MOTIF 119..121` described as
[file:human/AADACL4/AADACL4-uniprot.txt "Involved in the stabilization of the negatively"]
charged intermediate by the formation of the oxyanion hole. I verified these against the
sequence and against the family rather than taking the propagated positions on trust
(`AADACL4-bioinformatics/analyze_catalytic_machinery.py`):

- [file:human/AADACL4/AADACL4-bioinformatics/RESULTS.md "Triad residues in sequence order:
  **SDH**"] — the annotated positions really are Ser, Asp, His.
- [file:human/AADACL4/AADACL4-bioinformatics/RESULTS.md "Nucleophile elbow pentapeptide
  around Ser193: `GESVG`"] — the nucleophile sits in a canonical G-x-S-x-G elbow.
- [file:human/AADACL4/AADACL4-bioinformatics/RESULTS.md "Residues 119-121: `HGG` (the GDXG
  oxyanion-hole motif)"].
- All 7 relatives above the 31.3% identity cut (AADACL3, AADACL2, human/rat/mouse AADAC,
  human/mouse NCEH1) project their own annotated triads onto exactly residues 193/347/377 of
  AADACL4 by global alignment, with matching residue identity — 7 of 7. The cut is applied to
  the computed identity rather than to a hand-labelled set, and the run aborts if any panel
  member falls within 0.75 points of it; the numeric cut reproduces AADAC-family membership
  exactly. Placing it at 31.0 did abort, because M. tuberculosis NlhH sits at 30.3%.

This is what makes the ester-hydrolase call a statement about an intact active site rather
than a fold name transcribed into an activity. It also closes off the mirror error: there
is no lost triad residue and no displaced elbow to point at, so "fold without function" is
not available as a reading either.

### Why the phylogenetic annotation stopped at `hydrolase activity`

The `GO:0016787` IBA came from PANTHER node PTN009058710. Resolving all 17 WITH/FROM
tokens shows a node that reaches back past the plant/fungal/bacterial split and is
functionally heterogeneous: 9 ester hydrolases (EC 3.1.-), **2 arylformamidases**
(mouse Afmid Q8K4H1 and yeast BNA7 Q04066, EC 3.5.1.9 — an amide bond, not an ester), a
2-hydroxyisoflavanone dehydratase that is also classified as a **lyase** (soybean HIDH
Q5NUF3, EC 4.2.1.105), and 4 members with no EC assigned. HIDH is the sharpest case: its
annotated nucleophile is a **threonine**, not a serine. At that depth `hydrolase activity`
is the correct last-common-ancestor call. The general term is therefore not an
over-generalisation error by the PAINT curator — it is simply less informative than what
AADACL4's own subfamily signature (InterPro IPR017157 / PIRSF037251,
arylacetamide deacetylase) supports, and it is redundant with the `GO:0052689` row that
signature already produces on the same protein.

### The membrane call is prediction-only, and deliberately unrefined

UniProt says [file:human/AADACL4/AADACL4-uniprot.txt "SUBCELLULAR LOCATION: Membrane
{ECO:0000305}; Single-pass type II"] membrane protein, resting on
`TRANSMEM 5..25 ECO:0000255` [file:human/AADACL4/AADACL4-uniprot.txt "Helical;
Signal-anchor for type II membrane protein"]. Two things are worth recording.

First, within a set of paralogs that share the catalytic register exactly, UniProt's
N-terminal calls diverge and all of them are ECO:0000255 sequence-analysis predictions:

| Protein | N-terminal call | Location | PE |
|---|---|---|---|
| AADACL4 (Q5VUY2) | TRANSMEM 5-25, signal anchor | Membrane | 3 |
| AADACL3 (Q5VUY0) | none annotated | none | 2 |
| AADACL2 (Q6P093) | SIGNAL 1-18 (cleaved) | Secreted | 1 |
| AADAC (P22760) | TRANSMEM 6-23, signal anchor | ER membrane / microsome | 1 |
| NCEH1 (Q6PIU2) | TRANSMEM 5-25, signal anchor | Cell membrane / microsome | 1 |

AADACL3 has a comparably hydrophobic N-terminal segment (Kyte–Doolittle peak 2.5 starting
at residue 6, versus 2.8 at residue 6 for AADACL4) yet carries no feature and no
subcellular location at all. That is an internal inconsistency in the family's UniProt
annotation, and it is worth reporting upstream. It cannot be settled by hydropathy — mean
hydropathy does not discriminate a cleaved signal peptide from an uncleaved type-II signal
anchor, which is exactly why all these calls are ECO:0000255, and no licensed predictor
(SignalP/Phobius/DeepTMHMM) was run for this review.

Second, the `GO:0016020` IBA's own donors disagree about which membrane:
[file:human/AADACL4/AADACL4-bioinformatics/RESULTS.md "Distinct specific locations across
the donors: **4**"] — mouse Aadac and human AADAC are ER/microsomal membrane, mouse Nceh1
is plasma membrane. So `membrane` is the correct call at that node too; refining it to
`endoplasmic reticulum membrane` would mean picking one donor over the other with no
AADACL4 data to justify it. Both membrane rows (the IBA and the UniProt-SubCell IEA) make
the same claim by different routes and should both stay at this level.

A concrete way to test the topology does exist: the two predicted N-glycosylation sites
`CARBOHYD 168` and `CARBOHYD 269` both lie in the predicted lumenal/extracellular domain,
so glycan occupancy would confirm a type-II orientation, and its absence would argue for a
cytosolic or soluble protein.

### Expression and tractability

- [file:human/AADACL4/AADACL4-uniprot.txt "HPA; ENSG00000204518; Tissue enhanced
  (choroid)."]
- [file:human/AADACL4/AADACL4-uniprot.txt "Bgee; ENSG00000204518; Expressed in omental fat
  pad and 34 other cell types or tissues."]
- [file:human/AADACL4/AADACL4-uniprot.txt "Pharos; Q5VUY2; Tdark."]
- BioGRID-ORCS: 7 hits in 1138 CRISPR screens — no coherent fitness signal.
- IntAct holds exactly one record for Q5VUY2: an anti-tag co-immunoprecipitation
  association with a **rabies virus phosphoprotein** (miscore 0.35, source
  doi:10.1016/j.bsheal.2020.07.011, a study about ABCE1, with an unassigned PubMed id in
  IntAct). AADACL4 is an incidental hit in a viral-bait pulldown. GOA carries no
  `GO:0005515 protein binding` row, which is the right call.

### One non-human lead, flagged rather than used

Chicken `AADACL4B` is among the genes upregulated during keratinocyte differentiation and
enriched in interscale epidermis [PMID:34997067 "Many of the genes upregulated during
differentiation of back skin keratinocytes28, such as KRT9L4, LOR1, KRT9L3, BDH1L, EDQM2,
SPTSSB, EDQM1, AADACL4B, LIPML2, and ELOVL4 (Table 2) were enriched in interscale versus
scale epidermis."]. A skin-barrier lipid-ester role would fit an intact GDXG hydrolase, and
AADACL2 — the secreted paralog — is a skin gene (UniProt Q6P093 cross-references
`HPA; ENSG00000197953; Tissue enriched (skin).`). But the `B` suffix signals a
bird-specific duplicate, the orthology to human AADACL4 is not established here, and this
is mRNA co-expression in chicken. It goes in `suggested_questions`, not into any
annotation.

## GOA rows and the decisions taken

All 5 rows of `AADACL4-goa.tsv`, in file order.

| # | Term | Ev | Reference | WITH/FROM | Action |
|---|---|---|---|---|---|
| 1 | GO:0016787 hydrolase activity (enables) | IBA | GO_REF:0000033 | 17 tokens, node PTN009058710 | MODIFY → GO:0052689 |
| 2 | GO:0016020 membrane (is_active_in) | IBA | GO_REF:0000033 | mouse Aadac, mouse Nceh1, human AADAC, node PTN009058713 | ACCEPT |
| 3 | GO:0016020 membrane (located_in) | IEA | GO_REF:0000120 | ARBA00028763, IPR017157, SL-0162 | ACCEPT |
| 4 | GO:0016787 hydrolase activity (enables) | IEA | GO_REF:0000002 | InterPro:IPR013094 (Abhydrolase_3) | MODIFY → GO:0052689 |
| 5 | GO:0052689 carboxylic ester hydrolase activity (enables) | IEA | GO_REF:0000002 | InterPro:IPR017157 (Arylacetamide_deacetylase) | ACCEPT |

Both `MODIFY`s are granularity calls, not corrections: `GO:0052689` is a descendant of
`GO:0016787` via `GO:0016788` (confirmed from the QuickGO `is_a` ancestor list), the specific
term is already on the protein from the subfamily-level signature, and nothing about the
general rows is biologically wrong. *(As first written, both were recorded as
`root_cause: TERM_SCOPING_PROBLEM` with `failure_modes: [GRANULARITY_MISMATCH]`. Corrected when
the three paralogs were harmonised: they now carry `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT`
with no failure mode, because the donor set is heterogeneous, so the parent is its LCA and there
is no granularity defect — the replacement rests on redundancy alone.)*

Two things checked so the MODIFYs are not overstated. Neither `GO:0016787` nor `GO:0016020`
is in `gocheck_do_not_annotate` - QuickGO reports `usage: Unrestricted` for both - so no
annotation rule is being violated and the case is purely one of redundancy and
informativeness. And the replacement term is a claim about what AADACL4's annotation set
should contain, not a claim that node PTN009058710 could support `GO:0052689`: it could not,
which is exactly why the IBA landed on the general parent. The specific term has to come
from the subfamily signature (or from a deeper PANTHER node, if PAINT chose to annotate one).

Nothing was removed. No new term is proposed: `GO:0052689` already says exactly what the
evidence supports, and a substrate-level child would not be licensed by homology alone.

## WITH/FROM resolutions (for the record)

`GO:0016787` IBA, 17 tokens:

| Token | Resolved | Identity |
|---|---|---|
| AGI_LocusCode:AT1G49660 | Q9FX94 | A. thaliana probable carboxylesterase 5 |
| AGI_LocusCode:AT3G48690 | Q9SMN0 | A. thaliana probable carboxylesterase 12 |
| AGI_LocusCode:AT5G15860 | Q94AS5 | A. thaliana isoprenylcysteine α-carbonyl methylesterase |
| AGI_LocusCode:AT5G23530 | Q9LT10 | A. thaliana probable carboxylesterase 18 |
| MGI:MGI:1915008 | Q99PG0 | mouse Aadac, arylacetamide deacetylase (EC 3.1.1.3) |
| MGI:MGI:2443191 | Q8BLF1 | mouse Nceh1, neutral cholesterol ester hydrolase 1 |
| MGI:MGI:2448704 | Q8K4H1 | mouse Afmid, kynurenine formamidase (EC 3.5.1.9) |
| PANTHER:PTN009058710 | — | the ancestral node itself |
| RGD:631440 | Q9QZH8 | rat Aadac (EC 3.1.1.3) |
| SGD:S000002836 | Q04066 | yeast BNA7, kynurenine formamidase (EC 3.5.1.9) |
| UniProtKB:P22760 | P22760 | human AADAC (EC 3.1.1.3) |
| UniProtKB:P23872 | P23872 | E. coli Aes, acetyl esterase |
| UniProtKB:P71668 | P71668 | M. tuberculosis LipI esterase |
| UniProtKB:P95125 | P95125 | M. tuberculosis LipN carboxylic ester hydrolase |
| UniProtKB:P9WK87 | P9WK87 | M. tuberculosis NlhH carboxylesterase |
| UniProtKB:Q5NUF3 | Q5NUF3 | soybean HIDH, 2-hydroxyisoflavanone dehydratase (EC 4.2.1.105 + 3.1.1.1), Thr nucleophile |
| UniProtKB:Q9HTI0 | Q9HTI0 | P. aeruginosa PA2949, probable lipolytic enzyme |

`GO:0016020` IBA, 4 tokens: MGI:MGI:1915008 → Q99PG0 (ER membrane); MGI:MGI:2443191 →
Q8BLF1 (cell membrane); UniProtKB:P22760 (ER membrane); PANTHER:PTN009058713 (node).

These resolutions are not taken on trust: `analyze_catalytic_machinery.py` checks each
non-PANTHER token back against the resolved entry's own UniProt cross-references (MGI, RGD,
SGD, Araport, or accession equality) before it reports anything, and a mismatch aborts the
run. 19 token resolutions across the two IBA rows pass. I confirmed the guard actually bites
by temporarily mis-mapping `RGD:631440` to `Q8BLF1`, which exits non-zero with
`FATAL: token RGD:631440 was resolved to Q8BLF1, but that entry's RGD cross-references are []`.

`GO:0016020` IEA, 3 tokens: `ARBA:ARBA00028763` and `UniProtKB-SubCell:SL-0162` are the
UniProt automatic-annotation and controlled-vocabulary handles for the `Membrane`
subcellular-location line; `InterPro:IPR017157` is the arylacetamide-deacetylase family
signature. All three trace back to the same ECO:0000305 curator inference over an
ECO:0000255 topology prediction.

Neither IBA row is self-referential: PTN009058710 and PTN009058713 are ancestral nodes and
Q5VUY2 does not appear in either WITH/FROM list. Note also
[file:human/AADACL4/AADACL4-uniprot.txt "PAN-GO; Q5VUY2; 0 GO annotations based on
evolutionary models."] — the PAN-GO human reference-genome effort records no
evolutionary-model annotation for this protein, while GOA carries two GO_Central IBA rows.
That discrepancy is raised in `suggested_questions` rather than being resolved here.

## Process notes

- `just fetch-gene human AADACL4` seeded 5 GOA rows and 3 GO_REF stubs; no PMIDs were
  seeded, so `just fetch-gene-pmids` found nothing and all four literature references were
  located and fetched by hand.
- deepsig/tmhmm were considered for the signal-anchor question and dropped: deepsig needs a
  model checkout that is not appropriate to vendor into this repo, and tmhmm.py failed to
  build. Rather than substitute a weaker method silently, the limitation is stated in
  `RESULTS.md` and the question is moved to `suggested_experiments`.
- `RESULTS.md` is generated by the script and contains no hand edits; re-running it
  reproduces the committed file.

## Cross-gene adjudication of the PTN009058710 `GO:0016787` row (AADACL2 / AADACL3 / AADACL4)

**The defect.** AADACL2, AADACL3 and AADACL4 each carry one `GO:0016787 hydrolase activity` IBA
row from `GO_REF:0000033`, transferred from PANTHER node `PTN009058710`, and the `WITH/FROM`
fields are **byte-identical** across the three records — the same 17 tokens. Three separate
reviews nevertheless reached three different verdicts on that one row:

| gene | PR | verdict as merged |
|---|---|---|
| AADACL4 | #2263 | `MODIFY` → `GO:0052689`, `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH` |
| AADACL2 | #2266 | `MODIFY` → `GO:0017171`, `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH` |
| AADACL3 | #2264 (open) | keep `GO:0016787` as the genuine LCA; replace only as redundant, `EVIDENCE_CIRCULAR_OR_REDUNDANT` |

**How it was settled.** By measurement. The shared node audit
`genes/human/AADACL2/AADACL2-bioinformatics/audit_node_PTN009058710.py` resolves all 17 tokens
(16 proteins plus the tree node itself) and reads each donor's chemistry off its own EC numbers
*and* its own curated GO annotations classified by fetched ontology ancestry, and its nucleophile
off its own `ACT_SITE` features. It lives in the AADACL2 folder because it is one row shared by
three genes and is audited once; results are in `NODE_PTN009058710.md`:

```
GO:0016787 hydrolase activity:                  TRUE 16, FALSE 0, UNDETERMINED 0
GO:0052689 carboxylic ester hydrolase activity: TRUE 14, FALSE 2, UNDETERMINED 0
GO:0017171 serine hydrolase activity:           TRUE 15, FALSE 1, UNDETERMINED 0
```

Neither refinement is true of the whole node, and the two refutations lie on **different axes**:
the bond-type axis is blocked by the two kynurenine formamidases (mouse Afmid `Q8K4H1`,
`GO:0004061` by IMP; yeast BNA7 `Q04066`, `GO:0004061` by IDA — both EC 3.5.1.9, both on the
`GO:0016810` C–N branch, a sibling of the ester branch), and the mechanism axis by soybean HIDH
(`Q5NUF3`, nucleophile-elbow residue **Thr164**). Since `GO:0016788` and `GO:0016810` are
siblings whose only common ancestor below `GO:0003824` is `GO:0016787`, PAINT's term is the
**exact LCA** of its donors.

So **AADACL3's reading was the correct one.** AADACL4's *replacement term* was already right;
its *classification* was not. All three genes now use `MODIFY` → `GO:0052689` on redundancy
grounds only, with `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT` and **no** `failure_modes`.
`GRANULARITY_MISMATCH` is dropped because it presupposes donors that agree with a term still
sitting above them; here the donors disagree and the parent is their LCA, so there is no
granularity defect to record. The same change is applied to the `IPR013094` IEA row, whose fold
signature is likewise correctly scoped and merely redundant on this record.

**One premise that was wrong and mattered.** This review described soybean HIDH as "a
2-hydroxyisoflavanone dehydratase also classified as a lyase", implying it is not an ester
hydrolase. It is bifunctional: `GO:0033987` dehydratase by IDA **and** `GO:0106435
carboxylesterase activity` by IDA, EC 4.2.1.105 **and** EC 3.1.1.1. So HIDH does not block
`GO:0052689` at all (the two formamidases do) and does not threaten `GO:0016787` either; it
refutes only the serine mechanism term. `AADACL4-bioinformatics/RESULTS.md` already classified
it correctly as "ester hydrolase (EC 3.1.-) + lyase (EC 4.-)" and already said the general term
is "the correct last-common-ancestor call" — it was the review's `propagation_review` that
disagreed with its own analysis file.

**Where the mechanism term does belong.** `GO:0017171` is not wrong about this family, it is
attached to the wrong node. At the *family* node `PTN009058713` — whose `WITH/FROM` names only
human AADAC, mouse Aadac and mouse Nceh1 — it is true of every donor PAINT cites there and held
by **IDA** in all three of them, and all three are `IPR017157` members, while all three blockers at the deep node
lie *outside* `IPR017157`. The recommendation is therefore a **node move**
(`PTN002745055`/`PTN002745068` → `PTN009058713`), added to `suggested_questions` here and to
`knowledge_gaps` + `suggested_questions` in AADACL2, naming all three affected genes once.

**`supporting_entities` drift.** The audited row listed 5 of the 17 `WITH/FROM` tokens. It now
lists all 17, built from `AADACL4-goa.tsv` with an assertion in the fix script rather than by
hand, which is also what makes the "byte-identical across three genes" claim checkable from the
file.

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

### Round-5: retiring the divergence statements this harmonisation made false

Extending the harmonisation to AADACL3 invalidated every statement in the three reviews that
described them as disagreeing — and the round-4 sweep grepped for the `two of them` phrasings but
not for those, which is how they survived a round.

- **AADACL3's `suggested_questions`** said the merged AADACL2 review resolves the same row as
  `MODIFY → GO:0017171` with `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH`, that "both cannot be
  right about one row", and that "**PR #2266** needs a follow-up to settle it". None of that
  survives: AADACL2 now carries AADACL3's own verdict. Rewritten to ask PAINT only where the
  mechanism term should sit — the question that is genuinely still open — while keeping the
  merges-two-existing-rows argument, which is what settled the matter.
- **AADACL2's and AADACL4's row reasons** motivated the schema request with "since AADACL3's review
  reaches the same LCA conclusion while keeping the mode on the literal reading". That divergence
  no longer exists either. The request stands but the justification changes: all three paralogs now
  encode the row on the propagation-shape reading, which the enum text does not itself state, so
  the convention is carried by argument rather than by the schema.
- **The shared audit's "Why this audit exists"** section is explicitly marked *historical*, with a
  closing "Settled outcome" paragraph, so the one remaining mention of `TERM_SCOPING_PROBLEM`
  cannot be read as a live claim.
- **AADACL3's earlier conflict section** (in `AADACL3-notes.md`) is rewritten in the past tense
  with the resolution stated up front, rather than opening "This review now conflicts with the
  merged AADACL2 review … a curator reading both files today gets contradictory advice".
- **AADACL3's 13-of-14 serine count** now carries the pointer to the shared audit's 15 of 16 *at
  the place the count is stated* (`AADACL3-ai-review.yaml`, the analysis `review_notes`), not only
  in a `propagation_review` comment and a reference entry elsewhere in the file.

### The automation, which is the actual fix

Five items on this PR (9, 13, 17, 18, 22) were the same defect: a claim corrected in one place and
left standing in another, twice in a file that recorded the lesson. Round 5's own bullet asserted
two of these fixes that the tree did not contain. Being more careful demonstrably does not work, so
the checks are now a committed script:

`genes/human/AADACL2/AADACL2-bioinformatics/check_paralog_agreement.py`

It enforces two things across **AADACL2, AADACL3 and AADACL4** — the reviews, the notes files and
the audit prose:

1. **the agreement invariant** — for each of the six `GO:0016787` rows: `MODIFY` →
   `GO:0052689`, `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT`, no `GRANULARITY_MISMATCH`,
   `supporting_entities` equal to that gene's own GOA `WITH/FROM` column, one shared 17-token set
   across all three genes, `core_functions` molecular function `GO:0052689`, and the shared audit
   cited;
2. **the stale-claim greps** — no live `TERM_SCOPING_PROBLEM`, "both cannot be right", "needs a
   follow-up", `IDA … two of them`, unqualified "every donor at the family node", "13 of 14"
   without a superseding pointer, or "not yet in the tree", in *any* of those files. Text
   explicitly marked historical is exempt, and the exemption is itself checked.

All **eleven** guards were verified by **deliberately breaking them**: `--self-test` copies the
tree to a temporary directory, applies one mutation at a time, and requires each to be caught. That
paid for itself immediately — the first run reported `superseding pointer removed from a count:
NOT caught`, and the cause was the *mutation*, which only reworded a lead-in and left the pointer
inside the search window, so nothing was actually broken and the guard was right to stay silent.
Reading the guard would not have found that; only trying to break it did. The mutation now deletes
the whole clause and raises if its target text has moved, so the self-test cannot silently pass
later.

Two design points worth recording. Curator-facing text (reviews, the audit prose, `RESULTS.md`) is
grepped wholesale, but **notes files are journals** — a journal recording "X was wrong, now fixed"
necessarily contains X, so a blanket grep is unusable there. They are scanned paragraph by
paragraph and a stale phrase is allowed only where the paragraph, or a marker at the top of its
section, marks the passage retrospective; an unqualified stale sentence in running prose fails,
which is exactly the shape of the AADACL3 section that survived four rounds. And the section-level
exemption requires a *strong* marker (superseded, historical, since resolved …) rather than any
past tense, so appending a new live claim to an old section is not laundered by its header — there
is a self-test mutation for precisely that.

Integration with `just` is out of scope for a gene PR, so it runs as
`uv run --no-project --with pyyaml python check_paralog_agreement.py` and is documented in the
audit file.

Generalisable lesson, and the reason this is a script rather than a resolution: **when a change
makes a claim false, grep for the claim, not for the sentence you remember writing** — and when the
change is "these two now agree", the claims to hunt are the ones asserting that they do not.
