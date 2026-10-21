# Pnkd (B4F7D2): evidence and exact-input prediction review

The emitted HAGH reaction is an over-specific transfer across a functionally divergent family. PNKD-L shows very weak lactoylglutathione hydrolysis in vitro and fails to replace HAGH in vivo. B4F7D2 also differs from the longer PNKD product, so neither a standard glyoxalase II role nor the localization and synaptic function of a particular long isoform can be assumed.

## Input identity and functional boundary

B4F7D2 and the 424-residue rat D3ZXB0 record share RGD:2300155. Their first 79 residues are identical, but B4F7D2 lacks the next 39 reference residues and has a divergent C-terminal portion. The entire annotated metallo-beta-lactamase domain is conserved (163/163 identical residues). This establishes PNKD identity without equating the product to the experimentally studied PNKD-L or PNKD-M constructs. The model donor O35952 is rat Hagh, a different gene.

## Biological evidence

- [PMID:21487022 — Mutations in PNKD causing paroxysmal dyskinesia alters protein cleavage and stability.](https://pubmed.ncbi.nlm.nih.gov/21487022/): Human PNKD-L has weak measurable S-D-lactoylglutathione hydrolysis in vitro, rather than the robust HAGH activity; no complete absence of hydrolysis is claimed.

> PNKD-L has extremely low but consistent SLG hydrolysis activity


> introduction of a human PNKD-L transgene into the same null background shows no rescue of SLG metabolism


> the results suggest that PNKD-L is a membrane-associated protein.

## Exact non-GO claims

The complete emitted record is preserved in [Pnkd-protnlm-source.json](Pnkd-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Metallo-beta-lactamase domain-containing protein

CNN (CS 2). The name describes a verified domain present in B4F7D2; it does not itself claim beta-lactam antibiotic hydrolysis or glyoxalase-II substrate specificity. The full mapped domain is retained. [Sequence comparison](Pnkd-bioinformatics/RESULTS.md).

### Function

> Thiolesterase that catalyzes the hydrolysis of S-D-lactoyl-glutathione to form glutathione and D-lactic acid

PLI (CS 0; PARALOG_OVERANNOTATION) as a physiological enzyme-function assignment copied from Hagh/O35952. The direct comparison shows weak PNKD-L activity in vitro and failure to replace HAGH, so the HAGH reaction is not an established biological function of PNKD. This assessment does not mean that the bond can never be hydrolyzed by PNKD, and biochemical activity of B4F7D2 itself remains unmeasured. [PMID:21487022](https://pubmed.ncbi.nlm.nih.gov/21487022/).

### Location

> Mitochondrion matrix

UNC (CS 1). A HAGH mitochondrial localization cannot establish PNKD localization. Conversely, membrane localization of a particular human PNKD-L construct cannot categorically refute mitochondrial localization of every rat product. B4F7D2 retains the common N-terminus but has internal and terminal differences; no assay resolves its localization. The paper explicitly discusses conflicting mitochondrial localization results and isoform-specific evidence. [PMID:21487022](https://pubmed.ncbi.nlm.nih.gov/21487022/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

The PNKD/HAGH relationship supports fold ancestry but not a shared physiological substrate. The failed HAGH complementation is a direct functional boundary. The selected protein retains the annotated beta-lactamase domain, so it is not classified as a catalytically dead fragment simply from its shorter length. No ancestral gain/loss node or stable pseudoenzyme status is asserted.

## Evidence limits

The cached 2011 paper contains full text, including the low-activity and complementation results and the conflicting localization literature. Its experiments concern defined PNKD-L constructs, not B4F7D2. A biochemical substrate or synaptic core function is therefore not assigned to this exact product. The genuine Falcon report supplies source leads; its gene-level neuronal synthesis is subject to the product and isoform boundary above.

Exact sequence mapping: [Pnkd-bioinformatics/RESULTS.md](Pnkd-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Neuronal evidence and product scope

[PMID:25730884](https://pubmed.ncbi.nlm.nih.gov/25730884/), DOI [10.1073/pnas.1501364112](https://doi.org/10.1073/pnas.1501364112), reports PNKD-RIM1/2 interactions and altered release in neuronal experiments and knockout mice. It supports the gene-level neuronal context, but no experiment in the paper is identified as testing the 369-residue B4F7D2 product. The conserved beta-lactamase domain alone does not establish its synaptic localization or RIM regulation.

## Re-review 2026-10-04

**GOA changes.** None: the refreshed GOA carries the same two InterPro2GO (IPR017782) IEA rows, GO:0004416 hydroxyacylglutathione hydrolase activity and GO:0051596 methylglyoxal catabolic process. No new or retired rows.

**Row audit.** Actions unchanged.
- GO:0004416 stays `MARK_AS_OVER_ANNOTATED`: the overshoot is a physiological glyoxalase-II assignment from domain homology. Human PNKD-L hydrolyses S-D-lactoylglutathione only weakly [PMID:21487022 "PNKD-L has extremely low but consistent SLG hydrolysis activity"] and fails HAGH complementation [PMID:21487022 "introduction of a human PNKD-L transgene into the same null background shows no rescue of SLG metabolism"]. Added the Falcon statement that PNKD "must not be annotated as an established hydroxyacylglutathione hydrolase solely from domain homology".
- GO:0051596 stays `UNDECIDED`; added the Falcon statement that PNKD "is not established as a canonical methylglyoxal-detoxifying glyoxalase II".

**core_functions left empty (decision).** No molecular function is established for PNKD: the physiological substrate of the MBL-fold domain is unknown and the only measured hydrolysis is weak. The best-supported gene-level role, RIM1/RIM2 interaction and suppression of synaptic vesicle exocytosis [PMID:25730884 "PNKD interacts with synaptic active zone proteins Rab3-interacting molecule (RIM)1 and RIM2, localizes to synapses, and modulates neurotransmitter release"], was shown with defined neuronal PNKD isoforms. This product (B4F7D2, 369 aa) lacks reference residues 80-118 (most of the predicted helical transmembrane segment, 6/19 mapped) and has a divergent C-terminus (Pnkd-bioinformatics/RESULTS.md). Transferring that role to it would be an inference about an isoform nobody has assayed, so the "No core functions defined" warning is left.

**Open question.** Is B4F7D2 an expressed isoform, and does it keep RIM binding without the membrane anchor?

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### Identity of the benchmark accession (re-review 2026-10-20)

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

### Evolutionary placement

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

### Biological evidence (gene level, from orthologs)

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

### Annotation decisions

- `GO:0004416` (IEA, InterPro2GO IPR017782): **MODIFY** to `GO:0016790` thiolester
  hydrolase activity. The InterPro entry is a glyoxalase-II family signature that cannot
  separate the PNKD subfamily from HAGH; PAINT excluded PNKD from the glyoxalase II node
  but propagated the parent thiolester hydrolase activity, and the only measured activity
  (very low SLG turnover) is consistent with a thioesterase of unknown substrate.
- `GO:0051596` methylglyoxal catabolic process (IEA, InterPro2GO): **REMOVE**. PNKD does
  not perform the glyoxalase II step (no complementation; "does not catalyze the same
  reaction"), and PAINT did not propagate the HAGH pathway term to PNKD.

### Deep research

Pnkd-deep-research-falcon.md (present) agrees: no physiological substrate, not an
established glyoxalase II, and synaptic membrane association for PNKD-L. Its
isoform statements predate the intron-retention finding above.

### Open questions

- Is the BC168228 retained-intron transcript translated in vivo, or degraded by NMD?
- What is the physiological thioester substrate of PNKD-L?
