# PHB2 (Prohibitin-2, Q99623) — review notes

Reviewed for issue #3956 (PINK1-Parkin mitophagy project, `projects/MITOPHAGY.md`),
which lists PHB2 as the inner-membrane ("alternative") mitophagy receptor.

No provider deep-research file could be generated for this gene in the run that
produced the review: no Perplexity/OpenAI/Falcon credentials were available in the
environment, so `just deep-research` was not runnable. Per `CLAUDE.md` these notes are
therefore hand-written from the cached publications, the UniProt record and database
queries, and are **not** named as a `-deep-research-<provider>.md` file. Almost all of
PHB2's cited literature is abstract-only in `publications/` — only PMID:28017329,
PMID:31522117, PMID:21328542, PMID:32276428, PMID:19496786, PMID:30021884,
PMID:20833797, PMID:34800366 and (fetched for this review) PMID:23241883 have full
text. Where the judgement depends on something only the full text could settle, the
review says so rather than overruling the curator.

## What the protein is

- 299 aa, single-span inner mitochondrial membrane (IMM) protein of the prohibitin
  (Band 7/SPFH) family: `InterPro; IPR000163; Prohibitin`, `Pfam; PF01145; Band_7`,
  `PANTHER; PTHR23222:SF1; PROHIBITIN-2`. Protein existence 1 (evidence at protein
  level), with a 3D structure of the C-terminal heptad-repeat region.
- Historically named three times over, which is why its annotation set is so
  heterogeneous: **BAP37** (B-cell receptor-associated protein, from the CD86/B-cell
  work), **REA** ("repressor of estrogen receptor activity", from the nuclear
  corepressor work) and **D-prohibitin**/PHB2 (from the mitochondrial work). ASURA is
  a fourth name, used in the sister-chromatid-cohesion papers.
