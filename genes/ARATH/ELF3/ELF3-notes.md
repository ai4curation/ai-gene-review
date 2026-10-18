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
