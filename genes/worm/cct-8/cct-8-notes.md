# cct-8 (C. elegans) — research notes

Gene: `cct-8` / ORF `Y55F3AR.3` / WormBase `WBGene00021934`
UniProt: `Q9N358` (TCPQ_CAEEL), "T-complex protein 1 subunit theta" (CCT-theta / TCP-1-theta), 548 aa.
NCBI taxon: 6239.

This is a research journal. Provenance is recorded inline as `[PMID:xxxx "verbatim quote"]`
or `[file:... "quote"]`. KNOWN vs NOT-KNOWN are separated at the end.

## Identity and family

cct-8 encodes the theta (θ) subunit of the eukaryotic cytosolic chaperonin CCT
(chaperonin-containing TCP-1), also called TRiC (TCP-1 ring complex). UniProt:
"Belongs to the TCP-1 chaperonin family." InterPro domains identify it specifically as the
theta paralog: `IPR012721 Chap_CCT_theta`, plus the pan-family `IPR017998 Chaperone_TCP-1`,
`IPR002194 Chaperonin_TCP-1_CS`, and the Cpn60/GroEL/TCP-1 fold (`IPR002423`). PANTHER family
PTHR11353 (CHAPERONIN). NCBIfam TIGR02346 `chap_CCT_theta` and CDD `cd03341 TCP1_theta` are
theta-subunit-specific, so the subunit assignment is unambiguous.

