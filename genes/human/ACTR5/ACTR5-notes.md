# ACTR5 (ARP5, hARP5) — review notes

UniProt `Q9H9F9` · HGNC:14671 · 607 aa · `PE 1: Evidence at protein level` ·
chromosome 20 · MIM 619730.

Reviewed as part of the PAINT + affinage campaign. Sibling actin-family reviews
already merged: ACTB, ACTL7A, ACTL7B, ACTL8, ACTR1A, ACTR1B, ACTR10. A parallel
agent may be reviewing **ACTR8** (the other actin-related INO80 subunit); the
differences between ACTR5 and ACTR8 are set out under
"[Where ACTR5 and ACTR8 differ](#where-actr5-and-actr8-differ)" below.

---

## 1. What the gene product is

ARP5 is one of two actin-related proteins in the human INO80 chromatin-remodelling
complex. It is *not* a cytoplasmic actin: it is a nuclear ARP, and it sits in
INO80's catalytic **C-module** together with the Ino80 Snf2 motor, IES6/INO80C,
IES2/INO80B and the RuvBL1–RuvBL2 heterohexamer
[PMID:41775336 "INO80’s C-terminal region harbours the Snf2 domain (Ino80motor) and forms the nucleosome core particle mobilizing module along with nucleosome binding subunits ARP5 (actin-related protein 5), /IES6 (ino eighty subunit) subunit (INO80C), IES2 (INO80B), and the assembly chaperone heterohexamer AAA+ ATPases RuvBL1/RuvBL2 [28–30]."].
Human subunit mapping placed it there in 2011
[PMID:21303910 "a third that is composed of the hIno80 Snf2 ATPase domain, the Ies2 and Ies6 proteins, the AAA(+) ATPases Tip49a and Tip49b, and the actin-related protein Arp5"],
and the same study showed that catalysis requires the full conserved subunit set
[PMID:21303910 "ATP-dependent nucleosome remodeling by the hINO80 complex is catalyzed by a core complex comprising the hIno80 protein HSA/PTH and Snf2 ATPase domains acting in concert with YY1 and the complete set of its evolutionarily conserved subunits"].

hARP5 is predominantly nuclear but shuttles
[PMID:19014934 "We show here that hArp5 shuttles between the nucleus and the cytoplasm"],
and it complements a yeast `arp5Δ`
[PMID:19014934 "We show that human Arp5 (hArp5) proteins are localized in the nucleus, and that arp5Delta yeast cells are partially complemented by hArp5"] —
i.e. the ARP5 function is conserved from yeast to human, which is the biological
warrant for the phylogenetic (IBA) annotations discussed in §4.

## 2. The molecular function GO does not record: a nucleosomal-DNA grip point

This is the headline finding of the review.

ACTR5's GOA molecular-function record consists of exactly two things: one IBA to
`GO:0030234 enzyme regulator activity`, and fourteen rows of bare
`GO:0005515 protein binding`. **There is no DNA-binding, nucleosome-binding,
chromatin-binding or nucleotide-binding annotation of any kind** — even though
the mechanism has been resolved structurally in the human complex.

What the structures show. In the 2018 human INO80–nucleosome map the ARP5–IES6
module contacts the nucleosome on the face opposite the motor domains
[PMID:29643506 "The ARP5-IES6 module of INO80 makes additional contacts on the opposite side of the nucleosome"],
at SHL −2/−3
[PMID:29643506 "Our structure reveals these to be due to Arp5-Ies6 and are proximal to H2A/H2B on almost the opposite side of the nucleosome to those made by the motor domains (Figs 1b & 1c, Fig."].
The 2026 higher-resolution states identify the contacting element and the chemistry:
[PMID:41775336 "The DNA-binding domain (DBD) of ARP5 [30] interacts with nucleosomal DNA in the minor groove at SHL−3 in state N-7 and SHL−2 in state N-6, while it interacts with the hexasomal DNA at SHL+1 in state H-3 (Fig."]
and
[PMID:41775336 "ARP5 interacts with the phosphate backbone at the minor groove of DNA."].
So ARP5's contact is **sequence-independent nucleosomal DNA binding**, i.e.
`GO:0031492 nucleosomal DNA binding` (which is_a `GO:0031491 nucleosome binding`,
is_a `GO:0003677 DNA binding`, is_a `GO:0003682 chromatin binding`, so the single
specific term subsumes all three).

