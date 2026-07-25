# AANAT (Serotonin N-acetyltransferase) — review notes

UniProt: Q16613 (SNAT_HUMAN). HGNC:19. Gene on chromosome 17. 207 aa, 23.3 kDa.
Synonym: SNAT. EC 2.3.1.87.

## Core identity / function

AANAT is **serotonin N-acetyltransferase**, also called **arylalkylamine
N-acetyltransferase (AA-NAT)** — the pineal "timezyme." It is an
**acetyl-CoA-dependent GNAT-family acetyltransferase** that catalyzes the
**penultimate and circadian rate-controlling step of melatonin biosynthesis**:
N-acetylation of serotonin (5-hydroxytryptamine) to N-acetylserotonin (NAS),
consuming acetyl-CoA and releasing CoA.

- UniProt FUNCTION: "Controls the night/day rhythm of melatonin production in the
  pineal gland. Catalyzes the N-acetylation of serotonin into N-acetylserotonin,
  the penultimate step in the synthesis of melatonin."
  [file:human/AANAT/AANAT-uniprot.txt]
- UniProt CATALYTIC ACTIVITY: "a 2-arylethylamine + acetyl-CoA = an
  N-acetyl-2-arylethylamine + CoA + H(+)"; EC=2.3.1.87; Rhea:RHEA:20497.
  [file:human/AANAT/AANAT-uniprot.txt]
- UniProt PATHWAY: "Aromatic compound metabolism; melatonin biosynthesis;
  melatonin from serotonin: step 1/2." [file:human/AANAT/AANAT-uniprot.txt]
- UniProt SIMILARITY: "Belongs to the acetyltransferase family. AANAT subfamily."
  Domain 35..194 is an N-acetyltransferase (GNAT) domain; PROSITE PS51186 GNAT;
  Pfam PF00583 Acetyltransf_1; PANTHER PTHR10908 SEROTONIN N-ACETYLTRANSFERASE.
  [file:human/AANAT/AANAT-uniprot.txt]

The GNAT (GCN5-related N-acetyltransferase) fold and acetyl-CoA binding residues
(BINDING 124..126, 132..137, 168..170 for acetyl-CoA; SITE 120/122 substrate
deprotonation) confirm classical acetyl-CoA acyltransferase chemistry, not any
role in N-terminal protein acetylation (see over-annotation note below).
[file:human/AANAT/AANAT-uniprot.txt]

## Regulation (the "timezyme" switch)

- Enzyme activity rises sharply at night in the pineal gland; the enzyme is
  rapidly degraded in light. Regulated by cAMP/PKA phosphorylation on Thr-31
  (N-terminal) and Ser-205 (C-terminal), which promote 14-3-3 binding.
  UniProt PTM: "cAMP-dependent phosphorylation on both N-terminal Thr-31 and C-
  terminal Ser-205 regulates AANAT activity by promoting interaction with 14-3-3
  proteins." [file:human/AANAT/AANAT-uniprot.txt]
- UniProt SUBUNIT: "Interacts with several 14-3-3 proteins, including YWHAB,
  YWHAE, YWHAG and YWHAZ, preferentially when phosphorylated at Thr-31 ... The
  interaction with YWHAZ considerably increases affinity for arylalkylamines and
  acetyl-CoA and protects the enzyme from dephosphorylation and proteasomal
  degradation." [file:human/AANAT/AANAT-uniprot.txt] (By similarity, ECO:0000250)
- 14-3-3 binding switch established by Ganguly et al. 2001
  [PMID:11427721, cited in UniProt RN[5]; MUTAGEN Thr-31 T->A: "Loss of activation
  by cAMP." file:human/AANAT/AANAT-uniprot.txt]. Note: PMID:11427721 is not in the
  publications cache; used only via UniProt-quoted evidence.

## cAMP activation of intracellular AANAT (PMID:11313340)

Coon et al. 2001 [PMID:11313340] — the only cached primary paper directly on human
AANAT enzymology. full_text_available: false (abstract only). Key abstract points:
- "Arylalkylamine N-acetyltransferase (serotonin N-acetyltransferase, AANAT, EC )
  is the penultimate enzyme in melatonin synthesis." → supports MF GO:0004059 and
  BP melatonin biosynthesis GO:0030187.
- "1E7 hAANAT ... is immunocytochemically visualized in the cytoplasm." → supports
  CC cytoplasm GO:0005737.
- "treatment with forskolin, dibutyryl cAMP, isobutylmethylxanthine, or
  isoproterenol activate cellular hAANAT within intact 1E7 cells approximately
  8-fold" → supports BP cellular response to cAMP GO:0071320.
This paper is the `original_reference_id` for the UniProt EC=2.3.1.87 and Cytoplasm
subcellular-location experimental evidence.

## Location

- UniProt SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:11313340}."
  [file:human/AANAT/AANAT-uniprot.txt] Also cytosol (IDA:HPA, GO:0005829) and
  perinuclear region of cytoplasm (IDA:UniProtKB, GO:0048471). Consistent — a
  soluble cytosolic enzyme.

