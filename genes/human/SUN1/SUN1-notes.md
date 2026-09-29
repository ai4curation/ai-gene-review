# SUN1 review notes

## 2026-09-27 (claude-code)

Sources: UniProt O94901, cached GOA-cited publications, PMID:19874786, PMID:17724119, SUN1-deep-research-falcon.md.

- Type II INM protein [PMID:17724119 "Topological analyses indicate that Sun1 is a type II integral protein of the INM"].
- Binds KASH of nesprins 1-3 [PMID:18396275 "the KASH domains of Nesprins 1, 2 and 3 interact promiscuously with luminal domains of Sun1 and Sun2"].
- SUN1-KASH1/4/5 6:6 structures [PMID:33393904 "SUN1-KASH4, SUN1-KASH5, and SUN1-KASH1 form 6:6 complexes in solution"]; SUN1-KASH6 9:6 [PMID:38291267].
- Nucleokinesis/INM, redundant with SUN2 [PMID:19874786 "We show that SUN1 and SUN2 redundantly form complexes with Syne-2 to mediate the centrosome-nucleus coupling during both INM and radial neuronal migration in the cerebral cortex"].
- NPC distribution [PMID:17724119 "Cells that are either depleted of Sun1 by RNA interference or that overexpress dominant-negative Sun1 fragments exhibit clustering of NPCs"].
- Deep research (Falcon) agrees: core = LINC INM anchor; also NPC/mRNA export (NXF1), meiotic telomere tethering via KASH5, laminopathy modifier. Used as retrieval support only.

Term notes
- GO:0034993 (meiotic LINC) is_a GO:0106094 (verified QuickGO). Rows from somatic SUN-KASH papers were MODIFIED to GO:0106094;
  IBA/ARBA and the SUN1-KASH5 structure row kept at GO:0034993 because SUN1 has a genuine meiotic role.
- PMID:22632968 and PMID:33058875 are SUN2 structural papers (full text); SUN1 not directly assayed.
- No KASH-domain-binding MF term exists; SUN-KASH protein binding rows modified to GO:0140444.
