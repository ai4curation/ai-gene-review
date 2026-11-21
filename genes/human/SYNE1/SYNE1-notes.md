# SYNE1 review notes

## 2026-09-27 (claude-code)

- Core function: KASH protein of the LINC complex; KASH1 binds SUN1/SUN2 [PMID:18396275 "the KASH domains of Nesprins 1, 2 and 3 interact promiscuously with luminal domains of Sun1 and Sun2."];
  structures of SUN2-KASH1 and SUN1-KASH1 [PMID:22632968; PMID:33393904]. N-terminal CH domains bind actin [PMID:12408964].
  -> GO:0140444 cytoskeleton-nuclear membrane anchor activity at GO:0005640 nuclear outer membrane, part of GO:0106094.
- GOA uses GO:0034993 (meiotic) for the LINC complex; evidence is somatic/structural so MODIFY -> GO:0106094 (matches module choice).
- SUN1/SUN2 protein-binding rows MODIFY -> GO:0140444; emerin, DISC1, TMEM258 rows REMOVE.
- Neuronal migration: in mouse, Syne-2 alone is essential in cortex/hippocampus; Syne-1 acts redundantly with Syne-2 in midbrain, cerebellum, hindbrain
  [PMID:19874786 "Syne-1 and Syne-2 act redundantly in the midbrain, the cerebellum and the hindbrain"]; Syne-1 antibody co-IPs dynein from brain,
  isoform not resolved. Nesprin-1 is a weaker nucleokinesis participant in cortex than nesprin-2.
- Isoform-specific locations (Golgi, P-body, sarcomere, nucleus, lamin binding via myne-1) kept as non-core.
- Nucleolus IDA (PMID:24862572, abstract only; abstract does not mention nucleolus) left UNDECIDED.
- Falcon deep research used for muscle nuclear-shape/spacing statements (Leong 2023 via deep research).

## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- Two GO:0005794 rows: IDA PMID:12808039 (Gough et al. 2003) and IEA GO_REF:0000044 mapped from the
  UniProt item "[Isoform GSRP-56]: Golgi apparatus" (ECO:0000269, PMID:16875688).
- PMID:12808039 (full text in cache): tagged fragments co-stain Golgi ankyrin, KDEL receptor and p58;
  specificity-controlled antibodies stain endogenous Syne-1 with p58 and beta-COP in MDBK and human LB10
  cells [PMID:12808039 "These immunoreactive structures costained with antibodies to two markers of the
  Golgi complex, p58"]; endogenous protein leaves mannosidase II-positive membranes after brefeldin A
  [PMID:12808039 "bSyne-1 rapidly dissociates from Golgi membranes after 10-min treatment with BFA"].
- PMID:16875688 fetched; abstract only (no PMC record). Abstract reports endogenous 56-kDa GSRP-56
  predominantly in the Golgi of cardiomyocytes and C2C12 cells.
- Verdict: root supported, both rows KEEP_AS_NON_CORE (recruited, BFA-sensitive pool; core function is
  LINC at the nuclear envelope). Earlier "isoform-specific" wording softened: Gough also saw Golgi
  staining with antibodies to an upstream peptide. Added a SUSPECTED/CHECK source defect on the IEA row
  (no gene product form although the UniProt line names isoform GSRP-56, Q8NF91-12). No NEW
  sub-compartment row (markers span cis, medial and coat; recruited protein stays at the root).
