# Pnkd (rat, UniProt B4F7D2): review notes

## Identity of the benchmark accession (re-review 2026-10-20)

B4F7D2 (369 aa, TrEMBL, "Pnkd protein") is translated from the MGC spleen cDNA BC168228
and is identical to an Ensembl model (A0A0G2JTS8, 369 aa). Its relationship to the gene
is set out in [Pnkd-bioinformatics/RESULTS.md](Pnkd-bioinformatics/RESULTS.md), which
re-derives everything from UniProt, ENA and NCBI records:

- **Residues 1-328 are identical to rat PNKD isoform 1** (RefSeq NP_001128222.1, 385 aa),
  the ortholog of human PNKD-L (Q8N490-1) and mouse Pnkd isoform 1 (Q69ZP3-1).
  Full-length alignment to mouse Q69ZP3 gives 336/369 identical residues with a single
  ungapped block over 1-340.
- **Residues 329-369 are intron-encoded.** At the nucleotide level BC168228 matches the
  RefSeq CDS for 984 nt (328 codons), exactly to the end of the exon at
  JAXUCZ010000009.1:83384077-83384192, and then reads on into the intron (the divergent
  cDNA begins `GTGAGG...` directly after the exon's last base). The 41-residue G/P-rich
  tail (`VRPGGWEGRGGKPGPHPASTYHCPARACKLFLELWPLTAGV`) therefore replaces the conserved
  57-residue C-terminus of isoform 1 (`CPSTLGEERAYNPF...LKDMHKSK`). B4F7D2 is best
  treated as a **retained-intron (likely aberrant or NMD-prone) transcript product**,
  not a distinct conserved isoform; no protein-level evidence for it exists.
- All seven Zn(2+) ligands of the metallo-beta-lactamase site (mouse H172, H174, D176,
  H177, H229, D253, H291; by similarity to HAGH) are retained at the same positions.
  The lost C-terminal segment lies in the region corresponding to the HAGH C-terminal
  (substrate-lid) domain, so substrate binding of this product cannot be assumed.
- **Correction of the previous review.** The earlier notes compared B4F7D2 only with rat
  D3ZXB0 (424 aa) and concluded that B4F7D2 "lacks residues 80-118, most of the
  predicted transmembrane segment". That is backwards: D3ZXB0 is the rat counterpart of
  mouse isoform 3 (Q69ZP3-3, 424 aa), which carries an extra 39-residue exon after
  residue 79 (`AIGFPCGILFFVLTKQEVDKDRLKQMKARQNMRVSNTGE`). B4F7D2 has the canonical
  isoform-1 (PNKD-L) N-terminal and catalytic-domain structure; it lacks nothing there.

## Evolutionary placement

- PANTHER: PTHR11935 (BETA LACTAMASE DOMAIN) subfamily PTHR11935:SF116 (HYDROLASE
  PNKD-RELATED), the same subfamily as human PNKD Q8N490 and mouse Pnkd Q69ZP3. HAGH
  (glyoxalase II) sits in a different subfamily of the same family.
- PAINT (interpro/panther/PTHR11935/PTHR11935-paint.tsv):
  - `GO:0004416` hydroxyacylglutathione hydrolase activity is placed at PTN000232795
    (Eukaryota node, HAGH-type seeds). Human and mouse PNKD do **not** receive this IBA
    (QuickGO, 2026-10-20), so the PAINT curator placed PNKD outside the clade that
    inherited glyoxalase II activity. That omission is a deliberate decision.
  - `GO:0016790` thiolester hydrolase activity is placed at the deeper node
    PTN004322580 and is propagated by IBA to human and mouse PNKD.
  - `GO:0005739` mitochondrion is placed at PTN000940186 (Eumetazoa) seeded by human
    PNKD; the HAGH-specific node PTN002631193 carries `GO:0006749` glutathione metabolic
    process, which PNKD does not inherit.
- The closest experimentally characterised relative is **mouse Pnkd (Q69ZP3)**, a
  one-to-one ortholog in SF116 with knockout, synaptic and biochemical data; human PNKD
  (Q8N490) carries the enzyme assay. Neither has a review in this repo.

## Biological evidence (gene level, from orthologs)

- Enzyme: human PNKD-L hydrolyses S-D-lactoylglutathione only at a very low rate and does
  not rescue SLG metabolism in HAGH-null flies [PMID:21487022 "PNKD-L has extremely low
  but consistent SLG hydrolysis activity"; "introduction of a human PNKD-L transgene into
  the same null background shows no rescue of SLG metabolism"]. The abstract states it
  "shares highest homology with glyoxalase II but does not catalyze the same reaction".
  The physiological substrate is unknown.
- Glutathione: Pnkd-knockout mouse cortex has ~20% lower GSH [PMID:21487022 "In our
  Pnkd-deficient mice, GSH levels were ∼20% lower in the cortex, suggesting impaired
  redox regulation"]. This is a downstream phenotype, not evidence for a catalytic step
  in methylglyoxal catabolism.
- Localization: human PNKD-L is membrane-associated in neuronal-like cells
  [PMID:21487022 "the results suggest that PNKD-L is a membrane-associated protein."];
  mitochondrial localization was reported in Cos7 cells and is the PAINT CC placement.
- Synapse: PNKD interacts with RIM1/RIM2, localizes to synapses and suppresses
  neurotransmitter release; knockout mice have reduced RIM levels [PMID:25730884 "PNKD
  interacts with synaptic active zone proteins Rab3-interacting molecule (RIM)1 and RIM2,
  localizes to synapses, and modulates neurotransmitter release."]. The Pnkd-L
  immunoprecipitation used an antibody against a C-terminal peptide, the region that
  B4F7D2 replaces with intronic sequence.

## Annotation decisions

- `GO:0004416` (IEA, InterPro2GO IPR017782): **MODIFY** to `GO:0016790` thiolester
  hydrolase activity. The InterPro entry is a glyoxalase-II family signature that cannot
  separate the PNKD subfamily from HAGH; PAINT excluded PNKD from the glyoxalase II node
  but propagated the parent thiolester hydrolase activity, and the only measured activity
  (very low SLG turnover) is consistent with a thioesterase of unknown substrate.
- `GO:0051596` methylglyoxal catabolic process (IEA, InterPro2GO): **REMOVE**. PNKD does
  not perform the glyoxalase II step (no complementation; "does not catalyze the same
  reaction"), and PAINT did not propagate the HAGH pathway term to PNKD.

## Deep research

Pnkd-deep-research-falcon.md (present) agrees: no physiological substrate, not an
established glyoxalase II, and synaptic membrane association for PNKD-L. Its
isoform statements predate the intron-retention finding above.

## Open questions

- Is the BC168228 retained-intron transcript translated in vivo, or degraded by NMD?
- What is the physiological thioester substrate of PNKD-L?
