# ATP6V1B2 Research Notes

## Gene overview

ATP6V1B2 encodes the non-catalytic B subunit of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase), specifically the brain isoform (also known as subunit B2, the 58 kDa B subunit, or HO57). The V1 complex catalyzes ATP hydrolysis, with three non-catalytic B subunits alternating with three catalytic A subunits in the AB heterohexameric ring. The B subunit cannot independently hydrolyze ATP but is essential for assembly and function of the V1 complex.

## Core function — V-ATPase non-catalytic B subunit

The B2 subunit is the non-catalytic component of the catalytic AB heterodimer. While the catalytic site is on subunit A (ATP6V1A), the B subunit contributes to the structural integrity and regulation of the catalytic hexameric ring and the overall V1 complex assembly.

[PMID:33065002 "The V 1 ATPase is composed of three copies of subunits A, B, E, and G, and one copy of subunit C, D, F, and H"]

[PMID:2145275 "The B subunit (approximately 60 kDa) of the vacuolar H(+)-ATPase is one of the two major subunits comprising the hydrophilic catalytic complex of the enzyme."]

## Brain isoform vs. kidney isoform

ATP6V1B2 (B2) is the brain isoform of the B subunit, ubiquitously expressed. It was originally identified from human brain cDNA and is 90% identical at the amino acid level to the kidney isoform B1 (ATP6V1B1). The kidney isoform B1 is more specifically expressed in renal intercalated cells where it plays a critical role in urinary proton secretion; mutations in B1 cause distal renal tubular acidosis (dRTA).

[PMID:2145275 "We conclude that the B subunit cDNAs from human kidney and brain represent different isoforms. This is the first demonstration of an isoform of a vacuolar H(+)-ATPase subunit."]

ATP6V1B2 can partially compensate for B1 (ATP6V1B1) in renal intercalated cells under baseline conditions but cannot fully compensate under acid load.

[file:human/ATP6V1B2/ATP6V1B2-uniprot.txt "In renal intercalated cells, can partially compensate the lack of ATP6V1B1 and mediate secretion of protons (H+) into the urine under base-line conditions but not in conditions of acid load"]

## Subcellular localizations

ATP6V1B2 is localized to:
- Apical cell membrane of kidney early distal nephron (PMID:29993276, experimental)
- Melanosome (PMID:12643545, proteomics of stage I-IV melanosomes)
- Cytoplasm (by similarity with rat B2)
- Synaptic vesicle membrane (by similarity with rat B2)
- Clathrin-coated vesicle membrane (by similarity)

[PMID:29993276 "Abundant H+-ATPase B1 subunit immunoreactivity was observed in the human kidney. As expected, intercalated cells showed the strongest signal, but significant signal was also observed in apical membrane domains of the distal nephron, including TAL, macula densa, and DCT."]

Note: PMID:29993276 is primarily about B1 (ATP6V1B1), not B2. The paper notes that B2 is also expressed in TAL and DCT. The apical plasma membrane IDA annotation for ATP6V1B2 in GOA comes from this paper but is based on B1 antibody data showing B2 co-localization patterns.

## Tissue distribution

ATP6V1B2 is the ubiquitously expressed B subunit. The kidney paper (PMID:29993276) shows that B2 is expressed in thick ascending limb (TAL) and distal convoluted tubule (DCT). The original 1990 paper (PMID:2145275) isolated B2 from brain, establishing the "brain isoform" nomenclature.

## Melanosome localization

ATP6V1B2 was detected in early melanosomes by mass spectrometry (PMID:12643545). V-ATPase is required for melanosome acidification, which controls melanin biosynthesis.

[PMID:12643545 "Melanin is a heterogeneous biopolymer produced only by specific cells termed melanocytes, which synthesize and deposit the pigment in specialized membrane-bound organelles known as melanosomes."]

## Disease associations

**DDOD (Deafness, congenital, with onychodystrophy, autosomal dominant, MIM:124480)**: Caused by dominant mutations in ATP6V1B2. Main feature is congenital sensorineural hearing loss with nail dystrophy or absence. Coniform teeth, selective tooth agenesis, and hand/foot abnormalities present in some patients. The founding mutation identified by PMID:24913193.

**ZLS2 (Zimmermann-Laband syndrome 2, MIM:616455)**: Caused by dominant mutations in ATP6V1B2. Characterized by facial dysmorphism, gingival enlargement, hypoplasia or aplasia of terminal phalanges/nails, hypertrichosis, joint hyperextensibility, and hepatosplenomegaly. Some patients have intellectual disability with or without epilepsy. ZLS2 is caused by p.Arg485Pro variant (PMID:25915598). KCNH1 mutations cause the allelic Zimmermann-Laband syndrome type 1.

[PMID:25915598 paper: "Mutations in KCNH1 and ATP6V1B2 cause Zimmermann-Laband syndrome"]

## Protein interactions

ATP6V1B2 interacts with WFS1 (Wolfram syndrome protein), as shown in UniProt INTERACTION records. It also interacts with HTT (huntingtin), NEFL (neurofilament light), GFAP, and JPH3 (junctophilin-3). The interaction with HTT-related proteins may be relevant to neurodegenerative disease pathomechanisms.

## Annotation quality notes

- Three protein binding (GO:0005515) annotations from IPI evidence (PMID:25416956 proteomics interactome, PMID:32814053 neurodegeneration proteins interactome, PMID:34159380 SARS-CoV-2 Nsp2 interactome) should be MARK_AS_OVER_ANNOTATED.
- The apical plasma membrane IDA (PMID:29993276) annotation is primarily about the B1 isoform; B2 co-localization is noted but the study focused on B1. Annotation is valid but the evidence is weaker for B2 specifically.
- Regulation of macroautophagy (NAS, PMID:22982048) is an indirect downstream consequence of lysosomal acidification; the lipofuscin paper does not study ATP6V1B2 directly.
- Multiple Reactome TAS annotations for cytosol reflect V1-V0 disassembly; valid but non-core.
- Exosome HDA annotations are from high-throughput proteomics and likely reflect contamination.
