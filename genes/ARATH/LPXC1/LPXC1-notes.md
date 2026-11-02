# LPXC1 (At1g24793, F4IAT8) notes, with shared notes for the LPXC1-5 cluster

Deep research (falcon) fails in this environment (authentication), so no
`-deep-research-*.md` file exists. The literature summary below was compiled manually
from cached publications, the PMC full text of Li et al. 2011, and PubMed searches.
LPXC2-5 notes files point here.

## The cluster

- Five LpxC genes sit in tandem in a 68-kb region of chromosome 1
  [PMID:21709257 "There are five AtLpxC orthologs located in a 68-kb region on chromosome one"],
  probably from duplication
  [PMID:21709257 "They have very similar nucleotide sequences, suggesting possible gene duplications from a common ancestor."].
- Locus-to-name mapping (Li et al. 2011 Table 1, read from PMC3136250; the table is not
  in the cached markdown): AtLpxC1 = AT1G24793 (variants AtLpxC1.1, 326 aa; AtLpxC1.2,
  266 aa), AtLpxC2 = AT1G24880, AtLpxC3 = AT1G25054, AtLpxC4 = AT1G25145, AtLpxC5 =
  AT1G25210. UniProt uses the same numbering (LPXC1 F4IAT8 ... LPXC5 F4IAW1).
- EST/cDNA support exists for the family
  [PMID:21709257 "Expressed sequence tag (EST) and deduced cDNA databases indicate these AtLpxC genes generate at least eight different but related mRNA transcripts"].
  Two variants lack the catalytic C-terminus
  [PMID:21709257 "These residues are truncated in two of the eight AtLpxC proteins, specifically in AtLpxC1.2 and AtLpxC5.2 ( Table 1 ), suggesting that these two proteins are not catalytically active."].
- Bioinformatics (file:ARATH/LPXC1/LPXC1-bioinformatics/RESULTS.md): the five canonical
  UniProt sequences (326 aa) are 100% identical; each is 36.2% identical to E. coli LpxC
  and retains the Zn(2+) ligands (H109, H281, D285 = E. coli H79, H238, D242), D289 (D246)
  and the proton donor H313 (H265). F4IAT8 isoform 2 (266 aa = AtLpxC1.2) loses all
  C-terminal catalytic residues. Locus-level expression cannot be resolved because
  reads from identical coding sequences multi-map.
- UniProt gene-model notes: each locus was split from a larger erroneous model
  (e.g. At1g24793/At1g24800; At1g24880/At1g24881; At1g25054/At1g25055;
  At1g25145/At1g25150; At1g25210/At1g25211).

## Which locus was studied (Li et al. 2011, PMID:21709257, full text)

- Gene function was tested only collectively, by RNAi against all five genes
  [PMID:21709257 "To suppress transcription of the five closely linked AtLpxC genes ( Fig. 2 and Table 1 ), independent AtLpxC-RNAi transgenic lines were generated"],
  monitored with primers from shared sequence
  [PMID:21709257 "RT-PCR using primers designed from regions of sequence identity"].
- Lipid X (2,3-diacylglucosamine 1-phosphate, the product two steps downstream of LpxC)
  fell to 37%
  [PMID:21709257 "The lipid X level decreased in AtLpxC-RNAi transgenic plants to approximately 37% of the amount present in the Col-0 wild type"],
  and RNAi suppressed lipid X accumulation in atlpxb-1
  [PMID:21709257 "accumulation of lipid X in the atlpxb-1 mutant was greatly attenuated by suppressing the transcription of the AtLpxC genes, consistent with the proposal that LpxC functions before LpxB"].
- The authors explicitly do not know which copy is functional
  [PMID:21709257 "However, it remains unclear which of the closely related AtLpxC enzymes is functional in vivo"].
