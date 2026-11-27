# PA2986 (Q9HZL8) notes

Second LolC/LolE-family permease subunit of the P. aeruginosa LolCDE lipoprotein-release ABC
transporter (PA2986-PA2987 lolD-PA2988). No deep-research provider was available; literature
search was by hand (PubMed metadata and abstract for PMID:17350955; QuickGO for the E. coli
seeds). See PA2988-notes.md for the shared literature summary.

## Literature

- Tanaka, Narita & Tokuda 2007 (PMID:17350955; abstract only): purified P. aeruginosa LolCDE
  reconstituted in proteoliposomes released lipoproteins to LolA in an ATP-dependent manner
  ["When incubated in the presence of ATP and a LolA homologue, the reconstituted LolCDE homologue
  released lipoproteins, leading to the formation of a LolA-lipoprotein complex."].
- UniProt Q9HZL8 (unreviewed): four Phobius TM helices, MacB-like periplasmic core, TIGR02212.

## Review decisions

- GO:0044874 IDA and IBA: ACCEPT (core).
- GO:0042953 lipoprotein transport IDA and IEA: ACCEPT.
- GO:0089705 protein localization to outer membrane IDA: MODIFY to GO:0044874 (lipoprotein-
  specific; GO:0044874 is not an is_a child of GO:0089705 so TOO_GENERAL does not apply).
- GO:0016020: MODIFY to GO:0005886. GO:0098797 IBA: MODIFY to GO:0043190.
- NEW GO:0140306 lipoprotein releasing activity (IDA, PMID:17350955).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002524722 | GO:0044874 lipoprotein localization to outer membrane | 4 | 46 (26 taxa) | GO:0044874, IDA, PMID:17350955 (PseudoCAP only) | SOUND | Same reconstitution of purified P. aeruginosa LolCDE as for PA2988; direct evidence for the complex containing PA2986. | E. coli LolC P0ADC3, LolE P75958 (IDA); PA2988 Q9HZL6 (SOUND) | Yes; node record in genes/PSEAE/PA2988/PA2988-notes.md |

No PSEUDOCAP or GO_CENTRAL defect. The other PseudoCAP rows citing the same paper (GO:0042953,
GO:0089705) are sound; GO:0089705 is only less specific.
