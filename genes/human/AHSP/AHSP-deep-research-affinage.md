---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AHSP
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q9NZD4
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 19
citation_count: 19
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AHSP (human)

## Current model (mechanistic narrative)

AHSP is an erythroid-specific molecular chaperone that stabilizes free alpha-hemoglobin (alphaHb) during the assembly of hemoglobin A, preventing its precipitation and the cytotoxicity that accompanies unpaired alpha-globin [PMID:15550245, PMID:18179859]. Structural studies show that AHSP engages alphaHb through a hydrophobic interface recapitulating the alpha1-beta1 contact of HbA, recognizing the G and H helices, with the alpha119/H2 and alpha117/GH region of the H helix critical for binding [PMID:15550245, PMID:17052927, PMID:25369055]. The N-terminal H-helix segment mediates AHSP contact while the C-terminal segment supports heme binding [PMID:25369055]. AHSP binds alpha-globin even in the apo (heme-free) state, suppressing aggregation and promoting folding before heme acquisition [PMID:20860551]. Upon binding ferrous alphaHb, AHSP introduces strain into the proximal heme pocket via a Pro-30-mediated contact, lengthening the Fe-O2 bond, lowering O2 affinity, and accelerating autooxidation to a ferric bis-histidyl hexacoordinate hemichrome in which both proximal and distal histidines ligate the iron [PMID:15931225, PMID:23696640]. This configuration is redox-inert: it lowers the alpha-subunit redox potential, slows reaction with H2O2, blocks formation of ferryl species and protein radicals, and prevents precipitation, allowing the bound hemichrome to be enzymatically reduced and recycled into functional HbA [PMID:16901899, PMID:23264625, PMID:17194704]. AHSP preferentially traps the ferric intermediate, and reduction of bound ferric alphaHb triggers its release toward the beta-chain, so that incoming beta-hemoglobin competitively displaces AHSP to form tetrameric HbA [PMID:16901899, PMID:22298770, PMID:24060751]. By holding alpha-subunits in this protected state, AHSP also limits oxidative damage to partner beta-subunits, including betaCys93 [PMID:26995402]. AHSP transcription is driven in response to erythroid and oxidative-stress signals by STAT3 at an IL-6-responsive promoter element and by the Nrf2/MafG axis at a downstream MARE site, the latter mitigating alpha-globin precipitation and ROS in thalassemic erythroid cells [PMID:24740453, PMID:35092867]. Loss of AHSP function, whether by knockdown or by disease-associated variants such as V56G that shorten the AHSP-alphaHb contact time, causes alpha-globin precipitation, elevated ROS, and apoptosis during erythropoiesis [PMID:20371604, PMID:18179859].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0044183 protein folding chaperone, GO:0140313 molecular sequestering activity, GO:0016209 antioxidant activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** *(none)*
- **partners:** HBA1, STAT3, NFE2L2, MAFG, POU2F1
- **complexes:** AHSP-alpha-hemoglobin heterodimer

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | Crystal structure of AHSP bound to Fe(II)-alphaHb reveals that AHSP specifically recognizes the G and H helices of alphaHb through a hydrophobic interface that largely recapitulates the alpha1-beta1 interface of hemoglobin. The AHSP-alphaHb interactions are suboptimal, explaining competitive displacement by beta-hemoglobin to form HbA. Binding to AHSP facilitates conversion of oxy-alphaHb to a deoxygenated, oxidized [Fe(III)], nonreactive hexacoordinate form in which the distal but not the proximal histidine coordinates the heme iron. | PMID:15550245 | Cell |
| 2005 | High | Crystal structure of ferric alphaHb-AHSP complex at 2.4 Å resolution reveals a bis-histidyl configuration in which both proximal and distal histidines coordinate the heme iron atom, requiring drastic structural rearrangements of alphaHb including repositioning of several alpha-helices. This ferric bis-histidine configuration strongly and specifically inhibits redox chemistry catalysis and heme loss from alphaHb, explaining how AHSP stabilizes alphaHb. | PMID:15931225 | Nature |
| 2006 | High | AHSP-bound Fe(II) alphaHb undergoes auto-oxidation to form Fe(III) alphaHb-AHSP (hemichrome) at physiologic temperature and oxygen pressures. Unlike free Fe(III) alphaHb hemichromes, AHSP-bound Fe(III) alphaHb does not precipitate and can be recycled into functional HbA following enzymatic reduction. Addition of betaHb to either Fe(II) or Fe(III) alphaHb-AHSP displaces AHSP to generate tetrameric HbA. | PMID:16901899 | The Journal of biological chemistry |
| 2012 | High | AHSP binding dramatically reduces the redox potential of alpha-subunits from +40 to -78 mV, demonstrating higher AHSP affinity for Fe(III) versus Fe(II) alpha-subunits. Hexacoordination in the AHSP-met-alpha complex markedly decreases the rate of H2O2 reaction with iron and prevents ferryl heme species and protein-based radicals, providing protection against oxidative reactions. | PMID:23264625 | The Journal of biological chemistry |
| 2012 | High | AHSP rapidly binds ferrous alpha-globin with association rate ~10 µM⁻¹s⁻¹ and dissociation rate ~0.2 s⁻¹. A slow phase due to cis-to-trans prolyl isomerization of Asp29-Pro30 in AHSP was identified by P30A/P30W mutants. Met-alpha dissociates from AHSP ~100-fold more slowly than ferrous alpha-AHSP (k ~0.002 s⁻¹), enabling AHSP to preferentially stabilize and kinetically trap ferric alpha hemichrome folding intermediates, preventing their incorporation into mixed-valence HbA tetramers. | PMID:22298770 | The Journal of biological chemistry |
| 2013 | High | NMR and X-ray absorption spectroscopy (EXAFS) reveal that AHSP binding to CO-alphaHb alters the F, G, and H helices and heme pocket, induces a 0.03 Å lengthening of the Fe-O2 bond, and increases O2 dissociation rate 3-4-fold, explaining the ~4-fold decrease in O2 affinity and promotion of autooxidation. Pro-30 mutations in AHSP diminished NMR chemical shift changes in the proximal heme pocket and restored normal O2 dissociation, establishing that Pro-30-mediated contacts introduce strain into the proximal heme pocket to facilitate autooxidation. | PMID:23696640 | The Journal of biological chemistry |
| 2010 | Medium | AHSP forms a heterodimeric complex with apo-alpha-globin (lacking heme) and inhibits its aggregation while promoting folding in the absence of heme, demonstrating that AHSP functions as an alpha-globin-specific chaperone prior to heme acquisition. | PMID:20860551 | The Biochemical journal |
| 2006 | Medium | High hydrostatic pressure induces irreversible aggregation of free ferrous deoxy alpha-chains, whereas the AHSP/alpha-Hb complex shows reversible hexacoordination without aggregation. AHSP remained protective at 300 MPa. Ferric AHSP/alpha-Hb shows His-Fe-His hexacoordination even at atmospheric pressure. Reaction of ferric alpha-Hb within the complex with H2O2 also demonstrates protection against aggregation. | PMID:17194704 | The Journal of biological chemistry |
| 2006 | Medium | Co-expression of recombinant Hb Groene Hart (alpha119 Pro→Ser) with AHSP demonstrated impaired interaction between this alpha-chain variant and AHSP, while alpha mutants at positions 42 and 104 showed normal interaction, establishing that the alpha119 (H2) site is critical for AHSP binding. | PMID:17052927 | Blood cells, molecules & diseases |
| 2014 | Medium | Stepwise deletion of the alpha-globin H helix showed that the N-terminal part of the H helix is essential for interaction with AHSP, while the C-terminal part is required for heme interaction. Truncated alpha-Hb1-134 and shorter forms displayed modified absorption spectra and increased fluorescence, indicating lower heme affinity. Addition of betaHb displaced AHSP from all truncated forms. | PMID:25369055 | PloS one |
| 2010 | Medium | Kinetic analysis of AHSP(V56G) mutant (associated with mild thalassemia syndrome) showed it is partially unfolded but recovers structure upon alpha-Hb binding. The main defect is a dissociation rate ~4-fold faster than wild-type AHSP, resulting in insufficient contact time (~0.5 s vs ~2 s for WT) to complete structural modifications of alpha-globin. | PMID:20371604 | The Journal of biological chemistry |
| 2013 | Medium | AHSP binding to alpha-Hb is kinetically controlled (fast binding outcompetes direct alpha-beta association) and thermodynamically controlled by the alpha-Hb redox state rather than the liganded state. AHSP-bound ferric alpha-Hb is dramatically stabilized compared to free ferric alpha-Hb, and removing bis-histidyl hexacoordination (H58Q mutation) reduces AHSP's stabilizing effect. Reduction of AHSP-bound ferric alpha-Hb triggers its release toward beta-chain partner. | PMID:24060751 | Biochimica et biophysica acta |
| 2008 | Medium | A rare missense mutation N75I in AHSP impairs its ability to inhibit reactive oxygen species production by alpha-hemoglobin. A high-frequency intron 1 polymorphism (12391 G>A) alters an Oct-1 transcription factor binding site, impairs Oct-1 binding, and inhibits AHSP regulatory sequence-driven luciferase reporter expression. | PMID:17874450 | American journal of hematology |
| 2008 | Medium | RNA interference-mediated knockdown of AHSP in hemin-induced K562 and erythropoietin-induced CD34+ cells resulted in considerable alpha-Hb precipitation, significant decrease in HbF formation, increased ROS production, and increased apoptosis, establishing AHSP as required for alpha-Hb stabilization and normal hemoglobin formation during human erythropoiesis. | PMID:18179859 | Experimental hematology |
| 2016 | Medium | AHSP stabilizes alpha-subunits in a redox-inactive hexacoordinate conformation, preventing the ferric/ferryl transition. In the presence of AHSP, H2O2-induced oxidation of betaCys93 was substantially reduced in both HbA and HbE, demonstrating that AHSP protection of alpha-subunits limits oxidative damage to beta-subunits. | PMID:26995402 | Redox biology |
| 2014 | Medium | STAT3 directly binds the SB3 (IL-6RE) element in the AHSP promoter and activates AHSP gene expression. IL-6-induced STAT3 activation increased AHSP expression in K562 cells; STAT3 knockdown decreased it. ChIP confirmed STAT3 occupancy at the AHSP promoter, augmented by IL-6 and alpha-globin overexpression. EMSA confirmed direct STAT3-SB3 binding. | PMID:24740453 | Science China. Life sciences |
| 2022 | Medium | Nrf2 and its agonist tBHQ stimulate AHSP expression in K562 cells and thalassemic erythroblasts. MafG and Nrf2 occupancy at the MARE-1 site downstream of the AHSP transcription start site was detected by ChIP. MafG facilitates Nrf2-mediated AHSP activation. Nrf2 or AHSP knockdown exacerbated alpha-globin precipitation and ROS production in thalassemic erythroid cells; tBHQ treatment partially alleviated these effects. | PMID:35092867 | Redox biology |
| 2008 | Low | Hb Foggia (alpha117 Phe→Ser, at the GH5 position) results in no detectable alpha-chain or Hb variant despite normal mRNA levels, and the amino acid substitution at position 117 (within the AHSP binding interface) is proposed to impair AHSP interaction and prevent its stabilizing effect, leading to alpha-chain pool reduction. | PMID:18166800 | Haematologica |
| 2020 | Low | AHSP protein expression is negligible in early erythroblasts (CFU-Es, day 6), progressively increases to peak at day 12, then declines by day 14. Sub-cellular localization shifts from both cytoplasm and nucleus in early erythroblasts to predominantly nuclear in late stages, with AHSP expelled with the nucleus during enucleation. | PMID:32629835 | Methods and protocols |

## Citations

- PMID:15550245
- PMID:15931225
- PMID:16901899
- PMID:17052927
- PMID:17194704
- PMID:17874450
- PMID:18166800
- PMID:18179859
- PMID:20371604
- PMID:20860551
- PMID:22298770
- PMID:23264625
- PMID:23696640
- PMID:24060751
- PMID:24740453
- PMID:25369055
- PMID:26995402
- PMID:32629835
- PMID:35092867