- The only locus-specific construct is the GFP fusion of AtLpxC1.1 (AT1G24793), which is
  mitochondrial
  [PMID:21709257 "The GFP fluorescence from the full-length GFP fusions of AtLpxA and AtLpxC1.1 localized in mitochondria"];
  not chloroplastic
  [PMID:21709257 "In mesophyll cells, GFP signals were shown as 1 μm dots, but were not colocalized with chloroplasts (data not shown)."].
  Because the AtLpxC1.1 protein is identical to the canonical products of the other four
  loci, the localisation result applies to the protein each locus encodes; the 35S
  promoter construct says nothing about native expression of a given locus.
- No in vitro deacetylase assay or E. coli lpxC complementation of an Arabidopsis LpxC
  has been reported (contrast AtLpxA, PMID:22545860). The MF is inferred from orthology
  with full active-site conservation plus the in planta lipid X decrease.
- RNAi plants have no visible phenotype
  [PMID:21709257 "Null mutants of AtLpxA , AtLpxD2 , AtLpxB , AtLpxK , and AtKdtA , as well as AtLpxC-RNAi knock-down plants, show no obvious phenotypic differences compared to wild type under laboratory conditions"].
- Pathway conclusion
  [PMID:21709257 "our work demonstrates that plants synthesize lipid A precursors using the same enzymatic pathway present in E. coli"];
  end product unknown
  [PMID:21709257 "The end products of the plant lipid A pathway remain unknown."].

## Other evidence

- Carrie et al. 2015 (PMID:25732537) mitochondrial N-terminomics: UniProt cites it for a
  1-21 transit peptide (ECO:0000269) and mitochondrial location (ECO:0000305) on all five
  entries. The LpxC peptide is in supplementary data, not the cached text; an N-terminal
  peptide from the mature protein cannot be assigned to one locus since sequences are
  identical. Supports mitochondrial import of the shared product.

## GOA observations and decisions (applied identically to all five)

- `GO:2001289 lipid X metabolic process` is obsolete (QuickGO: isObsolete true, no
  replacement). The IMP rows from Li et al. capture the lipid X decrease after LpxC RNAi;
  MODIFY to `GO:0009245 lipid A biosynthetic process` (verified current in OLS/QuickGO).
  No lipid IVA-specific GO process term exists (OLS search).
- `GO:0103117` MF: ACCEPT (IBA/IEA/ISS/IMP). The IMP is family-level RNAi; it is
  consistent with the orthology inference and is not attributable to one locus.
- `GO:0005739 mitochondrion`: ACCEPT. IDA rows rest on AtLpxC1.1 GFP (identical protein).
- `GO:0009507 chloroplast` (AtSubP ISM): REMOVE; GFP was not chloroplastic and all Lpx
  enzymes tested were mitochondrial. Lipid X is found in chloroplast fractions, but that
  is the lipid, not the enzyme.
- `GO:0009245 lipid A biosynthetic process` (IBA/IEA): ACCEPT; refutes the Wei et al.
  2020 RAR flag (PMID:32470107; projects/RAR_MISANNOTATION.md).
- No NEW annotations: every experimentally supported term is already present in GOA for
  each locus (any evidence code); the experimental evidence is recorded in those rows.
- LPXC3 has no IBA rows in GOA (absent from the PAINT WITH/FROM list) and LPXC2 has no
  ISM chloroplast row; the gene product is identical, so the absence is a pipeline
  artefact, not biology.

## Searches

- PubMed "LpxC AND (Arabidopsis OR plant OR mitochondria)" (26 hits, bacterial LpxC
  inhibitor papers dominate) and "(lipid A OR lipid X OR UDP-3-O-acyl-N-acetylglucosamine
  deacetylase) AND Arabidopsis[Title/Abstract]" (20 hits; besides PMID:21709257,
  PMID:20124190, PMID:22545860, PMID:28202596 these are LPS perception papers, e.g.
  LORE, PMID:25729922). No later study of an individual AtLpxC locus was found.
