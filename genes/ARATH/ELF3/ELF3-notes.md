# ELF3 (At2g25930; UniProt O82804) curation notes

## 2026-10-06: initial review (module plant_circadian_clock_oscillator)

- Fetched with `just fetch-gene ARATH O82804 --alias ELF3`. Falcon deep research failed; review based on cached publications.

### Key findings
- Evening complex scaffold [PMID:21753751 "ELF3 is both necessary and sufficient to form a complex between ELF4 and LUX"]; LUX targets the EC to PIF4/PIF5 promoters [PMID:21753751].
- No DNA-binding domain [PMID:32165537 "LUX possesses a single MYB DBD, whereas ELF3 and ELF4 have no domains known to interact with DNA."].
- ELF4 recruits ELF3 into nuclear foci; ELF3 associates with the PRR9 promoter [PMID:22327739].
- Thermosensor prion-like domain [PMID:32848244 "A purified fragment encompassing the ELF3 PrD reversibly forms liquid droplets in response to increasing temperatures in vitro"]; EC target binding is temperature-dependent [PMID:28650433].
- Zeitnehmer that antagonises nocturnal light input [PMID:11402162]; required for clock function under thermocycles [PMID:20133619].
- COP1 substrate adaptor for GI degradation [PMID:19061637 "ELF3 acts as a substrate adaptor, enabling COP1 to modulate light input signal to the circadian clock through targeted destabilization of GI"].

### Decisions
- DNA-binding TF activity ISS (PYK20 paper, Q-rich domain only): MODIFY to transcription corepressor activity.
- Protein binding with ELF4: MODIFY to protein-macromolecule adaptor activity. With PHYB: REMOVE.
- IEP auxin/ABA: MARK_AS_OVER_ANNOTATED. Cold IEP: KEEP_AS_NON_CORE.
- Flowering, stomata, circumnutation and hypocotyl phenotypes: KEEP_AS_NON_CORE (clock outputs).
- NEW: response to temperature stimulus (GO:0009266), from Jung et al. 2020 thermosensing.

## 2026-10-19: literature update (2022-2026)

- Searched PubMed for ELF3 / evening-complex papers from 2022 onward (about 45 hits). None were cited in the review or behind any GOA row; the newest experimental GOA reference is from 2011 (PMID:21753751).
- Cached 17 priority papers with `just fetch-pmid`. Abstract only: PMID:40737553, PMID:36883592, PMID:34698833, PMID:41292294, PMID:40913711, PMID:39192577. The rest have full text.

### Key findings added
- Chromatin mechanism of EC repression [PMID:39880018 "ELF3 recruits the JUMONJI (JMJ) H3K4me3 demethylases JMJ17 and JMJ18 to the PIF4 and PIF5 loci in the evening to remove their H3K4me3 marks"]; SWR1/H2A.Z at PIF4 [PMID:38816994 "Transcriptional repression of PIF4 by ELF3, PRR5, and TOC1 is mediated by the SWI2/SNF2-RELATED (SWR1) chromatin remodeling complex"]; H2A.Z at GI [PMID:38327058].
- Temperature input to the clock [PMID:34698833 "ELF3 is essential for delivering temperature input to the clock"; "Genetic analyses suggest that the evening complex is not required for ELF3-controlled thermoresponsiveness"].
- PrLD biophysics [PMID:37399408 "This species undergoes LLPS in a pH- and temperature-sensitive manner"]; condensate hysteresis [PMID:35234947]; Ser364 site outside the PrD and ELF4-dependent ELF3 stability [PMID:41292294]; PrLD mainly in Brassicales [PMID:39391982].
- ABA signalling [PMID:40737553 "ELF3, ELF4, and LUX repress the function and accumulation of ABI3 and ABI5"].
- ELF3β from an alternative promoter in intron 2 [PMID:36883592 "AtELF3β physically interacted with AtELF3α, disrupting the formation of the evening complex"]; natural SNP near the ELF3β start site [PMID:42315129]. ELF3β is not UniProt isoform O82804-2, which is a C-terminal truncation (1-339).
- Regulators of ELF3 (not annotated to ELF3): SA reduces ELF3 LLPS [PMID:40913711]; BBX24/BBX25 bind and suppress ELF3 [PMID:40443038]; phyB-ELF3-HEMERA complex [PMID:39192577]; light-quality-dependent localization [PMID:35191492]; XCT and COP1 lower ELF3 abundance [PMID:41522720]. Phototropism output [PMID:40995069] noted but not annotated.

### Decisions
- Response to abscisic acid (IEP): MARK_AS_OVER_ANNOTATED changed to MODIFY → GO:0009788 negative regulation of abscisic acid-activated signaling pathway, based on the Tang et al. 2025 abstract. Full text still to be checked.
- Kept NEW GO:0009266 response to temperature stimulus rather than GO:0016048 detection of temperature stimulus. Comparator check: TAIR annotates PHYB (the canonical thermosensor) to GO:0009266, and no ARATH gene in this repo carries GO:0016048. Raised as a suggested question instead.
- Added supporting evidence to: DNA-binding TF → corepressor MODIFY (JMJ17/18), entrainment IMP (Zhu et al. 2022), and the thermosensor NEW row and core function (PNAS 2023, Plant Cell 2022).
