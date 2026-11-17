---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF2
affinage_run_date: 2026-06-14T07:33:11
uniprot_accession: Q92974
self_evaluation_pairwise: win
faith_pct: 
n_discoveries: 64
citation_count: 64
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF2 (human)

## Current model (mechanistic narrative)

ARHGEF2 (GEF-H1/Lfc) is a Dbl-family guanine nucleotide exchange factor that catalytically and specifically activates RhoA (and to a lesser extent Rac1) to drive actin stress fiber formation, cell contractility, mitotic spindle assembly, epithelial barrier regulation, and innate immune signaling [PMID:8910315, PMID:9857026, PMID:9890991]. Its activity is gated by microtubule binding through its C-terminal coiled-coil region: microtubule-associated GEF-H1 is held in an autoinhibited state, and microtubule depolymerization or release from the cytoskeleton liberates active GEF-H1 to load GTP onto RhoA [PMID:11912491, PMID:18287519, PMID:31420453]. Release is achieved by diverse inputs — drug-induced or mechanically/matrix-stiffness-induced microtubule destabilization [PMID:18287519, PMID:22593214], displacement by Gα subunits and RalA–Sec5 exocyst coupling downstream of GPCR ligands [PMID:25209408, PMID:22898781], and bacterial effectors (EPEC EspG/Orf3, Vibrio VopO, Bartonella BepC) that destabilize microtubules or directly bind and relocalize GEF-H1 to activate RhoA-ROCK signaling [PMID:15318166, PMID:25738744, PMID:33508040]. A dense phosphoregulatory network tunes the protein: phosphorylation by PAK1, PAK4, PAR1b/MARK2, MARK3, PKA/PKG creates 14-3-3 binding sites that tether GEF-H1 to microtubules and suppress exchange activity, while ERK (Thr678), NEK9, and HUNK (Ser645) phosphorylation enhance activity; PP2A reverses inhibitory phosphorylation at Ser885/Ser151 to restore activity [PMID:14970201, PMID:15827085, PMID:22072711, PMID:29089450, PMID:18211802, PMID:33500736, PMID:37193711, PMID:33762326, PMID:25209408]. GEF-H1 is sequestered at tight junctions by cingulin and paracingulin to restrain epithelial RhoA and G1/S progression [PMID:15866167, PMID:18653465], and is essential for RhoA-dependent mitotic spindle assembly and cleavage-furrow Rho activation during cytokinesis [PMID:15976019, PMID:17488622]. Beyond its catalytic role, GEF-H1 acts as a non-catalytic adaptor linking PP2A to the scaffold KSR-1 to activate MAPK downstream of oncogenic RAS [PMID:24525234], and is required for innate immune signaling through NOD1/NOD2–RIP2 to NF-κB, RIG-I/Mda5 to IRF3/IFN-β, and an IKKε–IRF5 peptidoglycan-sensing pathway [PMID:19043560, PMID:21887730, PMID:24270516, PMID:30902986]. Homozygous frameshift mutation in ARHGEF2 causes intellectual disability and midbrain-hindbrain malformation, with loss shifting mitotic spindle orientation toward symmetric divisions and reducing RhoA/ROCK/MLC signaling [PMID:28453519].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol, GO:0005815 microtubule organizing center, GO:0005886 plasma membrane, GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-168256 Immune System, R-HSA-1640170 Cell Cycle, R-HSA-1643685 Disease, R-HSA-5653656 Vesicle-mediated transport
- **partners:** RHOA, RAC1, TCTEX-1/DYNLT1, 14-3-3, CINGULIN, SEC5, NOD1, RIP2
- **complexes:** NOD2-RIP2 signaling complex, exocyst (via Sec5), PP2A-KSR-1 adaptor complex, AMPA receptor complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1995 | High | Lfc (ARHGEF2) was identified as an oncoprotein containing a Dbl homology (DH) domain in tandem with a pleckstrin homology (PH) domain; deletion analysis showed both PH and DH domains are required for NIH 3T3 transformation, with the PH domain mediating membrane recruitment necessary for transforming activity. | PMID:7629163 | The Journal of biological chemistry |
| 1996 | High | Lfc (ARHGEF2) functions as a highly specific guanine nucleotide exchange factor for RhoA in vitro, catalytically stimulating >10-fold GDP dissociation from RhoA; it forms tight complexes with nucleotide-depleted RhoA and, uniquely, also binds Rac (but not Cdc42 or Ras), distinguishing it from other Dbl-family GEFs. | PMID:8910315 | The Journal of biological chemistry |
| 1998 | High | GEF-H1 (ARHGEF2) stimulates guanine nucleotide exchange on Rac and Rho but not Cdc42, TC10, or Ras; it colocalizes with microtubules through its carboxyl-terminal coiled-coil domain, and overexpression in COS-7 cells induces membrane ruffles. | PMID:9857026 | The Journal of biological chemistry |
| 1999 | High | Lfc (ARHGEF2) localizes to microtubules via its PH domain interaction with tubulin; overexpression in NIH 3T3 cells induces actin stress fibers and membrane ruffles consistent with RhoA and Rac1 activation, and Lfc stimulates JNK activity in a Rac1-dependent (and partially RhoA-dependent) manner. | PMID:9890991 | The Journal of biological chemistry |
| 2002 | High | GEF-H1 (ARHGEF2) is regulated by microtubule binding: GEF-H1 mutants deficient in microtubule binding have higher RhoA GEF activity, and drug-induced microtubule depolymerization phenocopies active GEF-H1 expression in a dominant-negative GEF-H1-inhibitable manner, establishing that microtubule-bound GEF-H1 is in an inactive state. | PMID:11912491 | Nature cell biology |
| 2004 | High | PAK1 phosphorylates GEF-H1 at Ser885 (within the carboxyl-terminal inhibitory region), inducing 14-3-3 binding to GEF-H1 and relocation of 14-3-3 to microtubules; the carboxyl-terminal coiled-coil region of GEF-H1 is required for microtubule-dependent suppression of its GEF activity. | PMID:14970201 | The Journal of biological chemistry |
| 2004 | High | EPEC effectors EspG and Orf3 interact with tubulin and destabilize microtubules in vitro, thereby releasing GEF-H1 and activating RhoA-ROCK signaling to induce actin stress fibers; dominant-negative GEF-H1 and dominant-negative RhoA (but not Rac1/Cdc42) block EspG/Orf3-induced stress fiber formation. | PMID:15318166 | The EMBO journal |
| 2005 | High | PAK4 directly associates with GEF-H1 through a novel GEF-H1 interaction domain (GID) in PAK4 and phosphorylates GEF-H1 at Ser810, blocking stress fiber formation while promoting lamellipodia; the endogenous PAK4–GEF-H1 complex associates with microtubules, and PAK4 phosphorylation releases GEF-H1 into the cytoplasm. | PMID:15827085 | Journal of cell science |
| 2005 | High | GEF-H1 (Lfc/ARHGEF2) directly interacts with cingulin (a tight-junction adaptor protein); cingulin binding inhibits GEF-H1 RhoA GEF activity, providing a mechanism by which tight junction formation downregulates RhoA and inhibits G1/S cell cycle progression. | PMID:15866167 | Developmental cell |
| 2005 | High | Lfc (ARHGEF2) interacts with neurabin and spinophilin via its coiled-coil domain; upon neuronal stimulation, Lfc translocates from dendritic shafts (where it associates with microtubules) to spines, reducing spine length and size through RhoA in a coiled-coil-dependent manner. | PMID:15996550 | Neuron |
| 2005 | High | Lfc (ARHGEF2) is required for mitotic spindle assembly during prophase/prometaphase; inhibition of Lfc causes spindle defects and mitotic delay, rescued by constitutively active RhoA, placing Lfc upstream of RhoA in a pathway involving mDia1 for spindle formation. | PMID:15976019 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | Medium | Mutant p53 proteins (V157F, R175H, R248Q) transcriptionally activate GEF-H1 expression, leading to RhoA activation and accelerated tumor cell proliferation; growth of mutant p53 cells depends on GEF-H1 expression whereas wild-type p53 cells do not. | PMID:16778209 | Cancer research |
| 2006 | High | TRIF-dependent (but not MyD88-dependent) LPS signaling in dendritic cells activates GEF-H1, which in turn activates RhoB (but not RhoA, Rac, or Cdc42); GEF-H1–RhoB drives surface MHCII expression required for CD4+ T cell activation. | PMID:16917499 | The EMBO journal |
| 2007 | High | GEF-H1 localizes to the mitotic apparatus (cortical microtubule tips and midbody); Aurora A/B and Cdk1/Cyclin B phosphorylate GEF-H1, inhibiting its catalytic activity during mitosis; dephosphorylation before cytokinesis allows GEF-H1-dependent RhoA GTP-loading at the cleavage furrow, distinct from Ect2-dependent Rho activation. | PMID:17488622 | Developmental cell |
| 2008 | High | GEF-H1 is required and sufficient to mediate nocodazole-induced RhoA activation and cell contractility; siRNA depletion of GEF-H1 prevents nocodazole-induced RhoA activation, ROCK activation, MLC phosphorylation, and cell contraction, rescued by siRNA-resistant GEF-H1 re-expression. | PMID:18287519 | Molecular biology of the cell |
| 2008 | High | ERK1/2 phosphorylate GEF-H1 at Thr678, enhancing its guanine nucleotide exchange activity toward RhoA; ERK pathway inhibition (PD184352) abolishes this phosphorylation. | PMID:18211802 | Biochemical and biophysical research communications |
| 2008 | High | GEF-H1 interacts with NOD1 and is required for RIP2-dependent NF-κB activation in response to Shigella effectors IpgB2 and OspB and the NOD1 ligand γTriDAP; GEF-H1 is also required for Shigella cell invasion via RhoA activation. | PMID:19043560 | PLoS pathogens |
| 2009 | High | Lfc (ARHGEF2) localizes to the Golgi apparatus and growth cones in developing neurons and negatively regulates neurite sprouting and axon formation via RhoA; Tctex-1 (dynein light chain) physically interacts with Lfc, inhibiting its GEF activity, decreasing Rho-GTP, and antagonizing Lfc during neurite formation. | PMID:20463241 | The Journal of neuroscience |
| 2009 | High | Lfc (ARHGEF2) and its negative regulator Tctex-1 determine the balance between proliferative symmetric and neurogenic asymmetric divisions of cortical radial precursors; Lfc knockdown maintains cells as cycling radial precursors while Tctex-1 knockdown promotes neurogenesis; the two proteins regulate mitotic spindle orientation. | PMID:19448628 | Nature neuroscience |
| 2009 | High | PKA phosphorylates Lfc (ARHGEF2) in an AKAP121-dependent manner; this phosphorylation promotes 14-3-3 binding to Lfc in a phosphorylation-dependent manner and suppresses Lfc exchange activity on RhoA; Tctex-1 competes with 14-3-3 for Lfc binding. | PMID:19667072 | Molecular and cellular biology |
| 2009 | High | GEF-H1 directly interacts with paracingulin (at epithelial junctions), and paracingulin depletion increases RhoA activity; paracingulin is required for efficient recruitment of GEF-H1 to junctions, linking junction assembly to RhoA regulation. | PMID:18653465 | Molecular biology of the cell |
| 2009 | Medium | GEF-H1 interacts with the Y-box transcription factor ZONAB/DbpA; GEF-H1 overexpression induces nuclear ZONAB accumulation and activates ZONAB-dependent transcription; GEF-H1 and ZONAB together are required for RhoA-dependent cyclin D1 expression. | PMID:19730435 | EMBO reports |
| 2009 | High | GEF-H1 is a component of the AMPA receptor complex in the brain; it is enriched in the postsynaptic density, colocalizes with GluR1 at spines, and negatively regulates spine density and length through RhoA; AMPA-R-dependent changes in spine morphology are abolished by GEF-H1 knockdown. | PMID:19208802 | Proceedings of the National Academy of Sciences of the United States of America |
| 2009 | High | TNF-α activates GEF-H1 via ERK-mediated phosphorylation of Thr678 in tubular epithelial cells, leading to RhoA activation, MLC phosphorylation, and increased paracellular permeability; GEF-H1 was identified as a TNF-α-activated RhoGEF using a RhoG17A affinity precipitation/mass spectrometry approach. | PMID:19261619 | The Journal of biological chemistry |
| 2010 | High | TGF-β transcriptionally upregulates GEF-H1 in a Smad4-dependent manner in RPE cells; GEF-H1 induction leads to RhoA activation and is required for TGF-β-induced α-SMA expression and cell migration. | PMID:20089843 | Molecular biology of the cell |
| 2010 | High | Lfc (ARHGEF2) and p114-RhoGEF mediate Wnt-3a/Dishevelled-induced RhoA activation and neurite retraction; Lfc and p114-RhoGEF physically bind Dvl and Daam1, and their knockdown suppresses Dvl- and Wnt-3a-induced RhoA activation and neurite retraction. | PMID:20810787 | Molecular biology of the cell |
| 2011 | High | Mechanical force on integrins triggers GEF-H1 catalytic activation via ERK downstream of a FAK–Ras signaling cascade, and recruits GEF-H1 to adhesion complexes; this is distinct from LARG activation (which occurs via Fyn), and both GEFs are required for force-induced cellular stiffening (reinforcement). | PMID:21572419 | Nature cell biology |
| 2011 | High | GEF-H1 is required for NOD2- and RIP2-dependent NF-κB activation; GEF-H1 functions downstream of NOD2 as part of RIP2-containing signaling complexes and mediates Src tyrosine kinase-dependent phosphorylation of RIP2; the 3020insC NOD2 variant associated with Crohn's disease fails to activate this GEF-H1-dependent pathway. | PMID:21887730 | Inflammatory bowel diseases |
| 2011 | High | PAR1b/MARK2 phosphorylates GEF-H1 at Ser885 and Ser959, inhibiting GEF-H1 RhoA-specific GEF activity and suppressing stress fiber formation; Par1b-phosphorylated GEF-H1 loses the ability to activate RhoA. | PMID:22072711 | The Journal of biological chemistry |
| 2011 | High | Par1b/MARK2 phosphorylates GEF-H1 at multiple conserved serine residues, releasing GEF-H1 from microtubules and abrogating GEF-H1-induced microtubule stabilization/acetylation; non-phosphorylatable GEF-H1 (3SA mutant) remains statically bound to microtubules as visualized by live-cell imaging. | PMID:21513698 | Biochemical and biophysical research communications |
| 2011 | High | Calpain-6 (CAPN6) co-localizes and physically interacts with GEF-H1 on microtubules; CAPN6 knockdown causes GEF-H1 to translocate from microtubules to the lamellipodial region and interact with Rac1, leading to Rac1 activation, increased cell migration, and lamellipodial protrusion; this Rac1 activation requires GEF-H1. | PMID:21406564 | Journal of cell science |
| 2012 | High | GEF-H1 directly binds exocyst component Sec5 in a RalA GTPase-dependent manner; this interaction promotes RhoA activation, regulates exocyst assembly/localization, and is required for exocytosis. | PMID:22898781 | Developmental cell |
| 2012 | Medium | Non-centrosomal microtubules anchored by CAMSAP3 (Nezha) preferentially sequester GEF-H1; CAMSAP3 depletion increases the soluble pool of GEF-H1, upregulates RhoA activity, and promotes actin stress fiber formation; detyrosinated microtubules do not efficiently interact with GEF-H1. | PMID:23432781 | Genes to cells |
| 2012 | Medium | GEFH1 binds the BAR domain of ASAP1 (validated by endogenous Co-IP) and colocalizes with ASAP1 in podosomes; GEFH1 overexpression inhibits podosome assembly and ASAP1 GAP activity, while GEFH1 knockdown increases podosome assembly rate. | PMID:21352810 | Biochemical and biophysical research communications |
| 2012 | Medium | Microtubule stability is diminished by a stiff 3D extracellular matrix, leading to activation of GEF-H1 and RhoA; GEF-H1 loss decreases cell contraction and invasion through 3D matrices; MEK/ERK pathway does not contribute to stiffness-induced GEF-H1 activation in this context. | PMID:22593214 | Molecular biology of the cell |
| 2013 | High | GEF-H1 is essential for RIG-I-like receptor sensing of foreign RNA; upon microtubule release GEF-H1 activation controls RIG-I- and Mda5-dependent IRF3 phosphorylation and IFN-β induction; Arhgef2−/− mice show pronounced antiviral signaling defects against encephalomyocarditis virus and influenza A virus. | PMID:24270516 | Nature immunology |
| 2013 | High | TNF-α sequentially activates Rac (via GEF-H1 phosphorylation at S885) and then RhoA (via GEF-H1 T678 phosphorylation) through a single exchange factor; GEF-H1-mediated Rac activation drives TACE/ADAM17, which transactivates EGFR/ERK and leads to T678 phosphorylation and RhoA activation. | PMID:23389627 | Molecular biology of the cell |
| 2014 | High | GEF-H1 acts as an adaptor linking PP2A B' subunits to the scaffold protein KSR-1, mediating dephosphorylation of KSR-1 S392 and activating MAPK signaling downstream of oncogenic RAS; this role is independent of GEF-H1's RhoGEF catalytic activity. | PMID:24525234 | Cancer cell |
| 2014 | High | MARK3 (activated by LKB1) phosphorylates ARHGEF2 at Ser151, generating a 14-3-3 binding site that disrupts the ARHGEF2–DYNLT1 (Tctex-1) interaction and dissociates ARHGEF2 from microtubules; this stimulates RhoA activation and stress fiber/focal adhesion formation; PP2A dephosphorylates Ser151 to restore the inhibited state. | PMID:29089450 | Science signaling |
| 2014 | Medium | RASSF1A stimulates cofilin/PP2A-mediated dephosphorylation of GEF-H1, thereby activating GEF-H1 to activate the antimetastatic GTPase RhoB; RASSF1A loss reduces GEF-H1-mediated RhoB activation and increases nuclear YAP, promoting EMT and invasion. | PMID:26759237 | Cancer research |
| 2014 | High | GEF-H1 mediates GEF-H1/RhoA activation induced by LPA or thrombin (GPCR ligands) through a mechanism independent of microtubule depolymerization: Gα directly binds GEF-H1 and displaces it from Tctex-1, while Gβγ binds Tctex-1 and disrupts its dynein intermediate chain interaction; full GEF-H1 activation requires subsequent PP2A-mediated dephosphorylation of Ser885. | PMID:25209408 | Nature communications |
| 2014 | High | GEF-H1 functions in apical constriction and cell intercalation during Xenopus neural tube closure; GEF-H1 depletion (morpholino) causes neural tube defects with impaired MLC phosphorylation, Rab11 and F-actin accumulation; overexpressed GEF-H1 induces ROCK-dependent ectopic apical constriction. | PMID:24681784 | Journal of cell science |
| 2015 | High | VopO, a Vibrio parahaemolyticus type III effector, directly binds GEF-H1 via an alpha-helix region; this interaction is required for T3SS2-dependent RhoA-ROCK pathway activation and stress fiber formation; GEF-H1 binding activity of VopO correlates with its stress fiber-inducing and epithelial barrier disruption capacity. | PMID:25738744 | PLoS pathogens |
| 2015 | High | RalB (but not RalA) promotes TGFβ-induced cancer cell dissemination via GEF-H1; RalB acts through the exocyst subunit Sec5 to promote GEF-H1-dependent RhoA activation and actomyosin contractility; uncoupling Sec5 from GEF-H1 impairs RhoA activation and traction force generation. | PMID:26152517 | Scientific reports |
| 2016 | Medium | The TRPC3 channel mediates mechanical stress/TGFβ-induced GEF-H1 activation in cardiomyocytes and cardiac fibroblasts; TRPC3 functionally interacts with microtubule-associated Nox2, and Nox2 inhibition attenuates mechanical stretch-induced GEF-H1 activation; TRPC3 inhibition suppresses GEF-H1-mediated RhoA activation and fibrotic responses. | PMID:27991560 | Scientific reports |
| 2016 | High | Autophagy degrades GEF-H1 via a p62-dependent mechanism; in autophagy-deficient cells (Atg5/Atg7/Ulk1 KO), GEF-H1 accumulates, RhoA activity increases, and cells switch to amoeboid migration; GEF-H1 silencing in Atg5 KO cells reverts this phenotype. | PMID:27120804 | Oncotarget |
| 2016 | High | PP2A regulatory subunit PPP2R2A binds, dephosphorylates, and activates GEF-H1 at Ser885, leading to increased RhoA-GTP levels and ROCK activity in T cells, promoting Th1 and Th17 differentiation. | PMID:33762326 | Journal of immunology |
| 2017 | High | Vimentin intermediate filaments regulate actin stress fiber assembly via GEF-H1; vimentin loss induces phosphorylation of GEF-H1 at Ser886, promoting RhoA activity and stress fiber assembly; this requires intact vimentin filaments (not unit-length forms). | PMID:28096473 | Journal of cell science |
| 2017 | High | Homozygous frameshift mutation in ARHGEF2 causes intellectual disability and midbrain-hindbrain malformation; loss of ARHGEF2 perturbs progenitor cell differentiation, shifts mitotic spindle plane orientation toward symmetric divisions, and reduces RhoA/ROCK/MLC pathway activation; Arhgef2 mutant mice recapitulate the human malformation with aberrant precerebellar neuron migration. | PMID:28453519 | PLoS genetics |
| 2019 | High | GEF-H1 contains an autoinhibitory sequence; live-cell biosensor imaging reveals that autoinhibited GEF-H1 localizes to microtubules, while MT depolymerization at the cell cortex activates GEF-H1 in a ~5-µm peripheral band; Src phosphorylation activates GEF-H1 in a narrower ~0-2 µm band at the cell edge in coordination with protrusions. | PMID:31420453 | The Journal of cell biology |
| 2019 | High | GEF-H1 is specifically released upon microtubule destabilization in dendritic cells and drives DC maturation via JNK pathway and AP-1/ATF transcriptional response; GEF-H1 promotes cross-presentation of tumor antigens to CD8 T cells; Arhgef2−/− mice show impaired anti-tumor immunity. | PMID:31553907 | Cell reports |
| 2019 | High | GEF-H1 is required for IKKε-mediated phosphorylation and activation of IRF5 in response to microbial muramyl-dipeptides; GEF-H1 functions in a microtubule-based peptidoglycan recognition system independent of NOD-like receptors; deletion or dominant-negative GEF-H1 prevents IKKε and IRF5 activation and host defenses against Listeria monocytogenes. | PMID:30902986 | Nature communications |
| 2020 | High | BNIP-2 (a BCH domain protein) binds both GEF-H1 and RhoA and traffics with kinesin-1 on microtubules; upon microtubule disassembly, the BNIP-2–GEF-H1 interaction increases and BNIP-2 scaffolds GEF-H1–RhoA coupling; BNIP-2 depletion reduces RhoA activation and cell rounding after nocodazole treatment. | PMID:32789168 | Science advances |
| 2020 | Medium | PKA and PKG phosphorylate GEF-H1 at Ser886 in platelets, stimulating 14-3-3β binding and promoting GEF-H1 association with microtubules, thereby inhibiting GEF-H1 GEF function; microtubule disruption increases RhoA-GTP levels in platelets, confirming GEF-H1's role in platelet RhoA regulation. | PMID:32692911 | Journal of thrombosis and haemostasis |
| 2021 | High | YTHDF1 binds m6A sites on ARHGEF2 mRNA, enhancing ARHGEF2 translation; increased ARHGEF2 protein activates RhoA signaling and promotes CRC tumor growth and metastasis; siRNA-LNP delivery targeting ARHGEF2 suppresses tumor growth in vivo. | PMID:34968454 | Gastroenterology |
| 2021 | Medium | Glutamine deficiency triggers macropinocytosis in pancreatic cancer-associated fibroblasts via CaMKK2-AMPK signaling and ARHGEF2; ARHGEF2 is required for this stromal macropinocytic response, which supplies amino acids to both CAFs and tumor cells. | PMID:33653692 | Cancer discovery |
| 2021 | High | NEK9 directly phosphorylates ARHGEF2, activating RhoA and promoting gastric cancer cell motility; NEK9 is transcriptionally suppressed by miR-520f-3p, which is itself repressed by IL-6/STAT3 signaling, placing ARHGEF2 phosphorylation downstream of the IL-6-STAT3-NEK9 pathway. | PMID:33500736 | Theranostics |
| 2021 | High | Bartonella effector BepC binds GEF-H1 via its N-terminal FIC domain (in a non-catalytic manner) and re-localizes GEF-H1 from microtubules to the plasma membrane; this GEF-H1-dependent mechanism activates RhoA/ROCK and triggers actin stress fiber formation and cell fragmentation in migrating endothelial cells. | PMID:33508040 | PLoS pathogens |
| 2022 | Medium | Peptide inhibitors designed against the GEF-H1 autoregulatory C-terminal domain block RhoA/GEF-H1 binding in vitro and inhibit GEF-H1-dependent TGFβ-induced fibrosis, LPS-stimulated endothelial barrier disruption, and cell migration; the most potent inhibitor inhibits blood vessel leakage and retinal inflammation in an in vivo retinal disease model. | PMID:35681428 | Cells |
| 2023 | High | HUNK kinase directly phosphorylates GEF-H1 at Ser645, which activates RhoA and leads to cascading phosphorylation of LIMK-1/CFL-1, stabilizing F-actin and inhibiting EMT in colorectal cancer. | PMID:37193711 | Cell death & disease |
| 2012 | Medium | FAM123A binds to ARHGEF2 via a microtubule-associated interaction, and this binding inhibits ARHGEF2 GEF activity; FAM123A depletion increases actomyosin contractility, focal adhesion size, and decreases cell migration in an ARHGEF2-dependent manner. | PMID:22949735 | Science signaling |
| 2011 | High | hPTTG1 transcriptionally activates GEF-H1 gene expression by directly binding and activating the GEF-H1 promoter (validated by luciferase reporter and ChIP); hPTTG1 knockdown decreases GEF-H1 expression and RhoA activation, reducing breast cancer cell motility and invasion, rescued by GEF-H1 re-expression. | PMID:22002306 | Oncogene |
| 2016 | Medium | Tension on JAM-A activates RhoA via GEF-H1 (and p115 RhoGEF) through PI3K-mediated GEF-H1 activation; FAK/ERK further regulate GEF-H1; phosphorylation of JAM-A at Ser284 is required for this RhoA activation in response to tension. | PMID:26985018 | Molecular biology of the cell |
| 2016 | Medium | ONCOGENIC KRAS transcriptionally activates ARHGEF2 through a minimal RAS-responsive promoter regulated by ELK1, ETS1, SP1, SP3 (positive) and RREB1 (negative); RREB1 knockdown increases ARHGEF2 expression and extends RhoA activation duration; ARHGEF2 rescues SP3 loss-of-function invasion/migration defects. | PMID:27835861 | Oncotarget |

