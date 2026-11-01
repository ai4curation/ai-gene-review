# Blm (mus309, CG6920; UniProt Q9VGI8) - manual literature synthesis

No deep-research API was available for this review. This synthesis was compiled
by hand from the publications cached in `publications/` and PubMed searches.

## Identity and family

- Blm encodes a 1487-aa RecQ-family DNA helicase, the Drosophila ortholog of
  human BLM and yeast Sgs1 [PMID:10049920 "Dmblm is most closely related to the Homo sapiens BLM gene"].
- Dmblm cDNA partially complements the MMS sensitivity of yeast sgs1 mutants
  [PMID:10049920 "Dmblm cDNA partially rescued the sensitivity to methyl methanesulfonate"].
- Dmblm is allelic to the mutagen-sensitivity locus mus309 [PMID:11283371 "We show that Dmblm is identical to mus309"].
  An earlier paper had assigned mus309 to the Ku70/IRBP gene [PMID:8608940
  "mus3O9, contains a mutation in IRBP"]; the 2001 paper corrected the
  assignment, so phenotypes of mus309 alleles in PMID:8608940 are Blm phenotypes.
- Domain content (UniProt Q9VGI8): DEAD/DEAH helicase ATP-binding domain,
  helicase C-terminal domain, RecQ zinc-binding (RQC) domain, HRDC domain,
  large disordered N-terminus. Belongs to the helicase family, RecQ subfamily.

## Biochemistry

- Purified DmBLM (from S2 cell nuclear extracts) is a DNA-dependent ATPase with
  3'->5' helicase activity, prefers forked substrates and anneals complementary
  strands [PMID:17272294 "is a DNA-dependent ATPase, has 3'-->5'
  DNA helicase activity, prefers forked substrate DNAs and anneals complementary
  DNAs"]. It couples displacement and annealing (strand swapping).
- With Topo IIIalpha and RPA, Blm dissolves a mobile double Holliday junction to
  non-crossover products by convergent branch migration [PMID:16849422
  "Drosophila topoisomerase IIIalpha (Topo IIIalpha) and Blm (a homolog of Sgs1) are capable of resolving this substrate to non-cross-over products"].
- The Top3alpha C-terminus interacts directly with Blm, possibly compensating for
  absence of an Rmi1 in Drosophila [PMID:22511792 "This insert
  contributes an independent interaction with Blm"].
- The N-terminus of BLM orthologs, including Drosophila, has ssDNA annealing and
  strand-exchange activity [PMID:20389284 "These activities are conserved in the human and Drosophila orthologs"].

## Genetics / in vivo roles

- SDSA: Blm mutants are impaired in repair synthesis during gap repair and
  repair via error-prone deletion-forming pathways [PMID:12522255]; deletions
  depend on Rad51/strand invasion, supporting D-loop unwinding by Blm
  [PMID:15501916 "DmBlm acts downstream of strand invasion to unwind
  a D-loop intermediate"]. HELQ/FANCM act earlier, BLM processes
  intermediates [PMID:35328029].
- dHJ dissolution / anti-crossover: Blm mutants show 40-50-fold more crossing
  over during premeiotic DSB repair and template disruptions consistent with
  failed dHJ dissolution [PMID:17075047]; spontaneous mitotic crossovers
  increase by orders of magnitude [PMID:17507683].
- Synthetic lethality with the three HJ resolvases MUS81-MMS4, MUS312-SLX1 and
  GEN [PMID:22022278 "loss of DmBLM and GEN leads to lethality early in
  development"; PMID:25205745].
- Suppresses homeologous single-strand annealing [PMID:18978019 "the suppression of homeologous SSA depends on the Bloom helicase (Blm)"].
- Suppresses Lig4-independent alternative end joining during aging; blm mutants
  have reduced lifespan and increased tumorigenesis [PMID:22183041].
- NHEJ: RNAi interactions with Ku [PMID:15184650]; interpretation is that Blm
  influences break processing, not that it is an NHEJ factor.
- Meiosis: mus309 N-terminal alleles reduce crossovers to ~half and alter
  their distribution [PMID:17507683]; a hypomorph increased intergenic
  crossovers in some X intervals [PMID:16454858].
- Early embryo: maternal Blm required for syncytial cycles; anaphase bridges
  [PMID:17507683].
- Human BLM rescues DmBlm mutant female IR sensitivity [PMID:31772289].

## Localization

- Nuclear (protein purified from nuclear extract, PMID:17272294). In
  PMID:31772289 the nuclear localization imaged in S2 cells is of transfected
  human BLM (and human RECQL), not of DmBlm.
