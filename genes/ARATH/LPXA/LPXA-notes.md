# LPXA (At4g29540, Q9SU91) notes

Deep research via the falcon provider fails in this environment (authentication), so the
literature summary below was compiled manually from cached publications (both key papers
have full text cached) and PubMed searches. No `-deep-research-*.md` file was produced.

## Identity

- Swiss-Prot Q9SU91, "Probable acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine
  O-acyltransferase, mitochondrial" (AtLpxA), 336 aa precursor with a predicted
  N-terminal mitochondrial transit peptide (1-32, ECO:0000255). Transferase hexapeptide
  repeat family, LpxA subfamily; InterPro IPR010137 Lipid_A_LpxA; PANTHER PTHR43480:SF1;
  PDB 3T57 (residues 33-336).
- Two splice isoforms differing by two residues in the C-terminal region
  [PMID:21709257 "The AtLpxA gene ( Table 1 ) encodes two mRNA splice variants, one of which directs the synthesis of a protein with two additional amino acid residues inserted in the C-terminal region"].
- 38% identity to E. coli LpxA with all active-site residues conserved
  [PMID:21709257 "they share 38 and 37% sequence identity with E. coli LpxA, respectively, ( Table 1 ), with conservation of all active site residues"].

## Enzyme activity (direct, in vitro) - Joo et al. 2012 (full text)

- Purified AtLpxA catalyses the LpxA reaction (EC 2.3.1.129)
  [PMID:22545860 "In vitro assays show AtLpxA transfers a 3-hydroxymyristoyl group from 3-hydroxymyristoyl-ACP to the 3-OH of UDP-GlcNAc"],
  at about one tenth of EcLpxA specific activity (5.1 nmol/min/mg), similar to other
  heterologously expressed LpxA orthologs.
- Homotrimer [PMID:22545860 "Like EcLpxA, AtLpxA is a homotrimer in aqueous solution"];
  2.1 A crystal structure with the left-handed parallel beta-helix and conserved
  hydrocarbon-ruler glycine (Gly228, = EcLpxA Gly173), consistent with preference for
  R-3-hydroxymyristoyl-ACP.
- Complements a chromosomal E. coli lpxA deletion (not the ts SM101 allele) and supports
  wild-type lipid A synthesis
  [PMID:22545860 "AtLpxA was able to functionally replace EcLpxA by supporting the biosynthesis of the expected lipid A anchor of LPS"].
- Conclusion [PMID:22545860 "we have firmly established that the AtLpxA is a functional LpxA through in vitro and in vivo analyses of its biochemical activity"].

## In planta - Li et al. 2011 PNAS (full text)

- atlpxa-1 (Ws background) null mutant has reduced lipid X
  [PMID:21709257 "The level of lipid X in the atlpxa-1 insertion mutant was approximately 21% of its matched wild-type control"];
  residual lipid X suggests a second UDP-GlcNAc acylation route, possibly AtLpxD1
  [PMID:21709257 "This result implies that plants may have a second pathway for the acylation of UDP-GlcNAc not present in bacteria."].
- [PMID:21709257 "the genes encoding AtLpxA, AtLpxC, and AtLpxD2 are required for the efficient production of lipid X"].
- No visible phenotype [PMID:21709257 "Null mutants of AtLpxA , AtLpxD2 , AtLpxB , AtLpxK , and AtKdtA , as well as AtLpxC-RNAi knock-down plants, show no obvious phenotypic differences compared to wild type under laboratory conditions"].
- Localization: full-length AtLpxA-GFP colocalises with MitoTracker in root cells
  [PMID:21709257 "The GFP fluorescence from the full-length GFP fusions of AtLpxA and AtLpxC1.1 localized in mitochondria"];
  in leaves the punctate signal was not chloroplastic
  [PMID:21709257 "In mesophyll cells, GFP signals were shown as 1 μm dots, but were not colocalized with chloroplasts"].
  This argues against the AtSubP `chloroplast` prediction.
- Pathway end product unknown [PMID:21709257 "The end products of the plant lipid A pathway remain unknown."].

## GO term checks

- GO:2001289 `lipid X metabolic process` is obsolete (QuickGO 2026-10: "made in error and
  is an unnecessary grouping term"; no replacement/consider). OLS still showed it as
  non-obsolete, so QuickGO was used. The informative replacement for LpxA is
  GO:0009245 lipid A biosynthetic process (verified, not obsolete): LpxA catalyses its
  first committed acyl-transfer step, so the gene does the work of the process.
- GO:0008780 is the exact MF for EC 2.3.1.129.

## Wei et al. 2020 RAR flag (PMID:32470107)

Plant GO:0009245 annotations were flagged as misannotations. For LpxA this is refuted
by direct in vitro activity, E. coli complementation restoring lipid A, and reduced
lipid X in atlpxa-1. In current GOA LPXA carries no lipid A biosynthetic process row at
all (only the obsolete lipid X term); this review proposes it via MODIFY of the
lipid X rows and as a NEW experimental (IDA) row.

## HDA mitochondrion (PMID:21908688)

Narsai et al. 2011 is a germination transcriptome paper whose abstract reports GFP
confirmation of organellar localisation for 65 proteins; the abstract does not name
At4g29540. Full text not cached; the HDA is consistent with Li et al. GFP data and is
accepted deferring to the curator.

## Searches

- PubMed "(LpxA OR lipid A OR lipid X) AND (Arabidopsis OR plant) AND (mitochondria OR
  acyltransferase)" -> 18 hits; plant-relevant: 21709257, 22545860, 20124190 (KdtA),
  21896887, 28202596. The rest are rhizobial/cyanobacterial lipid A papers. No newer
  AtLpxA-specific study found.
