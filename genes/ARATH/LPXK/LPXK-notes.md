# LPXK (At3g20480, Q8LEA0) notes

Deep research could not be run in this environment (provider auth failure); notes are from the cached
full text of Li et al. 2011 (PMID:21709257, PMC3136250), the UniProt record and PubMed searches.

## Identity
- Single-copy Arabidopsis ortholog of E. coli LpxK (tetraacyldisaccharide 4'-kinase, EC 2.7.1.130;
  Pfam PF02606, InterPro IPR003758, PANTHER PTHR42724:SF1), 26% identity to E. coli LpxK
  [PMID:21709257 "Single copy genes encoding AtLpxB (AT2G04560), AtLpxK (AT3G20480) and AtKdtA
  (AT5G03770) ( Table 1 ) were also found, with 31, 26, and 34% sequence identity to the corresponding
  E. coli proteins, respectively"].
- UniProt: predicted mitochondrial transit peptide 1..32; "Belongs to the LpxK family"; the P-loop
  ATP-binding motif of LpxK is the basis of the ATP binding IEA.

## Genetics and lipid chemistry (Li et al. 2011)
- Alleles atlpxk-1 (SALK_063783C), atlpxk-2 (SALK_100275C), atlpxk-3 (SALK_145083), Col-0; null mutants
  viable, no visible phenotype.
- Substrate accumulation: the LpxK substrate disaccharide 1-phosphate (DS-1-P) accumulates in atlpxk-1
  (and in atkdta-1) but is undetectable in wild type [PMID:21709257 "The disaccharide 1-phosphate was not
  seen in wild-type Arabidopsis , but accumulates in the atlpxk-1 and the atkdta-1 mutants"].
- Lipid X modestly up [PMID:21709257 "In the atlpxk-1 and atkdta-1 mutants, lipid X levels were 2.6- and
  2.2-fold higher than in the Col-0 wild type, respectively"].
- The LpxK product lipid IVA is detected only in kdta mutants, i.e. it is made in lpxk+ plants and
  consumed by KdtA [PMID:21709257 "Lipid IV A ( Fig. 1 ) was detected only in the atkdta-1 mutant"].
- Independent alleles agree [PMID:21709257 "The independently isolated atlpxb-2 , atlpxk-2 , and atlpxk-3
  mutants showed similar lipid accumulation patterns as the atlpxb-1 and atlpxk-1 mutants."].
- No in vitro kinase assay or complementation reported for AtLpxK.

## Localization
- 5'-terminal GFP fusion mitochondrial; full-length fusion too dim [PMID:21709257 "However, 5′-terminal
  fusions of AtLpxD1, AtLpxD2, AtLpxB, and AtLpxK to GFP showed the same mitochondrial pattern as
  full-length AtLpxA and AtLpxC"]. Caveat: the 5' fusion shows the targeting signal is mitochondrial,
  not where the mature full-length enzyme sits within mitochondria.

## Curation decisions
- GO:2001289 lipid X metabolic process is obsolete (QuickGO confirms; no replacement). LPXK does not
  act on lipid X; the IMP (lipid X rise) is an indirect pathway effect. MODIFY to GO:0009245 lipid A
  biosynthetic process, which is also supported directly by DS-1-P accumulation.
- No NEW rows: all supported terms are already in GOA (kinase activity IMP, mitochondrion IDA, lipid A
  biosynthetic process IEA); experimental evidence placed in those rows.
- RAR (PMID:32470107) flagged the plant lipid A family of annotations; refuted for this pathway.
