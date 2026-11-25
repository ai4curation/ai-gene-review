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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined both GOA rows, the description and core functions from the literature,
PAINT (PTHR11935) and a new sequence analysis. No ProtNLM output was opened or used.

**Identity correction (isoform, not a TM-less product).** New analysis
`Pnkd-bioinformatics/compare_isoforms_rereview.py` → `RESULTS-rereview.md` maps B4F7D2 onto every
reviewed human (Q8N490) and mouse (Q69ZP3) PNKD isoform and the other rat Pnkd TrEMBL products.
- B4F7D2 (369 aa) is identical to the Ensembl model A0A0G2JTS8 (ENSRNOT00000090383, gene
  ENSRNOG00000014806, RGD:2300155): an annotated alternative transcript, cDNA-supported (MGC AAI68228).
- It is collinear with mouse PNKD-L (Q69ZP3-1, 385 aa) over 1-340 (328/340 identical) and human PNKD-L
  over 1-341. The N-terminal region carrying the MTS/disease alanines and the hydrophobic segment
  (~76-95, LAWYSLYTRTWLGYLFYR) is present.
- The earlier note that B4F7D2 "lacks reference residues 80-118 (most of the predicted helical
  transmembrane segment)" was an artefact of using D3ZXB0 as reference: D3ZXB0 (424 aa) is the
  equivalent of mouse isoform 3 (Q69ZP3-3), which has a 39-residue insertion after residue 79. The
  original RESULTS.md is kept unchanged; its reference_review now flags this.
- All seven Zn(2+) ligands of human Q8N490 (H172, H174, D176, H177, H229, D253, H291) are conserved.
- Residues 341-369 are a divergent tail (not a simple frameshift of the PNKD-L C-terminus; the other
  two frames of the CDS also do not give it), replacing the C-terminal half of the HAGH_C helical
  domain: Pfam PF16123 spans 292-329 in B4F7D2 versus 292-380 in mouse/human PNKD-L.
- No reviewed rat PNKD exists; the rat gene-centric product with RGD ISO annotations is D3ZXB0 (22 GOA
  rows on 2026-10-21, QuickGO), which has no review in the repo.

**PAINT reading (PTHR11935-paint.tsv).** GO:0016790 thiolester hydrolase activity is placed at the root
node PTN004322580 (human/mouse PNKD carry the IBA); GO:0004416 is at PTN000232795, which excludes the
PNKD branch (no GO:0004416 IBA on human or mouse PNKD); GO:0006749 is on the HAGH-only node
PTN002631193. Mitochondrion is placed on PTN000940186 (Eumetazoa) seeded by human Q8N490 alone.
Rat B4F7D2 has no IBA rows at all in GOA.

**Row decisions.**
- GO:0004416 → MODIFY to GO:0016790, following the PAINT placement and the biochemistry
  [PMID:21487022 "We show that PNKD-L recognizes the same substrate in this pathway (SLG), but catalyzes
  the same reaction as HAGH at a very low level"].
- GO:0051596 → REMOVE (was UNDECIDED). PNKD-L fails HAGH complementation [PMID:21487022 "further
  supporting the idea that PNKD-L does not use SLG as an in vivo substrate"], and PAINT propagated
  no glyoxalase process term to the PNKD subfamily.

**Not added.** Mitochondrion: the PNKD clade IBD rests on Ghezzi 2009 [PMID:19124534 "both MR-1L and
MR-1S isoforms are mitochondrial proteins"], directly contradicted for PNKD-L by Shen 2011 [PMID:21487022
"no co-localization with mitochondria was found"]; left as a suggested question. Negative regulation of
synaptic vesicle exocytosis (GO:0046929): shown for PNKD-L (PMID:25730884; the co-IP antibody was raised
to the C-terminal peptide that B4F7D2 lacks). Not transferred to this splice product with an altered C-terminus.

**Core function added.** GO:0016790 thiolester hydrolase activity, with the caveat that no activity has
been measured for this isoform and the HAGH_C domain is truncated.

**Relative.** Rule applies: B4F7D2 is an alternative splice product; the canonical rat product D3ZXB0
has no review → next review is genes/rat/Pnkd__D3ZXB0 (same_gene_canonical). Characterised orthologs in
the same PANTHER subfamily (SF116) are mouse Q69ZP3 and human Q8N490; neither has a review in the repo.
Family review interpro/panther/PTHR11935/PTHR11935-review.yaml places Pnkd in SF116, consistent with
UniProt; no disagreement. Module: modules/methylglyoxal_detoxification.yaml covers the HAGH step; PNKD
should not be a part of it.
