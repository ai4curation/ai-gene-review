# slp1 (Cdc20/Fizzy ortholog) — review notes

## Identity
- UniProt P78972, SPAC821.08c, gene `slp1`. WD repeat-containing protein, 488 aa, 7 WD40 repeats (178–473). Belongs to the WD repeat CDC20/Fizzy family.
- Fission-yeast ortholog of CDC20/p55CDC/Fizzy; the mitotic substrate-recognition co-activator of the anaphase-promoting complex/cyclosome (APC/C). PDB 4AEZ (88–488) is the WD40 beta-propeller; structure of the S. pombe MCC (Mad2-Mad3-Slp1/Cdc20) is PDB-related to PMID:22437499.

## Core function
- Slp1/Cdc20 is the transiently available APC/C activator early in mitosis; later in mitosis/G1 the activator switches to Ste9/Cdh1 [PMID:18556659 "In order for the APC/C to become active, it must interact with a transiently available activator; early in mitosis, this is Slp1/Cdc20, and later in mitosis and in G1, it switches to Ste9/Cdh1"].
- Cdc20Slp1-APC/C targets securin (Cut2) and cyclin B (Cdc13) for destruction by the 26S proteasome; once securin is destroyed, cohesin is cleaved and sister chromatids separate [PMID:26882497 "Cdc20Slp1-APC/C targets the separase inhibitor securin and the CDK1 activating subunit cyclin B for destruction by the 26S proteasome ... Once securin is destroyed, cohesin is cleaved and sister chromatids separate and segregate in anaphase"].
- Slp1 is essential for anaphase onset [PMID:9461438 "Slp1, a WD (tryptophan-aspartic acid)-repeat protein essential for the onset of anaphase"].

## Spindle assembly checkpoint (SAC) target
- Slp1/Cdc20 is the key target of the SAC; the mitotic checkpoint complex (MCC = Mad2-Mad3-Slp1/Cdc20 in S. pombe) binds and inhibits Cdc20-APC/C until kinetochores are correctly attached [PMID:18556659 "Cdc20 is the key target of the SAC ... the mitotic checkpoint complex (MCC, typically Mad3/BubR1-Bub3-Mad2-Cdc20) is a far more potent inhibitor than Mad2 in vitro"].
- Mad2 forms a complex with Slp1; disrupting the Slp1-Mad2 interaction abolishes the spindle checkpoint [PMID:9461438 "Mad2 formed a complex with Slp1 ... When the physical interaction between the two proteins was disrupted, the spindle checkpoint was no longer functional"]. Mutation of Slp1 residues 131-132 (AF->PY) abrogates Mad2 binding and overrides checkpoint activation (UniProt MUTAGEN feature; PMID:9461438).
- The S. pombe MCC crystal structure (Mad2, Mad3, Cdc20/Slp1) shows MCC inhibits the APC/C by obstructing degron recognition sites on Cdc20 and displacing Cdc20 from forming a bipartite D-box receptor with Apc10; C-Mad2 positions the Mad3 KEN-box to bind Cdc20 [PMID:22437499 "the crystal structure of Schizosaccharomyces pombe MCC (a complex of mitotic spindle assembly checkpoint proteins Mad2, Mad3 and APC/C co-activator protein Cdc20) ... The MCC inhibits the APC/C by obstructing degron recognition sites on Cdc20 ... and displacing Cdc20 ... Mad2, in the closed conformation (C-Mad2), stabilizes the complex by optimally positioning the Mad3 KEN-box degron to bind Cdc20"].
- Mad3 N-terminal KEN box (KEN1) is required for stable Mad3-Cdc20/Slp1 binding and MCC assembly [PMID:18556659 "mutation of the N-terminal KEN box abolishes incorporation of Mad3 into the mitotic checkpoint complex (Mad3-Mad2-Slp1 in S. pombe ...)"]. Slp1-362 mutant cannot bind APC/C at restrictive temperature [PMID:18556659 "the mutant Slp1-362 protein is unable to bind the APC/C at restrictive temperature"].
- Mps1Mph1 phosphorylation of Mad3 (near KEN2) directly potentiates inhibition of Cdc20Slp1-APC/C; in vitro Cdc20Slp1-APC/C ubiquitinates radiolabelled securin/Cut2 and Mad3 phosphomimics inhibit it [PMID:26882497 "recombinant fission yeast Mad3p can directly inhibit in vitro Cdc20Slp1-APC/C activity: as the concentration of recombinant Mad3p was increased, a corresponding decrease in Cdc20 Slp1-APC/C dependent ubiquitination of the radio-labelled securinCut2 substrate was observed"]. This is the basis for the GO:1990757 (ubiquitin ligase activator activity) IDA annotation.

