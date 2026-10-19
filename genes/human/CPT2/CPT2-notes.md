# CPT2 (Carnitine O-palmitoyltransferase 2, mitochondrial) — review notes

UniProt: P23786 (CPT2_HUMAN), 658 aa, HGNC:2330, chromosome 1p32.
EC 2.3.1.21. Belongs to the carnitine/choline acetyltransferase family.

## Core biology (verified)

CPT2 is the matrix-facing enzyme of the mitochondrial **inner membrane** that
completes the carnitine shuttle. After CPT1 (outer membrane) converts long-chain
acyl-CoA + carnitine to acylcarnitine, and the carnitine/acylcarnitine
translocase (SLC25A20) moves acylcarnitine across the inner membrane, **CPT2
regenerates long-chain acyl-CoA in the matrix**: long-chain acylcarnitine + CoA →
long-chain acyl-CoA + L-carnitine. This is the final step of the shuttle and is
required so that beta-oxidation can proceed in the matrix.

- UniProt FUNCTION: "Involved in the intramitochondrial synthesis of
  acylcarnitines from accumulated acyl-CoA metabolites ... Reconverts
  acylcarnitines back into the respective acyl-CoA esters that can then undergo
  beta-oxidation, an essential step for the mitochondrial uptake of long-chain
  fatty acids and their subsequent beta-oxidation in the mitochondrion. Active
  with medium (C8-C12) and long-chain (C14-C18) acyl-CoA esters."
  [ECO:0000269|PubMed:20538056, PubMed:24780397]
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane
  protein; Matrix side." Topology features: matrix 26-178, intramembrane 179-208
  ("Mitochondrial inner membrane"), matrix 209-658. So the bulk (incl. catalytic
  domain) is matrix-facing but the protein is anchored/peripheral at the inner
  membrane. This makes both `mitochondrial inner membrane` (located_in) and
  `mitochondrial matrix` (is_active_in) reasonable.
- Catalytic activity: RHEA:12661 (hexadecanoyl-CoA + carnitine ⇌ palmitoylcarnitine
  + CoA), EC 2.3.1.21. Physiological direction annotated right-to-left (regenerating
  acyl-CoA). Multiple additional Rhea reactions for C8-C20 acyl-CoAs.

## Substrate specificity (PMID:20538056, Violante et al. 2010)

Human CPT2 expressed in S. cerevisiae; substrate profiling by ESI-MS/MS.
- "CPT2 is active with medium (C8-C12) and long-chain (C14-C18) acyl-CoA esters,
  whereas virtually no activity was found with short- and very long-chain
  acyl-CoAs or with branched-chain amino acid oxidation intermediates."
- Supports MF: carnitine O-palmitoyltransferase activity (GO:0004095, C16),
  carnitine O-octanoyltransferase activity (GO:0008458, C8), and the parent
  carnitine O-acyltransferase activity (GO:0016406).
- "trans-2-C16:1-CoA may act as a competitive inhibitor of CPT2 (K(i) of 18.8
  microM)" → ACTIVITY REGULATION.
- Km 7.1 uM for hexadecanoyl-CoA.
- This is the IDA/EXP basis for GO:0004095, GO:0008458, GO:0016406, GO:0016746
  (acyltransferase), GO:0001676 (long-chain fatty acid metabolic process),
  GO:0006635 (fatty acid beta-oxidation), GO:0009437 (carnitine metabolic process).
  All from the same paper (Reactome/UniProt attributions).

## Disease (context, not a GO BP by itself)

CPT2 deficiency (MONDO:0015515): autosomal recessive inborn error of mitochondrial
long-chain FAO. Three forms: lethal neonatal (CPT2DLN), severe infantile
hepatocardiomuscular (CPT2DI), and the common adult myopathic form (CPT2D,
MIM:255110) — the most common inherited disorder of muscle FA metabolism,
presenting as exercise/fever/fasting-triggered myalgia, rhabdomyolysis,
myoglobinuria. Thermolabile variants (F352C, V368I) predispose to
influenza-associated encephalopathy (IIAE4). Confirms core role in long-chain FAO
/ carnitine shuttle. (UniProt DISEASE; dismech KB
Carnitine_Palmitoyltransferase_II_Deficiency.yaml; PMID:24780397, PMID:7711730.)

## Thermogenesis (GO:0120162)

