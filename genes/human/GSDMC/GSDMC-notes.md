# GSDMC (Q9BYG8) review notes

## Why this gene was selected

GSDMC is a contested-function case with an almost empty GOA. Three mutually incompatible
molecular pictures of the protein have been published, and the curated record carries
essentially none of them: five IBA rows propagated from the gasdermin family node, two
UniProt subcellular-location IEAs, one EXP plasma-membrane row, and one IDA cytoplasm row.
There is no GO annotation at all for pore formation, for vesicle targeting, or for anything
nuclear. So this is a curation gap layered on a live scientific dispute.

## The three positions

### Position A - intracellular (Rab7+ vesicle) permeabilization, not plasma-membrane pyroptosis

Pandey et al., *Immunity* 2025 (PMID:40701157, full text available) is the strongest
single body of work on GSDMC in its main tissue, the intestinal epithelium. It opens by
setting itself against the family paradigm:
[PMID:40701157 "Gasdermins are canonically associated with plasma membrane pore formation
and lytic cell death."]

Their central claims:

- Cathepsin S is the activating protease in intestinal epithelial cells, and lysis is not
  the point: [PMID:40701157 "Although IEC cell death is not the main consequence of GsdmC
  cleavage, inserting a single amino acid (aa) within the lipid-binding motif to match that
  of the other gasdermins enhanced GsdmC oligomerization and increased GsdmC-mediated cell
  death."]
  This is the mechanistically important observation: GSDMC's beta1-beta2 lipid-binding
  motif is one residue *short* relative to the other gasdermins, and completing it converts
  GSDMC into a better killer. On this reading GSDMC is a deliberately poor pore-former.
- The target membrane is intracellular, not the plasma membrane:
  [PMID:40701157 "Mechanistically, instead of localizing to the plasma membrane, we showed
  that cleaved GsdmC targeted Rab7+ vesicles, such as late endosomes."] and, at the level
  of the primary imaging, [PMID:40701157 "Red fluorescent protein (RFP)-tagged
  CTSS-generated GSDMCN-ter colocalized with, and even penetrated into Rab7+ vesicles, when
  expressed in HeLa cells, unlike full-length GSDMC"].
- The downstream consequence is lipid-droplet/lipid-turnover control feeding type 2
  immunity: [PMID:40701157 "This modulated lipid droplet accumulation, which promoted
  goblet cell hyperplasia and type 2 immune responses."]
- They separate the two models pharmacologically: [PMID:40701157 "CID-1067700 treatment did
  not affect cell death in organoids or in HEK293T-overexpression mGSDMC2N-ter conditions,
  further supporting the idea that GSDMCs contribute to type 2 immunity by targeting Rab7+
  vesicles rather than modulating cell death"]
- And they state the generalization explicitly: [PMID:40701157 "Overall, this work expands
  the role of Gsdm beyond plasma membrane pore formation for pyroptosis and IL-1 family
  cytokine release."]

Note the important asymmetry: most of the mechanistic imaging is on murine GSDMC2/GSDMC4
(mouse has four *Gsdmc* paralogs) in HeLa cells and *C. elegans*, though human GSDMC is
also cleaved by CTSS and the human N-terminal fragment was the one imaged in HeLa.

### Position B - nuclear chromatin scaffold

Ren et al., *Cell Rep* 2026 (PMID:42176271, abstract only in our cache). The title is about
metabolic reprogramming, so the molecular claim is easy to miss; it is in the abstract:
[PMID:42176271 "phosphorylated STAT3 at Ser727 transcriptionally induces GSDMC, which
translocates into the nucleus via the IPO7-KPNB1-NUP93 complex."] and
[PMID:42176271 "In the nucleus, GSDMC functions as a scaffold molecule, recruiting NAT10 to
mediate histone H3 acetylation and recruiting BAZ1B/SMARCA5 to modulate chromatin
remodeling and chromatin accessibility."]

This asserts a molecular function with no membrane component at all. It is a single
laboratory, one paper, not independently replicated, and we have only the abstract. It is
worth noting that the original cloning paper already flagged nuclear-targeting sequence
features: [PMID:11223543 "Human homolog of mMlze (hMlze) contained one leucine zipper
structure and two potential nuclear localizing signals."] - although that same paper named
the protein *extranuclear* factor (MLZE = melanoma-derived leucine zipper-containing
extranuclear factor), so the older literature points the other way on localization.
I did not find independent corroboration of nuclear GSDMC acting as a chromatin scaffold.

### Position C - classical pyroptotic executioner

The founding result is Hou et al., *Nat Cell Biol* 2020 (PMID:32929201, full text):
[PMID:32929201 "GSDMC is specifically cleaved by caspase-8 with TNFα treatment, generating
a GSDMC N-terminal domain that forms pores on the cell membrane and induces pyroptosis."]
This is not merely a cell-biology inference; there is direct reconstitution:
[PMID:32929201 "the N-terminal domain, but not full-length GSDMC, bound to liposomes, as
evidenced by its detection in the liposome pellet"] and
[PMID:32929201 "Upon incubation with caspase-8-cleaved GSDMC, the liposome surface showed
multiple pores of regular shape and size"].
Independently, Zhang et al., *Cell Res* 2021 (PMID:34012073) reported the metabolite
alpha-ketoglutarate driving DR6/caspase-8-dependent [PMID:34012073 "GSDMC-dependent
pyroptosis"].

Wu et al., *Signal Transduct Target Ther* 2025 (PMID:41407678, full text) adds a third
protease: [PMID:41407678 "we discovered a chemical compound, dodecyl
1H-benzo[d]imidazole-5-carboxylate (DdBIC), that targeted the nuclear receptor Nur77 to
induce pyroptosis through cleaving GSDMC by granzyme B in melanoma cells."] and
[PMID:41407678 "reveals a novel paradigm, by which granzyme B, rather than caspases,
cleaves GSDMC for pyroptotic induction"].

**The DdBIC paper is weaker support for the physiological model than it looks.** It shows
GSDMC *can* be pushed into forming a lytic pore by a synthetic Nur77 ligand acting through
a long mito-ROS / OMA1 / OPA1 / PERK / ISR cascade. That establishes pore competence, not
that pore formation is what GSDMC normally does - which is exactly what Position A denies.
It also further destabilizes the canonical model in a second way, by making the activating
protease granzyme B rather than caspase-8. In other words, the three pyroptosis papers
agree that GSDMC can kill but disagree on what cleaves it (caspase-8 vs caspase-6 vs
granzyme B) and under what trigger.

### The field has named the problem

[PMID:41092892 "Cutting the Gordian knot: Untangling gasdermin C from pyroptosis."], a
2025 *Immunity* commentary on the Pandey paper, which nonetheless still frames GSDMC in
membrane terms: [PMID:41092892 "Membrane targeting and pore formation of gasdermin C are
facilitated by its proteolytic cleavage."]

## Adjudication taken in this review

1. **Pore-forming (wide pore channel) activity is retained as the core molecular
   function.** It is the only one of the three positions with direct, reconstituted,
   protein-level evidence (liposome binding, EM-visible pores, dye leakage; PMID:32929201),
   and it is reproduced across independent labs and independent activating proteases.
   Position A does *not* contradict pore competence - it accepts it and shows that
   completing the lipid-binding motif enhances it.
2. **What is contested, and recorded as contested, is the target membrane and the
   physiological consequence.** In the tissue where GSDMC is actually expressed at
   steady state (intestinal epithelium), the evidence favours permeabilization of Rab7+
   late endosomal vesicles with lipid-droplet consequences over plasma-membrane lysis.
   Both plasma-membrane annotations are therefore kept but demoted to non-core, and a
   NEW late endosome location is proposed from PMID:40701157.
3. **Pyroptosis is kept as non-core, not accepted as core.** It is real in caspase-8-driven
   cancer-cell settings and under the DdBIC/granzyme-B trigger, but the primary-tissue data
   and the incomplete lipid-binding motif argue it is not the default behaviour of this
   paralog. This is a deliberate demotion, not a rejection.
4. **Position B is recorded but not annotated.** One paper, abstract only, no independent
   replication, and a molecular claim (chromatin scaffold) that would be a major departure
   for a gasdermin. It goes into `suggested_questions` and `suggested_experiments` rather
   than into `existing_annotations`, because asserting `chromatin binding` or a
   `nucleus` location on this basis would put a machine-readable claim into the record
   that the evidence does not yet carry.

## The family-level IBAs

All five IBA rows trace to PANTHER node PTN000419132. I resolved the donor identifiers
(they are not inspectable as a PAINT tree from inside this repository, so I did **not**
attempt structured `propagation_review` metadata):

| GOA `WITH/FROM` id | resolves to |
|---|---|
| MGI:MGI:1916396 | mouse *Gsdmd* (ENSMUSG00000022575) |
| MGI:MGI:2146102 | mouse *Gsdmc2* (ENSMUSG00000056293) |
| MGI:MGI:3044668 | mouse *Gsdma3* (ENSMUSG00000064224) |
| UniProtKB:P57764 | human GSDMD |
| UniProtKB:Q96QA5 | human GSDMA |
| UniProtKB:Q8TAX9 | human GSDMB |
| UniProtKB:Q9BYG8 | human GSDMC (the target itself) |

Two observations that matter for the review:

- The three phospholipid-binding IBAs (GO:0005546, GO:0070273, GO:0001786) are seeded
  **only** by GSDMD (mouse and/or human). They assert exactly the inner-leaflet
  phosphoinositide/phosphatidylserine recognition paradigm that Position A argues GSDMC
  does *not* follow, given its one-residue-short beta1-beta2 lipid-binding motif. The only
  GSDMC-specific lipid data is a bulk liposome assay whose mix contained PC, PE, PS, PI and
  PI(4,5)P2 together (PMID:32929201 methods), which cannot resolve headgroup specificity.
  These are kept as non-core, with the doubt written into `reason`, rather than removed:
  per project guidance an IBA is a considered phylogenetic judgement and overturning one
  requires arguing with the node placement, which I could not inspect.
- GSDMC itself (UniProtKB:Q9BYG8) appears in the `WITH/FROM` of the GO:0070269 IBA. Per
  project guidance this is **not** circular: it marks that the target carries its own
  experimental grounding for the term, and the IBA then adds the claim that the function is
  inherited rather than lineage-specific.

`GO:0042742 defense response to bacterium` is the weakest of the five. Its donors are
GSDMD, GSDMA and GSDMB - each of which has direct antibacterial evidence - while GSDMC's
own documented in-vivo immune role is anti-*helminth* type 2 immunity, not antibacterial.
Kept as non-core and raised as a question for PAINT.

## Localization annotations

- `GO:0005737 cytoplasm` IDA from PMID:11223543. Our cache of that paper is abstract-only
  and the abstract does not state the localization; the curator read the full text. Per
  project rules this is accepted, not challenged. It is also biologically uncontroversial:
  full-length GSDMC is an autoinhibited cytosolic zymogen.
- `GO:0005886 plasma membrane` appears twice (IEA from UniProt SubCell SL-0039, and EXP
  from PMID:32929201). Both must carry the same action. The EXP row is genuine for the
  caspase-8/cancer-cell context but is precisely what PMID:40701157 reports *not* to happen
  for the physiologically cleaved intestinal form, so both are kept as non-core.
