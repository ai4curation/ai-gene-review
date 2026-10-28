# LOC542140 notes

## 2026-10-28 session

- Task target: A0A804M424. `just fetch-gene MAIZE LOC542140` first resolved A0A804M423 (sibling
  TrEMBL entry, transcript Zm00001eb057440_T002, 660 aa, 4 GOA rows). A0A804M424 is the GeneID
  542140 / RefSeq-mapped entry of the same EnsemblPlants gene Zm00001eb057440, with 6 GOA rows
  including 2 IBA rows. I re-fetched with `--uniprot-id A0A804M424 --force` and reviewed that entry.
- Gene = ZmGT1 (NCBI alias). Confirmed by sequence: 99.6% identical to FJ573212
  (`LOC542140-bioinformatics/RESULTS.md`).
- Key papers PMID:22792398 and PMID:23144728 are expression-only (RT-PCR induction by herbicides
  and a safener). The transport claim (GSH/GS-conjugate uptake in yeast) rests on the authors' own
  earlier work, which is not in PubMed:
  [PMID:23144728 "Our earlier work has shown that ZmGT1 is able to mediate the uptake of both GSH and GS conjugates by yeast cells"].
- Closest characterised ortholog: AtOPT3 (80.3% identity), a phloem plasma-membrane Fe/Cd/Cu
  transporter (PMID:24867923, PMID:24880337, PMID:36814393).
- Decisions:
  - The oligopeptide transporter MF rows (IBA, IEA) and the derived BP row are UNDECIDED. GSH is a
    tripeptide, and GO:0034634 glutathione transmembrane transporter activity is_a GO:0042937
    tripeptide transmembrane transporter activity is_a GO:0035673 (checked with OLS). So the claimed
    activity would make the oligopeptide term true, but that claim cannot be inspected. The OPT3 clade
    is characterised as a metal transporter, and OPT3 fails to reach the yeast plasma membrane.
  - Plasma membrane (IBA): ACCEPT. Membrane (IEA): MODIFY to plasma membrane.
    Transmembrane transport: ACCEPT, because it is as precise as the evidence allows.
  - No NEW terms. Detoxification and herbicide response rest on expression data only, which does not
    meet the NEW bar. Possible iron transport by orthology is raised as a question instead.
