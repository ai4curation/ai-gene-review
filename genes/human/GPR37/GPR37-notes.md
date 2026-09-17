# GPR37 (O15354, GPR37_HUMAN / Pael-R / ETBR-LP-1) — curation notes

## The problem

GPR37 is one of the most over-deorphanized receptors in the literature. Four
different endogenous ligands have been proposed, from three different chemical
classes, and the 2025-2026 literature asserts several of them simultaneously
without the proposing groups engaging one another. Separately, GPR37 has a
completely non-ligand body of work — it is the parkin substrate "Pael-R" — that
is arguably its most reproducible molecular phenotype.

| Proposed ligand | Class | Origin | Status |
|---|---|---|---|
| head activator (HA) | invertebrate undecapeptide | Rezgaoui 2006, PMID:16443751 | **refuted** |
| prosaposin / prosaptide (TX14A) | secreted protein / peptide fragment | Meyer 2013, PMID:23690594 | contested in 2015, substantially strengthened since |
| protectin D1 / neuroprotectin D1 | DHA-derived lipid mediator | Bang 2018, PMID:30010619 | repeatedly reproduced, mostly within one lab lineage |
| osteocalcin (OCN) | 49-aa bone-derived peptide hormone | Qian 2021, PMID:34678058 | reproduced, but by the same senior authors |

## 1. Head activator — refuted, and the GOA rows should go

`GO:0008188 neuropeptide receptor activity` (IDA), `GO:0007218 neuropeptide
signaling pathway` (IDA) and `GO:0042923 neuropeptide binding` (IPI) all trace to
PMID:16443751. The IPI `WITH/FROM` field is the giveaway: `UniProtKB:P69251`,
which is **MORN_HYDVU, "Morphogenetic neuropeptide / Head activator" of
_Hydra vulgaris_**. So a human GPCR carries an experimental binding annotation
whose partner is a cnidarian peptide.

The claim did not survive:

- [PMID:26635605 "These studies contrast with that of Dunham et al. (2009), who attempted to replicate the finding that HA was a ligand for GPR37 but found no evidence of HA-mediated internalization, ERK1/2 phosphorylation or cAMP stimulation. HA was also included in a larger screen of all remaining orphan GPCRs but did not register as a \"hit\" for any GPCR tested (Southern et al., 2013). Finally, perhaps the most damning evidence against HA as the endogenous ligand for GPR37 is the fact that it has not been found in the human genome (Davenport et al., 2013). Thus, it appears that HA is unlikely to be an agonist at GPR37 and is certainly not its endogenous ligand."]
- Even the prosaposin paper, which is friendly to the HA result, concedes HA's
  standing is analogical rather than orthologous:
  [PMID:23690594 "HA does not seem to be a true ortholog of prosaptide, but nonetheless we propose that this invertebrate peptide may possess the ability to act as a GPR37 agonist owing to its similarity to prosaptide and prosaposin."]

This is not "second-guessing a curator I disagree with": it is a published,
direct failure to replicate by an independent laboratory, plus the non-existence
of the ligand in the human genome. That is exactly the "genuinely contradicted
function" case for which REMOVE exists. No information is lost by removing them,
because the peptide-receptor content survives in `GO:0008528` and `GO:0036505`,
which rest on the prosaposin work.

The `GO:0005737 cytoplasm` IDA from the same paper reflects
[PMID:16443751 "Overexpression of GPR37 led to aggregate formation, retention of the receptor in the cytoplasm and low survival rates of transfected cells"]
— i.e. ER retention of a misfolding-prone multipass membrane protein, not a
cytosolic pool. MODIFY to `GO:0005789 endoplasmic reticulum membrane`.

## 2. Prosaposin — the pairing GOA already carries, and the one I keep

