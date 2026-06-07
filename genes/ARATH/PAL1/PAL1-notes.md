# PAL1 (Arabidopsis thaliana) — curation notes

UniProt: P35510 (PAL1_ARATH); locus At2g37040; 725 aa. EC 4.3.1.24.

## Core enzymatic identity
- Catalyzes the first, rate-limiting step of the phenylpropanoid pathway: non-oxidative deamination of L-phenylalanine to (E)-cinnamate (trans-cinnamic acid) + NH4+. [UniProt P35510 CATALYTIC ACTIVITY: "Reaction=L-phenylalanine = (E)-cinnamate + NH4(+); ... EC=4.3.1.24; Evidence={ECO:0000269|PubMed:15276452}"]
- Enzyme is a homotetramer with an autocatalytically formed 4-methylidene-imidazol-5-one (MIO) cofactor from an Ala-Ser-Gly motif. [UniProt P35510 PTM/CROSSLNK 211..213 "5-imidazolinone (Ala-Gly)"; SUBUNIT "Homotetramer"]
- Belongs to the PAL/histidase family (Pfam Lyase_aromatic, TIGR01226 phe_am_lyase). [UniProt SIMILARITY]
- Recombinant AtPAL1 is catalytically competent for L-Phe deamination; L-Phe is the true physiological substrate (low/undetectable activity on L-Tyr). KM ~64-68 uM for L-Phe. [PMID:15276452 "recombinant native AtPAL1, 2, and 4 were demonstrated to be catalytically competent for l-phenylalanine deamination"; "establishing that l-Phe is the true physiological substrate"]

## Biological role and redundancy
- Arabidopsis has four PAL genes (PAL1-PAL4). PAL1 and PAL2 act redundantly in flavonoid biosynthesis. [PMID:20566705 "Thus, PAL1 and PAL2 have a redundant role in flavonoid biosynthesis."]
- pal1 pal2 double mutants: yellow seeds (loss of condensed tannins), deficient anthocyanin, more UV-B sensitive, more drought tolerant. [PMID:20566705 "three independent pal1 pal2 double mutants were fertile and generated yellow seeds due to the lack of condensed tannin pigments in the seed coat ... deficient in anthocyanin pigments ... more sensitive to ultraviolet-B light but more tolerant to drought"]
- pal1 pal2 pal3 pal4 quadruple mutants: stunted, sterile, ~10% residual PAL activity, reduced salicylic acid, increased susceptibility to Pseudomonas syringae. [PMID:20566705 "quadruple knockout mutants, which are stunted and sterile ... still contained about 10% of the wild-type PAL activity ... accumulated substantially reduced levels of salicylic acid and displayed increased susceptibility to a virulent strain of the bacterial pathogen Pseudomonas syringae"]
- Note: most BP phenotypes (pollen development, drought recovery, UV-B response, salicylic acid, lignin) in PMID:20566705 derive from double/triple/quadruple mutant combinations or are family-level, indicating redundancy; PAL1 contributes within a small family. The TAIR IMP annotations to "lignin catabolic process" (GO:0046274) and "salicylic acid catabolic process" (GO:0046244) are mislabeled — PAL produces precursors for lignin BIOsynthesis and feeds salicylate biosynthesis, it does not catabolize lignin or SA. These look like curation/automated-mapping errors.

## Defense / immunity
- PAL1 is required for RPS2-mediated effector-triggered immunity (ETI); pal1 mutant shows reduced ETI-associated programmed cell death. [PMID:31568832 "we observed a significant reduction in ETI-associated PCD in pal1"; "phenylalanine ammonia lyase 1 (PAL1) for conversion of phenylalanine to phenylpropanoid compounds were among the RF up-regulated genes (EC 4.3.1.24)"]
- PAL1/PAL2 are oxidative-stress-responsive duplicated genes with divergent expression. [PMID:15634198 "Examination of the expression patterns of PAL1 and PAL2 ... suggests Arabidopsis evolved a number of distinct oxidative stress response mechanisms"]
- PAL gene family historically linked to defense response and wounding. [PMID:7888622 "Phenylpropanoid derivatives ... have many important roles in plants during normal growth and in responses to environmental stress."]

