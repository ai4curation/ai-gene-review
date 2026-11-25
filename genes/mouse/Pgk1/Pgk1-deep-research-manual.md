# Pgk1 manual deep research notes

`just deep-research-perplexity mouse Pgk1 --fallback perplexity-lite` failed because the active
`deep-research-client` install exposed only the `claude_code` provider. To avoid spawning another
agent while Rosalind is CPU-limited, this file records the manual evidence pass for the review.

Mouse Pgk1 encodes the X-linked somatic phosphoglycerate kinase 1 isozyme. Older mouse genetics
papers mapped the X-linked PGK-1 enzyme by electrophoretic variation and somatic cell genetics
[PMID:17248765, PMID:4817529, PMID:943046], and Crisp and Pogson directly measured recovery of
phosphoglycerate kinase activity in mouse liver parenchymal-cell preparations [PMID:4262895].
The UniProt record for P09411 records the conserved reversible EC 2.7.2.3 reaction,
`3-phosphoglycerate + ATP = 1,3-bisphosphoglycerate + ADP`, with both glycolytic and
gluconeogenic physiological directions by homology to human PGK1.

The PTHR11406 family review scopes phosphoglycerate kinase activity, cytosol, glycolysis, ATP
binding and ADP binding to the root PGK node. It treats the root gluconeogenesis placement as
sound for PGK1-like cytosolic PGKs, while noting that PAINT should prune it from the testis PGK2
branch. Mouse Pgk1 is the animal PGK1 subfamily member PTHR11406:SF14, so the GO-CAM
gluconeogenesis placement agrees with the family review.

The GOA row citing PMID:30174313 comes from the Lncenc1 mouse ESC paper. The paper perturbed
Lncenc1, not Pgk1; it nevertheless measured lower glycolytic-gene expression and lower glycolytic
flux when Lncenc1 was depleted, which is enough to keep the glycolysis biology while replacing the
obsolete `GO:0061621 canonical glycolysis` term with live `GO:0006096 glycolytic process`.
PMID:19643083 perturbed hepatocyte Hif1a and observed impaired hepatic gluconeogenesis with lower
PGK-1 and PEPCK expression; the paper is expression/regulator evidence, but the Pgk1 product
itself catalyzes the reversible PGK step used in gluconeogenesis.

Human PGK1 has two conserved moonlighting functions that are transferred to mouse Pgk1 in GOA.
Lay et al. identified secreted phosphoglycerate kinase from fibrosarcoma conditioned medium as a
plasmin disulfide reductase that promotes angiostatin release and inhibits tumor angiogenesis
[PMID:11130727]. Li et al. showed that hypoxia or oncogenic signaling induces mitochondrial PGK1
translocation, where PGK1 phosphorylates PDHK1 at Thr338 and inhibits mitochondrial pyruvate
utilization [PMID:26942675]. These are context-specific and non-core relative to cytosolic PGK
activity. Qian et al. subsequently showed that PGK1 phosphorylates Beclin1 Ser30 during
glutamine deprivation- and hypoxia-induced autophagy [PMID:28238651], so the RHEA-based
`protein serine kinase activity` rows are probably true; the defect is narrower, on the human
UniProt serine-kinase catalytic-activity line that cites the PDHK1 Thr338 paper rather than the
Beclin1 Ser30 paper.

The remaining human-derived context rows are weaker. Buhrke et al. found PGK1 in a proteomic
comparison of proliferating and differentiated Caco-2 cells, which is correlative expression
evidence and over-annotates PGK1 to epithelial cell differentiation [PMID:21492153]. Fork et al.
detected human PGK1 in a SILAC membrane-raft fraction from endothelial cells [PMID:25204797];
this does not establish a mouse membrane-raft function. Zhang et al. recovered human PGK1 in a
kinase-trapping mass spectrometry experiment with dephosphorylated human KCC3 [PMID:27782176],
which is at most a non-core transporter-binding observation.

PMID:33274589 is a yeast Ykt6/Atg1 autophagy paper. Its Pgk1 experiments use the yeast Pgk1-GFP
bulk autophagy marker and anti-Pgk1 immunoblots in yeast `ykt6ts` strains; it is the wrong
reference for a mouse Pgk1 cytosol IDA row. PMID:28209736 is a Pejvakin hair-cell paper and did
not mention phosphoglycerate kinase or PGK1 in the cached text; it is also a wrong reference for
mouse Pgk1 cytoplasm.
