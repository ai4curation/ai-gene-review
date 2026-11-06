# GNG2 (human, P59768) review notes

## Provenance / process

- 2026-10-23: `just fetch-gene human GNG2` already run; `just fetch-gene-pmids human GNG2` cached 13/13 GOA PMIDs.
- Deep research (`just deep-research-falcon human GNG2 --fallback perplexity-lite`) FAILED twice:
  falcon returned "Edison API request failed: Failed to authenticate" and the
  perplexity-lite fallback reported "Provider 'perplexity' not available". No
  deep-research file exists for GNG2; this review relies on the UniProt record and
  the cached publications only.

## Gene product

- 71 aa G protein gamma subunit (G-gamma family, Pfam PF00631, PANTHER PTHR13809).
  Init Met removed, Ala2 N-acetylated; C-terminal CaaX: Cys68 geranylgeranylated and
  carboxymethylated, residues 69-71 removed [file:human/GNG2/GNG2-uniprot.txt
  "S-geranylgeranyl cysteine"; "Removed in mature form"].
- Location: "Cell membrane {ECO:0000305}; Lipid-anchor" cytoplasmic side
  [file:human/GNG2/GNG2-uniprot.txt].
- UniProt FUNCTION: "The beta and gamma chains are required for the GTPase activity,
  for replacement of GDP by GTP, and for G protein-effector interaction"
  [file:human/GNG2/GNG2-uniprot.txt].

## Key evidence

- Gbeta1-gamma2 is the workhorse Gbetagamma used in essentially every GPCR-G protein
  cryo-EM structure: 5-HT1B/mini-Go [PMID:29925951 "assembled into a complex containing
  5-HT1BR, donitriptan, mini-GO, β1 and γ2 subunits"], calcitonin receptor/Gs
  [PMID:28437792 "the CTR was co-expressed with Gαs, His-Gβ1, and Gγ2"], glucagon
  receptor [PMID:32371397], D2 dopamine receptor/Gi [PMID:32528175 "An additional
  pFastBac-Dual baculovirus was made with human Gβ1 and human Gγ2 genes."], 5-HT1A/1D/1E
  [PMID:33762731], 5-HT1F [PMID:34239069]. These support heterotrimeric G-protein complex
  (IDA) and Gbeta binding, but the complexes are reconstituted in insect cells, so they
  say nothing about which Ggamma a given receptor uses in vivo.
- GIRK2-Gbeta1gamma2 crystal structure: Gbetagamma alone activates GIRK
  [PMID:23739333 "these reconstitution experiments show that Gβγ by itself is sufficient
  to activate the GIRK channel."; "The full-length human G protein β1 and γ2 subunits
  were cloned into pFastbac vectors."]. Supports potassium channel activator activity.
- GNB2 R52L (familial sinus node / AV block) enhances GIRK activation when co-expressed
  with Ggamma2 [PMID:28219978 "Gγ2; this was in contrast to coexpression of mutant
  Gβ2-Gγ2 with other cardiac"].
- Gbeta5 can pair with Ggamma2 in HEK293 cells by FRET [PMID:12606627 "observed that
  Gbeta5 could interact with Ggamma2 and Ggamma13, after their"].
- Combinatorial co-IP of all beta/gamma pairs with alpha-i1/alpha-sL: broad promiscuity
  [PMID:25733868 "So far, crystal structures of G proteins have only included the
  combinations β 1 γ 1 or β 1 γ 2 ."].
- Background: Deutsch et al. 2026 smFRET of Galpha-i in muOR-Gi used human Gbeta1 and
  Ggamma2 [PMID:42870023 "we used a single virus containing the genes for both the human
  Gβ1 and Gγ2 subunits"]; WT Gi heterotrimer was Galpha-i1 beta1 gamma2. This is about
  Galpha-i dynamics; GNG2 is a reagent there. Cited only as further illustration that
  Gbeta1gamma2 is the standard Gbetagamma for reconstituted Gi heterotrimers.
- Interactome screens (BioPlex 3.0 [PMID:33961781], OpenCell [PMID:35271311]) find
  GNG2-GNB1; exosome proteome [PMID:20458337].

## Decisions

- protein binding IPI rows: all partners are G beta subunits (GNB1 P62873, GNB2
  P62879) -> MODIFY to GO:0031681 G-protein beta-subunit binding.
- G protein activity (IBA): GO/PAINT convention applies heterotrimer-level G protein
  activity to beta and gamma subunits; Ggamma itself has no nucleotide binding. Accepted
  (the node placement is sound), and in core_functions recorded as
  contributes_to_molecular_function with G-beta binding as subunit MF.
- Plasma membrane (IEA + many Reactome TAS, all location rows): ACCEPT; Reactome rows
  here are only location claims for reactions at the plasma membrane, none are pathway
  process annotations.
- membrane (ISS) -> MODIFY to plasma membrane.
- Ligand-specific ISS processes from bovine GNG2 (dopamine/adenylate cyclase, PGE,
  catecholamine): KEEP_AS_NON_CORE; Gbetagamma is a generic transducer component with no
  ligand specificity.
- NEW: GO:0031680 G-protein beta/gamma-subunit complex (free Gbeta1gamma2 dimer is the
  GIRK-activating species). Comparator: STE18 (yeast), git5 (S. pombe), rat Gng5 carry
  this CC term by IDA, i.e. Ggamma subunits in the same role.
- Taste (bitter/sweet/umami) roles in UniProt rest on cryo-EM reconstitutions with
  Gbeta1gamma2; the physiological gustducin partner is reported to be Gbeta3gamma13 in
  the literature I recall, but no cached source -> not added; raised as a question.
