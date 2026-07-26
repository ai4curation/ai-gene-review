---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCL
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q9NW38
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 22
citation_count: 22
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCL (human)

## Current model (mechanistic narrative)

FANCL is the catalytic RING-type E3 ubiquitin ligase subunit of the Fanconi anemia core complex, partnering with the E2 enzyme UBE2T to monoubiquitinate FANCD2 and FANCI and thereby drive homologous-recombination repair of DNA interstrand crosslinks [PMID:19111657, PMID:17352736]. Its crystal structure resolves a tripartite architecture in which the central DRWD/URD domain binds the FANCD2/FANCI substrate dimer while the C-terminal RING domain mediates E2 recruitment, and an extensive electrostatic/hydrophobic RING–UBE2T interface confers selective recruitment of UBE2T over other E2 enzymes [PMID:20154706, PMID:24389026]. Reconstitution shows FANCL and UBE2T are sufficient to monoubiquitinate FANCD2, with FANCI both stimulating the reaction and restricting modification to the correct lysine (K561 on FANCD2; K523 on FANCI) [PMID:19111657, PMID:19589784]; the N-terminal ELF domain additionally binds free ubiquitin via the Ile44 patch to promote efficient damage-induced FANCD2 monoubiquitination in cells [PMID:26149689]. FANCL-dependent monoubiquitination is required for FANCD2 chromatin and nuclear-matrix association and for HR repair of induced chromosomal breaks, an epistatic relationship conserved from Drosophila to vertebrates [PMID:14712086, PMID:17352736, PMID:16860002]. A catalytic-cysteine knock-in mouse establishes that loss of RING E3 ligase activity alone reproduces all major Fanconi anemia phenotypes, and FANCL variants causing protein destabilization or cytoplasmic mislocalization underlie premature ovarian insufficiency [PMID:41259745, PMID:32048394]. Beyond DNA repair, FANCL extends K11-linked non-proteolytic ubiquitin chains on β-catenin to enhance Wnt target transcription in hematopoietic stem/progenitor cells [PMID:22653977], supports Parkin-mediated mitophagy through a ubiquitin ligase-independent mitochondrial function [PMID:35644338], and is required for primordial germ cell proliferation and oocyte survival through meiosis [PMID:12417526, PMID:20661450].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein, GO:0031386 protein tag activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-392499 Metabolism of proteins, R-HSA-162582 Signal Transduction, R-HSA-9612973 Autophagy, R-HSA-1474165 Reproduction
- **partners:** UBE2T, FANCD2, FANCI, UBE2W, CTNNB1, GGN, AXIN1
- **complexes:** Fanconi anemia core complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | FANCL acts as an E3 ubiquitin ligase that, together with the E2-conjugating enzyme Ube2t, is sufficient to monoubiquitinate FANCD2 in a minimal reconstituted system. A conserved RWD-like domain in FANCL stimulates monoubiquitination, and addition of FANCI enhances the reaction and restricts it to the correct in vivo lysine residue on FANCD2 (K561). | PMID:19111657 | Molecular cell |
| 2004 | Medium | FANCL (PHF9), but not BRCA1, is the likely E3 ubiquitin ligase responsible for FANCD2 monoubiquitination. In FANCL-mutant cells, monoubiquitinated FANCD2 is absent from chromatin and nuclear matrix fractions, whereas non-ubiquitinated FANCD2 resides in the soluble fraction, demonstrating that FANCL-dependent monoubiquitination is required for FANCD2 chromatin association. | PMID:14712086 | Cell cycle (Georgetown, Tex.) |
| 2010 | High | Crystal structure of FANCL at 3.2 Å reveals three domains: an N-terminal E2-like fold (ELF domain), a novel double-RWD (DRWD) domain, and a C-terminal RING domain. Binding assays show the DRWD domain (not ELF) is responsible for substrate (FANCD2/FANCI) binding, while the RING domain mediates E2 (Ube2T) interaction. | PMID:20154706 | Nature structural & molecular biology |
| 2014 | High | Crystal structure of the FANCL RING domain in complex with Ube2T reveals an extensive network of specific electrostatic and hydrophobic interactions beyond the generic E3–E2 interface, and mutagenesis shows these specific interactions are required for selective recruitment of Ube2T over other E2 enzymes by FANCL. | PMID:24389026 | Structure (London, England : 1993) |
| 2011 | High | Structure of the central (DRWD/URD) domain of human FANCL confirms conservation with Drosophila FANCL. Mutational analysis identifies residues in the DRWD domain required for binding FANCD2 and FANCI substrates, and a separate region required for Ube2T binding. | PMID:21775430 | The Journal of biological chemistry |
| 2006 | High | The WD40 repeats (not the PHD/RING domain) of FANCL are required for interaction with other FA core complex subunits. The PHD domain is dispensable for core complex incorporation but is required for FANCD2 monoubiquitination; a conserved tryptophan in the PHD analogous to the c-CBL RING finger is required for in vitro auto-ubiquitination and in vivo FANCD2 monoubiquitination. | PMID:16474167 | The Journal of biological chemistry |
| 2007 | High | FANCL physically interacts with FANCD2 via its PHD domain (co-immunoprecipitation in 293T cells and yeast two-hybrid). FANCL is required for FANCD2 monoubiquitination and focus formation in DT40 cells, and loss of FANCL (or FANCD2 monoubiquitination) causes quantitatively identical defects in homologous recombination repair of I-SceI-induced chromosomal breaks. | PMID:17352736 | Genes to cells : devoted to molecular & cellular mechanisms |
| 2009 | High | The UBE2T–FANCL pair can monoubiquitinate FANCI on Lys-523 in vitro. FANCI binds branched DNA structures through its C-terminal fragment, a binding activity that likely positions it as a substrate. | PMID:19589784 | The Journal of biological chemistry |
| 2010 | Medium | UBE2W interacts with the PHD domain of FANCL (the PHD domain is necessary and sufficient for this interaction) and catalyzes monoubiquitination of the FANCL PHD domain in vitro. UBE2W overexpression promotes FANCD2 monoubiquitination in cells, and UBE2W knockdown reduces UV-induced (but not MMC-induced) FANCD2 monoubiquitination, indicating UBE2W regulates FANCD2 monoubiquitination through FANCL by a mechanism distinct from UBE2T. | PMID:21229326 | Molecules and cells |
| 2015 | High | The N-terminal ELF domain of FANCL mediates a non-covalent interaction with ubiquitin via the canonical Ile44 patch on ubiquitin. This interaction is not required for FANCD2 monoubiquitination in vitro, nor for core complex recognition or Ube2T binding, but is required for efficient DNA damage-induced FANCD2 monoubiquitination in vertebrate cells, indicating a regulatory in vivo function for ubiquitin binding by the ELF domain. | PMID:26149689 | The Journal of biological chemistry |
| 2012 | Medium | FANCL ubiquitinates β-catenin with atypical lysine-11 ubiquitin chain extension (non-proteolytic), enhancing β-catenin nuclear activity and transcription of Wnt targets c-Myc and Cyclin D1. FANCL-deficient cells show diminished β-catenin activation, and suppression of FANCL in human CD34+ stem/progenitor cells reduces β-catenin-active cells and inhibits multilineage progenitor expansion. | PMID:22653977 | Blood |
| 2013 | Medium | FANCL protein is constitutively targeted for proteasomal degradation via K48-linked polyubiquitination. The ELF (E2-like fold) domain may direct this polyubiquitination. FANCL is stabilized in a complex with axin1 when GSK-3β is overexpressed, and constitutively active Akt (myristoylated) increases FANCL steady-state levels by reducing K48-linked polyubiquitination. Phosphorylated (acidic) forms of FANCL are not subject to polyubiquitination. | PMID:23783032 | Molecular biology of the cell |
| 2017 | Medium | Arsenite (As3+) binds directly to the PHD/RING finger domain of FANCL both in vitro and in cells. This binding compromises FANCL-mediated FANCD2 ubiquitination in cells, reduces FANCD2 chromatin recruitment to DNA damage sites, and renders cells more sensitive to DNA interstrand cross-linking agents. | PMID:28535027 | ACS chemical biology |
| 2019 | Medium | A small-molecule inhibitor identified by high-throughput screening inhibits UBE2T/FANCL-mediated FANCD2 monoubiquitylation and sensitizes cells to the DNA cross-linking agent carboplatin, validating the UBE2T–FANCL catalytic pair as a druggable target in the FA pathway. | PMID:31525021 | ACS chemical biology |
| 2022 | Medium | FANCL protein localizes to mitochondria (in both basal and mitochondrial stress conditions), and its ubiquitin ligase activity is not required for this mitochondrial localization. CRISPR/Cas9 knockout of FANCL in parkin-overexpressing HeLa cells impairs clearance of damaged mitochondria (mitophagy) upon oligomycin/antimycin treatment; this defect is rescued by reintroduction of either wild-type FANCL or the catalytically dead FANCL(C307A) mutant, demonstrating a ubiquitin ligase-independent role in supporting Parkin-mediated mitophagy. | PMID:35644338 | Biochimica et biophysica acta. Molecular basis of disease |
| 2006 | Medium | In Drosophila, FANCL is necessary for monoubiquitination of FANCD2, and epistasis analysis places FANCL upstream of FANCD2 in a linear DNA repair pathway. Knockdown of either FANCL or FANCD2 confers hypersensitivity to cross-linking agents. | PMID:16860002 | DNA repair |
| 2002 | Medium | Mouse Pog (the ortholog of FANCL) is necessary for primordial germ cell (PGC) proliferation between E9.5 and E10.25 dpc. Deletion of Pog causes the germ-cell-deficient (gcd) phenotype with reduced PGC numbers and adult sterility; the proliferation defect rather than aberrant migration is responsible. | PMID:12417526 | Human molecular genetics |
| 2003 | Medium | POG (FANCL ortholog) interacts with GGN1 and GGN3 (gametogenetin isoforms) via yeast two-hybrid and co-expression in HeLa cells. Co-expression of POG with GGN1 or GGN3 relocalizes POG to the perinuclear region or nucleoli, respectively, and Pog-deficient mice show impaired meiosis during spermatogenesis. | PMID:12574169 | The Journal of biological chemistry |
| 2010 | High | In zebrafish, fancl is expressed in developing germ cells at the critical time of sexual fate determination. Loss of fancl causes Tp53-mediated germ cell apoptosis (demonstrated by caspase-3 immunoassay), compromises oocyte survival through meiosis, and results in female-to-male sex reversal. Introduction of a tp53 mutation into fancl mutants rescues sex reversal by reducing germ cell apoptosis. | PMID:20661450 | PLoS genetics |
| 2020 | Medium | Two heterozygous frameshift mutations in FANCL (c.1048_1051delGTCT and c.739dupA) identified in POI patients cause cytoplasmic retention of mutant FANCL protein (whereas wild-type FANCL is nuclear), impaired ubiquitin-ligase activity, and compromised DNA repair after mitomycin C treatment. | PMID:32048394 | Human mutation |
| 2026 | High | A murine FanclTATΔ allele removing the catalytic cysteine in the RING domain generates a core complex that retains structural integrity but lacks FANCD2 monoubiquitination activity. Homozygous mice phenocopy human FA (infertility, craniofacial anomalies, DNA damage hypersensitivity, progressive HSC loss). CRISPR-Cas9 or prime editing correction of the mutation restores FANCD2 monoubiquitination and DNA damage resistance in myeloid cells, demonstrating that loss of RING E3 ligase activity alone explains all major FA phenotypes. | PMID:41259745 | Blood advances |
| 2020 | Medium | Analysis of 17 FANCL URD-domain variants from patient cancer cells shows that mutations I136V, L154S, W212A, L214A, R221W, R221C, and V287G destabilize FANCL, while E217K, T224K, M247V, and the hydrophobic patch mutants (L248A, F252A, L254A, I265A) impair catalytic function without destabilizing the fold. N270K and E289Q specifically destabilize the C-terminal helices of the URD domain. These functional defects correlate with cellular sensitivity to an interstrand cross-linking agent. | PMID:32420600 | Bioscience reports |

## Citations

- PMID:12417526
- PMID:12574169
- PMID:14712086
- PMID:16474167
- PMID:16860002
- PMID:17352736
- PMID:19111657
- PMID:19589784
- PMID:20154706
- PMID:20661450
- PMID:21229326
- PMID:21775430
- PMID:22653977
- PMID:23783032
- PMID:24389026
- PMID:26149689
- PMID:28535027
- PMID:31525021
- PMID:32048394
- PMID:32420600
- PMID:35644338
- PMID:41259745
