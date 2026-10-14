# SHC1 (P29353) curation notes

## Identity and isoforms

- Human SHC1 / ShcA; three major isoforms p46Shc, p52Shc (alternative translation start) and p66Shc (alternative promoter, extra N-terminal CH2). Domain order PTB (PID) - CH1 - SH2. [UniProt:P29353 "Isoform p46Shc and isoform p52Shc, once phosphorylated, couple activated receptor tyrosine kinases to Ras via the recruitment of the GRB2/SOS complex"]
- All GOA rows are on the canonical accession P29353; none are isoform-specific in the GOA file, so no `isoform` fields were added. Isoform differences are handled in review reasons (p46 mitochondrial matrix; p66 oxidative stress).

## Core molecular function: phosphotyrosine adaptor

- PTB domain binds NPXpY: [PMID:7542744 "We demonstrate that the PI domain of Shc binds the LXNPXpY motif that encompasses Y-1148 of the activated EGFR."]
- SH2 domain binds EGFR pY1173/pY992: [PMID:7518560 "Both competition experiments with synthetic phosphopeptides and dephosphorylation protection analysis demonstrated that Y-1173 and Y-992 are major and minor binding sites, respectively, for Shc on the EGFR."]
- INSR and IGF1R NPEY motifs via the N-terminal PTB region: [PMID:7537849 "We conclude that SHC interacts directly with the IR and that phosphorylation of Tyr-960 within the IR juxtamembrane domain is necessary for efficient interaction."]; [PMID:7541045 "We conclude that SHC and IRS-1 interact with the tyrosine-phosphorylated NPEY motif of the IGFIR"]
- Receptor-to-GRB2-SOS bridging (adaptor activity): [PMID:9544989 "In addition, Shc bound to the activated EGF receptor via the PTB domain dominantly interacts with Grb2-Sos complex and plays a major role in the Ras-signaling pathway."]; Y239/240 and Y317 are the GRB2 docking sites [PMID:8939605 "Mutagenesis studies indicate that Y239/240 make an important contribution to the association of Shc with Grb2."]
- Insulin: [PMID:8491186 "The interactions between GRB2 and these two proteins require ligand activation of the insulin receptor and are mediated by the binding of the SH2 domain of GRB2 to phosphotyrosines on both IRS-1 and Shc."]
- Late-phase scaffold switching: PEAK1/SgK269 binds SHC1 PTB via phosphorylated NPXY [PMID:23846654 "SgK269 binds the Shc1 PTB domain through a phosphorylated NPXY site, and brings in Ppp1c serine/threonine phosphatases and other Cluster 3 proteins"]
- GO-CAM: mouse insulin receptor model (gocams index) types Shc1 p52 as GO:0005068 transmembrane receptor protein tyrosine kinase adaptor activity, consistent with the review.

## p66Shc and p46Shc

- p66shc knockout mice: stress resistance and longer life span [PMID:10580504 "p66shc-/- mice have increased resistance to paraquat and a 30% increase in life span"]
- Proposed redox activity [PMID:16051147 "We report here that p66Shc is a redox enzyme that generates mitochondrial ROS (hydrogen peroxide) as signaling molecules for apoptosis."] (contested; left as a suggested question, no NEW annotation).
- p46Shc mitochondrial matrix [PMID:14573619 "Here we demonstrate the specific and selective localization of p46Shc to the mitochondrial matrix."]
- Deep research notes that much apparent mitochondrial p66Shc may be at MAMs [file:human/SHC1/SHC1-deep-research-falcon.md "p66Shc is mainly cytosolic/ER/MAM-associated, with a smaller or condition-dependent mitochondrial pool"].

## Protein-binding (GO:0005515) policy applied

82 IPI rows, grouped by partner and paper:

- Phosphotyrosine recognition shown in the cited paper (EGFR site mapping, ErbB SH2/PTB microarray, INSR NPEY, JAK2, CEACAM1 pY488, APP pY682, PEAK1, MET/KIT/GAB1/AR FP interactome, ALK MaMTH, EGFR phosphopeptide pulldown) -> MODIFY to GO:0001784.
- Receptor-SHC1-GRB2(-SOS) bridging shown (insulin/GRB2, Y239/240 mutagenesis, PTB-bound SHC1 with GRB2-SOS, p66 knockdown reducing EGFR-GRB2 association) -> MODIFY to GO:0005068.
- GRB2 SH2 structural/biophysical studies with SHC1-derived peptides: the binding activity is GRB2's; SHC1 only supplies the motif -> REMOVE.
- High-throughput AP-MS / Y2H / proximity / complex co-IP without a defined SHC1 activity (CALCOCO2, CBLC, SMAD4, CFTR, NS1, PTPN12, GAB2, CPNE3, ESR1, many GRB2/EGFR rows) -> REMOVE; removal does not assert the interaction is false.
- EGFR crystal structure with primed Shc1 peptide (PMID:26551075): SHC1 is the kinase substrate -> REMOVE.

## Other judgement calls

- GO:0048408 epidermal growth factor binding (IEA from mouse): mouse source is IPI with mouse Egfr as WITH/FROM, so the intended claim is receptor binding -> MODIFY to GO:0005154.
- GO:0042742 defense response to bacterium (IMP, Tarp paper): full text shows SHC1 is not needed for bacterial propagation and is exploited for host-cell survival [PMID:20624904 "SHC1 is recruited immediately after infection, where it is not directly needed for adhesion, invasion, inclusion formation, or bacterial propagation"] -> MARK_AS_OVER_ANNOTATED (not REMOVE, deferring to curator on an experimental row).
- Transcription regulation IMP rows (same paper): indirect transcriptome effects -> MARK_AS_OVER_ANNOTATED.
- PMID:19593445 (known batch miscitation) is not cited in the SHC1 GOA set.
