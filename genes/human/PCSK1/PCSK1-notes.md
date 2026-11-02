# PCSK1 (P29120) — curation notes

Deep research: the client failed in this session (`just deep-research-falcon human PCSK1` timed out
after 600 s with "agentapi not found in PATH"), so the literature work below was done manually
from PubMed and the cached `publications/` entries. The provider finished afterwards and
`PCSK1-deep-research-falcon.md` is committed; it was checked against this review on 2026-10-11.

- It agrees on the core annotation: a calcium-dependent subtilisin/kexin-family serine
  endoprotease performing limited proteolysis immediately after a basic residue at paired-basic
  sites, autocatalytically processed during maturation, sorted to dense-core secretory granules
  where it acts at about pH 5-5.5. A dibasic motif alone does not make a protein a substrate.
- It supports the granule-sorting annotation with the Dikeakos NMR work: residues 738-750 form an
  amphipathic helix and a hydrophobic patch centred on Leu745 redirects a constitutively secreted
  reporter to regulated granules. That is a trafficking role of the C-terminal tail, distinct from
  catalysis by the S8 domain.
- It raises a species caveat worth noting against the proinsulin substrate rows. The familiar
  division of labour in which PC2 cuts the other proinsulin junction is largely mouse-based; in
  primary human islets, validated staining found essentially no PC2 in ordinary beta cells, and
  blocking PC2-dependent glucagon formation did not prevent mature insulin formation, while two
  PC1/3 inhibitors did impede proinsulin processing.
- It agrees that proglucagon processing to GLP-1 and GLP-2 in intestinal L cells is PCSK1's, and
  that the same precursor yields glucagon by a PC2-dependent route in alpha cells, so the product
  depends on which convertase the cell expresses.
- It notes PC2 can partly compensate for pro-IAPP processing, and that some authentic circulating
  ACTH remains in human PCSK1 deficiency, so PCSK1 is not invariably the exclusive processor of
  its substrates.

## Enzyme identity

- PC1/3 (neuroendocrine convertase 1, EC 3.4.21.93) is a calcium-dependent subtilisin/kexin-like
  serine endoprotease
  [PMID:27187081 "is a serine endoprotease that is involved in the processing of a variety of
  proneuropeptides and prohormones"] that cleaves at paired basic residues
  [file:human/PCSK1/PCSK1-uniprot.txt "Reaction=Release of protein hormones, neuropeptides and renin
  from their precursors, generally by hydrolysis of -Lys-Arg-|- bonds"].
- Substrate range
  [file:human/PCSK1/PCSK1-uniprot.txt "Substrates include POMC, renin, oxytocin, vasopressin,
  enkephalin, dynorphin, somatostatin, insulin and AGRP"].
- The zymogen's propeptide is removed autocatalytically before the Golgi
  [PMID:8397508 "demonstrated that the onset of the conversions of pro-PC1 into PC1"], after which
  mature enzyme is stored in dense-core granules
  [file:human/PCSK1/PCSK1-uniprot.txt "Cytoplasmic vesicle, secretory vesicle. Note=Localized in the
  secretion granules"], colocalised with its substrate
  [PMID:8916141 "the colocalization of PC1/3 and insulin, and that of PC2 and glucagon, were observed
  in the same secretory granules"]. A fraction is also secreted
  [PMID:8397508 "Secretion of glycosylated and sulphated PC1 (84 kDa) occurs about 30 min after the
  onset of biosynthesis"], which is why the extracellular-region rows were kept but as non-core.

## Pathway position (leptin–melanocortin)

- PC1 cleaves POMC to ACTH and beta-lipotropin, the obligatory step upstream of alpha-MSH, whereas
  PC2 makes the downstream cuts
  [PMID:2023902 "PC1 cleaves POMC into corticotropin and beta-lipotropin"]. This is the step that
  places PCSK1 between POMC and MC4R in the module.
- proAgRP is also a PC1/3 substrate (UniProt, above), so the enzyme matures both the agonist and the
  antagonist arms of melanocortin signalling.
- In human beta cells PC1/3, not PC2, performs proinsulin conversion
  [PMID:32291281 "By demonstrating that healthy human β-cells process proinsulin by PC1/3 but not
  PC2"; PMID:32291281 "suppression of PC1/3 blocked processing of proinsulin but not proglucagon"].

## Human genetics

- The first patient was a compound heterozygote with obesity, abnormal glucose homeostasis,
  hypogonadotropic hypogonadism and hypocortisolism
  [PMID:9207799 "suggestive of a defective prohormone processing by the endopeptidase, prohormone
  convertase 1"], one allele acting by ER retention
  [PMID:9207799 "Gly-->Arg483 prevents processing of proPC1 and leads to its retention in the
  endoplasmic reticulum"].
- The syndrome
  [PMID:27187081 "obesity, malabsorptive diarrhea, hypogonadotropic hypogonadism, altered thyroid and
  adrenal function, and impaired regulation of plasma glucose levels in association with elevated
  circulating proinsulin-to-insulin ratio"], with small-intestinal involvement
  [PMID:14617756 "We postulate that PC1, presumably in the enteroendocrine cells, is essential for the
  normal absorptive function of the human small intestine"].
- Common variants carry polygenic obesity risk, and N221D measurably reduces catalysis
  [PMID:18604207 "Functional analysis showed a significant impairment of the N221D-mutant PC1/3
  protein catalytic activity"].
- Allele-specific, tissue-dependent substrate failure is documented
  [PMID:26786350 "Proinsulin processing was drastically reduced, while processing of
  proopiomelanocortin (POMC) to adrenocorticotropic hormone (ACTH) in pituitary was only mildly
  impaired"], and some alleles retain autoprocessing while failing in trans
  [PMID:34068683 "the p.E345A mutation in PC1/3 resulted in a (near) normal autocatalytic proPC1/3
  processing"].

## Annotation decisions worth recording

- `GO:0043043 peptide biosynthetic process` (IEA and ISS) was retermed to peptide hormone processing:
  the usual sense of that term is translation, whereas PC1/3 makes peptides by limited proteolysis.
- `GO:0016020 membrane` (IBA, is_active_in) was removed: that propagation reflects the
  membrane-anchored members of the subtilisin-like family (furin, bacterial and fungal enzymes), not
  PCSK1, which is soluble in the granule lumen.
- `GO:0042802 identical protein binding` (IEA) was removed: the underlying observation is most likely
  zymogen autoprocessing rather than a homodimerisation function.
- `GO:0007267 cell-cell signaling` (TAS) was removed: the enzyme acts upstream of hormone signalling
  by maturing precursors; the contribution is already recorded as peptide hormone processing and
  hormone biosynthesis.
- `GO:0042446 hormone biosynthetic process` (IDA) was accepted rather than questioned under the
  substrate-vs-participant rule: PC1/3 performs the cleavage that creates the mature hormone, so it
  does the work of that step (contrast the AGT case, where the substrate does none of it).
