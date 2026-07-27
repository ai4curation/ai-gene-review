# AGFG1 (P52594, HRB / RIP / RAB) — review notes

Working journal for the GO annotation review. Computed results live in
`AGFG1-bioinformatics/RESULTS.md`; this file records the reasoning, the process
history, and the leads that did and did not pay off.

## What the gene is

562-aa protein with an N-terminal ArfGAP domain (UniProt `DOMAIN 11..135 Arf-GAP`,
`ZN_FING 29..52 C4-type`) followed by ~430 residues of low-complexity sequence carrying
ten phenylalanine–glycine (FG) repeats, three FxxFxxF AP-2-appendage motifs and NPF
motifs. Two names, two literatures: the 1995 HIV work (hRIP/Rab/RIP — a Rev cofactor)
and the 2001–2008 trafficking work (Hrb — an endocytic clathrin adaptor and an acrosome
biogenesis factor).

`PE 1: Evidence at protein level`, so the protein is detected; what is thin is
*biochemical* characterisation of the ArfGAP activity, not detection.

## Row-count reconciliation (do this first)

```
AGFG1-goa.tsv          36 lines = 35 annotations + header, 35 distinct
AGFG1-ai-review.yaml   34 '- term:' entries as seeded
```

The stub collapsed the two `GO:0005515 / IPI / PMID:25416956` rows, which differ only in
the WITH/FROM partner (`UniProtKB:P56282` POLE2 and `UniProtKB:Q9P242` NYAP2). Restored
to one entry per partner, so the review has **35** entries against 35 distinct GOA rows.
This is the documented `GOAValidator.seed_missing_annotations` behaviour (the seed key
omits WITH/FROM), not corruption — but it hides exactly the granularity that per-partner
judgement needs, and here the two partners get the same verdict only because they came
from the same screen.

## The paralogue question, answered rather than assumed

The task brief said "the shared name implies they are paralogues — verify that". Done
three ways in `paralogy.py`: shared PANTHER family `PTHR46134` with distinct subfamilies
SF1/SF4, identical InterPro signature sets, and 71.2% identity over the ArfGAP domain
(48.9% full length) against 48.2% for the accepted ARFGAP1/ARFGAP3 paralogue pair and
19.6% for an unrelated control. They are genuine, relatively recent paralogues.

### The finding: one node, two paralogues, one gene's evidence

`PTN002919572` carries `GO:0001675`, `GO:0007289` and `GO:0045109` to **36** gene
products, whose human reach is exactly {AGFG1, AGFG2}. All three rest on mouse *Agfg1*
IMPs and nothing else. Mouse and rat *Agfg2* are themselves IBA recipients, so no AGFG2
orthologue in any species carries experimental evidence for any of the three.

