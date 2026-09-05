# AGT (angiotensinogen, P01019) — review notes

Human PAINT/affinage campaign. Sources: UniProt P01019 (ANGT_HUMAN, 476 aa), the
GOA TSV (114 rows), `AGT-deep-research-affinage.md`, the PANTHER PAINT slice for
PTHR11461, the cached publications, and three analyses in `AGT-bioinformatics/`.

## The shape of the problem

AGT is a heavily annotated gene whose annotation set is not really *about* AGT.
Sorting the 114 GOA rows by what molecule was actually assayed gives three layers:

| layer | what was assayed | rows |
|---|---|---|
| 1. the precursor itself | full-length secreted AGT protein | ~6 |
| 2. the released peptides | synthetic angiotensin I/II/(1-7) added to cells, or Ang II binding a receptor | ~45 |
| 3. neither | Reactome reaction membership, plasma proteomics, editorial statements, family inference | ~63 |

Layer 1 — the biology that is uniquely angiotensinogen's, and the only layer where
the 476-residue protein is the experimental subject — is almost entirely missing
from GOA. The single row that touches it is a bare `GO:0005515 protein binding`
against renin.

That framing decided most of the actions below. It did **not** lead me to strip
the layer-2 peptide rows: GOA's annotation unit is the UniProt accession, and
UniProt itself hangs the angiotensin functions on P01019 (as `FUNCTION:
[Angiotensin-2]`, `FUNCTION: [Angiotensin-3]`, `FUNCTION: [Angiotensin 1-7]`
sub-entries and as `PRO_` chain-level IntAct entries). There is no separate gene
for angiotensin II. Peptide pharmacology belongs on AGT. What does not belong is
(a) a serpin activity AGT provably lacks, and (b) treating every cellular
response to added Ang II as a process the gene product is *involved in*.

## 1. The serpin inhibitor leak — the clearest error

Three rows give AGT `GO:0004867 serine-type endopeptidase inhibitor activity`:
an IBA, an IEA from InterPro, and a TAS. The GO definition is *"Binds to and
stops, prevents or reduces the activity of a serine-type endopeptidase"*, which
is falsifiable, and it is false.

**Four independent lines say so.**

*Explicit statement in the primary structural literature.*
[PMID:20927107 "Blood pressure is critically controlled by angiotensins, which are vasopressor peptides specifically released by the enzyme renin from the tail of angiotensinogen-a non-inhibitory member of the serpin family of protease inhibitors."]

*Structural demonstration that the inhibitory mechanism is absent.* Serpins
inhibit by cleaving at the reactive centre loop and undergoing a stressed-to-relaxed
transition that traps the protease. Yan et al. crystallised loop-cleaved AGT
specifically to test this:
[PMID:30563843 "To confirm conclusions from biochemical experiments that cleavage of the reactive center loop of AGT does not trigger the stressed-to-relaxed (S-to-R) transition characteristic of inhibitory serpins, we solved the structure of AGT cleaved by thermolysin treatment and compared it with that of intact AGT."]
and, in the discussion,
[PMID:30563843 "In contrast, it has been shown that AGT has lost the ability to undergo this typical serpin S-to-R transition (29), confirmed here by our structure of loop-cleaved AGT, so it was very puzzling why the serpin framework was selected in the course of evolution as an angiotensin carrier."]

*Sequence features* (`AGT-bioinformatics/serpin_inhibitory.py`, 19-serpin panel).
UniProt annotates a `SITE` "Reactive bond" for 10 of the 12 inhibitors in the
panel and for AGT it annotates none. At the hinge position equivalent to
SERPINA1 Ala371 (P12), AGT carries **Pro430** — a proline where loop insertion
into β-sheet A requires a small residue. AGT's whole P17–P9 hinge reads
`ADEREPTES` (P01019 residues 425–433) against SERPINA1's `EKGTEAAGA`, 2/4 versus
4/4 small residues at P12–P9.

*MEROPS.* AGT is **I04.953**. MEROPS reserves the `.9xx` range of family I04 for
non-inhibitor homologues. Every one of the 7 resolvable seed proteins of the IBD
node that donated the term is in the inhibitor range (I04.001, I04.004, I04.027,
I04.082, …). 7/7.

And the physiology: AGT's protease partner is **renin, an aspartyl protease**, and
AGT is renin's **substrate**, not its inhibitor. The GO term is doubly wrong —
wrong catalytic class and wrong role.

### Where the propagation broke

