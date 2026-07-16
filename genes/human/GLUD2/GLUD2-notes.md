# GLUD2 (P49448) review notes

Human GLUD2, glutamate dehydrogenase 2, mitochondrial (EC 1.4.1.3). HGNC:4336, GeneID 2747,
X-linked, intronless. UniProt entry name DHE4_HUMAN. Sources below are the local files in
`genes/human/GLUD2/` and cached publications in `publications/`.

## Identity, gene origin, expression

- GLUD2 is a **hominoid-specific retrogene** that arose by retroposition (reverse transcription of
  a GLUD1 mRNA) in the common hominoid ancestor ~18-25 Mya; it is intronless and X-linked
  [PMID:18688271 "It is encoded by the intronless GLUD2 gene, which emerged via the reverse transcription of a messenger RNA from its parental gene GLUD1 in the hominoid ancestor 18–25 million years ago (Mya)"].
- Originally described as a "novel human glutamate dehydrogenase expressed in neural and testicular
  tissues and encoded by an X-linked intronless gene"; RT-PCR showed expression in retina, testis,
  and, at lower levels, brain [PMID:8207021 "the novel cDNA is expressed in human retina, testis, and, at lower levels, brain"].
- UniProt TISSUE SPECIFICITY: "Expressed in retina, testis and, at a lower level, brain."
  [file:human/GLUD2/GLUD2-uniprot.txt]. In brain, GDH is predominantly astrocytic
  [PMID:12742085 "In mammalian brain, glutamate dehydrogenase (GDH) is located predominantly in astrocytes"].
- Note: a later observation cited in PMID:18688271 says GLUD2 is transcribed in many/most human
  tissues, in contrast to the earlier brain/retina/testis-restricted picture
  [PMID:18688271 "recent work revealed that GLUD2 (similarly to GLUD1) is transcribed in many or most human tissues"].
  HPA (UniProt DR) lists it as "Group enriched (liver, testis)".

## Molecular function (catalysis)

- Reversible oxidative deamination of L-glutamate, using either NAD+ or NADP+ as cofactor
  (EC 1.4.1.3). UniProt records both catalytic activities
  [file:human/GLUD2/GLUD2-uniprot.txt "Reaction=L-glutamate + NAD(+) + H2O = 2-oxoglutarate + NH4(+) + NADH +"]
  and
  [file:human/GLUD2/GLUD2-uniprot.txt "Reaction=L-glutamate + NADP(+) + H2O = 2-oxoglutarate + NH4(+) + NADPH"].
- The recombinant retinal (GLUD2) enzyme catalyzed the oxidative deamination of glutamate with
  catalytic properties similar to native brain GDH
  [PMID:8207021 "producing a protein capable of catalyzing the oxidative deamination of glutamate"].
- The reaction links glutamate/amino-acid/nitrogen metabolism to the TCA cycle by producing
  2-oxoglutarate (alpha-ketoglutarate) and ammonia
  [PMID:18688271 "an enzyme catalyzing the oxidative deamination of glutamate to α-ketoglutarate (generating ATP through the Krebs cycle) and ammonia, a reversible reaction that takes place in mitochondria"].
- Because the deamination/reductive-amination reaction is reversible, GDH can also run in the
  glutamate-synthesizing (reductive amination) direction; GOA carries an IDA for
  L-glutamate biosynthetic process (GO:0097054) from PMID:11032875.

## Allosteric regulation (the adaptive, GLUD2-distinguishing properties)

- Unlike housekeeping GLUD1, GLUD2 is essentially **insensitive to GTP inhibition** in its basal
  state, has low basal activity, and is **strongly activated by ADP and by L-leucine**
  [PMID:11032875 "Nonactivated GLUD1 GDH was markedly inhibited by GTP (IC(50) = 0.20 microM:), whereas nonactivated GLUD2 GDH was totally insensitive to this compound (IC(50) > 5,000 microM:)"]
  [PMID:11032875 "L-leucine, at 1.0 mM:, enhanced the activity of the nerve tissue-specific (GLUD2-derived) enzyme by approximately 1,600%"]
  [PMID:11032875 "the presence of ADP (10-50 microM:) sensitized the two isoenzymes to L-leucine"].
- Two positively selected substitutions (Arg443Ser and Gly456Ala relative to GLUD1) account for the
  GTP resistance and ADP dependence, adapting GLUD2 to a high ADP:ATP ratio and intracellular
  acidification, as in synaptic astrocytes during glutamatergic transmission
  [PMID:12742085 "substitution of Ser for Arg443 and Ala for Gly456 are the main evolutionary changes that led to the adaptation of the GLUD2 GDH to the unique metabolic needs of the nerve tissue"]
  [PMID:15578726 "These properties may allow the brain isoenzyme to function well under conditions of intracellular acidification and increased turnover of ATP to ADP, as occurs in synaptic astrocytes during excitatory transmission"].
