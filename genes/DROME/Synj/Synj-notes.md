# Synj (Drosophila melanogaster, Q5U0V7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this review.

### Identity
- Benchmark accession Q5U0V7 (TrEMBL, unreviewed, PE 2) is 1218 aa, from cDNA BT016135, and has
  RefSeq NP_569729/NP_726155/NP_001246454. It is the full-length FlyBase Synj (FBgn0034691, CG6562)
  product, with an N-terminal SAC domain (PROSITE PS50275, 120-455), a central IPPc 5-phosphatase,
  a SYNJ1/2 RRM-like module (IPR015047) and a disordered proline-rich C-terminus (1006-1218).
- The only other UniProt entry for the gene is Q8MR94 (959 aa, also unreviewed). No Swiss-Prot
  entry exists. Q5U0V7 is the longest and most complete product, so it is not a fragment or
  isoform problem. Catalytic motifs of both domains are intact
  (Synj-bioinformatics/RESULTS.md: SAC CLDCLDRT at 396; 5-ptase WCGDFNYR at 737, PAWTDRV at 812).
  Fly R228 (the residue of the R228Q knock-in) aligns to human canonical O43426 R219.

### Evolutionary placement
- PANTHER PTHR11200:SF257 ("PHOSPHOINOSITIDE 5-PHOSPHATASE") contains fly Synj, worm UNC-26
  (G5ECL2), yeast INP52/INP53 and S. pombe syj1. Vertebrate SYNJ1 (SF158) and SYNJ2 (SF148) sit
  in their own subfamilies, so SF257 is the non-vertebrate synaptojanin subfamily.
- The PAINT synaptojanin node PTN000878538 (synaptic vesicle endocytosis) is seeded by Synj itself,
  unc-26, mouse Synj1 and human SYNJ1/SYNJ2, so it spans the vertebrate and invertebrate
  synaptojanins. The PI(4,5)P2 5-phosphatase node PTN008514002 is deeper (whole family).
  The Ins(1,4,5)P3 node PTN002597976 is seeded by rat Synj1/Synj2, human SYNJ1 and pombe syj1.
- Family review interpro/panther/PTHR11200/PTHR11200-review.yaml lists Q5U0V7 under SF257, which
  agrees with UniProt. No placement disagreement.

### Key literature (cached)
- PMID:14622578 (Verstreken 2003): presynaptic localization, vesicle association, Endophilin
  recruitment, endocytic defects.
- PMID:16269341 (Dickman 2005): synj/endo nulls retain slowed classical endocytosis at 10-20% of the
  wild-type rate; Synj and Endo "function to uncoat vesicles".
- PMID:24977345 (Chen 2014), PMID:27559170 (Geng 2016): direct TLC assay of fly Synj 5-phosphatase
  (PI(4,5)P2 to PI(4)P); Mnb phosphorylates S1029 and enhances activity.
- PMID:34596663 (Peng 2021): the 5-phosphatase is required for CME; in ADBE the 5-phosphatase
  suppresses and SAC promotes; calcineurin dephosphorylates S1029.
- PMID:28331029 (Vanhauwaert 2017): SAC R228Q knock-in blocks presynaptic autophagosome maturation
  (Atg18a retention) with endocytosis intact.
- PMID:30541947 (Ahaley 2018): wing-disc RNAi raises PI(4)P and Smo activation. Not annotated:
  knockdown-only and plausibly indirect (see suggested_questions).
- PMID:10224048 (Guo 1999): SAC-like domains of synaptojanin/Inp52/Inp53 are PI(3)P/PI(4)P/PI(3,5)P2
  phosphatases.

### Decisions changed vs the previous file
- nucleic acid binding (IEA, IPR035979 superfamily): UNDECIDED changed to REMOVE. This is a fold-level
  match to the synaptojanin RRM-like module, with no nucleic-acid binding evidence.
- membrane (IBA): ACCEPT changed to MODIFY, replaced by vesicle membrane (GO:0012506, which FlyBase also
  has by IDA).
- phosphatase activity (IEA): MODIFY now proposes both GO:0004439 and GO:0043812, because the
  InterPro sources include both IPPc and SAC.
- synapse (IEA): ACCEPT changed to MODIFY, replaced by presynapse.
- Ins(1,4,5)P3 5-phosphatase (IBA): UNDECIDED changed to KEEP_AS_NON_CORE. The PAINT node is
  synaptojanin-seeded and there is no evidence of loss, but the physiological fly substrates are lipids.
- NEW: GO:0016191 synaptic vesicle uncoating. Comparator check: worm unc-26 IMP and mouse Synj1
  IDA/IMP carry it.
- NEW: GO:0043812 PI4P phosphatase (SAC). NEW: GO:0097352 autophagosome maturation (non-core,
  SAC-dependent lipid remodelling on the autophagosome).
- The description and core_functions were rewritten (two catalytic modules).

### Upstream annotations not in the GOA seed
UniProt DR GO lines show FlyBase IDA/IMP/ISS rows that are absent from Synj-goa.tsv: autophagosome,
autolysosome, terminal bouton, type I terminal bouton, vesicle membrane, PI3P/PI4P/PIP 5-phosphatase
ISS, bulk and clathrin-dependent SV endocytosis, maintenance of presynaptic active zone structure,
negative regulation of smoothened signaling, positive regulation of autophagosome assembly, and
regulation of synapse structure or activity. These were not reviewed as rows, because they are not
in the seed. The new MF/BP rows overlap them, and the Hedgehog regulation row is deliberately not
proposed.

### Relative for next review
Closest characterized relative by PANTHER subfamily (SF257) and PAINT node PTN000878538 is worm
unc-26 (G5ECL2), which already has a complete review (genes/worm/unc-26). Human SYNJ1 (O43426,
SF158) is the best-characterized vertebrate co-ortholog but sits in a different subfamily, and the
repo has no review of it yet.

### Modules
modules/synaptic_vesicle_endocytosis.yaml (uncoating step, annoton synaptojanin_pip2_phosphatase,
PTHR11200); modules/synaptic_vesicle_cycle.yaml (mentions synaptojanin uncoating).
