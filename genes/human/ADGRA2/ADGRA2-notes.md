# ADGRA2 (GPR124 / TEM5) — review notes

UniProt: **Q96PE1** (AGRA2_HUMAN, Swiss-Prot, 1338 aa, PE 1: Evidence at protein level).
Accession verified independently against `projects/paint/human-no-IBA-simple.csv` line 6342
(`human,Q96PE1,ADGRA2`) and against the UniProt REST record
(`uniProtkbId: AGRA2_HUMAN`, `organism: Homo sapiens`, `entryType: UniProtKB reviewed (Swiss-Prot)`).

Deep research: `ADGRA2-deep-research-affinage.md`, `gates_passed: True`, `faith_pct: 85.7`,
10 citations, all numeric PMIDs (no `PMID:bio_*` preprint ids). Its narrative was used only as a
lead list; every claim below is anchored to a PMID or to the UniProt record directly.

## 0. Bookkeeping done first

**GOA row reconciliation.** `ADGRA2-goa.tsv` has 60 lines = 59 data rows, all distinct; live QuickGO
for `UniProtKB:Q96PE1` returns `numberOfHits: 59`, so the cached TSV is complete and current.
The `fetch-gene` stub seeded only **41** `existing_annotations`. The whole 18-row deficit is the
known `GOAValidator.seed_missing_annotations` collapse (WITH/FROM is not part of the seeding key):
the 21 `GO:0005515` rows collapsed to 3 stubs (2→1 for PMID:15021905, 1→1 for PMID:24550280,
18→1 for PMID:36115835). All 21 were restored one-per-partner, so each partner carries its own
verdict. Final count 59 = 59, asserted mechanically by `ADGRA2-bioinformatics/check_coverage.py`.

**Retraction / erratum / correction sweep.** `ADGRA2-bioinformatics/check_corrections.py` checked all
15 cited PMIDs against `CommentsCorrections/RefType` on each article's own PubMed record *and*
against Crossref `relation`/`update-to`. One hit: **PMID:36115835 carries an Author Correction,
PMID:36477203** (Nat Commun 2022;13:7555). Nothing retracted, no expression of concern.

> Writing that checker produced a defect worth recording. The first version read the DOI with
> `.//ArticleId`, which also matches ArticleIds inside `ReferenceList`, so three of fifteen PMIDs
> were Crossref-checked against a DOI belonging to a paper they merely *cited* — PMID:28600358 was
> checked as `10.3791/50316` (a JoVE paper) and PMID:35649360 and PMID:27979830 both as
> `10.1016/j.devcel.2014.08.018`. Every one reported `crossref=none`, i.e. a **false clean**. It was
> caught only because two different PMIDs printed the *same* DOI. The fix anchors to
> `PubmedData/ArticleIdList` and asserts the DOI's Crossref title matches the PubMed title;
> `--self-test` break-tests it in five directions, including the happy path and the
> reference-scoped variant of the same bug in `CommentsCorrections`.

## 1. What the protein is

ADGRA2 is an endothelial adhesion-class GPCR: cleaved signal peptide (1–33), a long extracellular
region (34–771) carrying four leucine-rich repeats, an LRRCT, an Ig-like domain, a **GAIN-B domain
(594–759) with a GPS region (710–759)**, then a canonical seven-transmembrane bundle (772–1068) and a
269-residue cytoplasmic tail ending in **…LWKSETTV** — a class-I PDZ-binding motif (verified from the
Q96PE1 FASTA). A cryptic **RGD motif at 362–364** sits in the ectodomain
[`file:human/ADGRA2/ADGRA2-uniprot.txt` FT MOTIF 362..364 /note="RGD"].

So the adhesion-GPCR architecture is complete and genuine — this gene is *not* a case of a
fold-name misapplied to a protein that lacks the fold. The question is what the fold does here.

## 2. The central question: does ADGRA2 do G-protein-coupled receptor activity?

`GO:0004930` is defined as *"Combining with an extracellular signal and transmitting the signal
across the membrane by activating an associated G-protein; promotes the exchange of GDP for GTP on
the alpha subunit of a heterotrimeric G-protein complex"* (QuickGO
`/ontology/go/terms/GO:0004930/complete`, `isObsolete: false`). Three things are needed: a ligand,
an associated Gα, and nucleotide exchange. For ADGRA2:

