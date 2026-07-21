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
- Selected gene OpenScientist reports: 8/8 complete and assessed

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
- The glutamine-dependent NAD synthetase variant uses reviewed human NADSYN1
  (UniProtKB Q6IA69) as an orthology exemplar. PANTHER PTHR23090:SF9 was
  rejected as a selector because the local family export also contains compact
  ammonia-dependent proteins, so the subfamily does not safely encode nitrogen
  donor specificity. Rendered QC still calls this leaf ungrounded because it
  counts family `representative_members` but not the concrete `ORTHOLOG_OF`
  target; Q6IA69 is present and linked in the rendered node.
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

The fresh PSEPK pathway/taxon report was generated from the final route graph
and the 30-gene ppu00760 candidate inventory. It independently recovered the
seven catalytic genes, the constructive-versus-catabolic boundary, the
ammonia-dependent identity of NadE, and the absence of canonical PncA/NadV
entries. Several provider extensions were checked rather than accepted
verbatim:

- The report alternates between "about eight" in-scope genes and a seven-gene
  catalytic list. The curated count is seven catalytic genes plus PP_3298 as an
  unresolved manual hole-fill; PP_3298 was not in the commissioned ppu00760
  candidate list and was not assessed by this pathway run.
- Q88JT5/PP_2562 was proposed as the sole cryptic PncA candidate from its
  isochorismatase-like annotation. It is one of ten KT2440 proteins carrying
  broad PF00857, has no EC 3.5.1.19 assignment or specificity assay, and was not
  promoted. The canonical PncA gap remains open without a nominee.
- The report's single-copy and low-paralog-ambiguity language was not adopted
  for NMN deamidation. PP_3298 is a second compact PF02464/TIGR00199 protein and
  remains unresolved rather than transferred into the PncC catalytic role.
- PncC deamidates NMN, not nicotinamide. Without PncA or NadV, its presence does
  not establish nicotinamide salvage; the report's "indirect" wording does not
  create a route from free nicotinamide.
- PnuC/Q88IY9 and Q88IZ0 were useful transporter/regulatory leads, but neither
  establishes the missing NR-to-NAD+ chemistry. They remain future questions
  outside this module realization.
- Exact negative-search, copy-number, and network-context claims in the report
  have no retained query or alignment artifacts. Curated assignments remain
  grounded in the fetched target records, local inventory, and verified
  reaction identifiers.
- The fresh generic report reflects the final two-topology route graph: NaMN
  sources require adenylylation plus deamido-NAD amidation, while NAMPT-derived
  NMN requires direct NMN adenylylation. Its NadD/NMNAT family alternatives and
  ammonia/glutamine donor variants are useful literature-triage context.
- Cross-species claims about physical NadB-NadA channeling, strict bacterial
  NadD substrate exclusion, PncC turnover physiology, universal essentiality,
  detailed PncA mechanism, and ancestral route order were not promoted. The
  curated reactions and route requiredness remain authoritative.
- The generic report's provenance figure is illustrative, not a route
  enumeration. Its Markdown image name does not match the archived provenance
  filename, so the bundled provider HTML/PDF is the intact visual artifact; the
  provider Markdown was not edited.

The first PP_3298 OpenScientist job (`max_iterations=3`) timed out at the
7200-second provider ceiling without a file. A bounded `max_iterations=2`
retry completed in 5155 seconds and retained both HTML and PDF artifacts. The
report correctly identifies a compact CinA-C/PncC-family protein, but promotes
NMN deamidase activity, cytoplasmic localization, and pathway physiology from
an unsaved 38.1% alignment, asserted motif conservation, and negative genomic
context, while omitting comparison with the better-annotated Q88ME5/pncC
paralog. It simultaneously acknowledges no direct Q88HQ5 experiment, moderate
identity, inactive family members, and untested specificity. Those stronger
claims were not propagated: PP_3298 remains MF-dark, outside the catalytic
graph, and absent from representative members pending a product-forming
specificity assay.

## Research Artifacts

- Both refreshed module-level OpenScientist reports record
  `max_iterations: 3` and provider `timeout: 7200` in their generated
  frontmatter.
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
- [x] Complete and assess all OpenScientist runs.
- [x] Validate all selected reviews and the module.
- [x] Render all touched gene, module, and project pages.
- [x] Open the batch pull request.
