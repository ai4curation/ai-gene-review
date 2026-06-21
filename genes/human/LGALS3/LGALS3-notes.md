# LGALS3 (Galectin-3, P17931) — Gene Review Notes

## Summary of identity
- Human galectin-3 / Mac-2 antigen / CBP35 / IgE-binding protein / L-29 / L-31. HGNC:6563, UniProt P17931, 250 aa, chromosome 14.
- The **only chimera-type galectin** in mammals: a single C-terminal carbohydrate-recognition domain (CRD, ~residues 113–250) fused to an intrinsically disordered, proline/glycine-rich N-terminal tail (collagen-like repeats) that enables oligomerization.
- The CRD binds β-galactosides (lactose, N-acetyllactosamine/LacNAc), structurally solved at high resolution (e.g. PDB 1A3K, 2.1 Å; UniProt RN[25] PMID:9582341).

## Core molecular function: β-galactoside / carbohydrate binding + lattice formation
- "Galactose-specific lectin which binds IgE" (UniProt FUNCTION). Cloned as a galactose-specific macrophage lectin [PMID:2402511 "Molecular cloning of a human macrophage lectin specific for galactose"] and as a galactoside-binding lectin homologous to mouse Mac-2 [UniProt RN3 PMID:2022338].
- Gal-3 is monomeric but achieves functional **multivalency** via N-terminal self-association: "galectin-3 is monomeric, and its functional multivalency therefore is somewhat of a mystery... the disordered N-terminal domain (residues ∼20-100) interacts with itself and with a part of the CRD... forming a fuzzy complex" and "galectin-3 can also undergo liquid-liquid phase separation" [PMID:28893908]. This is the molecular basis for lattice/agglutination.
- Extracellular agglutination/lattice: "The mechanism through which galectin-3 agglutinates (acting as a 'bridge' to aggregate glycosylated molecules)... Our data show that its N-terminal domain (NTD) undergoes LLPS... aggregate LPS micelles. Aggregation is reversed when interactions between the LPS and the carbohydrate recognition domains are blocked by lactose" [PMID:32144274]. → DisProt annotated GO:0140693 molecular condensate scaffold activity from these two papers.
- Polysaccharide binding to NT: a novel binding site within the N-terminal tail in addition to two CRD sites [PMID:28973299 "two within its carbohydrate recognition domain (CRD) and one at a novel site within the NT"]. → supports GO:0030246 carbohydrate binding EXP DisProt.

This carbohydrate-binding + lattice-forming activity is the CORE function; nearly all downstream biology (adhesion, immune modulation, chemoattraction, apoptosis regulation) is mediated by cross-linking glycoconjugates.

## Localization (intracellular + extracellular)
- UniProt SUBCELLULAR LOCATION: Cytoplasm; Nucleus; Secreted (non-classical). Nuclear and cytoplasmic well-supported experimentally [PMID:7682704 nucleus IDA; PMID:14961764, PMID:22761016].
- Secreted by a non-classical (leaderless) pathway facilitated by cargo receptor TMED10 → translocation cytoplasm→ERGIC→secretion [UniProt; PMID:32272059].
- Acts both intracellularly and at the cell surface/ECM. Many HDA proteomics annotations place it in extracellular exosome/ECM/extracellular region — consistent with abundant secretion, but these are localization-by-detection (mass spec) not function.
- Nuclear role as pre-mRNA splicing factor (UniProt FUNCTION; spliceosomal complex keyword); RNA binding HDA from mRNA interactome [PMID:22658674].

## Damaged-endomembrane sensing / autophagy (lysophagy)
- "Together with TRIM16, coordinates the recognition of membrane damage with mobilization of the core autophagy regulators ATG16L1 and BECN1 in response to damaged endomembranes" [UniProt FUNCTION; PMID:27693506]. Gal-3 detects exposed luminal glycans on ruptured endo/lysosomal membranes and recruits autophagy machinery (a glycan-sensing function). Important, increasingly recognized intracellular role.

