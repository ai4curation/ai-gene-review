---
title: "Extracellular Cytochrome Nanowires"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [GEOSL, SHEON]
genes: [omcS, omcE, omcZ]
# "III" is the oxidation state in Fe(III), not the BPM13 phage gene of that name.
autolink_exclude: [III]
manifest:
  artifacts:
    - href: https://claude.ai/artifact/J6iDADErEjrJXDAc3SwtJS
      title: Project brief
---

# Extracellular Cytochrome Nanowires

**Bottom line:** some bacteria and archaea respire on solid surfaces they cannot
bring inside — iron and manganese oxides, electrodes, and other cells — by
polymerising a multiheme c-type cytochrome into a filament micrometres long and
passing electrons along its stacked hemes. The filaments were taken for type IV
pili for nearly two decades until cryo-EM showed otherwise in 2019, and they are
now reported across both prokaryotic domains. **GO has no term for any of this**:
no cellular component for the filament, and no biological process for
extracellular electron transfer, direct interspecies electron transfer or
dissimilatory metal reduction. The whole field is annotated with three generic
terms. This project collects the reviews, proposes the missing terms, and records
why the sequence-based classification resources fail on this particular class.
Three *Geobacter sulfurreducens* filament cytochromes are reviewed so far; two of
them had **no GOA annotations at all** before review.

We did this because the class is defined by a property that sequence homology
does not capture. OmcE and OmcS share no detectable sequence or backbone
similarity yet build filaments with the same heme geometry, so the resources that
drive automated annotation either misplace these proteins or miss them entirely —
and the missing GO terms mean even a correct classification would have nothing to
assign.

## The ontology gap, stated precisely

Checked against GO via OLS on 2026-11-10:

| What the biology needs | What GO has |
|---|---|
| the filament, as a cellular component | nothing |
| extracellular electron transfer (process) | nothing |
| direct interspecies electron transfer (DIET) | nothing |
| dissimilatory metal reduction | nothing |

The nearest cellular-component terms are all wrong in a way that matters.
`GO:0009289` pilus and `GO:0009288` bacterial-type flagellum describe
pilin- and flagellin-based appendages, and mistaking cytochrome filaments for
pili is the exact error the structural work corrected; annotating to them would
re-introduce it. `GO:0070069` cytochrome complex is for membrane respiratory
complexes such as bc₁, not for a micrometre-long homopolymer of a single subunit.
The children of `GO:0030312` external encapsulating structure are cell wall,
outer membrane, glycocalyx, S-layer and extracellular matrix — none of them a
discrete conductive appendage.

So reviewers are left with `GO:0009055` electron transfer activity, `GO:0019645`
anaerobic electron transport chain and `GO:0009986` cell surface. All three are
true, none is informative, and that is what every gene review in this project has
had to use.

## What the class is

The defining feature is **heme packing, not sequence**. Baquero et al. 2023
solved two archaeal extracellular cytochrome nanowires (ECNs) and found that
"the ECN protein subunits lack similarities in their folds; however, they share a
common heme arrangement" (PMID:37290436). The same paper reports homologs across
methane-oxidising Methanoperedenaceae, alkane-degrading Syntrophoarchaeales and
the giant extrachromosomal Borg elements, concluding that such filaments "may be
a common and widespread mechanism for long-range electron transfer in both
prokaryotic domains of life".

Wang et al. reached the same conclusion from the bacterial side when they solved
OmcE: it and OmcS have "no overall sequence or structural similarities" yet both
polymerise into filaments "that share a conserved haem packing arrangement in
which haems are coordinated by histidines in adjacent subunits" (PMID:35798889),
and they proposed "a broad class of conductive bacterial appendages with
conserved haem packing (rather than sequence homology)".

That cross-subunit heme-histidine ligation — a heme in one subunit coordinated by
a histidine from the next — recurs in OmcS, OmcE and the archaeal filaments, and
the OmcE authors describe it as unique among c-type cytochrome structures solved
to date. It is the best candidate for a structural definition of the class.

## The three *Geobacter sulfurreducens* filaments

