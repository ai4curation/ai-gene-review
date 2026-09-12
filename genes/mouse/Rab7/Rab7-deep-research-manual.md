# Rab7 (mouse, Rab7a / P51150) — Manual Research Synthesis

> **Provenance note.** Automated deep-research providers could not be run in this
> environment: the Falcon provider requires the `agentapi` binary (not in PATH),
> and the OpenAI/Perplexity/Anthropic providers require API keys that are not set.
> Per project policy, no `-deep-research-{provider}.md` file was fabricated. This
> file is a **manual** synthesis assembled from cached primary literature
> (`publications/PMID_*.md`) and the requested Nature Biotechnology 2026 paper.
> Every assertion carries a PMID and supporting quote.

## 1. Identity and core function

Mouse **Rab7** (official symbol **Rab7a**, MGI:105068; UniProt **P51150**, 207 aa)
is a Rab-family small GTPase (EC 3.6.5.2) and the direct ortholog of human RAB7A.
It is the master switch of the late endocytic pathway, GTP-loaded by Mon1-Ccz1 on
maturing endosomes and turned off by TBC-domain GAPs.

- TBC-domain GAPs accelerate Rab7 GTP hydrolysis by a dual-finger mechanism
  [PMID:16855591, "TBC-domain GAPs for Rab GTPases accelerate GTP hydrolysis by a
  dual-finger mechanism"].

## 2. Rab7a is functionally distinct from Rab7b

A point worth flagging so the two paralogs are not conflated (mouse "Rab7" = Rab7a):

- [PMID:23179371, "RAB7A is localized to late endosomes and controls transport to
  late endosomes and lysosomes as well as maturation of phagosomes and
  autophagosomes [...] while RAB7B controls transport from endosomes to the Golgi
  apparatus"].

This also supports flagging the lone **Golgi apparatus** annotation
(GO:0005794, from a bulk Golgi-membrane proteomics survey [PMID:11042173]) as an
over-annotation — Golgi-directed traffic is the province of Rab7b, not Rab7a.

## 3. Most interesting / novel finding — the requested paper

**[PMID:41814093]** Jozić et al. (2026) *Nature Biotechnology*,
"In vivo endosomal escape assay identifies mechanisms for efficient hepatic LNP
delivery." DOI: 10.1038/s41587-026-03022-6.

- The authors built an in vivo assay (LysoTag mice + "Lysosomal Barcoding") to
  quantify, in intact mouse liver, how much of an mRNA lipid-nanoparticle (LNP)
  dose escapes the endolysosomal system into the cytosol
  [PMID:41814093, "we used LysoTag mice, which allow immunoisolation of liver
  lysosomes"].
- **Counterintuitive, therapeutically important result:** removing Rab7 *increases*
  cytosolic escape of LNPs
  [PMID:41814093, "Loss of Rab7, a mediator of late endosomal maturation, increased
  LNP escape"].

Why this is interesting: most of the Rab7 literature frames it through degradation
and disease. This study reframes Rab7 as a **rate-limiting "checkpoint" that
partitions endocytosed cargo toward lysosomal degradation and away from cytosolic
delivery** — i.e., the same maturation activity that makes Rab7 essential for
degradation is exactly what limits the efficiency of nucleic-acid therapeutics in
vivo. It also provides rare *in vivo, intact-tissue* genetic evidence for Rab7's
role in late endosomal maturation, complementing the mostly cell-line-based
mechanistic literature.

## 4. Mouse-specific physiology (beyond the canonical degradation role)

The genuinely *mouse-experimental* (non-ISO) annotations cluster around tissue
physiology rather than generic trafficking, which is the most distinctive aspect of
the mouse dataset:

- **Adipocyte lipophagy / β-adrenergic lipolysis.** Rab7 couples autophagy to fat
  mobilization [PMID:23708524, "RAB7 plays a pivotal role in the regulation of this
  autolysosome-mediated lipid degradation in fat cells"; and "ADRB2 stimulation has
  caused a marked increase in the autophagy-targeted LDs for lysosomal degradation,
  which is dependent on the LD-associated RAB7"].
- **Osteoclast bone resorption.** Rab7 is enriched at the osteoclast ruffled border
  and required for resorption [PMID:38744829, "Rab7 is highly expressed at the
  ruffled border of bone-resorbing osteoclasts and its knockdown disrupts both the
  targeting of vesicles to the ruffled border and bone resorption"]; it acts through
  the PLEKHM1/DEF8 positioning complex [PMID:27777970, "PLEKHM1 binds to RAB7 and is
  critical for lysosome trafficking"] and the effector RUFY4 [PMID:38744829, "RUFY4
  is an effector of small GTPases such as Rab7"]. RUFY4 deletion *prevents*
  pathological bone loss — a potential therapeutic angle.
- **Neuronal synaptic plasticity.** Rab7 routes AMPA receptors from postsynaptic
  endosomes to lysosomes during long-term depression [PMID:24217640].
- **Secretory-lysosome trafficking.** The a3 isoform of V-ATPase recruits Rab7 to
  drive secretory-lysosome trafficking [PMID:29712939, "Essential Role of the a3
  Isoform of V-ATPase in Secretory Lysosome Trafficking via Rab7 Recruitment"]; this
  pathway is linked to albinism/immunodeficiency syndromes.

## 5. Curation observations

- No NOT/negated and no isoform-specific annotations exist for mouse Rab7.
- The MF core (GTPase/G-protein activity, GTP/GDP binding, retromer binding) is
  well supported; ~half the dataset is ISO transfer from human/rat, consistent with
  the deeply conserved trafficking role.
- Two cached publications (PMID:24760869, PMID:24334765) supporting late-endosome
  localization annotations are abstract-only and do not contain a Rab7 sentence in
  the cached text, so those ACCEPTs remain without a verbatim quote (4 residual
  validation warnings, all benign).
