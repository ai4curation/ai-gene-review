---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADPRS
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9NX46
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 17
citation_count: 18
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADPRS (human)

## Current model (mechanistic narrative)

ADPRS (ARH3/ADPRHL2) is an all-alpha-helical, Mg2+-dependent hydrolase that serves as the principal cellular eraser of ADP-ribosylation, controlling the reversibility of ADP-ribose marks during the DNA damage response and the oxidative stress response [PMID:17015823, PMID:16511307, PMID:28650317]. Catalysis is organized around two active-site Mg2+ ions coordinated by acidic residues, with vicinal aspartates D77/D78 and a dynamic Glu41 mediating glycosidic bond cleavage; ADP-ribose recognition in the catalytic groove is itself required for recruitment of ARH3 to DNA lesions [PMID:17075046, PMID:30045870]. The enzyme has broad substrate scope: it efficiently degrades poly(ADP-ribose) and is the dominant PAR-degrading activity in the mitochondrial matrix [PMID:22433848], hydrolyzes the sirtuin product O-acetyl-ADP-ribose at far higher rates than poly(ADP-ribose) [PMID:17075046], and removes serine- and tyrosine-linked ADP-ribosylation from histones and other proteins [PMID:28650317, PMID:39342999]. By erasing PARP-installed mono- and poly-ADP-ribose marks at single-strand break repair sites, ARH3 reverses DNA-damage-induced chromatin scars, restores H3K9 acetylation, and normalizes transcription [PMID:32636369]. Loss of ARH3 causes PAR accumulation, AIF nuclear translocation, and parthanatos-type cell death that is rescued by PARP1 inhibition, and its correct nuclear localization is essential for clearing nuclear ADP-ribosylation during stress [PMID:30830864, PMID:34479984]. Loss-of-function mutations in ADPRHL2 cause a neurodegenerative disorder, with the cell-death phenotype placed genetically downstream of PARP [PMID:30100084].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0140096 catalytic activity, acting on a protein, GO:0140098 catalytic activity, acting on RNA, GO:0003723 RNA binding
- **localization:** GO:0005634 nucleus, GO:0005739 mitochondrion, GO:0005829 cytosol, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-5357801 Programmed Cell Death, R-HSA-4839726 Chromatin organization, R-HSA-8953897 Cellular responses to stimuli
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | Crystal structure of human ARH3 (hARH3) determined at 1.6 Å resolution, revealing an all-alpha-helical fold with two magnesium ions flanked by conserved amino acids pinpointing the active-site crevice. Recombinant hARH3 binds free ADP-ribose with micromolar affinity and efficiently de-ADP-ribosylates poly- but not mono-ADP-ribosylated proteins in vitro. | PMID:17015823, PMID:16511307 | Proceedings of the National Academy of Sciences of the United States of America |
| 2006 | High | ARH3 hydrolyzes O-acetyl-ADP-ribose (a Sir2/sirtuin reaction product) to ADP-ribose in a time- and Mg2+-dependent reaction, at a rate 250-fold faster than its hydrolysis of poly(ADP-ribose). Replacement of vicinal aspartates D77 and D78 with asparagine abolishes this activity, defining these residues as essential for catalysis. ARH2 and PARG were inactive on this substrate. | PMID:17075046 | Proceedings of the National Academy of Sciences of the United States of America |
| 2012 | High | ARH3, not PARG isoforms, is responsible for the degradation of mitochondrial matrix-associated poly(ADP-ribose). Embryonic fibroblasts from ARH3-knockout mice lack most of the mitochondrial PAR-degrading activity detected in wild-type cells. The mitochondrial PARG isoform lacks catalytic activity due to absence of exon 5-encoded residues. | PMID:22433848 | The Journal of biological chemistry |
| 2017 | High | ARH3/ADPRHL2 specifically and efficiently removes serine-linked ADP-ribosylation (Ser-ADPr) from histones and other proteins in cells. Quantitative proteomics showed that histone Ser-ADPr is reversible during the DNA damage response, and this reversal is dependent on ARH3. | PMID:28650317 | eLife |
| 2018 | High | Crystal structure of ARH3 in complex with ADP-ribose (ADPR) reveals that acidic residues coordinate two Mg2+ ions at the catalytic center; dynamic conformational changes of Glu41 are observed, and Mg2+ ions together with Glu41 and water351 mediate cleavage of the glycosidic bond in serine-ADPR substrate. Site-directed mutagenesis of key catalytic pocket residues confirmed their roles in hydrolyzing Ser-linked ADP-ribosyl groups and in DNA damage repair. ADPR recognition is essential for ARH3 recruitment to DNA lesions. | PMID:30045870 | The Journal of biological chemistry |
| 2018 | Medium | Loss-of-function mutations in ADPRHL2 (ARH3) cause neurodegeneration; loss of the Drosophila paralog Parg showed lethality under oxidative challenge that was rescued by human ADPRHL2, demonstrating functional conservation. Pharmacological inhibition of PARP rescued the lethality phenotype, placing ADPRHL2 downstream of PARP in a cell-death pathway. | PMID:30100084 | American journal of human genetics |
| 2018 | Medium | Patient fibroblasts lacking ADPRHL2 protein show reduced cell viability upon hydrogen peroxide exposure; this is rescued by expression of wild-type ADPRHL2 mRNA and by PARP1 inhibitor treatment, placing ARH3 as a negative regulator of PARP1-dependent cell death downstream of oxidative stress. | PMID:30401461 | American journal of human genetics |
| 2019 | High | ARH3 confers protection against oxidative stress by lowering cytosolic and nuclear PAR levels and preventing apoptosis-inducing factor (AIF) nuclear translocation. ARH3-deficient patient fibroblasts and ARH3-knockout mice show increased sensitivity to H2O2 and cerebral ischemia/reperfusion-induced PAR accumulation and cell death; PARP1 inhibition alleviates this injury. | PMID:30830864 | JCI insight |
| 2020 | High | ARH3-mutated patient cells accumulate mono(ADP-ribose) scars on core histones that are a molecular memory of recently repaired DNA single-strand breaks. These scars reduce endogenous H3K9 acetylation levels and cause measurable deregulated transcription. Prolonged PARP inhibition removes the mono(ADP-ribose) scars from chromatin and restores chromatin acetylation to normal, establishing ARH3 as an eraser of ADP-ribose chromatin scars at PARP-active DNA single-strand break repair sites. | PMID:32636369 | Nature communications |
| 2020 | Medium | Small molecule AI26 binds to the catalytic pocket of ARH3 and inhibits its enzymatic activity (IC50 ~2.41 μM in vitro), suppressing hydrolysis of DNA damage-induced ADP-ribosylation in cells and causing DNA damage repair defects. | PMID:32753484 | The Journal of biological chemistry |
| 2021 | Medium | A novel ARH3 C26F mutation causes protein instability and reduced protein function. The recurrent V335G mutant retains enzymatic activity but loses cytosolic/nuclear localization while retaining mitochondrial localization; this mislocalization minimally affects basal ADP-ribosylation but results in elevated nuclear ADP ribosylation during stress, demonstrating that ARH3 subcellular localization is critical for reversing nuclear ADP-ribosylation during DNA damage. | PMID:34479984 | Life science alliance |
| 2024 | Medium | ARH3 hydrolyzes tyrosine-linked ADP-ribosylation (Tyr-ADPr) in addition to serine-linked ADPr. Tyr-ADPr sites are enriched among ribosome biogenesis and mRNA processing proteins and are affected by ARH3 status; PARG also reverses Tyr-ADPr in vitro. | PMID:39342999 | The Journal of biological chemistry |
| 2024 | Medium | The ARH3 H182R variant (active-site residue) causes protein instability and degradation, reduced expression, and failure to localize to the nucleus; the resulting accumulation of mono-ADP-ribosylated species in cells establishes that nuclear localization of ARH3 is required for proper removal of mono-ADP-ribosylation. | PMID:39580621 | HGG advances |
| 2024 | Medium | Omega-3 fatty acids reduce cytokine-induced β-cell apoptosis by upregulating ARH3 expression via a mechanism involving reduction of the PRC2 component Suz12, which epigenetically derepresses Arh3 expression. ARH3 knockdown (siRNA) in MIN6 cells confirmed that ARH3 reduces CXCL9 chemokine expression in response to pro-inflammatory cytokines. | PMID:38383396 | Cell communication and signaling : CCS |
| 2024 | Medium | DNA damage-induced histone poly-ADP-ribosylation triggers a transient increase in nucleosome mobility switching chromatin from a densely-packed to a looser conformation; mono-ADP-ribosylation is sufficient to maintain the open-chromatin state. Removal of histone ADP-ribose marks by ARH3 hydrolase leads to chromatin recondensation, establishing ARH3 as a direct regulator of chromatin compaction dynamics at DNA lesions. | PMID:bio_10.1101_2024.08.28.610034 | bioRxiv |
| 2023 | Medium | ARH3 regulates PAR homeostasis in myocardium to preserve cardiac function and protect against oxidative stress. Arh3-KO male mice display cardiac hypertrophy and decreased cardiac contractility; KO hearts show increased ischemia-reperfusion infarct size and elevated PAR levels. PARP inhibitor rucaparib improves cardiac contractility and reduces infarct size in ARH3-deficient mice. Arh3-KO and heterozygous myoblasts/myotubes show PAR-dependent cell death under H2O2 that is reduced by PARP inhibitors or Arh3 transfection. | PMID:36945462 | bioRxiv |
| 2025 | High | A 2-hydrazinopyrimidin-4-one analog (compound 27/MDOLL-0286, 2 μM potency) inhibits ARH3's poly-ADP-ribose hydrolytic activity on cellular substrates but does not effectively inhibit hydrolysis of mono-ADP-ribosylation from natural protein substrates. Co-crystal structure of the initial hit compound bound to ARH3 reveals overlap with the ADP-ribose binding site, consistent with competitive inhibition. | PMID:40952342 | ACS chemical biology |

## Citations

- PMID:16511307
- PMID:17015823
- PMID:17075046
- PMID:22433848
- PMID:28650317
- PMID:30045870
- PMID:30100084
- PMID:30401461
- PMID:30830864
- PMID:32636369
- PMID:32753484
- PMID:34479984
- PMID:36945462
- PMID:38383396
- PMID:39342999
- PMID:39580621
- PMID:40952342
- PMID:bio_10.1101_2024.08.28.610034
