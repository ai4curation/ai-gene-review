# MLO (barley, P93766) curation notes

## 2026-10-02 — initial review

Sources: UniProt P93766, GOA (2 IEA rows), falcon deep research, cached abstracts
(PMID:9054509, 10574976, 11919636, 12114562, 15703292, 15352871, 28095124) and full text
(PMID:20170486, 36588121). Most barley papers are cached as abstracts only.

### Identity / structure
- Plant-specific 7-TM protein, N-terminus outside, C-terminus inside, plasma membrane
  [PMID:10574976 "Mlo is membrane-anchored by 7 transmembrane (TM) helices such that the N terminus is located extracellularly and the C terminus intracellularly"]
  [PMID:10574976 "Fractionation of leaf cells and immunoblotting localized the protein to the plant plasma membrane."]
- Self-associates in planta [PMID:15352871 "FRET (fluorescence resonance energy transfer) analysis revealed evidence for in planta MLO dimerization/oligomerization."]
- Biochemical activity unknown for barley MLO [PMID:20170486 "Mlo codes for a member of a plant-specific family of polytopic integral membrane proteins with unknown biochemical activity."]

### Molecular function evidence
- Ca2+-dependent calmodulin binding [PMID:11919636 "We have identified a domain in MLO that mediates a Ca2+-dependent interaction with calmodulin in vitro."]
  and in vivo FRET [PMID:15703292 "an increase in MLO/calmodulin FRET around penetration sites coincident with successful host cell entry"].
  Not in GOA -> proposed NEW GO:0005516.
- Channel hypothesis: Arabidopsis paralogs are Ca2+ channels
  [PMID:36588121 "We identified MILDEW RESISTANCE LOCUS O (MLO) family proteins MLO1, 5, 9, 15, as Ca2+ channels required for Ca2+ influx and pollen tube integrity."].
  Deep research cites a 2026 bioRxiv preprint (modeling) and reported Ba2+/Mg2+ currents for HvMLO, but no peer-reviewed barley conductance data in the cache. Not annotated; raised as a question.

### Biological role
- Susceptibility factor: wild-type MLO enables fungal entry; loss gives resistance
  [PMID:15703292 "Barley mildew resistance locus o (Mlo) is required for host cell invasion upon attack by the ascomycete powdery mildew fungus"].
- Negative regulation of defense / cell death
  [PMID:12114562 "Wild-type MLO dampens the cell wall-restricted hydrogen peroxide burst at points of attempted fungal penetration of the epidermal cell wall"]
  [PMID:11919636 "Loss of calmodulin binding halves the ability of MLO to negatively regulate defence against powdery mildew in vivo."].

### Decisions
- GO:0006952 defense response (IEA, InterPro2GO): MODIFY -> GO:0031348 negative regulation
  of defense response. Sign of the IEA is wrong for the wild-type protein. Comparator:
  Arabidopsis MLO2 carries GO:0031348 (TAIR IMP, acts_upstream_of_or_within). No
  "negative regulation of defense response to fungus" term exists (checked QuickGO/OLS).
  Did NOT propose "defense response to fungus": that would assert MLO executes defense,
  which is a necessity/phenotype inversion.
- GO:0016020 membrane (IEA): MODIFY -> GO:0005886 plasma membrane.
- NEW GO:0005516 calmodulin binding (IDA, PMID:11919636).

### Open questions
- Does HvMLO conduct Ca2+? If yes, calcium channel activity should become the core MF.
- Is the regulatory process term overreaching given purely genetic evidence?