PMID:25578732 (Lee et al.): adipose-specific Cpt2 knockout MOUSE (Cpt2^A-/-).
"CPT2(A-/-) mice became hypothermic after an acute cold challenge, and CPT2(A-/-)
brown adipose tissue (BAT) failed to upregulate thermogenic genes..." Shows adipose
FAO (via CPT2) is required for cold-induced thermogenesis. The human
GO:0120162 "positive regulation of cold-induced thermogenesis" is an ISS/IEA
transfer from mouse ortholog P52825. This is a genuine but tissue-specific
(BAT), context-dependent physiological role — KEEP_AS_NON_CORE. The core function
is the enzymatic step of the carnitine shuttle; thermogenesis is a downstream
organismal consequence in a specific tissue.

## Protein-binding IPIs (bare protein binding)

- PMID:28514442 (BioPlex/Huttlin interactome), PMID:32296183 (HuRI binary
  interactome; partners CYSRT1/A8MQ03, OTX1/P32242), PMID:33961781 (BioPlex
  cell-specific). MCUR1 (Q96AQ8) interaction also listed. These are high-throughput
  interactome screens; CPT2 appears only in supplementary partner tables, not main
  text. Bare `protein binding` (GO:0005515) is uninformative and none define a
  specific molecular function. Per policy: MARK_AS_OVER_ANNOTATED (not REMOVE for
  experimental IPI). UniProt INTERACTION section lists CYSRT1, MCUR1, OTX1.

## Annotation plan summary

Core functions:
- MF GO:0004095 carnitine O-palmitoyltransferase activity (well supported IDA/EXP).
- BP GO:0006853 carnitine shuttle (directly_involved_in) — the process CPT2 completes.
- BP GO:0006635 fatty acid beta-oxidation (directly_involved_in) — enabled by CPT2's step.
- CC GO:0005743 mitochondrial inner membrane (location; matrix side).

Actions:
- ACCEPT: MF carnitine O-palmitoyltransferase (IBA, IEA, EXP, IDA, NAS);
  carnitine O-octanoyltransferase (IEA, EXP); carnitine O-acyltransferase (EXP x2);
  fatty acid beta-oxidation (IBA, IEA, IDA); carnitine shuttle (IEA, TAS);
  carnitine metabolic process (IDA); long-chain fatty acid metabolic process (IDA);
  mitochondrion (IBA, IDA, HTP); mitochondrial inner membrane (IEA, TAS x2, NAS);
  mitochondrial matrix (IEA).
