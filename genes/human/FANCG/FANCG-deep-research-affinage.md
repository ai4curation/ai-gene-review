---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCG
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: O15287
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 30
citation_count: 30
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCG (human)

## Current model (mechanistic narrative)

FANCG (identical to XRCC9) is a tetratricopeptide-repeat (TPR) scaffold protein of the Fanconi anemia (FA) DNA-repair pathway, originally identified by its ability to complement the mitomycin C-, cisplatin-, and crosslink-hypersensitive phenotype and chromosomal instability of FA-G cells [PMID:9806548, PMID:9256465]. Within the FA nuclear core complex, FANCG directly binds FANCA through an arginine-rich motif at the FANCA N-terminus and its own C-terminal/TPR contact surfaces, mutually stabilizing the two proteins, promoting nuclear import of the complex, and additionally recruiting FANCC via its C-terminus [PMID:10373536, PMID:10567393, PMID:11050007, PMID:10961856]; cryo-EM of the FANCA-FANCG complex shows FANCG making independent contacts with the FANCA N-terminal region and C-terminal HEAT solenoid, both required for FANCA nuclear localization [PMID:32002546]. Its TPR motifs (notably TPR1, 2, 5, 6) constitute the protein-protein interaction scaffold needed for assembly of both the core complex and downstream complexes [PMID:14697762, PMID:20450923]. The assembled core complex is required for damage-induced monoubiquitination of FANCD2, the central activating event of the pathway [PMID:11751423, PMID:11719385]. Independently of core-complex function, FANCG nucleates a discrete D1-D2-G-X3 complex with BRCA2/FANCD1, FANCD2, and the RAD51 paralog XRCC3, an assembly that depends on phosphorylation of FANCG at Ser7 and supports homologous-recombination repair of interstrand crosslinks [PMID:12915460, PMID:16621732, PMID:18212739], consistent with FANCG being required for efficient HR repair of double-strand breaks [PMID:12861027]. FANCG is further phosphorylated at Ser383/Ser387 by Cdc2 during mitosis [PMID:15367677] and modified by K63-linked polyubiquitin chains that recruit the Rap80-BRCA1 complex for HR repair while being dispensable for FANCD2 monoubiquitination [PMID:25132264], and it links the pathway to the ERCC1-XPF endonuclease that performs ICL unhooking through its TPR motifs [PMID:20518486]. A mitochondrial pool of FANCG, separable from its nuclear repair function, protects against oxidative stress and supports FANCJ helicase iron-sulfur integrity via frataxin [PMID:32989015].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0005198 structural molecule activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1643685 Disease
- **partners:** FANCA, FANCC, FANCF, BRCA2, XRCC3, FANCD2, ERCC1, XPF
- **complexes:** FA nuclear core complex, D1-D2-G-X3 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1998 | High | FANCG is identical to XRCC9, a gene that complements the MMC-sensitive Chinese hamster mutant UV40, implicating FANCG in DNA post-replication repair or cell cycle checkpoint control. | PMID:9806548 | Nature genetics |
| 1997 | High | XRCC9/FANCG partially corrects hypersensitivity of CHO UV40 cells to mitomycin C, cisplatin, ethyl methanesulfonate, UV, and gamma-radiation, and almost fully corrects spontaneous chromosomal aberrations, placing FANCG in a postreplication repair or cell cycle checkpoint function. | PMID:9256465 | Proceedings of the National Academy of Sciences of the United States of America |
| 1999 | High | FANCG protein is required for binding of FANCA and FANCC proteins to each other, and is itself a component of a nuclear protein complex containing FANCA and FANCC; the amino-terminal region of FANCA is required for FANCG binding. | PMID:10373536 | Molecular and cellular biology |
| 1999 | High | FANCG localizes to both cytoplasm and nucleus, and forms a physical complex with FANCA both in vivo and in vitro; the FANCA/FANCG complex is absent in FA-A and FA-G cell lines but present in FA-D and FA-E cells, indicating group-specific assembly requirements. | PMID:10468606 | Proceedings of the National Academy of Sciences of the United States of America |
| 1999 | High | The FANCA-FANCG interaction domain maps to amino acids 18-29 of FANCA (arginine-rich motif RRRAWAELLAG) and to two non-contiguous carboxy-terminal domains of FANCG (aa 400-475 and 585-622); mutations in this domain abolish complementation of MMC sensitivity, demonstrating that nuclear FANCA-FANCG complexes are required for cellular resistance to MMC. | PMID:10567393 | The Journal of biological chemistry |
| 2000 | High | FANCF forms a nuclear complex with FANCA, FANCC, and FANCG; each FA protein (except FANCD) is required for these complexes to form, as demonstrated by absence of interactions in the corresponding complementation group cell lines. | PMID:11063725 | Human molecular genetics |
| 2000 | High | FANCG and FANCA stabilize each other: correction of FA-G cells with FANCG cDNA prolongs FANCA half-life and increases nuclear accumulation of the FA protein complex; reciprocally, FANCA correction increases FANCG half-life. FANCG binds the amino-terminal NLS of FANCA, and this binding is required for nuclear translocation of the complex. | PMID:11050007 | Blood |
| 2000 | High | The amino-terminal two-thirds of FANCG (aa 1-428) binds to the FANCA NLS, but the carboxy terminus of FANCG is additionally required for binding FANCC and for functional complementation of FA-G cells; thus FANCG binding to FANCA is necessary but not sufficient for full FANCG activity. | PMID:10961856 | Blood |
| 2000 | Medium | Yeast two-hybrid analysis confirms a strong direct interaction between full-length FANCA and FANCG proteins, and a weak interaction between FANCA and FANCC. | PMID:10627486 | Blood |
| 2001 | High | FANCG-deficient CHO mutants (NM3 and UV40) fail to express the monoubiquitinated form of FANCD2 (FANCD2-L); restoration of FANCG by cDNA transfection restores FANCD2-L expression, demonstrating FANCG is required for FANCD2 monoubiquitination. | PMID:11751423 | Carcinogenesis |
| 2001 | High | Disruption of murine Fancg results in failure to monoubiquitinate FANCD2 in response to ionizing radiation in primary lymphocytes, confirming Fancg's essential role in the FA pathway upstream of FANCD2 activation. | PMID:11719385 | Blood |
| 2001 | Medium | alphaIISp (nonerythroid alpha spectrin), FANCA, FANCC, and FANCG proteins bind to DNA containing psoralen interstrand cross-links, as demonstrated by DNA affinity chromatography from HeLa cell nuclei; purified bovine brain spectrin binds cross-linked DNA directly. | PMID:11401546 | Biochemistry |
| 2002 | Medium | FANCG interacts with cytochrome P450 2E1 (CYP2E1) by yeast two-hybrid; FANCG localizes to cytoplasm and nucleus, with increased cytoplasmic staining after MMC treatment; complementation of FA-G cells with FANCG decreases CYP2E1 levels and reduces oxidative DNA damage (8-oxoG). | PMID:11756225 | Carcinogenesis |
| 2003 | High | FANCG directly interacts with two separate sites in BRCA2 (flanking the BRC repeats) by yeast two-hybrid; FANCG co-immunoprecipitates with BRCA2 from human cells; FANCG co-localizes in nuclear foci with BRCA2 and RAD51 following MMC-induced DNA damage. | PMID:12915460 | Human molecular genetics |
| 2003 | High | FANCG is required for efficient homologous recombination (HR) repair of I-SceI-induced chromosomal double-strand breaks; FANCG-deficient DT40 cells show ~9-fold decreased HR repair efficiency and mild decrease in gene targeting efficiency. | PMID:12861027 | Molecular and cellular biology |
| 2004 | High | FANCG contains at least seven tetratricopeptide repeat (TPR) motifs; targeted missense mutagenesis disrupting TPR1, TPR2, TPR5, and TPR6 causes loss of FANCG function (failure to complement FA-G cells) correlated with loss of FANCA binding, establishing TPR motifs as functional protein-protein interaction scaffolds within FANCG. | PMID:14697762 | DNA repair |
| 2004 | High | FANCG is phosphorylated at serine 7; mutation of Ser7 to Ala (S7A) abolishes functional complementation of FA-G cells, causes aberrant chromatin localization (globule formation), and fails to abrogate internuclear bridges, despite S7A retaining ability to bind and stabilize FANCA and FANCC. Phosphoserine 7 was mapped by mass spectrometry. | PMID:15299017 | The Journal of biological chemistry |
| 2004 | High | FANCG is phosphorylated at serines 383 and 387 during mitosis by Cdc2 kinase; mutation of S383A and S387A abolishes mitotic phosphorylation and impairs FANCG's ability to complement FA-G human and hamster cells; S387A abolishes Cdc2-mediated phosphorylation of FANCG fusion protein. | PMID:15367677 | Molecular and cellular biology |
| 2001 | Medium | FANCG is a phosphoprotein in both nuclear and cytoplasmic fractions; TNF-alpha treatment induces FANCG protein expression and increases nuclear FANCA/FANCG complex levels; IKK-2 inactivation modulates FANCG expression, placing TNF-alpha/NF-kB signaling upstream of FANCG regulation. | PMID:11181053 | Biochemical and biophysical research communications |
| 2006 | High | FANCG directly interacts with the RAD51 paralog XRCC3 by yeast two-hybrid; this interaction is disrupted by the FA-G patient-derived mutation L71P; FANCG co-immunoprecipitates with both XRCC3 and BRCA2 independently of other core complex FA proteins; XRCC3 and BRCA2 co-precipitate in a FANCG-dependent manner. | PMID:16621732 | DNA repair |
| 2008 | High | FANCG promotes formation of a novel protein complex (D1-D2-G-X3) comprising BRCA2/FANCD1, FANCD2, FANCG, and XRCC3; expression of FANCG but not other core complex proteins is required for BRCA2-FANCD2 co-precipitation; phosphorylation of FANCG Ser7 is specifically required for co-precipitation with BRCA2, XRCC3, and FANCD2, and for direct BRCA2-FANCD2 interaction; FANCG and XRCC3 are epistatic for sensitivity to DNA crosslinking agents in DT40 cells. | PMID:18212739 | Oncogene |
| 2009 | Medium | FANCG interacts directly with the SH3 domain of alphaII spectrin (alphaIISp) through a consensus SH3-binding motif in FANCG; site-directed mutagenesis of this motif disrupts the interaction; FANCC and FANCF, which lack SH3-binding motifs, do not interact with the alphaIISp SH3 domain. | PMID:19102630 | Biochemistry |
| 2010 | Medium | FANCG binds directly to ERCC1 (strong affinity) and XPF (moderate affinity) via its TPR motifs; TPRs 1, 3, 5, and 6 are required for FANCG-ERCC1 binding; ERCC1 interacts with FANCG through its central domain (distinct from its XPF-binding region), establishing a direct link between FANCG and the ERCC1-XPF endonuclease that performs ICL unhooking. | PMID:20518486 | Biochemistry |
| 2010 | High | Mutation of FANCG TPR1, TPR2, TPR5, or TPR6 abolishes in vivo binding to BRCA2, XRCC3, FANCA, and FANCF, fails to restore FANCD2 monoubiquitylation, and fails to complement MMC and phleomycin hypersensitivity; FANCG functions as a mediator of protein-protein interactions essential for both FA core complex and D1-D2-G-X3 complex assembly. | PMID:20450923 | Mutation research |
| 2014 | High | FANCG is modified by K63-linked polyubiquitin chains in response to DNA damage; K63 ubiquitination of FANCG (at K182, K258, K347) is required for FANCG interaction with the Rap80-BRCA1 complex and for HR repair of ICLs; K63Ub-FANCG is dispensable for FANCD2 monoubiquitination; BRCC36 deubiquitinase removes K63Ub from FANCG in vitro and in vivo. | PMID:25132264 | Oncogene |
| 2020 | High | Cryo-EM structures of Xenopus laevis FANCA alone (3.35 and 3.46 Å) and two distinct FANCA-FANCG complexes (4.59 and 4.84 Å) reveal that FANCA CTD adopts an arc-shaped solenoid; FANCG makes independent contacts with either the FANCA C-terminal HEAT repeats or the N-terminal region; mutations disrupting either interaction prevent FANCA nuclear localization and FA pathway function. | PMID:32002546 | Nucleic acids research |
| 2020 | Medium | An FANCG variant (p.Arg22Pro, c.65G>C) that loses mitochondrial localization retains nuclear DNA repair function and FANCD2 monoubiquitination but fails to protect mitochondria from oxidative stress; loss of mitochondrial FANCG causes transcriptional downregulation of frataxin (FXN) and resulting iron deficiency of the FANCJ helicase. | PMID:32989015 | Molecular and cellular biology |
| 2021 | Medium | Fancg deficiency causes abnormal primordial germ cell (PGC) migration in mouse embryos: Fancg-/- PGCs show increased random motility, delayed migration to genital ridges, increased cell death, and PGC attrition starting at E9.5; RAC1 inhibition mitigates the abnormal migratory pattern in Fancg-/- PGCs. | PMID:34368842 | Human molecular genetics |
| 2011 | Medium | Fancg is required for hematopoietic stem cell (HSC) quiescence, homing, and engraftment: Fancg-/- HSCs show reduced LSK compartment, loss of quiescence, impaired CXCL12-directed migration in vitro, and defective BM homing after transplantation; key genes involved in HSC self-renewal, quiescence, and migration are dysregulated in Fancg-/- LSK cells. | PMID:21968513 | Human molecular genetics |
| 2009 | Medium | Loss of functional Fancg in mesenchymal stem/progenitor cells (MSPCs) causes defective MSPC proliferation and impaired ability to support hematopoietic stem cell (HSPC) adhesion and engraftment; transplantation of wild-type but not Fancg-/- MSPCs into Fancg-/- recipients restores HSPC engraftment and BM cellularity. | PMID:19129541 | Blood |

## Citations

- PMID:10373536
- PMID:10468606
- PMID:10567393
- PMID:10627486
- PMID:10961856
- PMID:11050007
- PMID:11063725
- PMID:11181053
- PMID:11401546
- PMID:11719385
- PMID:11751423
- PMID:11756225
- PMID:12861027
- PMID:12915460
- PMID:14697762
- PMID:15299017
- PMID:15367677
- PMID:16621732
- PMID:18212739
- PMID:19102630
- PMID:19129541
- PMID:20450923
- PMID:20518486
- PMID:21968513
- PMID:25132264
- PMID:32002546
- PMID:32989015
- PMID:34368842
- PMID:9256465
- PMID:9806548
