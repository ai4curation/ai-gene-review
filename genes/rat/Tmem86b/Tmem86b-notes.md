# Tmem86b (rat) review notes

- Fetched B0BNF0 (Swiss-Prot, RGD:1593455, GeneID 690610); GOA keyed to B0BNF0, 21 rows.
- Key paper PMID:21515882 (full text): rat liver microsomal lysoplasmalogenase purified and
  identified as Tmem86b; cloning experiments used the human cDNA (NP_776165).
- Core function: lysoplasmalogenase (GO:0047408, EC 3.3.2.2) acting on both choline and
  ethanolamine lysoplasmalogens [PMID:21515882 "Lysoplasmalogenase (EC 3.3.2.2 and EC 3.3.2.5)
  is an enzyme that catalyzes hydrolytic cleavage of the vinyl ether bond of lysoplasmalogen"].
  The ethanolamine-specific GO term GO:0047409 is obsolete (EC 3.3.2.5 merged into 3.3.2.2), so
  GO:0047408 is the only live activity term.
- No "ether lipid catabolic process" or "plasmalogen catabolic process" term exists; GO:0046485
  ether lipid metabolic process is as precise as GO allows.
- GO:0047826 D-lysine 5,6-aminomutase activity: wrong term on the human donor Q8N661 (IDA:UniProtKB
  citing PMID:21515882) and propagated to rat by PAINT IBA (PTN000785233), UniProt ISS and RGD ISO.
  Removed and recorded as source defects (UniProt for the donor/ISS, GO_Central for the IBA, RGD
  for the ISO).
- Generic membrane and cytoplasm rows modified to ER membrane (GO:0005789): microsomal enzyme,
  eight TM helices, paralog TMEM86A ER-localised.
- Identical protein binding: human IntAct self-interaction plus possible dimer band on Western;
  kept as non-core.
- No NEW process terms proposed: KO lipidomics (PMID:40245986) shows necessity for normal
  plasmalogen levels, already captured by the activity and GO:0046485.
