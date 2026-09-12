# GLUL (Glutamine synthetase / glutamate--ammonia ligase) — review notes

UniProt: P15104 (GLNA_HUMAN). HGNC:4341. Gene synonym GLNS. EC 6.3.1.2.
Chromosome 1. 373 aa; N-terminal Met removed, mature protein 2..373.

## Core enzymatic function

GLUL is glutamine synthetase, the ATP-dependent ligase that condenses
L-glutamate + ammonium + ATP to give L-glutamine + ADP + phosphate.

- UniProt CATALYTIC ACTIVITY: `Reaction=L-glutamate + NH4(+) + ATP = L-glutamine + ADP + phosphate + H(+)`; `Rhea:RHEA:16169`; `EC=6.3.1.2`; evidence `ECO:0000269|PubMed:16267323, PubMed:30158707, PubMed:36289327` [file:human/GLUL/GLUL-uniprot.txt].
- FUNCTION line: "Glutamine synthetase that catalyzes the ATP-dependent conversion of glutamate and ammonia to glutamine" [file:human/GLUL/GLUL-uniprot.txt].
- Reaction proceeds via a gamma-glutamyl phosphate intermediate; requires divalent metal cofactor Mg(2+) or Mn(2+) (UniProt COFACTOR: Mg2+ ECO:0000250|P09606, Mn2+ ECO:0000269|PubMed:18005987; PDB 2QC8 shows bound Mn). Activity inhibited by methionine sulfoximine (MSO) [file:human/GLUL/GLUL-uniprot.txt, "Glutamine synthetase activity is inhibited by"].
- Structure: decamer composed of two pentamers [file:human/GLUL/GLUL-uniprot.txt, "Decamer; composed of two pentamers"; PMID:18005987 crystal structures of mammalian GS]. Note: human brain GS reported as octamer by [PMID:12387715], but the crystallographic/EM consensus is decameric (two stacked pentamers).

## Physiological role of the enzymatic activity

Principal enzyme of ammonia detoxification/assimilation and glutamine (nitrogen
carrier, neurotransmitter precursor) biosynthesis.

- "in the brain, it regulates the levels of toxic ammonia and converts neurotoxic glutamate to harmless glutamine, whereas in the liver, it is one of the enzymes responsible for the removal of ammonia" [file:human/GLUL/GLUL-uniprot.txt].
- Astrocytic role in the glutamate-glutamine cycle (Reactome R-HSA-210455 "Astrocytic Glutamate-Glutamine Uptake And Metabolism").
- Reactome R-HSA-70606: "Cytosolic glutamine synthetase (glutamate-ammonia ligase - GLUL) catalyzes the reaction of glutamate, ammonia, and ATP to form glutamine, ADP, and orthophosphate. The enzyme is a decamer" [reactome/R-HSA-70606.md].
- Liver zonation: GS is perivenous; glutamate is taken up by perivenous hepatocytes and is the main source for glutamine synthesis catalyzed by GS [PMID:21757002 "Glutamate is taken up by perivenous hepatocytes and is the main source for the synthesis of glutamine, catalyzed by glutamine synthase (GS)"].
- Broad review context: "Glutamine synthetase plays a major role in ammonia detoxification, interorgan nitrogen flux, acid-base homeostasis, and cell signaling" [PMID:16267323 abstract].

## Location

Mainly cytosol, with a fraction at the plasma membrane (lipid-anchored via
palmitoylation).

- "SUBCELLULAR LOCATION: Cytoplasm, cytosol ... Microsome ... Mitochondrion ... Cell membrane; Lipid-anchor. Note=Mainly localizes in the cytosol, with a fraction associated with the cell membrane" [file:human/GLUL/GLUL-uniprot.txt]. IDA cytosol + IDA plasma membrane from [PMID:30158707], IDA cytosol from [PMID:36289327].
- Microsome/mitochondrion assignments are `ECO:0000250|UniProtKB:P09606` (by similarity, sheep enzyme) — not human-experimental. IEA mitochondrion (SubCell) and ISS mitochondrion are low-confidence; the mammalian enzyme is overwhelmingly cytosolic.

## Disease

- Congenital glutamine deficiency (GLND, MIM:610015), autosomal recessive: "two unrelated newborns who had congenital human glutamine synthetase deficiency with severe brain malformations resulting in multiorgan failure and neonatal death. Glutamine was largely absent from their serum, urine, and cerebrospinal fluid. Each infant had a homozygous mutation in the glutamine synthetase gene (R324C and R341C)" [PMID:16267323]. R324C / R341C reduce GS activity.
- Developmental and epileptic encephalopathy 116 (DEE116, MIM:620806), autosomal dominant late-onset systemic form: caused by de novo start-loss variants that reinitiate translation at Met-18; the resulting protein is enzymatically competent but insensitive to glutamine-induced degradation [file:human/GLUL/GLUL-uniprot.txt DISEASE DEE116; PMID:38579670 (UniProt ref, not cached)].
- GS is regulated by feedback: elevated glutamine promotes p300/EP300 acetylation (Lys-11, Lys-14) followed by CRL4(CRBN)-mediated ubiquitination and proteasomal degradation (PMID:26990986, UniProt).