## Post-translational regulation (protein interactors)
- Kelch repeat F-box (KFB) proteins KFB01 (AT1G15670), KFB20 (AT1G80440), KFB50 (AT3G59940) physically interact with the four PAL isozymes and target them for ubiquitin-26S proteasome degradation. [PMID:24363316 "the Arabidopsis thaliana Kelch repeat F-box (KFB) proteins KFB01, KFB20, and KFB50 physically interact with four PAL isozymes and mediate their proteolytic turnover via the ubiquitination-26S proteasome pathway"]
- SAGL1 (SMALL AND GLOSSY LEAVES1, AT1G55270), another Kelch repeat F-box protein, interacts with PAL1 for proteasome-mediated degradation. [PMID:30542810 "SMALL AND GLOSSY LEAVES1 (SAGL1), a Kelch repeat F-box protein, interacts with PAL1 protein for proteasome-mediated degradation"]
- These IPI "protein binding" annotations capture PAL1 as the SUBSTRATE of E3-ligase-mediated turnover. They are real interactions but uninformative as a molecular function ("protein binding"); the biologically meaningful description is that PAL1 is regulated by KFB/F-box-mediated ubiquitin-proteasome turnover. Marked over-annotated rather than accepted as core MF.

## Localization
- Cytoplasm (no targeting signals; soluble cytosolic enzyme). [UniProt SUBCELLULAR LOCATION "Cytoplasm {ECO:0000305}"]

## Curation decisions summary
- Core MF: GO:0045548 phenylalanine ammonia-lyase activity (ACCEPT EXP/IDA; verified by EC 4.3.1.24 + Rhea:21384).
- Generic MF terms GO:0003824 (catalytic activity) and GO:0016841 (ammonia-lyase activity): MODIFY -> GO:0045548 (too general; specific activity known).
- Core BP: GO:0006559 (L-phenylalanine catabolic process), GO:0009698 (phenylpropanoid metabolic process), GO:0009800 (cinnamic acid biosynthetic process) — ACCEPT.
- Defense/stress BP (defense response, response to wounding, oxidative stress, UV-B): downstream consequences of phenylpropanoid output; KEEP_AS_NON_CORE.
- GO:0046274 lignin catabolic process & GO:0046244 salicylic acid catabolic process: REMOVE/MODIFY — direction wrong (PAL feeds biosynthesis, not catabolism); these are TAIR IMP family-level over/mis-annotations.
- protein binding (GO:0005515) x several IPI: MARK_AS_OVER_ANNOTATED (PAL1 as proteasome-turnover substrate of KFB/SAGL1 F-box proteins; not an informative MF, no adapter function).

## Deep research synthesis (Falcon / Edison Scientific)

Source: `file:ARATH/PAL1/PAL1-deep-research-falcon.md` (Edison Scientific Literature; 27 citations). The report corroborates the existing review and adds no contradictory evidence. Key corroborations folded into `supported_by`:

- Core reaction / MF: "PAL catalyzes the non-oxidative deamination of L-phenylalanine (Phe) to trans-cinnamic acid (t-cinnamate) and ammonia (NH3), representing the first committed step channelling carbon from primary metabolism into the phenylpropanoid pathway." Reinforces GO:0045548, GO:0006559, GO:0009800, GO:0009698 as core.
- Substrate specificity: "AtPAL1, AtPAL2, and AtPAL4 show robust phenylalanine deamination activity, whereas AtPAL3 has low activity" — independent support for PAL1 as a major catalytic isoform (consistent with PMID:15276452).
- Localization: corpus has no direct PAL1-protein localization experiment, but "PAL-dependent SA production is explicitly described as operating in a cytosolic PAL pathway" — pathway-level support for cytosolic action; consistent with UniProt cytoplasm. No basis to change the ACCEPT for GO:0005737.
- Catabolic mis-annotations confirmed wrong-direction: PAL1 "supplying precursors for lignin, flavonoids/anthocyanins, and contributing to salicylic acid (SA) biosynthesis" and participating in the "cytosolic 'PAL pathway' contributing to salicylic acid (SA) biosynthesis." This reinforces the REMOVE decisions for GO:0046274 (lignin catabolic) and GO:0046244 (SA catabolic) — PAL feeds biosynthesis, not catabolism.
- Post-translational regulation: "proteasome-dependent PAL degradation mediated by Kelch-domain F-box (KFB) proteins" — corroborates KFB/SAGL1 IPI annotations as PAL1-as-substrate (kept MARK_AS_OVER_ANNOTATED for bare protein binding).
- Transcriptional regulation (new context, not annotated): ERF114 directly binds the PAL1 promoter and activates expression during elicitor/pathogen defense ("ERF114 positively modulates elicitor-induced lignin and SA accumulation, likely via PAL1 activation"); WHY1 represses PAL1 indirectly via MYB15. These are regulators OF PAL1, not PAL1 functions, so they do not generate new PAL1 GO annotations.

No UNDECIDED annotations existed; none required resolution. No new GO term could be added with a GOA/UniProt-verifiable ID beyond those already present (regulatory/defense relationships are upstream-of-PAL1 and not appropriate as PAL1 MF/BP additions). `proposed_new_terms` therefore remains empty. status kept DRAFT.
