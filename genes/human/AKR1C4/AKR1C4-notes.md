# AKR1C4 (P17516) — gene review notes

## Identity
- UniProt: P17516 (AK1C4_HUMAN), 323 aa, gene AKR1C4 (synonym CHDR), human (NCBITaxon:9606).
- Names: Aldo-keto reductase family 1 member C4; 3-alpha-hydroxysteroid 3-dehydrogenase type I (3-alpha-HSD1); Chlordecone reductase (CDR); Dihydrodiol dehydrogenase 4 (DD-4/DD4); HAKRA. [file:human/AKR1C4/AKR1C4-uniprot.txt, "RecName: Full=Aldo-keto reductase family 1 member C4"]
- Member of the aldo/keto reductase family. [file:human/AKR1C4/AKR1C4-uniprot.txt, "Belongs to the aldo/keto reductase family."]

## Core molecular function
- Cytosolic NADPH-dependent aldo-keto reductase catalyzing reduction of ketosteroids to hydroxysteroids, with broad substrate specificity producing 3alpha/beta-, 17beta- and 20alpha-hydroxysteroids. [file:human/AKR1C4/AKR1C4-uniprot.txt, "Cytosolic aldo-keto reductase that catalyzes NADPH-dependent"]
- The general catalyzed reaction: `a 3alpha-hydroxysteroid + NADP(+) = a 3-oxosteroid + NADPH + H(+)` (EC 1.1.1.357; GO:0140169 3-alpha-hydroxysteroid 3-dehydrogenase [NAD(P)+] activity). Physiological direction is right-to-left (reductase). [file:human/AKR1C4/AKR1C4-uniprot.txt, "Reaction=a 3alpha-hydroxysteroid + NADP(+) = a 3-oxosteroid + NADPH +"]
- Named as type 1 3alpha-HSD; the expressed enzyme interconverts 5alpha-dihydrotestosterone and 5alpha-androstane-3alpha,17beta-diol, and is virtually liver-specific. [PMID:7650035 "The expressed proteins \ncatalyzed the interconversion between 5 alpha-dihydrotestosterone and 5 \nalpha-androstane-3 alpha,17 beta-diol"], [PMID:7650035 "The mRNA transcript of the type I enzyme \nwas found only in the liver"]
- Most catalytically efficient of the four human AKR1C 3alpha-HSD isoforms; virtually liver-specific; forms 5alpha/5beta-tetrahydrosteroids robustly. [PMID:10998348 "AKR1C4 was the most catalytically efficient"], [PMID:10998348 "AKR1C4 was virtually liver-specific \nand its high k(cat)/K(m) allows this enzyme to form \n5alpha/5beta-tetrahydrosteroids robustly"]
- Also displays significant 3beta-HSD activity (reduces DHT to both 3alpha- and 3beta-diol); in vivo works preferentially as a reductase because the oxidase activity is inhibited by low micromolar NADPH. [PMID:14672942 "AKR1Cs catalyze the \nreduction of DHT into both 3alpha- and 3beta-Diol"], [PMID:14672942 "in vivo all AKR1Cs will preferentially \nwork as reductases"]
- NADP(H)-dependent; cofactor binding residues span 20-24, 50, 166-167, 190, 216-221, 270-280 (crystal 2FVL, NADP+ complex). [file:human/AKR1C4/AKR1C4-uniprot.txt, "COMPLEX WITH NADP(+)"]

## Additional (broad, promiscuous) activities — mostly in-vitro substrate range
- Estradiol 17-beta-dehydrogenase (reduces estrone to 17beta-estradiol, low efficiency). [file:human/AKR1C4/AKR1C4-uniprot.txt, "Catalyzes the reduction of estrone into 17beta-"], EXP PMID:10998348.
- Androsterone dehydrogenase [NAD(P)+] (GO:0047023): reduction of 5alpha-androstan-3,17-dione ⇌ androsterone. EXP PMID:10998348, PMID:7650035; IDA PMID:21851338.
- Testosterone dehydrogenase (NAD+/NADP+) (GO:0047035 / GO:0047045): oxidizes testosterone to androst-4-ene-3,17-dione (EC 1.1.1.51). EXP PMID:10998348.
- 5-alpha-androstane-3-beta,17-beta-diol dehydrogenase (NADP+) (GO:0047024, EC 1.1.1.210): the 3beta-HSD reaction. EXP PMID:14672942.
- Chlordecone reductase (GO:0047743, EC 1.1.1.225): biotransforms the pesticide chlordecone (Kepone) to its alcohol, increasing biliary excretion and reducing neurotoxicity. Historically purified/cloned as "chlordecone reductase". [PMID:2427522 "chlordecone reductase resembles the family of xenobiotic metabolizing enzymes"], [PMID:2187532 "Chlordecone (Kepone), a toxic organochlorine pesticide, undergoes bioreduction \nto chlordecone alcohol in human liver"]. IDA PMID:2427522, EXP PMID:2187532.
- Reduces conjugated (sulfate/glucuronide) DHT; AKR1C4 shows superior catalytic efficiency versus the other isoforms, unaffected by conjugation → hepatic "conjugation pathway" for Dht metabolism (UGT2B17 then AKR1C4). [PMID:19218247 "AKR1C4,\n however, showed superior catalytic efficiencies versus the other\n isoforms, and those were unaffected by steroid conjugation"], [PMID:19218247 "sequential reactions of\n UGT2B17 and AKR1C4 in liver"].
- Retinaldehyde reductase: reduces retinaldehyde with low Km (~1 uM). [PMID:21851338 "All of the enzymes except AKR1C2 showed \nretinaldehyde reductase activity with low Km values"]. IDA (retinal dehydrogenase GO:0001758) PMID:21851338.

