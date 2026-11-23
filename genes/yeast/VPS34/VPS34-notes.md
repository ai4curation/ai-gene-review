# VPS34 (P22543, YLR240W) notes

Evidence journal (YeastPathways phosphoinositide_biosynthesis batch, 2026-10-06).

## Activity
- Sole yeast PI3K; PI-specific [PMID:7989323 "Vps34p is a phosphatidylinositol-specific 3-kinase, as it is able to utilize phosphatidylinositol (PtdIns) but not PtdIns(4)P or PtdIns(4,5)P2 as substrates"].
- [PMID:8385367 "Yeast strains deleted for the VPS34 gene or carrying vps34 point mutations lacked detectable PI 3-kinase activity and exhibited severe defects in vacuolar protein sorting."]
- Autophosphorylation (protein kinase activity; non-core) [PMID:7989323 "the Vps34 phosphatidylinositol 3-kinase undergoes an autophosphorylation event both in vivo and in vitro"].
- YeastPathways step PI + ATP -> PI3P (EC 2.7.1.137) correct.

## Complexes
- [PMID:11157979 "two distinct Vps34 PtdIns 3-kinase complexes exist: one, containing Vps15p, Vps30p, and Apg14p, functions in autophagy and the other containing Vps15p, Vps30p, and Vps38p functions in CPY sorting"].
- Atg38 in complex I [PMID:24165940 "In atg38Δ cells, autophagic activity was significantly reduced and PI3-kinase complex I dissociated into the Vps15-Vps34 and Atg14-Vps30 subcomplexes."].
- Complex II structure [PMID:26450213 "Vps34 and Vps15 intertwine in one arm, where the Vps15 kinase domain engages the Vps34 activation loop to regulate its activity."].

## Location
- PAS, vacuolar membrane, endosomes [PMID:16421251 "Vps34p and Vps30p, components shared by the two complexes, localized to the PAS, vacuolar membranes, and several punctate structures that included endosomes."].
- Peroxisome [PMID:21121900], NV junction [PMID:23335340] minor.

## Curation decisions
- protein binding rows (Vps15, Atg38, Gpa1) REMOVE (captured by complex terms).
- obsolete GO:0034045 -> MODIFY to GO:0000407.
- RCA cytosol -> MODIFY endosome membrane.
- Transcription elongation (PMID:23335340) kept non-core.
