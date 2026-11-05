# wbpD (PA3156, G3XD01) notes

No deep-research provider was available; literature research done manually (PubMed MCP + cached
publications).

## Identity

- UniProt G3XD01 (Swiss-Prot), 191 aa, *P. aeruginosa* PAO1, locus PA3156, B-band (O-specific
  antigen, OSA) cluster of serotype O5. Hexapeptide-repeat (left-handed beta-helix, LbetaH)
  acyltransferase superfamily; PANTHER PTHR43300 ("ACETYLTRANSFERASE"), subfamily SF4.
- EC 2.3.1.201, UDP-2-acetamido-3-amino-2,3-dideoxy-alpha-D-glucuronate N-acetyltransferase
  (RHEA:33587).

## Function

- Step 4 of the five-enzyme Wbp pathway UDP-GlcNAc -> (WbpA, C6 dehydrogenase) UDP-GlcNAcA ->
  (WbpB/WbpE, C3 dehydrogenase/aminotransferase pair) UDP-GlcNAc3NA -> (WbpD) UDP-GlcNAc3NAcA ->
  (WbpI, C2 epimerase) UDP-ManNAc3NAcA, the donor for the D-ManNAc3NAcA residue of the B-band
  O-antigen repeat [PMID:19348502 "It is then hypothesized that the C3-dehydrogenase WbpB,
  aminotransferase WbpE, and acetyltransferase WbpD sequentially convert UDP-GlcNAcA into
  UDP-2,3-diacetamido-2,3-dideoxy-d-glucuronic acid (UDP-GlcNAc(3NAc)A)"].
- 2005 genetics: knockout lacks long-chain B-band O antigen and semi-rough LPS; His6-WbpD is
  trimeric and binds acetyl-CoA; no substrate available so no activity assay; K136A partially
  complements [PMID:16102001 "As a substrate for studying the enzymatic activity of WbpD is
  unavailable at present"; "His6-WbpD has trimeric organization"].
- 2009 biochemistry (two groups): MS detection of the WbpD product in coupled WbpB/WbpE/WbpD
  reactions and NMR structure of UDP-GlcNAc3NAcA [PMID:19282284 "in reactions involving WbpB,
  WbpE, and WbpD, an ion consistent with the expected product of WbpD (UDP-d-GlcNAc3NAcA) was
  identified"]; kinetics, Km 107 uM, kcat 2.9 x 10^3 min-1 [PMID:19348502 "we confirm that WbpD
  catalyzes the acetylation of UDP-GlcNAc(3NH(2))A to give UDP-GlcNAc(3NAc)A"].
- Bordetella pertussis WlbB is a functional homolog (cross-complements P. aeruginosa wbpD)
  [PMID:18621892 "the genes that encode the putative oxidase, transaminase, N-acetyltransferase,
  and epimerase enzymes in B. pertussis are functional homologs of those in P. aeruginosa"].

## Is WbpD in "UDP-glucuronate biosynthetic process"?

No. GO:0006065 is the formation of UDP-glucuronate (UDP-GlcA, made by UDP-glucose
6-dehydrogenase). WbpD neither makes nor consumes UDP-GlcA: its substrate is the
2-acetamido-3-amino-2,3-dideoxy uronic acid UDP-GlcNAc3NA and its product UDP-GlcNAc3NAcA. Even the
first enzyme of the pathway (WbpA) oxidises UDP-GlcNAc to UDP-GlcNAcA, not UDP-Glc to UDP-GlcA.
The term was probably chosen because the products are "glucuronic acid" derivatives. The correct
genus is GO:0009226 nucleotide-sugar biosynthetic process (no GO term exists for
UDP-ManNAc3NAcA biosynthesis). Moreover the cited paper (PMID:16102001) had no substrate and
could not have shown any nucleotide-sugar biosynthesis directly.

No GO MF term exists for EC 2.3.1.201 (OLS search). GO:0008080 N-acetyltransferase activity is
the most specific existing term.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001917401 | GO:0016407 acetyltransferase activity | 1 (sole seed) | 67 (28 taxa) | GO:0016407 acetyltransferase activity, EXP, PMID:19282284 | SOUND | 19282284 detects the WbpD N-acetylated product by MS and NMR; 19348502 gives kinetics. Acetyltransferase is an appropriately broad node term for a hexapeptide-repeat clade whose members use acetyl-CoA. Caveat: PTHR43300:SF4 is named for LpxA-type acyl-ACP O-acyltransferases; if the node spans true LpxA orthologs, "acyltransferase activity" would be safer. Node membership not inspected. |
| PTN001292385 | GO:0006065 UDP-glucuronate biosynthetic process | 1 (sole seed) | 8 (8 taxa) | GO:0006065 UDP-glucuronate biosynthetic process, EXP, PMID:16102001 | WRONG | WbpD acetylates UDP-GlcNAc3NA in UDP-ManNAc3NAcA synthesis; UDP-glucuronate is neither substrate nor product of the pathway, and 16102001 could not assay activity at all (no substrate). Replace with GO:0009226 nucleotide-sugar biosynthetic process at the node (and on the seed). The 8 leaf IBAs inherit a false process. |
