# HSD17B10 (Q99714) review notes

Human 17-beta-hydroxysteroid dehydrogenase type 10. UniProt RecName is
"3-hydroxyacyl-CoA dehydrogenase type-2". Aliases: HADH2, MRPP2, SCHAD, SDR5C1,
ERAB, ABAD, XH98G2. HGNC:4800; Gene ID 3028; X-linked (Xp11.22). 261 aa, homotetramer.

## Summary of biology (a genuinely moonlighting/multifunctional protein)

HSD17B10 has **two distinct, essential roles** that are functionally independent
(the disease impairs both):

1. **Catalytic (metabolic) NAD+-dependent dehydrogenase** of the SDR family.
   - Physiologically the key activity is **(S)-2-methyl-3-hydroxybutyryl-CoA
     dehydrogenase (MHBD)** in **L-isoleucine catabolism** — oxidizes
     (2S,3S)-3-hydroxy-2-methylbutanoyl-CoA to 2-methyl-3-oxobutanoyl-CoA
     (EC 1.1.1.178; GO:0047015). Deficiency causes the "2-methyl-3-hydroxybutyryl-CoA
     dehydrogenase (MHBD) deficiency" organic aciduria
     [PMID:20077426 "a deficiency of the mitochondrial enzyme 2-methyl-3-hydroxybutyryl-CoA dehydrogenase (MHBD) involved in isoleucine metabolism"].
   - Broad **(S)-3-hydroxyacyl-CoA dehydrogenase** activity (EC 1.1.1.35; GO:0003857),
     preferring short/medium straight-chain acyl-CoA, e.g. 3-hydroxybutyryl-CoA
     [PMID:9553139 "This NAD+-dependent dehydrogenase catalyzes the reversible oxidation of L-3-hydroxyacyl-CoAs to form 3-ketoacyl-CoAs, but it does not act on the D-isomers."].
   - Weak intrinsic **17-beta-hydroxysteroid / 3-alpha-hydroxysteroid / alcohol
     dehydrogenase** activity toward steroids, bile acids and 2-propanol
     [PMID:10600649 "The k(cat) of the ADH activity was three orders of magnitude less than the l-3-hydroxyacyl-CoA dehydrogenase activity but was comparable with that of the enzyme's hydroxysteroid dehydrogenase (HSD) activity for oxidizing 17beta-oestradiol"].
   - Multiple steroid/bile-acid substrate specificities were characterized in vitro
     [PMID:12917011 "we here demonstrate novel activities of 17beta-HSD10. Both species variants oxidize the 20beta-OH and 21-OH groups in C21 steroids, and act as 7beta-OH dehydrogenases of ursodeoxycholic or isoursodeoxycholic acid"; "the human orthologue oxidizes the 7alpha-OH of chenodeoxycholic acid ... and cholic acid"].
   - Oxidizes the 3-alpha-OH of **allopregnanolone (brexanolone)**, a neurosteroid
     GABA-A modulator [PMID:19706438 "HSD10(E249Q) was unable to catalyze the dehydrogenation of 2-methyl-3-hydroxybutyryl-CoA and the oxidation of allopregnanolone, a positive modulator of the gamma-aminobutyric acid type A receptor"].
   - Also reported as a **cardiolipin phospholipase C-like** enzyme in vitro
     [PMID:26338420 "SCADs that prevent neurodegenerative disorders, such as Drosophila Sniffer and human HSD10, oxidize cardiolipin with similar kinetic parameters. HSD10 exhibits a strong preference for cardiolipin with oxidized fatty acids. This activity is inhibited in the presence of the amyloid β peptide."].

2. **Structural, NON-catalytic moonlighting** as **MRPP2**, an essential subunit of
   **mitochondrial RNase P** (with TRMT10C/MRPP1 and PRORP/MRPP3). This role is
   independent of the dehydrogenase activity.
   - mt-RNase P is a protein-only enzyme that removes tRNA 5' extensions
     [PMID:18984158 "we identified the components of human mitochondrial RNase P and reconstituted the enzymatic activity from three recombinant proteins ... human mitochondrial RNase P is a protein enzyme that does not require a trans-acting RNA component for catalysis ... composed of a tRNA methyltransferase, a short-chain dehydrogenase/reductase-family member, and a protein of hitherto unknown functional and evolutionary origin"].
   - The MRPP1-MRPP2 (TRMT10C-SDR5C1) subcomplex is a bifunctional
     **m1A9/m1G9 methyltransferase** (SDR5C1/MRPP2 is the non-catalytic partner)
     [PMID:23042678 "a subcomplex of human mitochondrial RNase P ... is the methyltransferase responsible for m(1)G9 and m(1)A9 formation ... the human mitochondrial enzyme, moreover, requires a short-chain dehydrogenase as a partner protein"].
   - The MRPP1/2 complex is a **tRNA-maturation platform**: after 5' cleavage it
     retains the tRNA and enhances ELAC2 3'-processing and presents the tRNA to the
     CCA-adding enzyme
     [PMID:29040705 "MRPP1/2 is not only a component of the mitochondrial RNase P but that it retains the tRNA product from the 5'-processing step and significantly enhances the efficiency of ELAC2-catalyzed 3'-processing for 17 of the 22 tRNAs ... presents the nascent tRNA to the mitochondrial CCA-adding enzyme"].
   - Confirmed by cryo-EM structures of mt-RNase P and mt-RNase Z (ELAC2/SDR5C1/TRMT10C)
     [PMID:38824131; PMID:39516281 "a SDR5C1 ... tetramer of SDR5C1 interacts with a monomer of TRMT10C that wraps around the mt pre-tRNA"].
   - Binds tRNA [GOA: GO:0000049 tRNA binding IDA PMID:29040705].
   - Localizes to mitochondrial matrix / nucleoid, initiating RNA processing there
     [PMID:24703694 "mitochondrial RNA processing enzymes involved in tRNA excision, ribonuclease P (RNase P) and ELAC2 ... associate with nucleoids to initiate RNA processing and ribosome assembly"].