- **No ligand.** The gene is called an orphan in its own defining paper's title
  [PMID:21421844 "GPR124, an orphan G protein-coupled receptor, is required for CNS-specific
  vascularization and establishment of the blood-brain barrier."]. IUPHAR/GtoPdb target 198 returns
  `{"GtoPdb Web Services":"No natural ligands found for target ID:198 "}` and an **empty**
  `/interactions` list — no agonist, no antagonist, no transducer record.
- **No coupling measurement for ADGRA2 — and this is now a published statement, not a search
  result.** GtoPdb has no transduction comment for ADGRA2, and the 2025 study that *did* measure
  coupling in this clade says it outright: *"Whereas ADGRA2 has never been shown to couple to
  heterotrimeric G proteins, it has been extensively studied for its role in the assembly of a
  complex signalosome"* [PMID:40127866]. `"GPR124 Stachel"` and `adhesion GPCR GPR124 tethered
  agonist` both return **0** PubMed records — an ADGRA2-specific negative that stands.

> ### CORRECTION: my search returned nothing; that is not the same as nothing existing
>
> This review originally asserted, in the notes and at **four places** in the YAML, that *no*
> G-protein coupling assay exists for ADGRA1, ADGRA2 **or** ADGRA3, and none for the ADGRA clade.
> **That is false**, twice over:
>
> - **ADGRA3** — *"We found low-level activation of Gi and Gs by ADGRA3 and slightly more by its
>   CTF."*, and removing the first three residues of the stachel tethered agonist gave
>   *"abrogated G protein-mediated signaling"* [PMID:40127866].
> - **ADGRA1** — *"ADGRA1 activates several G proteins, notably Gα13"*, on the full TRUPATH BRET2
>   panel [PMID:41961591].
>
> **Why the sweep missed it, which is the reusable part.** The query recorded above requires
> `"G protein coupling"` / `"coupling profile"` / `"constitutive activity"` / `"transducer"` in
> `[tiab]`. The ADGRA3 abstract says *"G protein-mediated signaling"* and *"Gi and Gs"* and contains
> **none of the four**. So the query was **too narrow, not the corpus stale** — re-running it any
> number of times would never have surfaced the paper. A keyword conjunction over a field as
> variable as an abstract is a filter whose false-negative rate is unknown to the person running it.
>
> **And the sharper distinction.** These notes phrased it defensibly — a *corpus-level negative
> about the literature, not an inference about the protein*. The YAML did not: it promoted "my query
> returned nothing" into "no such study exists". Those are different propositions and **only the
> first was ever mine to assert.** The same failure mode as quoting an abstract-only paper about its
> full text, in a new costume: an epistemic upgrade smuggled in while restating a true finding.
>
> **The correction runs in my favour, which is worth stating so it does not read as damage control.**
> ADGRA2 itself still has no coupling assay, and now has a published statement saying so — stronger
> evidence than an absence of hits. And a clade in which two of three paralogs demonstrably couple
> makes `MARK_AS_OVER_ANNOTATED` **better** founded than `REMOVE` on the InterPro rows: a fold-based
> inference of coupling is not absurd for an ADGRA protein, it is merely unverified for this one.
> The two `REMOVE`s rest on the projection test and are untouched.
>
> **How it was found: not by me.** The paper reached this branch only because the sibling ADGRA3
> review merged and brought its cached publication along. Reviewing paralogs in parallel is what
> caught it — the same pairing the brief calls the campaign's richest source of findings.
- **The one G-protein contact points the other way.** Gβγ binds the ADGRA2 C-tail rather than being
  released by it: *"In addition, Gβγ interacts with the C-terminal tail of GPR124 and promotes the
  formation of a GPR124-Elmo complex."* [PMID:28600358]. That is Gβγ acting on receptor-complex
  assembly, the reverse of the GO definition's Gα nucleotide exchange. The same abstract states the
  starting position plainly: *"However, the signaling properties of GPR124 remain poorly defined."*
  [PMID:28600358] — and the assays there are ectopic-expression based ("ectopic expression of GPR124
  promotes cell adhesion"), i.e. IMP-grade, not a direct coupling measurement.
- **UniProt says so itself.** The FUNCTION block states the characterised activity does not use the
  GPCR machinery: *"ADGRA2-tethering function does not rely on its G protein-coupled"* … *"receptor
  (GPCR) structure but instead on its combined capacity to interact with"* … RECK extracellularly and
  Dishevelled intracellularly (PubMed:30026314)
  [`file:human/ADGRA2/ADGRA2-uniprot.txt` CC FUNCTION, lines 221–224 — the sentence spans three
  `CC ` continuation lines and cannot be quoted verbatim on one line].

Conclusion: the GPCR-activity claim is **unmeasured**, not refuted. The architecture is real and a
coupling assay has never been run and failed; per the ACBD3 lesson, an absence of reports is not a
demonstration of absence.

**But the four rows are not equally defective, and the actions are calibrated to the difference.**

| route | rows | action | why |
|---|---|---|---|
| InterPro2GO | `GO:0004930` IEA, `GO:0007186` IEA | `MARK_AS_OVER_ANNOTATED` | The signature genuinely matches ADGRA2. The inference has a real, if over-extended, basis. |
| GDB `TAS` | `GO:0004930` TAS, `GO:0007186` TAS | **`REMOVE`** | `TAS` asserts a *traceable author statement* about this gene, and the reference cannot supply one. **The stated evidence does not exist** — argued from the annotation distribution, not from the full text (see below). |

The `REMOVE` is on **evidentiary** grounds, not on the grounds that ADGRA2 provably lacks GPCR
activity — the two are different claims and conflating them is what makes the calibration look
inconsistent. Because the InterPro rows remain, removing the TAS rows does not erase the claim from
GOA; it removes two rows whose cited support is absent. This is complementary to, not a substitute
for, the `suggested_questions` item asking GO whether the whole 78-annotation GDB block across 27
entities should be retired: that is a consortium-level decision, this is the gene-level one.

**Divergence from the merged ADGRA3 review, stated rather than left to be noticed.** ADGRA3 (#2315)
`ACCEPT`s both `PMID:15203201` TAS rows — *"right conclusion, weak provenance - kept because the
conclusion has since been earned"* — and recommends GOA re-evidence them against PMID:40127866.
This review `REMOVE`s the identical pair. **Both follow one rule**: a defective TAS row is kept
where the claim it makes is independently established *for that gene*, and removed where nothing
else on the gene carries it. ADGRA3's claim was earned by a direct Gi/Gs measurement; ADGRA2's was
not, and the same paper says so. The rule is visible inside this review too, which is the check that
it is a rule and not a rationalisation: the `GO:0016020` TAS row from this very block is kept on
exactly ADGRA3's logic. Flagged per the AADACL2/3/4 precedent, where three reviews gave one row
three answers and nobody reconciled them until afterwards.

**Stated within what the cache supports.** PMID:15203201 is `full_text_available: false`, so this
review does *not* claim to know what its full text contains — that would be the same unsupported
assertion it objects to elsewhere. Two things are claimable and they suffice: the **abstract**
describes genome-database searching, phylogenetic analysis and EST expression charting and reports
no functional assay on any receptor; and the **projection test needs no full text at all**, because
a paper cannot make 25 gene-specific author statements about G-protein coupling — two of them about
pseudogenes — as a by-product of cataloguing a repertoire.

**And what is deliberately *not* removed.** The `GO:0016020` TAS row from the same GDB block carries
the **identical** evidentiary defect and would be a legitimate `REMOVE` on the same reasoning. It is
kept because removing it would achieve nothing: membrane localisation is directly demonstrated for
ADGRA2 elsewhere in this very GOA record — three `EXP` rows, an `IDA` and an `IBA` to the child term
`GO:0005886` — so that row is redundant rather than misleading. Leaving the asymmetry unexplained
would have made the calibration look arbitrary; the rule is *remove where the defective row is
carrying the claim, flag where it merely duplicates a directly demonstrated one.*

### A reviewer suggestion that is factually wrong: `GO:0060070` and `GO:0090263` are not redundant

Core function 1 lists both `GO:0060070 canonical Wnt signaling pathway` and
`GO:0090263 positive regulation of canonical Wnt signaling pathway` under `directly_involved_in`, and
this was flagged as listing a term together with its child. It is not. QuickGO
`/ontology/go/terms/GO:0090263/ancestors?relations=is_a,part_of` returns 18 ancestors and
**`GO:0060070` is not among them**; `GO:0060828 regulation of canonical Wnt signaling pathway` is.
Reading it from the other end, `GO:0060070`'s child list gives the relation explicitly:

```
GO:0090263  positively_regulates
GO:0090090  negatively_regulates
GO:0060828  regulates
GO:0061316 / GO:0044336 / GO:0044337 / GO:0044338   is_a
```

GO deliberately keeps regulation terms out of the subsumption hierarchy of the process they
regulate, so neither term entails the other: `GO:0060070` says ADGRA2 participates in the pathway,
`GO:0090263` says it increases its output. Both are separately annotated in GOA (IDA and IBA
respectively) and both are retained. Same shape as the ABR lesson (GO keeps the Rac and Rho
regulation branches disjoint) and the ACTMAP one (proteolysis and protein-modification disjoint) —
a `positively_regulates` edge in a child listing reads like subsumption and is not.

### Where the claim actually enters GOA — and it is NOT the retired SPKW route

The campaign brief predicts that this error class was swept out of GOA by the ~April 2026 retirement
of Swiss-Prot-keyword annotations, surviving only in the UniProt entry. **Half confirmed, half
refuted, on the same gene:**

*Confirmed for the KW route.* Q96PE1's `DR GO;` block contains **no `IEA:UniProtKB-KW` line at all**,
while the flat file still carries `KW G protein-coupled receptor;`, `KW Receptor;` and
`KW Transducer;`. The keyword is live upstream and gone from GO — exactly as ADCK5 predicted.

*Refuted for GOA overall.* ADGRA2's GOA still carries four GPCR-signalling rows, by **two routes the
SPKW retirement never touched**:

1. **InterPro2GO** (`GO_REF:0000002`): `GO:0004930` from `IPR000832|IPR001879|IPR017983|IPR036445`
   and `GO:0007186` from `IPR000832|IPR017983`.
2. **`TAS` assigned by GDB**, citing **PMID:15203201**, Bjarnadóttir et al., *"The human and mouse
   repertoire of the adhesion family of G-protein-coupled receptors"* (Genomics 2004).

### Which signature licenses which term — InterPro2GO already draws the line

`ADGRA2-bioinformatics/interpro_signatures.py` resolves every InterPro token in the GOA WITH/FROM
and cross-checks it against the authoritative `interpro2go` mapping:

| entry | InterPro name | type | interpro2go targets |
|---|---|---|---|
| `IPR017981` | GPCR, family 2-like, 7TM | domain | `GO:0004888`, `GO:0007166`, `GO:0016020` |
| `IPR000832` | GPCR, family 2, secretin-like | family | `GO:0004930`, `GO:0007186`, `GO:0016020` |
| `IPR017983` | GPCR, family 2, secretin-like, conserved site | conserved site | `GO:0004930`, `GO:0007186` |
| `IPR001879` | GPCR, family 2, extracellular hormone receptor domain | domain | `GO:0004930`, `GO:0016020` |
| `IPR036445` | GPCR family 2, extracellular hormone receptor domain superfamily | superfamily | `GO:0004930`, `GO:0016020` |

Two things fall out.

**InterPro curators already made the distinction this review argues for.** `IPR017981` is the entry
covering ADGRA2's transmembrane bundle, and InterPro describes it as *"the transmembrane domain of
family 2 GPCR receptor proteins and Frizzled proteins"* — Frizzleds being the textbook 7TM family
whose principal signalling is not through heterotrimeric G proteins. Accordingly `interpro2go` maps
it **only** to the generic `GO:0004888`/`GO:0007166`, never to `GO:0004930`/`GO:0007186`, and that is
exactly the pair of terms ADGRA2 receives from it. The restraint is deliberate and it is a built-in
negative control: when a signature's membership includes non-coupling 7TMs, the mapping is generic.

**The over-reach comes from the hormone-receptor entries.** `IPR001879` and its superfamily
`IPR036445` are *not* the GPS or GAIN entries — they are the family-2 **extracellular hormone
receptor** domain, which InterPro calls *"the major ligand recognition domain"* and exemplifies with
the calcitonin, corticotropin-releasing-factor 1, diuretic hormone, GLP-1 and parathyroid hormone
receptors. ADGRA2 matches them on its GAIN/hormone-receptor module. So a **peptide-hormone
ligand-recognition** signature is being converted into "activates a G protein" for a receptor that
has no ligand at all. That is a sharper and more testable objection than a generic
fold-became-an-activity complaint.

> **My own error, recorded because it had already reached the prose.** I hand-wrote these five
> labels and **three of five were wrong**, two substantively: I called `IPR001879` the "GPCR
> proteolysis site (GPS) domain" and `IPR036445` the "GAIN domain superfamily". Both are the
> hormone-receptor domain and its superfamily. This is the ACBD3 GOLD-versus-Q error exactly — a
> domain misassignment propagating into an argument — and it was caught only by scripting the
> comparison against InterPro instead of reading my own list back. The labels are now computed, the
> comparison is a committed guard with a self-test, and the guard additionally asserts that every GO
> term a row claims is one `interpro2go` actually licenses for that signature. Correcting it made
> the argument stronger, not weaker.

The TAS block is the interesting one and the projection test settles it. Querying QuickGO by
*reference* rather than by gene (`?reference=PMID:15203201`, fully paginated, 78 = 78):

| | |
|---|---|
| annotations | **78** |
| distinct entities | **27**, all human |
| evidence | 100% `TAS` |
| assignedBy | 100% `GDB` |
| terms | `GO:0016020` (27 entities), `GO:0007186` (26), `GO:0004930` (25) |

Twenty-seven entities receiving one identical generic triple from one reference is the shape of a
**bulk classification import**, not 27 traceable author statements.

**The pseudogene sub-claim, checked rather than inferred.** "Two of the recipients are pseudogenes"
does not follow from the 25-of-27 distribution — that figure is equally consistent with ADGRE4P and
ADGRF2P being the two that *missed* the molecular function. The per-entity matrix settles it: the two
entities that do not receive `GO:0004930` are **ADGRG3** and **ADGRV1**, both protein-coding, so both
pseudogenes are confirmed among the 25 that do. `projection_test.py` checks them by name and fails
loudly if either drops out, so the claim cannot silently rot. The paper itself performs no
functional assay on any of them — it is genome mining plus phylogenetics plus expression:
*"Here, 2 new human adhesion-GPCRs, termed GPR133 and GPR144, have been found by searches done in
the human genome databases."* and *"EST expression charts for the entire repertoire of
adhesion-GPCRs in human and mouse were established."* [PMID:15203201]. Two of the 27 recipients —
**ADGRE4P and ADGRF2P — are pseudogenes**, which a molecular-function assertion should not reach.

Applying the ACTR8/ACTRT3 two-question discriminator: (1) the reference annotates 27 entities with
identical evidence; (2) there is **no perturbed gene at all** for a functional term to stay on,
because no gene was perturbed. Both answers point to projection.

## 3. What ADGRA2 actually does

**Wnt7-specific co-activation of canonical Wnt signalling — the core function.** ADGRA2 and RECK
together let brain endothelium read WNT7A/WNT7B specifically: *"Gpr124 and Reck enable brain
endothelial cells to selectively respond to Wnt7."* [PMID:30026314]. RECK is the Wnt7 receptor;
ADGRA2 makes the Reck-bound ligand available to Frizzled by nucleating a higher-order complex —
*"Through polymerization, Dishevelled recruits Gpr124 and the associated Reck-bound Wnt7 into
dynamic Wnt/Frizzled/Lrp5/6 signalosomes, resulting in increased local concentrations of Wnt7
available for Frizzled signaling."* [PMID:30026314]. Independently:
*"WNT1- and WNT7B-mediated synergistic Wnt signaling requires FZD5, FZD8 and LRP6, as well as the
WNT7B co-receptors GPR124 (also known as ADGRA2) and RECK."* [PMID:28289266].

That is a **scaffolding/adaptor** activity, and GO already has the right term:
`GO:0030159 signaling receptor complex adaptor activity` — *"The binding activity of a molecule that
provides a physical support for the assembly of a multiprotein receptor signaling complex."*
The precedent is exact: **CD19**, a B-cell co-receptor, holds `GO:0030159` by EXP; CDH5, LAT, IRS1
and MAGI2 hold it too. ADGRA2 currently holds **no** informative MF term, so this is a real gap and
is proposed as a `NEW` row.

**Physiology.** *"Expression of GPR124 was found to be required for invasion and migration of blood
vessels into neuroepithelium, establishment of BBB properties, and expansion of the cerebral
cortex."* [PMID:21421844] — a mouse global and endothelial-specific knockout. Keep function and
phenotype separate: this establishes the BP rows (CNS angiogenesis, BBB) but on its own says nothing
about the molecular activity.

**A second, shed-ectodomain activity that GO does not record at all.** The ectodomain is released
and, after further processing, engages integrin αvβ3 through the cryptic RGD:
*"Matrix metalloprotease 9-processed, but not full-length, sTEM5 mediated endothelial cell adhesion
by direct interaction with integrin alpha(v)beta3."* and *"We found that sTEM5 binds to several
glycosaminoglycans."* [PMID:16982628]. UniProt records both as human experimental facts
(`ECO:0000269|PubMed:16982628`). Neither `GO:0005178 integrin binding` nor
`GO:0005539 glycosaminoglycan binding` appears anywhere in ADGRA2's GOA. Two `NEW` rows.
The shedding route is further characterised in [PMID:22013897]:
*"Binding of N60 to RGD-dependent integrins may modulate cellular functions such as adhesion and
migration during angiogenesis."*

**A third arm, weaker.** ADGRA2 promotes Rac/Cdc42-dependent adhesion via Elmo/Dock and ITSN1
[PMID:28600358], and mediates contact inhibition of endothelial proliferation — *"An excess of the
soluble TEM5 extracellular domain or an inhibitory monoclonal TEM5 antibody blocked contact
inhibition of endothelial cell proliferation"* [PMID:19853600]. Both rest on ectopic expression or
on blocking reagents, so they are IMP-grade; no GO row exists and none is proposed here.

## 4. The 21 `GO:0005515` rows are one biochemical fact, measured twice

`ADGRA2-bioinformatics/resolve_partners.py` builds the partner list **from the GOA TSV** (never by
hand — hand-maintained source lists have drifted on every gene in this campaign that tried it) and
resolves each accession. Result: **19 distinct partners, 19/19 reviewed Swiss-Prot at canonical
length**, no TrEMBL or ORFeome substitutions (the ACRV1 `Q86WV8`-for-TSC1 check, run and **negative**
here). The only length mismatch is `Q12959-2`, a genuine DLG1 splice isoform (926 vs 904 aa).
**18/19 carry at least one annotated PDZ domain**; the exception is that same DLG1 isoform
accession, whose feature list is not returned per-isoform — so effectively 19/19.

Both sources are large-scale PDZ-motif assays against the same C-terminal ETTV motif:
PMID:24550280 is proteomic peptide-phage display (*"we generated phage libraries containing all
human and viral C-terminal peptides using custom oligonucleotide microarrays."*) and PMID:36115835 is
quantitative holdup (*"we measure the affinities of 65,000 interactions involving PDZ domains and
their target PDZ-binding motifs (PBM)"*). The one non-screen source agrees: *"The PDZ domains of
hDlg bound the C-terminal PDZ-binding motif of TEM5."* [PMID:15021905].

So this is not screen noise — it is a real, quantitatively measured, and intrinsically promiscuous
motif–domain activity. Every row is `MODIFY` → **`GO:0030165 PDZ domain binding`**, which is
informative where bare `protein binding` is not, and is honest about the promiscuity in a way that
naming 19 individual partners as biological interactors would not be. **Not** core — see §6.

Cross-paralog check: ADGRA1 (Q86SQ6) and ADGRA3 (Q8IWK6) carry the **same** PMID:36115835 PDZ panel,
so the whole ADGRA family was profiled together. Counted from QuickGO rather than by eye, because
a first hand count of the ADGRA1 panel came out one short:

| gene | total `GO:0005515` | PMID:36115835 | PMID:24550280 | PMID:15021905 |
|---|---|---|---|---|
| ADGRA1 Q86SQ6 | 22 | 21 | 1 | – |
| ADGRA2 Q96PE1 | 21 | 18 | 1 | 2 |
| ADGRA3 Q8IWK6 | 19 | 18 | 1 | – |

Any future review of ADGRA1 or ADGRA3 should reach the same `GO:0030165` verdict on the same rows;
diverging silently from this one would repeat the AADACL2/3/4 failure.

## 5. PAINT node analysis — both directions of the node question

Only two PANTHER nodes appear in ADGRA2's WITH/FROM. `ADGRA2-bioinformatics/node_reach.py`
paginates QuickGO with a `numberOfHits == len(results)` assertion (never a page-size constant —
QuickGO clamps at 100 and a `limit=200` request silently returns 200 of 348).

| node | annotations | entities | **human reach** | terms given |
|---|---|---|---|---|
| `PTN002914520` | 136 | 29 | **ADGRA2 only** | `GO:0002040`, `GO:0007417`, `GO:0090263`, `GO:1990909` (+ `GO:0005886`/`GO:0007166` to 10 fish/shark entries) |
| `PTN001738137` | 348 | 174 | ADGRA1, ADGRA2, ADGRA3 | `GO:0005886`, `GO:0007166` |

**Reciprocal question, asked and answered negatively.** The node whose human reach is *exactly my
gene set* is `PTN002914520`, and what it gave ADGRA2 is sprouting angiogenesis, CNS development,
positive regulation of canonical Wnt signalling and the Wnt signalosome — precisely the four things
ADGRA2 is known for. No AADACL2/3/4- or ACTG2-style inversion here: the specific biology sits at the
ortholog node and the generic terms sit at the family node, which is the correct direction.
**This check came back negative and that is worth stating**, because on a gene whose paralogs are
under-characterised the null tells the next reviewer the check was run rather than skipped.

I nearly reported a false positive here. A single un-paginated `limit=200` query on
`PTN001738137` returned 200 of 348 rows, and human ADGRA1 and ADGRA3 were absent from that page —
which reads exactly like the ACTG2 "the family node misses the human paralogs" finding. Full
pagination shows all three are reached. The anti-truncation assertion is what converted a
publishable-looking finding into a non-finding.

**What PAINT did *not* give, and it is the most informative thing in the record.** Across all three
human ADGRA paralogs there is **not one MF IBA**, and the BP term PAINT chose is
`GO:0007166 cell surface receptor signaling pathway` — the *parent* — never
`GO:0007186 G protein-coupled receptor signaling pathway`. PAINT curators looking at this family
declined both the GPCR molecular function and the GPCR-specific pathway. InterPro2GO and GDB/TAS
assert both anyway. The two judgements sit side by side in the same GOA record, and PAINT's is the
better founded one.

Self-referential IBA: `GO:0005886`, `GO:0007166` and `GO:1990909` list `UniProtKB:Q96PE1` in their
own WITH/FROM. That is valid — a PAINT curator judging the function core — and is recorded as
`root_cause: NO_FAILURE_CORE`, never CIRCULAR.

Note also that ADGRA2 appears in `projects/paint/human-no-IBA-simple.csv`, a worklist of genes
*lacking* IBA, with all reviewer columns empty in `human-no-IBA.tsv`. It now has six IBA rows, so
PAINT has annotated PTHR45930 since the worklist was drawn.

## 6. ISS / Ensembl-Compara transfers: donor checked, all sound

Every non-IBA inferred row transfers from **mouse Adgra2, `UniProtKB:Q91ZV8`** (Swiss-Prot, 1336 aa)
— the true 1:1 ortholog, confirmed via `xref:mgi-1925810`. Querying the donor's own GOA (QuickGO,
35 = 35 hits) shows it holds its own **experimental** annotation for every transferred term:

| term | mouse Adgra2 evidence |
|---|---|
| `GO:0002040` sprouting angiogenesis | IMP PMID:23918385, IMP PMID:21071672 |
| `GO:0007417` CNS development | IMP PMID:21071672 |
| `GO:0043542` endothelial cell migration | IMP PMID:21071672 |
| `GO:0045765` regulation of angiogenesis | IMP PMID:21071672 |
| `GO:0050920` regulation of chemotaxis | IMP PMID:21071672 |
| `GO:0090210` reg. establishment of BBB | IMP PMID:21421844, IMP PMID:28288111 |
| `GO:0090263` pos. reg. canonical Wnt | IDA PMID:28803732 |
| `GO:0005886` plasma membrane | EXP PMID:25558062, IDA PMID:28803732 |

So none of these is a family-level guess, and `SOURCE_WEAK_OR_INFERRED` would be factually
contradicted by my own analysis. They are accepted.

The donor query also exposes a **coverage gap in the other direction**: mouse Adgra2 additionally
holds `GO:0010595 positive regulation of endothelial cell migration` (IDA, PMID:21421844),
`GO:0009986 cell surface` (IDA, PMID:21421844), `GO:0001525 angiogenesis` (IMP, PMID:21421844) and
`GO:1900747 negative regulation of vascular endothelial growth factor signaling pathway`
(IMP, PMID:21421844) — none transferred to human. `GO:0010595` is proposed as a `NEW` ISS row; it is
the *regulation* term whose unregulated parent `GO:0043542` did transfer, so this is a completeness
gap rather than the ACRV1 "propagation landed above its donor" defect (the donor holds both).

`GO:0009986 cell surface` is a stranger case: it is present in **UniProt's own `DR GO;` block** as
`IEA:Ensembl` but absent from GOA entirely. Reported as a UniProt/GOA inconsistency, not acted on.

## 7. Species caveat that UniProt does not carry

UniProt's FUNCTION attributes the Dishevelled-recruitment step to human ADGRA2 on PubMed:30026314,
whose central genetics is zebrafish. A later paper from the same laboratory reports that the
mammalian receptor does not need its intracellular domain for the Frizzled interaction:
*"By contrast, mammalian Gpr124 receptors exhibit an ICD-independent interaction mechanism governed
by species-specific attributes of their transmembrane and extracellular domains."* and, at results
level, *"These data imply that an alternative interaction modality exists between Fz4 and mouse
GPR124, which occurs independently of the recruitment of intracellular proteins to the GPR124 ICD."*
[PMID:35649360].

This does not disturb any GO row — `GO:1990909` and `GO:0060070` are about complex membership and
pathway participation, not about which domain mediates them — but it does mean the *mechanism*
sentence in UniProt is zebrafish-derived, and it makes the physiological role of the conserved human
ETTV motif and its 19 measured PDZ partners genuinely open. That is why `GO:0030165 PDZ domain
binding` is proposed as the informative replacement for `protein binding` but is **not** promoted to
a core function: the biochemistry is solid, the mammalian physiology is not.

## 8. What was checked and came back negative

Recording nulls so the next reviewer knows these were run, not skipped:

- **Node-placement inversion** (AADACL2/3/4, ACTG2 shape) — absent; specific terms are at the
  ortholog node, generic terms at the family node, correct direction.
- **Human paralogs missing from the family node** — absent once the query is paginated.
- **Paralog-transfer donors** — every IBA/ISS donor resolves to a genuine ADGRA2 ortholog
  (mouse Adgra2, zebrafish adgra2) or, on the family node only, to the true paralogs
  (mouse Adgra3 `MGI:1917943` → Q7TT36, zebrafish adgra3 `ZDB-GENE-131003-2` → S4X0Q8), which is
  legitimate for a node whose reach is the whole ADGRA family.
- **TrEMBL / ORFeome partner substitution** — absent; 19/19 partners reviewed and canonical.
- **`NbExp` inflation from sub-methods** — not applicable; the interaction data are affinity
  measurements from two named large-scale PDZ assays, not IntAct sub-method counts.
- **Retractions** — none. One Author Correction (PMID:36477203 → PMID:36115835).
- **Fold-name-became-an-activity in GOA** — **confirmed here**, unlike the three prior
  non-confirmations, but via InterPro2GO and GDB/TAS rather than the retired SPKW route.

## 9. WITH/FROM entity-type audit

Per-evidence-code semantics, checked by eye because `supporting_entities` is an unconstrained string
list and nothing validates it:

- `ISS` rows list `UniProtKB:Q91ZV8` alone — the sequence-similar entity. Correct.
- `IEA` Compara rows list `UniProtKB:Q91ZV8|ensembl:ENSMUSP00000033876` — ortholog plus its Ensembl
  protein. Correct.
- `IPI` rows list the interacting partner. Correct.
- `IBA` rows list the PANTHER node plus MOD-namespace seed genes (`MGI:MGI:1925810`,
  `ZFIN:ZDB-GENE-081104-363`, …). Correct, and the MOD ids were resolved rather than treated as
  opaque tokens.

No hand-written WITH/FROM was introduced; the `NEW` ISS row for `GO:0010595` lists only
`UniProtKB:Q91ZV8`.

## 9b. Merge conflicts with the sibling ADGRA3 review, and how they were resolved

ADGRA3 (#2315) merged first and touched two files this branch also adds. Both resolutions were
asserted rather than eyeballed, because the reflex is wrong on one of them.

**`interpro/panther/PTHR45930/PTHR45930-metadata.yaml` — took main's.** Both branches ran
`fetch-gene` on the same PANTHER family **27 seconds apart** (`19:50:35` vs `19:51:02`). Verified
line-by-line before choosing: the files are 54 lines each and **exactly one** line differs,
`_fetch_info.fetched_date`. Taking main's makes the file byte-identical to main, so this PR no longer
touches it at all — the right outcome for a cache whose only difference is when it was fetched.

**`publications/PMID_24550280.md` — took MINE, against the reflex.** main's copy is
`full_text_available: false`, 80 lines; this branch's is `true`, 101 lines, with an extracted
`## Full Text` section. Resolving toward main — "keep what is already merged" — would have **silently
downgraded a cached publication from full text to abstract-only**, the defect class PR #2287 fixed
repo-wide, and no validator would catch it. It matters here specifically: PMID:24550280 is one of the
two ProP-PD/holdup papers underpinning the `GO:0030165` call, so the full text is load-bearing.

The superset was asserted, not assumed, both before and after resolution:

```python
missing = [l for l in main_lines if l not in branch_lines and l.strip()]
assert missing == ["full_text_available: false"]
```

Generalised afterwards over **every** publication this PR touches that also exists on main: none is
downgraded.

**Then everything the earlier merges had established was re-verified**, because a later merge can
quietly undo an earlier resolution: all 18 gene files byte-identical to their pre-merge hashes;
`cache/go/terms.csv` compared as a **multiset**, so main's pre-existing duplicate curies `GO:0001675`
and `GO:0009566` are each confirmed still present **twice** (a set comparison would silently pass a
collapse); only `GO:0090210` added; no new duplicate curies; `just validate human ADGRA2` passing on
the merged tree; and `git status --porcelain` clean afterwards.

**One process note.** GitHub reported `CONFLICTING`/`DIRTY` after the push and then recomputed to
`MERGEABLE` — the stale-flag behaviour the campaign has seen repeatedly. My first local probe
*appeared* to confirm a conflict, but `git merge-tree --write-tree` does not exist in git 2.37
(added in 2.38), so the command had failed to parse and its non-zero exit read as "conflicts". A
rejected query and a real negative result are indistinguishable downstream unless the exit status is
checked. The authoritative probe is `git rev-list --count HEAD..origin/main`, which is **0**.

## 10. Files

- `ADGRA2-bioinformatics/node_reach.py` → `node_reach.json` — PANTHER node reach, paginated with a
  `numberOfHits == len(results)` assertion.
- `ADGRA2-bioinformatics/resolve_partners.py` → `partners.json` — GO:0005515 partners built from the
  GOA TSV; Swiss-Prot status tested with `startswith("UniProtKB reviewed")`, because `"reviewed" in
  entryType` also matches `"unreviewed"`.
- `ADGRA2-bioinformatics/check_corrections.py` → `corrections.json` — retraction/erratum/Crossref
  sweep, with `--self-test`.
- `ADGRA2-bioinformatics/check_coverage.py` — asserts the review covers every GOA row exactly once,
  and rejects duplicate YAML keys on the raw text.
- `ADGRA2-bioinformatics/interpro_signatures.py` → `interpro_signatures.json` — resolves every
  InterPro token in the GOA WITH/FROM, audits the review's `source_label` values against InterPro's
  own names, and asserts every claimed GO term is one `interpro2go` licenses for that signature.
- `ADGRA2-bioinformatics/check_action_prose.py` — asserts every annotation's prose names the action
  that annotation actually has, and that no reason argues the same point twice. Written after the
  fourth round in which a change landed on the structured field but not on every sentence describing
  it; it selects on `review.action` rather than by re-reading prose, which is how the misses happened.
- `ADGRA2-bioinformatics/projection_test.py` → `projection_test.json` — the GDB `TAS` projection
  test. This is the load-bearing evidence for the two `REMOVE` verdicts and was the last analysis
  here still being run ad hoc; it is now reproducible, emits the per-entity term matrix, and checks
  the pseudogene sub-claim by name.
