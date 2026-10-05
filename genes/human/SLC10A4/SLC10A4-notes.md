# SLC10A4 (Q96EP9) — curation notes

**Deep research was unavailable in this container** (Falcon returned HTTP 402, OpenAI
HTTP 401, perplexity not registered). No `-deep-research-*.md` file was generated. The
synthesis below was assembled manually from the cached publications in `publications/`,
the UniProt record `SLC10A4-uniprot.txt`, and the GOA file `SLC10A4-goa.tsv`.

## Summary of the gene

SLC10A4 (also called VAAT, "vesicular aminergic-associated transporter") is the fourth
member of the SLC10 / bile acid:sodium symporter (BASS, TC 2.A.28) family, whose founding
members are the hepatic bile salt carrier NTCP (SLC10A1) and the ileal carrier ASBT
(SLC10A2). It is a 437-residue, seven-transmembrane integral membrane protein with an
N(exo)/C(cyt) orientation and an unusually long extracellular N-terminus relative to
SLC10A1/A2/A6 [PMID:18355966 "The rat Slc10a4 protein consists of 437 amino acids and
exhibits a seven transmembrane domain topology with N(exo)/C(cyt)trans-orientation of the
N- and C-terminal ends."].

**It is an orphan carrier: no substrate has been identified.** This is the single most
important fact for the annotation review, and it is supported by four independent
laboratories using four different expression systems:

- CHO cells, no Na+-dependent taurocholate uptake [PMID:17106928 "Functional analysis of
  SLC10A4 showed no significant taurocholate uptake in the presence of sodium when
  compared to untransfected CHO cells."].
- HEK293 cells and *Xenopus* oocytes, no uptake of any NTCP substrate, and no choline
  [PMID:18355966 "Despite its close phylogenetic relationship to Ntcp, Slc10a4 showed no
  transport activity for the Ntcp substrates taurocholate, estrone-3-sulfate,
  dehydroepiandrosterone sulfate, and pregnenolone sulfate when expressed in HEK293 cells
  or Xenopus laevis oocytes."].
- A systematic 14-substrate screen in HEK293, CAD and oocytes [PMID:26084360 "SLC10A4
  failed to show transport activity for dopamine, serotonin, norepinephrine, histamine,
  acetylcholine, choline, acetate, aspartate, glutamate, gamma-aminobutyric acid,
  pregnenolone sulfate, dehydroepiandrosterone sulfate, estrone-3-sulfate, and adenosine
  triphosphate, at least in the transport assays used."]. Critically, that study also
  excluded the obvious trafficking confounder: an SLC10A4–NTCP C-terminal chimera that
  *does* reach the plasma membrane still had no activity [PMID:26084360 "When the
  C-terminus of SLC10A4 was replaced by the homologous sequence of NTCP, the SLC10A4-NTCP
  chimeric protein revealed clear plasma membrane expression in CAD and HEK293 cells."],
  [PMID:26084360 "But this chimera also did not show any transport activity, even when the
  N-terminal domain of SLC10A4 was deleted by mutagenesis."].
- A dopamine-focused study likewise found none [PMID:25176177 "We did not find evidence for
  direct transport of dopamine by SLC10A4; however, synaptic vesicle preparations lacking
  SLC10A4 showed decreased dopamine vesicular uptake efficiency."].

The field's own framing is unambiguous [PMID:28439090 "In spite of significant efforts, the
substrate(s) of SLC10A4 still essentially remains unknown"].

## Localization: synaptic vesicles and secretory granules, not the hepatocyte surface

Unlike NTCP/ASBT, SLC10A4 is not a bulk plasma-membrane carrier at steady state. It is a
synaptic-vesicle protein of cholinergic and monoaminergic neurons, and a granule protein of
mast cells:

- [PMID:18355966 "Co-localization studies with the cholinergic marker proteins choline
  acetyltransferase (ChAT), vesicular acetylcholine transporter (VAChT), and high-affinity
  choline transporter (CHT1) demonstrated expression of Slc10a4 in cholinergic neurons."]
- [PMID:21742018 "Western blot and immunoprecipitation experiments with rat brain vesicle
  preparations revealed that the Slc10a4 protein was expressed in synaptic vesicles where
  it co-localized with synaptophysin, VAChT and VMAT2."]
- [PMID:21742018 "Slc10a4 expression was also detected in granules of rat peritoneal and
  tissue mast cells using immunofluorescence and electron microscopy."]
- [PMID:25176177 "We show that SLC10A4 is localized on the same synaptic vesicles as either
  vesicular acetylcholine transporter or vesicular monoamine transporter 2."]
- Human brain: [PMID:23948907 "The protein was ubiquitously expressed, particularly in the
  cholinergic and monoaminergic neurons and in the lateral geniculate body."]

A plasma-membrane pool is nonetheless reported in heterologous overexpression, alongside
intracellular compartments [PMID:17106928 "immunoblotting analysis and immunofluorescence
staining demonstrated a 49-kDa protein that is expressed at the plasma membrane and
intracellular compartments"], and UniProt records `SUBCELLULAR LOCATION: Cell membrane`
with `ECO:0000269|PubMed:23589386`. So `located_in plasma membrane` is defensible as a
secondary/overexpression location; `is_active_in plasma membrane` is not where any
functional effect of this protein has ever been measured.

## What SLC10A4 does do: modulate vesicle/granule loading and release

Every reproducible functional effect is a *modulation of a vesicle's or granule's
properties*, measured by loss or gain of SLC10A4 rather than by any activity assayed on the
protein itself:

- Vesicular monoamine loading and lumenal acidification scale with SLC10A4 dose
  [PMID:25176177 "Furthermore, we observed an increased acidification in synaptic vesicles
  isolated from mice overexpressing SLC10A4."] together with the decreased dopamine uptake
  efficiency in knockout vesicles quoted above.
- Cholinergic hyperexcitability in null mice [PMID:23022458 "In contrast to wild type mice,
  gamma oscillations occurred spontaneously in hippocampal slices from Slc10a4 null mice."]
- Neuromuscular junction remodelling and altered release [PMID:25410831 "NMJs lacking VAAT
  had fewer branch points, whereas endplates showed an increased number of islands."]
- Mast cell degranulation [PMID:28439090 "Slc10a4 -/- bone marrow-derived mast cells
  (BMMCs) had a significant reduction in the release of granule-associated mediators in
  response to IgE/antigen-mediated activation"]

These are knockout/overexpression phenotypes — necessity and dose-sensitivity evidence.
Per the participation test in CLAUDE.md, they do not by themselves identify which entity
performs the step (VMAT2 performs monoamine loading; the V-ATPase performs acidification),
so no `NEW` process annotation is proposed from them. They are recorded instead in
`suggested_questions` and `suggested_experiments`.

## Interaction with NTCP: a trafficking effect on a partner, not bile acid transport

SLC10A4 heterodimerizes with NTCP and *reduces* NTCP surface abundance and taurocholate
uptake [PMID:22029531 "SLC10A4 and SLC10A6 co-immunoprecipitated with NTCP, demonstrating
that heteromeric complexes can be formed between SLC10A family members in vitro."],
[PMID:22029531 "Bile salt uptake is influenced by heterodimerization when this impairs NTCP
plasma membrane trafficking."], reproduced by an independent group
[PMID:31256060 "NTCP co-localized with SLC10A4, SLC10A5, SOAT and SLC10A7. This
co-localization was most pronounced for SLC10A4 and was additionally confirmed by
co-immunoprecipitation."], [PMID:31256060 "Interestingly, SLC10 carrier co-expression
decreased the taurocholate transport function of NTCP for most of the analyzed constructs,
indicating that SLC10 carrier heterodimerization is of functional relevance."].

Note the sign: this is a *negative* effect on bile salt uptake by a partner protein, and it
has only been shown in forced co-expression (U2OS, HEK293, yeast split-ubiquitin). Native
expression is also largely non-overlapping — SLC10A4 is brain/intestine-enriched while NTCP
is hepatocyte-specific. So this evidence does **not** support `involved_in bile acid and
bile salt transport`, and is far too indirect to support a regulation-of-transport term
either. It is raised as a question for experts rather than asserted.

## The central judgement call: GO:0008508, IMP, PMID:23589386

The GOA row is `NOT|enables GO:0008508 bile acid:sodium symporter activity`, IMP,
ECO:0000315, from PMID:23589386, assigned by UniProt. It is a **negated** annotation —
it asserts the *absence* of the activity.

PMID:23589386 is abstract-only in the cache (`full_text_available: false`). Its title
("SLC10A4 is a protease-activated transporter that transports bile acids") reads as a
positive claim, but the abstract both opens with the negative baseline and qualifies the
positive conclusion heavily:

- [PMID:23589386 "SLC10A4 belongs to the sodium bile acid cotransporter family, but has no
  transport activity for bile acids."]
- [PMID:23589386 "Lithocholic acid (LCA) and taurocholic acid (TCA) uptake and cell death
  effects of LCA were increased by thrombin treatment."]
- [PMID:23589386 "Therefore, SLC10A4 may have low activity but becomes activated by
  proteases, including thrombin, following cleavage."]

What the paper actually demonstrates is that thrombin treatment of TE671 cells increases
LCA/TCA accumulation, and that siRNA against SLC10A4 abolishes that increment. That is an
SLC10A4-dependent, protease-dependent *uptake phenotype in whole cells*. It is not a
demonstration of symport: no sodium dependence, stoichiometry, saturation kinetics, or
activity in a reconstituted or heterologous system is reported, and the measured
baseline activity is explicitly "no transport activity for bile acids".

The UniProt curator, who read the full text, drew the same conclusion and recorded it
twice: the negated GO row, and the FUNCTION comment "No significant bile acid transporter
activity could be measured despite its similarity to bile acid:sodium symporters."
(`ECO:0000269|PubMed:23589386`). This agrees with the four independent negative studies
above.

**Verdict: ACCEPT the negated annotation.** The NOT is the correct reading of this paper
and of the field. No action is taken against the curator; the `MODIFY`/
`MARK_AS_OVER_ANNOTATED` options that would apply to a *positive* IMP of symport activity
are not in play, because GOA does not assert the positive. (This is worth flagging: the
annotation was initially briefed to this review as a positive IMP. The `negated: true`
flag in the review YAML and the `NOT|enables` qualifier in the GOA tsv settle it.)

The inconsistency that *does* need fixing is elsewhere in the same GOA record: a
`GO:0015721 bile acid and bile salt transport` IBA sits alongside the NOT, propagated from
the rat bile acid carriers via PANTHER:PTN000040761. The experimental negation and the
phylogenetic inference contradict each other, and the experimental evidence (five
independent studies) wins. That row is `REMOVE`.

## The uninformative parents are the right answer here

`GO:0022857 transmembrane transporter activity` (IBA, PTN000040756) and its logically
inferred `GO:0055085 transmembrane transport` (IEA, GO_REF:0000108) are both deliberately
shallow. For a protein that demonstrably retains the BASS fold and seven-TM topology but
whose substrate has defeated four laboratories, this is exactly the right level of
specificity: it commits to carrier-type architecture without committing to a cargo. Both
are `ACCEPT`, and the reviews say explicitly that they should **not** be deepened until a
substrate is identified. An argument could be made that even the parent overstates matters
(SLC10A4 may act as a vesicular regulator rather than a carrier), but the PAINT node
placement is a judgement about where the carrier activity arose in the family, and there is
no target-specific evidence of fold loss to argue against it.

## Protein binding rows

Five `GO:0005515 protein binding` IPI rows from HuRI [PMID:32296183 "Specifically, yeast
two-hybrid (Y2H) represents the only binary PPI assay that can be operated at sufficient
throughput to systematically screen the human proteome for binary PPIs."] name TMEM218
(A2RU14), COL4A5 isoform 2 (P29400-2), VMA12/TMEM199 (Q8N511), SLC35A4 (Q96G79) and
DNAJC30 (Q96LL9) — all also listed in the UniProt INTERACTION block with NbExp=3. The
partners are membrane/ER proteins, which is broadly consistent with SLC10A4's membrane
residency, but none supports a specific informative molecular function. Per the Quality
Standards section of SKILL.md these are `REMOVE` as uninformative; removal does not imply
the interactions are false.

## Core function call

A core *molecular* function cannot be assigned with a substrate. The single core-function
entry uses `GO:0022857 transmembrane transporter activity` — the term the accepted IBA
already supports — with the location moved to `GO:0030672 synaptic vesicle membrane`, and
the `description` states plainly that the transported substrate is unidentified. No
`proposed_new_terms` entry is created: inventing a term such as "vesicular neurotransmitter
loading accessory activity" would assert a mechanism that the knockout-level evidence does
not establish.

## Action tally

| Action | Count | Rows |
|---|---|---|
| ACCEPT | 4 | GO:0008508 (NOT, IMP), GO:0016020 (IEA), GO:0022857 (IBA), GO:0055085 (IEA) |
| KEEP_AS_NON_CORE | 2 | GO:0005886 `located_in` (IDA), GO:0005886 `located_in` (IEA) |
| MODIFY | 1 | GO:0005886 `is_active_in` (IBA) → GO:0030672 synaptic vesicle membrane |
| REMOVE | 6 | 5 × GO:0005515 (IPI, HuRI), GO:0015721 (IBA) |
