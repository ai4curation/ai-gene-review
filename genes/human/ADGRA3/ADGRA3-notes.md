# ADGRA3 (GPR125) — review notes

UniProt `Q8IWK6` / `AGRA3_HUMAN`, 1321 aa, reviewed (Swiss-Prot), `PE 1: Evidence at protein level`.
HGNC:13839. Accession independently verified against `projects/paint/human-no-IBA-simple.csv`
(`human,Q8IWK6,ADGRA3`) and against the UniProt REST record before any other work was done.

## 1. Row reconciliation, done first

```
wc -l genes/human/ADGRA3/ADGRA3-goa.tsv   ->  32  (31 data rows + header)
grep -c '^- term:' ...-ai-review.yaml     ->  14  (the fetch-gene stub)
```

The 17-row gap is entirely the documented `seed_missing_annotations` collapse
(`goa_validator.py:577` keys on GO id + evidence + reference + negated + qualifier, and omits
WITH/FROM). GOA has **19** `GO:0005515` IPI rows — one from `PMID:24550280` and **18** from
`PMID:36115835`, differing only in the partner accession — and the stub collapsed the 18 into one.
No distinct GO term was lost. All 31 rows are restored one-per-line, so every partner gets its own
verdict, and `existing_annotations` is generated *from* the TSV by
`/tmp/adgra3/build.py` with `assert len(annotations) == 31` rather than assembled by hand.

Final counts: **31 GOA-derived rows + 7 `NEW` proposals = 38 entries** (9 ACCEPT, 22 MODIFY, 7 NEW).

## 2. The gene is not dark. GOA makes it look dark.

This was the single most consequential finding, and it is checkable. Querying QuickGO **by
reference** for each paper that experimentally characterised ADGRA3 returns **zero annotations, for
any species, for every one of them**:

| PMID | what it established | GO annotations anywhere |
|---|---|---|
| 36089063 | cis-autoproteolysis; DLG1 binding; basolateral targeting; apicobasal polarity | **0** |
| 40127866 | Gs and Gi coupling; stachel dependence; DVL-independence | **0** |
| 31659746 | surface expression; constitutive clathrin-dependent endocytosis | **0** |
| 39718208 | constitutive Gs-PKA-CREB adipose thermogenesis | **0** |
| 35414778 | osteoclastogenesis | **0** |
| 36688818 | obstructive azoospermia in `Adgra3-/-` males | **0** |
| 38589878 | imperforate vagina in `Adgra3-/-` females | **0** |

The whole human GO record is 3 IBA + 5 IEA + 1 ISS + 3 TAS (to a 2004 sequence catalogue) + 19 bare
`protein binding` rows from two PDZ affinity screens. So "dark by GOA" and "dark by literature" come
apart completely here, and per the brief's `PE 1` rule the honest statement is *uncurated*, not
*uncharacterised*. Filed under `knowledge_gaps` as a `CURATION` gap.

## 3. The paralog-transfer hypothesis: **not confirmed**

The task predicted transfer of ADGRA2's WNT7A/WNT7B co-activation and blood-brain-barrier biology
onto ADGRA3. I derived the family picture independently (no ADGRA2 review exists on `main` and no
ADGRA2 PR was open when I checked, so there was nothing to copy) and the prediction does not hold.
PAINT partitions this family cleanly:

| node | reach (reviewed members of PTHR45930) | terms it propagates |
|---|---|---|
| `PTN001738137` | **all 8** — ADGRA1/2/3 in human and mouse, plus adgra2 and adgra3 in zebrafish (which has no adgra1 in the family) | `GO:0005886`, `GO:0007166` |
| `PTN002914520` | **exactly the 3 ADGRA2 orthologs** | `GO:0002040`, `GO:0007417`, `GO:0090263`, `GO:1990909` |
| `PTN002914505` | **exactly the 2 ADGRA1 orthologs** | `GO:0014069`, `GO:0098978` |
| `PTN002914494` | **exactly the 3 ADGRA3 orthologs** | `GO:0009897` — and nothing else |

