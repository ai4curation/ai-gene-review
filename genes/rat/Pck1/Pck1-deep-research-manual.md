# Pck1 (rat, P07379) - manual literature synthesis

No deep-research provider was run for this gene. This file collects the literature work
done by hand from the cached publications in `publications/` and the UniProt record
(`Pck1-uniprot.txt`). Each assertion carries its source.

## Identity

- Rat Pck1 encodes cytosolic phosphoenolpyruvate carboxykinase [GTP] (PEPCK-C), 622 aa,
  EC 4.1.1.32 [file:rat/Pck1/Pck1-uniprot.txt "Phosphoenolpyruvate carboxykinase, cytosolic [GTP]"].
- Vertebrates carry two PEPCK-GTP isozymes, cytosolic PCK1 and mitochondrial PCK2
  [file:rat/Pck1/Pck1-uniprot.txt "In eukaryotes there are two isozymes: a cytoplasmic one
  and a mitochondrial one."]. Ballard and Hanson purified the rat liver cytosolic enzyme and
  showed it is immunochemically distinct from the mitochondrial one [PMID:4186849, title].

## Catalytic activity and mechanism

- Reaction: oxaloacetate + GTP = phosphoenolpyruvate + GDP + CO2 (RHEA:10388), reversible,
  with Mn2+ as the active-site metal [file:rat/Pck1/Pck1-uniprot.txt "Binds 1 Mn(2+) ion per subunit."].
- Rat PEPCK-C is the main structural model of the GTP-dependent PEPCKs. Structures with
  Mn2+, OAA, GDP and GTP show direct in-line phosphoryl transfer [PMID:17685635 "The structures
  are consistent with a mechanism of direct in-line phosphoryl transfer, supported by the
  observed stereochemistry of the reaction."].
- Holyoak lab kinetics on recombinant rat enzyme: active-site loop mutants (E89, H477R)
  [PMID:26709450; PMID:28345895 "This is exemplified by a reduction in kcat for the H477R
  mutant by an order of magnitude in the direction of OAA synthesis"]; inhibitors
  3-mercaptopicolinate at the substrate site and an allosteric site [PMID:26322521 "PEPCK is
  inhibited by the binding of MPA at two discrete binding sites"] and CMP [PMID:31461616
  "CMP acts as a competitive inhibitor at the OAA/PEP binding site"].
- Monomer [file:rat/Pck1/Pck1-uniprot.txt "SUBUNIT: Monomer."].

## Physiological roles

- Gluconeogenesis. PEPCK-C catalyses the committed step of gluconeogenesis from lactate,
  amino acids and TCA-cycle intermediates in liver and kidney. In rat liver, more than 90%
  of PEPCK activity is cytosolic and the cytosolic enzyme appears at birth with the onset
  of gluconeogenesis [PMID:6049928 "Similar studies of the intracellular distribution of
  phosphoenolpyruvate carboxykinase show that more than 90% of the activity is in the
  cytoplasm."]. siRNA knockdown in H4IIEC3 rat hepatoma cells lowers glucose production
  [PMID:18055057 "the knockdown of PEPCK, which is the rate-limiting enzyme for
  gluconeogenesis, led to a reduction in glucose production in rat hepatoma H4IIEC3
  cells."]. Renal cortex gluconeogenesis develops with PEPCK [PMID:4303362].
- Cataplerosis/anaplerosis. Mouse liver-specific knockout shows PEPCK-C removes TCA-cycle
  carbon [PMID:15347677 "Disruption of hepatic cataplerosis due to loss of PEPCK leads to
  the accumulation of TCA cycle intermediates"]. Acetylation of rat PCK1 (Lys91 and others)
  switches the enzyme toward PEP carboxylation under high glucose; SIRT1 deacetylation
  restores the gluconeogenic direction [PMID:30193097 "dynamic acetylation of PCK1
  interconverts the enzyme between gluconeogenic and anaplerotic activities"].
- Glyceroneogenesis. In adipose tissue PEPCK-C supplies PEP for glycerol-3-phosphate
  synthesis used to re-esterify fatty acids (mouse PPARE knock-in, PMID:11792850). Rat
  adipose Pck1 is induced together with other glyceroneogenic genes by methionine
  restriction [PMID:23052097]. The Holyoak lab describes PEPCK as operating in both
  gluconeogenesis and glyceroneogenesis [PMID:26709450 "Phosphoenolpyruvate carboxykinase
  (PEPCK) is an essential metabolic enzyme operating in the gluconeogenesis and
  glyceroneogenesis pathways."].
- Isozyme contrast in islets. Pancreatic beta cells (INS-1 832/13, rat and mouse islets)
  lack PEPCK-C; their PEPCK activity is entirely mitochondrial PEPCK-M (Pck2)
  [PMID:19635791 "PEPCK-M but not PEPCK-C is present in INS-1 832/13 cells, rat islets, and
  mouse islets."]. This supports keeping the mitochondrial location on Pck2 only.

## Regulation (expression)

- Transcription is induced by glucagon/cAMP and glucocorticoids and repressed by insulin
  [file:rat/Pck1/Pck1-uniprot.txt "Regulated by cAMP, dexamethasone, glucagon and by
  insulin."; PMID:18335579; PMID:21519922]. Many rat IEP annotations come from expression
  studies: osmotic stress in H4IIE cells [PMID:9530152], cytokines [PMID:18335579,
  PMID:17805558], LPS [PMID:19268478], hypoxia/HNF4A [PMID:24177414], retinoids
  [PMID:21519922], fructose [PMID:21212096], exercise [PMID:16458327], diet/programming
  [PMID:21486814, PMID:23307605, PMID:25943649, PMID:23052097].

## Non-canonical activities (not shown in rat)

- Protein serine kinase (GTP donor): in human HCC cells AKT-phosphorylated PCK1 (Ser90)
  moves to the ER and phosphorylates INSIG1/2, activating SREBPs [PMID:32322062 "Phosphorylated
  PCK1 translocates to the endoplasmic reticulum, where it uses GTP as a phosphate donor to
  phosphorylate INSIG1 at Ser207 and INSIG2 at Ser151."]. Rat annotations to this activity,
  ER location and lipid-biosynthesis regulation are all transfers of that one human study.
- Memory CD8+ T cells: mouse Pck1 is upregulated and channels gluconeogenic carbon to
  glycogen and the pentose phosphate pathway [PMID:29230018]. No rat data.
- Carbovir diphosphate phosphorylation: Reactome records rat PCK1 converting carbovir
  diphosphate to the triphosphate in vitro (PMID:1383219, R-RNO-2162084); the cached abstract
  does not mention PEPCK, and the full text was not available.
