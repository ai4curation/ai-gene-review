# CLPP (human, Q16740) review notes

## Session 2026-10-09

Chosen from `projects/MITOTOL.md` (Chen et al. 2026, PMID:42822426): human CLPP is the human half
of the ClpXP/ClpYQ non-homologous protease pair.

### Deep research

`just deep-research-falcon human CLPP --fallback perplexity-lite` was launched at the start of the
session (timeout 1500 s). See the end of this file for its outcome. The review below was built from
my own literature research (PubMed MCP plus cached publications), not from a deep-research file.

### Identity and structure

- Peptidase S14 (ClpP) family, MEROPS S14.003; PANTHER PTHR10381:SF11. Transit peptide 1-56;
  nucleophile Ser153, His178 (UniProt). S153A/C abolishes protease activity [PMID:11923310 via UniProt].
- Two heptameric rings with 7-fold symmetry, matrix-localized, tending to associate with the inner
  membrane [PMID:10525407 "the mammalian homologue of ClpP is located in the mitochondrial matrix"].
- Crystal structure: active sites sequestered in the chamber; N-terminal peptides line the axial
  channel and are needed for activity [PMID:15522782 "Mutation or deletion of these residues causes a
  drastic decrease in ClpX-mediated protein and peptide degradation."]. The 28-residue C-terminal
  extension is mammal-specific.
- Alone, human CLPP is a heptamer with almost no activity; ATP-bound CLPX converts it to an active
  tetradecamer [PMID:16115876 "Heptameric hClpP has no proteolytic activity and very low peptidase
  activity."; "hClpX must exert an allosteric effect on hClpP to promote a conformation that stabilizes
  the tetradecamer"].
- Reconstituted human ClpXP is an ATP-dependent protease; substrate choice is set by CLPX
  [PMID:11923310 "Our results establish that human ClpX and ClpP constitute a bone fide ATP-dependent
  protease"].

### Substrates and roles

- Mitoribosome assembly via ERAL1 (mouse): Clpp loss causes ERAL1 to stay bound to the 28S subunit,
  impairing 55S assembly and translation; wild-type but not S149A (mouse numbering) CLPP rescues
  [PMID:27797820 "We further show that the defect in mitoribosomal assembly is a consequence of the
  accumulation of ERAL1, a putative 12S rRNA chaperone, and novel ClpXP substrate."].
- OXPHOS proteins: BioID interactors include respiratory chain subunits; SDHA proposed substrate in
  AML [PMID:26058080 "Thus, these results support SDHA as a functionally important substrate for ClpP
  and a role for ClpP in maintaining oxidative phosphorylation in a subset of AML cells."].
- Heme-bound ALAS1 (via Reactome R-HSA-9838289, citing Kubota 2016, Nomura 2021). The ALAS activation
  role belongs to CLPX, not CLPP (see `genes/human/CLPX`).
- PINK1: ClpXP was one of four proteases found in an RNAi screen for PINK1 turnover; ClpXP knockdown
  did not stabilize PINK1 at the surface [PMID:22354088]. Peripheral.

### UPRmt

- C. elegans clpp-1 is needed for UPRmt signalling [PMID:17925224].
- In mice, CLPP is not required for UPRmt [PMID:27154400 "our results clearly show that mammalian CLPP
  is neither required for, nor it regulates the UPR(mt) in mammals"]. Loss of CLPP even improved
  DARS2-deficient cardiomyopathy. Reactome still asserts UPRmt involvement by inference from worm and
  rat; I did not add GO:0034514.

### Disease

- Perrault syndrome 3: homozygous T145P, C147S, splice variants [PMID:23541340]; Y229D [PMID:25956234].
- Clpp-/- mice: infertility, hearing loss, growth retardation, CLPX and mtDNA accumulation
  [PMID:23851121 "Thus, murine Clpp deletion represents a faithful Perrault model."].

### Pharmacology

- Imipridones (ONC201, ONC212) bind CLPP non-covalently in hydrophobic pockets between subunits and
  hyperactivate it, degrading respiratory chain proteins and killing cancer cells [PMID:31056398 "We
  identified imipridones as potent activators of ClpP."]. Resistance mutation D190A.
- Independent target identification of CLPP for ONC201/TR compounds by affinity chromatography
  [PMID:31021596].
- Not annotation material for normal function (drug response), but confirms the docking-pocket
  activation mechanism.

### Evolutionary context (PMID:42822426)

- LECA mitochondria likely had both ClpXP and ClpYQ (HslUV), lost in complementary patterns; humans
  keep ClpP, several pathogens keep ClpQ (an essential candidate target in P. knowlesi). This is
  comparative/computational and says nothing about CLPP's molecular function; used at LOW relevance.
  "Absent in humans" means the ClpYQ family is absent, not ATP-dependent matrix proteolysis.

### Curation decisions (summary)

- Core MF: serine-type endopeptidase activity (GO:0004252); ATPase binding (GO:0051117) for CLPX docking.
- Core BP: mitochondrial protein catabolic process (GO:0035694); protein quality control (IBA).
- Core CC: mitochondrial matrix; mitochondrial endopeptidase Clp complex (GO:0009841).
- GO:0004176 ATP-dependent peptidase activity accepted (EC 3.4.21.92 is the ClpP enzyme), with a
  question on contributes_to (CLPX supplies ATP hydrolysis).
- GO:0009368 IDA/IPI -> MODIFY to GO:0009841; IBA kept at family level.
- protein binding: CLPX IPIs -> MODIFY to ATPase binding; 22 HTP Y2H pairs (HuRI, neurodegeneration
  interactome) -> REMOVE as uninformative.
- GO:0008233 peptidase activity TAS (cloning paper) -> MODIFY to GO:0004252.
- membrane protein proteolysis (PINK1) and identical protein binding -> KEEP_AS_NON_CORE.
- No NEW annotations. Mitoribosome assembly raised as a question (mouse evidence; regulatory vs
  participatory is unclear).
- No GO-CAM model in `gocams/index.tsv` contains CLPP.

### Deep research outcome

The `just deep-research-falcon` wrapper reported "Provider falcon timed out after 600s", then the
perplexity-lite fallback failed ("Provider 'perplexity' not available"), and the recipe exited 1.
However, the orphaned falcon client kept running and wrote `CLPP-deep-research-falcon.md` itself at
16:02 (duration 1578 s). That file is genuine tool output, not written by me. I cross-checked it
after the main review and added three of its sources after verifying them against cached text:

- Complex I N-module salvage [PMID:32242014 "Here, we demonstrate that mitochondrial ClpXP protease is
  required for the turnover of the core part of the N-module of CI, which occurs at a higher rate and
  largely independently of the rest of the complex."].
- Perrault variant biochemistry [PMID:30150665 "The Y229D mutant not only inhibited CLPP-peptidase
  activity, but unexpectedly also prevented CLPX-docking"]; T145P disrupts oligomerization.
- Phosphoserine degrons recognized by CLPX [PMID:39879245 "We demonstrated that phosphorylated serine
  (pSer) targets substrates to ClpX and facilitates their degradation by ClpXP in biochemical assays."].

Falcon also cites a 2026 Nat Commun study (Aljghami et al.; CHCHD2, ALAS1, TFAM as human ClpXP
substrates, PDIP38 adaptor). I did not find or cache its PMID and did not cite it in the review.
Falcon's report that CLPP knockdown blunts ONC201 responses and that dordaviprone received FDA
accelerated approval (Aug 2025) is drug-response context only and was not used for annotation.