- So GO terms "GTP binding" (GO:0005525), "ADP binding" (GO:0043531) and "L-leucine binding"
  (GO:0070728) reflect experimentally documented allosteric-effector binding, not the catalytic
  active site. ADP is an activator (physiologically the salient one for GLUD2); GTP binds but does
  not inhibit basal GLUD2; L-leucine is an activator.

## Subcellular localization

- UniProt: **Mitochondrion matrix** (SUBCELLULAR LOCATION, evidence PubMed:22709669)
  [file:human/GLUD2/GLUD2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion matrix"]; N-terminal
  transit peptide residues 1-53 [file:human/GLUD2/GLUD2-uniprot.txt "TRANSIT         1..53"].
- GLUD2 is **specifically targeted to mitochondria** (in contrast to GLUD1, which is mitochondrial
  AND cytoplasmic), because of a positively selected E7K substitution in its mitochondrial targeting
  sequence [PMID:18688271 "whereas GLUD1 localizes to the mitochondria as well as the cytoplasm, GLUD2 is specifically targeted to mitochondria, due to a single key amino acid substitution in its signal peptide"].
- This is the experimental basis for the **NOT located_in cytosol** annotation (GO:0005829, IDA,
  PMID:18688271): GLUD2 is restricted to mitochondria and, unlike GLUD1, is not appreciably
  cytosolic. GOA also has an IDA "located_in mitochondrion" (GO:0005739) from the same paper.
- Confirmed as a mitochondrial protein by the high-confidence human mitochondrial proteome
  (HTP, PMID:34800366) and by HPA immunofluorescence (IDA, GO_REF:0000052).

## Interactions

- UniProt INTERACTION line: P49448 (GLUD2) with P00367 (GLUD1)
  [file:human/GLUD2/GLUD2-uniprot.txt "P49448; P00367: GLUD1; NbExp=2"]. GDH assembles as a
  homohexamer [file:human/GLUD2/GLUD2-uniprot.txt "SUBUNIT: Homohexamer"]; GLUD1 and GLUD2 are near-
  identical paralogs that can co-assemble.
- The two IPI "protein binding" (GO:0005515) annotations (PMID:28514442, PMID:33961781) are
  high-throughput AP-MS interactome screens; both cite WITH = UniProtKB:P00367 (GLUD1). These are
  uninformative bare protein-binding annotations (over-annotation), consistent with the documented
  GLUD1-GLUD2 association but not adding specific functional insight.

## Family / structure

- Belongs to the Glu/Leu/Phe/Val dehydrogenases family [file:human/GLUD2/GLUD2-uniprot.txt
  "SIMILARITY: Belongs to the Glu/Leu/Phe/Val dehydrogenases family"]; NAD(P)-binding Rossmann fold;
  PANTHER PTHR11606:SF15 GLUTAMATE DEHYDROGENASE 2, MITOCHONDRIAL. X-ray structure 6G2U.

## Curation decisions summary

Core functions:
- MF: **GO:0004353 L-glutamate dehydrogenase [NAD(P)+] activity** — best single term for the
  dual-cofactor (NAD+ and NADP+) EC 1.4.1.3 reaction that UniProt documents. GO:0004352 (NAD+) and
  GO:0004354 (NADP+) are the cofactor-specific children, both experimentally/IEA supported.
- MF: **GO:0043531 ADP binding** — physiologically salient allosteric activator (IDA, PMID:12742085).
- BP: **GO:0006538 L-glutamate catabolic process** (deamination direction) and
  **GO:0006536 glutamate metabolic process**.
- CC: **GO:0005759 mitochondrial matrix**.

Actions: experimental MF/BP/CC annotations describing catalysis, effector binding, and mitochondrial
matrix localization are ACCEPTed (or KEEP_AS_NON_CORE where they are supporting biology). The two
bare "protein binding" IPI annotations are MARK_AS_OVER_ANNOTATED (never REMOVE experimental IPI).
Generic IEA parents (oxidoreductase activity, amino acid metabolic process) are KEEP_AS_NON_CORE as
correct-but-general; the EC/InterPro/RHEA IEA catalytic terms are ACCEPT/MODIFY toward the specific
dual-cofactor term. The NOT located_in cytosol IDA is ACCEPTed (well-supported negative).
