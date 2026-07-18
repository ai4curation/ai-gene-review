# NDUFAF1 (CIA30 / Q9Y375) — review notes

## Identity and family
- NDUFAF1 = CIA30 = "Complex I intermediate-associated protein 30, mitochondrial"; alt name "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 1" [file:human/NDUFAF1/NDUFAF1-uniprot.txt "RecName: Full=Complex I intermediate-associated protein 30, mitochondrial"].
- Belongs to the CIA30 family; has a cleavable N-terminal mitochondrial transit peptide (residues 1–24) and a galactose-binding domain-like fold (Pfam PF08547 CIA30) [file:human/NDUFAF1/NDUFAF1-uniprot.txt "Belongs to the CIA30 family"], [file:human/NDUFAF1/NDUFAF1-uniprot.txt "TRANSIT         1..24"].
- Human homologue of the Neurospora crassa complex I chaperone CIA30 [PMID:16218961 "A \ngood candidate is NDUFAF1, the human homologue of Neurospora crassa complex I \nchaperone CIA30"].

## Function (assembly factor, NOT a catalytic/structural subunit)
- Function per UniProt: "As part of the MCIA complex, involved in the assembly of the mitochondrial complex I" [file:human/NDUFAF1/NDUFAF1-uniprot.txt "As part of the MCIA complex, involved in the assembly of the"].
- Required for CI assembly: RNAi knockdown reduces amount and activity of complex I [PMID:16218961 "knocking down its expression using RNA \ninterference leads to a reduced amount and activity of complex I"]; NDUFAF1 associates with 600/700 kDa assembly intermediates [PMID:16218961 "NDUFAF1 \nis associated to two complexes of 600 and 700 kDa in size"].
- Acts early: CIA30 "associates with newly translated mtDNA-encoded complex I subunits at early stages in their assembly before dissociating at a later stage" [PMID:17557076 "associates with newly translated mtDNA-encoded complex I subunits at"], and is "a crucial component in the early assembly of complex I" [PMID:17557076 "CIA30 is a crucial"].
- Assembly factors dissociate from the mature holoenzyme (Reactome: "The MCIA complex ... dissociate from the 980kDa complex, resulting in Complex I"). => NDUFAF1 has NO role in electron transport itself; GO:0006120 (NADH->ubiquinone electron transport) is an over-annotation.

## MCIA complex membership (GO:0160295)
- MCIA core subunits: NDUFAF1, ECSIT, ACAD9, TMEM126B; plus TMEM186 and COA1 [PMID:32320651 "assembly (MCIA) complex, containing assembly factors NDUFAF1, \nECSIT, ACAD9, and TMEM126B"], [file:human/NDUFAF1/NDUFAF1-uniprot.txt "comprises at least the core subunits TMEM126B, NDUFAF1, ECSIT and ACAD9"].
- Architecture: ECSIT bridges the complex — NDUFAF1 binds ECSIT's N-terminal domain, ACAD9 binds ECSIT's C-terminal domain; NDUFAF1 does NOT bind ACAD9 directly [PMID:33320993 "No direct interaction between NDUFAF1 and ACAD9 was observed"], [PMID:34646991 "ACAD9 binds \nto the carboxy-terminal half and NDUFAF1 to the amino-terminal half of ECSIT"].
- Purified mature NDUFAF1 (25–327) is a monodisperse monomer [PMID:33320993 "Purified mature NDUFAF1 (residues 25–327) behaved as a monodisperse monomer"].
- ACAD9/ECSIT/NDUFAF1 ternary complex is soluble and stable [PMID:34646991 "ACAD9, ECSIT, and NDUFAF1 interact to form the core mitochondrial CI assembly complex"].

## Interactions
- ECSIT [PMID:17344420 "it interacts with chaperone NDUFAF1"]; ACAD9 [PMID:20816094 "ACAD9 \nbinds complex I assembly factors NDUFAF1 and Ecsit"]; TMEM70/TMEM242 (via MCIA) [PMID:33753518 "TMEM70 and TMEM242 interact with the \nmitochondrial complex I assembly (the MCIA) complex"].
- HuRI (PMID:32296183) binary-interactome hits (PNLIPRP1, SLC30A2, STX8, TMEM86B, TMEM97, YIPF6) are non-mitochondrial and not CI-assembly relevant => generic "protein binding" over-annotation.

## Localization
- Mitochondrion; mitochondrion matrix; peripherally associated with the matrix face of the inner membrane [file:human/NDUFAF1/NDUFAF1-uniprot.txt "Peripherally associated with the matrix face of the mitochondrial inner membrane"].

## Disease
- Biallelic NDUFAF1 mutations cause mitochondrial complex I deficiency nuclear type 11 (MC1DN11), a cardioencephalomyopathy / fatal infantile hypertrophic cardiomyopathy [file:human/NDUFAF1/NDUFAF1-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 11 (MC1DN11)"], [PMID:17557076 "mutations in its gene can cause \nmitochondrial disease"].

## Review decisions summary
- Core BP: GO:0032981 mitochondrial respiratory chain complex I assembly (ACCEPT, well supported IDA/IMP/IBA/NAS).
- Core CC: GO:0160295 mitochondrial complex I intermediate assembly complex (ACCEPT, multiple IDA).
- Core MF: GO:0051082 unfolded protein binding — added as NEW (present in UniProt DR as IBA:GO_Central, absent from GOA TSV). Honest MF for a non-catalytic assembly chaperone. Did NOT assign any NADH dehydrogenase / oxidoreductase catalytic MF.
- GO:0006120 (electron transport NADH->ubiquinone, NAS) => MARK_AS_OVER_ANNOTATED (assembly factor, not a CI subunit).
- GO:0065003 (protein-containing complex assembly, NAS) => MODIFY to GO:0032981 (too general).
- All "protein binding" GO:0005515 IPI => MARK_AS_OVER_ANNOTATED (uninformative; MCIA membership captured by GO:0160295); per policy, experimental IPI is never REMOVED.
- Mitochondrion GO:0005739 (general) localizations => KEEP_AS_NON_CORE; matrix (GO:0005759) => ACCEPT; inner membrane (GO:0005743) => KEEP_AS_NON_CORE (peripheral).
