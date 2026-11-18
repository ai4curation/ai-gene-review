# galT (P09148, GAL7_ECOLI) notes

## Deep research status

- 2026-11-12: no deep-research provider key was available in this session, so no
  `galT-deep-research-*.md` file exists. This review is based on the UniProt record,
  the cached publications behind the GOA rows, and additional abstracts fetched with
  `just fetch-pmid` (PMID:8794735, PMID:7669762, PMID:9063869, PMID:3022232).

## Identity

- E. coli K-12 galT (b0758, JW0741; synonym galB), second gene of galETKM.
  Galactose-1-phosphate uridylyltransferase, EC 2.7.7.12, 348 aa, homodimer.
- Type 1 GalT family (HIT superfamily) [file:ECOLI/galT/galT-uniprot.txt "Belongs to the
  galactose-1-phosphate uridylyltransferase type 1 family."]; InterPro IPR001937,
  IPR005849, IPR005850; NCBIfam TIGR00209; PANTHER PTHR11943.

## Molecular function and mechanism

- Double displacement via a uridylyl-enzyme [PMID:321007 "The hydrolytic properties of
  the uridylyl-enzyme show that the uridylyl moiety is bonded to the protein through a
  phosphoramidate linkage."]. Note: the first sentence of the PMID:321007 abstract
  contains a substrate typo ("UDP-galactose and galactose-1-P with UDP-galactose").
- His166 Nepsilon2 is the nucleophile [PMID:8794735 "Well-defined electron density for the
  nucleotidylated imidazole supports the existence of a covalent bond between N epsilon 2
  of the nucleophile and the alpha-phosphorus of UMP."]; Gln168 contacts the phosphoryl
  oxygens.
- Ser161 essential, Cys160 not [PMID:10820011 "The results lead to the conclusion that
  the conserved Cys 160 does not play a critical role in catalysis."].
- Active site formed by both subunits [PMID:9063869 "the active site of the
  uridylyltransferase is formed by amino acid residues contributed from both subunits in
  the dimer"].
- Kinetics (UniProt, PMID:10820011): KM 0.2 mM UDP-Glc, 0.303 mM Gal-1-P, Vmax 180 U/mg.

## Metals

- Zn and Fe [PMID:7727423 "contains approximately 1.2 mol of tightly bound zinc/mol of
  subunits as well as variable amounts of iron, up to 0.7 mol/mol of subunits"].
- Zinc essential, iron not [PMID:10529216 "It is concluded that the presence of zinc is
  essential for maintaining GalT function, whereas the presence of iron is not
  essential."]. Zinc ligands Cys52, Cys55, His115, His164; iron ligands His281, Glu182,
  His296, His298 at the subunit interface (PMID:7669762, PMID:10529216).
- UniProt's MISCELLANEOUS note on iron cites PMID:10820011; the supporting abstract is
  PMID:10529216 (minor citation slip, not filed as a defect).

## Process and location

- Leloir pathway [PMID:7669762 "This enzyme participates in the Leloir pathway of
  galactose metabolism"]; gal cistrons (PMID:13914787).
- Cytosol (PMID:18304323 cytosolic proteome; GalT not named in cached main text).

## Curation decisions

- 15 GOA rows: ACCEPT 9, MODIFY 2, KEEP_AS_NON_CORE 3, REMOVE 1.
- REMOVE galactokinase activity IMP (PMID:18263746, CACAO): the paper uses a DeltagalK
  strain [PMID:18263746 "An Escherichia coli galactose kinase gene knockout (DeltagalK)
  strain"]; GalT is not a kinase. Source defect WRONG_GENE_PRODUCT -> galK P0A6T3.
- cytoplasm IBA -> MODIFY to cytosol (propagation_review: granularity).
- galactose metabolic process IEA -> MODIFY to GO:0033499.
- zinc ion binding (IDA, IEA) and ferrous iron binding (IDA): KEEP_AS_NON_CORE
  (structural metals). "Ferrous" oxidation state not stated in the cached abstract;
  deferred to the curator.
- No NEW rows proposed (homodimer is well supported structurally, but no
  homodimerization row was needed for the core function).
