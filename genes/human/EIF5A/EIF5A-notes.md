# EIF5A research notes

UniProt P63241 (IF5A1_HUMAN), 154 aa. HGNC:3300. eIF-5A-1, "eIF-4D", Rev-binding factor.

## Core function
Despite the legacy name "initiation factor," eIF5A is a **translation elongation/termination factor**.
- UniProt FUNCTION: "Translation factor that promotes translation elongation and termination, particularly upon ribosome stalling at specific amino acid sequence contexts [PMID:33547280]. Binds between the exit (E) and peptidyl (P) site of the ribosome and promotes rescue of stalled ribosome: specifically required for efficient translation of polyproline-containing peptides as well as other motifs that stall the ribosome."
- Acts as a ribosome quality control (RQC) cofactor joining the RQC complex to facilitate peptidyl transfer during CAT-tailing.
- The hypusine modification at Lys-50 is unique to eIF5A proteins and is essential for function [PMID:27306458, PMID:3095320; UniProt PTM]. "eIF-5As are the only known proteins to undergo this modification, which is essential for their function."
- Binds 80S ribosomes; mutually exclusive binding with eEF2 [PMID:27115996 ribosome-binding].

## Subcellular location
Cytoplasm + Nucleus + ER membrane (peripheral, cytoplasmic side). Hypusination promotes nuclear export / cytoplasmic localization; nuclear export mediated by XPO4 (exportin 4) with RanGTP [PMID:10944119, PMID:27306458]. Also detected at nuclear pore (IDA PMID:10381392) and annulate lamellae (IDA PMID:12210765) — consistent with XPO4/Ran nuclear-export shuttling.

## Moonlighting / pleiotropic roles (mostly downstream consequences of its translation role)
- Autophagy: required for ATG3 translation (Asp-Asp-Gly motif), facilitating LC3B lipidation [PMID:29712776].
- p53/apoptosis: with syntenin SDCBP regulates p53/TP53 and p53-dependent apoptosis [PMID:15371445]; positive regulation of intrinsic apoptotic signaling by p53.
- TNF-mediated apoptosis; nuclear accumulation upon TNFalpha [PMID:17187778].
- Microbial infection cofactor: cellular target of HIV-1 Rev and HTLV-1 Rex, required for retroviral mRNA export [PMID:8253832]. The two "cellular response to virus" IMP annotations (PMID:8596953, PMID:9465063) reflect this Rev/Rex cofactor role.
- mRNA decay / NMD: ts mutant accumulates NMD-targeted transcripts [PMID:16987817].

## Hypusine pathway partners
- DHPS (deoxyhypusine synthase, P49366) — interaction PMID:10229683; substrate-enzyme complex.
- DOHH (deoxyhypusine hydroxylase, Q9BU89) — interaction PMID:17213197.
These two IPI partners (DHPS, DOHH) are the enzymes that install the hypusine modification — biologically meaningful, not generic.

## RNA binding
- IDA RNA binding (PMID:15303967 mRNA binding) and HDA RNA binding (PMID:22681889, RNA interactome capture). U6 snRNA binding IDA (PMID:9285100). eIF5A binds mRNA at the ribosome; OB-fold domain. RNA binding is real but the informative function is ribosome/translation.

## Transcription annotation
- GO:0045944 positive regulation of transcription by RNA Pol II (IMP PMID:15371445) — this paper is about p53 regulation / apoptosis, the transcription effect is indirect (downstream of p53). Non-core.

## Interactome IPI partners (high-throughput, mostly homeodomain TFs / generic)
- PMID:25416956 (Y2H): CRX (O43186), DHPS (P49366), MEOX2 (P50222), REL (Q04864). 
- PMID:32296183 (HuRI binary): MEI4, SDCBP(O00560), GSC2, DHPS, LBX1, REL-2, MEOX2, PICK1. Many homeodomain TFs - likely Y2H artifacts of the OB-fold/basic protein.
- PMID:33961781 (BioPlex): DOHH (Q9BU89) — meaningful (hypusine pathway).

## Disease
Faundes-Banka syndrome (FABAS, autosomal dominant; dev delay, microcephaly, micrognathia). Variants reduce ribosome binding, hypusination, and polyproline translation [PMID:33547280].

## Curation conclusions
- CORE MF: translation elongation factor activity (GO:0003746); ribosome binding (GO:0043022) is core/supporting.
- CORE BP: translational elongation (GO:0006414); positive regulation of translational elongation (GO:0045901).
- Location cytoplasm/cytosol/nucleus = accept; ER membrane and nuclear pore/annulate lamellae = keep non-core (shuttling/peripheral).
- p53/TNF/apoptosis/transcription/virus = KEEP_AS_NON_CORE (real but pleiotropic/downstream).
- Generic protein binding IPI from HT screens = KEEP_AS_NON_CORE or MODIFY for the hypusine-enzyme partners.
- U6 snRNA binding = single old IDA, peripheral; keep non-core.
