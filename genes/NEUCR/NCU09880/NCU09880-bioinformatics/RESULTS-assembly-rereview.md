# NCU09880 (Q7S234) re-review: Sm-assembly factor homologs and SmG subfamily placement

Script: `assembly_factor_homologs_rereview.py` (run with `uv run --script assembly_factor_homologs_rereview.py`; live UniProt queries).

Output (2026-10-21):

```
PF06003	SMN	hits=0
PF20635	SMN Gemin2-binding domain	hits=1
  Q7RY22	NCU01700	Survival Motor Neuron Gemin2-binding domain-containing protein	149
PF04938	SIP1 (Gemin2/Brr1)	hits=1
  Q7SI32	NCU00620	Uncharacterized protein	526
Q7S234 Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 /
  DR   PANTHER; PTHR10553; SMALL NUCLEAR RIBONUCLEOPROTEIN; 1.
  DR   PANTHER; PTHR10553:SF2; SMALL NUCLEAR RIBONUCLEOPROTEIN G; 1.
P40204 Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  DR   PANTHER; PTHR10553; SMALL NUCLEAR RIBONUCLEOPROTEIN; 1.
  DR   PANTHER; PTHR10553:SF2; SMALL NUCLEAR RIBONUCLEOPROTEIN G; 1.
O74966 Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
  DR   PANTHER; PTHR10553; SMALL NUCLEAR RIBONUCLEOPROTEIN; 1.
  DR   PANTHER; PTHR10553:SF2; SMALL NUCLEAR RIBONUCLEOPROTEIN G; 1.
Q9VXE0 Drosophila melanogaster (Fruit fly).
  DR   PANTHER; PTHR10553; SMALL NUCLEAR RIBONUCLEOPROTEIN; 1.
  DR   PANTHER; PTHR10553:SF2; SMALL NUCLEAR RIBONUCLEOPROTEIN G; 1.
P62308 Homo sapiens (Human).
  DR   PANTHER; PTHR10553; SMALL NUCLEAR RIBONUCLEOPROTEIN; 1.
  DR   PANTHER; PTHR10553:SF26; SMALL NUCLEAR RIBONUCLEOPROTEIN G-RELATED; 1.
```

Interpretation: Neurospora crassa encodes one protein with the SMN Gemin2-binding domain (NCU01700, Q7RY22) and one SIP1-family (Gemin2/Brr1) protein (NCU00620, Q7SI32), so an SMN-Gemin2 Sm-assembly machinery is plausibly present in this organism; neither has been characterised experimentally. No protein carries the full SMN Pfam PF06003 signature. Q7S234 shares PANTHER subfamily PTHR10553:SF2 with budding-yeast SMX2 (P40204), fission-yeast smg1 (O74966) and Drosophila SNRPG (Q9VXE0); human SNRPG (P62308) is placed in the separate subfamily PTHR10553:SF26 (SMALL NUCLEAR RIBONUCLEOPROTEIN G-RELATED), alongside the human SNRPG pseudogene products.