## Tissue specificity

- UniProt: "Highly expressed in pineal gland and at lower levels in the retina.
  Weak expression in several brain regions and in the pituitary gland."
  [file:human/AANAT/AANAT-uniprot.txt]

## Circadian rhythm / photoperiod / sleep phenotype

- AA-NAT is "a rate-limiting enzyme in melatonin hormone synthesis and
  participates in daily oscillations of the melatonin level" [PMID:12736803
  abstract]. Hohjoh et al. 2003 report a significant association of the A129T
  (Ala->Thr, position 129) variant with delayed sleep phase syndrome (DSPS)
  [PMID:12736803; UniProt VARIANT 129 A->T, VAR_055086]. Supports involvement in
  circadian rhythm (IMP GO:0007623).
- IBA (PAN-GO) supports circadian rhythm and photoperiodism from the AANAT
  ortholog family. Photoperiodism, response to light stimulus are well-established
  for the AANAT family (pineal light gating) but in human are IBA/IEA-level; kept
  as non-core.

## Interactions (large-scale binary screens)

Bare "protein binding" (GO:0005515) IPI annotations come from high-throughput
binary interactome screens, mapping AANAT (Q16613 / bait EBI-7451846) to partners
such as BHLHE40 (O14503), MDFI (Q99750), GRB10 (Q13322-4), KRTAP8-1 (Q8IUC2),
EIF4E3 (Q8N5X7-2):
- PMID:25416956 (Rolland et al., human interactome map) — full_text_available: true
  but AANAT-specific partners only in supplementary data.
- PMID:25910212 (Sahni et al., interaction perturbations in genetic disorders).
- PMID:32296183 (Luck et al., HuRI reference interactome).
These do not identify a specific molecular function; kept as non-core
(MARK_AS_OVER_ANNOTATED for bare protein binding per policy). The biologically
meaningful interaction is with 14-3-3 (YWHAB/E/G/Z), captured separately by the
14-3-3 protein binding annotation (GO:0071889).

## Over-annotation flags

- **GO:0006474 N-terminal protein amino acid acetylation (IDA, PMID:11313340)**:
  AANAT acetylates the primary amine of small-molecule arylalkylamines (serotonin),
  NOT the alpha-amino group of protein N-termini. The cited paper is about
  intracellular activation of serotonin N-acetyltransferase activity, not
  N-terminal protein acetylation. This is an over-annotation (likely a
  misclassification of "N-acetylation" activity). It is an experimental (IDA)
  annotation, so per policy MARK_AS_OVER_ANNOTATED (not REMOVE).
- **GO:0004060 arylamine N-acetyltransferase activity (IEA:Ensembl, in UniProt DR
  but not in the current goa.tsv)**: this is a different NAT (NAT1/NAT2-type,
  aromatic amine acetylation) and would be a wrong-branch over-annotation; it is
  not present in the seeded goa.tsv so not reviewed here.
- The Ensembl orthology-transfer (GO_REF:0000107) BP terms — response to zinc/
  copper/calcium ion, insulin, cytokine, prostaglandin E, corticosterone, cAMP,
  peptide — are transferred from rat AANAT (Q64666). These describe stimuli that
  modulate pineal AANAT in rodent physiology; they are peripheral to the human
  gene's core function and are kept as non-core.

## Core function summary (for core_functions)

1. MF: aralkylamine N-acetyltransferase activity (GO:0004059) — serotonin
   N-acetyltransferase, acetyl-CoA-dependent (EC 2.3.1.87).
2. BP: melatonin biosynthetic process (GO:0030187) — penultimate step,
   serotonin -> N-acetylserotonin.
3. BP: circadian rhythm (GO:0007623) — rate-controlling, night-elevated,
   couples melatonin output to the clock/photoperiod.
4. CC: cytosol (GO:0005829) / cytoplasm — soluble cytosolic enzyme.

14-3-3 protein binding (GO:0071889) is a genuine, functionally important
regulatory interaction (stabilization/activation) but is regulatory, not the
catalytic core; noted but not listed as a core MF, and bare "protein binding"
is excluded from core functions.
