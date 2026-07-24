---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCA
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: O15360
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 29
citation_count: 29
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCA (human)

## Current model (mechanistic narrative)

FANCA is a large nuclear protein that serves as a scaffold organizer of the Fanconi anemia (FA) core complex, the assembly required for activating the FA/BRCA interstrand crosslink (ICL) repair pathway [PMID:9789045, PMID:21273304]. Through an N-terminal arginine-rich motif (residues 18–29, with Arg1/Arg2/Leu8 critical) FANCA binds FANCG, and the two proteins reciprocally stabilize each other and promote nuclear accumulation of the complex [PMID:10567393, PMID:11050007, PMID:32002546]; cryo-EM defines a C-terminal arc-shaped HEAT-repeat solenoid that forms a pseudo-symmetric dimer and engages FANCG at both N- and C-terminal interfaces, with disease mutations at these contacts blocking nuclear import and pathway function [PMID:32002546]. FANCA additionally complexes with FANCC and FANCF, and its nuclear localization is necessary and sufficient for correcting mitomycin C hypersensitivity in FA-A cells, distinct from FANCC's separable cytoplasmic role [PMID:9398857, PMID:9746759, PMID:11063725]. FAAP20 directly binds and stabilizes FANCA, and its loss reduces FANCD2 monoubiquitination and reproduces FA phenotypes, placing FANCA upstream of the central ICL-repair switch [PMID:22396592]. Patient-derived missense and truncation mutations cause FA by preventing nuclear relocation and pathway activation rather than by graded loss of an intrinsic activity, accounting for the absence of genotype–phenotype correlation [PMID:21273304]. FANCA is regulated by DNA-damage-induced ATR phosphorylation on Ser1449 and by NEK2 phosphorylation on Thr351 at centrosomes [PMID:19109555, PMID:23806870]. Beyond core-complex scaffolding, purified FANCA possesses intrinsic nucleic acid binding (RNA > ssDNA > dsDNA) via its C-terminal domain and directly catalyzes single-strand annealing and strand exchange comparable to RAD52, acting in the single-strand-annealing branch of double-strand break repair independently of the canonical FA pathway, with FANCG stimulating these activities [PMID:22194614, PMID:30057198]. FANCA also localizes to centrosomes and pericentriolar material during mitosis, where it maintains centrosomal integrity, spindle assembly, and spindle-assembly-checkpoint function [PMID:23806870, PMID:26366677]. It engages additional partners — BRCA1, the SWI/SNF subunit BRG1, alpha-spectrin II, and mu-calpain — linking it to chromatin and to a spectrin scaffold that recruits FANCA to crosslink sites [PMID:10551855, PMID:11726552, PMID:12354784, PMID:20518497].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0003723 RNA binding, GO:0140097 catalytic activity, acting on DNA, GO:0060090 molecular adaptor activity, GO:0005198 structural molecule activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol, GO:0005815 microtubule organizing center
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1640170 Cell Cycle
- **partners:** FANCG, FANCC, FANCF, FAAP20, BRCA1, BRG1, SPTAN1, NEK2
- **complexes:** Fanconi anemia core complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1996 | Medium | FANCA (FAA) encodes a predicted 162,752 Da protein containing two overlapping bipartite nuclear localization signals and a partial leucine zipper consensus, suggestive of nuclear localization and function. | PMID:8896563 | Nature genetics |
| 1997 | High | FANCA (FAA) and FANCC (FAC) proteins bind each other to form a complex; the complex localizes to both cytoplasm and nucleus, whereas unbound FAA and FAC localize predominantly to the cytoplasm. | PMID:9398857 | Nature genetics |
| 1998 | High | Nuclear localization of FANCA is necessary but not sufficient for its functional activity; FANCA requires binding to FANCC for complementation activity, and mutant FANCA that cannot bind FANCC fails to promote nuclear accumulation of FANCC and is non-functional. | PMID:9742112 | Molecular and cellular biology |
| 1998 | High | FANCA is phosphorylated in normal lymphoblasts; this phosphorylation, together with FANCA/FANCC complex formation and nuclear accumulation of the complex, is defective in FA cells from multiple complementation groups (A, B, C, E, F, G, H), defining these events as part of a shared FA signaling pathway. | PMID:9789045 | Proceedings of the National Academy of Sciences of the United States of America |
| 1999 | High | FANCA and FANCG form a physical complex both in vivo and in vitro; this complex is detected in non-FA cells and FA-D and FA-E cells, but absent in FA-A and FA-G cells; disruption of the complex correlates with the FA cellular phenotype. | PMID:10468606 | Proceedings of the National Academy of Sciences of the United States of America |
| 1999 | High | FANCA, FANCC, and FANCG interact in a functional nuclear complex; the amino-terminal region of FANCA is required for FANCG binding, FANCC binding, nuclear localization, and functional activity of the complex. | PMID:10373536 | Molecular and cellular biology |
| 1999 | High | Nuclear localization of FANCA is necessary and sufficient to correct mitomycin C sensitivity in FA-A cells; FANCA with nuclear export signal failed to correct, while FANCA with nuclear localization signal corrected. Separate from FANCC function in the cytoplasm. | PMID:9746759 | Blood |
| 1999 | Medium | Alpha spectrin II (alphaSpIISigma*) forms a nuclear complex with FANCA and FANCC; levels of alphaSpIISigma* are significantly reduced in FA-A, FA-B, FA-C, and FA-D cells, suggesting FA proteins are required for stability or expression of alphaSpIISigma*. | PMID:10551855 | The Journal of biological chemistry |
| 1999 | High | A patient-derived FANCA mutation (H1110P) abolishes FANCA phosphorylation, FANCC binding, nuclear accumulation, and functional complementation of MMC sensitivity. | PMID:10210316 | Experimental hematology |
| 1999 | High | FANCA interaction domain for FANCG maps to amino acids 18–29 of FANCA (arginine-rich motif RRRAWAELLAG); alanine mutagenesis identified Arg1, Arg2, and Leu8 as critical residues. FANCA-FANCG complex formation and nuclear co-localization are required for cellular resistance to MMC. | PMID:10567393 | The Journal of biological chemistry |
| 2000 | High | FANCG binds directly to the amino-terminal NLS region of FANCA, stabilizes FANCA protein by prolonging its cellular half-life, and promotes nuclear accumulation of the FA protein complex; the reciprocal is also true (FANCA stabilizes FANCG). Carboxy-terminal leucine zipper mutations in FANCA allow cytoplasmic FANCG binding but block nuclear translocation. | PMID:11050007 | Blood |
| 2000 | High | FANCF forms a nuclear complex with FANCA, FANCC, and FANCG; each FA protein except FANCD is required for these complexes to form. | PMID:11063725 | Human molecular genetics |
| 2001 | Medium | FANCA protein associates with BRG1, a component of the human SWI/SNF chromatin-remodeling complex; FANCA co-localizes with BRG1 in the nucleus and co-purifies with the endogenous SWI/SNF complex. | PMID:11726552 | Human molecular genetics |
| 2001 | Medium | AlphaSpIISigma*, FANCA, FANCC, and FANCG proteins specifically bind to DNA containing psoralen interstrand cross-links; purified brain spectrin directly binds cross-linked DNA, suggesting alphaSpIISigma* scaffolds FA proteins at damage sites. | PMID:11401546 | Biochemistry |
| 2001 | Medium | A cytoplasmic serine protein kinase (FANCA-PK), sensitive to wortmannin, forms a complex with FANCA and phosphorylates it; this kinase is also present in the FANCA/FANCG complex, suggesting it is a regulatory component of the FA complex. | PMID:11739169 | Blood |
| 2002 | High | BRCA1 directly interacts with FANCA; the interaction involves the amino-terminal portion of FANCA and the central part (aa 740–1083) of BRCA1; the interaction is constitutive and does not require DNA damage. | PMID:12354784 | Human molecular genetics |
| 2003 | Medium | AlphaSpIISigma* is essential for DNA-damage-induced recruitment of FANCA and XPF to nuclear foci following treatment with psoralen/UVA; FA-A cells with decreased alphaSpIISigma* show reduced XPF and alphaSpIISigma* focus formation; correction with FANCA cDNA restores alphaSpIISigma* levels and nuclear focus formation. | PMID:12571280 | Journal of cell science |
| 2008 | High | ATR phosphorylates FANCA on serine 1449 in response to DNA damage (not during S phase); ATR-dependent phosphorylation is confirmed both in vivo (ATR-deficient cells lack it) and in vitro (ATR kinase directly phosphorylates FANCA-S1449); the S1449A phospho-deficient mutant fails to fully complement FA-associated phenotypes. | PMID:19109555 | Blood |
| 2011 | High | Purified FANCA protein has intrinsic nucleic acid-binding activity, preferring ssDNA > dsDNA, with RNA binding even stronger; minimum ~30 nucleotides required; a 5'-flap or 5'-tail facilitates binding; the nucleic acid-binding domain localizes primarily to the C-terminus. A patient-derived truncation mutant (Q772X) shows diminished binding, while the C-terminal fragment C772-1455 retains binding activity. | PMID:22194614 | The Journal of biological chemistry |
| 2012 | High | FAAP20 is a component of the FA core complex that directly interacts with FANCA and stabilizes it; loss of FAAP20 reduces FANCD2 monoubiquitination and causes hallmarks of FA (MMC hypersensitivity, chromosome aberrations). | PMID:22396592 | Proceedings of the National Academy of Sciences of the United States of America |
| 2013 | High | FANCA co-immunoprecipitates with NEK2 kinase and localizes to centrosomes (notably during mitosis); NEK2 phosphorylates FANCA at threonine-351 in vitro; the phosphorylation-defective T351A mutant shows centrosomal abnormalities, aberrant mitotic arrest, and enhanced nocodazole sensitivity; FANCA knockdown increases centrosomal abnormality frequency. | PMID:23806870 | The international journal of biochemistry & cell biology |
| 2014 | Medium | FANCA modulates neddylation of the chemokine receptor CXCR5; FANCA (but not FANCC) is required for CXCR5 neddylation, which promotes CXCR5 membrane targeting and cell migration/motility. | PMID:25015289 | Journal of cell science |
| 2014 | Medium | Fanca is required for transition mutations at A/T residues during somatic hypermutation in B cells, and for stabilizing short microhomology duplexes during class switch recombination, thereby impeding short-range recombination downstream of double-strand breaks. | PMID:24799500 | The Journal of experimental medicine |
| 2015 | Medium | FANCA shuttles to the pericentriolar material to regulate spindle assembly at mitotic entry; loss of FA signaling renders cells hypersensitive to spindle chemotherapeutics and allows escape from the spindle assembly checkpoint. | PMID:26366677 | Experimental hematology |
| 2018 | High | Purified FANCA protein catalyzes bidirectional single-strand annealing (SA) and strand exchange (SE) at levels comparable to RAD52; FANCG directly interacts with FANCA and stimulates its SA and SE activities; a disease-causing mutant (F1263Δ) and five other patient-derived mutants are deficient in SA and SE; FANCA plays a direct role in the SSA sub-pathway of DSB repair independently of the canonical FA pathway and RAD52. | PMID:30057198 | Molecular cell |
| 2020 | High | The cryo-EM structure of Xenopus FANCA alone (3.35/3.46 Å) reveals a C-terminal domain (CTD) with an arc-shaped solenoid structure forming a pseudo-symmetric dimer; two cryo-EM structures of FANCA-FANCG complex (4.59/4.84 Å) show FANCG independently contacts either the FANCA C-terminal HEAT repeats or the N-terminal region; mutations disrupting either interaction prevent FANCA nuclear localization and FA pathway function. | PMID:32002546 | Nucleic acids research |
| 2010 | Medium | Cytoplasmic FANCA and FANCC form a cytoplasmic subcomplex that interacts with and stabilizes the leukemic nucleophosmin NPMc; loss of FANCA or FANCC leads to NPMc ubiquitination by IBRDC2 and proteasomal degradation; depletion of FANCA and FANCC in NPMc-positive leukemic cells increases NF-κB activation. | PMID:20864535 | The Journal of biological chemistry |
| 2010 | Medium | FANCA and FANCG bind directly to mu-calpain; this binding may inhibit mu-calpain activity in normal cells, thereby maintaining stability of alphaIISp; in FA-A cells, increased mu-calpain activity leads to increased alphaIISp breakdown, and siRNA knockdown of mu-calpain in FA-A cells restores alphaIISp levels and corrects DNA interstrand cross-link repair defects and chromosomal instability. | PMID:20518497 | Biochemistry |
| 2011 | Medium | Missense mutations in FANCA that cause FA lead to altered FANCA protein that is unable to relocate to the nucleus and activate the FA/BRCA pathway, explaining the lack of correlation between FANCA mutation type and cellular or clinical phenotype severity. | PMID:21273304 | Blood |

## Citations

- PMID:10210316
- PMID:10373536
- PMID:10468606
- PMID:10551855
- PMID:10567393
- PMID:11050007
- PMID:11063725
- PMID:11401546
- PMID:11726552
- PMID:11739169
- PMID:12354784
- PMID:12571280
- PMID:19109555
- PMID:20518497
- PMID:20864535
- PMID:21273304
- PMID:22194614
- PMID:22396592
- PMID:23806870
- PMID:24799500
- PMID:25015289
- PMID:26366677
- PMID:30057198
- PMID:32002546
- PMID:8896563
- PMID:9398857
- PMID:9742112
- PMID:9746759
- PMID:9789045