## Biological processes / physiology
- Bile-acid synthesis: as liver 3alpha-HSD it reduces the 3-oxo group of 5beta-reduced bile-acid intermediates to 3alpha-hydroxy (downstream of AKR1D1 5beta-reductase). Reactome places AKR1C4 in the reduction of 5beta-cholesten/cholestan-3-one intermediates (R-HSA-192036, -192160, -193758, -193781, -193800, -193841). DR Reactome bile-acid synthesis pathways R-HSA-193368/193775/193807.
- 3alpha-HSDs are known to be involved in the metabolism of glucocorticoids, progestins, prostaglandins, bile acid precursors, and xenobiotics. [PMID:11158055 "3 alpha-HSDs are involved in the \nmetabolism of glucocorticoids, progestins, prostaglandins, bile acid precursors, \nand xenobiotics"]
- Steroid hormone metabolism / pre-receptor regulation: modulates levels of active androgens, estrogens and progestins; inactivates 5alpha-DHT to 3alpha/3beta-androstanediols. [PMID:10998348 "ability to modulate the \nlevels of active androgens, oestrogens and progestins"], [file:human/AKR1C4/AKR1C4-uniprot.txt, "Regulates ligand availability for steroid hormone receptors."]
- "Backdoor" androgen pathway / male sex determination: with AKR1C2 converts 5alpha-DHP toward allopregnanolone en route to 5alpha-DHT for gonad differentiation; AKR1C4 splicing mutation acts as disease modifier in 46,XY DSD (SRXY8) with causative AKR1C2 mutations. [file:human/AKR1C4/AKR1C4-uniprot.txt, "component of\n"], [PMID:21802064 "The 46,XY DSD individuals also \ncarry a mutation causing aberrant splicing in AKR1C4"].
- Neurosteroid production: reduces 5alpha-DHP and 5alpha-DHDOC to allopregnanolone (3alpha,5alpha-THP) and 3alpha,5alpha-THDOC, GABA-A modulators. [file:human/AKR1C4/AKR1C4-uniprot.txt, "alter neural excitability via allosteric activation of gamma-"]
- Doxorubicin/daunorubicin metabolism: an L311V AKR1C4 variant significantly reduces in-vitro DAUN metabolism. [PMID:20837989 "the L311V variant of AKR1C4 significantly decreased V(max)"].
- Jasmonate target: AKR1C isoforms (incl. AKR1C4) are inhibited by jasmonic acid / methyl jasmonate in cancer cells. [PMID:19487289 "jasmonic acid (JA) and methyl jasmonate \n(MeJ) are capable of inhibiting all four human AKR1C isoforms"].

## Localization
- Cytoplasm, cytosol. [file:human/AKR1C4/AKR1C4-uniprot.txt, "SUBCELLULAR LOCATION: Cytoplasm, cytosol"]
- Reported in urinary/prostatic-secretion exosome proteome (HDA, PMID:23533145) — a large-scale MS catalog, not evidence for a physiological extracellular-exosome function.

## Interactions
- IntAct: binds AKR1C3 (P42330) and PLXDC2 (Q6UX71). [file:human/AKR1C4/AKR1C4-uniprot.txt, "P17516; P42330: AKR1C3"], [file:human/AKR1C4/AKR1C4-uniprot.txt, "P17516; Q6UX71: PLXDC2"]. IPI protein-binding annotations derive from high-throughput BioPlex interactome screens (PMID:28514442, PMID:33961781).

## Curation reasoning summary
- Core MF: GO:0140169 (3-alpha-hydroxysteroid 3-dehydrogenase [NAD(P)+] activity) — best-supported (8 EXP), covers bile-acid 3-oxo reduction and steroid 3-keto reduction. Supporting broad-but-real specific activities kept as non-core: GO:0047023, GO:0047024, GO:0047743, GO:0004303, GO:0047035, GO:0047045. Plus NADP binding as core cofactor MF (GO:0050661 — not currently annotated but supported by structure).
- Core BP: GO:0006699 (bile acid biosynthetic process), GO:0008202 (steroid metabolic process). Androgen metabolic process (GO:0008209) as core/non-core.
- Over-annotation flags: GO:0004032 (aldose reductase, IBA), GO:0047086 (ketosteroid monooxygenase, IBA — wrong reaction class), GO:0006693/GO:0042448/GO:0044597/GO:0044598 (IBA family metabolic processes), GO:0016491 (bare oxidoreductase), GO:0009055 (electron transfer — miscast for a dehydrogenase), GO:0015125/GO:0015721 (bile-acid transporter/transport — misinterpretation of "bile-acid binder"), GO:0071395 (jasmonic acid response — it is a drug target, not a JA-signaling participant), GO:0070062 (exosome HDA), GO:0032787/GO:0042445 (very general ARBA IEA), GO:0016655 (quinone-acceptor oxidoreductase — doxorubicin quinone reduction is peripheral).
- No experimental annotation is proposed for REMOVE. Clearly-wrong purely-electronic (IEA) or MF-miscast annotations proposed for REMOVE where justified; otherwise MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
</content>
</invoke>