## Immune / inflammatory roles (downstream, pleiotropic)
- Chemoattractant for monocytes/macrophages: "galectin-3 is a novel chemoattractant for monocytes and macrophages... mediated at least in part through a PTX-sensitive (G protein-coupled) pathway"; blocked by lactose [PMID:10925302]. This one paper underpins many BHF-UCL IDA annotations (monocyte/eosinophil/macrophage/neutrophil chemotaxis, positive chemotaxis, mononuclear cell migration, Ca2+ influx, chemoattractant activity).
- T-cell modulation: overexpression increases T-cell growth and confers resistance to apoptosis (Bcl-2-like NWGR motif, interacts with Bcl-2) [PMID:8692888]. Underpins regulation of T cell proliferation (IMP) and regulation of T cell apoptotic process / extrinsic apoptotic signaling.
- Negatively regulates TCR signaling at the immunological synapse, reduces TCR clustering, drives endocytosis-related changes [PMID:19706535]. Underpins immunological synapse localization (IDA) and the human IDA negative-regulation-of-endocytosis annotation; the ISS T-cell terms are transferred from mouse ortholog P16110.
- Acts as a soluble inhibitory ligand of NKp30/NCR3, blocking B7-H6–NKp30 activation → inhibits NK / NKT / ILC2 activation [PMID:25315772 tumor escape; PMID:26582946 ILC2/NKp30, where Gal-3 = "an inhibitory ligand"]. Underpins receptor ligand inhibitor activity (GO:0141069 IDA) and negative regulation of NK T cell activation.
- Anti-apoptotic in tumor cells; EGF downregulates cytoplasmic Gal-3 to permit apoptosis [PMID:22761016] → negative regulation of extrinsic apoptotic signaling pathway (IDA).
- NOT annotation: Gal-3 does NOT positively regulate dendritic cell differentiation [PMID:16116184 — this paper is about galectin-9 inducing DC maturation; the NOT|involved_in for Gal-3 reflects that Gal-3 lacks this activity]. Keep negated annotation.

## Glycosylation / lattice at the cell surface (mechanistic exemplar)
- β1,6-GlcNAc-branched N-glycans (GnT-V products) on receptors are recognized by Gal-3, retaining them at the surface and modulating their function: "GnT-V overexpression enhances galectin-3's cell-surface retention and promotes PTPRT's dimerization mediated by galectin-3" [PMID:24846175]. Underpins protein phosphatase binding (IPI, PTPRT/O14522), positive regulation of protein localization to plasma membrane, positive regulation of protein-containing complex assembly. The "protein phosphatase inhibitor activity" (GO:0004864 IDA) is indirect (it promotes PTPRT dimerization which lowers PTPRT activity) — this is a glycan-lattice effect, not a direct enzyme-inhibitor MF; flag as over-annotation/keep-non-core.

## Interactions ("protein binding", GO:0005515)
~25 GO:0005515 IPI annotations, mostly from high-throughput interactome screens (PMID:25416956, 28514442, 31515488, 32296183, 33961781, 40205054) or single-partner IPI (MMP7 PMID:20812334 — MMP7 cleaves Gal-3; CD6/ALCAM PMID:24945728; CHI3L1/IL13RA2 PMID:29427412; endoglin/ENG PMID:31540324; MICA PMID:21712812; SARS-CoV-2 spike PMID:32915505; F1F0-ATP synthase ATP5B PMID:19016746). Generic "protein binding" is uninformative per curation guidelines — mark as over-annotated; the informative MF is carbohydrate/galactoside binding (many of these are glycan-dependent contacts). Do NOT remove (experimental IPI), but down-grade to over-annotated.

## Verdict logic applied
- CORE: carbohydrate binding (GO:0030246), galactoside binding (GO:0016936), molecular condensate scaffold activity / lattice (GO:0140693), and the glycan-sensing endomembrane-damage role.
- Generic GO:0005515 protein binding → MARK_AS_OVER_ANNOTATED (uninformative).
- HDA proteomics localizations (exosome, ECM, membrane, mitochondrial inner membrane, extracellular region) → mostly KEEP_AS_NON_CORE; the mitochondrial inner membrane IDA (PMID:19016746) is a single ATP-synthase-interaction study, treat as non-core/over-annotated.
- Immune/chemotaxis/apoptosis BP terms → KEEP_AS_NON_CORE (real but pleiotropic, downstream of lattice function).
- IBA, IDA core lectin & nucleus/cytoplasm localizations → ACCEPT.
- Redundant IEA/IBA that duplicate experimental annotations → ACCEPT or KEEP_AS_NON_CORE.
- ARBA IEA broad T-cell process terms (GO_REF:0000117) → KEEP_AS_NON_CORE (real but transferred/pleiotropic).
- GO:0048018 receptor ligand activity (ARBA IEA) → the better-supported MF is the inhibitory-ligand activity (GO:0141069, IDA); generic receptor ligand activity is borderline — MARK_AS_OVER_ANNOTATED in favor of the specific IDA term.

## GO terms verified for core_functions (hard-validated, MF/BP/CC branch)
- GO:0030246 carbohydrate binding — MF (in GOA already)
- GO:0016936 galactoside binding — MF (QuickGO verified, def "Binding to a glycoside in which the sugar group is galactose")
- GO:0140693 molecular condensate scaffold activity — MF (in GOA, DisProt)
- GO:0061684 (chaperone-mediated autophagy? no) — not used
- locations: GO:0005634 nucleus, GO:0005737 cytoplasm, GO:0005576 extracellular region, GO:0009986 cell surface, GO:0031012 extracellular matrix (all CC, in GOA)
- BP: GO:0061709 (reticulophagy? no). Endomembrane damage response — GO:0061912 selective autophagy? Will use GO:0007165 sparingly. For lattice/adhesion will keep BP minimal.
</content>
</invoke>
