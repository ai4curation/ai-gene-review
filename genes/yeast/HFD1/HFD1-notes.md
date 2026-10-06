# HFD1 (YMR110C, UniProt Q04458) – review notes

## Identity and family
- Fatty aldehyde dehydrogenase HFD1; EC 1.2.1.3 and EC 1.2.1.64; ALDH superfamily, closest to the human ALDH3 family [UniProt:Q04458 "Belongs to the aldehyde dehydrogenase family"].
- PANTHER PTHR43570 (ALDEHYDE DEHYDROGENASE), subfamily SF16 [UniProt:Q04458].
- C-terminal single-pass membrane anchor (predicted) [UniProt:Q04458 "Single-pass membrane protein"].

## Activities
- Fatty aldehyde (hexadecenal) oxidation in the sphingosine-1-phosphate (S1P) degradation pathway: [PMID:22633490 "are responsible for conversion of the S1P degradation product hexadecenal to hexadecenoic acid"]. NAD+-dependent; UniProt lists EC 1.2.1.3 and the hexadecanal/hexadecanoate RHEA:33739 reaction with ECO:0000269 from this paper.
- 4-hydroxybenzaldehyde (4-HBz) -> 4-hydroxybenzoate (4-HB), last step of the tyrosine-to-4-HB route that supplies the CoQ ring precursor:
  - [PMID:27693056 "the oxidation of 4-hydroxybenzaldehyde to 4-HB by Hfd1"]; [PMID:27693056 "Inactivation of the HFD1 gene in yeast resulted in Q deficiency"]; rescued by human ALDH3A1.
  - Purified enzyme: [PMID:27669165 "WT Hfd1p catalyzes NAD+-dependent dehydrogenation of 4-HBz"]; it also acts on hexadecanal [PMID:27669165 "we observed Hfd1p activity in vitro with hexadecanal, similar to that observed with 4-HBz"].
  - Genetics: [PMID:33862086 "Thus far, HFD1 is the only known gene required for converting 4-HPP to 4-HB"]; [PMID:33862086 "catalyzed by the broad-specificity aldehyde dehydrogenase Hfd1"].
- Fatty aldehyde turnover limits heterologous alkane production [PMID:25545362 "elimination of the hexadecenal dehydrogenase Hfd1 and expression of a redox system are essential for alkane biosynthesis in yeast"].

## Location
- Mitochondrial outer membrane (proteomics of purified OM) [PMID:16407407 "including the yeast homologue (Hfd1/Ymr110c) of the human protein causing Sjögren-Larsson syndrome"].
- Lipid droplets [PMID:24868093 "Hfd1-GFP exhibited predominantly LD localization"].
- Endosome/punctate in the GFP collection (PMID:14562095), ER in the SWAT N-terminal GFP library (PMID:26928762; N-terminal tag may perturb the C-terminal anchor).
- Not reported in the mitochondrial inner membrane: the Reactome TAS location (R-SCE-9856799) is unsupported.
- YeastPathways PWY3O-1109 (p-hydroxybenzoate biosynthesis) gives the default "cytosol"; the catalytic domain is membrane-anchored on the cytosolic face of the outer membrane / LD, so "cytosol" is imprecise.

## YeastPathways / module
- HFD1 is not a gene in the YeastPathways summary reactions for PWY3O-1109 (the frame lists the coumarate route with no genes), but GOA carries an SGD RCA cytosol row from SGD_PWY:PWY3O-1109.
- Module ubiquinone_biosynthesis uses HFD1 as exemplar for the 4-HBz -> 4-HB step, GO:0018484. Agrees with literature. Note physiological cofactor is NAD+ in vitro (PMID:27669165); module lists NAD(P)+.

## GO term issues
- GO:0047770 carboxylate reductase activity (IMP, PMID:22633490): GO:0047770 is EC 1.2.99.6 with an unspecified acceptor; HFD1 is NAD+-dependent, so the correct term is GO:0050061 long-chain fatty aldehyde dehydrogenase (NAD+) activity (or GO:0004029). MODIFY.
- GO:0005743 mitochondrial inner membrane (Reactome TAS): MODIFY to outer membrane.