## Disease (HSD10 mitochondrial disease / MHBD deficiency)

X-linked, progressive neurodegeneration, psychomotor regression, seizures,
cardiomyopathy. Crucially, **symptom severity does NOT correlate with residual
dehydrogenase activity** — the pathogenic mechanism is loss of the non-enzymatic
mitochondrial (RNase P/tRNA processing, mitochondrial integrity) function
[PMID:20077426 "clinical symptoms in patients are not correlated with residual enzymatic activity of mutated HSD10 ... a property of HSD10 independent of its enzymatic activity is essential for structural and functional integrity of mitochondria"];
[PMID:25575635 title "Mitochondrial energy failure in HSD10 disease is due to defective mtDNA transcript processing"];
[PMID:24549042 "HSD10 protein levels are significantly reduced ... A reduction in HSD10 levels was accompanied by a reduction in MRPP1 protein ... evidence of impaired processing of precursor tRNA transcripts of the mitochondrial heavy strand"].
Pathogenic missense mutations (e.g. R130C, D86G, Q165H, K212E, P210S, R226Q, N247S,
V12L, V176M, E249Q) impair dehydrogenase AND tRNA methylation/processing
[PMID:25925575 "pathogenic mutations impair SDR5C1-dependent dehydrogenation, tRNA processing and methylation. Some mutations disrupt the homotetramerization of SDR5C1 and/or impair its interaction with TRMT10C"];
[PMID:26950678 "the p.K212E mutation impairs the SDR5C1-dependent mitochondrial RNase P activities"];
[PMID:28888424 "Both mutant proteins showed significant reduction in the dehydrogenase, methyltransferase and tRNA processing activities compared to wildtype"].

## ABAD/ERAB (Alzheimer / Aβ) — treat as disease-association binding, non-core

Historically discovered as an intracellular Aβ-binding protein (ERAB/ABAD) that
mediates neurotoxicity; identical to SCHAD
[PMID:9553139 "the amino acid sequence of this human brain enzyme is identical to that of an endoplasmic reticulum amyloid beta-peptide-binding protein (ERAB), which mediates neurotoxicity in Alzheimer's disease"].
The Aβ (APP) interaction is real but is a disease-association / binding role, not the
protein's evolved core function. Kept as non-core.

## Localization

Authoritative: **mitochondrion / mitochondrial matrix / mitochondrial nucleoid**
[file UniProt: "SUBCELLULAR LOCATION: Mitochondrion ... Mitochondrion matrix, mitochondrion nucleoid"].
Older PINC (ProtInc) TAS annotations to **cytoplasm** and **plasma membrane** (both
from PMID:9338779, the 1997 ERAB discovery paper that mislabeled it as ER/plasma
membrane) are legacy mislocalizations superseded by all later work; marked
over-annotated (kept, not removed, per experimental-annotation policy, though these
are TAS not EXP).

## Core functions authored

1. **MHBD / isoleucine catabolism (metabolic core):** MF GO:0047015
   (3-hydroxy-2-methylbutyryl-CoA dehydrogenase activity) [+ broad GO:0003857
   3-hydroxyacyl-CoA dehydrogenase], BP GO:0006550 (L-isoleucine catabolic process),
   NAD binding GO:0051287, location GO:0005759 (mitochondrial matrix).
2. **mt-RNase P / tRNA 5'-processing (structural moonlighting core):** MF GO:0000049
   (tRNA binding — subunit-level activity), BP GO:0097745 (mitochondrial tRNA 5'-end
   processing), in_complex GO:0030678 (mitochondrial ribonuclease P complex).

## Action tally rationale

- ACCEPT: the well-supported experimental core activities and the RNase P/tRNA roles,
  isoleucine catabolism, MHBD, mitochondrion localization, homotetramerization, tRNA
  binding, RNase P complex, tRNA methylation, 5'/3' processing, CCA addition.
- KEEP_AS_NON_CORE: broad "fatty acid metabolic process", steroid/bile-acid/estrogen/
  androgen/brexanolone/C21 metabolic processes and the various in-vitro HSD/bile-acid
  MF activities (real but minor/in-vitro, not the evolved core), cardiolipin
  dehydrogenase, Aβ (protein binding) interactions, mitochondrion organization (via
  the non-enzymatic role).
- MARK_AS_OVER_ANNOTATED: legacy cytoplasm/plasma membrane localizations; the generic
  "alcohol dehydrogenase (NAD+) activity" Rhea-derived IEA; RNA binding (HDA from a
  global mRNA-interactome screen, non-specific); bare "protein binding" IPIs.
- MODIFY: "cholate 7-alpha-dehydrogenase activity" TAS from PMID:9338779 (that 1997
  paper did not establish bile-acid activity — better to generalize / this is a
  legacy mis-association; the IDA from PMID:12917011 is the real support). Handled by
  keeping the PMID:12917011 IDA and flagging the 9338779 TAS as over-annotated.
- REMOVE reserved for clearly wrong IEA only (none needed to hard-remove here; the
  weak/broad IEAs are kept as non-core or over-annotated rather than removed, per policy).
</content>
</invoke>
