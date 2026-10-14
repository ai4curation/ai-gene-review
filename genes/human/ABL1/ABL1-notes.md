# ABL1 notes

No notes file existed for this COMPLETE review; this file was created for the
section below. Automated deep research was not run for this section; it is based
on papers retrieved from PubMed, cached with `just fetch-pmid`, and read.

## Premetazoan origin (ORIGINS_OF_MULTICELLULARITY, 2026-10-01)

### Sources read

- PMID:26090675 (Aleem, Craddock and Miller 2015, PLoS One), full text cached.
  The only biochemical characterisation of a premetazoan Abl (MbAbl2, from the
  choanoflagellate *Monosiga brevicollis*). This is the key paper.
- PMID:18621719 (Manning et al. 2008, PNAS), full text cached. The *M. brevicollis*
  tyrosine kinome.
- PMID:22550341 (Suga et al. 2012, Sci Signal), abstract only. The tyrosine kinomes of
  the filastereans *Capsaspora owczarzaki* and *Ministeria vibrans*.
- PMID:18273011 (King et al. 2008, Nature), full text cached. The *M. brevicollis*
  genome paper.
- PMID:27746046 (Sebé-Pedrós et al. 2016, Dev Cell), abstract only. *Capsaspora*
  phosphoproteomics.
- PubMed searches for Abl in choanoflagellates, *Capsaspora*, ichthyosporeans,
  sponges or cnidarians found no other primary study of a non-bilaterian Abl
  ("(Monosiga OR choanoflagellate OR Capsaspora) AND Abl" returned only PMID:26090675).

### Abl family distribution

- Abl is one of four cytoplasmic tyrosine kinase families with clear
  choanoflagellate orthologs
  [PMID:18621719 "the only clearly identifiable specific homologs were of the Src subgroup kinases (Src, Csk, Abl, and Tec)."].
- The cytoplasmic tyrosine kinase repertoire was already in place before
  filastereans split from choanoflagellates and animals
  [PMID:22550341 "we demonstrate that the basic repertoire of metazoan cytoplasmic tyrosine kinases was established before the divergence of filastereans from the Metazoa and Choanoflagellata clades."].
- Abl itself is found in choanoflagellates, filastereans and ichthyosporeans, but
  these unicellular Abls lack the long C-terminal region
  [PMID:26090675 "Abl genes have been identified in the unicellular choanoflagellate M. brevicollis [7–9], as well as in the filastereans C. owczarzaki and M. vibrans [10] and three ichthyosporean species [11]. In each of these premetazoan Abl kinases, the SH3-SH2-kinase domain architecture is preserved, but the large C-terminal portion is absent."].
  *M. brevicollis* has two Abl paralogs, MbAbl1 and MbAbl2
  [PMID:26090675 "The genome of M. brevicollis encodes two putative Abl family kinases (MbAbl1 and MbAbl2), both of which contain the conserved SH3-SH2-kinase domain structure [7]."].
- Background: the choanoflagellate genome has the full phosphotyrosine signalling
  toolkit (kinase, PTP and SH2 domains)
  [PMID:18273011 "These findings support a model in which the full set of pTyr signalling machinery evolved before the separation of the choanoflagellate and metazoan lineages."].

### What MbAbl2 does (in vitro and in mammalian cells)

- Active tyrosine kinase with the Abl substrate preference
  [PMID:26090675 "MbAbl2 exhibited highest activity toward the Abl substrate, lower activity toward the Src and IR peptides, and was inactive against the EGFR and PKA substrates (Fig 2D). Thus, the substrate preference of the Abl catalytic domain appears to have been established early in the evolution of this family."].
- Activation-loop autophosphorylation is conserved
  [PMID:26090675 "These results suggest that autophosphorylation evolved early as a mechanism for Abl kinase regulation."].
- No N-terminal myristoyl/cap autoinhibition, and constitutively active
  [PMID:26090675 "MbAbl2 lacks the N-terminal myristoylation and cap sequences that are critical regulators of mammalian Abl kinase activity, and we show that MbAbl2 is constitutively active."].
  In mouse NIH3T3 cells it phosphorylates many proteins and transforms cells more
  potently than c-Abl; it is poorly inhibited by imatinib, which binds the
  inactive conformation
  [PMID:26090675 "Our data indicate that the conformation of M. brevicollis MbAbl2 resembles that of activated forms of mammalian Abl."].
- No F-actin binding domain
  [PMID:26090675 "The C-terminal portion of MbAbl2 kinase is much smaller than that of metazoan Abl kinases, and the F-actin binding domain is missing (Fig 1A)."].
  The authors conclude that the F-actin- and DNA-binding C-terminus is an animal
  addition
  [PMID:26090675 "Another elaboration during metazoan evolution was the extended C-terminus, containing binding motifs for F-actin and for DNA. Thus, it is clear that additional functionality was appended to Abl kinase as part of the transition to multicellularity."].
- Caveats stated by the authors:
  - The second paralog, MbAbl1, has a possible N-terminal myristoylation glycine and
    has not been tested
    [PMID:26090675 "This kinase is predicted to contain an N-terminal Gly residue that could potentially be myristoylated."].
  - The cellular role of Abl in unicellular holozoans is unknown
    [PMID:26090675 "The normal cellular functions of Abl kinases in premetazoan lineages, however, remain enigmatic."].
  - Substrates of MbAbl2 in *M. brevicollis* were not identified. The transformation
    and phospho-blot data are from mouse cells, so they say nothing about native
    substrates.
