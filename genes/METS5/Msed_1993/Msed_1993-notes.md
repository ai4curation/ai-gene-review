# Msed_1993 (A4YI81) — curation notes

Metallosphaera sedula DSM 5348. ARCHAEA project gene; grounds the malonic semialdehyde
reductase step of `modules/hydroxypropionate_hydroxybutyrate_cycle.yaml`.

**Provenance note:** automated deep research was unavailable in this session; no
`-deep-research-*.md` file was created. Literature was searched manually (Europe PMC REST
search for "Msed_1993" and "malonic semialdehyde reductase Metallosphaera"; NCBI E-utilities
was returning backend errors) and read from the cached publications. PMIDs 25548047
(Nitrosopumilus malonic semialdehyde reductase) and 20008169 (M. sedula transcriptomics)
were found but could not be cached (`just fetch-pmid` failed), so they are not cited.

## Identity and activity

- UniProt TrEMBL entry, unreviewed; SubName "3-hydroxypropionate dehydrogenase (NADP(+))";
  BRENDA 1.1.1.298; family "3-hydroxyacyl-CoA dehydrogenase family" (ARBA); Pfam PF02737
  3HCDH_N + PF00725 3HCDH; PANTHER PTHR48075:SF1 "lambda-crystallin homolog".
- Native enzyme partially purified from autotrophic cells and identified by peptide mass
  fingerprinting: [PMID:19684143 "The best hit was with the gene gi|146304741 (100% identity, 54% coverage), annotated as 3-hydroxyacyl-CoA dehydrogenase (NAD binding) gene, encoding a 35.3-kDa protein (Msed_1993; 314 amino acids)."]
- Recombinant enzyme: [PMID:19684143 "The malonic semialdehyde reductase gene encoding the Msed_1993 protein was cloned into the expression vector pT7-7 ( 43 ) and expressed in E. coli Rosetta 2(DE3)."]
  Specific activity 200 U/mg at 65 C; homotrimer:
  [PMID:19684143 "The native molecular mass determined by gel filtration was 105 ± 10 kDa, suggesting a homotrimeric subunit composition."]
- Kinetics: [PMID:19684143 "The apparent K m for malonic semialdehyde was 70 ± 10 μM, and the apparent K m for NADPH was 70 ± 20 μM."]
- Cofactor: NADPH preferred, NADH partial: [PMID:19684143 "NADH (20% activity) could partially substitute for NADPH (100%)."]
- Substrate specificity: [PMID:19684143 "Succinic semialdehyde, acetaldehyde, butyraldehyde, propionaldehyde, or glutaraldehyde did not serve as a substrate"]
- No metal requirement; not classifiable from sequence:
  [PMID:19684143 "This enzyme cannot be classified unambiguously, and no divalent metal ion was required."]
- Summary sentence: [PMID:19684143 "Malonic semialdehyde reductase, a member of the 3-hydroxyacyl-CoA dehydrogenase family, reduces malonic semialdehyde with NADPH to 3-hydroxypropionate."]

## Physiological role

- Activity in extracts is about five-fold higher in autotrophic cells:
  [PMID:19684143 "The specific activity of this conversion in autotrophically grown cells was 1.8 μmol min −1 mg −1 protein, whereas in heterotrophically grown cells the specific activity was 0.35 μmol min −1 mg −1 protein."]
- NADPH preference argues for the reductive (anabolic) direction:
  [PMID:19684143 "Also, the NADPH specificity suggests that they function as reductases in an anabolic pathway rather than as dehydrogenases in a catabolic pathway."]
- Gene neighbourhood: [PMID:19684143 "the malonic semialdehyde reductase gene is located eight genes downstream of the 3-hydroxypropionyl-CoA dehydratase gene (Msed_2001)"]
- In vivo function in a heterologous host: Msed_1993 was the "E3" enzyme in the
  three-enzyme module (with ACC/PCC and MCR) that let engineered Pyrococcus furiosus make
  3-hydroxypropionate from CO2. [PMID:23530213 "E3 (malonate semialdehyde reductase, Msed_1993)"]
  [PMID:23530213 "E2 breaks the CoA–thioester bond and, with E3, reduces the carboxylate to an alcohol with NADPH as the electron donor."]
- Not in the 2016 kinetic reconstruction (PMID:27771364), which started from 3-hydroxypropionate.

## GO term choices

- GO:0035527 3-hydroxypropionate dehydrogenase (NADP+) activity — OLS definition:
  "3-hydroxypropanoate + NADP+ = 3-oxopropanoate + H+ + NADPH". 3-Oxopropanoate is malonate
  semialdehyde, so this is exactly the reaction (written in the oxidative direction, as GO
  does for reversible dehydrogenases). Ancestors: GO:0016616 -> GO:0016614 -> GO:0016491.
  So the module's MF term fits. The NAD+ sibling GO:0047565 describes the minor (20%) NADH
  activity and is not needed.
- GO:0050104 L-gulonate 3-dehydrogenase activity (TreeGrafter, PTN000592773): this is the
  lambda-crystallin/CRYL1 activity of the PANTHER subfamily name. No one has tested
  L-gulonate with Msed_1993; the protein's substrate is a C3 oxo acid, not a hexonate, and
  there is no glucuronate/uronate pathway context in this archaeon. Over-propagation from the
  family -> REMOVE.
- GO:0006631 fatty acid metabolic process (InterPro2GO from the 3HCDH signatures): the family
  mapping assumes 3-hydroxyacyl-CoA dehydrogenase in beta-oxidation. Msed_1993 acts on a free
  aldehyde, not an acyl-CoA, in CO2 fixation. Marked as over-annotation (same treatment as
  fatty acid beta-oxidation on the sibling Msed_2001).
- GO:0070403 NAD+ binding (IPR006176): the Rossmann domain binds the nicotinamide cofactor,
  but the physiological cofactor is NADPH; MODIFY to GO:0050661 NADP binding.
- GO:0016491 / GO:0016616: correct but general -> MODIFY to GO:0035527.
- NEW GO:0015977 carbon fixation (IDA, PMID:19684143), following the sibling reviews; GO:0043427
  (Chloroflexus cycle) not used. The proposed "carbon fixation by
  3-hydroxypropionate/4-hydroxybutyrate cycle" term is reused verbatim from Msed_0709.

## Open questions

- Does Msed_1993 have any L-gulonate 3-dehydrogenase or 3-hydroxyacyl-CoA dehydrogenase
  activity (never tested)?
- Structural basis for the switch from acyl-CoA to free semialdehyde substrate in this
  3HCDH-family member.
