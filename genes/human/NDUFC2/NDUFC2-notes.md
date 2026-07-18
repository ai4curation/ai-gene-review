# NDUFC2 (B14.5b) review notes

## Identity and family
- UniProt O95298, HGNC:7706, gene NDUFC2. RecName "NADH dehydrogenase [ubiquinone] 1 subunit C2"; AltNames "Complex I-B14.5b / CI-B14.5b", "NADH-ubiquinone oxidoreductase subunit B14.5b", and "Human lung cancer oncogene 1 protein / HLC-1" [file:human/NDUFC2/NDUFC2-uniprot.txt].
- 119 aa, single-pass membrane protein with one predicted TM helix at residues 56-75; "Belongs to the complex I NDUFC2 subunit family" [file:human/NDUFC2/NDUFC2-uniprot.txt].
- Multiple splice isoforms (O95298-1 "3" displayed, O95298-2 "4", O95298-3 "5"), plus a read-through fusion transcript NDUFC2-KCTD14 (E9PQ53-1, isoform "2") [file:human/NDUFC2/NDUFC2-uniprot.txt].

## Core function (accessory/supernumerary structural subunit)
- UniProt FUNCTION: "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis but required for the complex assembly." [file:human/NDUFC2/NDUFC2-uniprot.txt]. Same sentence adds Complex I "functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone." Evidence ECO:0000269|PubMed:27626371, ECO:0000269|PubMed:32969598.
- SUBUNIT: "Complex I is composed of 45 different subunits. Interacts with TMEM242 (PubMed:33753518)." [file:human/NDUFC2/NDUFC2-uniprot.txt].
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane ... Single-pass membrane protein ... Matrix side" [file:human/NDUFC2/NDUFC2-uniprot.txt].
- => Honest MF is GO:0005198 structural molecule activity (contributes to structural integrity of Complex I); NDUFC2 is non-catalytic. It contributes_to the complex-level GO:0008137 NADH dehydrogenase (ubiquinone) activity, but does NOT directly enable it. part_of GO:0045271 respiratory chain complex I. Core BP: GO:0006120 (electron transport, NADH to ubiquinone) and GO:0032981 (complex I assembly).

## Complex I membership evidence
- Murray et al. 2003 (PMID:12611891): immunocapture + MS identified human homologues of 42 complex I polypeptides; "The subunit composition of the human NADH dehydrogenase obtained by rapid one-step immunopurification." NDUFC2/B14.5b is among the identified subunits (UniProt cites this for complex membership and subcellular location) [PMID:12611891 abstract; file:human/NDUFC2/NDUFC2-uniprot.txt RN[10]].
- Stroud et al. 2016 (PMID:27626371): "Accessory subunits are integral for assembly and function of human mitochondrial complex I." Gene-editing knockout of each accessory subunit; "25 subunits are strictly required for assembly of a functional complex"; "loss of each subunit affects the stability of other subunits residing in the same structural module." [PMID:27626371 abstract]. UniProt cites this for FUNCTION and complex membership.
- Guo et al. 2017 (PMID:28844695): cryo-EM of human megacomplex I2III2IV2; "reveals the precise assignment of individual subunits of human CI and CIII." NDUFC2 placed within the CI membrane arm (UniProt DR PDB 5XTC/5XTD/5XTH chain g = NDUFC2) [PMID:28844695 abstract; file:human/NDUFC2/NDUFC2-uniprot.txt].
- Loeffen et al. 1998 (PMID:9878551): cDNA characterization of 8 nuclear-encoded complex I subunits (including this one); complex I "main function is the transport of electrons from NADH to ubiquinone, which is accompanied by translocation of protons from the mitochondrial matrix to the intermembrane space." [PMID:9878551 abstract]. This is a cloning paper; its NAS annotations for the catalytic MF (GO:0008137) and electron-transport BP are complex-level, not NDUFC2-specific.