CCT/TRiC is a ~1 MDa double-ring machine; each ring is a hetero-octamer of eight distinct but
paralogous subunits (CCT1–CCT8 / alpha–theta), arranged in a fixed order. In C. elegans the
eight paralogs are cct-1..cct-8. The assembled complex, not any single subunit, is the folding
machine. [PMID:15704212 "Eukaryotic chaperonins, the Cct complexes, are assembled into two
rings, each of which is composed of a stoichiometric array of eight different subunits, which
are denoted Cct1p-Cct8p."]

## Molecular function / mechanism (general CCT/TRiC, well conserved)

CCT/TRiC is an ATP-dependent foldase. Each subunit is a member of the group II chaperonin
(GroEL/Cpn60-like) fold with an equatorial ATP-binding/hydrolysis domain, an intermediate
domain, and a substrate-binding apical domain. ATP binding and hydrolysis by the subunits drives
the folding cycle. [PMID:16762366 "The eukaryotic cytosolic chaperonin CCT is an essential
ATP-dependent protein folding machine whose action is required for folding the cytoskeletal
proteins actin and tubulin, and a small number of other substrates, including members of the
WD40-propellor repeat-containing protein family."]

The complex acts as a genuine catalyst of folding. [PMID:16762366 "Yeast CCT catalyses the
folding of yeast ACT1p and human beta-actin with nearly identical rate constants and yields."]

The eight subunits are functionally non-equivalent — they have distinct substrate contacts and
distinct roles despite the shared fold. [PMID:15704212 "These results provide evidence for
functional differences among Cct subunits and for physiological properties of unassembled
subunits."] The conserved equatorial ATP-binding motif is required for the subunit-specific
activities. [PMID:15704212 "the cct6-24 mutation, containing GDGTT --> AAAAA replacements of the
conserved ATP-binding motif, was unable to suppress any of these traits"]

The GOA molecular-function annotations (ATP binding GO:0005524, ATP hydrolysis GO:0016887,
ATP-dependent protein folding chaperone GO:0140662) are all consistent with this conserved
mechanism and with the InterPro/PANTHER family assignment.

## C. elegans–specific biology

UniProt curates a worm-specific in-vivo role from a genome-wide RNAi screen: cct-8 is required
for correct localization of the germ-granule (P-granule) protein PGL-1.
[file:worm/cct-8/cct-8-uniprot.txt "Required for correct subcellular localization of pgl-1."]
Disruption phenotype: [file:worm/cct-8/cct-8-uniprot.txt "Low and diffuse subcellular
localization of pgl-1 in embryos rather than confined to granules in somatic cells."] The source
is the Updike & Strome genome-wide RNAi screen for P-granule genes; cct-8 was among 173 hits.
[PMID:19805813 "we report on a genomewide RNAi screen in C. elegans, which identified 173 genes
that affect the stability, localization, and function of P granules"] NOTE: the cached
PMID:19805813 record is abstract-only (`full_text_available: false`); the abstract does not name
cct-8 or pgl-1, so the specific pgl-1 phenotype is taken from the UniProt curation (which read
the full text), not quoted from the abstract.

The pgl-1 phenotype is most parsimoniously explained by cct-8's canonical chaperonin role: PGL-1
condensation into P granules likely depends on CCT/TRiC-assisted folding of PGL-1 itself or of a
partner. Whether PGL-1 (or actin, which scaffolds germ granules) is the direct CCT substrate has
not been established.

Protein-level evidence: the mature protein was directly sequenced by Edman/MS (UniProt
"Direct protein sequencing" keyword; PE:1 evidence at protein level), confirming expression.

Subcellular location: cytoplasm (UniProt SUBCELLULAR LOCATION "Cytoplasm"; by similarity to
human CCT-theta P50990). Consistent with the cytosolic role of CCT/TRiC. GOA has GO:0005737
cytoplasm (IEA). The more precise term would be cytosol (GO:0005829), but cytoplasm is not wrong.

## Existing GOA annotations (7) — all IBA or IEA, none experimental

1. GO:0006457 protein folding — IBA (GO_REF:0000033, involved_in) — core, ACCEPT
2. GO:0005832 chaperonin-containing T-complex — IBA (GO_REF:0000033, part_of) — core, ACCEPT
3. GO:0005524 ATP binding — IEA (GO_REF:0000002, enables) — ACCEPT
4. GO:0005737 cytoplasm — IEA (GO_REF:0000120, located_in) — ACCEPT (cytosol more precise)
5. GO:0006457 protein folding — IEA (GO_REF:0000002, involved_in) — duplicate of #1, ACCEPT
6. GO:0016887 ATP hydrolysis activity — IEA (GO_REF:0000002, enables) — ACCEPT
7. GO:0140662 ATP-dependent protein folding chaperone — IEA (GO_REF:0000002, enables) — best MF, ACCEPT

There is no `unfolded protein binding` (GO:0051082) annotation in the C. elegans GOA (unlike the
yeast/human orthologs), so no MODIFY is needed for that term here.

## KNOWN

- cct-8 is the theta subunit of the C. elegans cytosolic chaperonin CCT/TRiC (family assignment
  from InterPro/PANTHER/orthology; unambiguous theta-specific signatures).
- CCT/TRiC is an ATP-dependent foldase for actin, tubulin, and a subset of other cytosolic
  substrates (conserved; [PMID:16762366]).
- The eight CCT subunits are functionally non-equivalent ([PMID:15704212]).
- cct-8 is required for correct P-granule (pgl-1) localization in the C. elegans germline/embryo
  ([PMID:19805813] full text via UniProt curation).
- Cytoplasmic localization.

## Update after falcon deep research (2026-07-03)

Deep research (`cct-8-deep-research-falcon.md`, Edison, 32 citations) surfaced two key
C. elegans functional papers and subunit-level structural detail:

- **Noormohammadi et al. 2016, Nat Commun** [PMID:27892468]: cct-8/CCT8 is rate-limiting for
  TRiC/CCT assembly and its somatic increase boosts proteostasis and longevity.
  [PMID:27892468 "ectopic expression of a single subunit (CCT8) is sufficient to increase
  TRiC/CCT assembly"]; [PMID:27892468 "increased expression of CCT8 in somatic tissues extends
  Caenorhabditis elegans lifespan in a TRiC/CCT-dependent manner"]; [PMID:27892468 "increased
  TRiC/CCT complex is required to avoid aggregation of mutant Huntingtin protein"]; [PMID:27892468
  "ameliorates the age-associated demise of proteostasis and corrects proteostatic deficiencies
  in worm models"]. cct-8 is required for lifespan extension in daf-2, eat-2, and glp-1
  long-lived backgrounds (from the paper's body / deep-research synthesis), and its protective
  effect can be partly HSF-1-independent.

- **Calculli et al. 2021, Sci Adv** [PMID:34172445]: cct-8 acts cell-autonomously in neurons to
  prevent polyglutamine aggregation. [PMID:34172445 "knockdown of cct-8 promotes neuronal polyQ67
  aggregation"].

- **Subunit-specific properties** (from CCT/TRiC structural reviews via deep research): the theta
  subunit is a LOW-ATPase subunit (the "CCT6 hemisphere": CCT1/3/6/8), retains bound ADP, and
  contributes to substrate binding, allostery, and complex assembly rather than bulk ATP
  consumption. [file:worm/cct-8/cct-8-deep-research-falcon.md "CCT-8 occupies a defined position
  in the low-ATPase hemisphere and plays a specialized role in substrate binding, allosteric
  regulation, and complex assembly"]; [file:worm/cct-8/cct-8-deep-research-falcon.md "Both actin
  and tubulin make specific contacts with CCT-8-containing apical domains during folding"].

Impact on the review:
- Core-function `molecular_function` set to GO:0005524 (ATP binding) rather than ATP hydrolysis,
  because theta is a low-ATPase subunit; `contributes_to_molecular_function` = GO:0140662.
- GO:0016887 (ATP hydrolysis) existing annotation kept as ACCEPT (family-level InterPro; theta
  retains the catalytic P-loop/aspartate) with the low-ATPase nuance recorded.
- Knowledge gap #1 reframed: theta substrate contacts ARE structurally characterized, so the gap
  is now primarily the ONTOLOGY gap (no MF term for a chaperonin substrate-binding subunit) plus
  the residual BIOLOGY gap of the native worm client set.

## NOT KNOWN (candidate knowledge gaps)

- The subunit-specific substrate contacts / client repertoire of the theta subunit in
  C. elegans (or generally) are not defined. Which clients depend on the theta apical domain
  specifically is unknown.
- Whether PGL-1 is a direct CCT/TRiC substrate, or whether the pgl-1 mislocalization is an
  indirect consequence of impaired actin/tubulin folding, is undetermined.
- No dedicated GO molecular-function term expresses "structural/catalytic subunit of the CCT
  chaperonin" — the individual subunit's function is only expressible as the complex-level
  foldase activity (ontology gap).
- Non-canonical / moonlighting roles of free (unassembled) cct-8, if any, are unexplored in
  C. elegans (functional roles of unassembled Cct subunits are documented in yeast,
  [PMID:15704212]).
</content>
