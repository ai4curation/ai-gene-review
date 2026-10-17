# CFAP47 notes

## Deep research status

Automated deep research was attempted and failed, so no `CFAP47-deep-research-*.md`
file exists for this gene:

- `just deep-research human CFAP47 --provider falcon` failed with
  `Exception: Failed to authenticate` (Edison/Falcon JWT authentication error).
- `just deep-research human CFAP47 --provider perplexity` failed with
  `Provider 'perplexity' not available. Available: falcon, asta, openscientist`.

Notes below come from a manual PubMed search (`CFAP47[Title/Abstract]`, 18 hits,
2021-2026) and the cached publications. Every cited PMID was cached with
`just fetch-pmid` / `just fetch-gene-pmids`.

## Identity

- UniProt Q6ZTR5 (CFA47_HUMAN); X-linked (Xp21.1); very large (canonical isoform 5,
  3,187 aa); UniProt annotates a calponin-homology (CH) domain (1746-1869) and InterPro
  Ig-like folds; the mouse structure (PMID:40473901) resolves a chain of numbered ASH
  domains with the CH domain in the "CFAP47-ring". PANTHER PTHR45912. Highly expressed in testis and present in sperm.
- Disease: X-linked spermatogenic failure 3 (SPGFX3, MIM:301059).

## Structure: core of the central-apparatus bridge

- [PMID:40473901 "CFAP47, the core structural component of the bridge, binds C1 through
  its N-terminal domains, interacts with HYDIN via its central CFAP47-ring, and anchors to
  C2 through its C-terminal region."] (in situ cryo-ET of mouse sperm central apparatus,
  full text).
