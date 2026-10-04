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