## MCC composition (CC)
- Fission-yeast MCC is exclusively Mad3-Mad2-Cdc20/Slp1 (no Bub3) [PMID:18556659 "Mad3 is part of the MCC, which in fission yeast is comprised exclusively of Mad3, Mad2, and Cdc20. In other organisms, Bub3 is also a component of the MCC. However, S. pombe Mad3 lacks the GLEBS motif"]. Confirms `part_of mitotic checkpoint complex` (GO:0033597).

## Meiosis
- Slp1/Cdc20 is the only coactivator essential for meiosis I progression; slp1-NF410 ts cells delay anaphase I and stabilize Cut2/Cdc13 [PMID:21389117 "only Slp1/Cdc20 is essential for meiosis I progression ... The slp1-NF410 mutant diploid cells showed a significant delay in anaphase I onset and stabilization of Cut2 and Cdc13"]. Supports GO:1990949 (metaphase/anaphase transition of meiosis I) and APC/C-dependent catabolic process IMP/EXP.
- Mes1 is a meiosis-specific APC/C inhibitor and substrate that binds the WD40 domain of Fizzy-family activators including Slp1; ubiquitylation of Mes1 by APC/C-Slp1 relieves inhibition [PMID:18331722 "Mes1 directly binds the WD40 domain of the Fizzy family of APC/C activators"; PMID:21389117 "Slp1 alleviates Mes1 inhibition through its ubiquitylation"]. Mes1 (P41005, SPAC5D6.08c) interaction with Slp1 supports the protein-binding IPI annotations (PMID:15791259, PMID:21389117).
- For meiosis II, Slp1 reactivation contributes; GO:1990950 (metaphase/anaphase transition of meiosis II) EXP from PMID:21389117 (both Slp1 and Fzr1/Mfr1 become active to complete anaphase II).

## Localization
- HDA proteome localization study (PMID:16823372) reports nucleus, cell division site, mitotic spindle pole body, mitotic spindle. Consistent with Cdc20 nuclear/mitotic-structure localization, but HDA from a global ORFeome-tagging study; nucleus is the core compartment (where APC/C substrates are degraded). Spindle/SPB/division-site are mitotic-apparatus locations consistent with function but are best kept as non-core given they come from a single high-throughput dataset.
- Kinetochore (GO:0000776): NAS/TAS from PMID:15930132 (Mis6/Mad2 paper). This paper is about Mad2 kinetochore loading and does not directly assay Slp1 at kinetochore; the kinetochore localization annotation is curator-assigned (NAS/TAS). Cdc20/Slp1 transiently localizes to kinetochores in many systems. Keep as non-core (functions in checkpoint signalling that occurs at the kinetochore).

## Protein-binding (GO:0005515) annotations to refine
- PMID:15791259 / PMID:21389117 with Mes1 (P41005, SPAC5D6.08c): bind to meiotic APC/C inhibitor Mes1 -> better captured as adaptor/APC/C activator function; replace bare "protein binding".
- PMID:22437499 / PMID:9461438 with Mad2 (O14417): bind SAC protein Mad2 within MCC.
- PMID:18331722 with SPAC5D6.08c (Mes1).
- PMID:28178520 with SPAC18G6.15: Sgo2-dependent/Mad2-independent anaphase pathway paper. SPAC18G6.15 needs ID confirmation; treat the bare protein-binding term as over-annotation/uninformative -> replace with adaptor function or mark as over-annotated.

## IBA / IEA assessment
- IBA (GO_REF:0000033) for anaphase-promoting complex (CC), positive regulation of APC/C catabolic process, APC/C binding, APC/C-dependent catabolic process, ubiquitin ligase activator activity: all consistent with strong experimental data; ACCEPT.
- IEA InterPro2GO: GO:0010997 (APC/C binding) duplicate of experimental; GO:0097027 (ubiquitin-protein transferase activator activity) — APC/C is a RING E3 ligase, so "ubiquitin ligase activator activity" (GO:1990757) is the more accurate term; GO:0097027 is essentially equivalent/parent-ish and is supported. ARBA IEA GO:0031145 duplicate of experimental. Keep IEAs as ACCEPT (consistent) or note duplication.

## Core function summary
- MF: ubiquitin ligase activator activity (APC/C activator), APC/C binding (substrate-recognition WD40 co-activator/adaptor).
- BP: APC/C-dependent catabolic process, positive regulation of APC/C-dependent catabolic process, metaphase/anaphase transition (mitosis and meiosis I/II), mitotic spindle assembly checkpoint signalling (as the SAC target).
- CC: anaphase-promoting complex (slp1 variant), mitotic checkpoint complex, nucleus.