- Knockout: [PMID:40473901 "In the sperm of Cfap47-knockout (KO) mice, a hollow bridge
  region within the CA structure was observed, correlating with abnormal sperm motility
  and confirming the essential role of CFAP47 in CA function."]

## Human genetics

- MMAF: [PMID:33472045 "we conducted whole-exome sequencing (WES) and identified
  hemizygous missense variants in the X-linked CFAP47 in three unrelated Chinese
  individuals with MMAF."]; an Australian man with a whole-gene Xp21.1 deletion; a
  Cfap47-mutated mouse [PMID:33472045 "the adult males of which were sterile and presented
  with reduced sperm motility and abnormal flagellar morphology and movement."] Abstract
  only (PMC7895902 full text not retrievable through PubMed tools).
- Further MMAF/OAT families: PMID:37424856 (p.V472M; head, mitochondrial sheath and
  annulus defects; co-IP with SEPTIN4, CFAP65, CFAP69) and PMID:36571501 (abstract only;
  CFAP47 interacts with WDR87 in the midpiece).
- Airway: [PMID:37723893 "Two hemizygous missense variants of X-linked CFAP47 in two
  unrelated PCD individuals were identified."] Respiratory cilia were short and fewer but
  the 9+2 structure was intact; the PCD association rests on two patients.
- Kidney (weaker): [PMID:39698362 "CFAP47 was expressed in primary cilia of human kidney
  tubules"]; proposed X-linked PKD gene from three sporadic male patients.

## Localization by immunofluorescence

- Two IF studies place a CFAP47 signal at the sperm head-tail junction:
  GOA IDA from PMID:33472045 (head-tail coupling apparatus; abstract only) and
  [PMID:37723893 "Immunofluorescence analysis showed CFAP47 is located to junction of head
  and flagellum in sperm of control but absent in sperm of P1."]
- This contrasts with its structural position along the central apparatus of the whole
  axoneme (PMID:40473901). A neck pool or epitope accessibility could explain the IF.

## Annotation decisions (summary)

- sperm axoneme assembly (IBA, IMP) -> ACCEPT (structural core of CA bridge; KO hollow
  bridge).
- cilium assembly (IBA) -> TOO_GENERAL (entailed by sperm axoneme assembly).
- cilium (IBA) -> TOO_GENERAL, entailed by NEW axonemal central apparatus.
- NEW: axonemal central apparatus (GO:1990716). Comparator check: HYDIN (its bridge
  partner), SPAG16, SPAG17, CFAP65 and MYCBPAP carry GO:1990716 in human GOA.
- protein binding x3 (BioPlex UBB x2; CFAP65) -> REMOVE (uninformative).
- sperm head-tail coupling apparatus (IDA) -> KEEP_AS_NON_CORE.

## Review round 2 (PR 5062 automated review): molecular function and comparator checks

### Molecular function

The first pass removed the three `protein binding` rows and asserted no MF, leaving CFAP47
with no MF aspect. The in situ structure (PMID:40473901, full text) does support specific
activities, so two NEW MF rows were added:

- `GO:0005200 structural constituent of cytoskeleton` (enables; ISS from mouse Cfap47,
  MGI:MGI:3781475), also set as `core_functions.molecular_function`.
  [PMID:40473901 "CFAP47, the core structural component of the bridge, binds C1 through its
  N-terminal domains, interacts with HYDIN via its central CFAP47-ring, and anchors to C2
  through its C-terminal region."] and [PMID:40473901 "Although CFAP47 is not essential for
  CA assembly or for direct interactions with the 9 neighboring RSs, its absence disrupts
  the bridge structure, including the assembly of SPAG6 and GMCL1 (BTBD16), thereby
  weakening the connections between C1 and C2."] This follows the repository precedent for
  CFAP43 (`genes/human/CFAP43/CFAP43-ai-review.yaml`, NEW GO:0005200 enables from a native
  axoneme structure).
- `GO:0008017 microtubule binding` (enables; ISS from mouse Cfap47), a second core function.
  [PMID:40473901 "The ASH1 and ASH4 domains of CFAP47 bind to protofilament-13 and
  protofilament-1 of C1, respectively, reinforcing the C1 seam."] and [PMID:40473901
  "Additionally, the ASH18 domain of CFAP47 binds SPAG16, and its ASH20 domain interacts
  with protofilament-12 of the C2 microtubule"].
- Evidence code: the structure is of mouse sperm, so ISS with the mouse ortholog as the
  WITH/FROM entity, not IDA (CFAP43 was IDA because its structure was a native human
  axoneme). MGI:MGI:3781475 was confirmed as mouse Cfap47 (UniProt query
  `gene_exact:Cfap47 AND organism_id:10090` returns A0A0G2JEB6 with MGI:3781475, run
  2026-10-16) and is the MGI id already in the CFAP47 GOA WITH/FROM for the IBA rows.
- The NEW `GO:1990716 axonemal central apparatus` row now has `qualifier: part_of` and
  `supporting_entities: MGI:MGI:3781475`.

### Comparator checks (QuickGO annotation search, run 2026-10-16)

Query: `https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:<acc>&goId=<term>&goUsage=exact`.

- GO:1990716 axonemal central apparatus, human: HYDIN (Q4G0P3) ISS + IEA; SPAG16 (Q8N0X2)
  IBA + IEA; SPAG17 (Q6Q759) IBA + IEA; CFAP65 (Q6ZU64) ISS + IEA; MYCBPAP (Q8TBZ2) ISS.
  The claim in the review holds. CFAP47 (Q6ZTR5) itself has none.
- MF on central-apparatus proteins (`aspect=molecular_function`, excluding GO:0005515):
  HYDIN, SPAG6, SPAG16, SPAG17, SPEF2, CFAP46, CFAP54, CFAP74 carry no MF; CFAP65 only
  GO:0003723 (HDA); MYCBPAP only GO:0005543 and GO:0030276 (IBA). CFAP43 itself has no
  GO:0005200 in GOA yet (the precedent is a NEW proposal in this repository). So GOA has
  no convention for or against an MF on central-apparatus scaffolds; the absence reflects
  missing structural curation.
- GO:0008017 microtubule binding, human (`goId=GO:0008017&taxonId=9606`, all pages):
  axonemal/ciliary proteins carrying it include SPEF1 (IBA, ISS), CFAP144 (IDA), CFAP100
  (IMP), CFAP157 (IBA, IEA, ISS), SAXO1 (IBA, IDA, IEA), SAXO2 and SAXO6, DRC4 (IEA).
- GO:0005200 structural constituent of cytoskeleton, human: mainly tubulins, spectrins,
  ankyrins, talins; the only sperm-specific carriers are CYLC1/CYLC2 (calyx). No axonemal
  protein carries it in GOA.

### CFAP65 protein-binding row

Its own source (PMID:33472045) is abstract-only here and the abstract does not describe
the interaction; the reason now says so, and distinguishes this targeted assay from the
two BioPlex AP-MS rows. The quote is from the independent co-IP study PMID:37424856.