For AGFG1 this is an orthologue transfer from a decisive mouse null
[PMID:11711676 "male mice with a null mutation in Hrb are infertile and display
round-headed spermatozoa that lack an acrosome"], so the rows stand. For AGFG2 it is a
paralogue transfer. And AGFG2 has its own, unrelated characterised function — knockdown
in HUVECs halves stimulated von Willebrand factor secretion from Weibel–Palade bodies
[PMID:34369554 "In AGFG2KD cells, histamine-stimulated secretion of vWF was decreased"],
a paper that does not mention AGFG1 at all. So the divergence is real and the node's
reach is too broad.

Recommendation filed in `suggested_questions`, stated once with both genes named:
move the three terms from `PTN002919572` to the AGFG1-orthologue node
(`PTHR46134:SF1`). Relayed to the concurrent AGFG2 review as a **claim to verify**, not
as a fact.

### The reciprocal half

Two of AGFG1's own rows (`GO:0005737`, `GO:0031410`) carry `UniProtKB:P52594` in
WITH/FROM. On AGFG1 that is **self-referential** — a PAINT curator judging the function
core, which is valid. The byte-identical field on AGFG2 makes those rows
**paralogue-derived**. Same bytes, different evidential status; this is the AFF1/AFF4
pattern from the campaign brief, seen from the donor side.

## The "GAP domain in the name" lead: CONFIRMED after all — my first answer was wrong

> **Retraction, recorded rather than quietly overwritten.** The section below originally
> concluded that the pseudoenzyme hypothesis was NOT confirmed, because the arginine finger
> is intact. That was an artefact of testing **one** of the **three** residues the field says
> Arf GAP catalysis requires. AGFG1 retains one of three. `GO:0005096` moved from
> `KEEP_AS_NON_CORE` to `MARK_AS_OVER_ANNOTATED`. The reasoning below is preserved because
> it is still correct about what it tested and it is instructive about how the error
> happened; the correction is in the subsection that follows it.
>
> How the error happened, precisely: I anchored on `PMID:18809720`, which names the arginine
> and the four cysteines, and treated "the apparatus" as exhausted by what that paper names.
> The decisive paper — `PMID:23433073` — I had **fetched and then deliberately deleted**,
> reasoning that "nothing rests on it" because it looked like a family-classification paper.
> It contains the residue-level analysis that decides the question. The campaign brief's own
> warning applies exactly: a paper titled for the family holds the gene's answer, and an
> absence I created by not reading is not evidence.
>
> It was surfaced by the **concurrent AGFG2 review**, which is the strongest argument for
> reviewing paralogues in parallel that this gene produced. I verified it independently
> rather than inheriting it — see the subsection below — and the verification reproduced the
> sibling's AGFG2 number (Thr89) exactly while adding AGFG1, mouse Agfg1 and drongo.

## The original reasoning, preserved: the arginine finger is intact and the ADAP control matters

The brief flagged `PSEUDOENZYME_OVERANNOTATION` as the shape to look for. ~~It is absent
here~~ — **this sentence is the retracted claim; it is present here, see the correction
below** — and the check is still worth recording because the anchor is published rather than
remembered: `PMID:18809720` gives the ArfGAP catalytic spacing as
[PMID:18809720 "They contain a characteristic C4-type zinc finger motif and a conserved
arginine that is required for activity, within a particular spacing (CX2CX16CX2CX4R)."]
and names ArfGAP1's residues as Cys22/25/42/45 + Arg50. `arfgap_motif.py` reproduces
those numbers as a positive control and then finds AGFG1 intact at Cys29/32/49/52 +
**Arg57**. Both AGFG1 structures resolve the zinc on exactly those four cysteines
(2.26–2.40 Å), computed from coordinates with the SIFTS numbering offset handled.

But the same paper supplies the disconfirming control for the *opposite* over-reading:
[PMID:18809720 "Arf GAP activity has been demonstrated in vitro for at least one member
of each subfamily, with the exception of the ADAPs, which appear to lack in vitro GAP
activity."] — and ADAP1's CX2CX16CX2CX4R is complete. **An intact apparatus is necessary
and demonstrably not sufficient.** So the motif result cannot be used to certify
`GO:0005096` either.

**Round 2 of review caught that I was using half of that sentence.** Its first clause is a
blanket *positive* covering the AGFG subfamily — the paper puts the 31 human ArfGAPs into
ten subfamilies, AGFG is one, and only the ADAPs are excepted — so quoting the ADAP half as
a control while passing over the rest is the "verbatim but selectively bounded" defect, and
no gate can see it because the quote *is* verbatim. Both clauses are now argued, with four
checkable grounds for discounting the blanket clause's AGFG instance: it carries no
citation while the sentences either side of it do; it is stated at subfamily level and names
no species, protein or assay; the paper's own AGFG section supplies no measurement; and the
same paragraph warns that [PMID:18809720 "some ArfGAPs use their GAP domain to bind Arf
without promoting GTP hydrolysis"], which is precisely what a subfamily-level summary cannot
settle. Net effect on the verdict: none — but it does mean the clause raises the *prior* of
catalytic competence, which is part of why the row is kept rather than marked
over-annotated.

What tips `GO:0005096` to "keep, non-core" rather than "over-annotated":

* the *Drosophila* orthologue's GAP function is genetically required
  [PMID:31533044 "Notably, we found that the ArfGAP Drongo and its GTPase-activating
  function are essential for the initial detachment of the border cell cluster from the
  basal lamina."] and it acts against a specific Arf class
  [PMID:31533044 "Moreover, we show that toward the class III Arf, Drongo acts
  antagonistically to the guanine exchange factor Steppke."];
* human AGFG1 is placed with ARFs in a human proximity-labelling dataset
  [PMID:38606629 "AGFG1 was identified with class I classical ARFs (i.e. ARF1 and ARF3),
  the class III ARF (ARF6), as well as ARL8B and ARL13A."] — absent from GOA and from the
  affinage record;
* no GAP measurement on the human protein is reported by any source consulted here, and
  none for either human AGFG paralogue - a statement about those sources and about a
  recorded Europe PMC query, not an existence claim. `PMID:18809720`'s own AGFG section
  says only
  [PMID:18809720 "Much less information is available on AGFG2."] and says nothing about
  GAP activity for either.

That was the reasoning for `KEEP_AS_NON_CORE`, and it is superseded by the measurement below.

## The correction: two of three required residues are gone, subfamily-wide

`PMID:23433073` names three catalytically required positions in ASAP3 and states
[PMID:23433073 "Mutation of any one of these three residues leads to severe loss in Arf GAP
activity"]. R469 is the arginine finger; D484 contacts the Arf6 catalytic glutamine Q67 and
stabilises switch 2; W451 sits in the Arf–ArfGAP interface.

Measured in `catalytic_residues.py` with three controls that must all pass first — ASAP3's
own numbering still holding, **every GAP-competent panel member recovering all three**, and
the arginine agreeing with the independent motif scan (8/9 entries):

| protein | W451 | R469 | D484 | n/3 |
|---|---|---|---|---|
| ASAP3, ARFGAP1, ARFGAP3, ASAP1, SMAP1 | W | R | D | **3/3** each |
| **AGFG1 human** | **Y39** | R57 | **T71** | **1/3** |
| AGFG2 human | Y57 | R75 | T89 | 1/3 |
| Agfg1 mouse | Y39 | R57 | T71 | 1/3 |
| drongo | Y40 | R58 | A72 | 1/3 |

The source paper predicts exactly this from 40 AGFG sequences
[PMID:23433073 "Only two of the 40 AGFG sequences contain an aspartate at the position
homologous to D47 in the other subfamilies"] and
[PMID:23433073 "The AGFG consensus also uniquely lacks W14, which we predict to play a role in
hydrophobic interactions with Arfs."], and concludes
[PMID:23433073 "the ArfGAP is a very highly conserved structural domain that is predicted to
have lost substantial levels of GAP activity in at least one subfamily (AGFG)"].

**The reversal resolves the tension in my own evidence rather than creating one.** The ARF
proximity result had looked like support for catalysis; the same paper says it is not
[PMID:23433073 "These predicted changes (including complete loss, potentially) in GAP activity
or its regulation should not be confused with consequent changes in the ability to bind Arf
family GTPases."]. Binding retained + catalysis lost = an Arf **effector**. And the fly
genetics is reinterpreted rather than discarded: drongo scores 1/3 too, and an effector that
antagonises an Arf-GEF without hydrolysing GTP fits that genetics as well as a GAP does.

`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`: the domain is genuine, the zinc is really
bound, Arf binding is real, and no assay has been run on the human protein in either
direction.

Note GO has merged the substrate-specific GAP terms (`GO:0008060` and eight others are
`secondaryIds` of `GO:0005096`), so `GO:0005096` is already maximal and no substrate-
specific child should be proposed.

## The three legacy TAS rows are the real defects

All three come from the two 1995 discovery papers via ProtInc/PINC, each annotating
exactly one entity in all of GOA, and none exists on the mouse orthologue.

**`GO:0003723` RNA binding → REMOVE.** The direction of the interaction is inverted. The
cited paper has Rev binding the RNA and hRIP/Rab binding Rev's *protein* activation
domain [PMID:7634337 "Rab binds the Rev activation domain when Rev is assembled onto its
RNA target and can significantly enhance Rev activity when overexpressed."], and the
Rev–AGFG1 contact is not even direct [PMID:18809720 "The Rev–AGFG1 interaction is
indirect and possibly bridged by the nuclear export receptor CRM1."]. AGFG1 has no
RNA-binding module: the only nucleic-acid-suggestive feature is the ArfGAP C4 zinc
finger, which is buried and structural, and the FG repeats are protein-interaction
motifs that bind CRM1 and EH domains. UniProt records only a hedge — `FUNCTION: ... May
play a role in RNA trafficking or localization.` — and assigns no RNA-binding keyword.
Mouse *Agfg1* has zero `GO:0003723` rows. A recorded Europe PMC query found no study
reporting RNA binding by AGFG1 (that is a statement about the query, not the world).
Same shape as the ADIPOQ sialic-acid case: a *modification/partner* study read as a
binding activity.

**`GO:0005643` nuclear pore → REMOVE.** The term's definition is complex membership — "A
protein complex providing a discrete opening in the nuclear envelope" — and the cited
paper claims only sequence resemblance [PMID:7637788 "This hRIP protein has homology with
nucleoporins, a class of proteins that mediate nucleocytoplasmic transport."]. A primary
paper says so outright [PMID:10613896 "Second, it is not yet certain whether Hrb is an
authentic constituent of the nuclear pore complex (Bogerd et al. 1995; Fritz et al.
1995)."]. UniProt, curating the same two papers, records `Nucleus` and
`Cytoplasmic vesicle` and neither nuclear envelope nor nuclear pore. AGFG1 is not a
nucleoporin by any signature.

**`GO:0006406` mRNA export from nucleus → MODIFY.** The row is not false so much as
unable to say what it needs to: the evidence is entirely Rev/RRE-dependent *viral* RNA,
and the same lab later showed host mRNA is untouched [PMID:14701878 "We further show that
the RNA mislocalization pattern resulting from loss of hRIP activity is highly specific
to Rev function: the intracellular distribution of cellular poly(A)(+) mRNA, nuclear
proteins, and, most important, NES-containing proteins, are unaffected."]. The obvious
viral term cannot be used: `GO:0046784`'s definition and *all* its synonyms specify
**intronless** viral mRNA, while Rev exports unspliced and partly spliced (intron-
retaining) RNA. So the row goes to `GO:0075733 intracellular transport of virus`, whose
definition ("directed movement of a virus, or part of a virus, within the host cell") is
satisfied by what was actually measured, and the missing term is filed under
`proposed_new_terms`. This is a *sideways* move between the host-process and
viral-process branches, not a generalisation — `GO:0075733` is verified **not** to be a
descendant of `GO:0006406`.

## Protein-binding rows, decided per partner

* **VAMP7** (`PMID:18775314`) → MODIFY to `GO:0000149 SNARE binding`. One publication but
  three orthogonal methods including ITC; K_D 10.5 µM; a crystal structure; and paired
  mutations on both sides that abolish binding. The strongest molecular result on this
  gene.
* **POLE2** and **NYAP2** (`PMID:25416956`) → MARK_AS_OVER_ANNOTATED. Each is three
  IntAct records from **one** HuRI screen logged as `two hybrid array` +
  `two hybrid prey pooling approach` + `validated two hybrid` — the `NbExp=3` artefact —
  MI-score 0.56, no orthogonal assay. Neither partner is a promiscuous hub and neither is
  topologically inaccessible, so that arm of the argument is negative and the case rests
  on the single-screen evidence alone. Consistent with the corpus convention (554/803
  merged HuRI `GO:0005515` rows are marked over-annotated).
* **NXF3** (`PMID:11545741`) → UNDECIDED. The row's *validity* is not in doubt: the
  reference-projection test shows a curator annotated four proteins (AGFG1, NXF3, NXF1,
  XPO1) with five terms from that paper, so it is considered curation and not pipeline
  output. But the paper is not retrievable (Europe PMC `isOpenAccess N`, `inEPMC N`, no
  PMC id) and IntAct holds no record, so the informative molecular function that should
  replace bare `protein binding` cannot be identified. Per CLAUDE.md that is exactly what
  UNDECIDED is for.

## Cytosol: sixteen rows, one claim

Sixteen `GO:0005829` TAS rows differ only in the Reactome reaction id. One
(`R-HSA-8863718`, "AGFG1 binds VAMP7") is about AGFG1; the other fifteen are generic
downstream clathrin-mediated-endocytosis steps — BAR proteins binding the pit, SNX9
recruiting actin machinery, synaptojanin hydrolysing PI(4,5)P2, dynamin scission,
HSPA8-mediated uncoating — in which AGFG1 has no described role. They are pathway
membership carried through every reaction, not sixteen independent statements. Each gets
its own entry so the row count reconciles, all with the same verdict and a shared
analysis: `KEEP_AS_NON_CORE`. AGFG1 does have a cytosolic pool from which it is recruited
to coated pits, so the term is not wrong; it is just the least informative of its
locations.

## What GOA is missing (the coverage side)

`GO:0035615 clathrin-cargo adaptor activity`, `GO:0072583 clathrin-dependent
endocytosis`, `GO:0005905 clathrin-coated pit`, `GO:0030136 clathrin-coated vesicle` and
`GO:0008270 zinc ion binding` are all supportable and none is in GOA. The 2008 Cell paper
that establishes the mechanism has produced exactly **two** annotations in all of GOA,
both bare `GO:0005515` (on AGFG1 and on VAMP7), from a study with a structure, an ITC
constant, reciprocal mutagenesis and a depletion phenotype. That is an under-curation
gap of the AFF4 kind rather than an over-annotation problem.

One restraint worth recording: I did **not** propose `GO:0030276 clathrin binding`. The
paper calls Hrb a clathrin adaptor "in that it can be recruited into forming CCVs by its
interactions with AP2 appendages and clathrin (Figure S1 and Schmid and McMahon, 2007)" —
Figure S1 is the *sequence* figure and the citation is to a review, so the clathrin and
AP-2 contacts are motif-based inference in that paper, not measurements. The functional
term `GO:0035615` is supported by cargo binding plus colocalisation plus the depletion
phenotype; the direct clathrin contact is not.

Also not proposed: anything from `PMID:39089666` (AGFG1 raising cholesterol biosynthesis
via CAV1 in pancreatic cancer cells) or `PMID:15749819` (hRIP required for HIV-1
replication). Both are real human results absent from GOA, but one cancer-cell study is
not a basis for new process terms here. Noted as knowledge gaps instead.

## An unresolved contradiction in the literature, left unresolved

Two 2008 papers disagree about how general AGFG1's endocytic role is.
[PMID:18819912 "uptake experiments followed by fluorescence-activated cell sorting showed
that the endocytosis of fluorescent transferrin and pHLuorin-TI-VAMP is strongly reduced
in HRB knockdown cells."] argues for a general clathrin-dependent-endocytosis
requirement; the other reports the opposite for a different cargo — Pryor et al. found
that depleting Hrb "had no effect on the internalization and intracellular accumulation
of EGF nor on its degradation", which they read as evidence for a SNARE-*specific*
adaptor. Both are recorded; the review annotates `GO:0072583 clathrin-dependent
endocytosis` (which both support) and does not adjudicate the generality. The affinage
narrative states the general version as settled, which it is not.

## The Longin-domain artefact (a database defect, not a GO defect)

Gene3D assigns `G3DSA:3.30.450.50` "Longin domain" to AGFG1 residues 154–234 — a region
UniProt annotates as disordered and polar-biased. The cause is traceable: PDB 2VX8's
chains are a **fusion** of AGFG1 136–175 onto the mouse VAMP7 longin domain, exactly as
the authors describe building it, and the fold call has crossed the junction into AGFG1.
AGFG2, at 71.2% identity over the ArfGAP domain and with the identical InterPro set, has
no such assignment — so the error is keyed on having a chimeric PDB entry, not on family
membership. It currently produces no wrong GO term (the derived FunFam pair is one
condition of `ARBA00026971`, which grants only `cytoplasm`), so it is filed as a
CATH/Gene3D–UniProt correction request rather than acted on in GO.

## UniProt correction requests

* `KW DNA-binding` and `DR GO; GO:0003677; F:DNA binding; IEA:UniProtKB-KW` are not
  supported — see the RNA-binding argument above; the ArfGAP C4 finger is structural and
  fully occupied by zinc. GOA no longer imports the keyword route so there is no GO row
  to act on, which is why this is a UniProt request and not a GO action.
* `GO:0008270 zinc ion binding` is the mirror case: correct, keyword-derived, dropped
  from GOA, and structurally verified. It is proposed as a NEW GO annotation here.
* `SUBUNIT: Interacts with EPS15R and EPS15. Interacts with FCHO1.` has no counterpart in
  GOA. Those are curated interactions (`PMID:10613896`, `PMID:22484487`) that never became
  annotations.

## Process history

* Disk on the host was full (118 MB free on a 3.6 TB volume) at the start and blocked
  `git fetch`; cleared by removing pip/Homebrew/poetry *download* caches. Root cause
  appears to be several hundred full repo checkouts under
  `.claude/worktrees/`, which another process was already deleting.
* `donors.py` first reported "non-EXP only" for rows whose donors carry IMP, because it
  split a joined `acc:GO:0001675:IMP:PMID:...` string on `:` and read the term number
  where the evidence code should be. Fixed by carrying structured records. This is the
  campaign's substring-anchoring failure in yet another guise.
* `arfgap_motif.py`'s first run failed its own positive control (span computed as 28 for
  a 29-residue motif). The control is the only reason that was caught in one minute
  rather than shipped as a wrong residue number.
* `zinc_site.py` first reported Cys23/26/43/46 for 2D9L and failed its assertion; the
  cause was deposited author numbering being offset by +6 from UniProt. Fixed via SIFTS
  plus a per-residue identity check against the UniProt sequence.
* `node_reach.py` was first run over all five IBA terms and had to be stopped: `GO:0005737`
  has 593,028 IBA annotations. It now refuses to enumerate anything above a threshold and
  says so, rather than reporting a first-page number.
* The recipient composition of `PTN002919572` (21/12/3) was originally counted by eye;
  it is now computed with an assertion that the classes sum to the total, because the
  prose claimed it was computed.
* **Round 1 review found a real bug I had shipped:** `zinc_site.json` was written as `{}`
  because `main()` computed `r` for each PDB, printed it, asserted it, and never stored it
  in `results`. Every number reached stdout and none reached the artifact — and no gate
  could see it, because the `RESULTS.md` table it feeds still validated as a byte-exact
  quote. Fixed, and closed off as a class rather than an instance: `zinc_site.py` now
  asserts the payload before *and* after writing and re-reads what it wrote,
  `audit_review.py` check I fails on any empty JSON in the directory, and check J parses
  the rendered `RESULTS.md` table back out and asserts it agrees with the JSON. Both new
  checks are break-tested against the exact `{}` content that shipped in `e6ac0a131`.
* **The round-1 response turned a suggestion into a finding.** Asked whether an
  acrosome-associated CC should be proposed, I checked `GO:0001669`'s definition, found it
  denotes the *mature* organelle (which never forms in the null) and declined it — and the
  search surfaced `GO:0120211 proacrosomal vesicle fusion`, whose definition is the mouse
  phenotype verbatim and which is a verified descendant of the accepted `GO:0001675`. Added
  as a NEW ISS row with the mouse orthologue in `supporting_entities`.
* **One reviewer premise needed correcting rather than conceding.** The suggestion that
  `GO:0140312 cargo adaptor activity` "does not commit to clathrin" is not right: its
  definition reads *"Binding directly to the structural scaffolding elements of a vesicle
  coat (such as clathrin or COPII), and bridging the membrane, cargo receptor, and membrane
  deformation machinery"*, so retreating from `GO:0035615` to its parent would not avoid the
  coat commitment and would add a cargo-receptor clause that is wrong here (VAMP7 is the
  cargo). The substance of the point stands and is now acknowledged in the row; the proposed
  remedy would not have worked.
* `publications/PMID_18819912.md` carries `full_text_extraction_method: pdf_partial` and
  a `## Full Text` section containing only page boilerplate
  ("Preparing to download … HHS Vulnerability Disclosure"). The `full_text_available:
  false` flag is materially correct; the junk extraction is a cache-quality nuisance, not
  a stale flag, and was left alone.
