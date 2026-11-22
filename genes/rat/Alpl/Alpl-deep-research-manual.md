# Alpl (rat, P08289) - manual literature synthesis

No deep-research API was available for this session; this summary was compiled by hand
from the cached publications in `publications/` and the UniProt record
(`Alpl-uniprot.txt`). Each claim carries its provenance.

## Identity

- Rat tissue-nonspecific alkaline phosphatase (TNAP; "bone/liver/kidney" ALP), 524 aa,
  RGD:2100, GeneID 25586, UniProtKB P08289 (PPBT_RAT).
- Cloned from ROS 17/2.8 osteosarcoma cells: "The predicted amino acid sequence spans 524
  residues and includes an N-terminal signal peptide of 17 amino acids, the
  phosphohydrolase active site, a rather hydrophilic backbone with five potential
  N-glycosylation sites, and a short hydrophobic C-terminal sequence."
  [PMID:3422431, abstract]. A single-copy gene expressed in bone, liver and kidney but not
  intestine [PMID:3422431].
- Two alternative promoters give transcripts identical in coding sequence; the upstream
  promoter is used in calvaria/osteoblastic cells and is dexamethasone-inducible
  [PMID:2039500, abstract].
- UniProt: "Belongs to the alkaline phosphatase family"; Zn2+ (x2), Mg2+ and Ca2+
  cofactors and homodimer by similarity to human P05186/P05187; GPI-anchored cell
  membrane protein [Alpl-uniprot.txt].

## Rat-specific biochemistry

- Purified rat osteosarcoma enzyme: "specific activity of 759 units/mg protein at its
  optimal pH (10.5), and a Km of 0.8 mM for p-nitrophenylphosphate"; heat inactivation
  and homoarginine inhibition "characteristic of the bone-liver-kidney AP isoenzyme"
  [PMID:3472490, abstract].
- Membrane-bound TNAP extracted from rat bone marrow cells and reconstituted into
  proteoliposomes hydrolyses ATP and drives amorphous calcium phosphate precipitation;
  "TNAP is an ATP phosphohydrolase bound to cell and MV membranes via a
  glycosylphosphatidylinositol (GPI) anchor" [PMID:32710882, full text].

## Key experimental paper PMID:20048161 (Simão et al. 2010, JBC)

- Read in full. Important caveat: the TNAP used was **human** recombinant TNAP ("The
  2.5-kb human TNAP cDNA was cloned into pCMV-Script vector"), expressed in CHO-K1 cells;
  rat osseous-plate enzyme appears only as a literature comparator in the Discussion.
  It therefore supports the rat annotations by orthology only.
- Findings: in DPPC proteoliposomes at physiological pH, TNAP hydrolysed ATP, ADP, AMP,
  PLP, pNPP and PPi; PLP hydrolysis was exclusive to TNAP-containing proteoliposomes;
  "TNAP appeared more active in AMP formation than NPP1"; PPi hydrolysis by
  TNAP-containing proteoliposomes occurred "with catalytic efficiencies and mild
  cooperativity, effects comparable with those manifested by murine osteoblast-derived MVs".

## Mineralization (rat histology)

- Bisphosphonate-treated rat bone: "Intense TNSALP and ATPase reactions were confirmed
  along the limited portions of osteoblast membranes"; enzymes appear diffusely in
  osteoid and are later integrated into matrix vesicles [PMID:19697513, abstract].
- Acellular cementogenesis in rat molars: cementoblasts show intense TNSALP reaction at
  the onset of cementum mineralization [PMID:17043865, abstract].

## Physiological roles established in mouse/human (orthology)

- Pyrophosphate hydrolysis in matrix vesicles: "We conclude that TNAP is the enzyme that
  hydrolyzes both ATP and PP(i) in the MV compartment." [PMID:19874193].
- Vitamin B6: "Mice lacking tissue non-specific alkaline phosphatase die from seizures
  due to defective metabolism of vitamin B-6." [PMID:7550313].
- Non-redundant with PHOSPHO1: compound ablation "prevents skeletal mineralization"
  [PMID:20684022].
- Futile creatine cycle: mitochondrial TNAP in thermogenic adipocytes hydrolyses
  phosphocreatine [PMID:33981039].
- Phosphocholine / phosphoethanolamine dephosphorylation [PMID:41145834].
- Vascular calcification: "Overexpression of TNAP increased calcification of cultured
  aortas." [PMID:21490328] - i.e. TNAP promotes, not inhibits, ectopic mineralization.

## Expression-response papers (rat)

- LPS: TNAP is the main AP isozyme in bronchoalveolar fluid of LPS-instilled rats, but
  "LPS instillation induced IAP-I mRNA, but not IAP-II mRNA or TNAP mRNA" [PMID:11810315].
- Insulin/diabetes: bone ALP activity falls in STZ-diabetic rats and is restored by
  insulin [PMID:20818503].
- CSF-1 normalises ALP mRNA in toothless osteopetrotic rats, interpreted as secondary to
  correction of the osteopetrotic condition [PMID:7669437].
- Dexamethasone induces ALP mRNA/activity in ROS17/2.8 cells [PMID:2039500].
