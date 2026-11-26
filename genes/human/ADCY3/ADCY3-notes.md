# ADCY3 notes

## Manual literature summary

Automated Falcon/Perplexity deep research was unavailable for this checkout, so this review uses the cached GOA references, the UniProtKB O60266 record, the PANTHER PTHR45627 PAINT table and the cached Reactome events.

ADCY3 encodes human adenylate cyclase type 3. Yang et al. cloned a full-length human AC3 cDNA from fetal brain, predicted a 1144 amino-acid protein with the twelve transmembrane spans typical of mammalian membrane adenylyl cyclases, and detected ADCY3 transcript in human islets plus brain, heart, kidney, liver, lung, pancreas, placenta and skeletal muscle [PMID:9920776, "full-length cDNA encoding human AC3 from a human fetal brain cDNA library"].

Cote et al. localized ADCY3 protein in the human adrenal gland to both cytoplasm and plasma membrane pools [PMID:11549699, "adenylyl cyclases 3 and 2 in both the cytoplasm and the plasma membrane"]. This supports the existing cytoplasm and plasma-membrane component annotations, but the cytoplasmic fraction is peripheral relative to ADCY3's membrane cyclase activity.

Siljee et al. connected ciliary ADCY3 to hypothalamic GPCR/cAMP signaling. Their paper reports that "ADCY3 is expressed at the primary cilia of neurons", that MC4R colocalizes with ADCY3 at primary cilia in mouse PVN neurons, and that inhibiting adenylyl-cyclase signaling at those primary cilia increases food intake and body weight [PMID:29311635, "inhibition of adenylyl-cyclase signaling at the primary cilia of these neurons increases body weight"]. Saeed et al. and Grarup et al. independently connected human ADCY3 loss-of-function alleles to severe obesity or increased risk of obesity and type 2 diabetes [PMID:29311637, "homozygous mutations in the ADCY3 gene encoding adenylate cyclase 3 in children with severe obesity"; PMID:29311636, "carriers have decreased ADCY3 RNA expression"]. Together these support non-motile cilium membrane as the relevant specific location for ciliary GPCR/ADCY3 GO-CAM nodes.

Livera et al. provide the primary mouse evidence behind the transferred fertilization, sperm motility and acrosome-reaction rows: AC3 protein was detected in the developing acrosome and in mature spermatozoa, and Adcy3-null spermatozoa had decreased motility, increased spontaneous acrosome reactions and impaired zona-dependent fertilization [PMID:15705663, "these spermatozoa had decreased motility and showed an increase in spontaneous acrosome reactions"]. The cached abstract does not establish a sperm flagellar membrane pool, so the ciliary-membrane rows were refined specifically to the primary/non-motile cilium membrane rather than treated as covering all sperm functions.

The NK-cell membrane-proteome paper is broad high-throughput support for membrane association rather than ADCY3-specific biology [PMID:19946888, "identified 1843 proteins"].

## Orthology and inferred functions

PANTHER node PTN002899368 places adenylate cyclase activity, cAMP biosynthetic process, adenylate cyclase-activating GPCR signaling and plasma-membrane activity on the eukaryotic membrane adenylyl-cyclase clade. `just paint-losses human ADCY3` reported no IRD or IKR loss on the human ADCY3 lineage.

The GOA cilium, ciliary membrane, sperm, fertilization, acrosome reaction, olfactory and forskolin rows transfer mouse or rat ADCY3 assertions. They agree with UniProt's synthesis that ADCY3 participates in odorant-receptor/Golf signaling, is activated by Gs in primary cilia, and is required for mouse sperm motility, but the sperm and olfactory process contexts are peripheral to the ciliary GPCR-to-cAMP activity reviewed here. The two Golgi rows rest on rat AC3 (`UniProtKB:P21932`) or a UniProt SubCell mapping derived from the same rat-supported location; without positive evidence for a stable human Golgi pool, the root Golgi rows were marked over-annotated.

## GO-CAM consistency

The Smoothened/GPR161 GO-CAM models ADCY3 as a non-motile-cilium-membrane adenylyl cyclase involved in adenylate cyclase-activating GPCR signaling. The ADCY3 gene review agrees with that node. `gocams/index.tsv` also lists ADCY3 in four 6690711d TAAR/OR5AN1 human olfactory models, several 69d8496c/69ea8949 human olfactory receptor models, the 689e7a5d MC4R food-intake series, the 6918f237 GPR45 food-intake model, and additional 693b3c09/696022cd SMO-GPR161 models. The generic Reactome renal water homeostasis, glucagon and endothelial shear-stress rows are over-propagated to ADCY3 but do not create a disagreement with the target 696022cd00001523 model.
