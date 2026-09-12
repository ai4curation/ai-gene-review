# tomm-22 (C. elegans) — Research Notes

UniProt: O17287 (TOM22_CAEEL) · WormBase: WBGene00021133 · ORF: W10D9.5 · Chromosome II
Gene family: Tom22 (InterPro IPR005683; Pfam PF04281; PANTHER PTHR12504) · 109 aa

## Journal

### 2026-07-03 — initial synthesis

Deep research: falcon provider succeeded (`tomm-22-deep-research-falcon.md`, 41 citations,
Edison "Literature" model, 872 s). The perplexity-lite fallback failed (401 quota) but was
not needed. The falcon report is high quality and surfaced the key worm-genetic and
structural literature used below.

## What TOMM-22 is

TOMM-22 is the *C. elegans* ortholog of TOM22, a conserved, small single-pass integral
protein of the mitochondrial **outer membrane** and a central receptor/scaffold subunit of
the **TOM complex** (translocase of the outer mitochondrial membrane). The TOM complex is
the main entry gate through which the ~99% of mitochondrial proteins that are
nucleus-encoded and made on cytosolic ribosomes are imported into the organelle.

Topology (UniProt, by similarity to human Q9NS69): cytoplasmic 1–60, transmembrane helix
61–77, intermembrane-space (IMS) tail 78–109. This is the canonical TOM22 architecture: an
N-terminal cytosolic receptor domain, a single TM anchor, and a C-terminal IMS domain.

UniProt curated FUNCTION (O17287): *"Central receptor component of the translocase of the
outer membrane of mitochondria (TOM complex) responsible for the recognition and
translocation of cytosolically synthesized mitochondrial preproteins"* (By similarity) and
*"Together with the peripheral receptor tomm-20 functions as the transit peptide receptor
and facilitates the movement of preproteins into the translocation pore"*
[ECO:0000269|PubMed:21264209].

## Conserved molecular function (from orthologs — yeast/human/mammalian)