Meyer et al. screened orphan neuropeptides and got exactly one hit
[PMID:23690594 "We screened these receptors for potential activation by various orphan neuropeptides, and these screens yielded a single positive hit: prosaptide, which promoted the endocytosis of GPR37 and GPR37L1, bound to both receptors and activated signaling in a GPR37- and GPR37L1-dependent manner."]
with Gi-type signalling and ERK phosphorylation
[PMID:23690594 "Prosaptide stimulation of cells transfected with GPR37 or GPR37L1 induced the phosphorylation of ERK in a pertussis toxin-sensitive manner, stimulated 35 S-GTPγS binding, and promoted the inhibition of forskolin-stimulated cAMP production."]

The 2015 authoritative review was sceptical, for reasons worth recording:
[PMID:26635605 "Again, the claim that prosaposin and prosaptide are endogenous ligands for GPR37 and GPR37L1 is not without some controversy and is yet to be ratified by the International Union of Basic and Clinical Pharmacology (IUPHAR) Nomenclature Committee. First, the concentration of prosaposin or TX14A required for agonism is 100 nM, much higher than traditionally associated with peptide/GPCR interactions"]
and [PMID:26635605 "While direct agonism remains to be independently demonstrated for either receptor, it seems likely that prosaposin and TX14A have some influence on GPR37 subcellular localization, although the evidence itself is contradictory."]

**But the 2015 objection has largely been answered.** The Ji laboratory (Duke),
independent of the Hall laboratory that made the original pairing, reproduced
TX14 binding and GPR37-dependent signalling
[PMID:30010619 "Neuroprotectin D1 (NPD1) and prosaptide TX14 increase intracellular Ca2+ (iCa2+) levels in GPR37-transfected HEK293 cells. NPD1 and TX14 also bind to GPR37 and cause GPR37-dependent iCa2+ increases in peritoneal MΦs."]
and in 2026 showed that the in vivo actions of intrathecal TX14A require GPR37 in
a defined neuronal population
[PMID:42144155 "Global GPR37 knockout or conditional knockout of GPR37 in TRPV1-lineage sensory neurons abolished the long-term inhibitory effect and unpriming effect of i.th. TX14A, confirming that GPR37 in this specific cellular population mediates these effects."]

So: two laboratories, cell-free binding + heterologous signalling + cell-type-specific
conditional knockout in vivo. I ACCEPT `GO:0036505 prosaposin receptor activity` as
core, and record the residual reservations (potency, IUPHAR non-ratification, the
possibility that prosaposin also acts as a folding chaperone for GPR37) in the
`reason` field rather than pretending they do not exist.

## 3. Protectin D1 — a real second ligand, of a different chemical class

The brief asks whether "a peptide receptor and a lipid receptor are not easily the
same receptor". They are not — and yet the same experiments, in the same paper,
report both. PMID:30010619 tested NPD1 (= protectin D1) and TX14 side by side and
found both bind GPR37 and both raise Ca2+ in a GPR37-dependent way. The lipid arm
has since been replicated across models: sepsis/infection [PMID:33731716],
chemotherapy-induced neuropathy [PMID:40287118], spinal nociceptive sensitization
[PMID:42144155], and a 2026 rat pituitary study that treats both as established
[PMID:42649016 "Prosaposin (PSAP), a secreted glycoprotein with neurotrophic activity, and protectin D1, a docosahexaenoic acid-derived lipid mediator, are endogenous ligands of G protein-coupled receptor 37 (GPR37)."]

Two honest readings:
1. GPR37 is genuinely polypharmacological — peptide at one site, lipid at another
   (plausible for a class A GPCR with a very long N-terminus that is constitutively
   shed, PMID:26869225).
2. The two "ligands" are converging on a shared downstream Ca2+/phagocytosis
   readout that is not a clean measure of orthosteric occupancy, and one of them is
   not a direct agonist.

Nobody has done the experiment that distinguishes these: competition binding of
PD1 against labelled TX14A on the same receptor preparation. **Most of the
protectin D1 work shares a senior author (Ji).** So the chemical-class objection
stands, and the corroboration is less independent than the paper count suggests.

