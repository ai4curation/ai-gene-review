# PA5458 PAINT node composition

Script: `paint_node_leaves.py` (run as
`python -I paint_node_leaves.py .cache/paint/leaf.gaf.gz .cache/paint/IBD.gaf`);
raw output in `paint_node_leaves_output.txt`. Inputs are the PAINT `IBD.gaf` and
`gene_association.paint_uniprot.gaf.gz` from the PANTHER FTP (current release),
as cached by `projects/PSEUDOCAP/build_iba_seed_worklist.py`.

## IBD rows

- PTN000546841, GO:0009103 lipopolysaccharide biosynthetic process, IBD, sole
  seed UniProtKB:Q9HTB2 (PA5458). A NOT IRD at PTN004595801 (plant, taxon:3988)
  rejects it in one plant subclade.
- PTN000546715, GO:0000271 polysaccharide biosynthetic process, IBD, sole seed
  UniProtKB:Q9HTB2. The same node carries GO:0016020 membrane, seeded by
  WB:WBGene00044617 (C. elegans).

## PTN000546841 (GO:0009103): 31 leaf IBAs in 16 taxa

Leaves in organisms without lipopolysaccharide (Gram-positive bacteria and
mycobacteria): Mycobacterium tuberculosis H37Rv (taxon:83332, 5: Rv0111, Rv1565c,
Rv1254, Rv0517, Rv0228), Streptomyces coelicolor (taxon:100226, 4), Staphylococcus
aureus NCTC 8325 (taxon:93061, 2, including oatA Q2FV54), Listeria monocytogenes
EGD-e (taxon:169963, oatA Q8Y7I6), Streptococcus pneumoniae R6 (taxon:171101,
spr1868), Bacillus subtilis 168 (taxon:224308, yrhL), Bacillus cereus (taxon:226900).
So 15 of the 31 leaves are in organisms that make no LPS.

The remaining leaves are in diderm bacteria: P. aeruginosa PAO1 (4: PA5458,
PA4338, PA5238, PA3157), Bradyrhizobium diazoefficiens (4, including exoZ),
Leptospira interrogans (2), Salmonella Typhimurium LT2 (oafA Q8ZNJ3), Neisseria
meningitidis MC58, Coxiella burnetii, Bacteroides thetaiotaomicron, Xanthomonas
campestris, Fusobacterium nucleatum.

## PTN000546715 (GO:0000271): 113 leaf IBAs in 11 taxa

Caenorhabditis elegans (taxon:6239) 41, C. briggsae (6238) 29, Pristionchus
pacificus (54126) 27, Phytophthora ramorum (164328) 9, Ustilago maydis (237631) 1,
Thalassiosira pseudonana (35128) 1, Ricinus communis (3988) 1, Gloeobacter violaceus
(251221) 1, Rhodopirellula baltica (243090) 1, Bradyrhizobium diazoefficiens (224911)
1, Xanthomonas campestris (190485) 1.

So 109 of the 113 leaf IBAs are in eukaryotes, 97 of them nematode proteins.

## Interpretation

The only seed for both process IBDs is a P. aeruginosa mutant in which the CPA
(D-rhamnan O antigen) is still made but altered. The LPS node spans peptidoglycan
O-acetyltransferases of Gram-positive bacteria (OatA), which cannot take part in
LPS biosynthesis; the polysaccharide node propagates almost entirely to nematode
and oomycete acyltransferase-3 proteins for which no polysaccharide role is
known.