## Disease / functional requirement
- Alahmad et al. 2020 (PMID:32969598, full text): bi-allelic NDUFC2 variants cause early-onset Leigh syndrome (MC1DN36). "Biochemical and functional investigation of subjects' fibroblasts confirmed a severe defect in complex I activity, subunit expression and assembly." Rescue: "Lentiviral transduction of subjects' fibroblasts with wild-type NDUFC2 cDNA increased complex I assembly." "Complexome profiling confirmed a loss of NDUFC2 and defective complex I assembly, revealing aberrant assembly intermediates suggestive of stalled biogenesis of the complex I holoenzyme and indicating a crucial role for NDUFC2 in the assembly of the membrane arm of complex I, particularly the ND2 module." [PMID:32969598 abstract]. This is the primary IMP evidence for GO:0032981 (complex I assembly) and for the p.His58Leu MC1DN36 variant.

## TMEM242 interaction
- Carroll et al. 2021 (PMID:33753518, full text): TMEM242 co-purifies with membrane subunits of complex I: "TMEM242-t was also bound to TMEM70 and, to a lesser extent, to subunit c and to the NDUFC2, ND2, and ND3 membrane subunits of complex I". TMEM70-t associated with "NDUFB10, NDUFB11, NDUFC2, and ND2". [PMID:33753518 full text]. Supports the GO:0005515 IPI (NDUFC2 <-> TMEM242, UniProtKB:Q9NWH2).

## Other IPI / localization
- Formosa et al. 2020 (PMID:32320651): MCIA complex study; IPI links NDUFC2 to COA1 (UniProtKB:Q9GZY4) in GOA. Abstract-only; the membrane-arm ND2 module context is consistent (COA1 enriches with ND2). Bare protein-binding IPI.
- PMID:34800366 (Morgenstern et al., mitochondrial proteome): HTP mitochondrion localization (FlyBase-assigned); consistent with established mitochondrial protein. NDUFC2/O95298 not a plain-text string in cached full text (in supplementary tables).

## Over-annotation flags (Ensembl orthology GO_REF:0000107, IEA)
Rat-ortholog-transferred regulatory/process terms that are downstream/pleiotropic consequences of complex I activity, not NDUFC2's direct molecular role:
- GO:0010918 positive regulation of mitochondrial membrane potential
- GO:1901223 negative regulation of non-canonical NF-kappaB signal transduction
- GO:1903427 negative regulation of reactive oxygen species biosynthetic process
- GO:2001171 positive regulation of ATP biosynthetic process
These are indirect physiological consequences of a functional respiratory chain; over-annotations for an accessory structural subunit.

## Reactome neutrophil-degranulation mislocalizations
- Reactome:R-HSA-6798739 places NDUFC2 in "plasma membrane" (GO:0005886) and "azurophil granule membrane" (GO:0035577) via neutrophil degranulation pathway. Azurophil granules are MPO-rich secretory granules [reactome/R-HSA-6798739.md]. A bona fide mitochondrial inner-membrane complex I subunit is not a genuine neutrophil-granule/plasma-membrane resident; these are pathway-bulk over-inclusions -> MARK_AS_OVER_ANNOTATED.

## Cytoplasm IDA (LIFEdb, GO_REF:0000054)
- GO:0005737 cytoplasm from a fluorescent fusion-protein localization screen (LIFEdb). For a mitochondrial inner-membrane protein, "cytoplasm" is non-specific / likely reflects mistargeted overexpressed fusion; less informative than the mitochondrial annotations -> MARK_AS_OVER_ANNOTATED.

## Direct catalytic MF (NAS, PMID:9878551)
- GOA has GO:0008137 NADH dehydrogenase (ubiquinone) activity as `enables` (NAS). NDUFC2 is non-catalytic; the catalytic activity is a property of the holoenzyme, contributed to (not enabled) by this structural subunit. MODIFY the framing: use contributes_to_molecular_function for GO:0008137 in core_functions; the direct `enables` NAS annotation is over-annotated.
