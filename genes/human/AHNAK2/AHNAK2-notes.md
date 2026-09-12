# AHNAK2 (human, Q8IVF2) — review notes

Journal for the GO annotation review. Provenance is recorded inline as
`[PMID:x "quote"]`. The reproducible checks live in `AHNAK2-bioinformatics/`
and their findings are written up in that folder's `RESULTS.md`.

## The one-line finding

Of the 13 GOA rows on AHNAK2, **two** cite an experiment reported for AHNAK2 in
a source anyone can read (HPA immunofluorescence: cytosol, plasma membrane).
Five come from a paper whose public abstract is entirely about the paralogue
AHNAK, three are phylogenetic transfers whose donors are periaxin and AHNAK, and
three are electronic. Meanwhile ten of the eleven AHNAK2-relevant papers I read
produced **no** GO annotation on AHNAK2 at all, including a 1.75 Å crystal
structure of its only folded domain. The diagnosis is a **coverage** defect, not
an over-annotation defect — although four rows are over-reaching and are marked
as such.

## Protein

5795 aa, `PE 1: Evidence at protein level`. One folded domain: a PDZ at
112–193 (`FT DOMAIN ... /note="PDZ"`, PROSITE PS50106). Everything else is a
giant repeat plus 15 MobiDB-lite disordered regions. Three isoforms; isoform 2
(`VSP_031550`, "Missing (in isoform 2)" over residues 1..5002) is a C-terminal
793-aa fragment with no PDZ.

UniProt's entire functional content for this protein:

- `SUBUNIT: Homodimer (via PDZ domain) (PubMed:24675079). Interacts with DYSF;
  the interaction is direct and Ca(2+)-independent (PubMed:17185750).`
  (`ECO:0000269` for both)
- `SUBCELLULAR LOCATION: Nucleus {ECO:0000250}` — a bare by-similarity tag with
  **no source accession**.

There is no FUNCTION comment, no CATALYTIC ACTIVITY, no EC number, no
SIMILARITY line, no KW beyond Nucleus/Phosphoprotein/Alternative splicing.

## Step 1 — the paralogue test, which is the whole review

The brief's instruction was to check whether the rows rest on AHNAK's accession
or a shared PANTHER node. They do, and the answer is more specific than that.

**Verify the paralogy rather than assume it** (`paralogue_architecture.py`).
PANTHER PTHR23348 ("PERIAXIN/AHNAK") holds AHNAK2, AHNAK and the periaxins in
**three different subfamilies** — SF37, SF41, SF42. Measured on the only
structured domain any of them has:

- AHNAK2 PDZ vs AHNAK PDZ: **28.4%**
- AHNAK2 PDZ vs human PRX PDZ: **56.8%** (mouse Prx 58.0%, rat Prx 58.0%)
- ortholog controls: AHNAK2 vs mouse Ahnak2 89.7%, AHNAK vs mouse Ahnak 97.9%,
  PRX vs mouse Prx 97.6%