The PAINT slice (`interpro/panther/PTHR11461/PTHR11461-paint.tsv`) shows the
family carries `GO:0004867` at three separate IBD nodes. AGT inherits from
**PTN008970140** (taxon:7711, Chordata), the SERPINA-clade node, seeded by
SERPINA1, SERPINA5, SERPINA9, bovine SERPINA3-1/A3-3, rat Serpinc1/Serpina1/
Serpina5 and mouse Serpina1b. All inhibitors. AGT is the one non-inhibitory
member of that clade and the inference reaches it mechanically.

This is `PROPAGATION_BAD`, not `SOURCE_BAD`: no seed annotation is wrong.

Worth recording, because it shows the fix already exists in this family: at node
**PTN002606963** PAINT curators entered an **IRD** (`negated=true`) against
`GO:0005576` to stop the extracellular-region inference reaching the
ER-resident serpin subclade. The machinery to block a bad propagation is in use
in PTHR11461; it simply has not been pointed at angiotensinogen for
`GO:0004867`. An IRD at the angiotensinogen node would fix all IBA-derived
copies at once.

The IEA copy has a different route but the same shape: `InterPro:IPR000215` is
`Serpin_fam`, the whole family. Note the contrast that makes this diagnosable —
AGT *also* matches two angiotensinogen-specific signatures, `IPR000227`
(Angiotensinogen) and `IPR033834` (Angiotensinogen_serpin_dom), and those map to
`GO:0003081 regulation of systemic arterial blood pressure by renin-angiotensin`,
which is exactly right. The family-level signature produces the wrong molecular
function; the gene-level signatures produce the right process.

The TAS copy is the origin story. It cites a 1988 mouse gene-cloning paper whose
own words are careful and hedged:
[PMID:3397061 "Because angiotensinogen is homologous to other members of the serine protease inhibitor family, we aligned the putative reactive center of angiotensinogens from various species."]
— *homologous*, *putative reactive center*, an alignment. The same abstract then
says the human site differs from the rodent one. A sequence-similarity
observation became a molecular function annotation.

## 2. What AGT actually does, and what GOA is missing

The layer-1 biology is genuinely interesting and entirely absent from GOA.

**AGT is not a passive substrate.** The renin cleavage site is buried and has to
be released by a conformational change:
[PMID:20927107 "The 63-residue amino-terminal tail of angiotensinogen is seen as an ordered superstructure, anchored by two new helices, and with the renin-cleavage site, Leu10-Val11 in humans, held in an inaccessibly buried position."]
The renin complex is not a simple active-site encounter:
[PMID:20927107 "In addition to the predicted7,8 intimate interaction between the N-terminal substrate (angiotensin I) region of angiotensinogen and the active site cleft of renin there is a substantial contact surface of 670Å2 between the bodies of the two proteins, primarily hydrophobic in nature."]
Yan et al. worked out the mechanism and showed the specificity determinants sit
outside renin's catalytic cleft:
[PMID:30563843 "These structures revealed that AGT undergoes profound conformational changes and binds renin through a tail-into-mouth allosteric mechanism that inserts the N terminus into a pocket equivalent to a hormone-binding site on other serpins."]
[PMID:30563843 "Mutagenesis and kinetic analyses confirmed that renin-mediated production of angiotensin I is controlled by interactions of amino acid residues and glycan components outside renin's active-site cleft."]

That is a real molecular function of the precursor and it is currently recorded
only as bare `protein binding`. **`GO:0002020 protease binding`** is the
informative replacement, and it is what the `GO:0005515` IPI against renin
(PMID:20927107) has been MODIFIED to.

**The pathway term that names angiotensinogen does not annotate angiotensinogen.**
`GO:0002003 angiotensin maturation` is defined as *"The process leading to the
attainment of the full functional capacity of angiotensin by conversion of
angiotensinogen into mature angiotensin in the blood."* Querying QuickGO for it
across human/mouse/rat returns 110 annotations covering essentially every other
participant in the cascade — REN, ACE, ACE2, ENPEP, ANPEP, MME, PREP, PRCP,
CTSG, LVRN, Ace3, and even ATP6AP2, the (pro)renin receptor — and **angiotensinogen
is not among them**. The same is true of `GO:0002002 regulation of angiotensin
levels in blood` (117 annotations, no AGT).

Both are added as `NEW`. The evidence runs in both directions from the same
models: knockout removes the product,
[PMID:7989296 "These mice do not produce angiotensinogen in the liver, resulting in the complete loss of plasma immunoreactive angiotensin I."]
and re-expression restores it,
[PMID:25691624 "High plasma renin concentrations in hepAGT-/- mice were suppressed equally by both forms of AGT, which were accompanied by comparable increases of plasma AngII concentrations similar to hepAGT+/+ mice."]