Why the qualifier must be `contributes_to` rather than `enables`: the *isolated*
protein does not bind nucleosomes at physiological concentration without IES6
[PMID:29643506 "b, A comparison of Arp5-Ies6 and Arp5 nucleosome binding activity assayed by EMSA, demonstrating a lack of nucleosome binding activity by Arp5 at in vivo relevant concentrations in the absence of Ies6."].
The functional unit is the ARP5–IES6 module.

Why it matters mechanistically: the module is the anchor that converts the Ino80
motor's ATP turnover into directional nucleosome translocation
[PMID:29643506 "The Arp5-Ies6 subunits couple ATP hydrolysis to nucleosome sliding in INO8010,19,20."],
[PMID:29643506 "The Arp5-Ies6 module also plays a key role in coupling ATPase and sliding activities10,19,20."].
In yeast the same conclusion is reached from the opposite direction — adding back
the module restores both ATPase and sliding, whereas an insertion-domain deletion
uncouples them
[PMID:26306040 "ectopic addition of the wild-type Arp5-Ies6 module stimulates INO80-mediated ATP hydrolysis and nucleosome sliding in vitro"],
[PMID:26306040 "the addition of mutant Arp5 lacking unique insertion domains facilitates ATP hydrolysis in the absence of nucleosome sliding"],
and the 2025 yeast study states the role directly
[PMID:39676660 "its necessity in linking INO80's ATPase activity to nucleosome movement"].

