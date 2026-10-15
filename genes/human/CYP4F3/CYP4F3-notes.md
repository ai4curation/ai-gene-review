# CYP4F3 (Q08477) — review notes

Cytochrome P450 4F3, 520 aa, ER/microsomal membrane, single-pass. HGNC:2646,
synonym LTB4H. EC 1.14.14.1, 1.14.14.94 (LTB4 ω-hydroxylase), 1.14.14.79 (DHA
ω-hydroxylase).

## The central fact: two isoforms with different substrates

CYP4F3 is the textbook case of alternative splicing changing a P450's substrate
preference. Two isoforms arise by alternative promoter usage + alternative
splicing of mutually exclusive 48-codon exons; both are 520 aa.

- **CYP4F3A** (Q08477-1, incorporates exon 4) — blood neutrophils and bone marrow.
- **CYP4F3B** (Q08477-2, incorporates exon 3, VSP_047193) — liver and kidney;
  also predominant CYP4F in trachea and GI tract.

[PMID:11461919 "CYP4F3A, which incorporates exon 4, inactivates LTB4 by
omega-hydroxylation (Km = 0.68 microm) but has low activity for arachidonic acid
(Km = 185 microm); it is the only CYP4F isoform expressed in myeloid cells in
peripheral blood and bone marrow."]

[PMID:11461919 "CYP4F3B has a 30-fold higher Km for LTB4 compared with CYP4F3A,
but it utilizes arachidonic acid as a substrate for omega-hydroxylation (Km = 22
microm) and generates 20-HETE, an activator of protein kinase C and
Ca2+/calmodulin-dependent kinase II."]

So LTB4 is the A isoform's substrate and arachidonate the B isoform's. This
matters for the review because GOA carries both activities on one accession with
no isoform qualifier.

## LTB4 inactivation is a three-step cascade on one enzyme

The purified neutrophil enzyme (i.e. CYP4F3A) ω-hydroxylates LTB4 and then keeps
going, oxidising the ω-alcohol to the aldehyde and on to the acid:

[PMID:9675028 "The enzyme catalyzed the omega-hydroxylation of LTB4 with a Km of
0.64 microM and Vmax of 34 nmol/min/nmol of P450 in the presence of rabbit
hepatic NADPH-P450 reductase and cytochrome b5."]

UniProt states the cascade explicitly for isoform A: "Inactivates LTB4 via three
successive oxidative transformations to 20-hydroxy-LTB4, then to 20-oxo-LTB4 and
to 20-carboxy-LTB4 (PubMed:9675028)".

GO represents all three steps, which is unusual and important (see the
[CYTOCHROME_P450](../../../projects/CYTOCHROME_P450.md) project — this trio is
the precedent that family's new-term proposals are modelled on):

| Step | Reaction | GO term |
|---|---|---|
| 1 | LTB4 → 20-OH-LTB4 | GO:0050051 leukotriene-B4 20-monooxygenase activity |
| 2 | 20-OH-LTB4 → 20-oxo-LTB4 | GO:0097258 20-hydroxy-leukotriene B4 omega oxidase activity |
| 3 | 20-oxo-LTB4 → 20-carboxy-LTB4 | GO:0097259 20-aldehyde-leukotriene B4 20-monooxygenase activity |

The original cDNA cloning established the enzyme identity:
[PMID:8486631 "The microsomes from yeast cells transfected with an expression
vector pAAH5 carrying isolated cDNA catalyzed the omega-hydroxylation of LTB4
with a Km value of 0.71 microM, and its activity was significantly inhibited by
carbon monoxide and by antisera against CYP4A4"]

## Substrate range of the purified A isoform — and what it does NOT do

[PMID:9675028 "Furthermore, various eicosanoids such as 20-hydroxy-LTB4,
6-trans-LTB4, lipoxin A4, lipoxin B4, 5-HETE and 12-HETE, and
12-hydroxy-stearate and 12-hydroxy-oleate were efficiently omega-hydroxylated,
although their Km values were much higher than that of LTB4."]

[PMID:9675028 "In contrast, no activity was detected toward laurate, palmitate,
arachidonate, 15-HETE, prostaglandin A1, and prostaglandin E1, all of which are
excellent substrates for the CYP4A fatty acid omega-hydroxylases."]

Two consequences for this review:

1. **5-HETE ω-hydroxylation is experimentally established**, which bears on
   GO:0097265 (see the term-defect section below).
2. **The A isoform does not hydroxylate arachidonate.** Taken with PMID:11461919,
   the arachidonate ω-hydroxylase annotations are CYP4F3B activities, not a
   property of the gene product as a whole.

## CYP4F3B: 20-HETE and other PUFAs

[PMID:18577768 "CYP4F3A and CYP4F3B were the most efficient omega-hydroxylases
of these PUFAs."] (ETA, AA, EPA, DHA)

[PMID:16820285 "We observed that a microsomal preparation containing recombinant
human CYP4F3B, which converts AA to 20-HETE, converted eicosapentaenoic acid
(EPA) to 20-OH-EPA. Likewise, docosahexaenoic acid (DHA) was converted to
22-OH-DHA, indicating that human CYP4F3B also can oxidize 22-carbon omega-3
fatty acids."]

On the ω-1 question — UniProt says CYP4F3B "Can also catalyze the oxidation of
the penultimate carbon (omega-1 oxidation) of PUFAs with lower efficiency
(PubMed:18577768)". The paper frames ω-1 as the *other* families' route, not the
CYP4F route:

[PMID:18577768 "With the CYP4F enzymes, the main pathway was always the
omega-hydroxylation of PUFAs, whereas it was the (omega-1)-hydroxylation with
CYP1A1, CYP2C19, and CYP2E1."]

**So I am not proposing an ω-1 hydroxylase annotation.** The reading that
supports one is UniProt's gloss, while the cited paper's own framing makes ω-1 a
minor side-activity distinguishing CYP4F from CYP1A1/2C19/2E1. Proposing
GO:0120502/GO:0120319 here would over-annotate.

## Very-long-chain fatty acids: the ω-oxidation route, and an X-ALD angle

[PMID:16547005 "Studies with individually expressed human recombinant P450
enzymes revealed that two P450 enzymes, i.e. CYP4F2 and CYP4F3B, participate in
the omega-hydroxylation of VLCFAs. Both enzymes belong to the cytochrome P450 4F
subfamily and have a high affinity for VLCFAs."]

This is the ω-oxidation bypass of peroxisomal β-oxidation, of therapeutic
interest in X-linked adrenoleukodystrophy. It supports GO:0140692 (very
long-chain fatty acid ω-hydroxylase activity) — whose own definitional PMID is
this paper.

Steps 2 and 3 of that cascade are also catalysed by CYP4F3, **both isoforms**:

[PMID:18182499 "The second pathway involves the NADPH-dependent hydroxylation of
omega-hydroxy-VLCFAs by CYP4F2, CYP4F3B, or CYP4F3A."]

but it is the minor of two routes:

[PMID:18182499 "Enzyme kinetic studies show that oxidation of
omega-hydroxy-VLCFAs occurs predominantly via the NAD(+)-dependent route."]

**GO has no term for these two steps.** That gap is the subject of the
CYTOCHROME_P450 project's SSSOM batch 8 (RHEA:39055/39059 for the ω-oxo step,
RHEA:39043/39047 for the dicarboxylate step), and PMID:18182499 is direct
CYP4F3-specific experimental support for proposing them here. Note the
asymmetry that motivates the proposal: GO has all three LTB4 steps for this very
protein, and only step 1 for the fatty-acid route.

## Fatty acid epoxides

[PMID:15145985 "CYP4F2 and CYP4F3B catalyzed mainly the omega-hydroxylation of
C18-epoxides with an apparent Vmax of between 0.84 and 15.0 min(-1), whereas the
apparent Vmax displayed by CYP4F3A, the isoform found in leukocytes, ranged from
3.0 to 21.2 min(-1)."]

The paper's title is "Human CYP4F3s are the main catalysts in the oxidation of
fatty acid epoxides" — so epoxide ω-hydroxylation is a well-supported activity
of both isoforms. It is covered by the long-chain ω-hydroxylase term rather than
needing its own.

## GO:0097265 is a defective term (ontology bug, not an annotation error)

`GO:0097265 "5(S)-hydroxyeicosatetraenoic acid dehydrogenase activity"` is
annotated to CYP4F3 by IEA from RHEA (GO_REF:0000116). Three observations, all
checked against QuickGO (GO release `releases/2026-09-27`) and RHEA:

1. **Its definition is an ω-hydroxylation, not a dehydrogenation.** Definition:
   "5-hydroxy-(6E,8Z,11Z,14Z)-eicosatetraenoate (5-HETE) + reduced
   [NADPH-hemoprotein reductase] + O2 = 5,20-dihydroxy-(6E,8Z,11Z,14Z)-
   eicosatetraenoate (5-oxo-ETE) + oxidized [NADPH-hemoprotein reductase] + H2O
   + H+", xref RHEA:48656. RHEA:48656 confirms the product is
   `5,20-dihydroxy-(6E,8Z,11Z,14Z)-eicosatetraenoate`.
2. **The definition text contradicts itself**: it glosses
   "5,20-dihydroxy-…-eicosatetraenoate" as "(5-oxo-ETE)". 5-oxo-ETE is the
   product of a genuine 5-hydroxyeicosanoid *dehydrogenase*; 5,20-diHETE is the
   product of an ω-hydroxylase. The term conflates two different reactions.
3. **Its placement follows the wrong half.** `is_a` path:
   `GO:0016616` (oxidoreductase, acting on the CH-OH group of donors, NAD or
   NADP as acceptor) → `GO:0016614` → `GO:0016491`. An O2-consuming
   monooxygenation does not belong there; it belongs under `GO:0004497` /
   `GO:0016712`, where every other CYP4F3 activity term sits.

What CYP4F3 actually does is the reaction in the *definition* (5-HETE
ω-hydroxylation, PMID:9675028 above), not the reaction in the *name*. So the
annotation is substantively right and the term is wrong. Handled as MODIFY to
the long-chain ω-hydroxylase class term, with a `suggested_questions` entry
asking GO to fix or obsolete GO:0097265.

## GO:0052869 is obsolete and self-documents its replacement

`GO:0052869 "arachidonate omega-hydroxylase activity"` carries four EXP
annotations here but is obsolete. QuickGO: `isObsolete: true`,
`replacements: [{id: GO:0102033, type: replaced_by}]`, comment "The reason for
obsoletion is that this term represents a specific substrate of the parent term."

This is the same obsoletion pattern as `GO:0018777` (documented in
[RHEA-PROMISCUOUS-FAMILIES](../../../projects/RHEA/RHEA-PROMISCUOUS-FAMILIES.md)):
GO does not keep a term per substrate for ω-hydroxylases. So the four
experimental arachidonate rows move to GO:0102033, which the gene already
carries.

## Vitamin K: the IBAs are plausible but have no CYP4F3-specific evidence

`GO:0042361` (menaquinone catabolic process) and `GO:0042376` (phylloquinone
catabolic process) are annotated to CYP4F3 by **IBA only** (GO_REF:0000033).
QuickGO shows the same IBA across CYP4F2, CYP4F3, CYP4F8, CYP4F11 and CYP4F12,
but **IDA only on CYP4F2 and CYP4F11**, both from PMID:24138531.

I read that paper's full text (it is the one cached publication here with full
text). It assays CYP4F2 and CYP4F11:

[PMID:24138531 "CYP4F2 and CYP4F11 were expressed and purified and found to be
equally efficient as in vitro catalysts of MK4 ω-hydroxylation."]

**CYP4F3 is never assayed.** It appears twice in the whole paper, only as
background: [PMID:24138531 "In human liver, CYP4F2, CYP4F3B, CYP4F11, and
CYP4F12 are all readily detectable at the mRNA level."] And the authors leave the
question open: [PMID:24138531 "Studies are ongoing to determine if other human
liver enzymes might be involved in MK4 metabolism."]

So this is *not* a case of tested-and-negative, and the PAINT node judgment is
not contradicted — CYP4F3B is a liver CYP4F with ω-hydroxylase chemistry on
lipophilic isoprenoid-tailed substrates, so inheritance is reasonable. But there
is no CYP4F3 evidence, and vitamin K catabolism is not what this gene is for.
`KEEP_AS_NON_CORE` rather than `REMOVE`: removing would overrule a curator's
phylogenetic judgment on the strength of a paper that simply did not test the
paralog.

## A UniProt curation discrepancy worth flagging

UniProt's CYP4F3B FUNCTION line says it "Omega-hydroxylates long-chain
3-hydroxy fatty acids, likely initiating the oxidative conversion to the
corresponding 3-hydroxydicarboxylic fatty acids (PubMed:18065749)". The cited
paper says the opposite for this enzyme:

[PMID:18065749 "Upon reconstitution, CYP4F11 and, to a lesser extent, CYP4F2
catalyzed omega-hydroxylation of 3-hydroxystearate, whereas CYP4F3b, CYP4F12,
and CYP4A11 exhibited negligible activity."]

[PMID:18065749 "CYP4F11 was the lone CYP4F/A enzyme that effectively oxidized
3-hydroxypalmitate."]

The paper's conclusion is that **CYP4F11** is the 3-hydroxy fatty acid
ω-hydroxylase and CYP4F3B is specifically among the enzymes that are *not*. No
GO annotation rests on this, so there is nothing to action in
`existing_annotations`, but it is recorded here and raised as a
`suggested_questions` item, since the UniProt line could easily seed a future
over-annotation.

## Disease / pharmacology context

No Mendelian disease is assigned to CYP4F3 in UniProt. Relevance is via the
pathways: 20-HETE is a vasoactive/natriuretic mediator affecting blood pressure
(CYP4F3B), LTB4 inactivation is a resolution-of-inflammation step (CYP4F3A), and
the VLCFA ω-oxidation route is a proposed therapeutic bypass in X-ALD.