**The redox switch — and the negative that keeps it out of the review's claims.**
UniProt records `DISULFID 42..162` (mature Cys18–Cys138) and Zhou et al. built a
model on it: the bridge is labile, plasma holds a ~40:60 reduced:oxidised
mixture, and the oxidised form binds receptor-bound renin better
[PMID:20927107 "the prorenin receptor whilst having little effect on the reduced form gives a 4-fold increase in the renin-binding affinity (Km) of the oxidised form, with a consequent 4-fold increase in the catalytic release of angiotensin"].
It is a beautiful mechanism and I nearly proposed a GO term for it. Then I found
the in vivo test, which affinage did not surface:
[PMID:25691624 "These data indicate that the Cys18-Cys137 disulfide bond in AGT is dispensable for AngII production and AngII-dependent functions in mice."]
Cys→Ser mutants delivered by AAV into hepatocyte-specific Agt-null mice gave
equivalent plasma Ang II, systolic blood pressure and atherosclerotic lesion
size. So the structural observation stands but the physiological claim is
contested, and **no GO term is proposed for it**. It is recorded as a knowledge
gap instead.

The M235T variant is worth one line because it is so often mis-told. The
structure places it away from the functional sites:
[PMID:20927107 "This strengthens previous deductions5,6 that the predisposition to hypertension results from the small increase in concentration of the polymorphic angiotensinogen rather than a change in its function."]
Concentration, not function — which is also why `GO:0007267 cell-cell signaling`
TAS from the preeclampsia association paper (PMID:8513325) is not a real
functional annotation.

## 3. Rows where the citation does not support the term

Four of these, all checkable, none requiring me to second-guess a full text I
could not read.

**`GO:1903598 positive regulation of gap junction assembly` (IGI, PMID:17416596)
has the sign backwards.** The model is dTGR — rats carrying human renin *and*
human angiotensinogen, which is why the row is correctly coded IGI with
`UniProtKB:P00797`. The result:
[PMID:17416596 "Left-ventricular mRNA expression of potassium channel subunit Kv4.3 and gap-junction protein connexin 43 were significantly reduced in dTGR compared with Los-treated dTGR and SD."]
Connexin 43 goes **down** when the human RAS transgenes are active. MODIFIED to
`GO:1903597 negative regulation of gap junction assembly`.

**`GO:0008083 growth factor activity` (IDA, PMID:10406457) is contradicted by its
own paper.** The definition is "The function that stimulates a cell to grow or
proliferate". The cited study is an AT2-receptor intracellular-loop mutagenesis
in PC12 cells, and what it measures is
[PMID:10406457 "Deletion of residues 240-244 within the intermediate portion of the i3 loop resulted in a complete loss of AT2-mediated apoptosis, inhibition of extracellular signal-regulated kinases (ERK), and SHP-1 activation."]
— apoptosis and ERK *inhibition*. A second AGT-cited paper independently reports
no proliferative effect in its own system:
[PMID:15652490 "Moreover, Ang II induces a time- and dose-dependent augmentation in cell migration, but does not affect HUVEC proliferation."]
Marked over-annotated rather than removed, because Ang II is genuinely mitogenic
for vascular smooth muscle via AT1 — the term is not absurd, this citation just
does not support it.

**`GO:0003014 renal system process` (IDA, PMID:21183621) rests on an
autoantibody biomarker study.** The full text is cached and complete. It reports
that anti-angiotensinogen autoantibody titres are raised in chronic kidney
disease, and it explicitly cannot say what the antibodies even bind:
[PMID:21183621 "We cannot distinguish whether these auto-Ab are targeting angiotensinogen or angiotensin I, as cross-reactivity in antibodies against these two antigens has been described ( 33 )."]
There is no renal-process experiment in it. AGT's genuine renal biology is
already carried by `GO:0002019` and `GO:0035813`.

**`GO:0005515 protein binding` with the HCV F protein (IPI, PMID:16237761,
assigned by AgBase) could not be verified.** The cached full text runs from
abstract through the complete discussion, enumerates all 36 positive colonies by
identity, discusses each hit in turn, and never mentions angiotensinogen — the
word appears zero times. The serpin it *does* report is C1 inhibitor (SERPING1).
I have marked this over-annotated rather than removed and raised it as a
question for the assigning group, since a table that did not survive text
extraction cannot be ruled out.

## 4. The bulk: what 63 rows of layer 3 are made of