Every ADGRA2-specific term (sprouting angiogenesis, Wnt signalosome assembly, positive regulation of
canonical Wnt signalling, CNS development) is confined to the ADGRA2-only node and **does not reach
ADGRA3**. ADGRA1's synaptic terms are likewise confined. `UniProtKB:Q96PE1` (ADGRA2) *is* present in
ADGRA3's WITH/FROM, but only on the two family-root rows, where the terms are `plasma membrane` and
`cell surface receptor signaling pathway` — generic and true of ADGRA3 in its own right.

This is a **non-confirmation**, and per the brief it is worth as much as a finding. It is the fifth
in the campaign's running tally.

## 4. The reciprocal node question, which *did* find something

Asking the other half — *which node's reach is exactly my gene set, and what did it give them* —
produces the real defect. `PTN002914494` covers precisely human ADGRA3, mouse Adgra3 and zebrafish
adgra3, and hands them one localisation term. Meanwhile a member of that very node, zebrafish
adgra3, carries from `PMID:23821037`:

- `GO:0060071` Wnt signaling pathway, planar cell polarity pathway — **IDA**
- `GO:2000095` regulation of Wnt signaling pathway, planar cell polarity pathway — **IMP + IPI**
- `GO:0005886` plasma membrane — **IDA**

and only the third of these reaches human and mouse (via the *other*, family-root node). So the
direction of error in this family is **ortholog under-transfer at the ADGRA3 node**, not paralog
over-transfer — the mirror image of the predicted failure, and the same shape as the ACTG2 finding
where the node whose reach was exactly the smooth-muscle actins gave them `extracellular region`.

I checked the obvious innocent explanation and it fails: the terms are not IBA-ineligible. QuickGO
returns **70** IBA annotations to `GO:0060071` and **36** to `GO:2000095` across many taxa,
including human. So PAINT propagates these terms elsewhere and declined to here.

I did **not** turn this into a proposed `GO:0060071` annotation for human ADGRA3. Doing so would
manufacture the ortholog transfer PAINT declined, and the human data cut both ways (see §6). It is
raised as a `suggested_questions` item for GO Central and recorded as an open `knowledge_gap`.

## 5. `GO:0005515` — 19 rows, one motif

All 19 rows trace to peptide/PDZ-domain affinity assays on the same four residues.

