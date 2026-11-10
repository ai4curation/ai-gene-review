# CSGALNACT1 (Q8TDX6) review notes

**Deep research status:** falcon (Edison) deep research failed with an authentication
error on 2026-10-24, and no other provider key was available. No `-deep-research-*.md`
file exists for this gene. The notes below come from the cached publications in
`publications/`, the UniProt record, and cached Reactome entries.

## Identity

- 532-aa type II Golgi membrane protein, chromosome 8 [PMID:11788602 "which consisted
  of 532 amino acids with a type II transmembrane protein topology"; "The coding region
  of this enzyme was divided into seven discrete exons and localized to chromosome 8"].
- CAZy GT7; Pfam PF05679 (CHGN); PANTHER PTHR12369:SF19, in the chondroitin synthase
  family (UniProt record). Two predicted divalent-metal binding sites (UniProt FT
  BINDING 360 and 477, ECO:0000255).
- UniProt: "Belongs to the chondroitin N-acetylgalactosaminyltransferase family."

## Molecular function

- Transfers beta1,4-GalNAc from UDP-GalNAc to GlcA. Uyama et al. 2002 showed both
  GalNAcT-II (polymer chondroitin) and GalNAcT-I (linkage-region acceptor) activity
  [PMID:11788602 "transferred beta1,4-N-acetylgalactosamine (GalNAc) from
  UDP-[(3)H]GalNAc not only to a polymer chondroitin representing growing chondroitin
  chains (beta-GalNAc transferase II activity) but also to
  GlcUAbeta1--3Galbeta1-O-C(2)H(4)NH-benzyloxycarbonyl, a synthetic substrate for
  beta-GalNAc transferase I"].
- Gotoh et al. 2002 independently: [PMID:12163485 "N-Acetylgalactosaminyltransferase
  activity was observed toward chondroitin poly- and oligosaccharides, chondroitin
  sulfate oligosaccharides, and linkage tetrasaccharide (GlcA-Gal-Gal-Xyl-O-methoxyphenyl)"].
  It transferred GalNAc, not Gal [PMID:12163485 "It transferred N-acetylgalactosamine, not
  galactose, to para-nitrophenyl-beta-glucuronic acid"].
- Division of labour with CSGALNACT2: T1 is the main initiator, T2 mainly elongates
  [PMID:12446672 "CSGalNAcT-1 is involved in the initiation of chondroitin sulfate
  synthesis, whereas CSGalNAcT-2 participates mainly in the elongation, not initiation"].
  Overexpressing CSGALNACT1 in CHO cells switched a heparan sulfate attachment site to
  chondroitin sulfate [PMID:12446672 "the replacement of heparan sulfate on a
  syndecan-4/fibroblast growth factor-1 chimera protein by chondroitin sulfate"].
- Disease variants lose activity: H234R and M509R [PMID:21160489 "they exhibited no
  N-acetylgalactosamineT-II activities"]; P384R [PMID:27599773 "Biochemical studies
  revealed a reduced GalNAc-transferase activity of the Arg-384 mutant protein"];
  D432Y and N264S [PMID:31705726 "Biochemical studies demonstrated significantly reduced
  CSGalNAcT-1 activity of the novel missense variants"].

## Biological process

- Chondroitin/dermatan sulfate chain initiation and elongation on the GAG-protein linker
  tetrasaccharide [PMID:11788602 "the enzyme is involved in the biosynthetic initiation
  and elongation of chondroitin sulfate and is the key enzyme responsible for the
  selective chain assembly of chondroitin/dermatan sulfate on the linkage region
  tetrasaccharide"].
- Cartilage: highest-expressed CS GalNAc transferase in developing cartilage;
  overexpression increases CS chain number on aggrecan [PMID:17145758 "These
  observations indicate that CSGalNAcT-1 overexpression increases the number of CS
  chains attached to aggrecan core protein"].
- Human disease: biallelic loss of function causes a mild skeletal dysplasia with joint
  laxity and advanced bone age (SDJLABA, CSGALNACT1-CDG) [PMID:27599773; PMID:31325655;
  PMID:31705726]. Patient fibroblasts show fewer CS/DS chains and more HS
  [PMID:31705726 "A consequent decrease in CS/DS chain initiation activity was reflected
  in reduced numbers of CS/DS chains on core proteins in fibroblasts from patients P1 and
  P2"]. Increased HS is attributed to linker accumulation, not to an HS-synthesising
  role of CSGALNACT1 [PMID:31705726 "caused by accumulation of the tetrasaccharide
  linker, which functions as an acceptor substrate for the HS glycosyltransferases"].

## Location

- Golgi membrane (Reactome R-HSA-1971482, R-HSA-9632033; UniProt subcellular location
  "Golgi apparatus, Golgi stack membrane", ECO:0000305 from PMID:11788602).

## The PMID:11514575 problem (FRR:0001 flag)

- FRR:0001 flagged the IDA `GO:0008955 peptidoglycan glycosyltransferase activity`.
  GO:0008955 (checked in OLS, not obsolete) is defined by the bacterial lipid II
  GlcNAc-MurNAc-pentapeptide polymerisation reaction on undecaprenyl diphosphate. No
  vertebrate GT7 enzyme does this. The term is wrong.
- The paper itself is about a different protein. Kitagawa et al. 2001 cloned human
  **chondroitin synthase** (CHSY1, Q86X52): [PMID:11514575 "The identified protein
  consists of 802 amino acids with a type II transmembrane protein topology"; "The
  coding region of the chondroitin synthase was divided into three discrete exons and
  localized to chromosome 15"]. CSGALNACT1 is 532 aa on chromosome 8 and was cloned in
  2002 using that synthase as the homology query [PMID:11788602 "Based on sequence
  homology with the recently cloned human chondroitin synthase, we identified a novel
  beta1,4-N-acetylgalactosaminyltransferase"; "The amino acid sequence displayed 27%
  identity to that of human chondroitin synthase"]. Because the abstracts state these
  facts, the attribution can be judged without the full text. CHSY1's GOA carries the
  same paper (GO:0047238 and GO:0050510 IDA), and this repo's CHSY1 review relies on it.
- So all ten UniProt 2003-12-16 rows on Q8TDX6 from PMID:11514575 are wrong-gene rows.
  Rows whose term is true of CSGALNACT1 on other evidence (Golgi membrane,
  acetylgalactosaminyltransferase activity, CS proteoglycan biosynthesis) are kept on
  that other evidence, and their reference is flagged. Rows whose term is false or
  CHSY1-specific (peptidoglycan GT, glucuronosyltransferase, UDP-GlcA and UDP-GalNAc
  metabolism, heparan sulfate and heparin PG biosynthesis) are removed.
- Decision on GO:0008955: **REMOVE**, not MODIFY. A MODIFY would leave a GalNAc-transferase
  claim on CSGALNACT1 resting on a paper that never assayed CSGALNACT1. The correct
  activity (GO:0047238/GO:0047237) is already carried by other rows with proper
  evidence. Two source defects are recorded: WRONG_TERM (the CHSY1 activity the curator
  meant is GO:0047238/GO:0050510) and WRONG_GENE_PRODUCT (should be Q86X52).

## ISS rows from PMID:11788602 (WITH UniProtKB:Q8N6G5)

- PMID:11788602 directly characterised CSGALNACT1 itself (532 aa, chr 8). The ISS rows
  name Q8N6G5 (CSGALNACT2) as the source. The evidence is better stated as IDA on
  Q8TDX6. The terms themselves are fine. A CHECK source defect is recorded on the
  evidence code.

## Metal ion binding

- NAS from PMID:12163485; the abstract does not mention metals. UniProt predicts two
  divalent-metal binding residues (ECO:0000255). GT7 enzymes typically use Mn2+ with
  UDP-sugar donors, but there is no CSGALNACT1-specific metal data in the cached
  sources. Kept as non-core.