**27 rows are one fact.** All 27 Reactome TAS rows say `located_in GO:0005576
extracellular region`. They differ only in which reaction identifier is cited —
R-HSA-2022403 (renin:prorenin receptor cleaving AGT), R-HSA-2022368 (neprilysin
making Ang-(1-7)), and so on. That is 24% of AGT's GOA record expressing a single
correct claim once per reaction the protein or one of its peptides appears in.
The term is right, so each is accepted, but no one should read 27 as 27 findings.

**11 rows rest on a two-page editorial.** PMID:17159080 is typed
`Comment / Editorial / Review` in PubMed, is a comment on another paper, and the
cached record contains no abstract text at all — only the citation line. It is
the sole source for 11 GOA rows, four of them coded TAS (traceable author
statement) and seven NAS. Several of the terms are perfectly correct RAS
physiology (`GO:0002016`, `GO:0002018`, `GO:0002019`, `GO:0019229`,
`GO:0035813`) and those are accepted on the biology while the citation is flagged
in `reference_review`. The generic ones (`GO:0001558 regulation of cell growth`,
`GO:0042127 regulation of cell population proliferation`) are marked
over-annotated: uninformative terms with an unreadable source.

**10 rows are one large-scale yeast two-hybrid screen.** PMID:32814053 is an
interactome of *neurodegenerative disease* proteins. AGT is not one. Its ten
partners are, per UniProt: mitochondrial intermembrane space and matrix (NME4),
cytosol (EIF2B4), nucleus/cytoplasm (PRMT5, SLFN12), ER membrane (VKORC1L1),
trans-Golgi network (TGOLN2), dendrite (TMEM185A), membrane (SNX12), and two
with no annotated location (NPHP1, PRRG2). **0 of 10** share a compartment with
a secreted plasma protein (`AGT-bioinformatics/y2h_partners.py`). Y2H
reconstitutes a transcription factor in the yeast nucleus, so a signal-peptide-
cleaved, disulfide-bonded, four-site N-glycosylated protein is being tested
somewhere it never is. UniProt's `NbExp=3` on each is replicates within this one
study. None has functional follow-up. All ten marked over-annotated.

**5 HDA proteomics rows.** `GO:0005576` from colostrum and venous-hypertension
ECM proteomes is correct and accepted. `GO:0031012 extracellular matrix` (colon
cancer ECM), `GO:0070062 extracellular exosome` (prostatic-secretion exosomes)
and `GO:0072562 blood microparticle` (plasma microvesicles) are marked
over-annotated: an abundant plasma protein appears in every such preparation,
and detection is not localisation of function.

## 5. The IBAs, one by one

All four resolved through `resolve_withfrom.py`; 80 distinct WITH/FROM tokens
across the GOA file, 0 unresolved.

- **`GO:0005576` / PTN000156123 / 49 donors** — accepted, `NO_FAILURE_CORE`. The
  node is broad on purpose: its seeds include non-inhibitory serpins
  (SERPINF1/PEDF, SERPINA6/CBG, SERPINA7/TBG, ovalbumin) alongside inhibitory
  ones, because secretion is what they actually share. Correctly placed.
- **`GO:0038166 angiotensin-activated signaling pathway` / PTN008518321 /
  `MGI:MGI:87963` + `UniProtKB:P01019`** — accepted, `NO_FAILURE_CORE`. The node
  is angiotensinogen-specific, seeded by mouse Agt (P11859) and human AGT itself.
  **The target appearing in its own WITH/FROM is correct and expected** — AGT's
  own experimental annotation is one of the descendant evidences the PAINT
  curator used to place the IBD, so it is marked `SUPPORTS_TRANSFER`, never
  `CIRCULAR_OR_REDUNDANT`. A three-token donor list is not weak support here; it
  is a tight, correct clade.
- **`GO:0004867` / PTN008970140 / 9 inhibitor seeds** — removed,
  `PROPAGATION_BAD`. See §1.
- **`GO:0042981 regulation of apoptotic process` / PTN008518321 / mouse Agt +
  rat Agt + human AGT** — kept as non-core, `NO_FAILURE_NON_CORE`, **no failure
  mode**. It is tempting to call the bare parent a `GRANULARITY_MISMATCH`, but
  that only applies when a single direction is inherited and a more specific term was
  available. Angiotensin II is pro-apoptotic through AT2 (PMID:10406457, and AGT
  already carries `GO:2001238`) and anti-apoptotic/proliferative through AT1, so
  the neutral parent is the correct least common ancestor, not a defect. GO's own
  comment on the term endorses exactly this use.

## 6. ISS and IC rows