## Moonlighting / non-canonical functions (annotated, but non-core)

1. Angiogenesis / endothelial cell migration, glutamine-synthesis-independent
   [PMID:30158707, Nature 2018]: "Independently of its glutamine synthetase
   activity, required for endothelial cell migration during vascular
   development" [file:human/GLUL/GLUL-uniprot.txt]. Mechanism: GLUL
   autopalmitoylates and palmitoylates the GTPase RHOJ, sustaining RHOJ membrane
   localization/activation. This underlies the IDA annotations to
   protein-cysteine S-palmitoyltransferase activity (GO:0019706), protein
   palmitoylation (GO:0018345), regulation of endothelial cell migration
   (GO:0010594), regulation of sprouting angiogenesis (GO:1903670), and RHOJ
   interaction (GO:0005515 IPI Q9H4E5). The palmitoyltransferase activity is a
   proposed (EC 2.3.1.225, ECO:0000305) function, not a canonical acyltransferase
   fold; treat as real but non-core.
2. Ribosomal 40S subunit biogenesis [PMID:26711351]: genome-wide RNAi screen —
   "intracellular glutamine synthesis supports 40S subunit production." GS/GLUL
   was identified as required (R324A mutant loses nucleolar localization of BYSL;
   the GLND R324C variant also impairs 40S synthesis). This supports the IMP
   annotations to ribosome biogenesis (GO:0042254) and regulation of protein
   localization to nucleolus (GO:1904749). Note the paper attributes the effect
   to glutamine synthesis, i.e. downstream of the canonical enzymatic activity.
3. BEST2 chloride channel regulation / glutamate release [PMID:36289327, Nature
   2022]: GLUL forms a complex with bestrophin-2 (BEST2, Q8NFU1); the interaction
   tethers a GS fraction to the membrane and reciprocally gates BEST2. Underlies
   the IPI to Q8NFU1 and the membrane-tethered cytosol IDA.
4. Proliferation of fetal skin fibroblasts [PMID:18662667]: GS activity is
   required for proliferation; loss of activity (R324C or MSO) drops
   proliferation without affecting apoptosis. Supports GO:0008283 IDA. This is
   plausibly a downstream consequence of glutamine supply rather than a distinct
   molecular function.
5. Erythropoiesis / ammonium detoxification during heme synthesis: "Plays a key
   role in ammonium detoxification during erythropoiesis" (By similarity to mouse
   P15105); supports ISS GO:0045648 positive regulation of erythrocyte
   differentiation and ISS GO:0097275 intracellular ammonium homeostasis.

## Protein-binding / interactome annotations

Many `protein binding` (GO:0005515) and `identical protein binding` (GO:0042802,
homodecamer self-interaction) IPI annotations come from large-scale interactome
screens (PMID:16189514, 19447967, 21988832, 25416956, 25502805, 25910212,
31515488). These full-text papers do not mention GLUL by name in the cached text
(GLUL appears only in supplementary interaction tables) — they are uninformative
bare-binding annotations, kept as non-core. TAT (P17735) interaction (PMID:25910212)
is a systematic-screen hit. Informative interactions with functional context are
RHOJ (Q9H4E5, PMID:30158707) and BEST2 (Q8NFU1, PMID:36289327).

## Location over-annotations to watch

- GO:0005634 nucleus (HDA, PMID:21630459, sperm-nucleus proteome) and GO:0070062
  extracellular exosome (HDA, PMID:19056867, urinary exosome proteome) are
  high-throughput mass-spec localizations typical of abundant cytosolic enzymes;
  over-annotations, keep as non-core.
- GO:0005739 mitochondrion (IEA SubCell + ISS from sheep P09606) and GO:0005886
  plasma membrane: mitochondrion is by-similarity only and biologically dubious
  for the human cytosolic enzyme; plasma membrane is the palmitoylation-anchored
  fraction (supported by IDA).

## Core function synthesis

Single dominant core molecular function: glutamine synthetase activity
(GO:0004356) + ATP binding (GO:0005524), in the cytosol (GO:0005829), driving
L-glutamine biosynthesis (GO:1901704) and intracellular ammonium homeostasis
(GO:0097275). Note GO:0006542 "glutamine biosynthetic process" is OBSOLETE;
current term is GO:1901704 "L-glutamine biosynthetic process" (verified via OLS,
2026-07). The palmitoyltransferase/angiogenesis role is a genuine but
non-canonical moonlighting activity.
