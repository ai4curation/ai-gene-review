# MKKS / BBS6 (Q9NPJ1) review notes

## Identity & family
- HGNC:7108, MKKS, synonym BBS6. UniProt Q9NPJ1, 570 aa, chromosome 20.
- Divergent member of the **TCP-1 / group II (type II) chaperonin (CCT/TRiC) family** [UniProt SIMILARITY: "Belongs to the TCP-1 chaperonin family"]. InterPro IPR002423 (Cpn60/GroEL/TCP-1), IPR028790 (MKKS); Pfam PF00118.
- UniProt RecName is "Molecular chaperone MKKS"; original gene paper calls it a "putative chaperonin" [PMID:10802661 "Mutation of a gene encoding a putative chaperonin causes McKusick-Kaufman syndrome"].

## Core molecular/cellular function
- MKKS, together with **BBS10 and BBS12** and the **CCT/TRiC chaperonin**, forms the **"BBS-chaperonin complex"** that mediates **BBSome assembly** [PMID:20080638 "a novel complex composed of three chaperonin-like BBS proteins (BBS6, BBS10, and BBS12) and CCT/TRiC family chaperonins mediates BBSome assembly... Chaperonin-like BBS proteins interact with a subset of BBSome subunits and promote their association with CCT chaperonins"].
- It acts as an **assembly factor / chaperone, not a stable structural subunit of the mature BBSome**. The BBSome itself comprises BBS1,2,4,5,7,8,9 [PMID:22500027 "Seven of the BBS proteins (BBS1, 2, 4, 5, 7, 8, and 9) have been shown to form a complex known as the BBSome"]. MKKS/BBS6, BBS10, BBS12 form a separate **BBS-chaperonin complex** with CCT/TRiC and BBS7 that is **required for BBSome assembly** [PMID:22500027 "Three additional BBS genes (BBS6, BBS10, and BBS12) have homology to type II chaperonins and interact with CCT/TRiC proteins and BBS7 to form a complex termed the BBS-chaperonin complex. This complex is required for BBSome assembly"].
- Mechanistically the chaperonin complex stabilizes BBS7 and nucleates the BBS7-BBS2-BBS9 "BBSome core" [PMID:22500027 "the BBS-chaperonin complex plays a role in BBS7 stability. BBS7 interacts with BBS2 and becomes part of a BBS7-BBS2-BBS9 assembly intermediate referred to as the BBSome core complex"].
- UniProt FUNCTION: "Probable molecular chaperone that assists the folding of proteins upon ATP hydrolysis... Plays a role in the assembly of BBSome... May play a role in cytokinesis" [ECO:0000269|PubMed:20080638, PubMed:28753627]. ATP binding is **inferred from the chaperonin fold** (IEA, InterPro IPR002423; UniProt FT BINDING 192..199 ATP, ECO:0000255). No experimental ATPase assay specific to MKKS in the cached literature.

## Localization
- Centrosome / pericentriolar material (PCM); shuttles rapidly between cytosol and centrosome [UniProt SUBCELLULAR LOCATION: "Cytoplasm, cytoskeleton, microtubule organizing center, centrosome... The majority of the protein resides within the pericentriolar material... highly mobile and rapidly shuttles between the cytosol and centrosome"]. Original characterization: "MKKS/BBS6... is a novel centrosomal component required for cytokinesis" [PMID:15731008, J Cell Sci].
- HPA IDA: centrosome (GO:0005813) and ciliary basal body (GO:0036064) [GOA, GO_REF:0000052].
- Actively transported between cytoplasm and nucleus; the McKusick-Kaufman allele (H84Y;A242S) is defective in this transport [PMID:28753627 "BBS6 is actively transported between the cytoplasm and nucleus, and that BBS6H84Y; A242S, is defective in this transport"]. IDA nucleus + cytoplasm from this paper.

## Nuclear / transcription-related role (SMARCC1)
- BBS6 interacts with the SWI/SNF chromatin-remodeling protein SMARCC1 (Smarcc1a in zebrafish), predominantly in cytoplasm, and modulates SMARCC1 subcellular localization; this underlies congenital heart defects in McKusick-Kaufman syndrome [PMID:28753627 "we find interaction with the SWI/SNF chromatin remodeling protein Smarcc1a (SMARCC1 in humans)... BBS6 modulates the sub-cellular localization of SMARCC1"]. GOA IPI: SMARCC1 (Q92922).
- GO:0061629 (RNA Pol II transcription factor binding) IPI to RFX-related TF Q99496 (RFX1) from PMID:22302990 (BBS proteins in transcriptional regulation). That paper's abstract foregrounds BBS7 nuclear role but states "our data supports a similar role for other BBS proteins"; full text not cached. Curator (MGI) made the IPI assignment.