There is no GO term for protectin D1 receptor activity, and GOA carries no lipid
MF for GPR37. I therefore propose a new term rather than shoehorning it into
`GO:0045125 bioactive lipid receptor activity`, and flag the unresolved
competition-binding question.

## 4. Osteocalcin — reproduced, but not independently

Original pairing: [PMID:34678058 "GPR37 is identified as a previously unknown receptor for OCN, thus regulating OL differentiation and CNS myelination."]
2026 extension: [PMID:41679312 "Here, we demonstrate that osteocalcin (OCN), a bone-derived hormone, permits rapid visual escape by enhancing the excitability of a ventral tegmental area (VTA) GABAergic neuron subpopulation through the OCN-G Protein-Coupled Receptor 37 (GPR37)-cAMP-TWIK-related halothane-inhibited potassium channel (THIK-1) pathway."]

Two caveats that matter for curation:
- **These are not independent groups.** Zhengjiang Qian, Xiang Li and Liping Wang
  are authors on both the 2021 Sci Adv paper and the 2026 Neuron paper, from the
  same Shenzhen institute. A second paper from the same lab is corroboration, not
  replication.
- The Neuron paper carries a **published erratum** spanning four journal pages
  (PMID:42001851, Neuron 2026;114:1695-1698), which is substantial for an erratum.
- OCN already has two other claimed receptors, GPRC6A (periphery) and GPR158
  (brain); a third is not impossible but raises the bar.

No GO annotation for osteocalcin exists on GPR37 and no osteocalcin receptor GO
term exists at all. I propose the term and leave the pairing out of
`core_functions`.

## 5. Pael-R / parkin — the best-replicated molecular fact about GPR37

[PMID:11439185 "A putative G protein-coupled transmembrane polypeptide, named Pael receptor, was identified as an interacting protein with Parkin"], with
[PMID:12150907 "we show that CHIP, Hsp70, Parkin, and Pael-R formed a complex in vitro and in vivo."] and a second E3
[PMID:17059562 "This study shows that HRD1 was expressed in substantia nigra pars compacta (SNC) dopaminergic neurons and interacted with Pael-R through the HRD1 proline-rich region, promoting the ubiquitylation and degradation of Pael-R."]

**Is this better supported than any ligand claim? In reproducibility, yes** — it
comes from at least three laboratories, was found by unbiased interaction
screening, is echoed in the UniProt PTM block, and is corroborated by the
independent observation that GPR37 aggregates and is ER-retained on overexpression
(PMID:16443751, PMID:25977097 for the ASD R558Q mutant). **But it is not the same
kind of claim.** Being a parkin/HRD1 substrate describes ER quality control of an
aggregation-prone GPCR; it is a property the protein has because it folds badly,
not a function it evolved to perform. I therefore keep these annotations as
`KEEP_AS_NON_CORE` rather than promoting them over the receptor function, and I
mark `GO:0000151 ubiquitin ligase complex` as over-annotated, because a substrate
held by an E3 is not a component of the ligase.

## Actions summary

- **REMOVE** (3): GO:0008188, GO:0007218, GO:0042923 — all head-activator-derived.
- **MODIFY** (1): GO:0005737 cytoplasm -> GO:0005789 endoplasmic reticulum membrane.
- **MARK_AS_OVER_ANNOTATED**: GO:0005515 protein binding (x4 references),
  GO:0000151 ubiquitin ligase complex.
- **KEEP_AS_NON_CORE**: GO:0031625, GO:0030544, GO:0031072, GO:0042277,
  GO:0034614, GO:0016358, GO:0043235.
- **ACCEPT**: the prosaposin-receptor / Gi / MAPK / localisation set.
- **NEW**: nothing added to existing_annotations for the lipid or osteocalcin
  pairings; both are recorded as `proposed_new_terms` plus `suggested_questions`,
  because in my judgement neither has the independent replication that a
  ligand-specific MF assertion requires.

No NOT/negated qualifiers are present in the GOA file.
