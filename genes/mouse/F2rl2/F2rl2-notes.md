# F2rl2 (Mouse PAR3) - Research Notes

## Gene Identity

- **Gene:** F2rl2 (Mus musculus)
- **UniProt:** O08675 (PAR3_MOUSE)
- **Full name:** Proteinase-activated receptor 3 (PAR-3)
- **Synonyms:** Par3, Coagulation factor II receptor-like 2, Thrombin receptor-like 2
- **MGI:** MGI:1298208

## Key Literature

### Discovery and Cloning

PMID:9087410 (Ishihara et al., Nature 1997) - "Protease-activated receptor 3 is a second thrombin receptor in humans." Original cloning of PAR3. Reports PAR3 as a new G-protein-coupled receptor activated by thrombin via proteolytic cleavage, mediating phosphoinositide hydrolysis. Expressed in bone marrow and megakaryocytes. Also reports the mouse sequence (strain C57BL/6J). [PMID:9087410 "PAR3 can mediate thrombin-triggered phosphoinositide hydrolysis and is expressed in a variety of tissues, including human bone marrow and mouse megakaryocytes"]

### Critical Discovery: Mouse PAR3 is a Cofactor, Not a Signaling Receptor

PMID:10766244 (Nakanishi-Matsui et al., Nature 2000) - "PAR3 is a cofactor for PAR4 activation by thrombin." This is the seminal paper showing that **mouse PAR3 does not itself mediate transmembrane signaling**. Instead, mPAR3 functions as a cofactor that binds thrombin and presents it to PAR4 for cleavage and activation. This is a fundamentally different mechanism from human PAR3, which can signal directly. [PMID:10766244 "mPAR3 does not itself mediate transmembrane signalling but instead functions as a cofactor for the cleavage and activation of mPAR4 by thrombin"]

### PAR3 Knockout Mouse

PMID:12384423 (Weiss et al., Blood 2002) - "Protection against thrombosis in mice lacking PAR3." Par3-/- mice are protected against ferric chloride-induced thrombosis and thromboplastin-induced pulmonary embolism. Platelet thrombin responses are decreased but not absent (because PAR4 can still be activated at high thrombin concentrations). Similar degree of protection as Par4-/- mice. [PMID:12384423 "Par3(-/-) mice were protected against ferric chloride-induced thrombosis... even a partial decrease in mouse platelet responsiveness to thrombin protected against thrombosis"]

### PAR4 Knockout (Context for PAR3 Function)

PMID:11544528 (Sambrano et al., Nature 2001) - "Role of thrombin signalling in platelets in haemostasis and thrombosis." PAR4 knockout ablates all thrombin signaling in mouse platelets, confirming that mPAR3 does not independently signal. [PMID:11544528 "supports the model that mouse PAR3 (mPAR3) does not by itself mediate transmembrane signalling but instead acts as a cofactor for thrombin cleavage and activation of mPAR4"]

### PAR3-PAR4 Dimerization and Negative Regulation

PMID:23405206 (Arachiche et al., PLoS ONE 2013) - PAR3 forms constitutive homodimers and heterodimers with PAR4 (shown by BRET). PAR3 negatively regulates PAR4-mediated maximum Ca2+ mobilization and PKC activation in mouse platelets by physical interaction. [PMID:23405206 "PAR3 negatively regulates PAR4-mediated maximum Ca(2+) mobilization and PKC activation in mouse platelets by physical interaction"]

### PAR3 and Insulin Secretion

PMID:26742564 (Hanzelmann et al., Islets 2015) - "Thrombin stimulates insulin secretion via protease-activated receptor-3." PAR3-activating peptide (PAR3-AP; SFNGGP) stimulates insulin secretion from mouse islets via PLC activation and Ca2+ release from intracellular stores. The PAR3 tethered ligand acts as an agonist. This paper was done primarily with mouse islets but also human islets. An anti-PAR3 antibody (H103) blocking the thrombin cleavage site prevented thrombin-stimulated insulin secretion. [PMID:26742564 "thrombin stimulates insulin secretion, an effect that was prevented by an antibody that blocks the thrombin cleavage site of PAR3"]

