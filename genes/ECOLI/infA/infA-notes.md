# infA (IF1, P69222) — Escherichia coli K-12 notes

## Identity

- UniProt P69222 (IF1_ECOLI), 72 aa, b0884. Initiator Met removed; mature chain 2-72
  [file:ECOLI/infA/infA-uniprot.txt "INIT_MET        1"].
- Single S1-like / OB-fold domain; Pfam PF01176 (eIF-1a), InterPro IPR004368 (TIF_IF1),
  HAMAP MF_00075, NCBIfam TIGR00008 [file:ECOLI/infA/infA-uniprot.txt "Belongs to the IF-1 family"].
- NMR structure: five-stranded beta-barrel, OB fold shared with CspA/CspB
  [PMID:9135158 "The structure of IF1 is characterized by a five-stranded beta-barrel"].
  The OB-fold domain and the Pfam eIF-1a family make IF1 the bacterial counterpart of
  archaeal aIF1A and eukaryotic eIF1A.
- PANTHER PTHR33370 (family name dominated by the chloroplast IF-1 member).

## Function (literature)

- UniProt curated function: essential initiation component, binds near the A site,
  stabilizes IF-2 and IF-3 on the 30S subunit, released when the 50S joins
  [file:ECOLI/infA/infA-uniprot.txt "Binds in the vicinity of the A-site. Stabilizes the binding of IF-2 and IF-3 on the 30S subunit"].
- 16S rRNA footprinting (Moazed et al. 1995): IF-1 protects G530, A1492, A1493, the
  bases protected by A-site tRNA, suggesting IF-1 mimics A-site tRNA
  [PMID:7739034 "IF-1 protects G530, A1492 and A1493 and causes enhanced reactivity of A1408"].
- Crystal structure of IF1 on the 30S subunit (Carter et al. 2001): IF1 occludes the
  A site and flips out A1492/A1493 of h44
  [PMID:11228145 "Binding of IF1 occludes the ribosomal A site and flips out the functionally important bases A1492 and A1493 from helix 44 of 16S RNA"].
  Abstract only cached; abstract does not name the organism of the factor/30S (the
  structure is widely described as Thermus thermophilus 30S); used here only as
  family-level structural support.
- Real-time kinetics (Milon et al. 2012, E. coli): IF3 and IF2 bind first, IF1 joins
  and locks the 30S PIC
  [PMID:22562136 "IF3 and IF2 are the first factors to arrive, forming an unstable 30S-IF2-IF3 complex. Subsequently, IF1 joins and locks the factors in a kinetically stable 30S PIC"].
- Cryo-EM of the complete E. coli 30S IC (Julian et al. 2011): IF1 at the A site, in the
  cleft of the 530 loop, h44 and S12, contacted by the IF2 NTD
  [PMID:21750663 "IF1 is a one-domain compact protein which binds at the A site of the 30S subunit"].
- Fidelity: IF2 and IF1 synergistically recognize the formyl group of fMet-tRNA; IF1 is
  essential in E. coli
  [PMID:16857585 "recognition of the formyl group by the synergistic action of IF2 and IF1"].
- Cold: IF1 levels rise relative to ribosomes after cold shock and IF1 stimulates
  translation in the cold without mRNA selectivity
  [PMID:14730025 "IF1 and the RNA chaperone CspA, which stimulate translation preferentially in the cold without mRNA selectivity, can also contribute to the translational bias"].
  Not annotated in GOA for IF1; not proposed (indirect).

## GOA rows — reasoning summary

- GO:0003743 / GO:0006413: core; ACCEPT.
- GO:0005829 cytosol (IDA PMID:18304323 cytosolic-fraction proteomics; IBA): ACCEPT.
- GO:0005737 cytoplasm (EXP PMID:376343, IEA): correct but general; MODIFY to cytosol,
  which the gene already carries.
- GO:0043022 ribosome binding (IDA PMID:7739034, IEA): MODIFY to GO:0043024 ribosomal
  small subunit binding (all evidence is for 30S binding).
- GO:0003676 nucleic acid binding, GO:0003723 RNA binding: MODIFY to GO:0019843 rRNA
  binding (16S rRNA contacts).
- GO:0019843 rRNA binding: KEEP_AS_NON_CORE (mechanistic contact underlying 30S binding).
- GO:0140517 protein-RNA adaptor activity (IBA, PTN002120760, seeded only by P69222):
  IF1 does not bridge IF2 to rRNA; IF2 binds the 30S before IF1 arrives (PMID:22562136).
  MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI with MqsA, PMID:24561554 binary Y2H screen): REMOVE
  per protein-binding policy.

`just paint-losses ECOLI infA`: no IRD/IKR loss on this lineage.
