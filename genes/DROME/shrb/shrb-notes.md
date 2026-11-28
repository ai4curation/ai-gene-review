# shrb (shrub, Vps32/Snf7/CHMP4; FBgn0086656; UniProtKB Q8T0Q4) review notes

## Scope and sources

- Fetched accession Q8T0Q4 (Swiss-Prot, 226 aa, 44 GOA rows). It is the only UniProt
  entry for shrb in a gene-name search, so no other accession carries rows.
- Deep research source: the FlyBase hand-written description
  (`shrb-deep-research-flybase.md`). No Falcon or Perplexity report was run.
- PAINT node placement: `shrb-bioinformatics/RESULTS.md`.
- Literature queries run (PubMed E-utilities and web search, 2026-11-17):
  `(shrub OR shrb OR CHMP4) AND Drosophila AND (membrane repair OR wound)` (3 hits, none
  a fly repair study), `ESCRT AND Drosophila AND plasma membrane repair` (4 hits, none
  testing Shrub), `(shrub OR shrb) AND Drosophila AND nuclear envelope` (1 hit,
  PMID:32032426), `(shrub OR shrb) AND Drosophila AND intraluminal vesicle*` (4 hits),
  `CHMP7 Drosophila` (0 hits); web searches "Drosophila Shrub ESCRT-III nuclear envelope
  sealing CHMP7" and "Drosophila shrub ESCRT-III plasma membrane repair wound".
  Result for membrane repair: no Drosophila experiment testing Shrub in plasma membrane
  or wound repair was found. Papers added to the cache for this review: PMID:32032426,
  PMID:16713958, PMID:27452459, PMID:28564595, PMID:22389409, PMID:25804739,
  PMID:33660341.

## Core biology

- Shrub is the fly Snf7/CHMP4, the core polymerising ESCRT-III subunit
  [PMID:16713958 "shrub encodes an evolutionarily conserved coiled-coil protein homologous to the yeast protein Snf7"].
  Its core forms staggered electrostatic filaments; interface mutants fail to
  polymerise and fail to rescue [PMID:27452459 "Mutations that disrupt interface salt bridges interfere with Shrub polymerization and function."].
  Lgd binds the same surface and regulates assembly
  [PMID:28564595 "Lgd regulates ESCRT activity by controlling access to the Shrub self-assembly surface"].
- MVB biogenesis and receptor down-regulation: ESCRT-III pinches off ILVs
  [PMID:33349255 "which is eventually pinched off as an ILV by the concerted action of ESCRT-III and Vps4"];
  hypomorphic Shrub activity slows ILV formation [PMID:33349255 "This hypomorphic shrub mutant situation causes a slight decrease in the rate of ILV formation"].
  Shrub delivers Notch into MVBs [PMID:22162134 "Shrub promotes the lysosomal degradation of the receptor by mediating its delivery into multivesicular bodies (MVBs)."];
  ESCRT mutants accumulate ubiquitylated cargo and over-signal through Notch and EGFR
  [PMID:19571114 "All ESCRT components are required for trafficking of ubiquitylated proteins and are required to prevent excess Notch and EGFR signaling."].
- Abscission: Shrub is needed to complete abscission of female germline stem cells
  [PMID:25635693 "Here we show that ALIX and the ESCRT-III component Shrub are required for completion of abscission"]
  [PMID:25647097 "We found that Shrub is required for complete abscission, and that levels of Shrub are critical for proper timing of abscission."]
  and of sensory organ precursors, where it is also recruited to neighbouring-cell
  membrane protrusions [PMID:37226981 "In addition, Shrub is recruited to membrane protrusions and is required for SJ integrity"].
- Neurons: shrub mutants have reduced dendrite fields with ectopic branching
  (the name), and Shrub with Myopic is needed for neurite severing during pruning
  [PMID:25676218 "Our data show that a specific ESCRT pruning module, including members of the ESCRT-I and ESCRT-III complexes, but not ESCRT-0 or ESCRT-II, are required for the neurite scission event during pruning."].

## Nuclear envelope (two non-duplicative IBA rows)

- Human ESCRT-III, recruited by CHMP7 via CHMP4B, seals the reforming nuclear envelope
  [PMID:26040712 "ESCRT-III and its regulatory AAA (ATPase associated with diverse cellular activities) ATPase VPS4 are specifically recruited by the ESCRT-III-like protein CHMP7 to sites where the reforming nuclear envelope engulfs spindle microtubules"]
  [PMID:26040713 "The ESCRT-III component charged multivesicular body protein 2A (CHMP2A) is directed to the forming NE through binding to CHMP4B"].