### Apical Plasma Membrane Localization (PMID:16892058)

PMID:16892058 (Cappello et al., Nat Neurosci 2006) - "The Rho-GTPase cdc42 regulates neural progenitor fate at the apical surface." This paper is primarily about Cdc42 and neural progenitors. It mentions the "Par complex" (aPKC-Par3-Par6) at the apical surface. **IMPORTANT NOTE:** The Par3 referenced in this paper is the cell polarity protein PARD3, NOT the thrombin receptor F2rl2/PAR3. The GO annotation of F2rl2 to "apical plasma membrane" (GO:0016324) based on this paper may be erroneous -- possibly a confusion between the two proteins named "Par3."

### Asymmetric Cell Division / Protein Interactions

PMID:16094321 (Lechler & Fuchs, Nature 2005) - "Asymmetric cell divisions promote stratification and differentiation of mammalian skin." Reports interaction of PAR3 with INSC (Inscuteable) and GPSM2 (LGN). **IMPORTANT NOTE:** This paper also refers to the cell polarity protein PARD3 (Par3), not F2rl2. The UniProt entry for O08675 states "INTERACTION WITH INSC AND GPSM2" citing this paper, but this appears to be an error -- these are interactions of the polarity protein PARD3, not the thrombin receptor PAR3/F2rl2.

### DNA Methylation Context

PMID:28179424 (Lupu et al., FASEB J 2017) - Found altered methylation and expression of F2rl2 in Bhmt-null mouse liver, associated with preneoplastic foci. Peripheral to core function but shows F2rl2 expression in liver.

## Key Biological Insights

1. **Mouse PAR3 is fundamentally different from human PAR3.** Human PAR3 can signal independently via Gq. Mouse PAR3 does NOT signal independently -- it acts as a cofactor to present thrombin to PAR4.

2. **Cofactor mechanism:** mPAR3 binds thrombin via its extracellular domain, concentrating it near PAR4 on the platelet surface. This lowers the effective thrombin concentration needed for PAR4 activation.

3. **PAR3 also negatively regulates PAR4 signaling amplitude** through constitutive heterodimer formation (PMID:23405206).

4. **The "receptor ligand activity" annotation (GO:0048018)** from PMID:26742564 reflects the tethered ligand mechanism -- after proteolytic cleavage, the new N-terminus of PAR3 acts as an intrinsic ligand. The PAR3-activating peptide (SFNGGP) can stimulate insulin secretion, showing the tethered ligand has biological activity.

5. **Questionable annotations from PMID:16892058 and PMID:16094321:** Both papers study the POLARITY protein Par3 (Pard3), not the thrombin receptor PAR3 (F2rl2). The apical plasma membrane annotation and the protein interaction annotations may be erroneous.

## GO Annotation Assessment

### Annotations that are well-supported:
- GPCR activity (IBA, IEA) - PAR3 is a 7TM GPCR
- GPCR signaling pathway (IBA, IEA, IDA from PMID:26742564) - well-supported
- Plasma membrane (IBA, IEA) - multi-pass membrane protein
- Thrombin-activated receptor activity (IEA) - direct thrombin substrate
- Blood coagulation (IEA) - role in hemostasis via PAR4 cofactor function
- Thrombin-activated receptor signaling pathway (IEA) - core function
- Proteinase-activated receptor activity (IGI from PMID:26742564) - well-supported
- Receptor ligand activity (IDA from PMID:26742564) - tethered ligand mechanism

### Annotations that are questionable:
- Apical plasma membrane (IDA from PMID:16892058) - likely refers to PARD3 not F2rl2
- Protein-containing complex (ISO/IEA) - likely refers to PARD3 complex, not F2rl2

### Annotations that should be considered:
- Positive regulation of insulin secretion (GO:0032024) - from PMID:26742564
- PAR3 cofactor function for PAR4 - the most distinctive function of mouse PAR3 (PMID:10766244)