- *Capsaspora* phosphoproteomics shows that tyrosine kinases are among the proteins
  whose phosphorylation changes across life stages
  [PMID:27746046 "they affect key genes involved in animal multicellularity, such as transcription factors and tyrosine kinases."].
  Only the abstract was read, and it does not name Abl.

### Core functions of the existing review: ancestral or animal-specific

| Core function (existing review) | Classification | Evidence |
|---|---|---|
| GO:0004715 non-membrane spanning protein tyrosine kinase activity | **Ancestral** (choanoflagellate, filasterean and ichthyosporean Abl present; MbAbl2 shown active with Abl-type substrate preference and autophosphorylation) | PMID:26090675, PMID:18621719, PMID:22550341 |
| Tight autoinhibition (myristoyl/cap clamp; not a GO core function but stated in the description) | **Animal-specific**, at least for MbAbl2; MbAbl1 untested | PMID:26090675 |
| ...directly_involved_in GO:0032956 regulation of actin cytoskeleton organization | **Unresolved**. No unicellular Abl has been tested for an actin role. The direct actin-binding route through the C-terminal domain is absent in all premetazoan Abls, so any ancestral actin role would have to go through substrates | PMID:26090675 |
| ...directly_involved_in GO:0006281 DNA repair | **Unresolved / probably animal-specific**. No data from unicellular holozoans. The DNA-binding C-terminus is absent | PMID:26090675 |
| GO:0051015 actin filament binding | **Animal-specific**. No F-actin binding domain in any premetazoan Abl examined | PMID:26090675 |
| GO:0003677 DNA binding, with DNA damage response and apoptotic process | **Animal-specific** for DNA binding (C-terminal DNA-binding region absent). DNA damage response unresolved. The apoptotic machinery ABL1 feeds into (TP73 and others) is animal; its age was not tested here | PMID:26090675 |
| Locations nucleus, cytosol, cytoskeleton, plasma membrane | **Unresolved**. No localisation data for any unicellular Abl. The ABL1 NLS/NES and myristoyl membrane anchor sit in regions that MbAbl2 lacks; this inference is mine and is not stated in the paper | none |

Summary: the ancestral Abl was an SH3-SH2-kinase module with Abl-type substrate
specificity and activation-loop autophosphorylation. Animals added two things to
it: tight N-terminal autoinhibition, and the long C-terminus with F-actin and DNA
binding. Both of ABL1's best-known cellular roles, direct actin cytoskeleton
remodelling and the nuclear DNA damage response, depend on the animal additions.
No paper tests what Abl does in a unicellular holozoan. The repository's SRC and
CSK reviews reach the same conclusion for Src: the catalytic module is ancestral,
and stringent negative regulation is a later addition (disputed for Csk-Src).
This fits the general model the Miller lab proposes for Src, Abl and Pak.

### Action changes

None. No row's rationale depends on premetazoan evidence. The IBA
`GO:0005886 plasma membrane` row cites myristoylation of isoform IB. MbAbl2 has
no myristoylation site, but that does not bear on whether human ABL1 is at the
plasma membrane.

### Track C: IBA node reach into unicellular holozoans (QuickGO, 2026-10-01)

Query: `annotation/search?withFrom=PANTHER:<PTN>&taxonId=<T>&taxonUsage=descendants`,
T = 28009 Choanoflagellata, 2687318 Filasterea, 127916 Ichthyosporea.

| PTN node (ABL1 IBA terms) | Choanoflagellata | Filasterea | Ichthyosporea |
|---|---|---|---|
| PTN002521457 (GO:0004713 protein tyrosine kinase activity; GO:0005886 plasma membrane) | 105 rows on 59 *M. brevicollis* (taxon 81824) proteins: GO:0004713 IBA x46, GO:0005886 IBA x59 | 0 | 0 |
| PTN002815481 (GO:0007229 integrin-mediated signaling pathway; GO:0010595 positive regulation of endothelial cell migration) | 0 | 0 | 0 |
| PTN008405112 (GO:0007173 epidermal growth factor receptor signaling pathway) | 0 | 0 | 0 |

- No animal tissue, organ or developmental process term from an ABL1 IBA node
  reaches a unicellular holozoan. The endothelial-migration and integrin terms sit on
  PTN002815481, which reaches no choanoflagellate, filasterean or ichthyosporean
  protein.
- PTN002521457 is a broad tyrosine kinase node, not an Abl node. Its MF transfer to
  *M. brevicollis* is consistent with the biochemistry above. Its CC transfer
  (plasma membrane) reaches all 59 proteins. That includes cytoplasmic kinases, and
  for unicellular Abl there is no localisation evidence at all. This is a possible
  localisation over-reach worth flagging in the propagation audit; it is not a
  multicellular process term.
- No *Salpingoeca rosetta*, *Capsaspora* or ichthyosporean protein receives any of
  these IBAs, even though UniProt places *S. rosetta* and *Capsaspora* tyrosine
  kinases in PTHR24418. This probably reflects which proteomes are in the PANTHER
  tree; I did not check that.
