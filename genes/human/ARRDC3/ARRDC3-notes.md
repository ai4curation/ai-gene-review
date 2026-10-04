# ARRDC3 review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:20559325: ARRDC3 recruits NEDD4 to beta2AR via PPxY.
  - PMID:23208550: ARRDCs are secondary adaptors that traffic Nedd4-beta2AR to early endosomes. This contrasts with the first paper and is presented in the adaptor MODIFY.
  - PMID:23236378 (full text): alpha-arrestins recruit Nedd4 E3s; ARRDC3 at plasma membrane and endosomes.
  - PMID:21982743: mouse knockout; beta-adrenergic receptor binding.
  - PMID:20603614: ITGB4.
  - PMID:29364502: YAP.
- 67 protein-binding rows were resolved by UniProt batch query.
  - NEDD4/NEDD4L/ITCH/WWP1/WWP2 rows → MODIFY to ubiquitin protein ligase binding.
  - ADRB2 → beta-2 adrenergic receptor binding.
  - ITGB4 → integrin binding.
  - All others → REMOVE.
- The IBA node PTN008513893 (endosome, plasma membrane) is seeded only by ARRDC3 itself (Q96B67).

## Decisions
- ACCEPT: plasma membrane, endosome, early endosome; beta-3 adrenergic receptor binding.
- MODIFY: molecular adaptor activity (IBA) → ubiquitin-like ligase-substrate adaptor activity, the core MF.
- KEEP_AS_NON_CORE:
  - Lysosome, cytoplasm.
  - Hippo regulation, positive regulation of ubiquitin-protein transferase activity.
  - Cold-induced thermogenesis (mouse ISS/IEA).

## 2026-10-04 review round (PR #4208)

- Deep-research coverage: cached and cited nine papers (see history). AXL and insulin-receptor cargo claims are not checked (papers not cached).
- Thermogenesis: [PMID:28291835 "Additionally, canonical β-adrenergic receptor signaling was not different in Arrdc3-null adipocytes."] disputes the PMID:21982743 mechanism; the phenotype stands.
- beta2AR: [PMID:27226565 "Although ARRDC3 has no effect on β2AR endocytosis or degradation, it negatively regulates β2AR entry into SNX27-occupied endosomal tubules."] contrasts with PMID:20559325.
- Receptor-downregulation BP: no NEW process. ARRDC3 ubiquitinates the sorting factor ALIX rather than PAR1, and β2AR degradation data conflict. Added GO:0016567 instead, after a comparator check: ARRDC1, ARRDC4, ARRB1 and ARRB2 all carry it.