- Obligate partner of PHB1: [PMID:11302691 "We show that the mammalian prohibitins are
  present in the inner mitochondrial membrane and are always bound to each other, with
  no free protein detectable."]. PHB1+PHB2 assemble into a ring-shaped ~1 MDa
  supercomplex in the IMM (the `GO:0035632` mitochondrial prohibitin complex).
- The C-terminal heptad repeat is the oligomerisation element:
  [PMID:31522117 "We found that the HR region of PHB2 forms a dimeric antiparallel
  coiled-coil with a highly charged surface."], and
  [PMID:31522117 "Disruption of the HR coiled-coil abolishes well-ordered PHB complexes
  and the mitochondrial tubular networks accompanying PHB-dependent signaling."].

## Core function 1 — inner-membrane mitophagy receptor

This is the function the mitophagy project cares about, and it is the best-evidenced
single claim about PHB2.

- [PMID:28017329 "Here, we identify the inner mitochondrial membrane protein, prohibitin
  2 (PHB2), as a crucial mitophagy receptor involved in targeting mitochondria for
  autophagic degradation."]
- The binding is direct and LIR-dependent. Three candidate W/F/YxxL/I/V motifs were
  tested and only one works:
  [PMID:28017329 "Thus, we conclude that amino acids 121–124 (YQRL) represent the PHB2
  LIR domain."], after
  [PMID:28017329 "In contrast, a Y121A/L124A mutation in StrepII-SUMO- PHB2 blocked in
  vitro binding to GST-LC3 (Figure 5C)."]
- The LIR is required for the function, not merely for the binding, and the mutant is
  correctly localised — so the phenotype is not an indirect structural effect:
  [PMID:28017329 "Together, these data indicate that PHB2 functions in mitophagy via an
  interaction between its LIR domain and LC3, rather than indirectly as a result of
  other effects on mitochondrial structure or function."]
- Mechanistically PHB2 is only reachable after the outer membrane is breached:
  [PMID:28017329 "The binding of PHB2, an IMM protein, to LC3-II during mitophagy
  suggested that OMM rupture was necessary for binding to occur."]
  This is why the receptor is at the IMM and why "type 2" (depolarisation-/Parkin-
  initiated) mitophagy is the setting in which the human experiments were done
  (oligomycin/antimycin-treated HeLa/Parkin cells and Parkin-expressing
  `Phb2flox/flox` MEFs).
- Conserved and physiological: [PMID:28017329 "Thus, sperm-derived phb-2 is essential
  for the proper degradation of paternal mitochondria."] — i.e. PHB2 also works in a
  Parkin-independent mitophagy event, so the general term `GO:0000423` is true of the
  gene even though the human rows are specifically type 2.
- Separable from the structural role: [PMID:28017329 "Our results with the PHB2 LIR
  domain mutant indicate that previously described functions regulated by prohibitins,
  including OPA1-dependent cristae morphogenesis and cellular proliferation, are
  functionally distinct from its interaction with LC3 and role as a mitophagy
  receptor."]

Matching MF term: `GO:0140580` mitochondrion autophagosome adaptor activity (synonym
"mitophagy receptor"; definition "The binding activity of a molecule that brings
together a mitochondrial membrane and an autophagosome membrane during mitophagy").
PHB2 has no MF annotation for this — the LC3-binding evidence currently sits in GOA as
a bare `GO:0005515` IPI row with `WITH` = `UniProtKB:Q9GZQ8` (MAP1LC3B), which is where
this review redirects it. FUNDC1 (`genes/human/FUNDC1`) already carries `GO:0140580`
for the same kind of activity at the outer membrane.

## Core function 2 — IMM scaffold that stabilises respiratory-chain and other clients

- UniProt frames it as a chaperone: `CC FUNCTION` "functions as a chaperone protein that
  stabilizes mitochondrial respiratory enzymes and maintains mitochondrial integrity in
  the IMM, which is required for mitochondrial morphogenesis, neuronal survival, and
  normal lifespan".
- PHB2 loss fragments mitochondria and destabilises clients:
  [PMID:17008324 "RNA interference-mediated knockdown of PHB2 in HeLa cells resulted in
  caspase-dependent apoptosis through down-regulation of Hax-1 and fragmentation of
  mitochondria."]
- The prohibitin ring sits in cardiolipin-enriched microdomains assembled with SLP-2
  (STOML2): [PMID:21746876 "We propose that the function of SLP-2 is to recruit
  prohibitins to cardiolipin to form cardiolipin-enriched microdomains in which electron
  transport complexes are optimally assembled."] Note the direction of the
  stabilisation shown in the other SLP-2 paper is SLP-2 → prohibitins:
  [PMID:18339324 "Depleting HeLa cells of SLP-2 lead to increased proteolysis of
  prohibitins and of subunits of the respiratory chain complexes I and IV."] — so that
  paper's own direct result has prohibitins as a *client*, with their stabilising role
  inferred. The `GO:0050821` claim is nevertheless carried by PMID:17008324 (HAX1) on
  this gene.
- Scaffold-dependent cardiolipin remodelling (mouse, ISS source for `GO:1900208`):
  [PMID:24856930 "Prohibitins form large protein and lipid scaffolds in the inner
  membrane of mitochondria that are required for mitochondrial morphogenesis, neuronal
  survival, and normal lifespan."] and
  [PMID:24856930 "The loss of PHB/DNAJC19 complexes affects cardiolipin acylation and
  leads to the accumulation of cardiolipin species with altered acyl chains."]
- Sphingosine-1-phosphate is a specific, high-affinity ligand of PHB2 (not PHB1) that
  tunes complex IV:
  [PMID:20959514 "Here, we demonstrate that S1P, produced in the mitochondria mainly by
  sphingosine kinase 2 (SphK2), binds with high affinity and specificity to prohibitin 2
  (PHB2), a highly conserved protein that regulates mitochondrial assembly and
  function."] and
  [PMID:20959514 "Moreover, depletion of SphK2 or PHB2 led to a dysfunction in
  mitochondrial respiration through cytochrome-c oxidase."]

The best-fitting MF for "holds the complex together" is `GO:0140378` protein complex
scaffold activity, which the crystal-structure/HR-disruption result in PMID:31522117
supports directly. It is used only twice in human (CCDC6, CHIC2) and on no
mitochondrial complex subunit, so this review does **not** propose it as a new
annotation — the systematic absence looks like a convention rather than a gap — and
raises it as a question instead. It is used in `core_functions` as this review's own
synthesis.

## Secondary, compartment-specific functions (real, but not the core)

- **Nuclear corepressor (REA).** [PMID:10359819 "This clone, denoted REA for 'repressor
  of estrogen receptor activity,' encodes a 37-kDa protein that is an ER-selective
  coregulator."] and "Its competitive reversal of steroid receptor coactivator 1
  enhancement of ER activity and its direct interaction with liganded ER suggest that it
  may play an important role in determining the sensitivity of estrogen target cells".
  Nuclear import of PHB2 is ERα/estradiol-dependent:
  [PMID:17008324 "although PHB2 is predominantly expressed in the mitochondria of HeLa
  cells, it translocates to nucleus in the presence of estrogen receptor alpha and
  estradiol"]. In the nucleus it is part of a ZNF703-DCAF7-PHB2 corepressor assembly:
  [PMID:21328542 "Moreover, DCAF7 and PHB2 co-localized with ZNF703 in the dot-like
  nuclear structures (Fig 2D)."]. A second nuclear repression route runs through RNF2:
  [PMID:18629613 "Luciferase reporter assays showed that RNF2 represses the
  CP2c-stimulated luciferase activity in a PHB2 dose-dependent manner."].
  Note PHB1 already carries `GO:0003714` transcription corepressor activity (IDA,
  PMID:18487222), which is the comparator for proposing the same MF for PHB2.
- **Plasma-membrane/cell-surface pool.** Surface prohibitins on activated T cells
  [PMID:22417827 "we found that a considerable proportion of prohibitin-1 and -2 induced
  in response to T cell activation was expressed on the surface of activated T cells"],
  and PHB2 as the surface receptor for IGFBP-6-driven migration
  [PMID:24003225 "Here, we report that prohibitin-2 (PHB2), a single-span membrane
  protein, is a key regulator of IGFBP-6-induced RMS cell migration."].
- **CD86/B-cell arm (mouse, ISS source for `GO:0002639`, `GO:0042113`, `GO:1901224`).**
  [PMID:23241883 "Using a proteomics-based identification approach, we show that the
  tyrosine-containing transmembrane adaptor proteins prohibitin (Phb)1 and Phb2 bind to
  CD86."] The NF-κB branch this paper reports is the **canonical** one —
  "which we previously reported leads to NF-κB p50/p65 activation" and IκBα
  phosphorylation — so the `GO:1901224` *non-canonical* NF-κB term that GOA propagates
  from the mouse row looks like a term-choice error (see `source_defects` in the
  review).
- **RIG-I antiviral signalling scaffold.** PHB complexes tether CLPB (IMS) to MAVS
  (OMM): [PMID:31522117 "Taken together, these results demonstrated that CLPB bridges
  PHB complexes (IMM) and MAVS (OMM) with the assistance of AKAP1 and ATAD3A at the IMS
  and invokes an immune response from the mitochondrial signalosome (Figure S5I)."] and
  the dependence on PHB is direct:
  [PMID:31522117 "Importantly, the virus-induced MAVS-CLPB interactions were abolished
  when the PHB proteins were depleted by siRNA (Figure 5J), suggesting that the scaffold
  function of the PHB complexes is required for the phenomenon."]
- **Sister chromatid cohesion (ASURA).** [PMID:23548868 "The present co-immunoprecipitation
  analysis reveals that ASURA interacts with cohesin subunit Scc1 in vivo."] A single
  group, orthogonal to everything else known about the protein; kept non-core.
- **Virus host factor.** EV-A71 VP1 (PMID:32276428), HIV-1 Env-CT (PMID:19906925),
  SARS-CoV nsp2 (PMID:19640993), CHIKV entry (PMID:22997079 — reported for "prohibitin",
  and annotated to PHB1 as well). These are host-pathogen interactions, not PHB2
  functions.

## Annotations this review argues against

1. **`GO:0030449` regulation of complement activation, IDA, PMID:17070910 — wrong gene
   product.** The paper's own abstract excludes PHB2:
   [PMID:17070910 "PHB1, but not the closely related PHB2, was able to enhance
   complement activation and induce lysis of sensitized sheep erythrocytes when added
   with normal serum but not with C3-deficient serum."] QuickGO confirms the paper was
   also annotated to PHB1 (P35232) for `GO:0001850` and `GO:0001851`, i.e. the intended
   target carries it. This is the "abstract defines the entity as another protein" case
   in `CLAUDE.md`, so the claim is confident: `REMOVE` + `WRONG_GENE_PRODUCT`
   (`CONFIRMED`, `DELETE_ROW`).
2. **`GO:0043410` positive regulation of MAPK cascade, IDA, PMID:24003225 — contradicted
   by its own paper.** [PMID:24003225 "In contrast, IGFBP-6-induced MAPK pathway
   activation was not affected, suggesting that PHB2 may act as a downstream effector of
   these pathways."] PHB2 knockdown abolished migration but left MAPK activation intact,
   so the paper places PHB2 downstream of the cascade, not as a positive regulator of
   it.
3. **`GO:0006606` protein import into nucleus, IDA, PMID:17008324 — PHB2 is the cargo.**
   The result is that PHB2 itself translocates to the nucleus when ERα and estradiol are
   present. Being transported is not participating in the transport process
   (`CLAUDE.md`: "being the thing it acts on is not participation"). Marked over-annotated
   rather than removed, because the full text is not in the cache and could conceivably
   show PHB2 promoting the import of another protein.
4. **`GO:0005741` mitochondrial outer membrane, IDA, PMID:17008324 — wrong membrane.**
   The complex reported there contains VDAC2 (OMM) and ANT2 (IMM), i.e. it spans a
   contact site; co-purification with an OMM protein does not place PHB2 in the OMM, and
   every dedicated localisation study and UniProt place it in the IMM. The mitophagy
   mechanism depends on PHB2 being behind the OMM.
5. **`GO:0043066` negative regulation of apoptotic process, IMP, PMID:17008324 and
   `GO:0070374` positive regulation of ERK1/2 cascade, IMP, PMID:22417827 —
   over-annotation from indirect perturbation.** Knocking out a structural IMM scaffold
   fragments mitochondria, which triggers apoptosis downstream; and the same PHB1/PHB2
   paper that reports mitochondrial roles cautions against reading expression as an
   apoptosis role: [PMID:11302691 "expression levels are indicative of a role in
   mitochondrial metabolism, but are not compatible with roles in the regulation of
   cellular proliferation or apoptosis"]. The ERK row rests on antibody-bead
   co-clustering of surface prohibitins, which does not separate PHB1 from PHB2.

## Gaps and open questions

- How the IMM/PHB2 becomes exposed in *Parkin-independent* mitophagy is unknown:
  [PMID:28017329 "It is not yet known how the IMM and its mitophagy receptor PHB2 become
  exposed during Parkin-independent mitophagy, as occurs during paternal mitochondrial
  elimination during C."] (the sentence runs on into "C. elegans fertilization").
- Whether PHB2's own LIR is regulated (phosphorylation, as for FUNDC1 and BNIP3L) is not
  established; PHB2 is known to be tyrosine-phosphorylated downstream of IGFBP-6 at the
  plasma membrane, but no modification of the YQRL LIR has been reported.
- No GO molecular function describes what the prohibitin ring does structurally;
  `GO:0140378` exists but is essentially unused for complex subunits.