- Fly data: in dividing larval neuroblasts, Shrub-GFP puncta line the reforming daughter
  nuclei in telophase and mark the contacts where lagging acentric fragments fuse into
  the nucleus; Shrub RNAi raises micronucleus formation from acentrics from 17% to 51%
  [PMID:32032426 "Shrub-GFP puncta localized along the periphery of daughter nuclei, presumably mediating fusion of nuclear membrane on daughter nuclei"]
  [PMID:32032426 "RNAi depletion of Shrub also resulted in acentrics forming micronuclei in 51% (n = 37) of divisions imaged (compared with 17% of control divisions)."].
  The authors did not run a sealing assay (GFP-NLS) on Shrub-depleted cells, so the
  fly evidence is localization plus a requirement for nuclear-membrane fusion of
  acentrics, not a direct sealing test.
- Flies have a CHMP7-type paralog, CG5498/BcDNA.GH08385 (FBgn0027565), inside the
  PAINT CHMP7 clade (`shrb-bioinformatics/RESULTS.md`).
- PAINT places both IBDs at the family root, with CHMP4A/B/C among the seeds; shrb is a
  CHMP4 ortholog with no loss on its path. Verdict: ACCEPT both, corroborated by the
  fly neuroblast data.

## Vesicle budding and plasma membrane (two non-duplicative IBA rows)

- Vesicle budding from membrane: ESCRT-III budding and scission of ILVs was
  reconstituted with yeast Snf7, Vps20 and Vps24 [PMID:19234443 "Here we show that three subunits of ESCRT-III, Vps20, Snf7 and Vps24, are sufficient to detach intralumenal vesicles."];
  CHMP4 filaments bend membrane away from the cytoplasm into buds [PMID:18209100 "We demonstrate that hSnf7 proteins form novel membrane-attached filaments that can promote or stabilize negative curvature and outward budding."].
  Fly ILV data above. Verdict: ACCEPT.
- Cytoplasmic side of plasma membrane: the IBD (PTN000509454) is seeded by CHMP4A and
  CHMP4B. In flies Shrub acts on the cytosolic face of the plasma membrane at the
  intercellular bridge during abscission and at the membrane protrusions of
  neighbouring cells. Verdict: ACCEPT.

## FlyBase description

- "shrub (shrb) encodes Shrub encodes Vps32/Snf7, ..." is a duplicated phrase. The
  sentence appears to be adapted from the abstract of PMID:33660341 [PMID:33660341 "Shrub (CG8055) encodes the vps32/snf7 protein, a filament-forming subunit of the ESCRT (endosomal sorting complexes required for transport)-III complex involved in inward membrane budding."].
  Recorded as an editorial (OTHER) defect, not a wrong biological statement.
- "inward membrane budding" (FlyBase) and "outward budding" (PMID:28564595, UniProt)
  describe the same reverse topology from different reference frames (into the
  endosome lumen, away from the cytosol). Not a defect.
- Traced: filament-forming ESCRT-III subunit, MVB biogenesis, cytokinesis, membrane
  signalling. Untraced: membrane repair (no fly experiment found; see queries above).

## Row-level notes

- GO:0070938 contractile ring (IDA, PMID:25635693): the paper shows GFP-Shrub at midbody
  rings (MRs) and midbodies after furrowing, not at the constricting actomyosin ring.
  Midbody is already annotated from the same paper. MARK_AS_OVER_ANNOTATED.
- GO:0036258 obsolete multivesicular body assembly (NAS, ComplexPortal): QuickGO marks
  it obsolete with consider GO:0032509. MODIFY to GO:0032509.
- GO:0000281 mitotic cytokinesis (IMP x2): both papers show abscission defects; MODIFY
  to GO:0061952 midbody abscission (part_of mitotic cytokinesis).
- GO:0046718 symbiont entry into host cell (HMP, PMID:30445201): RNAi screen of
  trafficking genes for baculovirus entry in DL1 cells; abstract-only and does not name
  shrb. UNDECIDED.
- GO:0016322 neuron remodeling (IMP, PMID:25458013): abstract-only and does not name
  shrb, but neuron pruning by Shrub is shown in PMID:25676218. Kept as non-core like the
  sibling row, deferring to the curator.
- GO:0005515 protein binding (IPI, Borealin FBgn0032105, PMID:22724069): bare protein
  binding; REMOVE per policy. The interaction is real and is described in the reason.
