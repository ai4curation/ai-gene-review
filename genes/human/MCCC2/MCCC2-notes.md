# MCCC2 (Q9HCC0) review notes

## Identity
- Methylcrotonoyl-CoA carboxylase beta chain, mitochondrial (MCCB_HUMAN); gene MCCC2/MCCB.
- 563 aa precursor; N-terminal mitochondrial transit peptide (1..22), mature chain 23..563.
- HGNC:6937; MIM gene 609014; MIM phenotype 210210.

## Verified biology
- Beta = **carboxyltransferase (CT), non-biotin-containing subunit** of 3-methylcrotonyl-CoA carboxylase (MCC).
- Alpha (MCCC1, Q96RQ3) is the biotin-containing (BC + BCCP) subunit that carries carboxybiotin.
- Holoenzyme = **alpha6-beta6 dodecamer** (~750 kDa); UniProt SUBUNIT: "Probably a dodecamer composed of six biotin-containing alpha subunits (MCCC1) and six beta (MCCC2) subunits." Chu & Cheng (PMID:17360195) report ~500-800 kDa complex, 1:1 alpha:beta stoichiometry.
- Reaction (EC 6.4.1.4, RHEA:13589): 3-methylbut-2-enoyl-CoA (3-methylcrotonyl-CoA) + HCO3- + ATP -> 3-methyl-(2E)-glutaconyl-CoA + ADP + phosphate + H+.
- The beta/CT subunit binds the acyl-CoA (3-methylcrotonyl-CoA) substrate and transfers the carboxyl group from carboxybiotin (on MCCC1) [PMID:11170888 full text: "the β subunits contain the binding site for the acyl-CoA substrate"].
- Step 2 of L-leucine degradation (UniPathway UPA00363/UER00861); also relevant to isovaleric acid catabolism.
- Localization: **mitochondrial matrix**; imported via cleavable N-terminal presequence, cleavage Ala22/Tyr23 for MCCbeta (PMID:16023992).
- Kinetics (recombinant human MCC, PMID:17360195): kcat ~4.0 s-1; KM ATP 45 uM; KM 3-methylcrotonyl-CoA 74 uM.
- Family: AccD/PCCB (carboxyl transferase); domains CoA carboxyltransferase N-terminal (49..306) and C-terminal (309..555); acyl-CoA binding region 343..372.

## Disease
- Biallelic loss-of-function variants in MCCC2 (CGB / MCCA-complementation-independent) cause 3-methylcrotonyl-CoA carboxylase deficiency (3-MCCD / 3-methylcrotonylglycinuria; MONDO:0018950), an autosomal recessive inborn error of leucine catabolism. Highly variable, from asymptomatic (frequently detected on newborn screening) to severe neonatal decompensation.
- Biochemical hallmark: elevated C5OH (3-hydroxyisovalerylcarnitine), urinary 3-hydroxyisovaleric acid and 3-methylcrotonylglycine, often secondary carnitine deficiency (UniProt DISEASE; dismech KB 3-MCCD; PMID:11170888).
- >40 pathogenic MCCC2 missense/truncating variants catalogued in UniProt.

## Annotation review reasoning
- Core MF = GO:0004485 methylcrotonoyl-CoA carboxylase activity. Qualifier is correctly `contributes_to` (activity is a property of the holoenzyme; beta alone binds substrate but full carboxylation needs the biotinylated alpha). IDA (PMID:17360195), NAS (11170888, 11181649), IBA, IEA(EC) all converge -> ACCEPT the experimental/IBA ones; keep the NAS/IEA as accept (correct).
- Core BP = GO:0006552 L-leucine catabolic process (IMP PMID:9544913, IBA, IEA, TAS PMID:11170888). GO:0009083 BCAA catabolic process (NAS) is the parent — keep as non-core (correct but less specific). GO:0015936 coenzyme A metabolic process (IEA/Ensembl ortholog) is a very broad/tangential mapping (CoA is a cofactor scaffold, not what MCC metabolizes) -> over-annotated.
- Core CC = GO:0005759 mitochondrial matrix (multiple IDA + TAS + IEA) and GO:1905202 methylcrotonoyl-CoA carboxylase complex (IDA/IPI/IBA/NAS/TAS). GO:0005739 mitochondrion is the correct broader parent (accept, non-core relative to matrix).
- GO:0005829 cytosol (TAS Reactome) reflects the modeled cytosolic->matrix translocation step of the nascent/apo carboxylase in Reactome pathways, NOT a steady-state functional location. Mark as over-annotated (transient import intermediate, not a site of function).
- GO:0016874 ligase activity (IEA InterPro) is the correct broad parent of GO:0004485 (verified GO:0004485 is_a GO:0016874) -> accept as non-core (less informative than the specific EC).
- GO:0005515 protein binding (7x IPI): the only biologically meaningful partner is MCCC1 (Q96RQ3, the intra-complex alpha subunit; captured better by GO:1905202). CFTR (P13569) hits come from CFTR-interactome / proximity-labeling screens (PMID:35156780, 36012204) — likely non-specific for a matrix metabolic enzyme. Per policy: bare `protein binding` IPI -> MARK_AS_OVER_ANNOTATED (uninformative term), do not REMOVE.

## Deep research
- `just deep-research human MCCC2 --provider falcon` FAILED (exit 1, no output, no file produced). Did NOT fabricate a -deep-research-*.md. Grounded review in UniProt (Q9HCC0), seeded GOA, dismech disorder KB, and cached publications/PMID_*.md.
