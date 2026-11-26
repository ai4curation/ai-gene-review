# ADCY3 notes

## Manual literature summary

Automated Falcon/Perplexity deep research was unavailable for this checkout, so this review uses the cached GOA references, the UniProtKB O60266 record, the PANTHER PTHR45627 PAINT table and the cached Reactome events.

ADCY3 encodes human adenylate cyclase type 3. Yang et al. cloned a full-length human AC3 cDNA from fetal brain, predicted a 1144 amino-acid protein with the twelve transmembrane spans typical of mammalian membrane adenylyl cyclases, and detected ADCY3 transcript in human islets plus brain, heart, kidney, liver, lung, pancreas, placenta and skeletal muscle [PMID:9920776, "full-length cDNA encoding human AC3 from a human fetal brain cDNA library"].

Cote et al. localized ADCY3 protein in the human adrenal gland to both cytoplasm and plasma membrane pools [PMID:11549699, "adenylyl cyclases 3 and 2 in both the cytoplasm and the plasma membrane"]. This supports the existing cytoplasm and plasma-membrane component annotations, but the cytoplasmic fraction is peripheral relative to ADCY3's membrane cyclase activity.

Siljee et al. connected ciliary ADCY3 to hypothalamic GPCR/cAMP signaling. Their paper reports that "ADCY3 is expressed at the primary cilia of neurons", that MC4R colocalizes with ADCY3 at primary cilia in mouse PVN neurons, and that inhibiting adenylyl-cyclase signaling at those primary cilia increases food intake and body weight [PMID:29311635, "inhibition of adenylyl-cyclase signaling at the primary cilia of these neurons increases body weight"]. This supports non-motile cilium membrane as the relevant specific location for the GO-CAM ADCY3 node.

The NK-cell membrane-proteome paper is broad high-throughput support for membrane association rather than ADCY3-specific biology [PMID:19946888, "identified 1843 proteins"].

## Orthology and inferred functions

PANTHER node PTN002899368 places adenylate cyclase activity, cAMP biosynthetic process, adenylate cyclase-activating GPCR signaling and plasma-membrane activity on the eukaryotic membrane adenylyl-cyclase clade. `just paint-losses human ADCY3` reported no IRD or IKR loss on the human ADCY3 lineage.

The GOA cilium, ciliary membrane, sperm, fertilization, acrosome reaction, olfactory and forskolin rows transfer mouse Adcy3 assertions. They agree with UniProt's synthesis that ADCY3 participates in odorant-receptor/Golf signaling, is activated by Gs in primary cilia, and is required for mouse sperm motility, but the sperm and olfactory process contexts are peripheral to the ciliary GPCR-to-cAMP activity reviewed here.

## GO-CAM consistency

The Smoothened/GPR161 GO-CAM models ADCY3 as a non-motile-cilium-membrane adenylyl cyclase involved in adenylate cyclase-activating GPCR signaling. The ADCY3 gene review agrees with that node. The generic Reactome renal water homeostasis, glucagon and endothelial shear-stress rows are over-propagated to ADCY3 but do not create a disagreement with the model.
