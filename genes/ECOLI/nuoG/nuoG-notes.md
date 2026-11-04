# nuoG (E. coli K-12, P33602) notes

## 2026-10-23 review

Deep-research providers are unavailable in this environment (no API keys), so
the literature was reviewed manually from cached `publications/PMID_*.md` files
and the UniProt record. Full text cached for PMID:17640900, PMID:18603533,
PMID:18316732, PMID:9495756, PMID:24561554, PMID:34308841; the rest are
abstract-only. Newly cached: PMID:16469879 (Sazanov & Hinchliffe 2006, abstract
only; PMID verified via NCBI esummary).

- NuoG is the complex I 75 kDa family subunit
  [file:ECOLI/nuoG/nuoG-uniprot.txt "Belongs to the complex I 75 kDa subunit family."]
  in the peripheral sector [file:ECOLI/nuoG/nuoG-uniprot.txt "Subunits NuoCD, E, F, and G constitute the peripheral sector of the complex."].
- Clusters: [2Fe-2S] N1b [PMID:17640900 "we attribute EPR signal N1b to 2Fe[G]"];
  [4Fe-4S] N4 and N7 [PMID:15520003 "The former signal was assigned to cluster N4, and the latter signal was assigned to cluster N1c because of their disappearance in Delta N4 and Delta N1c."];
  His(Cys)3 N5 [PMID:18603533 "no cluster N5 signals were found in any of the N5 mutants, whereas EPR signals from all other clusters were detected"].
  (Note PMID:17640900 argued N4 is on NuoI; PMID:18603533 maintains N4/N5 on NuoG. Either way NuoG binds 1x[2Fe-2S] + 3x[4Fe-4S].)
- N1b, N4, N5 are on the main path [PMID:18603533 "These seven Fe/S clusters are lined up to form the main electron transfer pathway"];
  N7 is off-path and structural [PMID:17489563 "Thus, N7 is essential for the stability of the complex but is not involved in electron transfer."].
- FMN is in NuoF [PMID:18603533 "The primary electron acceptor of complex I is a noncovalently bound flavin mononucleotide (FMN) located in the NuoF subunit."];
  the contributes_to FMN binding IDA row is marked over-annotated (not removed, experimental, abstract-only paper).
- Molybdopterin: NuoG carries InterPro/Pfam molybdopterin-oxidoreductase domain
  signatures (IPR006656, IPR006657, PF00384, PF01568) reflecting shared ancestry
  with formate dehydrogenase/nitrate reductase (PANTHER PTHR43105), but complex I
  contains only FMN and Fe-S redox centres
  [PMID:16469879 "This subcomplex consists of eight subunits and contains all the redox centers of the enzyme, including nine iron-sulfur clusters.";
  PMID:7607227 "The preparation contains one noncovalently bound FMN/molecule."]. GO:0043546 REMOVEd.
- E. coli G-loop insertion stabilises peripheral arm interfaces
  [PMID:34308841 "the G-loop fills a crevice between NuoCD, NuoI, and NuoG subunits"].
- NuoG is essential [PMID:9495756 "we present evidence that NuoG, a peripheral subunit, is essential for complex I function"].

## Decisions

- Protein binding IPI rows (NuoCD, NuoE partners): REMOVE per protein-binding
  policy (intra-complex contacts; membership captured by GO:0045271).
- Generic MF terms (GO:0003954, GO:0016491, GO:0016651) MODIFY to GO:0008137;
  GO:0016020 to GO:0005886; GO:0030964 and GO:1990204 to GO:0045271;
  GO:0051536 to GO:0051537 + GO:0051539; GO:1902600 to GO:0015990.
- NEW GO:0009055 electron transfer activity (IDA, PMID:18603533) as the module
  leaf function; core functions use contributes_to GO:0008137.
- Cytoplasm, aerobic respiration, cellular respiration, ATP synthesis coupled
  electron transport kept as non-core.
