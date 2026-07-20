---
title: "PSEPK ppu00760 NAD+ biosynthesis and salvage batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [nadB, nadA, nadC, nadD, nadE, pncB, pncC, PP_3298]
autolink_gene_symbols: false
---

# PSEPK ppu00760: NAD+ biosynthesis and salvage

- Module: `nad_biosynthesis_salvage`
- Broad KEGG ppu00760 candidate genes: 30
- Additional domain-based hole-fill candidates: 1
- Primary ppu00760 bucket genes: 25
- Selected constructive-pathway genes: 7
- Selected uncertain family paralogs: 1
- Excluded broad-map genes: 23
- Selected reviews with PENDING actions: 0
- OpenScientist provider: gene, generic module, and module/pathway/taxon runs

## Boundary

This batch covers constructive NAD+ metabolism in *Pseudomonas putida* KT2440:

1. De novo L-aspartate to quinolinate: `nadB` and `nadA`.
2. Quinolinate to NaMN: `nadC`.
3. Shared NaMN to deamido-NAD to NAD+ completion: `nadD` and the
   ammonia-dependent `nadE`.
4. Direct nicotinate/Preiss-Handler entry: `pncB`.
5. NMN deamidation into the NaMN branch: `pncC`.
6. Hole-filled specificity gap adjacent to NMN salvage: `PP_3298`, a second
   compact CinA-C/PncC-family protein that is reviewed but not asserted as an
   NMN deamidase or catalytic module member.

The boundary ends at NAD+. Nicotinate degradation, NADP formation, redox
balancing, NAD-consuming reactions, broad nucleotide turnover, and unrelated
aldehyde metabolism are outside the module.

The reusable graph is deliberately limited to L-aspartate de novo synthesis
and selected salvage entries. Its root requires one or more complete
realizations: either a NaMN-producing precursor route followed by the required
NaMN-to-NaAD-to-NAD+ completion steps, or NAMPT-dependent NMN production
followed by direct NMN-to-NAD+ adenylylation. Route expansion produces 17
nonempty minimal routes, and the empty context does not satisfy the module.
PncB- and PncC-dependent routes connect only to NaMN completion; the NAMPT
route connects only to direct NMN completion. Tryptophan/kynurenine de novo
NAD+ synthesis remains owned by the reusable `kynurenine_nad_de_novo` module,
which this module references instead of duplicating.

## Selected Genes

| Gene | Locus | UniProt | Role | Evidence assessment |
|---|---|---|---|---|
| `nadB` | PP_1426 | Q88MZ2 | L-aspartate oxidase; de novo entry | NadB-specific family, RHEA:25876, and pathway mapping agree; target record is unreviewed. |
| `nadA` | PP_1231 | Q88NH8 | [4Fe-4S] quinolinate synthase | HAMAP/type 1 NadA family and RHEA:25888 agree; target record is unreviewed. |
| `nadC` | PP_0787 | Q88PR1 | Quinolinate phosphoribosyltransferase to NaMN | NadC domains, EC 2.4.2.19, RHEA:12733, and pathway mapping agree; target record is unreviewed. |
| `nadD` | PP_4810 | Q88DL5 | NaMN adenylyltransferase to deamido-NAD | Reviewed UniProt/HAMAP NadD record and RHEA:22860. |
| `nadE` | PP_4869 | Q88DF6 | Ammonia-dependent deamido-NAD amidation | Reviewed UniProt/HAMAP ammonia-specific enzyme and RHEA:21188; glutaminase-family spillover was removed. |
| `pncB` | PP_4868 | Q88DF7 | Nicotinate phosphoribosyltransferase to NaMN | Reviewed UniProt/HAMAP NAPRTase record and RHEA:36163. |
| `pncC` | PP_1628 | Q88ME5 | NMN deamidase to NaMN | PncC-specific TIGR00199/CinA-C architecture plus experimentally established bacterial family role; no direct Q88ME5 assay was found. |
| `PP_3298` | PP_3298 | Q88HQ5 | Unresolved CinA-C/PncC-family paralog | Domain-only hole-fill from `orphan:domain_only_no_pathway`; no catalytic name, EC, GO activity, or specificity assay, so it is excluded from the catalytic core. |

All 38 seeded GOA rows across the eight selected reviews were assessed; PP_3298
has no GOA rows. No NEW rows were added because the seven catalytic functions
were already present. The family-supported salvage placement of `pncC` is kept
as module context rather than added as a target-level GO:0034355 core-function
term, and no target-specific experiment justified an activity assertion for
PP_3298.

## PncA Gap

KT2440 has no annotated canonical PncA nicotinamidase. On 2026-07-20, exact
UniProt proteome queries against UP000000556 returned no entries for `gene:pncA`,
EC 3.5.1.19, protein name `nicotinamidase`, PncA-specific InterPro IPR052347,
NCBIfam NF008623, or PANTHER PTHR11080. Ten proteins carry the broad
isochorismatase Pfam PF00857, but that fold is not specific enough to nominate a
PncA replacement. Independent queries also returned no `nadV`, EC 2.4.2.12,
PANTHER PTHR43816, or nicotinamide phosphoribosyltransferase entry. Therefore
the defensible gap is salvage of free nicotinamide by either deamidated or
amidated entry; no candidate is proposed.

`pncC` does not close this gap: PncC acts on NMN, not nicotinamide. It remains in
scope because NMN deamidation yields NaMN and feeds the Preiss-Handler
completion branch. The nicotinamidase gap does not preclude uptake of nicotinate
for `pncB` or recycling of NMN through `pncC`.

## Exclusions