**Consequence for `GO:0030234`.** The vague parent should be replaced by two
informative terms: `GO:0060590 ATPase regulator activity` (exactly what the
donor's own IDA measured — modulation of an ATP hydrolysis activity) and, with
`contributes_to`, `GO:0140658 ATP-dependent chromatin remodeler activity` (the
activity of the machine ARP5 is an obligate part of).

The hierarchy here was checked in QuickGO and confirmed in OLS, and the first
version of this review got part of it wrong — corrected after review of #2291:

| term | its only `is_a` parent | descendant of `GO:0030234`? |
|---|---|---|
| `GO:0060590` ATPase regulator activity | `GO:0060589` nucleoside-triphosphatase regulator activity | **yes**, two steps down — *not* a direct child, as originally written |
| `GO:0060589` | `GO:0030234` | yes, directly |
| `GO:0001671` ATPase activator activity | `GO:0140677` molecular function activator activity | **no** |

So `GO:0001671` really is outside the `GO:0030234` branch (the reviewer's guess
that it sits under `GO:0060590` is not what either ontology service reports —
`GO:0060590`'s single `is_a` child is `GO:0000774` adenyl-nucleotide exchange
factor activity), but `GO:0060590` is a grandchild rather than a child, and
naming both `GO:0140677` and `GO:0098772` as `GO:0001671`'s parents was
redundant since `GO:0140677 is_a GO:0098772`.

`GO:0001671` is now **named as the available alternative rather than dismissed**:
it is the term the yeast add-back licenses, and a curator who weights
PMID:26306040's explicit stimulation result above the human coupling data should
use it. This review prefers the direction-neutral `GO:0060590` because the yeast
result is an ectopic reconstitution add-back of the whole module, and because in
human INO80 the mutations that break the ARP5/IES6-side nucleosome contacts lose
sliding while retaining robust ATPase — so what the *human* evidence isolates is
coupling, not stimulation.

## 3. Residues, in both directions: `ACTR5-bioinformatics/`

`ACTR5-bioinformatics/nucleotide_site.py` → `results.json` → `RESULTS.md`
(regenerating reproduces the committed report byte-for-byte; four deliberate
break-tests confirm the guards fire). Full numbers in
`file:human/ACTR5/ACTR5-bioinformatics/RESULTS.md`.

**Positive direction — a nucleotide really is there, in the actin site.** ADP is
modelled inside the ARP5 chain in **3 of the 6** human INO80 depositions
(7ZI4 3.2 Å, 9GCG 3.43 Å, 9GE5 3.35 Å; 12–16 ARP5 residues within 4.0 Å); ATP
never is. The ARP5 chain is identified from the PDBe SIFTS UniProt mapping, so a
missing `Q9H9F9` mapping aborts the run rather than producing a silent zero.
The **reciprocal** test — do ARP5's *observed* contacts land on positions that
align to β-actin's own ATP contacts in 2BTF? — gives 13/16, 11/14 and 8/12
(0.81 / 0.79 / 0.67). The retained contacts are actin's two phosphate-binding
loops (ACTB G13-S14-G15-M16-K18 → ACTR5 G38-S39-F40-Q41-R43; ACTB G156 → ACTR5
G189) and the adenosine shelf (ACTB G302/M305/Y306 → ACTR5 G496/M499/Y500). This
is the canonical actin cleft, not an adventitious surface site.

Every one of those depositions was prepared with ADP·BeF3
[PMID:41775336 "The structures were determined in the presence of the ATP analog ADP–BeF3 without any chemical crosslinking."],
which would ordinarily leave the identity of the ligand ambiguous. It does not
here, and this was **computed rather than argued** (added after review of #2291,
which asked exactly the right question): in all three entries the ARP5 chain
contains no BeF3, AlF, VO4 or PO4 group alongside its ADP, and in 7ZI4 the only
BeF3 in the whole entry sits in chain **G**, the Ino80 motor — which is where an
ATP mimic belongs. The soak therefore qualifies what the *motor* was trapped
with, not what ARP5 holds. What the structures still cannot do is rank ADP
against ATP, because no ATP was offered to ARP5 in solution; that limitation
stays in `knowledge_gaps`. `GO:0043531 ADP binding` follows the campaign's stated
rule ("annotate the ligand actually observed") and matches ACTR1A/ACTR1B.

Resolutions in the report are now the PDBe-reported values, fetched rather than
transcribed (6HTS 4.8, 7ZI4 3.2, 9GCG 3.43, 9GE5 3.35, 9GEV 3.47, 9GFB 3.55 Å).
These differ from the "3.5–3.7 Å" figures the 2026 paper quotes, which are its
own overall *map* resolutions for the nucleosome/hexasome states; both are
correct and the review now says which is which rather than mixing them.

**Negative direction — no ATPase, no filament.** Of the five literature-defined
actin catalytic positions (ACTB D11/Q137/D154/V159/H161, the same set the ACTL7A
audit used), ACTR5 keeps **2/5**: `DDSCH`. Asp11 and His161 are retained but
Gln137 — which orients the attacking water — plus Asp154 and Val159 are not. So
the pocket binds while the hydrolysis machinery is degenerate; no ATPase term is
warranted, and GOA asserts none. Independent corroboration: the already-merged
`genes/human/ACTL7A/ACTL7A-bioinformatics/results.json` computes the identical
string `DDSCH` for `ARP5_HUMAN`, and this script hard-fails on disagreement.

On the F-actin protomer interface (8A2S, 72 consensus positions) ACTR5 retains
**20.8%** identity, against **51.4%** for ARP1/ACTR1A — the one ARP that really
does polymerise, used here as the positive control — and 100%/94.4% for
ACTB/ACTA1. A 2.5-fold gap, unchanged under BLOSUM45 with a (−14,−2) gap model
(18.1%). ACTR5 cannot be expected to polymerise, and GOA correctly carries **no**
actin-binding, actin-filament or protein-polymerisation term.

**No cytoplasmic-actin leakage.** This was checked explicitly, in both of the
directions this campaign has been burned by. ACTL8's defect was a divergent actin
placed inside PANTHER's cytoplasmic β/γ-actin subfamily; ACTR10's was a
`GO:0005634 nucleus` IBA transferred from nuclear ARPs of a *different*
subfamily. Neither shape applies here: every resolvable WITH/FROM donor on every
ACTR5 IBA row is an ARP5 **ortholog** (§4), and ACTR5's nuclear localisation is
its own (three IDAs plus one EXP), not a transfer. The only cytoplasmic claim in
the record is ACTR5's own documented shuttling — see §5.

## 4. Every WITH/FROM donor resolved, and every donor's own evidence queried

Five PAN-GO IBA rows, `GO_REF:0000033`, all at PANTHER node **PTN000233752**
inside the pan-actin family PTHR11937. Accessions resolved with
`size=2`+ queries and `primaryAccession == requested` as the liveness guard:

| WITH/FROM token | resolves to | status | name |
|---|---|---|---|
| `FB:FBgn0038576` | Q9VEC3 (+ TrEMBL duplicate A0A0B4KG83, same gene, same name) | Swiss-Prot | Actin-related protein 5, *D. melanogaster* |
| `SGD:S000005004` | P53946 | Swiss-Prot | Actin-related protein 5, *S. cerevisiae* |
| `PomBase:SPBC365.10` | Q9Y7X8 | Swiss-Prot | Actin-like protein arp5, *S. pombe* |
| `AGI_LocusCode:AT3G12380` | Q940Z2 | Swiss-Prot | Actin-related protein 5, *A. thaliana* |
| `UniProtKB:Q9H9F9` | self | Swiss-Prot | ACTR5 — a self-referential IBA, i.e. a PAINT curator judging the function core |
| `PANTHER:PTN000233752` | internal tree node, not a protein | — | — |

This is the cleanest donor set the campaign has seen: **five for five reviewed
Swiss-Prot ARP5 orthologs, zero paralogs, zero unreviewed entries.** Contrast
ACTL8, where the node's other members were β-actin at ≥90% identity.

Donor evidence for the term each donated (QuickGO, `goUsage=descendants`,
experimental codes EXP/IDA/IPI/IMP/IGI/IEP/HTP/HDA/HMP/HGI/HEP):

| term | donors | each donor's own experimental evidence |
|---|---|---|
| `GO:0006338` chromatin remodeling | fly, pombe, yeast, self | fly IMP (PMID:16618800); pombe IDA (PMID:19933844); yeast IDA ×3 + IMP ×2 + IPI; self IDA (PMID:21303910) |
| `GO:0031011` Ino80 complex | fly, pombe, yeast, self | fly IDA+IPI; pombe IDA+IPI; yeast IDA ×2 + IMP + IPI ×2 |
| `GO:0006355` reg. of DNA-templated transcription | fly, self | fly IMP (PMID:16618800); self IMP via `GO:0045893` |
| `GO:0030234` enzyme regulator activity | yeast | yeast IDA (PMID:26306040) |
| `GO:0005737` cytoplasm | Arabidopsis, self | Arabidopsis IDA (PMID:19679120); self IDA (PMID:19014934) |

**Every donor carries its own experimental evidence for the term it donated.** So
`SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` are factually excluded here,
and no row was dismissed on source-quality grounds. The only propagation defects
found are (a) a qualifier that over-reaches (§5) and (b) a term the node holds
but never propagated (§6).

The bioinformatics panel adds that the four donor orthologs sit in the same
structural regime as human ARP5 — partly conserved nucleotide pocket (33–39%),
degenerate filament interface (15–22%), 1–2/5 catalytic positions — so the
nucleotide site and the loss of polymerisation competence are **family-wide ARP5
properties**, not human peculiarities.

## 5. The one propagation defect: `is_active_in cytoplasm`

`GO:0005737 cytoplasm` reaches ACTR5 three times: an IBA with
`is_active_in`, an IEA from `UniProtKB-SubCell:SL-0086`, and an IDA from
PMID:19014934, all `located_in` except the IBA.

The **term** is right. hARP5 genuinely visits the cytoplasm — that is the
gene's own finding
[PMID:19014934 "We show here that hArp5 shuttles between the nucleus and the cytoplasm"] —
and UniProt records `Cytoplasm {ECO:0000269|PubMed:19014934}` with the note that
the protein is predominantly nuclear. The donor is equally sound: Arabidopsis
ARP5 has its own cytoplasm IDA.

The **qualifier** is not. `is_active_in` asserts that the gene product carries out
its molecular function in that compartment. Every characterised ARP5 activity —
nucleosomal DNA binding, INO80 C-module assembly, chromatin remodelling, the DNA
repair phenotypes — is nuclear; nothing has been shown for the cytoplasmic pool
beyond its existence in transit. Recorded as `MARK_AS_OVER_ANNOTATED` with
`root_cause: TERM_SCOPING_PROBLEM` (whose definition explicitly covers a wrong
qualifier) and a PAINT recommendation to change `is_active_in` → `located_in` at
node PTN000233752. The `located_in` rows are kept.

## 6. A term the donor node holds and never propagated

Budding-yeast ARP5 (`SGD:S000005004`, P53946) — a WITH/FROM donor on four of the
five ACTR5 IBA rows — carries **`GO:0031491 nucleosome binding` IDA from
PMID:39676660** in its own record. That term has not reached ACTR5 or any other
ARP5 ortholog. Checked across the family with QuickGO: of ACTR5, fly, yeast,
pombe and Arabidopsis ARP5, plus human ACTR8, ACTL6A, ACTR6, ACTR1A and ACTR10,
**only yeast ARP5 (`GO:0031491`, IDA), ACTL6A (`GO:0031492`, HDA;
`GO:0003682`) and ACTR6 (`GO:0031491`, IBA) hold anything in the
nucleosome/chromatin-binding branch, and not one of the eleven holds a
nucleotide-binding term.**

So the missing MF is a family-level PAINT gap, not a human oversight — and it is
the same family-wide nucleotide-binding gap that the ACTR1A, ACTR1B and ACTR10
reviews independently reported for the dynactin ARPs. Filed as a single PAINT
recommendation in `suggested_questions`, naming the node once.

## 7. Histone binding: supported, but read the whole figure

Three pieces of evidence bear on whether human ARP5 binds histones directly.

1. **For.** Purified human ARP5 pulls down untagged H2A–H2B dimers
   [PMID:29643506 "Consistent with these contacts, Arp5 binds to H2A/H2B dimers in solution and the Arp5-Ies6 complex binds to nucleosomes (Extended Data Fig."],
   the experiment being
   [PMID:29643506 "a, Actin and Actin-related proteins were all expressed with a C-terminal double-Strep tag and used as bait to capture untagged H2A-H2B dimers."].
   IntAct curates ARP5–H2AC4 and ARP5–H2BC11 from this study (pull-down + 3d-em).
2. **For, from yeast, and it localises the surface.** Yeast Arp5 has two distinct
   nucleosome-proximal regions, and free-dimer binding maps to the second
   [PMID:39676660 "The other region has a hydrophobic/acid patch of Leu and Asp that binds free histone H2A-H2B dimers"],
   distinct from the arginine anchor that engages the nucleosome
   [PMID:39676660 "One region has an arginine anchor that binds nucleosomes and is vital for INO80 mobilizing nucleosomes"].
3. **Bounding it.** Human ARP5's insertion domain is truncated relative to the
   fungal "grappler"
   [PMID:41775336 "Human ARP5 has a much smaller insertion domain that particularly lacks the acidic patch binding foot."],
   and human nucleosome/hexasome recognition by this module is DNA-mediated
   [PMID:41775336 "The predominantly DNA-mediated hexasome binding contrasts yeast and fungal orthologs, where the Arp5 grappler insertion [30] (largely missing in human INO80) binds either the H2A/H2B acidic patch on the nucleosome or H3/H4 on the hexasome."].
   And the pull-down was n=1 at 20 µM bait / 40 µM prey — the *adjacent panel of
   the same figure* is the EMSA showing ARP5 alone fails to bind nucleosomes at
   in-vivo-relevant concentrations.

Reading (3) as refuting (1) would be the error the campaign made on ACTR10, where
a true verbatim quote was selectively bounded. The 2026 statement is about the
nucleosome **acidic-patch-binding foot**, which is a different surface from the
free-dimer-binding hydrophobic/acidic patch that the yeast work maps. So
`GO:0042393 histone binding` is proposed as a NEW annotation (IDA,
PMID:29643506), with the concentration/replication limitation and the missing
foot recorded in `knowledge_gaps` rather than suppressed.

## 8. `GO:0005515` — fourteen rows, adjudicated per partner

All five partner accessions resolve to **reviewed Swiss-Prot canonical entries of
the expected length** — no TrEMBL or ORFeome substitutions of the kind found on
ACRV1:

| accession | gene | length | reviewed | first GOA row |
|---|---|---|---|---|
| Q9H981 | ACTR8 (ARP8) | 624 | Swiss-Prot | PMID:16230350 |
| Q9ULG1 | INO80 | 1556 | Swiss-Prot | PMID:19014934 |
| Q16531 | DDB1 | 1140 | Swiss-Prot | PMID:20855601 |
| Q6PI98 | INO80C (IES6) | 192 | Swiss-Prot | PMID:26496610 |
| O60437 | PPL (periplakin) | 1756 | Swiss-Prot | PMID:32296183 |

Uniform rule applied, stated once so the verdicts are not ad hoc:

* **MARK_AS_OVER_ANNOTATED** where the partner is an INO80-complex subunit
  detected by co-purification / AP-MS / cryo-EM of the whole complex (11 rows:
  INO80, ACTR8 and INO80C in PMIDs 16230350, 19014934, 20855601, 26496610 ×3,
  29643506, 33961781 ×2, 35271311 ×2). Bare `protein binding` adds nothing that
  `part_of GO:0031011 Ino80 complex` does not already say, and whole-complex
  co-purification does not establish direct contact.
* **KEEP_AS_NON_CORE** for the two rows resting on targeted binary assays that
  make a distinct biological point: ACTR8 in PMID:18163988 (reciprocal co-IP,
  present in interphase and absent in metaphase-arrested cells — UniProt records
  this as evidence for INO80 dissociation in mitosis), and DDB1 in PMID:20855601
  (a **non**-INO80 partner, three assays in IntAct from that study, functionally
  coherent with the UV-damage-repair IMP on the same paper).
* **MARK_AS_OVER_ANNOTATED** for PPL. The IntAct record for PMID:32296183 logs
  this single HuRI screen three ways — `two hybrid array` + `two hybrid prey
  pooling approach` + `validated two hybrid` — which is where UniProt's
  `NbExp=3` comes from. Exactly the ACRV1 pattern: one experiment counted three
  times. Periplakin is a 1756-aa plakin cytolinker of desmosomes and the
  cornified envelope; there is no orthogonal assay and no follow-up.

IntAct check run in full (130 records): the only non-INO80, non-histone partners
are high-throughput singletons, including an *E. coli* `argI` two-hybrid hit
(PMID:20711500, a human–bacterial-pathogen interactome screen) which GOA has
correctly not imported.

## 9. ComplexPortal subunit projections: five rows whose experiments are on other subunits

Five IMP rows come from ComplexPortal annotating CPX-846 (the INO80 complex) and
projecting onto every subunit:

| term | reference | what the paper actually perturbed |
|---|---|---|
| `GO:0006275` reg. of DNA replication | PMID:25016522 | INO80 and **ARP8** |
| `GO:0060382` reg. of DNA strand elongation | PMID:25016522 | INO80 and **ARP8** |
| `GO:0033044` reg. of chromosome organization | PMID:26340092 | INO80 / "INO80 complex" knockdown |
| `GO:0051726` regulation of cell cycle | PMID:26340092 | as above |
| `GO:0045893` pos. reg. of DNA-templated transcription | PMID:27641337 | INO80 and INO80B in NSCLC |

PMID:25016522's **full text is cached and contains zero occurrences of "Arp5" or
"ACTR5"** (`grep -ci` = 0); its knockdowns were
[PMID:25016522 "cells deficient for Ino80 and Arp8 had impaired replication restart after treatment with replication inhibitors"]
and
[PMID:25016522 "INO80 was specifically needed for efficient replication elongation, while it was not required for initiation of replication"].
PMID:26340092 and PMID:27641337 are abstract-only in the cache, so what their
full texts assayed cannot be checked from here.

These are **not** removed. Projecting a complex-level process onto an obligate
subunit is legitimate GO practice, and ACTR5 is required for the complex's
catalytic activity (§1). They are marked `KEEP_AS_NON_CORE`: the biology is
INO80's, one step removed from ARP5's own molecular function. The evidence-code
question — IMP on a gene product that was not itself perturbed — is raised once,
as a recommendation to ComplexPortal/GO, not repeated per row.

## 10. ACTR5-specific transcriptional evidence, and what the record gets backwards

GOA gives ACTR5 `GO:0045893 positive regulation of DNA-templated transcription`
(IMP, from a paper about INO80/INO80B in lung cancer) and nothing negative. The
one study that assayed **ACTR5 itself** at a promoter found the opposite sign:

* ACTR5 occupies the *CDKN2A* promoter
  [PMID:36563143 "Furthermore, the presence of ACTR5 at the CDKN2A promoter region was confirmed by TST-mediated ChIP-seq and ChIP–quantitative polymerase chain reaction (qPCR) (Fig."];
* CRISPRi knockdown de-represses *CDKN2A*
  [PMID:36563143 "Suppression of ACTR5 activated CDKN2A expression, ablated"];
* and H3K9me2 at the *CDKN2A* TSS falls
  [PMID:36563143 "Our results revealed a significant reduction of H3K9me2 but not H3K27me3 at the CDKN2A TSS locus upon ACTR5 depletion (Fig."].

Hence a NEW `GO:0000122 negative regulation of transcription by RNA polymerase II`
(IMP), with the caveats stated in the row: HepG2/HCC-specific, single study, and
the study carries a 2025 erratum (PMID:41071901) correcting **Fig. 2D** — the
CDKN2A western — because the ACTR5 and U87 panels were inadvertently duplicated
from Fig. 3A. The publisher states the conclusions are unaffected, and the mRNA
(RNA-seq), ChIP-qPCR and H3K9me2 evidence is independent of the corrected panel.
The sign of ACTR5's transcriptional effect is therefore **locus-dependent**, and
neither the existing positive row nor the new negative row should be read as the
gene's general behaviour.

**The paper's "INO80-independent" claim is not adopted.** Its title asserts it,
but the support is the *absence* of a HepG2-selective essential domain in the
other subunits
[PMID:36563143 "Unexpectedly, none of these INO80 members exhibited a HepG2-selective essential domain, suggesting a distinct usage of ACTR5 in HCC that is unconventional to the INO80 complex."],
and the requirement it does map — the surface region A5 (G502–S519) — works
*through* IES6
[PMID:36563143 "Characterization of the ACTR5-associated proteins using MS (LC-MS/MS) revealed a unique loss of interaction between ΔA5-ACTR5 and IES6 in HepG2 cells (Fig."],
which is itself an INO80 subunit (INO80C). Differential CRISPR dependency can
reflect differential redundancy rather than complex-independence. Recorded in
`knowledge_gaps`, not as an annotation. Affinage's record rests almost entirely
on this paper and cites it without flagging the erratum.

## 11. Where ACTR5 and ACTR8 differ

Both are nuclear ARPs in human INO80, so the two reviews will overlap on the
complex and on the shared literature. They differ in three checkable ways:

1. **Module.** ARP5 is in the catalytic **C-module** with the Snf2 motor, IES6,
   IES2 and RuvBL1/2; ARP8 is in the **A-module** with nuclear actin, ARP4 and
   YY1, which binds extranucleosomal entry DNA [PMID:21303910; PMID:41775336].
2. **Mitosis.** ARP8, *not* ARP5, goes onto mitotic chromosomes
   [PMID:18163988 "Here we report that hArp8, but not hArp5, accumulates on mitotic chromosomes"],
   and ARP5 depletion does not disturb chromosome alignment
   [PMID:18163988 "depletion of hIno80 and hArp5 did not cause misalignment of chromosomes"].
   Any chromosome-segregation term belongs to ARP8, not ARP5.
3. **Nucleotide pocket.** In the bioinformatics panel ARP8 retains 55.6% of the
   actin nucleotide pocket but only **1/5** catalytic positions (`HEDKS`, losing
   even Asp11), versus ARP5's 44.4% and 2/5 (`DDSCH`). Neither is an ATPase; only
   ARP5 has an actually-resolved nucleotide (ADP, three structures).

Also note that the PMID:25016522 replication annotations projected onto ACTR5
(§9) rest on experiments in which **ARP8** was the subunit knocked down — so for
ACTR8 the same rows have direct support that they lack for ACTR5.

## 12. Actions taken

39 review rows, one per GOA line. The GOA TSV has 40 data lines; the seeded
review collapses them to 34 on (term, evidence, reference, qualifier). The five
collapsed `GO:0005515` rows are restored here so each interaction partner is
adjudicated separately (the two partners on PMID:20855601 receive *different*
verdicts). The one remaining exact duplicate — `GO:0031011` IDA PMID:21303910
asserted by both ComplexPortal and UniProt, identical in every
schema-representable field — is reviewed once.

| action | n | rows |
|---|---|---|
| ACCEPT | 12 | chromatin remodeling ×2 (IBA, IDA), Ino80 complex ×3 (IBA, IDA ×2), nucleus ×4 (IEA, EXP, IDA ×2), UV-damage excision repair, DSB repair, nucleoplasm |
| KEEP_AS_NON_CORE | 10 | reg. of DNA-templated transcription (IBA), cytoplasm (IEA, IDA), 5 ComplexPortal projections, ACTR8 + DDB1 protein-binding rows |
| MODIFY | 1 | `GO:0030234` → `GO:0060590` + `GO:0140658` |
| MARK_AS_OVER_ANNOTATED | 16 | `is_active_in` cytoplasm IBA, 3 ARBA parents, 12 redundant/noise `GO:0005515` rows |
| NEW | 4 | `GO:0031492`, `GO:0043531`, `GO:0042393`, `GO:0000122` |

Totals: 39 reviewed GOA rows + 4 NEW = 43. Counts are recomputed from the YAML
by `ACTR5-bioinformatics/audit_review.py`, which is the authority; the table
above is copied from its output.

## 12a. Checkers, and breaking them

Two committed scripts, both tested by deliberate mutation rather than by reading:

* `ACTR5-bioinformatics/nucleotide_site.py` — four break-tests fire correctly:
  a catalytic position that does not match ACTB aborts with the numbering-frame
  message; substituting the dead accession `O15507` aborts because the returned
  `primaryAccession` is `P56159`, not what was asked for; and swapping ARP5's
  accession for ARP8's makes the cross-check against the committed ACTL7A audit
  abort (`ours=HEDKS theirs=DDSCH`). Re-running the pair of scripts reproduces
  `results.json` and `RESULTS.md` byte-for-byte.
* `ACTR5-bioinformatics/audit_review.py` — six break-tests, all firing: deleting
  a reviewed row, perturbing one `source_entities` token, emptying one IPI row's
  `supporting_entities`, injecting a forbidden claim, deleting a required claim,
  and an empty GOA file. The fifth of those initially *failed to fire*, and the
  reason is instructive: the test mutated the YAML by string replacement, but
  `yaml.dump` hard-wraps long scalars, so the phrase was split across a line
  break and the replacement silently matched nothing. That is the campaign's
  "string replacement across wrapped YAML" trap appearing inside a test. The fix
  was twofold — mutate through the parser in the test, and normalise whitespace
  before the phrase scan in the lint, which was masking the same problem.
* The strict reference-title check (`just validate-references`) reports
  `Total checks: 0` on a clean file, which reads like a no-op; corrupting one
  title makes it emit `[ERROR] Title mismatch for PMID:29643506`, so it is
  genuinely running.

## 13. Provenance / method log

* `just fetch-gene human ACTR5`; `just fetch-gene-pmids human ACTR5`;
  `just fetch-pmid` for 26306040, 16618800, 39676660, 41775336, 36563143,
  40386946.
* Affinage record: `self_evaluation_pairwise: win`, trust gates clear, 2 citations, 3 findings. Both cited
  PMIDs are real PubMed records (no `PMID:bio_*` preprint ids). Neither is
  retracted; PMID:36563143 has the 2025 erratum described in §10, which the
  provider does not flag. PMID:40386946 (a childhood-lupus trio-WES study whose
  only ACTR5 datum is an IFN-β luciferase reporter effect of one de novo variant)
  is cited in the review at `relevance: LOW` and supports no annotation.
* WITH/FROM resolution and donor-evidence queries: UniProt REST (`size=2`,
  `primaryAccession` guard) and QuickGO annotation search with
  `goUsage=descendants&goUsageRelationships=is_a,part_of`.
* Term existence/obsoletion checked with QuickGO
  `/ontology/go/terms/<ids>/complete` (reading `isObsolete` and `secondaryIds`)
  and `/ancestors`: `GO:0060590` is a direct child of `GO:0030234`;
  `GO:0031492` has `GO:0031491`, `GO:0003677` and `GO:0003682` among its
  ancestors; `GO:0001671` is not under `GO:0030234`.
* `source_entities` on every `propagation_review` were generated from the GOA
  WITH/FROM column programmatically, with an assertion that the token counts
  match GOA — not typed by hand.

## 14. Round-2 changes (review of PR #2291)

The reviewer raised two blocking items and three suggestions. Verified before
conceding, per the campaign rule that the reviewer's checkable premises should be
checked:

1. **Hierarchy of `GO:0001671` / `GO:0060590`.** Partly conceded, partly pushed
   back — see the corrected table in §2. My "not a descendant of `GO:0030234`"
   claim for `GO:0001671` is confirmed by both QuickGO and OLS; the reviewer's
   suggestion that it sits under `GO:0060590` is not what either reports. But the
   reviewer is right that `GO:0060590` is a *grandchild*, not a direct child
   (`GO:0060589` sits between), and right that listing two parents for
   `GO:0001671` was redundant. Both corrected, and `GO:0001671` is now offered as
   a named alternative rather than dismissed.
2. **Two `supporting_text` entries that pass the verbatim check but do not support
   their claims.** Conceded outright; this is the failure mode no mechanical check
   can catch, and both were mine. The filament fragment on the `is_active_in`
   cytoplasm row and the nucleotide-table row on the `part_of GO:0031011` row are
   replaced with PMID quotes that actually bear on those claims.
3. **Suggestion: use the primary structure PMID as `original_reference_id` for the
   `GO:0043531` IDA** (ACTR1A precedent). Taken: now `PMID:41775336`, with the
   RESULTS.md quotes retained in `supported_by` and the note that 7ZI4 — the
   highest-resolution of the three — is an unpublished deposition not covered by
   that paper.
4. **Suggestion: surface that the BeF3 in 7ZI4 is in chain G, not ARP5's chain H.**
   Taken, and made a computed field rather than prose: `nucleotide_site.py` now
   records, per ARP5 nucleotide, which ATP-mimic groups are in the same chain and
   which are elsewhere in the entry, and the resolution is fetched from PDBe.
   This is a genuinely better answer to the ADP-vs-ATP objection than the caveat
   it replaces.
5. **Suggestion: reconcile the "3.5–3.7 Å" figures with RESULTS.md.** Taken; the
   two figures come from different sources and the review now says so.
