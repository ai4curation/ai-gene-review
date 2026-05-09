# CLV1 review notes

Manual review completed for Arabidopsis thaliana CLV1 (Q9SYQ8), using the
seeded GOA, UniProt record, Falcon deep research, cached publications, and the
PANTHER PTHR48056 plant LRR-RLK family context.

Core synthesis: CLV1 is a plasma membrane LRR receptor-like Ser/Thr kinase that
binds CLV3-family CLE peptides and signals through CLV1/BAM/CIK and downstream
RLCK modules to restrict meristem stem cell proliferation. The original cloning
paper supports the mutant phenotype and receptor-kinase identity
[PMID:9160749 "Arabidopsis plants homozygous for mutations at the CLAVATA1
(CLV1) locus accumulate excess undifferentiated cells"; "It encodes a putative
receptor kinase, suggesting a role in signal transduction"]. CLV3-dependent
signaling complex assembly is supported by the 450-kD complex paper
[PMID:10072399 "CLV3 functions to promote the assembly of the active 450-kD
complex, which then relays signal transduction through a Rho GTPase"].

Kinase activity is supported by KAPP studies and newer RLCK work. KAPP binds
autophosphorylated CLV1 and co-immunoprecipitates with CLV1 from meristematic
tissue [PMID:9701578 "KAPP binds directly to autophosphorylated CLV1 in vitro
and co-immunoprecipitates with CLV1 in plant extracts derived from meristematic
tissue"]. CLV1 phosphorylates itself and KAPP [PMID:9294234 "CLV1 has kinase
activity: it phosphorylates both itself and KAPP"]. PBL34/35/36 interact with
CLV1/BAM/CIK proteins and are phosphorylated by CLV1/BAM1 [PMID:34935965
"PBL34/35/36 interacted with CLV1, BAM1/3, and CIKs, and were phosphorylated by
CLV1 and BAM1"].

Binding curation: all generic GO:0005515 protein binding rows were treated as
non-core and, where evidence was clear, modified to a more informative term:
protein phosphatase binding for KAPP, peptide hormone binding for CLV3/CLE
ligands, receptor Ser/Thr kinase binding for CLV1/BAM/CIK/CRN receptor-module
interactions, kinase binding for MAZ/Pti1-like and PBL RLCK partners, and
14-3-3 protein binding for the TAP-MS 14-3-3 interaction. The PMID:29320478
IntAct row was left UNDECIDED because the cached article text describes the
large LRR-RK network but not the CLV1-specific partners.

Localization curation: plasma membrane is accepted as the active signaling
location [PMID:21051944 "CLV1 primarily co-localizes with a plasma membrane
marker"]. Plant-type vacuole is kept as non-core because CLV3 causes ligand-
dependent trafficking of CLV1 to lytic vacuoles [PMID:21333538 "plasma
membrane-localized CLV1 is reduced in concentration by CLV3, which causes
trafficking of CLV1 to lytic vacuoles"]. Plasmodesma is kept as non-core for
root meristem context [PMID:23394827 "Both CLV1 and ACR4 overlap in their
expression domains in the distal root meristem and localize to the plasma
membrane (PM) and plasmodesmata (PDs)"].