## Interactions (GOA IPI partners)
- BBS12 (Q6ZW61): repeatedly captured (PMID:20080638, 22500027, 26900326, 28514442, 33961781); disease mutations reduce BBS12 interaction [UniProt VARIANT notes]. Core to BBS-chaperonin complex.
- BBS2 (Q9BXC9): via coiled-coil [PMID:20080638; UniProt SUBUNIT].
- SMARCC1 (Q92922): PMID:28753627 (see above).
- CCDC28B / MGC1203 (Q9BUN5): pericentriolar epistatic modifier of BBS [PMID:16327777 "MGC1203 encodes a pericentriolar protein that interacts and colocalizes with the BBS proteins"].
- DLEC1 (Q9Y238): mouse spermatogenesis study; Dlec1 interacts with Mkks [PMID:33144677].
- CEP290 (O15078): MKKS directly interacts with CEP290; BBS mutations disrupt it [PMID:22446187 "the domain deleted in the protein encoded by the Cep290rd16 allele directly interacts with another ciliopathy protein, MKKS"].
- PCM1 (Q9NRI5): centrosomal recruitment context [PMID:18762586] — note: this paper is primarily about DISC1/BBS4/PCM1; MKKS IPI to PCM1 assigned by SYSCILIA_CCNET.
- CDR2 (Q01850), ZBED1 (O96006): high-throughput binary interactome (PMID:32296183, IntAct). Low biological specificity.

## Disease
- McKusick-Kaufman syndrome (MKKS, MIM 236700): hydrometrocolpos, postaxial polydactyly, congenital heart defects [PMID:10802661, PMID:28753627].
- Bardet-Biedl syndrome 6 (BBS6, MIM 605231): retinopathy, obesity, polydactyly, hypogenitalism, renal malformation, intellectual disability; oligogenic/triallelic inheritance.

## GO term notes (verified via QuickGO 2026-06)
- **GO:0051082 "unfolded protein binding" is OBSOLETE** (replaced by activity terms). UniProt DR still lists it (TAS:ProtInc) but it is not in the GOA TSV given to us. Better MF term for MKKS chaperone activity: **GO:0044183 "protein folding chaperone"** (def: "Binding to a protein or a protein-containing complex to assist the protein folding process") or, if ATP-driven, GO:0140662 "ATP-dependent protein folding chaperone". Since MKKS folding/ATPase activity is only inferred (no direct assay), protein folding chaperone is the most defensible MF if proposing one.
- GO:0051131 "chaperone-mediated protein complex assembly" — directly matches the experimentally supported BBSome-assembly role. This is the BEST BP term for MKKS's core function.
- GO:1902636 "kinociliary basal body" = a ciliary basal body that is part of a kinocilium (verified). Over-specific transfer from zebrafish ortholog; GO:0036064 ciliary basal body is the better-supported (HPA IDA) localization.

## Evidence-quality flags
- Many BP terms are **ISS transferred from mouse Mkks (Q9JI70) or zebrafish (Q7ZVV0)** under GO_REF:0000024 (BHF-UCL, 2008): melanosome transport, pigment granule aggregation, social behavior, smell, sound detection, several brain-region developments, heart looping, L/R asymmetry, convergent extension, spermatid development, photoreceptor maintenance, fat cell differentiation, appetite/leptin. These reflect pleiotropic ciliopathy phenotypes of orthologs, not MKKS's direct molecular activity — appropriate to keep as NON-CORE where biologically plausible (cilia-dependent phenotypes) but several are quite indirect.
- IEA from mouse ortholog (GO_REF:0000107, Ensembl): motile cilium, basal body, appetite/leptin, fat cell differentiation, cilium beat frequency, kinociliary basal body.
- The leptin/appetite (GO:0038108), fat cell differentiation (GO:0045444), and cilium-beat-frequency (GO:0060296) terms are downstream physiological consequences in mouse, not direct molecular function — over-annotations at the human level.

## Summary judgment
- CORE: chaperone-mediated protein complex assembly (BBSome assembly) [GO:0051131]; centrosome/PCM + ciliary basal body localization; protein folding chaperone MF (inferred).
- SUPPORTING/NON-CORE: cilium assembly (via BBSome), nuclear-cytoplasmic shuttling / SMARCC1-mediated modulation, cytokinesis.
- OVER-ANNOTATION risk: the many ortholog-transferred ISS developmental/behavioral/physiology terms; high-throughput "protein binding" hits; obsolete unfolded protein binding.