- **Presequence (targeting-sequence) receptor.** TOM20 and TOM22 recognize the N-terminal
  amphipathic targeting presequences of preproteins; TOM22 has both a *cis* (cytosolic) and
  a higher-affinity *trans* (IMS) presequence-binding site, and hands substrates to the
  TIM23 inner-membrane translocase. [PMID:35733257 "Tom20 and Tom22 are involved in
  targeting signal recognition during protein import"] (human TOM cryo-EM, Su et al. 2022).
- **Chaperone-like activity.** The cytosolic domain of mammalian Tom20/Tom22 suppresses
  aggregation of unfolded preprotein substrates, keeping them import-competent.
  [PMID:14699115 "Tom20 and Tom22 have chaperone-like activity"] (Yano et al. 2004).
- **Structural organizer / scaffold.** Two TOM22 molecules sit between the two TOM40
  β-barrels in the dimeric TOM core, tethering and stabilizing the complex (structural work
  in yeast/human; falcon report). TOM22 is one of the most ancient TOM subunits — the
  ancestral complex is thought to have consisted minimally of Tom40 + Tom22.

TOMM-40 (the β-barrel) forms the actual conducting pore; TOMM-22 is the receptor/scaffold
that contributes to import but does not itself form the channel. This is why its GOA
molecular-function annotation (GO:0008320) carries the **contributes_to** qualifier.

## Direct experimental evidence *in C. elegans* (loss-of-function only)

All worm data are RNAi/knockdown phenotypes; no biochemical assay of the worm protein and
no characterized null allele exist.

1. **Billing, Kao & Naredi 2011 (PMID:21264209)** — the primary functional paper. RNAi of
   *tomm-22* (as well as *tomm-20*) induces the mitochondrial unfolded protein response and
   causes a DAF-28/insulin secretion defect, but is milder than *tomm-40*:
   - [PMID:21264209 "RNAi against either tomm-20 or tomm-22 induced the mitochondrial
     unfolded protein response, indicating a perturbed mitochondrial protein handling"]
   - [PMID:21264209 "inactivation of tomm-20 or tomm-22 caused a defect in DAF-28 secretion"]
   - [PMID:21264209 "did not produce the highly penetrant larval arrest phenotype seen in
     tomm-40(RNAi) worms"]
   - The secretion defect is specific: ANF::GFP and INS-22::VENUS are secreted normally,
     and coelomocyte endocytosis is intact.
   - Framing of TOM receptor biology: [PMID:21264209 "TOM20 and TOM22, are receptors that
     recognize different subgroups of mitochondria-destined preproteins"] and
     [PMID:21264209 "it acts along with other components, such as Tom20 and Tom22, to import
     proteins into the mitochondria"].
   - The authors explicitly note how little is known in worm:
     [PMID:21264209 "In C. elegans, there are few reports describing functions of putative
     TOM-complex subunit homologues"].

2. **Bennett et al. 2014 (PMID:24662282)** — genome-scale *hsp-6p::gfp* UPRmt RNAi screen.
   *tomm-22* is a UPRmt inducer, classed as a protein-import gene:
   [PMID:24662282 "These included tomm-22, a component of the TOM complex which functions as
   a translocase in the outer mitochondrial membrane"] and grouped with
   [PMID:24662282 "a subset of RNAi clones related to mitochondrial protein import (tomm-22,
   E04A4.5, T09B4.9, F45G2.8, F15D3.7, and dnj-21)"]. Note the paper's thesis: UPRmt
   activation does not predict longevity — lifespan effects of import-gene RNAi are
   context-dependent, not a core function.

3. **Xin et al. 2022 (PMID:35608535)** — the strongest worm evidence that *tomm-22* is
   functionally required for import: [PMID:35608535 "knocking down TOM complex component
   tomm-22 abolished the effect of cco-1 RNAi on improving import capacity"]. TOM genes are
   themselves upregulated during UPRmt as an adaptive response:
   [PMID:35608535 "Genes encoding TOM complex proteins, including tomm-20, tomm-22, and
   tomm-40, were enhanced one- to twofold"].

4. **Tan et al. 2025 (PMID:40522955)** — uses *tomm-22(RNAi)* as the canonical
   "import-associated UPRmt" background for a metformin/aging study. Important for
   separating core function from downstream stress phenotype:
   [PMID:40522955 "the primary role of tomm-22 is a mitochondrial outer membrane transporter
   rather than a mitochondrial UPR stress regulator"] and
   [PMID:40522955 "The activation of hsp-6 response in tomm-22 RNAi worms in our study was
   likely a response to changes in the mitochondrial import machinery instead of a direct
   regulatory response to mitochondrial stress."].

Mechanistic UPRmt link (why an import defect activates UPRmt): the weak-MTS transcription
factor ATFS-1 fails to be imported when TOM/TIM capacity drops and instead goes to the
nucleus (Rolland et al. 2019, PMID:31412237, general mechanism — abstract does not name
*tomm-22*; treated as background, not tomm-22-specific evidence).

## KNOWN vs NOT KNOWN

KNOWN (well supported):
- Subunit of the TOM complex / mitochondrial outer membrane translocase complex (family +
  UniProt SUBUNIT + worm papers). CORE cellular component.
- Localizes to the mitochondrial outer membrane, single-pass (topology by similarity).
- Functions in protein import into mitochondria; required for import capacity in worm
  (Xin 2022). CORE biological process.
- Contributes to the complex's protein-transmembrane-transport activity as a
  receptor/scaffold (not the pore). CORE molecular contribution.
- Loss reduces import → activates ATFS-1/UPRmt (hsp-6) and impairs DAF-28/insulin
  secretion. These are downstream consequences of the import role, not separate functions.

NOT KNOWN (genuine gaps):
- **The worm protein's own biochemistry is unmeasured.** Presequence-binding (cis/trans),
  chaperone-like activity, and substrate-class specificity are inferred from yeast/human
  orthologs; no in vitro or in vivo binding assay of *C. elegans* TOMM-22 exists. The field
  itself flags the paucity of worm data (PMID:21264209). → MF_DARK / residual sub-gap.
- **Essentiality is unresolved.** Only RNAi (partial) data exist; *tomm-22(RNAi)* is far
  milder than *tomm-40(RNAi)* and no null/deletion allele has been characterized, so whether
  complete loss is lethal in *C. elegans* is unknown. → BIOLOGY gap.
- **Isoforms.** Two splice isoforms are annotated: a (O17287-1, full length) and b
  (O17287-2, "Missing 1..94" = lacks essentially the entire cytosolic receptor domain and TM
  anchor). The existence, expression, and function of isoform b are uncharacterized.
- **Lifespan direction is contradictory** across studies (Bennett 2014 reports increased
  mean lifespan on *tomm-22* RNAi; Tan 2025 describes the background as short-lived) — a
  pleiotropic/context-dependent readout, explicitly not a core function.

## Annotation review plan

| Term | Aspect | Ev | Decision | Rationale |
|---|---|---|---|---|
| GO:0005742 mito outer membrane translocase complex | CC | IBA | ACCEPT (core) | TOM complex subunit |
| GO:0030150 protein import into mito matrix | BP | IBA | ACCEPT (core) | entry receptor; import required (Xin) |
| GO:0008320 transmembrane protein transporter activity (contributes_to) | MF | IBA | ACCEPT (core, contribution) | receptor/scaffold, not pore — contributes_to correct |
| GO:0005741 mitochondrial outer membrane | CC | IEA | ACCEPT (core) | single-pass OMM |
| GO:0005741 mitochondrial outer membrane | CC | ISS | ACCEPT | same location, ISS from human ortholog |
| GO:0006886 intracellular protein transport | BP | IEA | KEEP_AS_NON_CORE | generic InterPro2GO parent of GO:0030150 |

Core MF for synthesis: GO:0030943 mitochondrion targeting sequence binding (conserved
presequence-receptor activity; the human TOMM22 review uses the same term — note it is
slated for eventual GO obsoletion in favor of a "mitochondrial signal sequence receptor
activity" NTR, but is live as of 2026-05/07).