The six ISS rows (`GO_REF:0000024`) transfer from rat Agt (P01015) and mouse Agt
(P11859) — true 1:1 orthologues, not paralogues. I checked each donor actually
still carries the term via QuickGO, and all six do, with experimental evidence:
`GO:0005179` IDA PMID:8348686, `GO:0005576` IDA ×2, `GO:0010613` IDA
PMID:8348686, `GO:0014873` IMP PMID:8252633, `GO:0048146` IDA PMID:8348686,
`GO:0010718` IMP PMID:34615811. So `SOURCE_WEAK_OR_INFERRED` would be wrong for
all of them; they are `SUPPORTS_TRANSFER`.

The two IC rows infer `GO:0005179` and `GO:0005576` from `GO:0031702`. Both
inferences are sound — a molecule that binds a cell-surface angiotensin receptor
is extracellular and is acting as a hormone. They are kept as non-core and
classified `EVIDENCE_CIRCULAR_OR_REDUNDANT`, in the specific sense the enum
defines ("the target already has stronger direct evidence"): AGT already holds
both terms by IDA and ISS. The inference is not wrong, it just adds nothing.

## 7. Where affinage went wrong

The trust gate tripped (`self_evaluation_pairwise: tie`, not `win`), and the
record earns `LOW_QUALITY` on its own merits independently of that.

**It confused AGT with AGXT.** The narrative asserts: *"Independently of its
angiotensin-precursor role, AGT possesses peroxisomal alanine:glyoxylate
aminotransferase enzymatic activity required for glyoxylate-to-glycine
metabolism"*, citing PMID:40203111, a primary hyperoxaluria type 1 study in
`AgxtQ84-/-` rats. "AGT" is also the common abbreviation for alanine-glyoxylate
aminotransferase, whose HGNC symbol is **AGXT** (P21549) — a different gene, a
different protein, a different compartment. The error then propagates into
affinage's own GO grounding, which lists `GO:0016740 transferase activity` and
`GO:0005777 peroxisome` for a secreted plasma serpin. This is exactly why the
brief forbids importing `mechanism_profile` GO ids, and none were imported.

**Its recall was poor on the gene's own literature.** Of the 11 papers it cites,
**none** appears in AGT's GOA record, and it missed every paper that matters for
the molecular biology: PMID:20927107 (the Nature structure of AGT and of the
AGT–renin complex, and the redox switch), PMID:30563843 (the renin-specificity
structures and the loop-cleaved AGT that settles the serpin question),
PMID:7989296 (the angiotensinogen knockout mouse), PMID:25691624 (the in vivo
negative on the disulfide), PMID:12045255 (the prorenin receptor). I found these
by searching Europe PMC on the mechanism rather than the symbol — "angiotensinogen
Cys18 Cys138", "angiotensinogen AND renin AND crystal structure",
`TITLE:"angiotensinogen"` sorted by citation count. The affinage report's centre
of gravity is transcriptional regulation and cancer associations, which is where
the recent literature is, not where the gene's function is.

Not everything in it is wrong — the hepatic-knockdown and M235T-secretion items
are real — but nothing from it is cited as `supporting_text` for a mechanistic
claim in this review.

## 8. Deliberate non-findings

- **No GO term proposed for the redox switch**, because PMID:25691624 tested it
  in vivo and it was dispensable.
- **No removal of peptide pharmacology.** The receptor-binding and
  hormone-activity rows are correct under GOA's annotation unit, and UniProt
  attaches them to `PRO_` chains of the same accession.
- **The 0/3 compartment "mismatch" for AGTR1/AGTR2** in `y2h_partners.py` is not
  a finding. A secreted ligand meeting a cell-surface receptor is the normal
  case; the metric is only diagnostic for the yeast two-hybrid rows, and
  `RESULTS.md` says so.
- **I did not claim the serpin fold is degraded.** It is not:
  [PMID:20927107 "Although angiotensinogen has only 22% sequence identity to its closest relatives amongst other serpins3, it substantially retains the typical serpin fold"].
  The fold is intact; the *mechanism* is not. Those are different claims and the
  review only makes the second.

## 9. Reconciliation and validation

`AGT-bioinformatics/check_goa_reconciliation.py` maps every GOA row to exactly
one review entry on (GO id, evidence, reference, qualifier, normalised
WITH/FROM), verifies `supporting_entities` against the GOA field verbatim, and
requires `propagation_review` on every IBA/ISS/IEA/IC row that carries a
WITH/FROM (15 rows). 114 GOA rows map to 113 entries: the one collapse is a
genuine exact duplicate in GOA, `GO:0005179 IDA PMID:1567413 enables`, which
appears twice with identical fields.