## Citations

- PMID:11912491
- PMID:14970201
- PMID:15318166
- PMID:15827085
- PMID:15866167
- PMID:15976019
- PMID:15996550
- PMID:16778209
- PMID:16917499
- PMID:17488622
- PMID:18211802
- PMID:18287519
- PMID:18653465
- PMID:19043560
- PMID:19208802
- PMID:19261619
- PMID:19448628
- PMID:19667072
- PMID:19730435
- PMID:20089843
- PMID:20463241
- PMID:20810787
- PMID:21352810
- PMID:21406564
- PMID:21513698
- PMID:21572419
- PMID:21887730
- PMID:22002306
- PMID:22072711
- PMID:22593214
- PMID:22898781
- PMID:22949735
- PMID:23389627
- PMID:23432781
- PMID:24270516
- PMID:24525234
- PMID:24681784
- PMID:25209408
- PMID:25738744
- PMID:26152517
- PMID:26759237
- PMID:26985018
- PMID:27120804
- PMID:27835861
- PMID:27991560
- PMID:28096473
- PMID:28453519
- PMID:29089450
- PMID:30902986
- PMID:31420453
- PMID:31553907
- PMID:32692911
- PMID:32789168
- PMID:33500736
- PMID:33508040
- PMID:33653692
- PMID:33762326
- PMID:34968454
- PMID:35681428
- PMID:37193711
- PMID:7629163
- PMID:8910315
- PMID:9857026
- PMID:9890991
