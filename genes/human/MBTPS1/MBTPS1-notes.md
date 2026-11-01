# MBTPS1 (S1P / SKI-1 / PCSK8) review notes

## Provenance / process

- 2026-10-18: Deep research via Falcon (`just deep-research-falcon human MBTPS1`) attempted once and
  failed at authentication ("Exception: Failed to authenticate"; the Edison/Falcon key returns 403).
  No `-deep-research-*.md` file exists for this gene; these notes were compiled manually from the
  cached publications (mostly abstract-only), the UniProt record and Reactome.
- Additional PMIDs cached for this review: 8674110, 10644685, 10944850, 16417584, 32857899
  (plus 10805775/10419520 used for MBTPS2).

## Identity and structure

- 1052 aa type I membrane protein: signal peptide 1-17, propeptide 18-186, lumenal domain
  187-998 containing the peptidase S8 (subtilisin) domain 190-472 with the Asp218/His249/Ser414
  charge-relay triad, a single TM helix 999-1021 and short cytosolic tail (UniProt).
- "Belongs to the peptidase S8 family" (UniProt); a member of the proprotein convertase
  subtilisin/kexin family (PCSK8), but unlike the furin-like PCs it cleaves after non-basic residues
  with Arg/Lys at P4 (R-X-[hydrophobic]-X↓ / RX(L/V/I)X motifs) [PMID:9990022 "Cleavage specificity
  studies show that SKI-1 generates a 28-kDa product from the 32-kDa brain-derived neurotrophic
  factor precursor, cleaving at an RGLT"].
- Ca2+-dependent serine protease [PMID:10644685 "Our data demonstrate that SKI-1 is a
  Ca(2+)-dependent proteinase exhibiting optimal cleavage at pH 6.5."].
- Zymogen; propeptide removed by intramolecular autocatalytic cleavage after Leu186 (RRLL186)
  [PMID:10944850 "the pro-peptide sequence that is released when S1P is self-activated by
  intramolecular cleavage"]; prosegment fragments remain associated and inhibit the enzyme
  [PMID:10644685 "recombinant prosegments of SKI-1 inhibit its activity with apparent inhibitor
  constants of 100-200 nM"].

## Localization

- Processing of proSKI-1 in the ER; mature enzyme in Golgi and punctate endosome-like structures;
  a 98 kDa form is shed into the medium [PMID:9990022 "Immunocytochemical analysis of stably
  transfected HK293 cells shows that SKI-1 is present in the Golgi apparatus and within small
  punctate structures reminiscent of endosomes."; "Late along the secretory pathway some of the
  membrane-bound enzyme is shed into the medium as a 98-kDa form."].
- Golgi is the site of SREBP/ATF6 cleavage [PMID:12782636 "As the Site-1 protease is localized in
  the Golgi apparatus, both SREBP and ATF6 must relocate to the Golgi apparatus to be cleaved."].
- A 2022 report claims a mitochondrial pool forming a complex with ETFA/ETFB [PMID:35362222 "we
  found that S1P is a novel mitochondrial protein that forms a trimeric complex with ETFA/ETFB"].
  Single study; S1P has a canonical ER signal peptide and lumenal catalytic domain, so how a
  mitochondrial pool arises is unexplained. Treated as non-core.

## Substrates / functions (pleiotropic)

1. SREBP-1/-2: first (luminal-loop) cleavage in regulated intramembrane proteolysis (RIP)
   [PMID:8674110 "The first, regulated by sterols, occurs in the lumenal loop."; PMID:9809072
   "Release is initiated by Site-1 protease (S1P), which cleaves SREBPs in the ER luminal loop
   between two membrane-spanning regions."]. Sterol regulation is exerted through SCAP/INSIG
   transport control rather than on S1P itself.
2. ATF6/ATF6B: first cleavage during the UPR [PMID:11163209 "ATF6 is processed by Site-1 protease
   (S1P) and Site-2 protease (S2P), the enzymes that process SREBPs in response to cholesterol
   deprivation."]. AEBSF inhibition of S1P blocks ATF6 cleavage [PMID:12782636].
3. CREB3 family (OASIS/CREB3L1, BBF2H7/CREB3L2, CREB-H/CREB3L3, LUMAN/CREB3) [PMID:16417584
   "OASIS is processed by Site-1 and -2 proteases (S1P and S2P), enzymes that reside at the Golgi
   apparatus and process activating transcription factor 6 (ATF6), in response to ER stress."; Reactome
   R-HSA-8874204, R-HSA-8874206]. BBF2H7 activation drives TANGO1/SEC23A expression and mega-vesicle
   collagen export [PMID:30046013].
4. GNPTAB α/β precursor: S1P cleavage activates GlcNAc-1-phosphotransferase, required for M6P
   tagging of lysosomal enzymes [PMID:21719679 "Here we found that the α/β-subunit precursor is
   cleaved by the site-1 protease (S1P)"]. LYSET/TMEM251 is required for efficient processing
   [PMID:36096887].
5. FAM20C propeptide removal, required for FAM20C secretion and kinase activity in biomineralization
   [PMID:34349020].
6. Pro-BDNF, and (literature, not cached here) viral glycoproteins of arenaviruses (Lassa, LCMV GPC)
   and Crimean-Congo hemorrhagic fever virus — host-pathogen role, not curated here.

## Disease

- Spondyloepiphyseal dysplasia Kondo-Fu type (SEDKF): ~1% residual MBTPS1 gives skeletal dysplasia
  and elevated plasma lysosomal enzymes but near-normal lipids [PMID:30046013 "We found that the
  residually expressed S1P is sufficient for lipid homeostasis but not for ER and lysosomal
  functions, especially in chondrocytes."]; second patient PMID:32857899.
- CAOP syndrome (cataract, alopecia, oral mucosal disorder, psoriasis-like) [PMID:35362222].

## Curation decisions summary

- Core MF: serine-type endopeptidase activity (GO:0004252); generic endopeptidase / serine-type
  peptidase IEAs -> MODIFY to GO:0004252.
- Core location: Golgi membrane; ER membrane (zymogen maturation), extracellular (shed form),
  mitochondrion kept as non-core. ER lumen TAS rows -> MODIFY to ER membrane (the protein is a
  type I membrane protein whose catalytic domain faces the lumen).
- Process: membrane protein intracellular domain proteolysis (RIP) and protein processing;
  ATF6-mediated UPR; positive regulation of cholesterol biosynthesis (via SREBP) replaces the
  generic "regulation of" TAS row (mouse Mbtps1 already carries GO:0045542).
- `proteolysis` rows -> MODIFY to GO:0031293 + GO:0016485 (pleiotropic, both supported).
- `protein maturation` (GNPTAB) -> MODIFY to GO:0016485 protein processing.
- protein binding (FAM20C; ETFA/ETFB) -> REMOVE (uninformative).
- mitotic G2 DNA damage checkpoint signaling (IEA from mouse) -> MARK_AS_OVER_ANNOTATED: downstream
  of CREB3L1 activation, not an S1P activity.
- NEW: protein autoprocessing (GO:0016540) for propeptide autocatalysis.
- Comparator check for GO:0032933 SREBP signaling pathway: carried in human/mouse/rat by SCAP,
  INSIG1/2, SREBF1/2, ERLIN1/2 but by no S1P/S2P protease (QuickGO query 2026-10-18); not proposed
  as NEW, raised as a suggested question instead.
