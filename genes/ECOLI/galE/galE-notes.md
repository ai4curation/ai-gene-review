# galE (P09147, GALE_ECOLI) notes

## Deep research status

- 2026-10-23: `just deep-research ECOLI galE --provider perplexity` was attempted once
  and failed (`Provider 'perplexity' not available. Available: falcon, openscientist`).
  No deep-research file was generated; this review is based on the cached
  publications, additional PMIDs fetched with `just fetch-pmid`, and the UniProt record.

## Identity

- E. coli K-12 galE (b0759, JW0742; synonym galD), first gene of the galETKM operon.
  UDP-glucose 4-epimerase / UDP-galactose 4-epimerase, EC 5.1.3.2, 338 aa.
- Family: NAD(P)-dependent epimerase/dehydratase (SDR extended) family; InterPro
  IPR005886 UDP_G4E, NCBIfam TIGR01179 galE, PANTHER PTHR43725:SF47
  [file:ECOLI/galE/galE-uniprot.txt "Belongs to the NAD(P)-dependent epimerase/dehydratase
  family."].

## Molecular function

- Reversible interconversion of UDP-glucose and UDP-galactose; curated UniProt
  function [file:ECOLI/galE/galE-uniprot.txt "Catalyzes the conversion of UDP-galactose
  (UDP-Gal) to UDP-glucose (UDP-Glc) through a mechanism involving the transient reduction
  of NAD. It is only active on UDP-galactose and UDP-glucose."] (evidence PMID:14235524).
- Kinetics (UniProt, from PMID:14235524, PMID:8241178, PMID:9271498): KM 160 uM UDP-Gal,
  225 uM UDP-Glc, kcat 760 s-1 for UDP-Glc.
- Tightly bound NAD+ is the redox cofactor [PMID:8652544 "UDP-galactose 4-epimerase from
  Escherichia coli contains tightly bound NAD+, which participates in catalyzing the
  interconversion of UDP-galactose and UDP-glucose through its redox properties."];
  two NAD+ per dimer [PMID:8652544 "there are two molecules of NAD+ per dimer"].
- Mechanism: transient oxidation at C4 to a UDP-4-ketopyranose with nonstereospecific
  hydride return; Tyr149 base, Ser124 and Lys153 [PMID:23339688 "Early studies revealed
  that uridine(5')diphospho(1)α-D-4-ketopyranose (UDP-4-ketopyranose) and NADH are
  reaction intermediates."]; [PMID:8241178 "Mutation of this residue to methionine or
  alanine decreases the catalytic activity of the enzyme by a factor of more than 10(3)."].
- Structure: homodimer, Rossmann NAD domain (1-180) and C-terminal substrate domain
  [PMID:1579570 "As isolated from E. coli, the molecule is a dimer of chemically
  identical subunits with a total molecular weight of 79,000."]; abortive NADH/UDP-Glc
  complex at 1.8 A [PMID:8611497].
- Y299C mutant gains UDP-GlcNAc 4-epimerase activity (UniProt, PMID:12019271), i.e. the
  wild-type enzyme is specific for UDP-Glc/UDP-Gal.

## Biological roles

- Leloir pathway: galE is one of the three gal cistrons required for galactose
  utilization [PMID:13914787 "The functions pertaining to the three genetically defined
  cistrons were found to relate, respectively, to the expression of galactokinase,
  galactose 1-phosphate uridyl transferase, and uridine diphosphate galactose
  4-epimerase."]. galE mutants are galactose-sensitive (PMID:7025059, title only).
- De novo UDP-galactose supply: when cells grow on non-galactose carbon sources GalE is
  the route from UDP-glucose to UDP-galactose [PMID:23339688 "All healthy cells produce
  UDP-gal from uridine(5')diphospho(1)α-D-glucose (UDP-glc) by the action of
  UDP-galactose 4-epimerase (GalE)."]. UDP-galactose feeds galactosylated surface
  glycans (LPS core/O antigen, colanic acid). In O157:H7, gal genes are needed for O
  antigen [PMID:17158899 "The GalE, GalT, GalK, and GalU proteins are necessary for
  modifying galactose before it can be assembled into the repeating subunit of the O
  antigen."]. These are downstream consumer pathways; GalE only provides the
  nucleotide sugar.
- Colanic acid annotations (PMID:14124321, PMID:14060648) have no abstract in cache;
  kept as non-core upstream precursor supply.
- galE mutants, unlike galU mutants, do not alter sigma S-dependent gene expression
  [PMID:7814331 "Mutants deficient in UDP-galactose epimerase (galE mutants) and
  trehalose-6-phosphate synthase (otsA mutants) do not exhibit such an effect on gene
  expression"].

## Location

- Soluble cytosolic enzyme (cytosol proteomics PMID:18304323, PMID:15911532,
  PMID:16858726).

## Review decisions summary

- Core MF GO:0003978 accepted (IBA, IDA, IEA). GO:0016857 (parent) -> MODIFY to GO:0003978.
- Process: Leloir pathway GO:0033499 accepted; general carbohydrate/monosaccharide/galactose
  metabolic process rows -> MODIFY to GO:0033499. NEW GO:0052574 UDP-galactose
  biosynthetic process (GalE catalyses the forming step itself).
- identical protein binding -> MODIFY to GO:0042803 protein homodimerization activity.
- Bare protein binding (Y2H with YjjW) -> REMOVE per protein-binding policy.
- cytoplasm -> MODIFY to cytosol.
