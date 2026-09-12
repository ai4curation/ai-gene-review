# ATPAF2 (ATP12 homolog) review notes

UniProt: Q8N5M1 (ATPF2_HUMAN), 289 aa, Precursor with N-terminal mitochondrial
transit peptide (1-40). HGNC:18802. Gene on 17p11.2. Belongs to the ATP12 family
(Pfam PF07542; InterPro IPR011419).

## Core biology (verified)

ATPAF2 is the human ortholog of yeast Atp12p. It is a **molecular chaperone /
assembly factor for the F1 sector of the mitochondrial ATP synthase (Complex V)**.
It binds the unassembled **F1 alpha subunit (ATP5F1A)** during assembly and
prevents non-productive self-aggregation of the alpha subunit, promoting formation
of the alpha3-beta3 catalytic core. It is **non-catalytic** (a chaperone, not an
enzyme).

- PMID:14701807 (Hinton, Gatti, Ackerman 2004) — human Atp12p in vitro:
  "Atp12p binds to unassembled alpha subunits of F(1) and in so doing prevents the
  alpha subunit from associating with itself in non-productive complexes during
  assembly of the F(1) moiety of the mitochondrial ATP synthase." Recombinant
  HuAtp12p was shown to have chaperone activity: "Wild type HuAtp12p suppresses the
  aggregation of thermally inactivated citrate synthase." Basis for the IDA
  GO:0044183 protein folding chaperone (MF) annotation.
- PMID:11410595 (Wang, White, Ackerman 2001) — cloned human ATP11/ATP12; "Atp11p
  and Atp12p were first described as proteins required for assembly of the F(1)
  component of the mitochondrial ATP synthase"; "the human proteins function like
  their yeast counterparts." Reports interaction with an F1 subunit (UniProt SUBUNIT:
  interacts with ATP5F1B; IntAct IPI with ATP5F1A P25705 and ATP5F1B P06576).
- PMID:14757859 (De Meirleir et al. 2004) — first pathogenic mutation in a human
  nuclear-encoded ATPase assembly gene; ATP12/ATPAF2 W94R causes respiratory chain
  complex V deficiency (MC5DN1; MIM:604273), a severe encephalopathy /
  encephalomyopathy phenotype. "revealed a mutation in the ATP12 assembly gene in
  one patient. This mutation is believed to be the cause of the impaired complex V
  activity."

## Localization

UniProt SUBCELLULAR LOCATION: Mitochondrion inner membrane; Peripheral membrane
protein (PMID:11410595). As an F1-assembly chaperone acting on the soluble F1 sector,
it functions on the matrix face of the inner membrane — anatomical location for the
review is the **mitochondrial matrix (GO:0005759)** per curation directive. GOA also
carries HTP mitochondrion (PMID:34800366) and IEA/IBA mitochondrion/inner-membrane.
The **GO:0016607 nuclear speck (IDA, LIFEdb GFP-fusion)** annotation is inconsistent
with the mitochondrial-matrix biology and is an over-annotation artifact of an
overexpressed fusion construct.

## Annotation-set observations

- Many `GO:0005515 protein binding` IPI rows come from large-scale Y2H / AP-MS /
  interactome studies (PMID:21516116, 25416956, 25910212, 28514442, 29892012,
  31515488, 32296183, 33961781, 40205054) and capture many non-physiological
  partners (zinc-finger TFs, keratins/KRTAPs, nuclear proteins). These are
  uninformative bare `protein binding` -> MARK_AS_OVER_ANNOTATED (retain, not remove).
- The functionally meaningful interactions are with F1 subunits ATP5F1A (P25705) and
  ATP5F1B (P06576) (PMID:11410595, 27499296, 29892012, 31515488, 40205054) and with
  the assembly co-factor FMC1 (Q96HJ9; PMID:28719601).
- GO:0044183 protein folding chaperone (IDA, PMID:14701807) is the informative MF and
  the core molecular function.
- Assembly BP: GO:0033615 mitochondrial proton-transporting ATP synthase complex
  assembly (specific) and GO:0043461 proton-transporting ATP synthase complex
  assembly (parent) both apply.

## Deep research

falcon deep-research is OUT OF CREDITS (402); no -deep-research-falcon.md generated.
Grounded instead in UniProt (Q8N5M1), seeded GOA, and cached publications.
