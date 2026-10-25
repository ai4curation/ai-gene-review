# NORK (DMI2 / MtSYMRK), Medicago truncatula, Q8L4H4: notes

## Sources
- UniProt Q8L4H4 (Swiss-Prot). Falcon deep research (`NORK-deep-research-falcon.md`).
- Cached PMIDs. Only 28267253 and 11006338 have full text; the others are abstract-only.

## Identity and architecture
- Signal peptide 1-29, malectin-like domain, 4 LRRs (408-500), TM 522-542, kinase domain 596-873 (UniProt).
- [PMID:12087406 "The identified 'nodulation receptor kinase', NORK, is predicted to function in the Nod-factor perception/transduction system"]. Cloned from M. sativa, with M. truncatula alleles.
- Lotus/pea ortholog SYMRK: [PMID:12087405 "SYMRK ... required for both fungal and bacterial recognition"].

## Genetics: both symbioses
- [PMID:11006338 "dmi1 , dmi2 , and dmi3 mutants are also unable to establish a symbiotic association with endomycorrhizal fungi"]
- [PMID:11078514 "We defined two genes, DMI1 and DMI2, required in common for early steps of infection and nodulation and for calcium spiking."] So DMI2 acts upstream of calcium spiking, while DMI3 acts downstream of it.
- Nodules: [PMID:16006515 "encoding the receptor kinase DOES NOT MAKE INFECTIONS 2 (DMI2) is essential for symbiosome formation"]
- The two roles are separable. The G795E (dmi2-4/R38) allele is Nod- but Myc+ (UniProt MUTAGEN, from PMID:12087406), and that variant is kinase-dead: [PMID:28267253 "Here we demonstrate that the kinase activity is indeed abolished in the R38 mutant’s version of NORK"]. So kinase activity is needed for nodulation but apparently not for AM. This is important for keeping the nodulation and AM terms distinct.

## Biochemistry
- [PMID:28267253 "the wild-type versions of LYK3 and NORK exhibited auto-phosphorylation ... and trans-phosphorylation (as indicated by the phosphorylation of casein)"]; NORK phosphorylates kinase-dead LYK3 on Ser269/273/307/323/471. LYK3 did not phosphorylate NORK.
- PUB1 (E3 ligase) is an interactor and in vitro substrate: [PMID:26839127 "PUB1 also interacts with and is phosphorylated by DOES NOT MAKE INFECTIONS 2"]. According to the deep research summary, PUB1 did not ubiquitinate DMI2.
- HMGR1 interacts with the active kinase domain [PMID:18156218] but is not a demonstrated substrate.
- No ligand has been identified for the ectodomain.

## Localisation
- [PMID:16006515 "The protein locates to the host cell plasma membrane and to the membrane surrounding the infection threads."]
- Expressed in root epidermis/cortex and in nodule primordia; not expressed in root apices [PMID:16134899].

## Curation decisions
- All kinase MF annotations (IDA, EXP, and the IEAs) were accepted. Core MF is GO:0004674. GO:0004675 (transmembrane receptor Ser/Thr kinase) was not proposed because no ligand is known.
- protein binding (PUB1): changed (MODIFY) to GO:0031625 ubiquitin protein ligase binding.
- NEW annotations: GO:0009877 nodulation (IMP), GO:0036377 AM association (IMP), GO:0005886 plasma membrane (IDA).
  - Comparator check: LYK3 (Q6UD73) and CCaMK (Q6RET7) carry GO:0009877 by IMP; LYK3 carries plasma membrane by IDA. NORK lacking these terms is a gap, not a convention.
  - Participation check: NORK is an active signalling kinase in the pathway, not a substrate.
- No defense terms are present. No ligand-binding or receptor-activity terms were proposed.