- MODIFY: GO:0016746 acyltransferase activity (IEA, IDA) — too general; replace with
  GO:0004095. GO:0015909 long-chain fatty acid transport (ARBA IEA) — CPT2 does not
  transport FAs across membrane (that's the translocase SLC25A20); its role is
  enzymatic regeneration of acyl-CoA enabling import. Replace with carnitine shuttle
  / fatty acid beta-oxidation.
- KEEP_AS_NON_CORE: GO:0120162 positive regulation of cold-induced thermogenesis
  (ISS, IEA) — real but tissue-specific downstream role.
- MARK_AS_OVER_ANNOTATED: three GO:0005515 protein binding IPIs (bare protein binding).
</content>


## 2026-10-12: source-specific reassessment

This entry supersedes the earlier blanket protein-binding overannotation policy, the assertion that an enzyme cannot participate in transport, and the duplicate formal catalytic cores. The historical journal above is preserved. The current synthesis is one reversible carnitine O-acyltransferase activity at the matrix face of the mitochondrial inner membrane. Broader beta-oxidation participation remains supported; the most compact core process is the carnitine shuttle.

### Human enzyme, reaction direction and product

The human liver peptide/cDNA paper describes the enzyme [PMID:1988962 "an inner mitochondrial membrane enzyme"]. The official precursor has 658 residues and the original mature N terminus supports a 25-residue leader. Its [published correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC53056/) changes G283 to A and E375 to G, retaining product length. There is one officially displayed product and no listed alternative isoform. Historical use of CPT1 for this locus is accession-qualified; it is not a transfer from modern CPT1A.

The [genuine accepted manuscript of PMID:20538056](https://hal.archives-ouvertes.fr/hal-00608982/document) was recovered separately from the unchanged abstract cache. Methods 2.2–2.5 describe a complete, sequence-verified human ORF expressed in yeast and homogenate assays with endogenous CAT2 removed, empty-vector controls and ESI-MS/MS acylcarnitine detection. The measured direction is acyl-CoA plus carnitine to acylcarnitine, whereas the ordinary matrix shuttle regenerates acyl-CoA. The protein reaches the yeast mitochondrial fraction but is incompletely processed. The authors explicitly describe reverse activity in that original study (PMID:20538056). This does not turn the assay into direct measurement of human beta-oxidation flux.

The full substrate panel includes C8–C18 activity and lower C20 activity. C18 is not an absolute cutoff. C8 and C16 functions, broad carnitine O-acyltransferase activity and the more general metabolic assertions can coexist. The broad acyltransferase rows are refined to carnitine O-acyltransferase; no additional activity is manufactured. The current carnitine-shuttle definition includes acyl transfer and is a typed child of long-chain fatty-acid transport, so the shuttle refinement records the target-performed chemistry rather than denying transport-pathway participation.

The COS-cell disease-variant abstract reports depressed variant activity [PMID:7711730 "both mutations drastically depressed the catalytic activity of CPT II"]. Full Methods were not recovered, so exact inserts and substrates are not invented. The patient-derived myocyte abstract reports C16 accumulation [PMID:24780397 "CPT II-deficient myocytes accumulated more palmitoylcarnitine (C16)"]. These are cellular profiles, distinct from an isolated turnover assay. Their positive curated activity assertions are retained with these access limits.

### Localization and conditional physiology

The current protein record specifies peripheral association with the inner membrane on its matrix side. Actual human MitoCoP Table S1 has CPT2/P23786 in sheet A row 265 and sheet B row 240, with positive subtractive, spatial and importomics evidence and a peripheral-membrane classification. Its protein group does not establish an unlisted isoform. HPA antibody HPA028214 supports mitochondrial staining in three human cell lines, with additional nuclear locations in its metadata; no exclusive localization or new nuclear annotation follows. Original image pixels were not examined for HPA.

The rat structure in [PMID:16781677](https://doi.org/10.1016/j.bbrc.2006.06.006) used residues 32–658 with a C-terminal His tag and detergent. Its membrane-attachment model and small crystal interfaces do not establish a fixed native human oligomer. The older human purification abstract reports a 274-kDa preparation and 66-kDa subunit estimate, but full Methods remain unavailable. No obligatory oligomer or demonstrated CPT2–translocase contact is added to the core.

Mouse muscle deletion in PMID:28916721 reduces long-chain fatty-acid oxidation, while the actual adipose study PMID:25578732 links Cpt2 loss to cold intolerance and deficient thermogenic gene induction. These support biochemical participation and a conditional thermogenic contribution, respectively. They are not human cold-challenge studies and do not make CPT2 an autonomous transcriptional regulator or kinase. The two existing thermogenesis transfers remain non-core.

### Phylogenetic and electronic evidence

The actual PTHR22589 tree contains 623 nodes. The 658-residue human sequence exactly matches its aligned target, and the three pertinent IBDs at PTN000501944 lie on the human lineage. The observed IRDs lie outside that path. Target-self evidence and a short donor list are not defects. The complete literal donor records remain available in the accompanying [authored evidence index](CPT2-manual-evidence.yaml); expression, perturbation and biochemical evidence are distinguished.

The fly beta-oxidation study PMID:25588812 has an [Editorial Expression of Concern](https://www.nature.com/articles/s41598-020-70053-7), PMID:32737422. The notice explains the unavailable materials [PMID:32737422 "not available for request by readers wishing to repeat this work"]. Specifically, the fly stocks and DNA constructs/maps were not retained. This is a reproducibility limitation, not a retraction or demonstration that its result is false. Human and mammalian evidence independently support the target process. The original fly Results and Methods also differ in the numbered residue of the inactive rat rescue construct; no unverified resolution is assumed.

Current ARBA00087538 and ARBA00088749 each match the target's three-FunFam branch. No current branch among ARBA00026962's 380 conditions matches the target. The historical mitochondrial-rule premise remains unresolved, while direct target localization remains sound. The authentic InterPro2GO, Rhea-linked UniProt reactions, Compara records, UniPathway cross-reference and official GO methods are distinguished from independent experiments. Direct Rhea webpage retrieval was blocked; the reaction is authenticated through the official target record, GO cross-reference and human chemistry.

### Positive interaction evidence and its limits

The exact 2017 and 2021 BioPlex records identify CPT2 as prey with tagged MCUR1 as bait in HEK293T AP-MS. They support positive association without resolving direct contact or calcium-uniporter regulation by CPT2. MCUR1 is a regulator rather than the channel itself. Those two assertions remain generic non-core binding under the standing campaign policy.

The actual HuRI records identify positive CPT2–CYSRT1 and CPT2–OTX1 pairs in yeast, including the original fusion and validation metadata. The separate OTX1 row is refined to RNA-polymerase-II-specific DNA-binding transcription-factor binding. This describes the partner class; it does not assign DNA binding, transcriptional regulation or native nuclear colocalization to CPT2. Human OTX1 was actually tested in PMID:18849347 despite its title foregrounding other OTX proteins. Promoter binding and reporter transactivation support its class; double normalization, the absence of detectable OTX1 in examined native RPE, and OTX2/CRX-only controls remain explicit. CYSRT1 has no defensible finer binding-class assignment here, so positive generic binding remains non-core.

### Source reconciliation and remaining questions

The 32 historical assertions are preserved. Thirty-one uniquely match current assertions at the fields they actually contain; 15 omit historical WITH/FROM information, which is not silently filled. The old HuRI aggregate lacks a unique partner mapping and is retained as retired provenance. Two complete current partner-specific rows and one current ARBA mitochondrial row are appended, giving 35 total objects and 34 active assertions. Retirement is not biological rejection. The complete current GOA records, source links and reconstruction details in the evidence index are authored provenance, not independent biological evidence.

Important remaining questions concern the physiological human assembly state, the endogenous contexts of the measured interaction pairs, and the balance of forward and reverse CPT2 flux under different metabolic conditions. None requires an additional unsupported GO annotation.


## 2026-10-12 — Substrate breadth and interaction scope

The single catalytic core is represented by carnitine O-acyltransferase activity (GO:0016406). This supersedes the narrower palmitoyl-only core label above, while preserving the experimentally supported palmitoyl and octanoyl annotations. In [PMID:20538056](https://doi.org/10.1016/j.bbadis.2010.06.002), the original accepted manuscript, Methods 2.2–2.5 and Results 3.1, describes the complete human ORF expressed in yeast and acylcarnitine formation in homogenates with empty-vector controls. The substrate panel includes medium and long chains and lower C20 activity. Mitochondrial processing was incomplete, and the measured direction is the reverse of the usual matrix acyl-CoA-regenerating reaction. The broader catalytic term therefore captures one enzyme's measured substrate range without adding a second activity or claiming a purified mature-human preparation.

The OTX1 interaction remains a secondary binding observation. [HuRI](https://doi.org/10.1038/s41586-020-2188-x) records EBI-22741336, EBI-22733631 and EBI-24264064 identify the human CPT2–OTX1 pair in yeast two-hybrid formats; they are related records from one study, not three independent publications. Separately, [PMID:18849347](https://pmc.ncbi.nlm.nih.gov/articles/PMC2605189/) establishes human OTX1 promoter binding and reporter transactivation (Results, Figures 2A and 3A; expression-vector, EMSA and transfection Methods). The reporter required double normalization because OTX1 also activated control promoters. Competition and detailed mutant-reporter results restricted to OTX2/CRX are not transferred to OTX1.

[GO:0061629](https://www.ebi.ac.uk/QuickGO/term/GO:0061629) classifies binding to a sequence-specific RNA polymerase II transcription factor. Its transcriptional requirement describes the bound factor, not an additional activity of CPT2. Positive interaction evidence and independent partner-class evidence therefore support this refinement under the project's binding guidance. They do not establish CPT2 DNA binding, transcriptional regulation, a nuclear role, or an endogenous CPT2–OTX1 complex. The physiological encounter remains unresolved. This is distinct from the MCUR1 and CYSRT1 associations, for which the same class-specific refinement has not been established.

The earlier quotation attributed to PMID:32737422 was read in the [original publisher's Editorial Expression of Concern](https://www.nature.com/articles/s41598-020-70053-7), in its operative paragraph about retained stocks and constructs. It was not read in the repository's metadata-only [publication cache](../../../publications/PMID_32737422.md). The notice concerns reproducibility materials, not a retraction or proof that the fly phenotype is false. The earlier journal entry and its quotation are preserved with this explicit source attribution.

Full original access remains unavailable for PMID:7711730, PMID:24780397, PMID:2174799 and PMID:12200419; their reference flags now agree with the existing access explanations. Rat studies PMID:9136891, PMID:2355018, PMID:12200419, PMID:10796071 and PMID:10380116 remain as donor or expression-context evidence, not invented human experiments. Their literal donor records and access boundaries are documented in the [manual evidence index](CPT2-manual-evidence.yaml), which is an authored provenance projection rather than an independent biological source.