| Category | Genes | Boundary reason |
|---|---|---|
| Nicotinate degradation | `nicA`, `nicB`, `nicC`, `nicD`, `nicF`, `nicX`, `maiA` | Consume nicotinate through the degradation pathway rather than construct NAD+. `nicF` is maleamate amidohydrolase, not PncA. |
| Pyridine-nucleotide redox balancing | `pntAA`, `pntAB`, `pntB`, `sthA` | Interconvert NAD(H) and NADP(H); they do not synthesize the pyridine nucleotide scaffold. |
| NADP formation | `nadK` | Phosphorylates NAD+ to NADP+ downstream of this module endpoint. |
| NAD/nucleotide consumption or turnover | `ushA`, `surE`, `mazG`, `PP_2531`, `nudC`, `cobB__Q88BY5` | Hydrolysis, deacylation, or broad nucleotide turnover is outside constructive biosynthesis. |
| NAD-consuming toxin/effector | `PP_3103` | Ntox46 and Tre1-like domains support an NAD+-consuming ADP-ribosyltransferase role, not constructive NAD+ metabolism. |
| Aldehyde and amino-acid metabolism | `davD`, `sad-I`, `sad-II`, `gabD-II` | Semialdehyde dehydrogenases assigned to other metabolic routes, not NAD+ biosynthesis. |

## Curation Decisions

- Broad molecular-function parents on `nadB`, `nadA`, `nadC`, `nadD`, and
  `nadE` were modified to their leaf catalytic activities.
- `nadE` GO:0003952 and GO:0004359 were removed. Q88DF6 is a 275-residue
  ammonia-dependent NAD synthetase with the IPR022926 ammonia-specific domain
  and no glutaminase module.
- `nadC` GO:0034213 was retained as non-core because the reaction consumes
  quinolinate, while its physiological role in this batch is NAD+ biosynthesis.
- Cofactor or substrate-binding terms were retained as non-core where valid.
- Each selected KT2440 protein is a representative member of its supported
  leaf family role alongside an experimentally stronger exemplar. Ancestral
  nodes are retained only for NadB, NadC, and the generic PncA branch, where
  tracked local PAINT TSVs verify the node and catalytic GO term. NadA, PncB,
  NadD, the ammonia-specific NadE, and PncC carry no PTN assertion.
- Provider reports were treated as literature-triage context, not as substitutes
  for target-specific evidence.
- `pncC` core function is restricted to GO:0019159. Its role in the salvage
  realization is modeled at module level; no unsupported GO:0034355 NEW row was
  added to the target review.
- `PP_3298` remains MF-dark. Its batch inclusion records the manual
  domain-family hole-fill; the absence of specificity evidence is preserved as
  a module knowledge gap rather than converted into a catalytic annotation.
- Requiredness and route expansion were checked programmatically: 16 complete
  NaMN routes and one complete NAMPT/NMN route are selectable, no root segment
  is optional, and no NaMN-producing route can enter the direct NMN branch.

## OpenScientist Assessment

The PSEPK pathway report independently recovered the seven catalytic genes, the
constructive-versus-catabolic boundary, the ammonia-dependent identity of NadE,
and the absence of canonical PncA/NadV entries. Several additional claims were
checked rather than accepted verbatim:

- The generic report supports the NaMN/NMN branch split, shared deamido-NAD
  completion, and family-level variant framing. Its NR/NadR discussion and
  mammalian NMNAT2/SARM1 disease section are contextual extensions; they do not
  expand this module, and the NAD-consuming SARM1 reaction remains out of scope.
- PP_3298 (Q88HQ5) is a second 167-aa protein with IPR008136, PF02464, and
  TIGR00199. It lacks a submitted PncC name, EC assignment, GO activity, and
  experimental evidence. It is included as an unresolved, domain-based
  hole-fill and module knowledge gap, but is not substituted for Q88ME5 or
  promoted into the catalytic graph.
- PP_2860 (Q88IY9) is annotated as a PnuC nicotinamide-riboside transporter, but
  the report did not establish a downstream NR kinase/completion route. It is
  outside the commissioned ppu00760 inventory and is retained as a future
  salvage question rather than added to the module realization.
- PP_3103 (Q88I96) independently resolves to InterPro IPR028238/IPR049195 and
  Pfam PF15538/PF21724 toxin domains. This supports exclusion as an NAD+
  consumer, while its exact physiological target remains untested.
- The report's suggestion that PncC handles nicotinamide released by NAD+
  consumers was rejected. PncC deamidates NMN; without PncA or NadV, free
  nicotinamide is the actual unresolved salvage gap.
- The report's GO:0003952 recommendation for `nadE` was rejected. That term is
  glutamine-hydrolyzing NAD+ synthase activity, whereas Q88DF6 is the compact
  ammonia-dependent enzyme represented by GO:0008795.

## Research Artifacts

- Generic module report:
  `modules/nad_biosynthesis_salvage-deep-research-openscientist.md`
- PSEPK ppu00760 module report:
  [`PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist.md`](../deep-research/PSEPK__nad_biosynthesis_salvage__ppu00760-deep-research-openscientist.md)
- Gene reports are stored beside each selected review under `genes/PSEPK/<gene>/`.
- Complete machine-readable candidate inventory and disposition:
  `projects/P_PUTIDA/batches/ppu00760_nad_biosynthesis_salvage.tsv`

## Workflow

- [x] Fetch selected gene scaffolds.
- [x] Curate all selected GOA rows with no PENDING actions.
- [x] Revise the reusable species-neutral module.
- [ ] Complete and assess all OpenScientist runs.
- [ ] Validate all selected reviews and the module.
- [ ] Render all touched gene, module, and project pages.
- [ ] Open the batch pull request.