The C-terminus is `...RTGLWKHETTV`; UniProt annotates `FT MOTIF 1319..1321 /note="PDZ-binding"`, and
the paper states it exactly: [PMID:36089063 "The CTT of GPR125 contains the extreme C-terminal
tetrapeptide Glu-Thr-Thr-Val (amino acid residues 1318–1321), which corresponds to the type I PDZ
domain–binding motif (PBM)"].

Partner audit (the ACRV1 checks, all run, results reported either way):

- **All 18 holdup partners resolve to reviewed Swiss-Prot canonical entries**, lengths matching the
  canonical gene. No TrEMBL clone, no partial ORFeome construct. *Negative result* — the ACRV1
  `Q86WV8`-style substitution is absent here.
- **All 18 carry PDZ domains**, between 2 (GRID2IP, APBA2) and 13 (MPDZ). The set is completely
  coherent with the bait.
- **`NbExp` is not independent replication.** IntAct holds **145** interactions for `Q8IWK6`;
  **117** of them are `holdup assay` from `PMID:36115835` alone, spanning **80** distinct PDZ
  proteins, of which GOA imported 18. Counting distinct *publications* per partner: **17 of the 18
  rest on one paper and one method**. Only DLG1 has more — `PMID:15021905` (2-hybrid + anti-tag
  co-IP + pull down), `PMID:24550280` (phage display) and `PMID:36115835` (holdup).
- **Topology/context split.** Nine partners (DLG1, MPDZ, TJP1, SCRIB, PATJ, MAGI1, MAGI2, PDZK1,
  FRMPD2) are junctional/basolateral scaffolds and are topologically compatible with a receptor that
  is itself basolaterally confined. Seven (DLG4, DLG2, DLG3, GRIP1, GRIP2, APBA2, GRID2IP) are
  postsynaptic scaffolds — a compartment where ADGRA3 has never been observed and where the
  *paralogue* ADGRA1 is the characterised family member (it is ADGRA1 that PAINT gives
  `GO:0014069` postsynaptic density and `GO:0098978` glutamatergic synapse). Two (IL16, LNX2) are
  neither.

Verdict: **MODIFY all 19 → `GO:0030165 PDZ domain binding`**, with the partner preserved in an
`extensions` block (`predicate: RO:0002233`). That states what was measured; `protein binding`
states nothing. Not `MARK_AS_OVER_ANNOTATED` — these are quantitative affinity measurements on
correctly identified partners, not unreplicated Y2H noise; what is unestablished is cellular
relevance, and that is captured per-partner in the row summaries rather than by downgrading the
term.

DLG1 is the exception in kind, not just in degree: [PMID:36089063 "These findings indicate that
GPR125 associates with Dlg1 in a PBM-dependent manner."] and [PMID:36089063 "Similarly, endogenous
Dlg1 in MDCK cells was coprecipitated with FLAG–GRP125-FL but not with FLAG–GRP125-ΔETTV"]. The
2004 paper that UniProt cites with `ECO:0000269` covers **both** paralogues — its "TEM5" is
ADGRA2 and its "TEM5-like" is ADGRA3 [PMID:15021905 "hDlg furthermore bound a novel seven-pass
transmembrane protein, which was homologous to TEM5, and was named here a TEM5-like protein
(TEM5-like)."]. So this is a case where the shared paper is genuinely about both genes, and the
transfer risk runs the *other* way: its endothelial-colocalisation and tumour-angiogenesis claims
are about TEM5/ADGRA2 only, and are not used here.

## 6. The gene is a real GPCR — the fold-propagation suspicion is wrong here

`GO:0004930` and `GO:0007186` reach ADGRA3 by two weak routes: InterPro signatures (IPR000832
secretin-like family, IPR001879 and IPR036445 hormone-binding domain) and three 2005 GDB **TAS**
rows citing `PMID:15203201`, a bioinformatic repertoire survey containing no experiment on GPR125.
That is the campaign's classic "a domain name became an activity" shape — arriving in a TAS row
rather than the retired SPKW route.

It has since been earned:

- [PMID:40127866 "We found low-level activation of Gi and Gs by ADGRA3 and slightly more by its
  CTF."]
- [PMID:40127866 "This resulted in abrogated G protein-mediated signaling, as observed for other
  aGPCRs."] (on deleting the first three CTF residues, i.e. the stachel tethered agonist)
- [PMID:40127866 "Collectively, this establishes classical G protein-mediated signaling for
  ADGRA3."]
- corroborated by [PMID:39718208 "Conversely, Adgra3 overexpression activated the adipose
  thermogenic program and improved metabolic homeostasis in mice without exogenous ligand."]

So: **ACCEPT** the terms, flag the *provenance* for upgrade to IDA, and add the specific children
`GO:0007189` (Gs) and `GO:0007193` (Gi) as `NEW`. Same lesson as ACBD3's `GO:0000062` — a
domain-derived annotation that eight rounds of scepticism argued against turned out to be right.

Two negatives from the same paper, which is why no Wnt term is proposed:

- [PMID:40127866 "No transcriptional activation was observed in an assay of downstream β-catenin
  activity."]
- [PMID:40127866 "Collectively, this suggests that ADGRA3 is capable of activating Gai signaling
  axes independently of DVL presence."]

But these do **not** close the PCP question, and I read the surrounding paragraphs before relying on
them (the ACTR10 rule). β-catenin is the *canonical* branch; PCP is not. And the same group that
showed the polarity role also detected DVL binding: [PMID:36089063 "GPR125 appears to also interact
with Dvl1 but mainly in a PBM-independent manner, in contrast to the absolute requirement of the PBM
for its binding to Dlg1."]. Hence `UNDECIDED`-in-spirit: recorded as a `knowledge_gap`, not as a
verdict in either direction.

## 7. UniProt still contradicts itself on cleavage — correction request, not a GO action

Following the ADCK5 rule (check the UniProt layer even when GOA is clean), the entry carries:

```
CC   -!- MISCELLANEOUS: Most adhesion GPCRs proteins undergo autoproteolysis at
CC       the GPS region of the GAIN-B domain. ADGRA3 is predicted non-cleavable
CC       because of the lack of a consensus catalytic triad sequence within GPS
CC       region. {ECO:0000305}.
```

`ECO:0000305` is a curator inference, and it was tested and refuted:

- [PMID:36089063 "In the present study, we show that human GPR125, expressed in kidney epithelial
  Madin-Darby canine kidney (MDCK) cells and embryonic kidney HEK293 cells, undergoes
  cis-autoproteolysis at the atypical GPS during an early stage of receptor biosynthesis."]
- [PMID:36089063 "GPR125 has been predicted to be noncleavable in the GAIN domain because of its
  atypical GPS motif (Ser736-Leu737-Ser738) but not the canonical one (His-Leu/Ile-Ser/Thr)"]
- and independently [PMID:40127866 "The GPS in most ADGRA3 vertebrate orthologs is SL|S/G (where |
  denotes the potential cleavage point)."]

Alanine substitution of the S736/L737/S738 tripeptide abolishes cleavage, so the atypical motif *is*
the site. Filed as a UniProt correction request in `suggested_questions`, plus a second one for the
`SUBCELLULAR LOCATION: Membrane {ECO:0000250|UniProtKB:S4X0Q8}` line, which is a pre-localisation
by-similarity inference and is the upstream source of all three `GO:0016020` rows.

The **GO** side of this is an addition, not a correction: `GO:0016540 protein autoprocessing` as
`NEW`. A QuickGO census of `GO:0016540` + descendants in human returns 68 annotations over 36 gene
products — caspases, hedgehogs, MYRF, PCSK9, SPRTN — and **not one adhesion GPCR**, though GAIN
autoproteolysis is the class's defining reaction. Raised for the family in `suggested_questions`.

## 8. The three `GO:0016020 membrane` rows

All three → **MODIFY → `GO:0005886`**, each for its own reason:

- **ISS** (`GO_REF:0000024`, from `UniProtKB:S4X0Q8`): the donor is the reviewed zebrafish
  orthologue — correct entity type for ISS, per the ADAMTSL3 rule — and QuickGO shows it holds
  `GO:0005886` by **IDA** (`PMID:23821037`). The inference therefore landed *one is_a step above*
  its own donor: `GO:0005886 --is_a--> GO:0016020` is a single edge on the QuickGO graph endpoint.
  (An earlier draft of this review said "three levels", in three places; the reviewer on #2315
  flagged it and the graph query confirms one. The verdict is unaffected — the MODIFY rests on the
  donor's IDA, not on the size of the gap — but the number was wrong and is corrected here, in the
  YAML and in the PR body.) With exactly one donor and no heterogeneous clade to blame, the step is
  small but free. Same shape as ACRV1, where the loss was larger.
  `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH`.

  For reference, the measured distances to `GO:0016020` over `is_a`/`part_of`: `GO:0005886` = 1,
  `GO:0009897` = 2, `GO:0016323` = 2.
- **IEA** (`GO_REF:0000120`): WITH/FROM includes `UniProtKB-SubCell:SL-0162`, i.e. it is the machine
  reflection of the same by-similarity UniProt line.
- **TAS** (`PMID:15203201`): the paper's only bearing on the term is the definitional
  [PMID:15203201 "The adhesion G-protein-coupled receptors (GPCRs) (also termed LN-7TM or EGF-7TM
  receptors) are membrane-bound proteins with long N-termini containing multiple domains."].

Human localisation is settled well below all of these: [PMID:31659746 "In summary, GPR125 is mainly
expressed on the cell surface and undergoes constitutive internalization under physiological
temperatures"] and [PMID:36089063 "in polarized MDCK cells, GPR125 is exclusively recruited to the
basolateral domain of the plasma membrane"].

## 9. `GO:0009897` — checked for the ACTR8 projection artefact, negative

The IBA's sole protein donor is `MGI:MGI:1917943` = mouse Adgra3 (`Q7TT36`, Swiss-Prot, the 1:1
orthologue), which holds `GO:0009897` by **IDA** from `PMID:17882221` — so the propagation neither
gains nor loses precision, and no downward MODIFY is warranted.

Ran the reference-projection test on the donor's paper. QuickGO `reference=PMID:17882221` returns
**5 annotations over 5 entities** — the superficial shape of a complex projection. It is not one:
the five are Adgra3 and Cd34 (`GO:0009897`), Pou5f1 (nucleus), Vim (intermediate filament) and Acta2
(actin cytoskeleton) — *five different compartments*, and no functional/phenotype term spreads
across the set. It is a marker-panel paper localising five markers independently, so the Adgra3 IDA
is its own. **Negative result, reported.**

Corroborated independently in human: the N-terminally FLAG-tagged receptor is detected on
non-permeabilised HEK293 cells, i.e. the ectodomain faces out.

## 10. Errata and retractions — one found

Per the ACTR5/ACTL8 rules I checked `CommentsCorrections/RefType` on every cited PMID's own record,
not by publication-type search.

**`PMID:36115835` carries an unflagged Author Correction, `PMID:36477203`** (doi
`10.1038/s41467-022-35177-6`), which affinage cites without mention. Crossref `updated-by` on the
original DOI confirms it, and the only other relation is the bioRxiv preprint. I read it: it
restores missing PCC values and axis labels in Figures 2, 4 and 5. It does not touch the affinity
data or anything ADGRA3-specific, so **nothing in this review rests on corrected material**. Flagged
in `reference_review.review_notes` rather than `is_invalid`.

All other 15 cited PMIDs: clean, no retraction, erratum or expression of concern.

## 10b. Constitutive internalisation — `GO:0031623`, and why not `GO:0072583`

Added after the #2315 review pointed out that this review asserted constitutive clathrin-dependent
endocytosis in both `description` and `core_functions`, with quotes attached, and then proposed no
term for it — an omission that reads badly in a review whose thesis is that *absence* is this gene's
dominant defect. Fair, and fixed.

Both candidate terms were checked against their **definitions and their actual curated usage**, not
their labels:

- **`GO:0072583 clathrin-dependent endocytosis` — rejected.** QuickGO returns 246 human annotations
  over 19 distinct gene products, and every one is endocytic **machinery**: AP2A1/A2/B1/S1, FCHO1/2,
  PICALM, SGIP1, SNAP91, HSPA8, ARHGEF37. No cargo. Annotating a receptor there would be role
  conflation.
- **`GO:0031623 receptor internalization` — chosen.** GO does use it for cargo: **TFRC holds it
  `involved_in` by IDA**, and TFRC is precisely the constitutively recycling receptor used as the
  colocalisation marker in this very experiment. CD36 likewise.

One honest caveat, recorded rather than smoothed away: `GO:0031623`'s **definition** says the process
"begins when cell surface receptors are monoubiquitinated following ligand-induced activation", and
ADGRA3's internalisation is neither ligand-induced nor β-arrestin-dependent
[PMID:31659746 "Moreover, we show that the internalization of GPR125 happens in a
β‐arrestin−independent, but TfR1 colocalizing/clathrin‐dependent manner."]. GO's curated usage is
plainly broader than its own definition here — TFRC is the proof — so the term is used as curators
use it, and the definition/usage mismatch is filed as an ontology question rather than being quietly
ignored.

Evidence is IDA on the human protein: surface ELISA on non-permeabilised HEK293 cells, loss of
surface signal over 30 min at 37 °C, and appearance in puncta overlapping GFP-TfR1
[PMID:31659746 "These data support that the constitutive internalization of GPR125 contributes to
its biological functions by controlling receptor surface expression"].

## 11. Provenance discipline on the `NEW` rows

`GO:0045197` is deliberately **ISS, not IMP**. The polarity loss-of-function
[PMID:36089063 "GPR125 is indispensable for correct cystogenesis and mitotic spindle orientation in
3D-cultured MDCK cells, indicating its crucial role in epithelial apicobasal polarization."] used
CRISPR knockout and siRNA against **endogenous canine Gpr125** in MDCK cells. The human protein
supplies the molecular arm (ETTV-dependent DLG1 binding, basolateral targeting) but was not the
perturbed gene. `supporting_entities: [UniProtKB:A0A8I3MZC6]` — the canine ADGRA3 entry, unreviewed
TrEMBL, 1313 aa; there is no reviewed dog entry, and that is stated rather than hidden.

By contrast `GO:0016323` and `GO:0016540` are **IDA**: the protein assayed in those experiments is
human GPR125, even though the host line is canine.

## 12. Affinage record

`gates_passed: True`, `faith_pct: 100.0`, 12 citations, all numeric PMIDs (no `PMID:bio_*`
preprint ids in a PMID-shaped field). Every cited PMID resolved and matched its stated finding. Two
provider claims were **not** used as evidence, per the never-quote-affinage-for-a-mechanism rule:
its GAIN/GPS description and its "Gper1-PI3K/AKT-β-catenin" osteoblast axis (`PMID:42210228`, a
May-2026 J Transl Med paper) — the mechanistic statements were re-derived from UniProt and the
primary full texts instead. Its failure to flag the `PMID:36115835` erratum is recorded in §10.

One validation warning is left standing deliberately: *"No annotations reference available deep
research files"*. Satisfying it requires a `file:...research....md` entry in an annotation's or a
core function's `supported_by`, i.e. citing an affinage sentence as evidence for a molecular claim —
precisely what the campaign rule forbids, because every finding in this record is mechanistic. The
record was used as intended (a lead), each of its claims was re-derived from the primary full texts,
and it is cited where it genuinely is the right source: as corpus-level provenance
(`citation_count: 12`) for the curation-gap `knowledge_gap` in §2. That location is not scanned by
the check, so the warning persists. Inventing a citation to clear it would be worse than the
warning.

## 13. `cache/go/terms.csv`

All six new curies (`GO:0030165`, `GO:0016323`, `GO:0045197`, `GO:0007189`, `GO:0007193`,
`GO:0016540`) were **already present** in the cache, so `just validate` took the cache-hit path and
did not rewrite the file — `git status --porcelain -- cache/go/terms.csv` is empty after the final
validate and this branch touches no shared cache state. Both directions checked anyway: deletions
against the **merge base** (not the moving `origin/main` tip) are none, and the only duplicated
curies are the two that predate this campaign, `GO:0001675` and `GO:0009566`, left alone.

## 14. Tooling note — `xref:zfin-<gene id>` misses the *reviewed* entry

The first draft reported zebrafish `adgra2` as lacking a Swiss-Prot record and resolving only to two
unreviewed TrEMBL accessions. **That was wrong**, and the #2315 reviewer caught it from the committed
`PTHR45930-entries.csv`. The reviewed entry is `E7FBY6` / `AGRA2_DANRE`, Swiss-Prot, 1367 aa — but:

```
xref:zfin-ZDB-GENE-081104-363  ->  ['A0A0U2ULT4', 'A0A8M1P7B9']     # both TrEMBL; E7FBY6 absent
```

So UniProt's `xref:zfin-` index, queried on a **ZFIN gene id**, does not return the Swiss-Prot entry
at all. This is the same class of resolver limit the campaign brief already records for WormBase
(`WB:WBGene…` absent from `xref:wormbase-`, which holds protein ids), and it is more dangerous,
because it does not fail loudly — it returns *plausible* accessions, so the reviewed/unreviewed
printout the brief mandates ends up lying in the direction of understating the source. Cross-check
any MOD-gene-id resolution against the cached PANTHER member table, which is derived from InterPro's
reviewed-protein endpoint and had the right answer sitting in this branch the whole time.

All five non-node donors on the ADGRA3 IBA rows are reviewed Swiss-Prot entries. Their *evidence*
claims were unaffected — those QuickGO queries were run on `E7FBY6` directly, not through the ZFIN
index — so only the provenance labels needed correcting.

## 15. Tooling note — `checkquotes.py` cannot see `knowledge_gaps[].provenance`

Found by a count that refused to add up: the file has **150** `reference_id` entries but
`checkquotes.py` reported **135** checked. The gap is exactly the **15** quotes in
`knowledge_gaps[].provenance[]`. The checker's `walk()` matches only `supported_by` and `findings`,
so `provenance` entries — which are the same `SupportingTextInReference` class — ship unverified,
and the repo's own reference validator has the same shape of scope. All 15 were verified here with
an extended walker that adds `provenance` and then asserts `raw_reference_id_count == checked`, so
the blind spot cannot recur silently. Worth folding into the campaign checker.

## 16. Verdict summary

| rows | term(s) | evidence | action |
|---|---|---|---|
| 1 | `GO:0005886` | IBA | ACCEPT (core) |
| 1 | `GO:0007166` | IBA | ACCEPT — refinement to `GO:0016055` considered and rejected |
| 1 | `GO:0009897` | IBA | ACCEPT — donor holds the identical term by IDA |
| 1 | `GO:0004888` | IEA | ACCEPT — correctly scoped to a 7TM-only signature |
| 1 | `GO:0007166` | IEA | ACCEPT — same signature, same reasoning |
| 1 | `GO:0007166` | IBA | ACCEPT — genuine LCA of a heterogeneous clade |
| 2 | `GO:0004930` | IEA, TAS | ACCEPT (core) — now experimentally demonstrated |
| 2 | `GO:0007186` | IEA, TAS | ACCEPT |
| 1 | `GO:0005886` | IBA | ACCEPT (core) |
| 1 | `GO:0009897` | IBA | ACCEPT |
| 3 | `GO:0016020` | IEA, ISS, TAS | MODIFY → `GO:0005886` |
| 19 | `GO:0005515` | IPI | MODIFY → `GO:0030165 PDZ domain binding` |
| **31** | | | **9 ACCEPT, 22 MODIFY** |
| +7 | `GO:0030165`, `GO:0016323`, `GO:0016540`, `GO:0007189`, `GO:0007193`, `GO:0031623`, `GO:0045197` | IPI/IDA/ISS | NEW |

### The `IPR017981` question, and how it resolved the *other* way

The first draft MODIFYed `GO:0004888` (redundant parent of `GO:0004930`) while ACCEPTing the IEA
`GO:0007166` (redundant parent of `GO:0007186`) — opposite reasoning applied to two identical
situations arising from the **same** InterPro signature. The #2315 reviewer caught it. My first fix
harmonised in the MODIFY direction; running `just validate` then produced a *second* warning —
*"Inconsistent review actions for term GO:0007166: ACCEPT (IBA); MODIFY (IEA)"* — because the repo
enforces same-term-same-action regardless of evidence code.

Two consistency pressures pointing opposite ways forced the question of which action is actually
*right*, and the answer is ACCEPT for both. **`IPR017981` is a 7TM-domain signature.** A
seven-transmembrane bundle cannot by itself tell you a receptor couples to a heterotrimeric G
protein — plenty of 7TM proteins do not. InterPro mapping it to the non-committal parents
`GO:0004888` and `GO:0007166` is therefore *the most that signature can honestly support*, not a
curator stopping short; the specific children arrive from `IPR000832` (GPCR family 2, secretin-like),
a family-level signature that does support them. Modifying a correctly-conservative signature mapping
downward would attribute to it evidence it does not carry — the AADACL4 lesson ("a GENERAL term can
be correct because the source is not specific — not lazy curation") arriving in a new guise, and my
initial MODIFY was the error, not the asymmetry.

The discriminator now applied uniformly across the review: **accept a general term when it is the
most its own source can support; modify it when the specific term is established for this gene and
the general row merely restates a compartment or activity now known precisely.** The three
`GO:0016020` rows sit on the other side of that line — they are superseded statements about where
this protein is, all three get the same action, and the ISS one additionally sits above its own
donor. Both warnings are gone and no term carries two actions.

No `REMOVE` and no `MARK_AS_OVER_ANNOTATED`: nothing in this record is false. The defects are
imprecision (three membrane rows, one redundant parent), uninformativeness (nineteen bare
protein-binding rows), and — the dominant one — absence.