So at its only domain AHNAK2 is *twice as close to periaxin as to AHNAK*, and
both are far below the ~90–98% ortholog scale. That matches PDB 4CN0, which
crystallised the PRX and AHNAK2 PDZ domains side by side as homologues
[PMID:24675079 "We present the crystal structures of the PDZ-like domains from
PRX and its homologue AHNAK nucleoprotein 2 (AHNAK2)."] and did not involve
AHNAK.

**How much of the AHNAK2/AHNAK similarity is just the repeat?** The best local
alignment between them runs 4838 residues at 36.9% identity — impressive until
it is partitioned: **71.9% of the aligned columns fall inside AHNAK2's
low-complexity repeat**, and identity is *higher* inside it (39.9%) than
outside (29.3%). The repeat units are not even shared: AHNAK2's most frequent
10-mer `KDSKFKMPKF` occurs 22× in AHNAK2 and 11× in mouse Ahnak2, and **zero**
times in AHNAK, mouse Ahnak, or any periaxin, whose own anchor is `KLKGPKFKMP`.

This is exactly the case the brief warned about: two giant repeat proteins
scoring as similar for a reason that carries no functional implication. I am
recording it as a negative result for the naive framing, not as a refutation of
the paralogy — they are genuinely one family, just not close enough for
AHNAK-specific cell biology to transfer.

## Step 2 — resolve every WITH/FROM, then query the donors' own evidence

`resolve_withfrom.py` + `check_multihit.py`. 13 GOA rows, 21 (row, token)
pairs, 13 distinct tokens, zero unresolved protein tokens.

| token | resolves to | status |
|---|---|---|
| MGI:MGI:108176 | mouse Prx, periaxin (O55103) | Swiss-Prot, 1391 aa |
| MGI:MGI:1316648 | mouse Ahnak (E9Q616) | **TrEMBL** — no Swiss-Prot entry exists |
| MGI:MGI:2144831 | mouse Ahnak2 (A0A7N9VR94) | **TrEMBL** — no Swiss-Prot entry exists |
| RGD:619960 | rat Prx, periaxin (Q63425) | Swiss-Prot, 1383 aa |
| UniProtKB:Q09666 | human AHNAK | Swiss-Prot |
| UniProtKB:Q9BXM0 | human PRX, periaxin | Swiss-Prot |
| UniProtKB:Q8IVF2 | AHNAK2 itself — self-referential, valid | Swiss-Prot |
| PANTHER:PTN001156025 | tree node, not a protein | — |

Multi-hit ambiguity reported rather than collapsed: 5 / 5 / 3 / 3 UniProt hits
respectively. Neither mouse Ahnak nor mouse Ahnak2 has a reviewed entry, so
their *names* are automatic even though their GO annotations are real IDAs —
evidence provenance and name provenance are separate.

**Every resolvable donor carries its own experimental evidence for the term it
donates, except one.** So "the sources only carry the same family-level
inference" would have been factually wrong here, and I am not making it. The
defect is elsewhere:

- `GO:0005634 nucleus`: 4 donors — mouse Prx, rat Prx, human PRX, mouse Ahnak.
  **The AHNAK2 ortholog is not among them.**
- `GO:0043484 regulation of RNA splicing`: 2 donors — mouse Prx (which holds
  the term **only by IBA**, i.e. circularly) and mouse Ahnak (IDA,
  PMID:21940993). **One donor with real evidence, and it is the paralogue.**
- `GO:0005737 cytoplasm`: 7 donors including mouse Ahnak2 and AHNAK2 itself.
  This is the one row with ortholog support.

## Step 3 — go one level deeper than the donor: what does that IDA actually say?

The single donor behind the splicing IBA is mouse Ahnak's IDA from
PMID:21940993, and reading it changes the verdict:

- [PMID:21940993 "During muscle differentiation the small AHNAK is strongly
  increased, thereby establishing a positive feedback loop to regulate mRNA
  splicing of its own locus."]
- [PMID:21940993 "A small 17-kDa isoform of Periaxin similarly traffics between
  the cytoplasm and the nucleus to regulate mRNA splicing."]
- [PMID:21940993 "These proteins interact in the cytoplasm, but the small AHNAK
  is also present in the nucleus."]

The demonstrated mechanism is **cis and locus-autonomous**: a small nuclear
isoform feeding back on its own gene's splicing. Transferring it to AHNAK2
asserts something specific and untested — that AHNAK2 also makes a small nuclear
isoform that regulates the AHNAK2 locus.

What makes the PAINT call *reasonable* rather than careless is that the same
authors flag the shared gene architecture: [PMID:21940993 "This genetic
structure is shared by AHNAK2 and Periaxin, which share a common ancestor."]
Two of three family members with that architecture do it. That is what IBA is
for, so I have marked the row over-annotated rather than removing it.

What argues against transfer, concretely: the AHNAK/periaxin nuclear pool is a
small **N-terminal, PDZ-containing** isoform (the small 5′ exons upstream of the
giant exon), and **UniProt annotates no such isoform for AHNAK2**. AHNAK2's only
short isoform, Q8IVF2-2, is residues 5003–5795 — the opposite end of the
protein, with no PDZ. Absence of an annotated isoform is not proof the transcript
does not exist, so this is a named deciding experiment, not a refutation.

Same logic applies to the nucleus rows, and it explains why they are stranded on
the full-length chain with no isoform qualifier.

## Step 3b — the reciprocal node question, which sharpened the splicing verdict

`node_reach.py`. The brief's second half of the PAINT question — *which node's
reach is exactly my gene set, and what did it give them?* — turned out to be the
one worth asking.

All three human PTHR23348 members (AHNAK2, AHNAK, PRX) hold the **same three IBA
terms from byte-identical WITH/FROM sets**, from node `PTN001156025`. PRX has
one extra, `GO:0032287` PNS myelin maintenance, from a **periaxin-specific**
node `PTN002763386`. So the machinery for subfamily-level placement exists and
was used once; everything else is assigned as if AHNAK2, AHNAK and periaxin were
one thing, when their only shared domain is 28.4–58% identical and they sit in
three different subfamilies.

And **none of the three holds `GO:0043484` by its own experimental evidence.**
Only PRX holds `GO:0005634` by its own IDA. So the family-wide holding of the
splicing term rests on a single mouse Ahnak IDA.

Reading that paper's full annotation set by reference is what closed it:

```
PMID:21940993 -> 17 annotations over exactly 2 entities
  mouse Ahnak (E9Q616): GO:0043484 IDA, GO:0005634 IDA, GO:0005829 IDA, + 5 ISS
  human AHNAK (Q09666): GO:0043484 ISS, GO:0043034 ISS, + 7 more
```

The curator made exactly **one species step within one gene** — mouse Ahnak IDA
to human AHNAK ISS — and did not extend it to AHNAK2 or to PRX. PAINT did. That
is a cleaner statement of the defect than "one donor with evidence", and it is
a *contrast between two curation decisions on the same paper* rather than my
opinion about transferability.

Bonus from the same query: human AHNAK acquired `GO:0043034 costamere` by ISS
from this paper. Human AHNAK2 has no costamere annotation at all, which is
exactly the coverage gap the NEW row proposes to fill — and AHNAK2 was one of
the two subjects of the costamere paper.

## Step 4 — where does the nucleus annotation come from at all?

`subcell_provenance.py`:

```
AHNAK2 Q8IVF2  Nucleus  ECO:0000250              <- no source accession
AHNAK  Q09666  Nucleus  (no evidence tag at all)
PRX    Q9BXM0  Nucleus  ECO:0000269|PubMed:24633211
Prx    O55103  Nucleus  ECO:0000269|PubMed:10671475
```

`GO:0005634 / IEA / GO_REF:0000044 / UniProtKB-SubCell:SL-0191` is a mechanical
mapping of the first line — a bare "by similarity" whose donor cannot be traced,
and whose presumed donor (AHNAK) carries an untagged assertion of its own. The
only *measured* nucleus in this family belongs to periaxin.

Against it: Human Protein Atlas immunofluorescence for AHNAK2, reliability
**Enhanced**, calls main location Cytosol and additional location Plasma
membrane, and no nuclear compartment — HPA's vocabulary includes nucleoplasm,
nuclear bodies and nuclear membrane, so this is a measurement that declined to
confirm. It is not proof of absence (the campaign's standing rule that an
absence is not a finding), which is why both nucleus rows are
`MARK_AS_OVER_ANNOTATED` and neither is `REMOVE`.

## Step 5 — the T-tubule row: a hypothesis I set out to remove and downgraded

Initial reading: `GO:0030315 T-tubule` is NAS from PMID:17185750, whose abstract
is entirely about AHNAK — [PMID:17185750 "In normal skeletal muscle, dysferlin
and AHNAK colocalize at the sarcolemmal membrane and T-tubules."] — and the one
study that used AHNAK2-specific antibodies reports the opposite: [PMID:20833135
"We used specific AHNAK1 and AHNAK2 antibodies to analyzed the detailed
localization of both proteins in mouse skeletal muscle."], [PMID:20833135
"Co-localization of AHNAK1 and AHNAK2 with vinculin clearly demonstrates that
both proteins are components of the costameric network."], [PMID:20833135 "In
contrast, no AHNAK expression was detected in the T-tubule system."]

Two corrections came out of checking rather than concluding:

1. **Affinage over-specified that sentence.** Its record says "no AHNAK2
   expression was detected in the T-tubule system". The abstract says "no AHNAK
   expression". The paper is about both proteins and calls them AHNAK1/AHNAK2,
   so the generic use plausibly covers both — but the provider's version is not
   what is written, and I am not quoting it.
2. **There *is* independent T-tubule evidence for AHNAK2**, from the AHNAK2
   discovery paper, in cardiomyocytes rather than skeletal muscle. It is weak
   but not nothing: the antibody was pan-AHNAK [PMID:15007166 "we found that a
   monoclonal antibody that reacts with multiple repeat domains of both AHNAKs
   localizes to Z-band regions of mouse cardiomyocytes when analyzed by light
   microscopic immunofluorescence."], the AHNAK2 assignment came from residual
   staining in null mice and is explicitly hedged [PMID:15007166 "Because
   AHNAK1-null mice show the same antibody staining pattern, which we assume
   labels AHNAK2 as well, we conclude that both AHNAKs are probably concentrated
   at these same subcellular sites"], and the T-tubule part is an inference from
   cosedimentation [PMID:15007166 "which is consistent with it being bound to a
   vesicle fraction derived from the T tubules"].

A 2022 review states the discrepancy directly [PMID:35158796 "However, in
contrast, a separate study of skeletal muscle showed no colocalisation of AHNAK
or AHNAK2 with dihydropyridine receptors [14]."].

**Neighbouring-sentence check on the quote I truncated.** The Komuro sentence I
quote ends mid-period in the abstract; the continuation is *"...but other
studies indicate that the association of AHNAKs with calcium channel proteins is
more widespread."* It does not disconfirm the hedge I am relying on — if
anything it widens it away from a cardiomyocyte-specific T-tubule claim. Running
the check and reporting the result, since a verbatim quote can be true and
selectively bounded and no validator can see that. The abstract's closing line is
also a nice arc: in 2004 the PDZ domain was *"predicted"*; by 2014 it had been
crystallised at 1.75 Å.

So: cardiac-vs-skeletal, pan-antibody-vs-specific-antibody, and the GOA row
cites neither of those papers. `MARK_AS_OVER_ANNOTATED`, not `REMOVE`. Recording
the downgrade because the aggressive version would have read as a confident
finding.

## Step 6 — per-partner judgement on the two `GO:0005515` rows

Both are IPI from PMID:17185750, whose abstract names only AHNAK. I cannot read
the full text (subscription; Europe PMC `inEPMC: N`, `hasPDF: N`), so the
CLAUDE.md rule applies: no `REMOVE` on a cached abstract. But the two rows are
not equally supported, and QuickGO by reference shows why the curation was
deliberate rather than copied — the curator built **reciprocal** pairs:

```
DYSF   IPI WITH=Q09666      AHNAK  IPI WITH=O75923
DYSF   IPI WITH=Q8IVF2      AHNAK  IPI WITH=Q9NZM1
MYOF   IPI WITH=Q09666      AHNAK2 IPI WITH=O75923
MYOF   IPI WITH=Q8IVF2      AHNAK2 IPI WITH=Q9NZM1
```

- **DYSF** (`O75923`): UniProt's AHNAK2 entry carries `Interacts with DYSF; the
  interaction is direct and Ca(2+)-independent` at `ECO:0000269|PubMed:17185750`
  — a Swiss-Prot curator reading the full text concluded AHNAK2 binds dysferlin.
  `KEEP_AS_NON_CORE`.
- **MYOF** (`Q9NZM1`): the abstract attributes this one explicitly to the
  paralogue [PMID:17185750 "As expected, the N-terminal domain of myoferlin also
  interacts with the carboxyterminal domain of AHNAK."], and **UniProt's AHNAK2
  SUBUNIT records DYSF but not MYOF**. That asymmetry is a real signal and not a
  refutation. `UNDECIDED`, which is what the enum is for.

Partner accessions resolved and checked against canonical: `O75923` DYSF
Swiss-Prot 2080 aa, `Q9NZM1` MYOF Swiss-Prot 2061 aa. No TrEMBL or ORFeome
substitutions (the ACRV1 `Q86WV8` failure mode) — reporting the negative.

## Step 7 — the IntAct check, which came back inverted

`intact_partners.py`. 164 records, 18 distinct publication records (17 PMIDs
plus one unassigned), 118 distinct partners, 11
detection methods. `two hybrid array` / `two hybrid prey pooling approach` /
`validated two hybrid` at 19/19/18 is the familiar one-screen-counted-three-ways
pattern, so UniProt's `NbExp=3` entries are not three experiments. 68 of the 164
records tested a short isoform (`Q8IVF2-3` 62, `Q8IVF2-2` 6).

The inversion: **none of those 118 partners reached GOA.** GOA's two
`GO:0005515` rows name DYSF and MYOF, and neither appears anywhere in IntAct's
AHNAK2 record. So the usual story — screen noise leaking into GO — is not what
happened here. A large high-throughput interactome sits outside GO entirely.

## Step 8 — the ARBA rows cannot be reproduced from the published rules

`arba_rules.py`. `ARBA00026971` (cytoplasm) has 2388 condition sets;
`ARBA00027801` (plasma membrane) has 686. Both condition only on InterPro,
PANTHER, FunFam and taxon. **Not one set in either rule mentions any of
AHNAK2's six signatures.** The script self-tests by constructing a true positive
from the rule's own conditions first, so the zero is a result rather than a
broken matcher. Reported as an unresolved provenance question, not spun into a
verdict — both terms are independently supported by the HPA IDA rows anyway.

## Step 8b — the propagation pipelines that are absent, and what that means

Resolving provenance means accounting for the GO_REFs that are *not* there as
well as the ones that are. AHNAK2's 13 rows use `GO_REF:0000033` (PAINT, 3),
`GO_REF:0000117` (ARBA, 2), `GO_REF:0000052` (HPA, 2), `GO_REF:0000044`
(SubCell, 1), plus 5 from PMID:17185750. There is **no `GO_REF:0000002`
(InterPro2GO)** row and **no `GO_REF:0000120`** row.

That absence is informative rather than a gap. The only interpro2go mapping
available for any of AHNAK2's signatures is

```
InterPro:IPR001478 PDZ domain > GO:protein binding ; GO:0005515
```

— i.e. the pipeline's best offer for this protein is exactly the uninformative
term the curation guidelines tell us to avoid, and it would be redundant with
the two IPI rows already present. So there is no InterPro2GO over-annotation to
find here, which is worth stating: the check ran and came back negative. It also
sharpens the case for `GO:0042803` — no automatic route can ever produce a
better molecular function for AHNAK2, so the structure has to be curated by
hand or the gene stays MF-dark.

## Step 9 — what has actually been measured on human AHNAK2

The best-measured fact about this protein is not in GO at all.

[PMID:24675079 "The unique intertwined, domain-swapped dimers provide a
structural basis for the homodimerization of both proteins."] PDB **4CN0**,
1.75 Å, chains A/B, residues 108–203 — and InterPro's representative structure
for the whole PTHR23348 family. UniProt curates it as `Homodimer (via PDZ
domain) (PubMed:24675079)` at `ECO:0000269`.

`gap_homodimer.py`: **PMID:24675079 has 0 GO annotations in all of GOA**, for
any protein, and none of AHNAK2, PRX or AHNAK holds `GO:0042803`, `GO:0046982`
or `GO:0051260`. Proposing `GO:0042803 protein homodimerization activity` (IDA)
gives AHNAK2 its first informative molecular function; the same paper should
give PRX one too, which is in `suggested_questions`.

The other measured AHNAK2 function is FGF1 export [PMID:25560297 "The heat
shock-dependent association of FGF1 with the large protein AHNAK2 was
observed."], [PMID:25560297 "Depletion of AHNAK2 resulted in a drastic decrease
of stress-induced FGF1 export but did not affect spontaneous FGF2 export and
FGF1 release induced by the inhibition of Notch signaling."]. Reading the
methods changes the evidence code: the knockdown is of **mouse** AHNAK2
[PMID:25560297 "Genetic constructs pGFP-V-RS expressing shRNAs that suppress the
expression of mouse AHNAK2 were obtained from Origene (Rockville, MD)."] in NIH
3T3 cells, and the co-IP used an adenovirally overexpressed V5-tagged
**C-terminal 483-aa fragment** of human AHNAK2, because [PMID:25560297
"commercially available anti-AHNAK2 antibodies failed to reliably detect AHNAK2
both in immunoblotting and immunofluorescence"]. So these are ISS/IPI on a
fragment, not IDA/IMP on the human protein — proposed as such.

## Step 9b — an ontology gap, checked properly before being called one

An empty OLS keyword search is not evidence a term is absent, so I enumerated
`GO:0009306`'s children from QuickGO instead. It has **23**: nine bacterial
secretion systems, three regulation terms, a basolateral and a platelet route,
and **ten cargo-named terms** — Wnt protein secretion, BMP secretion, insulin,
prolactin, adiponectin, amylase, matrix metallopeptidase, renin, pancreatic
trypsinogen, lysosomal enzymes. So the cargo-named pattern is well established
and populated, and **FGF is simply missing from it**. There is also no
unconventional- or non-classical-secretion term anywhere in GO.

I did **not** file a `proposed_new_terms` entry, because the nearest existing
term is `GO:0090269 fibroblast growth factor production`, defined as appearance
due to *"biosynthesis or secretion"* following a cellular stimulus — which
arguably already covers it, while sitting in the production branch rather than
under protein secretion. Proposing a duplicate of a term that may have been
created precisely to serve this case is the failure mode the campaign's
merged-GAP-terms lesson warns about. Recorded as an `ONTOLOGY` knowledge gap on
the FGF1 core function with the disambiguating question for GO curators, and
annotated to the undifferentiated parent in the meantime.

## Step 10 — what I declined to propose

- **`GO:0060090 molecular adaptor activity`.** Affinage's grounding proposes it,
  and it is the obvious term for a giant scaffold. But no experiment shows
  AHNAK2 bringing two molecules together, and the dedicated 2022 review says the
  evidence is not there. I am not annotating a role inferred from a protein's
  size and its paralogue's reputation.
- **`GO:0008092 cytoskeletal protein binding`** (also in affinage's grounding).
  The F-actin association in PMID:25560297 is colocalisation of an
  overexpressed tagged fragment, not binding.
- **`GO:0030018 Z disc`.** Mouse Ahnak2 holds it by IDA from PMID:15007166, but
  that assignment rests on the same pan-AHNAK antibody and null-mouse inference
  as the T-tubule claim. Left as a knowledge gap rather than transferred.
- **A direct AHNAK2–periaxin interaction.** Affinage's narrative states "it binds
  directly to periaxin", citing PMID:31011849, which does say [PMID:31011849
  "AHNAK2 binds directly to periaxin which is encoded by the PRX gene, and PRX
  mutations are associated with another form of AR-CMT (CMT4F)."] — but as
  background, not as its own measurement, and its own conclusion is hedged
  [PMID:31011849 "The altered expression of mutant AHNAK2 may disrupt the
  AHNAK2-PRX interaction in which one of its known functions is to regulate
  myelination."]. A Europe PMC search for "AHNAK2" AND "periaxin" returns 15
  records with nothing earlier than PMID:24675079, which reports **homodimers of
  each protein separately**, not a heterodimer. I think the "binds directly to
  periaxin" claim entered the literature by reading a two-homodimer structure
  paper as a heterodimer paper. Flagged in `reference_review` as the most
  salient issue with that citation, and raised in `suggested_questions` rather
  than asserted as fact.
- Affinage also describes the CMT variants as "compound heterozygous"; the
  abstract describes a consanguineous family with autosomal recessive
  inheritance and two segregating variants. Not load-bearing, but noted.

## Retraction / erratum check

`retraction_check.py` reads `CommentsCorrections/RefType` off each cited
article's own PubMed record, because a publication-type search cannot see a
Publisher Correction. **10 PMIDs checked, 0 flagged** — the 8 papers cited in
the review plus the two donor-evidence papers (PMID:24633211, PMID:10671475).
The cancer-biology papers in the affinage record support no annotation here, so
their status is not load-bearing.

## A defect my own rewrite introduced, found mechanically

`reconcile_goa.py` keys every GOA row on `(GO id, evidence, reference,
WITH/FROM)` and demands a 1:1 match with the review. It reported one mismatch:
the `GO:0005886 / IEA / GO_REF:0000117` row had **lost its
`ARBA:ARBA00027801` supporting entity** when I rewrote the YAML. Reading the
file did not catch it; the row-by-row key comparison did on the first run.

Worse, `audit_claims.py` had the bug the campaign brief names explicitly — *a
guard defeatable by deleting the thing it guards*. Its check read
`if supporting.get(key) and supporting[key] != want`, so an **empty** list
skipped the comparison and passed. Deleting the whole field was invisible to the
check written to protect it. Now fixed to assert presence
(`got = supporting.get(key, set())`), and both scripts are committed so the
invariant is enforced rather than remembered.

13 GOA rows + 4 NEW = 17 entries, reconciling exactly.

## Cross-check against the concurrent AHNAK review (PR #2999)

Diffed row-by-row rather than assumed, since independently reviewed paralogues
in this campaign have given the same row different answers. The two reviews
share **10** `(term, evidence, reference)` keys and diverge on **5**. Every
divergence is one I had predicted, and each has a checkable basis:

| shared row | AHNAK2 | AHNAK | why they differ |
|---|---|---|---|
| `GO:0005515` IPI PMID:17185750 | KEEP_AS_NON_CORE + UNDECIDED | ACCEPT x3 | the paper's subject is AHNAK; UniProt carried DYSF but not MYOF to AHNAK2 |
| `GO:0005634` IBA | MARK_AS_OVER_ANNOTATED | ACCEPT | **human AHNAK holds nucleus by ISS from its own mouse orthologue** (PMID:21940993); AHNAK2 has no equivalent |
| `GO:0030315` T-tubule NAS | MARK_AS_OVER_ANNOTATED | ACCEPT | AHNAK's own datum in that paper; AHNAK2's is not |
| `GO:0042383` sarcolemma NAS | KEEP_AS_NON_CORE | ACCEPT | same |
| `GO:0043484` IBA | MARK_AS_OVER_ANNOTATED | KEEP_AS_NON_CORE | **human AHNAK holds it by ISS from mouse Ahnak's IDA**; AHNAK2 holds it only by IBA |

The two rows that matter turn on the same fact, and it is one I got slightly
wrong on a first pass and corrected: **the PMID:21940993 IDA is on *mouse*
Ahnak; human AHNAK holds both `GO:0005634` and `GO:0043484` by *ISS* from it.**
That ISS is an ortholog-strength, same-gene transfer made by a curator reading
the paper. AHNAK2 has no such transfer for either term — it has only the IBA,
whose donor set is periaxin-dominated for nucleus and, for splicing, one mouse
Ahnak IDA plus a mouse Prx holding the term circularly. So the divergences are
**well-founded rather than an inconsistency to reconcile**: the same term is
ISS-supported on one gene and IBA-only on the other.

Two further points recorded for the AHNAK reviewer:

1. **`UniProtKB:Q09666` in a WITH/FROM** is *self-referential* on AHNAK and
   *paralogue-derived* on AHNAK2; `UniProtKB:Q8IVF2` mirrors it. The same string
   means different things per gene — the AFF1/AFF4 pattern.
2. **The PDZ measurement.** `GO:0042803` from PMID:24675079 would be wrong for
   AHNAK — the structure's two chains are PRX and AHNAK2, and AHNAK is not in
   it. Checked: the AHNAK review does not propose it.