| | hemes | structure | established role | GOA before review |
|---|---|---|---|---|
| OmcS (`UniProtKB:Q74A86`) | 6 | PDB 6EF8, 6NEF | Fe(III) oxide reduction; essential for DIET | 10 rows |
| OmcE (`UniProtKB:Q74FJ0`) | 4 | PDB 7TFS | Fe(III) oxide reduction only | **none** |
| OmcZ (`UniProtKB:Q74BG5`) | 8 | PDB 7LQ5, 8D9M | high-current-density anode biofilms | **none** |

Their deletion phenotypes barely overlap, which is the most useful curation fact
about them: OmcZ owns the electrode and is dispensable for Fe(III) oxide; OmcE is
confined to insoluble iron and is dispensable on anodes; OmcS covers both iron and
interspecies transfer. Why one organism maintains three unrelated polymerising
cytochromes with such different specificities is open.

Reviews: [omcS](https://github.com/ai4curation/ai-gene-review/blob/main/genes/GEOSL/omcS/omcS-ai-review.yaml) ·
[omcE](https://github.com/ai4curation/ai-gene-review/blob/main/genes/GEOSL/omcE/omcE-ai-review.yaml) ·
[omcZ](https://github.com/ai4curation/ai-gene-review/blob/main/genes/GEOSL/omcZ/omcZ-ai-review.yaml)

## Why the classification resources fail here

This is the part with consequences beyond these three genes. Checked 2026-11-09/10:

| | PANTHER | InterPro family | CDD | TCDB |
|---|---|---|---|---|
| OmcS | `PTHR30333:SF1` "…NAPC" — wrong | `IPR051174`, the same PANTHER family | **`cd21555` "C-type cytochrome OmcS and similar proteins"** | **`5.B.3.1.1`** G-NET |
| OmcE | `PTHR35038` "DISSIMILATORY SULFITE REDUCTASE SIRA" : `SF6` "SURFACE LOCALIZED DECAHEME CYTOCHROME C LIPOPROTEIN" — wrong on heme count, lipid anchor and family | `IPR010177`, a paired-CXXCH domain, not a family | none | none |
| OmcZ | none | Ig-like and multiheme superfamily, both on the C-terminus that maturation cleaves off | none | none |

Only CDD and TCDB get any of it right, and only for OmcS. Both are hand-curated
rather than HMM-derived, which is the pattern to notice: the discriminating
feature is not in the sequence, so a curator who looked at the structure
succeeded where an automated family assignment did not.

Two pieces of work follow from this:

- **[PTHR30333 family review](https://github.com/ai4curation/ai-gene-review/blob/main/interpro/panther/PTHR30333/PTHR30333-review.yaml)**
  records the family as HETEROGENEOUS. Its core is the NapC/NirT/NrfH inner-membrane
  quinol dehydrogenases, which all carry the NapC/NirT N-terminal domain
  (`PF03264` / `IPR005126`); OmcS matches neither and has no transmembrane anchor.
  The split crosses subfamily boundaries, since OmcS sits in SF1 beside NapC itself,
  so quinol-dehydrogenase activity is scoped `RESIDUE_DETERMINED` against a curated
  residue site rather than granted by membership. Both PAINT IBD rows at
  `PTN001251186` are nonetheless assessed SOUND: only generic terms were placed
  there, and that restraint is what keeps them safe for OmcS.
- **[CR-0007](https://github.com/ai4curation/ai-gene-review/blob/main/rules/curated/CR-0007.yaml)**
  assigns heme binding and electron transfer activity on `cd21555`. The model is
  unintegrated in InterPro and CDD carries no GO of its own, so it reaches GOA by no
  route at all: 52 of its 56 members lack a heme binding annotation despite every one
  being a c-type cytochrome. See [NCBIFam](NCBIFam.md) for the measurement and for why
  a blanket authored `cdd2go` is not worth building.

`PTHR35038`, OmcE's family, is not yet reviewed and looks at least as heterogeneous:
its SF6 holds OmcE alongside MtrA and a hydroxylamine oxidoreductase, and its single
PAINT node carries only `GO:0016491` oxidoreductase activity, seeded by NrfB.

## Proposed GO terms

The primary deliverable. One term is already proposed in two gene reviews; this page
is its single narrative home.

**`extracellular cytochrome filament`** (cellular component), proposed parent
`GO:0099080` supramolecular complex, `part_of` `GO:0005576` extracellular region.
A helical, non-membrane-bounded protein polymer outside the cell, built from
repeating subunits of a secreted multiheme c-type cytochrome, whose hemes stack
along the filament axis so that electrons can travel its length between the cell
and extracellular acceptors or donors.

On the name: the field's own term is **extracellular cytochrome nanowire (ECN)**,
used by Baquero et al. and by the ANME structural work. "Nanowire" is a metaphor and
is contested when it is taken to assert metallic-like conductivity — one 2024
perspective is titled "To be or not to be a cytochrome: electrical characterizations
are inconsistent with Geobacter cytochrome 'nanowires'" (PMID:38633696). The
descriptive label therefore seems the safer primary, with *extracellular cytochrome
nanowire* and *ECN* as exact synonyms so the term is findable under the name the
literature uses. This is a judgement worth a curator's opinion before submission.

Three further gaps are recorded but not yet drafted as terms, because each needs
thought about scope:

- **extracellular electron transfer** — the process the whole field is about.
- **direct interspecies electron transfer** — resists the usual single-organism
  framing of a biological process, since it is a property of a two-cell electrical
  connection.
- **dissimilatory metal reduction** — distinct from assimilatory iron uptake, which
  GO does cover.

## The conductivity dispute, recorded not adjudicated

How fast electrons move along these filaments, and by what physics, is contested.
Measurements of about 30 S/cm for OmcZ filaments (PMID:32807967) are disputed by
structure-based calculations predicting far smaller redox currents (PMID:37552847)
and by an argument that the electrical characterisations are artefactual
(PMID:38633696). A separate long-running thread holds that the conductive filaments
are PilA-based e-pili rather than cytochromes at all.

None of the annotations in this project depends on resolving any of that. That these
proteins carry electrons is not disputed — they have four to eight redox-active
hemes, deliver electrons to acceptors in vitro, and have clean genetic phenotypes.
The molecular-function annotations stay at `GO:0009055` and make no claim about
conduction mechanism, which is one practical reason to prefer the term *filament*
over *nanowire*.

## Open tasks

- Review `PTHR35038` (OmcE's family) and `PTHR30333` follow-up on OmcT.
- Review OzpA (`GSU2075`), the serine protease whose cleavage licenses OmcZ
  polymerisation, and the archaeal OmcZ-type cytochromes from the ANME work.
- Build the extracellular electron transfer module. Modules model reusable
  mechanisms, and this one — secretion through the PilA-N/PilA-C filament,
  proteolytic maturation, polymerisation, conduction to an acceptor — is a good fit.
  There is currently no EET module in `modules/`.
- Draft the three process terms above and submit the component term.
- Decide whether a structural condition type belongs in `rules/curated`. No rule can
  currently fire on OmcE or OmcZ, because neither has a usable sequence signature and,
  if the class really is defined by heme packing, neither may ever get one. The family
  review schema already understands structure (`site_source: STRUCTURE`, residue sites
  with contact atoms and PDB entries), so the machinery exists one level up. Related:
  [STRUCTURE_FUNCTION](STRUCTURE_FUNCTION.md), which argues that fold and site geometry
  persist where sequence HMMs fail and found it added nothing for lanmodulin; this
  class is the counter-case.

## Key references

| Reference | What it establishes |
|---|---|
| PMID:30951668 | OmcS filament structure; the conductive appendages are cytochrome polymers, not pili |
| PMID:35798889 | OmcE filament; no sequence or fold similarity to OmcS, same heme packing |
| PMID:36732469 | OmcZ structure; OzpA-controlled assembly; homologs in bacteria and archaea |
| PMID:36062910 | Independent OmcZ structure; cytochrome polymers arose more than once |
| PMID:37290436 | Two archaeal ECNs; the class spans both prokaryotic domains |
| DOI:10.1038/s41467-026-78976-x | Archaeal OmcZ-type nanowire at 3.3 Å from electrode-grown ANME; six phylogenetic groups |
| PMID:16332857 | Founding genetics for omcS and omcE |
| PMID:19461962 | Founding genetics for omcZ; omcE dispensable on anodes |
| PMID:34471289 | Export of OmcS and OmcZ requires the PilA-N/PilA-C filament |
